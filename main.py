from logging import log
import requests
from bs4 import BeautifulSoup
import json
from loguru import logger
import time
from configparser import ConfigParser
import random

file = "config.ini"
config = ConfigParser()
config.read(file, encoding="utf-8")

link = config["settings"]["link"]
text_abuse = config["settings"]["text"]
chat_id = config["telegram"]["chat_id"]
BOT_TOKEN = config["telegram"]["bot_token"]
reason = "spam"

print(link)
print(text)
print(chat_id)
print(BOT_TOKEN)

with open("proxies.txt") as fs:
    prox = fs.read()

print(
    "http://{0}".format(random.choice(prox)),
)

proxies = {
    "http": "http://{0}".format(random.choice(prox)),
    "https": "http://",
}
s = requests.session()
s.headers.update(
    {
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/85.0.4155.121 Safari/537.36 OPR/71.0.3770.284 (Edition Yx)",
    }
)

link = (
    "https://www.olx.kz/d/obyavlenie/diski-avto-obmen-IDlncD5.html#bfd32d1f83;promoted"
)

r = s.get(link)
soup = BeautifulSoup(r.text, "lxml")
ad_id = soup.find("span", {"class": "css-9xy3gn-Text eu5v0x0"}).text.replace("ID: ", "")


data = {"ad_id": ad_id, "reason": reason, "text": text_abuse}

abuse1 = s.post("https://www.olx.kz/api/v1/moderation/abuse/", data=data).json()
print(abuse1)

requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={abuse1}"
)
