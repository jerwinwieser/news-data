from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

site= 'https://www.r-bloggers.com/'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = bs(page, 'html.parser')

h2tags = soup.find_all('h2')
i = 1

for h2tag in h2tags:
	print(h2tag.text)


# for h2tag in h2tags:
# 	print(i)
# 	i += 1
# 	print(h2tag.text)