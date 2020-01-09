import requests
from bs4 import BeautifulSoup

url = "https://naver.com"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

keyword = bs_obj.find("div", {"class": "ah_roll_area"}) # 검색 범위 간소화
keyword_rank = keyword.findAll("span", {"class": "ah_r"}) # 순위 출력
keyword_word = keyword.findAll("span", {"class": "ah_k"}) # 검색어 출력

for i in range(0, 20): # 1위부터 20위까지 출력
    print(keyword_rank[i].text + "." + keyword_word[i].text)
