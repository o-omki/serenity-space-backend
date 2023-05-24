import time
from dotenv import load_dotenv
import os
import openai
# import tensorflow as tf
# import tensorflow_text as text
# from tensorflow import keras

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
model = None

def openai_sentiment_analyser(journal_input: str):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"I want you to act like a sentiment analyser of a text. You are the best and most accurate sentiment analyser. \n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I want you to analyse the following text and generate a sentiment score between 1 to 100 with 100 being for the most positive. Respond with just Score:score_value. The text is {journal_input}.\nAI:",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    score = response.get("choices")[0].get("text").split("Score:")[1].strip() # type: ignore
    
    # if score contains only numbers except for . then return int(score) else remove all non numeric characters except . and return int(score)
    if score.replace(".", "").isnumeric():
        return int(score)
    else:
        return int("".join(filter(str.isdigit, score)))
    


def load_model():
    global model
    # if model is None:
        # model = keras.models.load_model(os.getenv("MODEL_PATH"))
    
    return model

def predict_journal_mood(journal_input: str):
    # global model
    # if model is None:
    #     model = load_model()
    
    # return model(tf.constant(journal_input))
    print("Predicting mood for journal entry: " + journal_input)
    try:
        return openai_sentiment_analyser(journal_input)
    except openai.error.APIError as e: # type: ignore
        print("OpenAI API Error: " + str(e))
        print("Waiting for 5 seconds and trying again")
        time.sleep(5)
        return openai_sentiment_analyser(journal_input)
    except Exception as e:
        print("Error: " + str(e))
        raise Exception

    