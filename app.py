from flask import Flask, render_template
import pandas as pd
from analysis import analyze_sentiment, classify_satisfaction
import os

app = Flask(__name__, template_folder='D:/Aditya/Social-media-dataset-samples-main/templates')

# Path to your Instagram dataset
data_file = 'D:/Aditya/Social-media-dataset-samples-main/instagram_qos/data/Instagram-datasets.csv'

# Path to your Twitter dataset (corrected path)
twitter_data_file = 'D:/Aditya/Social-media-dataset-samples-main/instagram_qos/data/Twitter-datasets.csv'

@app.route('/')
def dashboard():
    df = pd.read_csv(data_file)

    # Ensure correct column names for Instagram data
    df.rename(columns={
        'comment': 'Comment',
        'likes_number': 'Likes',
        'replies_number': 'Replies'
    }, inplace=True)

    # Drop rows with missing comments
    df = df.dropna(subset=['Comment'])

    # Apply sentiment analysis
    df['Sentiment'] = df['Comment'].apply(analyze_sentiment)

    # Apply satisfaction classification
    df['Satisfaction'] = df.apply(classify_satisfaction, axis=1)

    # Prepare values for Instagram dashboard
    avg_sentiment = round(df['Sentiment'].mean(), 4)
    satisfaction_count = df['Satisfaction'].value_counts().to_dict()

    return render_template(
        'dashboard.html',
        avg_sentiment=avg_sentiment,
        satisfaction_count=satisfaction_count
    )

@app.route('/twitter_dashboard')
def twitter_dashboard():
    # Load the Twitter dataset using the correct path
    df = pd.read_csv(twitter_data_file)

    # Ensure correct column names for Twitter data
    df.rename(columns={
        'description': 'Comment',
        'likes': 'Likes',
        'replies': 'Replies'
    }, inplace=True)

    # Drop rows with missing comments
    df = df.dropna(subset=['Comment'])

    # Apply sentiment analysis
    df['Sentiment'] = df['Comment'].apply(analyze_sentiment)

    # Apply satisfaction classification
    df['Satisfaction'] = df.apply(classify_satisfaction, axis=1)

    # Prepare values for Twitter dashboard
    avg_sentiment = round(df['Sentiment'].mean(), 4)
    satisfaction_count = df['Satisfaction'].value_counts().to_dict()

    return render_template(
        'twitter_dashboard.html',
        avg_sentiment=avg_sentiment,
        satisfaction_count=satisfaction_count
    )

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
import pandas as pd
from analysis import analyze_sentiment, classify_satisfaction
import os

app = Flask(__name__, template_folder='D:/Aditya/Social-media-dataset-samples-main/templates')

# Path to your Instagram dataset
data_file = 'D:/Aditya/Social-media-dataset-samples-main/instagram_qos/data/Instagram-datasets.csv'

# Path to your Twitter dataset (corrected path)
twitter_data_file = 'D:/Aditya/Social-media-dataset-samples-main/twitter_qos/data/Twitter-datasets.csv'

@app.route('/')
def dashboard():
    df = pd.read_csv(data_file)

    # Ensure correct column names for Instagram data
    df.rename(columns={
        'comment': 'Comment',
        'likes_number': 'Likes',
        'replies_number': 'Replies'
    }, inplace=True)

    # Drop rows with missing comments
    df = df.dropna(subset=['Comment'])

    # Apply sentiment analysis
    df['Sentiment'] = df['Comment'].apply(analyze_sentiment)

    # Apply satisfaction classification
    df['Satisfaction'] = df.apply(classify_satisfaction, axis=1)

    # Prepare values for Instagram dashboard
    avg_sentiment = round(df['Sentiment'].mean(), 4)
    satisfaction_count = df['Satisfaction'].value_counts().to_dict()

    return render_template(
        'dashboard.html',
        avg_sentiment=avg_sentiment,
        satisfaction_count=satisfaction_count
    )

@app.route('/twitter_dashboard')
def twitter_dashboard():
    # Load the Twitter dataset using the correct path
    df = pd.read_csv(twitter_data_file)

    # Ensure correct column names for Twitter data
    df.rename(columns={
        'description': 'Comment',
        'likes': 'Likes',
        'replies': 'Replies'
    }, inplace=True)

    # Drop rows with missing comments
    df = df.dropna(subset=['Comment'])

    # Apply sentiment analysis
    df['Sentiment'] = df['Comment'].apply(analyze_sentiment)

    # Apply satisfaction classification
    df['Satisfaction'] = df.apply(classify_satisfaction, axis=1)

    # Prepare values for Twitter dashboard
    avg_sentiment = round(df['Sentiment'].mean(), 4)
    satisfaction_count = df['Satisfaction'].value_counts().to_dict()

    return render_template(
        'twitter_dashboard.html',
        avg_sentiment=avg_sentiment,
        satisfaction_count=satisfaction_count
    )

if __name__ == '__main__':
    app.run(debug=True)
