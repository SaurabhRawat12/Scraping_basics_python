# Importing essential libraries
from selenium import webdriver
from bs4 import BeautifulSoup
from random import randint
import pandas as pd


#this function gets called when you guessed the correct answer
def correct_ans():
    print("-"*100)
    print("you guessed it correct \n")
    choice =input("want to play again(y/n) \n")
    if type(choice) is not str:
        raise TypeError("choice must be string")
    return choice

#this function gets called when you enter a wrong choice and this provides you a hint
def hints():
    if h==2:
        print("\nheres your 1st hint \n")
        print(f"hint  : the author was born in {big_list[number][3]} at {big_list[number][4]} \n")
        value = input("enter the name \n")
        if type(value) is not str:
            raise TypeError("value must be string")
        return value
    elif h==1:
        print("\n heres your 2nd hint \n")
        print(f"here's a hint  : the author name starts with {big_list[number][0].split(' ')[0][0]} \n")
        value = input("enter the name \n")
        if type(value) is not str:
            raise TypeError("value must be string")        
        return value
    else:
        print("\n heres your 3rd and last hint \n")
        print(f"here's a hint  : the author full initials are {big_list[number][0].split(' ')[0][0]} {big_list[number][0].split(' ')[1][0]} \n")
        value = input("enter the name \n")
        if type(value) is not str:
            raise TypeError("value must be string")        
        return value
    
#this function tells you the remaining chances you have with you
def chances_fun():
    print("-"*100)
    print("no you are wrong \n")
    print(f"no of chances left : {chances} \n")
    if chances==0:
        print("-"*100)
        print(f"the correct answer is : {big_list[number][0]} \n")
        choice =input("want to play again(y/n) \n")
        if type(choice) is not str:
            raise TypeError("choice must be string")
        return choice
    
# scraping part where you extract data from quotes.toscape.com and store it as a tuple
# The tuple contains the Authors name,quote,his bio link,his date of birth,his birth place
driver = webdriver.PhantomJS(executable_path=r'E:\Downloads\Compressed\phantomjs-2.1.1-windows\bin\phantomjs.exe')
names=[]
texts=[]
links=[]
big_list=[]
locations=[]
date_borns=[]
while True:
    for j in range(1,11):
        driver.get(f'http://quotes.toscrape.com/page/{j}/')
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc,'html.parser')
        for quote in soup.find_all("div",class_="quote"):
            text_span = quote.find("span")
            text = text_span.text
            name_span = quote.find("span").find_next_sibling()
            name = name_span.find("small").text
            link = name_span.find("a")["href"]
            names.append(name)
            texts.append(text)
            links.append(link)
            driver.get(f"http://quotes.toscrape.com{link}")
            html_doc = driver.page_source
            soup = BeautifulSoup(html_doc,'lxml')
            date_born = soup.find("span",class_="author-born-date").text
            date_borns.append(date_born)
            location = soup.find("span",class_="author-born-location").text
            locations.append(location)
    if j==10:
        break        
big_list=list(zip(names,texts,links,date_borns,locations))

#creating a dataframe to store all the information
df = pd.DataFrame(names,columns=["Names"])
df["Text"]=texts
df["link"]=links
df["date_born"]=date_borns
df["locations"]=locations

#saving the dataframe as a csv file
df.to_csv("writer.csv")

#guessing game code
while True:   
    chances = 4
    h = 3
    print("-"*100)
    print("Hello! this is a guessing game")
    print("you have three chances to answer it correct \n you will be given a quote and you have to tell who said it \n")
    print("you have to write the name like: J.K. Rowling , Charles Babbage etc")
    size = len(big_list)
    number=randint(0,size-1)
    print("who said this \n")
    value = input(big_list[number][1])
    if type(value) is not str:
        raise TypeError("value must be string")
    if value == big_list[number][0]:
        choice = correct_ans()
        if choice == 'n':
            break
    else:
        chances-=1
        h-=1
        choice = chances_fun()
        if choice=='n':
            break
        print("-"*100)
        value = hints()
        if value == big_list[number][0]:
            choice = correct_ans()
            if choice == 'n':
                break
        else:
            chances-=1
            h-=1
            choice = chances_fun()          
            if choice=='n':
                break
            print("-"*100)
            value = hints()
            if value == big_list[number][0]:
                choice = correct_ans()
                if choice == 'n':
                    break
            else:
                chances-=1
                h-=1
                choice = chances_fun()              
                if choice=='n':
                    break
                print("-"*100)
                value = hints()
                if value == big_list[number][0]:
                    print("you guessed it correct \n")
                    choice = correct_ans()
                    if choice == 'n':
                        break
                else:
                    chances-=1
                    choice = chances_fun()
                    if choice=='n':
                        break
            