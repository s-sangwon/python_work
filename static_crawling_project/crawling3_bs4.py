# crawling_bs4.py
# 네이버 영화 검색 순위 크롤링 분석 테스트

import bs4, urllib.request

web_page = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
result_code = bs4.BeautifulSoup(web_page, 'html.parser')

#순위 값 기록된 태그 엘리먼트 찾기
# 하나의 태그 엘리멭트 정보 추출 : find(사용)
# find(찾을 텍스트가 기록된 상위 태그명,
# find_info = result_code.find("ul", class_="lst_detail_t1")
find_info = result_code.find(class_="lst_detail_t1")
print(find_info) # class 속성에 해당하는 ul 태그 전부 추출

# 영화 목록별로 추출 : ul > li
# 태그 엘리먼트 여러개 추출
movie_list = find_info.find_all("li")
print(len(movie_list)) # 추출한 li 태그 갯수 확인

# 각 li엘리먼트 안의 필요한 값들을 찾ㅇ냄
for idx in range(0, len(movie_list)):
# 제목 찾아내기
    movie_title = movie_list[idx].find(class_="tit").find('a').text
    print((idx) + 1, movie_title) # 상영순위