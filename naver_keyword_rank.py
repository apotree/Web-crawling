import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now() # 현재 날짜와 시간을 가져옴

url = "https://naver.com"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

keyword = bs_obj.find("div", {"class": "ah_roll_area"}) # 검색 범위 간소화
keyword_rank = keyword.findAll("span", {"class": "ah_r"}) # 순위 출력
keyword_word = keyword.findAll("span", {"class": "ah_k"}) # 검색어 출력


print("{}년 {}월 {}일 {}시 {}분 {}초 \n네이버 실시간 검색어\n".format(now.year, now.month, now.day, now.hour, now.minute, now.second))

for i in range(0, 20): # 1위부터 20위까지 반복
    print(keyword_rank[i].text + "." + keyword_word[i].text)
