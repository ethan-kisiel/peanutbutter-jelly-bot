import praw
import environment_vars
from time import sleep
from os import environ as env
from pbj_bot import bot

def main():
    test_bot = bot.Bot()
    scan_result = 0#test_bot.perform_scan("peanutbutterjellybot")
    if not scan_result:
        print("successful reply")
    else:
        print("scan returned non-zero output")
    test_bot.drain_bad_replies()

    for _id in test_bot.get_parent_ids():
        print(_id)
    return

if __name__ == "__main__":
    main()
