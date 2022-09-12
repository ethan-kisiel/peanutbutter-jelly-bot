import praw
import environment_vars
from time import sleep
from os import environ as env

class Bot:
    """
    class for controlling the
    functionality of the bot
    """

    CHECK_FOR = ["peanutbutterandjelly",
                "peanutbutter&jelly",
                "pbandj",
                "pb&j",
                "peanutbutterjellytime"]

    MESSAGE = "It's peanut butter jelly time!"
    LINK = "https://www.youtube.com/watch?v=BNIVUByuylE&autoplay=1"
    LINK_MESSAGE = f"[{MESSAGE}]({LINK})"
    FOOTER = "If this message recieves negative upvotes it will be removed."
    FINAL_MESSAGE = f"{LINK_MESSAGE}\n\n{FOOTER}"

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

    def __repr__(self):
        return self.redditor.name

    def __bool__(self):
        return True if self.redditor else False

    def initialize_comment_parents(self) -> set[str]:
        parent_ids = set()
        for comment in self.redditor.comments.new(limit=None):
            if hasattr(comment, "body") and  hasattr(comment, "parent_id"):
                parent_ids.add(comment.parent_id)

        return parent_ids

    def perform_scan(self, subreddit_name: str, limit: int) -> int:
        """
        Scans top level comments limit number of posts in subreddit_name
        """

        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            for submission in subreddit.hot(limit=limit):
                comments = submission.comments
                comments.replace_more(limit=None)
                for comment in comments:
                    if hasattr(comment, "body"):
                        if Bot.check_comment(comment):
                            reply_result = self.make_reply(comment)
                            if not reply_result:
                                print("sent reply")
                                sleep(660)
                                break
        except:
            print("caught exception")
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
            comment.reply(Bot.FINAL_MESSAGE)
            self.parent_ids.add(comment_id)
        else:
            return 1
        return 0


    def drain_bad_replies(self):
        """
        Runs through all bot comments
        if a comment has less than x
        upvotes, it will be deleted.
        """
        for comment in self.redditor.comments.new(limit=None):
            if comment.score < 1:
                comment.delete()
                self.parent_ids = self.initialize_comment_parents()
        return

    def get_parent_ids(self):
        return self.parent_ids

    def check_comment(comment) -> bool:
        """
        Iterates through CHECK_FOR
        if an element is contained,
        returns true
        """
        condensed_lower = comment.body.lower()
        condensed_lower = condensed_lower.replace(' ', '')
        for check in Bot.CHECK_FOR:
            if check in condensed_lower:
                return True
        return False

