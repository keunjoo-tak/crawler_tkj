# 급하게 코딩용 노트북을 사야함
# 어떤 노트북이 좋은지, 리뷰, 평점 고려

from socketserver import BaseRequestHandler
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%ED%95%9C%EA%B5%AD%ED%83%80%EC%9D%B4%EC%96%B4&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

res = requests.get(url=url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class": "name"}).get_text())

for item in items:

    # 광고제품 제외 코드
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("<광고 상품 제외>")
        continue

# 검색 제품 출력 코드
    # 제품 명
    name = item.find("div", attrs={"class": "name"}).get_text()
    # 제품명 조건 설정
    if "(당일무료발송)" in name:
        print("<당일무료발송 상품 제외>")
        continue

    # 가격
    price = item.find(
        "strong", attrs={"class": "price-value"}).get_text()

    # 평점
    rating = item.find("em", attrs={"class": "rating"})
    if rating:
        rating = rating.get_text()
    else:
        rating = "평점 없음"
        print(" <평점이 없는 상품 제외>")
        continue

    # 평점 수
    total_count = item.find(
        "span", attrs={"class": "rating-total-count"})
    if total_count:
        total_count = total_count.get_text()  # 예 : (127)
        total_count = total_count[1:-1]
    else:
        total_count = "평점 없음"
        print(" <평점 수 없는 상품 제외>")
        continue

    # [검색조건설정]리뷰 50개 이상, 평점 4.5 이상만 조회
    if float(rating) >= 4 and int(total_count) >= 10:
        print("["+name+"]", price+"원", rating+"점", total_count+"개")
