# class_oop
# 파이썬에서 객체 지향 프로그래밍(OOP) 적용

# 객체 지향 프로그래밍 에서의 클래스 멤버는
# 필드(멤버변수), 메소드(멤버함수), 생성자(constructor), 소멸자(destructor)
# OOP 에 사용되는 기술(3대 특징) 도 적용해야함
# 캡슐화(encapsulation), 상속(inheritance), 다형성(polymorphism) 3가지 기술
# 코드에 반드시 사용되어야 하는 기술임

# oop 적용기술 1 : 캡슐화
# 캡슐화 목적 : 데이터 보호가 목적임. 필드의 접근제한을 둠
# 필드에 접근제한자(access modifier) 를 사용하게 됨
# 접근에 제한을 두는 단어 : public(공개), private(비공개), protected(상속시 후손한테만 공개)
# 파이선에서는 접근제한자가 없음 (제공 안 됨)
# 파이선에서는 기본적으로 모든 멤버는 public 임

# public : 클래스 밖에서 멤버들을 사용할 수 있다는 의미임
# 레퍼런스.필드명, 레퍼런스.메소드명()
# 클래스명.필드명, 클래스명.메소드명(레퍼런스)

# privated : 클래스 밖에서 사용 못 함. 클래스 안에서만 사용할 수 있음
# 캡슐화란, 필드를 비공개 처리하는 것(필수), 메소드는 공개함(선택)
# 파이선에서 클래스 멤버를 비공개(private) 처리하려면,
# 필드명이나 메소드명 이름 앞에 '_'(underscore) 를 2개 붙이면 됨

# class PClass:
#     __num = 10  # private (비공개) 필드임
#
#     def set_num(self, n):
#         self.__num = n
#
#     def get_num(self):
#         return self.__num
#
#
# # 클래스 멤버 사용
# # print('PClass 의 __num 값 확인 : ', PClass.__num)
# pref = PClass()
# # print('pref 를 통한 참조 접근 : ', pref.__num)
# print('인스턴스 안의 __num 값 : ', pref.get_num())

# 생성자 (Constructor)
# 객체 인스턴스가 메모리에 할당될 때, 필드값 초기화가 목적인 함수임
# 생성자를 작성하지 않으면, 내부에서 기본생성자가 작동됨
# 생성자를 작성한다면, __init__ 로 정의해야 함
# 파이썬에서는 생성자 오버로딩(overloading) 할 수 없음 중복불가

'''
def __init__(self, 매개변수):
    self.필드명 = 매개변수

생성자 사용 :
레퍼런스 = 클래스명(전달값) 
'''

# 소멸자 함수 (Destructor)
# 객체가 소멸될 때(인스턴스가 메모리에서 제거될 때) 자동 실행되는 함수임
# 클래스 안에 직접 작성한다면, __del__ 로 정의함
# 해당 객체 관련 메모리나 자원들의 공유 설정, 점유 설정 등을 헤제할 때

'''
def __del__(self):
        소멸시 처리내용 코드 작성
'''


class Var:
    __num = 100

    def __init__(self, n):
        self.__num = n  # 객체가 메모리에 할당(생성)될 때 값 바꿈

    def __del__(self):
        print('인스턴스 메모리에서 제거됨.', id(self))

    def get_num(self):
        return self.__num

    def set_num(self, n):
        self.__num = n


# 클래스 객체생성
v1 = Var(77)
v2 = Var(88)

print('v1 : ', v1.get_num())
print('v2 : ', v2.get_num())

# 키보드 입력으로 필드값 변경시
v1.set_num(int(input('v1이 참조하는 인스턴스의 변경할 필드값 : ')))
print('v1 : ', v1.get_num())
v2.set_num(int(input('v1이 참조하는 인스턴스의 변경할 필드값 : ')))
print('v2 : ', v2.get_num())

# 정적 메소드 (static method) ----------------
# 프로그램 실행시 정적 메모리에 따로 기록되는 메소드
# 정적 메모리(static) 에 로딩된 소스 코드들이 기록됨 (method area)
# 일반적으로 stack 에 기록되는데 정적메소드는 정적 메모리에 기록됨
# 클래스영역 (클래스 이름공간) 이라고도 함
# 메소드 작성시 메소드 이름 위에 장식자(decorator)를 표시하면 됨
# @staticmethod
# 객체 인스턴스와 분리됨 => self 가 없는 메소드임

class C:
    def ham(self, x, y): # 동적 메모리 할당됨. self 매개변수 있음
        print('instance method : ', x, y) # 주소로 객체와 연결됨

class D:
    @staticmethod
    def spam(x, y): # 정적 메모리에 할당됨. self 가 없음
        print('static | class method : ', x, y)
    # 정적 메모리와 동적 메모리 간에는 주소 참조 못 함

# static method 는 사용시 객체레퍼런스(인스턴스의 주소) 없이 실행함
# 클래스명.메소드(전달값, 전달값)
D.spam(10, 20)
dref = D()
dref.spam(10, 20) # static method 는 instance method 처럼 사용해도 됨

# instance method 이용
ref = C()
ref.ham(11,22)
C.ham(ref, 11, 22)

# 연산자 오버로딩 (operator overloading)
# 오버로딩 : 중복 작성(정의), 같은 기능을 여러 번 만드는 것
# 연산자 : 값 계산에 사용되는 기호 문자
# c++, python 에서는 기존 값 계산에 사용되는 연산자에다가
# 클래스 객체에 대한 연산으로 새로운 의미를 정의하는 것
'''
객체 + 값 : __add__(self, value): return self.속성 + value
객체 - 값 : __sub__(self, value): return self.속성 - value
객체 * 값 : __mul__(self, value): return self.속성 * value
객체 / 값 : __truediv__(self, value): return self.속성 / value
객체 > 값 : __gt__(self, value): return self.속성 > value
객체 >= 값 : __ge__(self, value): return self.속성 >= value
객체 < 값 : __lt__(self, value): return self.속성 < value
객체 <= 값 : __le__(self, value): return self.속성 <= value
객체 == 값 : __eq__(self, value): return self.속성 == value
객체 != 값 : __ne__(self, value): return self.속성 != value

'''
# 시퀀스나 맵 타입으로 오버로딩할 수도 있음
class OOP:
    __num = 0
    def __init__(self, num):
        self.__num = num

    # + 연산자 메소드 오버로딩 작성
    def __add__(self, other):
        return self.__num + other

    # - 연산자 메소드 오버로딩 작성
    def __sub__(self, other):
        return self.__num - other

    # - 연산자 메소드 오버로딩 작성
    def __mul__(self, other):
        return self.__num * other

    # - 연산자 메소드 오버로딩 작성
    def __truediv__(self, other):
        return self.__num / other

    def get_num(self):
        return self.__num

# 클래스 객체 생성과 연산자 확인
ref = OOP(100)
print('ref -> __num : ', ref.get_num())
# 오버로딩된 연산자 메소드 사용 : 일반 연산자 사용함
print('+ 30 : ', ref + 30)#130
print('- 30 : ', ref - 30)#100
print('* 3 : ', ref * 3)#300
print('/ 3 : ', ref / 3)#100