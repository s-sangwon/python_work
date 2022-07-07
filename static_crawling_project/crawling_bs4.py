# crawling_bs4.py
# bs4(beautifulsoup4) 를 이용한 웹 크롤링 테스트 코드

# import bs4
# import urllib.request as ur
import urllib.request, bs4
# urllib.request : 웹 상의 데이터를 가져오는 모듈
# bs4 : 웹 페이지의 웹 문서를 html 로 분석하는 모듈임

web_page = urllib.request.urlopen("http://www.naver.com")
# 해당 url 페이지에 접속함
#print(web_page.read())
# 접속한 페이지 소스를 읽어와서, 출력함 : 인코딩된 상태임

result_code = bs4.BeautifulSoup(web_page, 'html.parser')
# 읽어온 인코딩된 웹 코드를 html 태그로 바꿈
print(result_code)
