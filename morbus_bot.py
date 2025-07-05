import tweepy
import os
import time

# ===== 馃攼 诪砖转谞讬 住讘讬讘讛 =====
BEARER_TOKEN = os.environ["BEARER_TOKEN"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]

# ===== 馃摗 讛转讞讘专讜转 诇-Twitter API v2 =====
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

print("馃攧 讛讘讜讟 专抓 (API v2)... 诪讗讝讬谉 诇爪讬讜爪讬诐 注诐 讛诪讬诇讛 '诪讜专讘讜住'")

# 砖诪讬专讛 注诇 爪讬讜爪讬诐 砖讻讘专 专讬讟讜讜讟谞讜
seen_ids = set()

while True:
    try:
        response = client.search_recent_tweets(
            query="诪讜专讘讜住 -is:retweet",
            tweet_fields=["id", "text", "author_id"],
            max_results=10
        )

        tweets = response.data or []

        for tweet in tweets:
            if tweet.id not in seen_ids:
                print(f"馃摙 专讬讟讜讜讬讟 诇爪讬讜抓: {tweet.text}")
                try:
                    client.retweet(tweet.id)
                    seen_ids.add(tweet.id)
                except Exception as e:
                    print(f"鈿狅笍 诇讗 讛爪诇讞谞讜 诇专讟讜讜讟: {e}")

        time.sleep(30)

    except Exception as e:
        print(f"鉂?砖讙讬讗讛 讻诇诇讬转: {e}")
        time.sleep(60)
