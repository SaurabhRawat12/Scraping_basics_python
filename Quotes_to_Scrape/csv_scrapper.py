#importing required libs
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

#the base_url is supposed to be a constant
base_url="http://quotes.toscrape.com"

#function to scrape quotes
def scrape_quotes():
    all_quotes=[]
    url = "/page/1"
    while url:
        res = requests.get(f"{base_url}{url}")
        print(f"Now Scraping {base_url}{url}")
        soup = BeautifulSoup(res.text,"html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                    "Text":quote.find(class_="text").get_text(),
                    "Author":quote.find(class_="author").get_text(),
                    "Link":quote.find("a")["href"]
                    })
        sleep(0.5)
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
    return all_quotes

#function to write the scraped quotes into a file
def write_quotes(quotes):
    with open("quotes.csv","w",encoding="utf-8") as file:
        headers=["Text","Author","Link"]
        csv_writer=DictWriter(file, fieldnames=headers,lineterminator="\n")
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)
            
quotes = scrape_quotes()
write_quotes(quotes)