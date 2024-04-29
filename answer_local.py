import pandas as pd
from tts import Say

data = pd.read_csv("qa_data.csv")
qa_dict = dict(zip(data["Q"], data["A"]))

class Answer:
    def __init__(self, text):
        user_input = text
        if user_input in qa_dict:
            response = qa_dict[user_input]
            print("Temmie (local) :", response)
            Say(response)
        else:
            print("hmm... I can't answer that question...;;")
            Say("hmm... I can't answer that question...")
