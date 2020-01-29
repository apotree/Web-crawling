import time
import re
import requests
import lxml.html
from pymongo import MongoClient

def main():
    """
    크롤러의 메인 처리
    """
    # 크롤러 호스트의 mongoDB에 접속
    client = MongoClient('localhost', 27017)
    # scraping 데이터베이스의 ebooks 컬렉션
    collection = client.scraping.ebooks
    # 데이터를 식별할 수 있는 유일키를 저장할 key 필드에 인덱스를 생성
    collection.create_index('key', unique=True)

    # 목록 페이지를 추출
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    # 상세 페이지의 URL 목록을 추출
    urls = scrape_list_page(response)
    for url in urls:
        # URL로 키를 추출
        key = extract_key(url)
        # MongoDB에서 key에 해당하는 데이터를 검색
        ebook = collection.find_one({'key':key})
        # MongoDB에 존재하지 않는 경우만 상세 페이지를 크롤링
        if not ebook:
            time.sleep(1)
            response = session.get(url)
            ebook = scrape_detail_page(response)
        # 책 정보를 출력
        print(ebook)


def scrape_list_page(response):
    """
    목록 페이지의 Response에서 상세 페이지의 URL을 추출
    """
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    """
    상세 페이지의 Response에서 책 정보를 dict로 추출
    """
    root = lxml.html.fromstring(response.content)
    ebook= {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [p.text_content()\
                    for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
                    if normalize_spaces(p.text_content()) != '']
    }
    return ebook

def extract_key(url):
    """
    URL에서 키(URL 끝의 p_code)를 추출
    """
    m = re.search(r"p_code=(.+)", url)
    return m.group(11)

def normalize_spaces(s):
    """
    연결돼 있는 공백을 하나의 공백으로 변경
    """
    return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    main()
