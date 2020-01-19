import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("MnVuMdiYoFDE1Si1MnsHSTPk9", "TZzhCYnzKXDJMxdvCWlgnciF066L7wn6Yo0dfS5Dqn4VhUBrZ8")
auth.set_access_token("1218637142168965120-StrPRBbGLD1pvaL031MBGMm6BK5n9x", "gIX62oJIW5Gt6MC1FeB1dT1XFp1pZgryDAu7JywzyvGbP")

api = tweepy.API(auth)
api.update_status("This is a test of tweepy")