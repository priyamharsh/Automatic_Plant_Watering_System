def get_weather():
	import requests
	from bs4 import BeautifulSoup

	# enter city name
	city = "bokaro"

	# creating url and requests instance
	url = "https://www.google.com/search?q="+"weather"+city
	html = requests.get(url).content

	# getting raw data
	soup = BeautifulSoup(html, 'html.parser')
	temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
	str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

	# formatting data
	data = str.split('\n')
	time = data[0]
	sky = data[1]
	return sky

def itw_rain():
	rain = False
	params = ['rain', 'Rain', 'storm', 'Storm', 'cloudy', 'Cloudy', 'shower', 'Showers']
	for i in params:
	    if get_weather() == i:
	        rain = True
	return rain

