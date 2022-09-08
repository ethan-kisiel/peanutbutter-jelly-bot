import praw
import environment_vars
from time import sleep
from os import environ as env

class Bot:
    """
    class for controlling the
    functionality of the bot
    """

    check_for = ["peanutbutterandjelly",
                "peanutbutter&jelly",
                "pbandj",
                "pb&j",
                "peanutbutterjellytime"]

    MESSAGE = "It's peanut butter jelly time!"
    LINK = "https://www.youtube.com/watch?v=BNIVUByuylE&autoplay=1"
    LINK_MESSAGE = f"[{MESSAGE}]({LINK})"

    def __init__(self) -> None:
        """
        initialize reddit instance
        and initialize structure for keeping track of comments
        """

        self.reddit = praw.Reddit(client_id=env.get("CLIENT_ID"),
                            client_secret=env.get("CLIENT_SECRET"),
                            user_agent=env.get("USER_AGENT"),
                            username=env.get("USERNAME"),
                            password=env.get("PASSWORD"))

        self.redditor = self.reddit.user.me()
        self.parent_ids = self.initialize_comment_parents()

    def initialize_comment_parents(self) -> set[str]:
        parent_ids = set()
        for comment in self.redditor.comments.new(limit=None):
            if hasattr(comment, "body") and  hasattr(comment, "parent_id"):
                parent_ids.add(comment.parent_id)

        return parent_ids

    def perform_scan(self, subreddit: str) -> int:
        """
        Scans for reddit comments
        """

        try:
            subreddit = reddit.subreddit(subreddit)
                for submission in subreddit.hot(limit=10):
                    comments = submission.comments
                    comments.replace_more(limit=None)
                    for comment in comments:
                        if hasattr(comment, "body"):
                            condensed_lower = comment.body.lower()
                            condensed_lower.replace(' ', '')
                            for check in check_for:
                                if check in condensed_lower:
                                    #comment.reply(link)
                                    if !make_reply(comment):
                                        sleep(660)
                                        break
        except:
            return 1
        return 0

    def make_reply(self, comment) -> int:
        """
        attempts to make a reply to
        given comment and adds the given
        comment's id to self.parent_ids
        """
        comment_id = comment.id
        # adds the comment id of the comment we are responding to
        if comment_id not in self.parent_ids:
            comment.reply()
            self.parent_ids.add(comment_id)

        else:
            return 1
        return 0


    def drain_bad_replies(self):
        """
        Runs through all bot comments
        if a comment has more than x
        percent downvote rate that comment
        is deleted
        """
        for comment in self.comments.new(limit=0):
            if comment.score < -2:
                comment.delete()
        return
