import requests
from bs4 import BeautifulSoup

url = 'https://pixabay.com/zh/photos/search/%E7%8C%AB/'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

img_urls = []
for img in soup.find_all('img', {'class':'img-fluid'}):
    img_url = img.get('src')
    img_urls.append(img_url)

print(img_urls)