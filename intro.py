import os
from getpass import getpass


"""
# This is me just leanring Langchain and its ecosystem. But if you want to use this to learn also, make sure to install the dependencies listed in the requirements.txt
#  file.
# For this training, I will be using OpenAI's GPT-4o model, so you will need to have an OpenAI API key and set it in your environment variables.

"""

open_ai_api_key = os.getenv("OPENAI_API_KEY")
if not open_ai_api_key:
    open_ai_api_key = getpass("Please enter your OpenAI API key: ")
    if not open_ai_api_key:
        raise ValueError("OpenAI API key is required. Please set it in your environment variables or enter it when prompted.")
    
openai_mode = os.getenv("OPENAI_MODE", "gpt--mini")