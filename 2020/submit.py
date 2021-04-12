import datetime
import pytz
import requests
import time
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def web():
    return "Web server online"


class Submit:
    def __init__(self, year=None, day=None):
        self.cookie = ""

        date = datetime.datetime.now(pytz.timezone("US/Eastern"))
        self.year = date.year if year is None else year
        self.day = date.day if day is None else day

        print("Loading input")
        self.file = self.__load_input()


    def __load_input(self):
        r = requests.get(f"https://adventofcode.com/{self.year}/day/{self.day}/input",
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
                              "cookie": self.cookie
                          })
        with open("input.txt", "w") as file:
            file.writelines(str(r.text))
        return open("input.txt").read().splitlines()

    def submit(self, num):
        print(num)
        r = requests.post("https://adventofcode.com/2018/day/2/answer", headers={
            "authority": "adventofcode.com",
            "cache-control": "max-age=0",
            "origin": "https://adventofcode.com",
            "upgrade-insecure-requests": "1",
            "dnt": "1",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://adventofcode.com/2018/day/2",
            "accept-language": "en-US,en;q=0.9",
            "cookie": self.cookie
        },
                          data={"level": 1, "answer": num}
                          )

        if "That\'s the right answer!" in str(r.content):
            print("That's right")
        else:
            print("That's wrong")
        time.sleep(20)

Submit()
app.run(port=80)
