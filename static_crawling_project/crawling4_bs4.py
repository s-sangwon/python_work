# crawling4_bs4
# 실습 1 :
# 영화 상영작 정보 페이지에서 전체관람가, 15세관람가, 12세 관람가 로
# 영화를 분류해서 각각 리스트에 저장한 다음 출력 확인
# 전체관람가 리스트, 15세 관람가 리스트, 12세 관람가 리스트
# 각 리스트에 저장 정보 예 : '1위 : 토르, 예매율 : 35%'
import urllib.request, bs4
def minepractice(movie_list):
    list_allspec = []
    list_12 = []
    list_15 = []
    spector = ''
    r12 = 1
    r15 = 1
    rall = 1

    for idx in range(0, len(movie_list)):
        movie_title = movie_list[idx].find(class_="tit").find('a').text
        try:
            spector = movie_list[idx].find(class_="tit").find('span').text
        except Exception as msg:
            print(movie_title, '은 몇세 이용 관람가인지 등록되지 않았습니다.')
        movie_title = movie_list[idx].find(class_="tit").find('a').text
        avgnum = movie_list[idx].find(class_="star_t1").find(class_="num").text
        if spector == '12세 관람가':
            text = str(idx+1) + '위 : ' + movie_title + '평점 : ' + avgnum + '점'
            list_12.append(text)
            r12 += 1
        elif spector == '15세 관람가':
            text = str(idx+1) + '위 : ' + movie_title + '평점 : ' + avgnum + '점'
            list_15.append(text)
            r15 += 1
        elif spector == '전체 관람가':
            text = str(idx+1) + '위 : ' + movie_title + '평점 : ' + avgnum + '점'
            list_allspec.append(text)
            rall += 1

    print(list_allspec)
    print(list_12)
    print(list_15)

if __name__ == '__main__':
    web_page = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
    result_code = bs4.BeautifulSoup(web_page, 'html.parser')


    find_info = result_code.find(class_="lst_detail_t1")

# 영화 목록별로 추출 : ul > li
# 태그 엘리먼트 여러개 추출
    movie_list = find_info.find_all("li")
    print(len(movie_list)) # 추출한 li 태그 갯수 확인

    # minepractice(movie_list)
    pass_all = []
    pass_12 = []
    pass_15 = []

    for idx in range(0, len(movie_list)):
        movie_title = movie_list[idx].find(class_="tit").find('a').text
        avgnum = movie_list[idx].find(class_="star_t1").find(class_="num").text
        if movie_list.find(class_='tit').find('span', class_='ico_ration_15'):
            movie_info = f'{idx+1} 위 : {movie_title}, 평점 : {avgnum} 점'
            pass_15.append(movie_info)
        elif movie_list.find(class_='tit').find('span', class_='ico_ration_12'):
            movie_info = f'{idx+1} 위 : {movie_title}, 평점 : {avgnum} 점'
            pass_12.append(movie_info)
        elif movie_list.find(class_='tit').find('span', class_='ico_ration_all'):
            movie_info = f'{idx+1} 위 : {movie_title}, 평점 : {avgnum} 점'
            pass_all.append(movie_info)
    print(pass_15)
# 각 li엘리먼트 안의 필요한 값들을 찾ㅇ냄
# for idx in range(0, len(movie_list)):
# 제목 찾아내기
#     movie_title = movie_list[idx].find(class_="tit").find('a').text
    # print((idx) + 1, movie_title) # 상영순위

# list_allspec = []
# list_12 = []
# list_15 =[]
# spector = ''
# r12=1
# r15=1
# rall=1
#
# for idx in range(1, len(movie_list)):
#     movie_title = movie_list[idx].find(class_="tit").find('a').text
#     try:
#         spector = movie_list[idx].find(class_="tit").find('span').text
#     except Exception as msg:
#         print(movie_title, msg)
#     movie_title = movie_list[idx].find(class_="tit").find('a').text
#     avgnum = movie_list[idx].find(class_="star_t1").find(class_="num").text
#     if spector == '12세 관람가':
#         text = str(r12)+'위 : ' + movie_title + '평점 : ' + avgnum + '점'
#         list_12.append(text)
#         r12 += 1
#     elif spector == '15세 관람가':
#         text = str(r15) + '위 : ' + movie_title + '평점 : ' + avgnum + '점'
#         list_15.append(text)
#         r15 +=1
#     elif spector == '전체 관람가':
#         text = str(rall) + '위 : ' + movie_title + '평점 : ' + avgnum + '점'
#         list_allspec.append(text)
#         rall += 1
#
#     print(list_allspec)
#     print(list_12)
#     print(list_15)

