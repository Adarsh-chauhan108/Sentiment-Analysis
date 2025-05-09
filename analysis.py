from textblob import TextBlob

def analyze_sentiment(comment):
    """
    Analyze sentiment using TextBlob. Returns polarity.
    """
    return TextBlob(comment).sentiment.polarity

def classify_satisfaction(row):
    """
    Classify user satisfaction based on likes, replies, and sentiment.
    """
    if row['Likes'] > 100 and row['Replies'] > 50 and row['Sentiment'] > 0:
        return 'Highly Satisfied'
    elif row['Likes'] > 50 and row['Replies'] > 20:
        return 'Satisfied'
    else:
        return 'Dissatisfied'
