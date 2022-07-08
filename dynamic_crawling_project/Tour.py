# Tour.py
# 여행 상품 정보를 담는 클래스
# 상품명, 여행기간, 가격, 썸네일이미지,링크 url, 상품상세정보, 출발가능기간
class TourInfo:
    #field
    __title = ''        #상품명
    __price = ''        #상품가격
    __img = ''        # 썸네일
    __subtitle = ''        # 부제목
    __tperiod = ''        # 여행기간
    __dperiod = ''        # 출발기간
    __content = ''        #

    # constructer
    def __init__(self, title, price, img, link, tperiod, dperiod, content):
        self.__title = title
        self.__price = price
        self.__img = img
        self.__link = link
        self.__tperiod = tperiod
        self.__dperiod = dperiod
        self.__content = content

    # 연산자 오버로딩 메소드
    # 객체가 가진 필드값들을 하나의 문장 만들어서 리턴

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}'.format(\
            self.__title, self.__price, self.__img, self.__subtitle,
                self.__tperiod, self.__dperiod, self.__content)

    # getter 메소드 : 필드값 리턴
    def get_title(self):
        return self.__title
    def get_price(self):
        return self.__price
    def get_img(self):
        return self.__img
    def get_subtitle(self):
        return self.__subtitle
    def get_tperiod(self):
        return self.__tperiod
    def get_dperiod(self):
        return self.__dperiod
    def get_content(self):
        return self.__content

    # setter 메소드 : 새 값 받아서, 필드 값 수정

    def set_title(self, title):
        self.__title=title
    def set_price(self, price):
        self.__price = price
    def set_img(self, img):
        self.__img = img
    def set_subtitle(self, subtitle):
        self.__subtitle = subtitle
    def set_tperiod(self, tp):
        self.__tperiod = tp
    def set_dperiod(self, dp):
        self.__dperiod = dp
    def set_content(self, co):
        self.__content = co


