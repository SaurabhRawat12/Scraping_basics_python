from selenium import webdriver
from bs4 import BeautifulSoup

# create driver
driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'http://stats.nba.com/players/?ls=iref:nba:gnav'

# download html page
driver.get(url)

# print driver.page_source

# create soup
soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_= 'col-lg-12')

# print div

for a in div.find_all('a'):
	print a.text

driver.quit()