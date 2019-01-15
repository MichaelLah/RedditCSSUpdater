import praw

reddit = praw.Reddit('rit', user_agent='rit_site')
print(reddit.user.me())
stylesheet = reddit.subreddit('MyTestPostSub').stylesheet()
new_sheet = stylesheet.stylesheet + '*{background-color: red;}'
reddit.subreddit('MyTestPostSub').stylesheet.update(new_sheet)
