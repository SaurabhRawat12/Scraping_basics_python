from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests

class Player():
	"""docstring for Player"""
	def __init__(self):
		self.name = ""
		self.link = ""
		self.Height = ""
		self.Weight = ""
		self.Born = ""
		
		

def get_player_list():
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

	player_list = []


	for a in div.find_all('a'):
		# print a.text
		# print a['href']
		new_play = Player()
		new_play.name = a.text
		new_play.link = a['href']
		player_list.append(new_play)


	for one_player in player_list:

		print one_player.name
		print one_player.link

	driver.quit()

	return player_list


def get_detail_for_all_players(player_list):

	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	for p in player_list[0:2]:

		# url = 'http://www.nba.com/playerfile/tony_allen/'

		url = p.link

		driver.get(url)

		# print driver.page_source

		soup = BeautifulSoup(driver.page_source, 'lxml')

		Height = ""

		h_span = soup.find('span', string = 'Height:')

		for span in h_span.findNextSiblings():
			Height = Height + span.text


		Weight = ""

		w_span = soup.find('span', string = 'Weight:')

		for span in w_span.findNextSiblings():
			Weight = Weight + span.text


		Born = ""

		b_span = soup.find('span', string = 'Born:')

		for span in b_span.findNextSiblings():
			Born = Born + span.text

		# print Height
		# print Weight
		# print Born

		p.Height = Height
		p.Weight = Weight
		p.Born = Born

	driver.quit()

	return player_list
	


driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'http://www.nba.com/playerfile/tony_allen/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

# print driver.page_source

div = soup.find('div', class_ = 'player-headshot')

img = div.find('img')

print img['src']

f = open('tony_allen.jpg','wb')

f.write(requests.get(img['src']).content)

f.close()

driver.quit()
