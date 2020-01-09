import requests
from bs4 import BeautifulSoup

url = "https://naver.com"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
eng = bs_obj.find("div", {"class": "tc_content"})
eng_in1 = eng.find("p", {"class": "tc_tt"})
eng_in2 = eng.find("p", {"class": "tc_st"})
eng_in3 = eng.find("p", {"class": "tc_pronounce"})

print("원문 : ", eng_in1.text)
print("영문 : ", eng_in2.text)
print("발음 : ", eng_in3.text)
