import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET_KEY"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
)

# Posting tweet menggunakan API v2
response = client.create_tweet(text="Test tweet using Tweepy v2")
print(response)
