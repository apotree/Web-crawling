import requests, re
from bs4 import BeautifulSoup

i = 1
numbers = []


def get_bp_info(url):

    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    eurusd = bs_obj.find("table", {"class": "tbl_exchange today"})
    eurusd0 = eurusd.findAll("tr")

    for index, table_rows in enumerate(eurusd0):
        if index > 0:
            tds = table_rows.findAll("td")
            date = tds[0].text.strip()
            nums = tds[1].text.strip()

            print("Date :", date + " Price :", nums)


def remove_tags(lists):
    re.replace()


for i in range(1, 1100):
    get_bp_info("https://finance.naver.com/marketindex/worldDailyQuote.nhn?fdtc=4&marketindexCd=FX_EURUSD&page=" + str(i))
