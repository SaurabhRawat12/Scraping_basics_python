#Scraping done with the help of Selenium and PhantomJS and BeautifulSoup


#importing the necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
from csv import writer

#calling the PhantomJS module from the stored location in memory
driver = webdriver.PhantomJS(executable_path=r'E:\Downloads\Compressed\phantomjs-2.1.1-windows\bin\phantomjs.exe')

i=0
k=0
while True:
    # For extracting the contents of the first page only
    if i == 0:
        headers=["DATE","LINK","TEXT"]
        driver.get('https://www.rithmschool.com/blog')
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc,'lxml')
        for article in soup.find_all('article'):
            h4 = article.find("h4")
            a = h4.find("a")
            text = a.text
            link = a["href"]
            div = article.find("div")
            time = div.find("time")
            date_val = time["datetime"]
            
            #creating a new csv file and storing the content there
            with open("first_python_scrapper.csv","a") as file:
                csv_writer = writer(file,lineterminator='\n')
                if k==0:
                    csv_writer.writerow(headers)
                    k+=1
                csv_writer.writerow([date_val,link,text])
        i+= 1

 # For extracting the contents of the rest of the pages
    else:
        for j in range(2,10):
            driver.get(f'https://www.rithmschool.com/blog?page={j}')
            html_doc = driver.page_source
            soup = BeautifulSoup(html_doc,'lxml')
            for article in soup.find_all('article'):
                h4 = article.find("h4")
                a = h4.find("a")
                text = a.text
                link = a["href"]
                div = article.find("div")
                time = div.find("time")
                date_val = time["datetime"]
                with open("first_python_scrapper.csv","a") as file:
                    csv_writer = writer(file,lineterminator='\n')
                    csv_writer.writerow([date_val,link,text])
           
            
        if j==9:
            break
