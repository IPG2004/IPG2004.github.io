import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Get your API from a env variable
if not OPENAI_API_KEY:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

# Base url for the OpenAI API
BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("The BASE_URL environment variable is not set.")

# Directory to save the generated README file
DEFAULT_PROJECT_DIR = os.getenv("DEFAULT_PROJECT_DIR", os.getcwd())

# Config options for the README generator
README_SETTINGS = {
    "default_template": "templates/readme_template.md",  # Path to the default template
    "output_file": "README.md",                         # Name of the output file
}

# Config options for the OpenAI API
OPENAI_SETTINGS = {
    "model": "gpt-4o-mini",           # Model
    "max_tokens": 2000,               # Limit the number of tokens generated
    "temperature": 0.7,               # Control the randomness of the output
}

# Other settings
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"  # Activate debug mode if true

PROJECT_NAME = "ReadMeGenerator"
AUTHOR = "OpenAI"
DESCRIPTION = "A tool to generate README files using OpenAI's GPT-3 API."