import requests
from bs4 import BeautifulSoup

def getTemp():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
    response= requests.get(url)

    naver_html = response.text
    soup = BeautifulSoup(naver_html, 'html.parser')

    temp = soup.select_one(".todaytemp")
    return temp.text