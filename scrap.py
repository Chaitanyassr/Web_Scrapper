my_url = 'https://www.worldometers.info/coronavirus/country/india/'

uClient = uReq(my_url)
page_html = uClinet.read()
uClinet.close()
page_soup = soup(page_html, "html.parser")

con = page_soup.findAll("div", ("class": "container"))
