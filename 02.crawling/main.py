import requests
from bs4 import BeautifulSoup

# 네이버 웹툰의 목록 페이지에 HTTP GET요청 전송, 결과를 response변수에 저장
response = requests.get('https://comic.naver.com/webtoon/weekday.nhn')

print(response)
print(dir(response))
print(response.url)
