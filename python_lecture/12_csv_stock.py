import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1-200.csv"
# newline="" : row 입력후 한줄이 공백으로 들어가는걸 없앰
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split(
    "\t")  # ["N", "종목명", "현재가"...] 형태로 들어감(list)
writer.writerow(title)


for page in range(1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find(
        "tbody").find_all("tr")
    for row in data_rows:
        cols = row.find_all("td")
        # 화면에 있는 구분선 제거(td가 1개 없는것들은 의미없는 공백이나 구분선))
        if len(cols) <= 1:
            continue
        data = [col.get_text().strip() for col in cols]
        # print(data)
        writer.writerow(data)
