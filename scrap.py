from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq

my_url = 'https://www.worldometers.info/coronavirus/country/india/'

uClient = uReq(my_url)
page_html = uClinet.read()
uClinet.close()
page_soup = soup(page_html, "html.parser")

'''where in below code we deifne a variable which acutlly represnet the container class of the page that contain information'''
con = page_soup.findAll("div", ("class": "container"))

cont = con[0]
print(con.div.)


