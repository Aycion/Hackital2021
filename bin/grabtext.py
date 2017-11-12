import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python")

soup = BeautifulSoup(r.text, "html.parser")
