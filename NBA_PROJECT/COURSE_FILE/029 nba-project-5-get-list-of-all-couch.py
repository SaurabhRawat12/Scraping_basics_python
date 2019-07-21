# already try with requests, this module not work
from bs4 import BeautifulSoup
from selenium import webdriver

# from original link nba.com
# get all coaches name

driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'http://www.nba.com/news/coaches/index.html?ls=iref:nba:gnav'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')
section = soup.find('section',{'id':'nbaArticleContent'})

for p in section.find_all('p'):
	for a in p.find_all('a'):
		# print a.text + "is coach of " + a.find_previous_sibling().text.replace(':','') + " team"
		print a.text + " ---> " + a.find_previous_sibling().text.replace(':','')

driver.quit()

