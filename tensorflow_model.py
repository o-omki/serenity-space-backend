from dotenv import load_dotenv
import os
# import tensorflow as tf
# import tensorflow_text as text
# from tensorflow import keras

model = None

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
    return 50
    

    
 