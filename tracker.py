import requests
import smtplib
from bs4 import BeautifulSoup

websiteURL= "https://www.ebay.com/itm/Samsung-Galaxy-S20-Ultra-SM-G9880-256GB-12GB-RAM-FACTORY-UNLOCKED-6-9-108MP/223918055600?hash=item34228e60b0:g:8bUAAOSwzZFeSGNo"

header = {"User Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

price = 0.0

def ebay():
    pg=requests.get(websiteURL, headers=header)
    soup = BeautifulSoup(pg.content, "html.parser")

    product = soup.find(id="itemTitle").get_text()
    product = product[16:]
    p = soup.find(id="prcIsum").get_text()
    price = float(p[4:])

    print("Fetching latest price of product: "+product)

    print("The latest price is: "+p)

def notify_me():
    server= smtplib.

ebay()
notify_me()