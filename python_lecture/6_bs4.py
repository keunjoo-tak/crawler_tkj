import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url=url)
res.raise_for_status()

# 가져온 html문서를 lxml파서를 통해서 bs4객체(soup)로 만든것
soup = BeautifulSoup(res.text, "lxml")

# print(soup.title)  # bs4객체를 통해서 html밑의 element에 접근 가능
# print(soup.title.get_text())
# print(soup.a)  # soup객체가 가지고 있는 모든 내용 중에서, 처음으로 발견되는 a element에 대한 정보 반환
# print(soup.a.attrs) # a element의 속성 정보를 반환
# print(soup.a['href']) # a element의 href 속성 '값' 정보를 반환

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))  # 클래스 값이 Nbtn_upload인 a element를 반환

# print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)
# print("rank1 :", rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
rank4 = rank3.next_sibling.next_sibling
# print("rank4 :", rank4.a.get_text())
rank3_1 = rank4.previous_sibling.previous_sibling
# print("rank3_1 : ", rank3_1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# print(rank1.parent)

# rank2_1 = rank1.find_next_sibling("li")
# print("rank2_1 : ", rank2_1.a.get_text())
# rank_3_2 = rank2_1.find_next_sibling("li")
# print("rank_3_2 : ", rank_3_2.a.get_text())

# print(rank1.find_next_siblings("li"))


webtoon = soup.find("a", text="싸움독학-120화 : 진심이었다고")
print(webtoon)
