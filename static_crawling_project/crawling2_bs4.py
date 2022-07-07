# crawling2_bs4.py
# url 을 키보드로 입력받아서 크롤링 테스트

import urllib.request, bs4
# url 은 웹상의 자원까지의 경로를 의미함
# 프로토콜://도메인명/폴더명/파일명?이름=값&이름=값
# 쿼리스트링 : 서버측 대상 코드파일로 전다로디는 값들을 표현한 것
#   ?이름=값&이름=값
# https://n.news.naver.com/article/094/0000010117?cds=news_media_pc&type=editn

url = input("접속할 웹페이지 url 을 입력하세요 : ")

web_page = urllib.request.urlopen(url)

result_code = bs4.BeautifulSoup(web_page, 'html.parser')

print(result_code)