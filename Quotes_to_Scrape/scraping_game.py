#importing required libs
import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader
base_url="http://quotes.toscrape.com"

#reading from the csv file containing quotes 
def read_quotes(filename):
    with open(filename,"r",encoding="utf8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

#code for the game
def begin_game(quotes):    
    quote = choice(quotes)
    remaining_guesses = 4
    print("\n Here's a quote :")
    print(quote["Text"])
    guess = ' '
    while guess.lower() != quote["Author"] and remaining_guesses > 0:
        guess = input(f"\n Who said this quote ?  Guesses Remaining : {remaining_guesses} \n")
        if guess.lower() == quote["Author"]:
            print("\n CONGRATS!! You guessed it correct")
        else:
            remaining_guesses -=1
            print_hint(quote,remaining_guesses)
                            
    again = ""
    while again.lower() not in ["yes","y","no","n"]:
        again =input("Would you like to play it again ? (y/n)")
    if again.lower() in ["yes","y"]:
        print("OK! You got to play it again.")
        return begin_game(quotes)
    else:
        print("OK!GOOD BYE.")
        
#function for printing the number of remaining guesses and providing hints accordingly
def print_hint(quote,remaining_guesses):
    if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['Link']}")
        soup = BeautifulSoup(res.text,"html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"\n Here's a hint : The Author was born in {birth_date} {birth_place}")
    elif remaining_guesses == 2:
        print(f"\n Here's a hint : The Author first name starts with : {quote['Author'][0]}")
    elif remaining_guesses == 1:
        print(f"\n Here's a hint : The Author last name starts with : {quote['Author'].split(' ')[1][0]}")
    else:
        print(f"Sorry! You ran out of guesses. The correct answer is {quote['Author']}")        

quotes = read_quotes("quotes.csv")
begin_game(quotes)
    