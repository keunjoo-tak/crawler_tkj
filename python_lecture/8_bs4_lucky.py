# 쇼미더 럭키짱 크롤링
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=783054"
res = requests.get(url=url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


# table이라는 element로 구성, a tag만 가지고는 title 등의 정보가 없음. 뒤에 있는 td태그의 class가 title인 것을 이요해서 스크래핑 시도
luckys = soup.find_all("td", attrs={"class": "title"})
title = luckys[1].a.get_text()

link = luckys[0].a["href"]

# print(title)
# print(link) # 이렇게만 하면 "??????/webtoon/detail?titleId=783054&no=75&weekday=mon"  앞쪽부분이 잘려있음

# print("https://comic.naver.com"+link)

# 만화 제목이랑 링크 가져오기
# for lucky in luckys:
#     title = lucky.a.get_text()
#     link = "https://comic.namver.com"+lucky.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0

lucky_rates = soup.find_all("div", attrs={"class": "rating_type"})

for lucky_rate in lucky_rates:
    rate = lucky_rate.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("점수 총합 : ", total_rates)
print("평균 점수 : ", total_rates/float(len(lucky_rates)))
