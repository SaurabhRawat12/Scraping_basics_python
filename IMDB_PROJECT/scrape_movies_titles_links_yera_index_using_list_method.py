#importing the required libs
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

#creating a folder to store the posters
if not os.path.exists("imdb_posters"):
    os.makedirs("imdb_posters")

#locating the PhantomJS
driver = webdriver.PhantomJS(executable_path=r"E:\Downloads\Compressed\phantomjs-2.1.1-windows\bin\phantomjs.exe")

#assigning the url to fetch the data
url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
driver.get(url)

#collecting the html data
html = driver.page_source

#instanting bs4 object
soup = BeautifulSoup(html,"lxml")

static_url = "https://www.imdb.com"

#the list that will contain the data
Movies=[]

#searching for the index, href, title, year_of_realease, image under the html tags
table = soup.find("table",class_="chart")
for td in table.find_all("td",class_="titleColumn"):
    
    #index
    index = td.text
    a = td.find("a")
    
    #title
    title = a.text
    
    #href
    href = a["href"]
    href = static_url+href
    
    #year
    year = a.findNextSibling().text
    
    #locating the PhantomJS again for the sub-tabs that contains the reamining data
    driver = webdriver.PhantomJS(executable_path=r"E:\Downloads\Compressed\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    driver.get(href)
    htmls = driver.page_source
    soups = BeautifulSoup(htmls,"lxml")
    
    div = soups.find("div",class_="poster")
    
    #poster_link
    poster_href = div.find("a")["href"]
    poster_href = static_url+poster_href
    driver.get(poster_href)
    htmlss = driver.page_source
    soupss = BeautifulSoup(htmlss,"lxml")
    img = soupss.find("img",class_="pswp__img")["src"]
    
    #fetching the poster link and storing them into nba_players imdb_posters
    with open(f"imdb_posters\{title}","wb") as file:
        file.write(requests.get(img).content)
    
            #creating a dictionary to store the items
    disc = {
            "index":index,
            "name":title,
            "year":year,
            "href":href
            }
    #appending it to the list    
    Movies.append(disc)

#printing the data stored in lists    
for thing in Movies:
    print(f"Index : {thing[0]}")
    print(f"title : {thing[1]}")
    print(f"href : {thing[2]}")
    print(f"year : {thing[3]}")    

    

