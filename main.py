import os
import PyPDF2
from openai import OpenAI 
from dotenv import load_dotenv,find_dotenv
import prompts

#load .env file

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

model = "gpt-4-turbo"
temperature = 0.3
max_tokens = 500
topic ="procrastination"


#read the pdf file
book = ""
file_path  = "Atomic_habits.pdf"
with open(file_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    start_page = 23
    end_page = total_pages-52

    for page_num in range(start_page, end_page):
        page = reader.pages[page_num]
        book += page.extract_text() + " "

# print(book)

#test call

system_message = prompts.system_message
prompt = prompts.generate_topic(book, topic)
messages = [
    {"role" : "system", "content": system_message},
    {"role" : "user", "content": prompt}
]

def get_summary():
    completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
    )
    return completion.choices[0].message.content


print(get_summary())