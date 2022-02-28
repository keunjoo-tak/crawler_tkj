# 급하게 타이어를 사야함
# 어떤 타이어가 좋은지 제품명, 가격, 리뷰, 평점을 한눈에 보고 싶음
# exe파일 생성 명령어 : pyinstaller -F 10_bs4_coupang_pages.py

from socketserver import BaseRequestHandler
from turtle import pen
from attr import attrs
from nbformat import write
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}


def CoupangSearch(pKeyword:str(), pEndpage:int(), pRating:float(), pReviweCnt:int() ):
    result = pd.DataFrame(columns=['제품명','가격','평점','평점수','URL'])

    for i in range(1, pEndpage):
        print("긁어오는중...............", i, "페이지")
        url = "https://www.coupang.com/np/search?q={}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(pKeyword,i)

        res = requests.get(url=url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
        # print(items[0].find("div", attrs={"class": "name"}).get_text())

        for item in items:

            # 광고제품 제외 코드
            ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
            if ad_badge:
                # print("<광고 상품 제외>")
                continue

        # 검색 제품 출력 코드
            # 제품 명
            name = item.find("div", attrs={"class": "name"}).get_text()
            # 제품명 조건 설정
            if "(당일무료발송)" in name:
                # print("<당일무료발송 상품 제외>")
                continue

            # 가격
            price = item.find("strong", attrs={"class": "price-value"})
            if price:
                price = price.get_text()
            else:
                price = "가격정보 없음"
                # print(" <가격정보 없는 상품 제외>")
                continue

            # 평점
            rating = item.find("em", attrs={"class": "rating"})
            if rating:
                rating = rating.get_text()
            else:
                rating = "평점 없음"
                # print(" <평점이 없는 상품 제외>")
                continue

            # 평점 수
            total_count = item.find(
                "span", attrs={"class": "rating-total-count"})
            if total_count:
                total_count = total_count.get_text()  # 예 : (127)
                total_count = total_count[1:-1]
            else:
                total_count = "평점 없음"
                # print(" <평점 수 없는 상품 제외>")
                continue

            link = item.find("a", attrs={"class": "search-product-link"})["href"]

            # [검색조건설정]리뷰 50개 이상, 평점 4.5 이상만 조회
            if float(rating) >= pRating and int(total_count) >= pReviweCnt:
                # print("["+name+"]", price+"원", rating+"점", total_count+"개")
                print(f"제품명 : {name}")
                print(f"가격 : {price}")
                print(f"평점 : {rating}점 ({total_count}개)")
                print("바로가기 : {}".format("https://www.coupang.com"+link))
                print("-"*100)  # *줄긋기
            
                result = result.append({'제품명':name, '가격':price, '평점':rating, '평점수':total_count, 'URL':'{}'.format('https://www.coupang.com'+link)}, ignore_index=True)
    return result.to_csv("coupang_result.csv", encoding='utf-8-sig')

Keyword = input("검색할 키워드를 입력하세요 : .............")
Endpage = input("검색할 페이지 수를 입력하세요 : .............")
Rating = input("제품의 최소 평점를 입력하세요 : .............")
ReviewCnt = input("제품의 최소 리뷰 갯수를 입력하세요 : .............")

CoupangSearch(pKeyword=Keyword, pEndpage=int(Endpage), pRating=float(Rating), pReviweCnt=int(ReviewCnt))