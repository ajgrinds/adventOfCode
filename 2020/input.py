import datetime
import pytz
import requests
import time

COOKIE = open("cookie.txt").read()


def load_input(year=None, day=None):
    if year is None and day is None:
        date = datetime.datetime.now(pytz.timezone("US/Eastern"))

        year = date.year
        day = date.day

        print("Loading input")
        time.sleep(5)

    if not 1 <= day <= 25:
        print("The day you inputted isn't right")
        return

    while True:
        r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",
                         headers={
                              "authority": "adventofcode.com",
                              "cache-control": "max-age=0",
                              "upgrade-insecure-requests": "1",
                              "dnt": "1",
                              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                            "(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                              "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                                        "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                              "sec-fetch-site": "same-origin",
                              "sec-fetch-mode": "navigate",
                              "sec-fetch-user": "?1",
                              "sec-fetch-dest": "document",
                              "accept-language": "en-US,en;q=0.9",
                              "cookie": COOKIE
                          })
        if r.text == "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is " \
                     "synchronized with the server time; the link will be enabled on the calendar the instant this " \
                     "puzzle becomes available.\n":
            print("The input isn't ready yet, retrying in 10 seconds")
        else:
            break
        time.sleep(5)

    with open("input.txt", "w") as file:
        file.writelines(str(r.text))
    print("Input written")


if __name__ == '__main__':
    load_input()
