# 웹툰정보 모두 긁어오기
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url=url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 모든 요일웹툰 목록 가져오기
cartoons = soup.find_all("a", attrs={"class": "title"})
# class 속성이 title인 모든 "a" element 반환
for cartoon in cartoons:
    print(cartoon.get_text())
