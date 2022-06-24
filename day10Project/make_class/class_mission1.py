# class_mission1.py
# 클래스 실습문제 1

class Book:
    __title = '제목없음'
    __author = '작자미상'
    __price = 0
    __tex = 0.05

    def __init__(self):
        print('생성자 실행됨.')
    def __del__(self):
        print('인스턴스 메모리에서 제거됨',id(self))

    def info(self):
        #return f'제목 : {self.__title}, 작가 : {self.__author}, 가격 : {self.__price}, 할인율 : {self.__tex}'
        #return '제목 : %s, 작가 : %s, 가격 : %d, 할인율 : %f' %(self.__title, self.__author, self.__price, self.__tex)
        return '제목 : {}, 작가 : {}, 가격 : {}, 할인율 : {}'.format(self.__title, self.__author, self.__price, self.__tex)
    def set_title(self, n):
        self.__title = n
    def get_title(self):
        return self.__title
    def set_author(self, n):
        self.__author = n
    def get_author(self):
        return self.__author
    def set_price(self, n):
        self.__price = n
    def get_price(self):
        return self.__price
    def set_tex(self, n):
        self.__tex = n
    def get_tex(self):
        return self.__tex

b1 = Book()
b1.set_title('전1시')
b1.set_author('고속도루')
b1.set_tex(0.06)
b1.set_price(5000)
print(b1.info())
print('도서금액 = ',b1.get_price() + b1.get_price() * b1.get_tex())