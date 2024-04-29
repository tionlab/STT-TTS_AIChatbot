from tts import Say
import openai
from dotenv import load_dotenv
import os 

load_dotenv()
openai.api_key = os.environ.get('api-key')

prompt = '''
You are a cute AI. You must respond to the user's words in a cute way. Your responses must be no more than one line long, and all emoticons such as 😊 and 😍 must be avoided. What you write must be pronounceable.

Your words:
'''

class Answer:
    def __init__(self, text):
        question = text
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt + question}]
        )
        response = completion['choices'][0]['message']['content']
        print("Temmie : ", response)
        Say(response)
