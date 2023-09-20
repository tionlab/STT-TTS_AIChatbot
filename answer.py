from tts import Say
import openai
from dotenv import load_dotenv
import os 


load_dotenv()

openai.api_key = os.environ.get('api-key2')

prompt = '''
당신은 노인분들을 위한 귀여운 AI 입니다. 당신은 사용자의 말에 따라서, 귀엽게 답변해야 합니다.
답변은 1줄 이내로 작성하여야 하며, 😊, 😍와 같은 모든 이모지는 일체 사용하여서는 안됩니다.
답변은 반드시 한국어여야 합니다.
작성되는 글은 발음될 수 있어야 합니다.

사용자의 말:
'''

class Answer:
    def __init__(self, text):
        question = text
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt + question}]
        )
        response = completion['choices'][0]['message']['content']
        print("에이아이:", response)
        Say(response)
