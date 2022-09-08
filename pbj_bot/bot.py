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
    LINK = "https://www.youtube.com/watch?v=eRBOgtp0Hac"
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

    def perform_scan(self) -> int:
        return 0

    def make_reply(self, comment) -> int:
        return


