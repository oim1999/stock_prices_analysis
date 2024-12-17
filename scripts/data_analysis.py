import pandas as pd
from textblob import TextBlob



def calc_moving_avrg(data, window):
    return data.rolling(window=window).mean()


# Perform Sentiment Analysis
def get_sentiment(text):
    """
    Function to calculate the sentiment polarity score of a text.
    Args:
        text (str): The input text (headline).
    Returns:
        float: Sentiment polarity score (-1 to +1).
    """
    return TextBlob(text).sentiment.polarity



# Classify Sentiments into Positive, Negative, and Neutral
def classify_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

