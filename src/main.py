from time import sleep
from pbj_bot import Bot

def main():
    """
    Perform scan on r/all every hour
    after each scan, drain bad replies
    """
    test_bot = Bot()
    print(test_bot)
    '''
    scan_result = test_bot.perform_scan("peanutbutterjellybot")

    if not scan_result:
        pass
    else:
        pass
    test_bot.drain_bad_replies()
    '''
    return

if __name__ == "__main__":
    main()
