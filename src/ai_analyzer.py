import json
import openai
import time
import logging
from pathlib import Path
from prompts import WowzaAnalysisPrompts
from config import get_config


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('wowza_analysis.log'),
        logging.StreamHandler()
    ]
)

def read_log_files(log_dir: Path) -> str:
    """
    Read all .log and .txt files in the specified directory and its subdirectories.
    Return the combined content as a string.
    """
    contents = []
    for ext in ("*.log", "*.txt"):
        for file in log_dir.rglob(ext):
            contents.append(file.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(contents)

def calculate_cost(prompt_tokens, completion_tokens, model):
    """
    Calculate cost based on token usage.
    
    Args:
        prompt_tokens (int): Number of input tokens
        completion_tokens (int): Number of output tokens
        model (str): Model name
        
    Returns:
        dict: Cost breakdown information
    """
    # OpenAI pricing (USD per 1M tokens)
    pricing = {
        "gpt-4o-mini": {
            "input": 0.15,     # $0.15 per 1M input tokens
            "output": 0.60     # $0.60 per 1M output tokens
        },
        "gpt-4o": {
            "input": 2.50,    # $2.50 per 1M input tokens
            "output": 10.00   # $10.00 per 1M output tokens
        },
        "gpt-5": {
            "input": 1.25,    # $1.25 per 1M input tokens
            "output": 10.00   # $10.00 per 1M output tokens
        }
    }
    
    # Use model from config, fallback to gpt-4o-mini (cheapest)
    model_key = model if model in pricing else "gpt-4o-mini"
    
    # Calculate cost based on 1M tokens
    input_cost = (prompt_tokens / 1_000_000) * pricing[model_key]["input"]
    output_cost = (completion_tokens / 1_000_000) * pricing[model_key]["output"]
    total_cost = input_cost + output_cost
    
    return {
        "model_used": model,
        "pricing_per_1m_tokens": pricing[model_key],
        "input_cost_usd": round(input_cost, 6),
        "output_cost_usd": round(output_cost, 6),
        "total_cost_usd": round(total_cost, 6)
    }

def analyze_logs(logs_folder):
    """
    Read log files and analyze with OpenAI using ALL prompts (simple + detailed).
    
    Args:
        logs_folder (str): Path to directory containing log files
        
    Returns:
        dict: Analysis results with cost breakdown
    """
    print("Reading log files...")
    
    # Use simple function to read logs
    log_dir = Path(logs_folder)
    all_logs_content = read_log_files(log_dir)
    
    if not all_logs_content:
        print("ERROR: No log files found!")
        return None
    
    print(f"SUMMARY: Read log files ({len(all_logs_content)} characters)")
    
    # Get ALL prompts (both simple and detailed)
    detailed_prompts = WowzaAnalysisPrompts.get_all_prompts()
    simple_prompts = WowzaAnalysisPrompts.get_simple_prompts()
    
    # Combine all prompts
    all_prompts = {**simple_prompts}
    
    print(f"\nStarting complete OpenAI analysis ({len(all_prompts)} prompts)...")
    
    # Analyze with each prompt
    results = {}
    
    for prompt_name, prompt_text in all_prompts.items():
        print(f"  Processing: {prompt_name}")
        
        # Create complete prompt
        full_prompt = f"""{prompt_text}

WOWZA LOG DATA:
{all_logs_content}

Please analyze and return JSON results according to the format requested above.
Provide clear and detailed analysis.
"""
        
        # Send to OpenAI
        try:
            config = get_config()
            client = openai.OpenAI(api_key=config['api_key'])
            
            # Measure latency
            start_time = time.time()
            
            # Log request
            logging.info("Starting analysis: %s with model %s", prompt_name, config['model'])
            
            # Use Responses API
            response = client.responses.create(
                model=config['model'],
                input=full_prompt,
                temperature=0.1
            )
            
            # Calculate latency
            end_time = time.time()
            latency = round(end_time - start_time, 2)
            
            answer = response.output_text
            
            # Format answer for better readability in JSON
            formatted_answer = answer.strip()
            # Try to parse as JSON and reformat if possible
            try:
                parsed_json = json.loads(formatted_answer)
                formatted_answer = json.dumps(parsed_json, indent=2, ensure_ascii=False)
            except (json.JSONDecodeError, ValueError):
                # If not valid JSON, just clean up the text
                formatted_answer = formatted_answer.replace('\\n', '\n').replace('\\t', '\t')
            
            # Get token usage information from Responses API
            usage = getattr(response, "usage")
            prompt_tokens = getattr(usage, "input_tokens")
            completion_tokens = getattr(usage, "output_tokens")
            total_tokens = getattr(usage, "total_tokens")

            # Calculate cost for this request
            request_cost = calculate_cost(prompt_tokens, completion_tokens, config['model'])
            
            results[prompt_name] = {
                "status": "success",
                "answer": formatted_answer,
                "token_usage": {
                    "prompt_tokens": prompt_tokens,
                    "completion_tokens": completion_tokens,
                    "total_tokens": total_tokens
                },
                "latency_seconds": latency,
                "cost_breakdown": request_cost,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Log success
            logging.info("SUCCESS: %s - %ss - %s tokens - $%s", prompt_name, latency, total_tokens, request_cost['total_cost_usd'])
            print(f"  Completed: {prompt_name} (Input: {prompt_tokens}, Output: {completion_tokens}, Total: {total_tokens} tokens, {latency}s, ${request_cost['total_cost_usd']})")
            
        except (openai.OpenAIError, ConnectionError, TimeoutError) as e:
            # Calculate latency for error
            end_time = time.time()
            latency = round(end_time - start_time, 2) if 'start_time' in locals() else 0
            
            results[prompt_name] = {
                "status": "error",
                "error": str(e),
                "answer": None,
                "latency_seconds": latency,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Log failure
            logging.error("FAILED: %s - %ss - Error: %s", prompt_name, latency, str(e))
            print(f"  ERROR: {prompt_name} - {e} ({latency}s)")
    
    # Add summary information
    # Calculate total tokens and cost
    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_tokens = 0
    
    for result in results.values():
        if result.get("status") == "success" and "token_usage" in result:
            usage = result["token_usage"]
            total_prompt_tokens += usage.get("prompt_tokens", 0)
            total_completion_tokens += usage.get("completion_tokens", 0)
            total_tokens += usage.get("total_tokens", 0)
    
    # Calculate pricing
    config = get_config()
    cost_info = calculate_cost(total_prompt_tokens, total_completion_tokens, config['model'])
    
    final_results = {
        "analysis_mode": "complete",
        "logs_info": {
            "total_characters": len(all_logs_content)
        },
        "token_summary": {
            "total_prompt_tokens": total_prompt_tokens,
            "total_completion_tokens": total_completion_tokens,
            "total_tokens": total_tokens,
            "cost_breakdown": cost_info
        },
        "analysis_results": results
    }
    
    # Display summary
    print("\nCost Summary:")
    print(f"  Model: {cost_info.get('model_used', 'Unknown')}")
    print(f"  Input tokens: {total_prompt_tokens:,}")
    print(f"  Output tokens: {total_completion_tokens:,}")
    print(f"  Total tokens: {total_tokens:,}")
    print(f"  Cost USD: ${cost_info['total_cost_usd']}")
    
    # Log summary
    logging.info("Total analysis completed - Model: %s - Tokens: %s - Cost: $%s", cost_info.get('model_used'), f"{total_tokens:,}", cost_info['total_cost_usd'])
    
    return final_results
