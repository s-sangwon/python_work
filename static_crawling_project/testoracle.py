import cx_Oracle
import urllib.request, Movie as mv, bs4


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

    # Movie 인스턴스 저장용 리스트
    instance_list = []


    for idx in range(0, len(movie_list)):
        movie_title = movie_list[idx].find(class_="tit").find('a').text
        point = movie_list[idx].find(class_="star_t1").find(class_="num").text
        rank = idx + 1
        age_grade = ''

        if movie_list[idx].find(class_='tit').find('span', class_='ico_rating_15'):
            age_grade = '15'
        elif movie_list[idx].find(class_='tit').find('span', class_='ico_rating_12'):
            age_grade = '12'
        elif movie_list[idx].find(class_='tit').find('span', class_='ico_rating_all'):
            age_grade = 'all'
        # Movie 객체 생성하면서, 초기값 전달 기록 처리
        # 파이썬 클래스 객체 생성 : 객체참조변수 = 모듈명.생성자(초기값,...)
        instance_list.append(mv.Movie(movie_title,point,age_grade,rank))


    cx_Oracle.init_oracle_client("C:\instantclient_21_6")

    conn = cx_Oracle.connect("c##student/student@localhost:1521/xe")

    print(conn)

    query = "insert into movie values(:1, :2, :3, :4)"

    cursor = conn.cursor()

    for instance in instance_list:
        print(instance)

    for instance in instance_list:
        cursor.execute(query, instance.return_tuple())
    conn.commit()
    cursor.close()
    conn.close()
