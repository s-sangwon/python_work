# Movie.py
# 크롤링한 영화 정보 저장용 객체를 위하 클래스 정의 스크립트

class Movie:
    # 멤버변수(field) : private 적용
    __title = ''        # 영화제목
    __star_point = 0    # 평점
    __age_grade = '00'     # 관람가능 제한 나이
    __rank = 0          # 평점 순위
    def get_point(self):
        return self.__star_point
    # 생성자(constructor) : new 할때 자동 작동되는 함수임
    def __init__(self, title, point, age, rank):
        self.__title = title
        self.__rank = rank
        self.__star_point = point
        if age:
            self.__age_grade = age
        else:
            self.__age_grade = '0'

    # 소멸자 생략
    # 멤버함수(method)
    # 연산자 오버로딩(overloading : 중복 정의) 메소드
    # __str__: 자바의 toString() 메소드와 같음
    # 객체가 가진 필드값들을 하나의 문장(str)으로 만들어서 리턴함

    def __str__(self):
        return '{}, {}점, {}세, 개봉순위 : {}위'.format\
            (self.__title, self.__star_point, self.__age_grade, self.__rank)

    def return_tuple(self):
        return (self.__title, self.__star_point, self.__age_grade, self.__rank)
