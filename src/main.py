import os
import json
from datetime import datetime

# Import custom modules
from config import get_config, check_config
from ai_analyzer import analyze_logs


def main():
    """
    Main program - Simple and straightforward approach.
    """
    print("Wowza Log Analyzer - Complete Analysis")

    # Check configuration
    print("\nChecking configuration...")
    if not check_config():
        return
    
    config = get_config()
    
    # Run complete analysis (all prompts)
    print("\nStarting complete analysis...")
    print("Running all prompts (simple + detailed)...")
    
    results = analyze_logs(config['logs_folder'])
    
    if not results:
        print("ERROR: Analysis failed!")
        return
    
    # Save results
    print("\nSaving results...")
    save_results(results, config['results_folder'])
    
    # Display summary
    print("\nAnalysis Summary:")
    show_summary(results)
    
    print("\nCompleted! Check 'results' folder for details.")


def save_results(results, results_folder):
    """
    Save results to JSON file.
    
    Args:
        results (dict): Analysis results
        results_folder (str): Directory to save results
    """
    os.makedirs(results_folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"wowza_analysis_complete_{timestamp}.json"
    filepath = os.path.join(results_folder, filename)
    
    final_data = {
        "timestamp": datetime.now().isoformat(),
        "mode": "complete",
        "results": results
    }
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(final_data, f, indent=4, ensure_ascii=False, sort_keys=True)
        print(f"  Saved: {filename}")
        print(f"  Location: {filepath}")
    except (IOError, OSError) as e:
        print(f"  ERROR saving file: {e}")


def show_summary(results):
    """
    Display simple summary of analysis results.
    
    Args:
        results (dict): Analysis results
    """
    print("  Analysis completed successfully!")
    
    # Count successful analyses
    success_count = 0
    total_count = 0
    
    # Check if it's detailed analysis results
    if "analysis_results" in results:
        analyses = results["analysis_results"]
        total_count = len(analyses)
        success_count = sum(1 for a in analyses.values() if a.get("status") == "success")
        
        # Display token usage
        total_tokens = sum(a.get("tokens_used", 0) for a in analyses.values() if a.get("tokens_used"))
        if total_tokens > 0:
            print(f"  Total tokens used: {total_tokens}")
    else:
        # Simple analysis results
        analyses = [k for k in results.keys() if not k.startswith("error")]
        success_count = len(analyses)
        total_count = success_count
    
    print(f"  Successful analyses: {success_count}/{total_count}")
    print("  All results saved to JSON file")


if __name__ == "__main__":
    main()
