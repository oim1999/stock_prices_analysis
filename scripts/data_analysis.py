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

""" data['sentiment_category'] = data['sentiment'].apply(classify_sentiment)

# Group by Stock Symbol to get average sentiment per stock
stock_sentiment = data.groupby('stock')['sentiment'].mean().reset_index()
stock_sentiment = stock_sentiment.rename(columns={'sentiment': 'average_sentiment'})

# Display Results
print("\nSentiment Analysis Results:")
print(data[['headline', 'stock', 'sentiment', 'sentiment_category']].head())

print("\nAverage Sentiment per Stock:")
print(stock_sentiment)

# Save the Results
data.to_csv("financial_news_with_sentiment.csv", index=False)
print("Sentiment analysis results saved to 'financial_news_with_sentiment.csv'") """