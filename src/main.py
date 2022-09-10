from time import sleep
from pbj_bot import Bot
def min_to_seconds(minutes: int) -> int:
    return minutes * 60

def main():
    """
    Perform scan on r/all every half hour
    after each scan, drain bad replies
    """
    subreddit = input("Scan on r/")
    test_bot = Bot()
    while test_bot:
        try:
            # perform a scan on top 15 posts of all
            scan_result = test_bot.perform_scan(subreddit, 15)
            if not scan_result:
                print("Successfully exited scan.")
            else:
                print("Scan exited with non-zero code.")

            sleep(min_to_seconds(30))
            test_bot.drain_bad_replies()
        except:
            print("uh oh... Something bad is happening!")
            break

    return

if __name__ == "__main__":
    while True:
        main()
