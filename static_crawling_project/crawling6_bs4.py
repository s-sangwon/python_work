# crawling5_bs4.py
# 네이버 영화 상영 정보 제공 페이지에서
# 상영순위, 제목, 평점, 관람가능나이 를 추출해서
# Movie 클래스에 대한 객체(instance)에 저장한 다음에
# 각 객체를 데이터베이스 movie 테이블에 저장한(insert) 다음
# select 조회로 출력 확인 테스트

import Movie as mv
import bs4, urllib.request
import common.oracle_db as oradb

if __name__ == '__main__':
    oradb.oracle_init()
    conn = ''
    cursor = ''
    try:
        web_page = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
        result_code = bs4.BeautifulSoup(web_page, 'html.parser')


        find_info = result_code.find(class_="lst_detail_t1")
        movie_list = find_info.find_all("li")
    # 영화 목록별로 추출 : ul > li
    # 태그 엘리먼트 여러개 추출

        conn = oradb.connect()
        cursor = conn.cursor()

        query = "insert into movie values(:1, :2, :3, :4)"

        print(len(movie_list)) # 추출한 li 태그 갯수 확인

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
            ref = mv.Movie(movie_title,point,age_grade,rank)
            print(ref)

            # 쿼리문에 반영 : 튜플 만들기
            tp_value = (movie_title,point,age_grade,rank)
            cursor.execute(query, tp_value)
            oradb.commit(conn)
    # db 에 기록 저장 끝 -----------------------------

    # 저장 확인을 위해 db 에서 select 조회해서 출력 처리
        resultset = cursor.execute('select * from moive').fetchall()

        for row in resultset:
            print(row) # 행 단위로 출력


    except Exception as msg:
        oradb.rollback(conn)
        print(conn)
        print('네이버 영화 크롤링 분석 관련 에러 : ', msg)
    finally:
        cursor.close()
        oradb.close(conn)
