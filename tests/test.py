import spacy

nlp = spacy.load('pt_core_news_sm')
texto = input("->")

doc = nlp(texto)

for token in doc:
    print(token.text, token.pos_)


"""import geocoder
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_current_location():
    g = geocoder.ip('me')
    return g.city 

current_location = get_current_location()

def weather(city):
    city=city.replace(" ","+")
    res=requests.get(f'https://www.google.com/search?q={city}&oq={city}'f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid='f'chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    print(soup.select('.BNeawe.iBp4i.AP7Wnd')[1].getText())

weather(current_location + " weather")"""