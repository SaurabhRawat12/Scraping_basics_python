#importing the required libs
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

#locating the PhantomJS
driver = webdriver.PhantomJS(executable_path=r'E:\Downloads\Compressed\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#assigning the url to fetch the data
driver.get('https://in.global.nba.com/playerindex/')

#collecting the html data
html_doc = driver.page_source

#instanting bs4 object
soup = BeautifulSoup(html_doc,'lxml')

#the list that will contain the data
names = []


#searching for the names, href, height, weight, dob, image under the html tags
tr = soup.find_all("tr",class_="ng-scope")
for i in tr:
    td =i.find("td",class_="left player")
    anchor = td.find("a",class_="player-name ng-isolate-scope")
    
    #href
    href = td.find("a")["data-ng-href"]
    
    span = anchor.find("span",class_="ng-binding")
    spans = anchor.find("span",class_="ng-binding").findNextSibling().findNextSibling()
    
    #name 
    name = span.text + " " + spans.text  
    
    #full href
    linktoplayer = 'https://in.global.nba.com'+href
    
    #locating the PhantomJS again for the sub-tabs that contains the reamining data
    driver = webdriver.PhantomJS(executable_path=r'E:\Downloads\Compressed\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(linktoplayer)
    html_docs = driver.page_source
    soups = BeautifulSoup(html_docs,'lxml')
    
    #creating a folder to store the images
    if not os.path.exists("nba_players"):
        os.makedirs("nba_players")
    
    #checking whether the img src is NULL or not
    if soups.find("img",class_="player-img")['src'] == "/media/img/players/head/230x185/not_found.svg":
        continue
    else:
        img = soups.find("img",class_="player-img")['src']
        
        
        #image link
        img='https:'+img
        
        #fetching the image link and storing the images into nba_players
        with open(f"nba_players\{name}","wb") as file:
            file.write(requests.get(img).content)  
            
        div = soups.find("div",class_="player-info-right hidden-sm")
        p = div.find("p",class_="ng-binding")
        upperspan = p.find("span",class_="ng-binding")
        innerspan = upperspan.find("span",class_="ng-binding")
        
        #height
        height = innerspan.text
        
        #weight
        weight = innerspan.next_sibling.next_sibling.next_sibling
        
        #dob
        dob = upperspan.next_sibling.next_sibling.next_sibling
        dob = dob.split(" ")[1]
        
        #creating a dictionary to store the items
        bio ={
        "name":name,
        "href":href,
        "height":height,
        "weight":weight,
        "dob":dob
        }
        
        #appending it to the list
        names.append(bio)
    


