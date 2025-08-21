# 🚀 AI-Powered Analysis Tool

AI-powered analysis tool using OpenAI - Automatically analyzes errors and provides detailed solutions.

## 📁 Project Structure

```
📦 Research/
├── 📁 .vscode/
│   └── launch.json          # VS Code debug configuration
├── 📁 src/                  # Main source code
│   ├── main.py             # Entry point - run the program
│   ├── ai_analyzer.py      # OpenAI analysis
│   ├── prompts.py          # Analysis prompts
│   ├── config.py           # Configuration management
├── 📁 logs/                # Place Wowza log files here
├── 📁 results/             # Analysis results (JSON files)
├── .env                    # Environment variables (API keys)
├── .env.example           # Template for .env file
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
└── README.md             # This guide
```

## 🎯 Key Features

- ✅ **Automated Analysis**: Runs ALL prompts (simple + detailed)
- ✅ **4 prompts analysis**: 3 simple + 1 detailed prompts
- ✅ **Cost tracking**: Calculate OpenAI API costs
- ✅ **JSON output**: Beautifully formatted, easy to read results
- ✅ **Error handling**: Comprehensive error handling and detailed logging
- ✅ **Debug support**: VS Code debug configuration ready

## 📋 System Requirements

- **Python**: 3.7+ (recommended 3.11+)
- **OpenAI API Key**: Requires OpenAI account
- **VS Code**: (optional) for debugging and development
- **Log files**: Wowza log files (.log, .txt)

## 🛠️ Step-by-Step Installation

### Step 1: Clone/Download Project
```bash
# If you have git
git clone <https://github.com/vuphanden/research.git>
cd Research

# Or download and extract ZIP
```

### Step 2: Install Python Dependencies
```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install manually
pip install openai>=1.0.0 python-dotenv>=1.0.0
```

### Step 3: Setup Environment Variables
1. **Copy template file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit .env file:**
   ```bash
   OPENAI_API_KEY=sk-your-actual-api-key-here
   OPENAI_MODEL=gpt-4o-mini
   OPENAI_TIMEOUT=60
   ```

3. **Get OpenAI API Key:**
   - Visit: https://platform.openai.com/api-keys
   - Create new API key
   - Copy and paste into .env file

### Step 4: Prepare Log Files
```bash
# Create logs directory (if not exists)
mkdir logs

# Copy Wowza log files here
# Supports: .log, .txt files
cp /path/to/your/wowza.log logs/
```

## 🚀 How to Use

### Run basic analysis:
```bash
cd /path/to/project
python src/main.py
```

### Debug with VS Code:
1. Open project in VS Code
2. Press `F5` or `Ctrl+F5`
3. Select "Run Main" configuration

### Expected output:
```
Wowza Log Analyzer - Complete Analysis
======================================

Checking configuration...
✓ Configuration valid

Reading log files...
SUMMARY: Read log files (15,234 characters)

Starting complete OpenAI analysis (4 prompts)...
  Processing: main_errors
  Completed: main_errors (Input: 1,205, Output: 342, Total: 1,547 tokens, 2.3s, $0.000234)
  Processing: root_causes
  Completed: root_causes (Input: 1,205, Output: 298, Total: 1,503 tokens, 1.8s, $0.000187)
  Processing: solutions
  Completed: solutions (Input: 1,205, Output: 445, Total: 1,650 tokens, 2.1s, $0.000278)
  Processing: error_classification
  Completed: error_classification (Input: 1,205, Output: 523, Total: 1,728 tokens, 2.7s, $0.000345)

Saving results...
  Saved: wowza_analysis_complete_20250822_143022.json
  Location: C:\Project\results\wowza_analysis_complete_20250822_143022.json

Analysis Summary:
  Analysis completed successfully!
  Successful analyses: 4/4
  Total tokens used: 6,428

Cost Summary:
  Model: gpt-4o-mini
  Input tokens: 4,820
  Output tokens: 1,608
  Total tokens: 6,428
  Cost USD: $0.001044

Completed! Check 'results' folder for details.
```

## 📊 Understanding Analysis Results

### JSON output file contains:
```json
{
  "timestamp": "2025-08-22T14:30:22.123456",
  "mode": "complete",
  "results": {
    "analysis_mode": "complete",
    "logs_info": {
      "total_characters": 15234
    },
    "token_summary": {
      "total_prompt_tokens": 4820,
      "total_completion_tokens": 1608,
      "total_tokens": 6428,
      "cost_breakdown": {
        "model_used": "gpt-4o-mini",
        "total_cost_usd": 0.001044
      }
    },
    "analysis_results": {
      "main_errors": {
        "status": "success",
        "answer": "Formatted analysis result...",
        "token_usage": {...},
        "cost_breakdown": {...}
      }
    }
  }
}
```

### 4 types of analysis performed:

1. **main_errors**: "What are the main errors in these Wowza logs? Please list the top 5 most important errors with their frequency."
2. **root_causes**: "What are the root causes of the errors found in these Wowza logs? Explain why these problems occurred."
3. **solutions**: "What are the specific solutions to fix the errors in these Wowza logs? Provide step-by-step instructions."
4. **error_classification**: Detailed error classification and statistics (detailed prompt)

## 🔧 Customization

### Change OpenAI model:
```bash
# In .env file
OPENAI_MODEL=gpt-4o-mini  # Cheapest
OPENAI_MODEL=gpt-4        # Best but more expensive
```

### Add new prompts:
Edit `src/prompts.py`:
```python
def get_simple_prompts():
    return {
        "your_new_prompt": "Your question about the logs...",
        "main_errors": "What are the main errors in these Wowza logs?...",
        "root_causes": "What are the root causes of the errors...",
        "solutions": "What are the specific solutions to fix..."
    }
```

**Note**: Currently only 1 detailed prompt (error_classification) is active. Other detailed prompts are commented out in the code.

## 🐛 Troubleshooting

### Common errors:

**1. "No log files found!"**
```bash
# Check logs directory
ls logs/
# Ensure there are .log or .txt files
```

**2. "Invalid API key"**
```bash
# Check .env file
cat .env
# Ensure API key has correct format: sk-...
```

**3. "Module not found"**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**4. "Permission denied"**
```bash
# Check write permissions for results folder
chmod 755 results/
```

### Debug mode:
```bash
# Run with detailed logging
python -u src/main.py

# Check log file
tail -f wowza_analysis.log
```

## 💰 Usage Costs

### Estimated costs (USD):
- **gpt-4o-mini**: ~$0.001-0.005 per analysis
- **gpt-4**: ~$0.05-0.20 per analysis

### Cost-saving tips:
- ✅ Use `gpt-4o-mini` for daily analysis
- ✅ Only use `gpt-4` when high accuracy is needed
- ✅ Filter log files before analysis

## 🔄 Recommended Workflow

1. **Preparation**: Prepare log files in `logs/`
2. **Quick test**: Run with 1 small file first
3. **Full analysis**: Run with all logs
4. **Review results**: Check JSON file in `results/`
5. **Action items**: Implement suggested solutions

## 📚 Technical Documentation

### Core modules:

- **main.py**: Entry point and user interface (simplified version)
- **ai_analyzer.py**: OpenAI Responses API integration and cost calculation
- **prompts.py**: Analysis prompt templates (3 simple + 1 detailed active)
- **config.py**: Environment configuration management from .env file
- **log_parser.py**: Log file processing utilities (for custom parsing if needed)

### APIs used:
- **OpenAI Responses API**: `client.responses.create()` with input/output format
- **Automatic error handling**: OpenAIError, ConnectionError, TimeoutError
- **Token tracking**: Real-time cost monitoring for gpt-4o-mini and gpt-4

### Actual files in project:
- ✅ `.env.example` - Template config file
- ✅ `requirements.txt` - openai>=1.0.0, python-dotenv>=1.0.0  
- ✅ `.vscode/launch.json` - Debug configuration "Run Main"
- ✅ `logs/` and `results/` folders

