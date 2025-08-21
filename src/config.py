import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def get_config():
    """
    Get configuration from .env file.
    Returns: dictionary containing all settings
    """
    config = {
        'api_key': os.getenv('OPENAI_API_KEY'),
        'model': os.getenv('OPENAI_MODEL', 'gpt-4o-mini'),
        'logs_folder': os.path.join(os.path.dirname(__file__), '../logs'),
        'results_folder': os.path.join(os.path.dirname(__file__), '../results')
    }
    
    return config

def check_config():
    """
    Check if configuration is complete and valid.
    Returns: True if OK, False if something is missing
    """
    config = get_config()
    
    if not config['api_key']:
        print("ERROR: Missing OPENAI_API_KEY in .env file")
        return False
    
    if not os.path.exists(config['logs_folder']):
        print(f"ERROR: Logs folder does not exist: {config['logs_folder']}")
        return False
    
    print("SUCCESS: Configuration is valid!")
    return True
