import pandas as pd
from tts import Say

data = pd.read_csv("qa_data.csv")

qa_dict = dict(zip(data["질문"], data["답변"]))

class Answer:
    def __init__(self, text):
        user_input = text
        if user_input in qa_dict:
            response = qa_dict[user_input]
            print("ㅇㅔ이ㅇㅏ이:", response)
            Say(response)
        else:
            print("ㅇㅔ이ㅇㅏ이: 어ㅓㅓ;;; 그런 질문은 답 못하는ㄷㅔ..;;")
            Say("어... 그런 딜문은 답 못하눈데...")
