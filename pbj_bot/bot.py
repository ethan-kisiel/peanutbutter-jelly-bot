import praw
import environment_vars
from time import sleep
from os import environ as env

class bot:
    """
    class for controlling the
    functionality of the bot
    """

    check_for = ["peanutbutterandjelly",
                "peanutbutter&jelly",
                "pbandj",
                "pb&j",
                "peanutbutterjellytime"]

    message = "It's peanut butter jelly time!"
    link = "https://www.youtube.com/watch?v=eRBOgtp0Hac"
    link_message = f"[{message}]({link})"

    def __init__(self) -> None:
        return

    def perform_scan(self) -> int:
        return 0

    def make_reply(self, comment)


