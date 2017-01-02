import requests
from bs4 import BeautifulSoup
daily_star = requests.get('http://www.thedailystar.net')
print(daily_star.url)
print(daily_star.status_code)

test_html = BeautifulSoup(daily_star.text, 'lxml')
headlines  = test_html.find_all('h5')


print(headlines[0])

