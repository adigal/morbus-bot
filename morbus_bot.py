import tweepy
import time
import os

# ===== 🔐 קריאה ממשתני סביבה =====
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

# ===== 📡 התחברות ל-Twitter API =====
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# ===== 🧠 שמירה על ציוצים שכבר ריטווטנו =====
seen_tweet_ids = set()

print("🔄 הבוט רץ... מאזין לציוצים עם המילה 'מורבוס'")

while True:
    try:
        for tweet in api.search_tweets(q="מורבוס", lang="he", result_type="recent", count=5):
            if tweet.id not in seen_tweet_ids and not tweet.retweeted:
                print(f"📢 ריטוויט לציוץ של @{tweet.user.screen_name}: {tweet.text}")
                api.retweet(tweet.id)
                seen_tweet_ids.add(tweet.id)

        time.sleep(30)

    except tweepy.TweepyException as e:
        print(f"❌ שגיאה: {e}")
        time.sleep(60)
