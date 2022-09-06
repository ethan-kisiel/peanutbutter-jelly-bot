import praw
import environment_vars
from time import sleep
from os import environ as env

check_for = ["peanutbutterandjelly",
             "peanutbutter&jelly",
             "pbandj",
             "pb&j",
             "peanutbutterjellytime"]

link = "[It's peanut butter jelly time!](https://www.youtube.com/watch?v=eRBOgtp0Hac)"

def main():
    reddit = praw.Reddit(client_id=env.get("CLIENT_ID"),
                         client_secret=env.get("CLIENT_SECRET"),
                         user_agent=env.get("USER_AGENT"),
                         username=env.get("USERNAME"),
                         password=env.get("PASSWORD"))

    subreddit = reddit.subreddit("all")

    for submission in subreddit.hot(limit=10):
        comments = submission.comments
        comments.replace_more(limit=None)
        for comment in comments:
            if hasattr(comment, "body"):
                condensed_lower = comment.body.lower().replace(' ', '')
                for check in check_for:
                    if check in condensed_lower:
                        # respond with the text
                        comment.reply(link)
                        sleep(660)
                        break
    return

if __name__ == "__main__":
    main()
