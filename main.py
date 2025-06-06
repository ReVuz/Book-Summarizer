import os
import PyPDF2
from openai import OpenAI 
from dotenv import load_dotenv,find_dotenv

#load .env file

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

model = "gpt-3.5-turbo"
temperature = 0.3
max_tokens = 500
topic =""