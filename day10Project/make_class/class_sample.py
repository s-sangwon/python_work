# class_sample.py
# 파이썬에서 클래스 만들어 사용하기

# 파이썬은 객체지향 스크립트 언어이다.
# 절차지향 프로그래밍이 가능함 : 실행코드 구문이 작성된 순서대로 작동됨
# 객체(Object) 지향(Oriented) 프로그래밍(Programing) : OOP
# 프로그램을 작성해서 구동시킬 때 객체를 사용한다는 의미
# 객체 : 클래스(class)로 만들어지는 메모리 할당 공간임
# 객체 == 인스턴스(instance) 라고도함

# 객채지향 프로그래밍은 클래스 만들기 부터 시작함

'''
class 클래스명:
    멤머변수 = 초기값
    ...
    def 함수명(self, 매개변수, *매개변수):
        필드에 대한 값 처리 내용에 대한 코드 작성
        self.멤버변수 = 변경할값   또는   return self.필드명
* 멤버변수 : 클래스에 속한 변수, 필드(Filed) 라고 함 또는 속성(attribute)
* 초기값 : 첫번째로 기록되는 값, default 값이라고 함
* 멤버함수 : 클래스에 속한 함수, 메소드(Method) 라고 함 또는 기능
        메소드 만들때 반드시 첫번째 매개변수는 self 라고 지정함
*매개변수 self : 자바, c++, c#.net, javascript 의 this 와 같음
        해당 메소드가 실행될 때 참조하는 인스턴스의 주소를 자동으로
        전달받는 매개변수

'''
# 클래스 이름은 첫글자 영문 대문자를 권장함함
class SClass:
    pass # 멤버가 없는 빈 클래스 작성할 수 있음
# 빈 클래스는 실행시 이름공간(namespace)이 할당됨
# 즉, 이름만 있어도 공간이 할당됨

# 클래스 사용 : 객체 생성(메모리에 객체공간(인스턴스) 할당됨)
# 참조변수 = 클래스명()
# 참조변수 (reference) : 객체의 주소를 가진 변수
c1 = SClass() # c1 은 빈 SClass 객체공간을 참조함 (주소를 가짐)
c2 = SClass() # c2 은 빈 SClass 객체공간을 참조함 (주소를 가짐)

print('c1이 가진 주소 : ', c1)
print('c2이 가진 주소 : ', c2)

# 파이썬은 실행할 때 (동적으로) 멤버변수(필드)를 추가할 수 있음
# 레퍼런스.변수명 = 기록할 값
c1.a = 10 # c1이 참조하는 인스턴스 안에 a를 추가하고 10 기록함
c1.sum = lambda  x, y:x+y
print('c1 이 참조하는 객체안의 a 필드가 가진 값 : ', c1.a)
# print('c2 이 참조하는 객체안의 a 필드가 가진 값 : ', c2.a) # error

# 파이선에서의 변수 종류

a = 1 # 전역변수 (global variable : 함수 밖에서 선언된 변수

def func():
    a = 3 # local variable 지역변수 : 함수 안에서 선언된 변수
    print('a : ', a) # a : 3 출력

class SS:
    a = 2 # 멤버변수 (field == attribute) : 클래스 안에 선언된 변수

print('a : ', a) # a : 1 출력
func() # 함수 실행시 함수 안의 지역변수 사용
print('SS.a : ', SS.a) # 클래스가 가진 속성 a 출력

s1 = SS()
print('s1.a : ', s1.a) # 객체공간(인스턴스) 안에 있는 속성 a 출력

# 클래스 만들고 멤버(필드, 메소드) 구성하기 --------------------------
class MyClass:
    # field(atrribute) : self.필드명 = 초기값
    value = 0 # 필드 선언시 self 는 생략

    # method 정의 : 정의방식은 일반함수와 같은
    # 다른 점은 첫번째 매개변수가 반드시 self 표기함
    def get_value(self):
        # self : 참조변수가 가진 주소를 자동으로 저낟ㄹ받음
        print('self가 받은 주소', id(self))
        return self.value # 필드 사용시에는 반드시 self.필드명 으로 작성
        # 주소 안의 value 값 리턴 처리

    def set_value(self, v): # setter라고함
        self.value = v # 주소 위치의 필드값을 변경 처리

    def increment_value(self):
        # value 필드 값을 1 증가시키는 메소드
        self.value += 1 # 메소드를 이용 : self.set_value)value(self.get_value() + 1 )
        #메소드 안에서 필드나 메소드 사용시에는 반드시
        #self.필드명, self(메소드명) 으로 selfl


# 클래스의 사용 1 ----------------------------
# MyClass 에 대한 객체(인스턴스) 생성 : 참조변수 = 클래스면()
ref = MyClass()
print('ref의 주소', id('idb'))

print('인스턴스 안 필드 값 확인 : ', ref.value)
print('인스턴스 안 필드 값 확인 : ', ref.get_value())

ref.set_value(20)
print('인스턴스 안 필드 값 확인 : ', ref.value)
print('인스턴스 안 필드 값 확인 : ', ref.get_value())

# 클래스의 메소드 사용2
# 레퍼런스가 아닌 클래스명으로 메소드를 실행할 수도 있음
# 레퍼런스.메소드() 실행시, 레퍼런스가 가진 주소를 self 가 자동 전달받음
# 클래스명 메소드() 실행시에는 메소드 안의 self가 받을 주소가 없게 됨
# 이 경우에는 메소드(주소) 방식으로 객체의 주소를 직접 전달해야 됨

MyClass.set_value(ref,345)
print('인스턴스 안 필드 값 확인 : ', ref.value)
print('인스턴스 안 필드 값 확인 : ', ref.get_value())
print('인스턴스 안 필드 값 확인 : ', MyClass.get_value(ref))

ref.increment_value() # 메소드의 self 는 ref 의 주소를 자동 전달받음
print('인스턴스 안 필드 값 확인 : ', ref.value)
print('인스턴스 안 필드 값 확인 : ', ref.get_value())
print('인스턴스 안 필드 값 확인 : ', MyClass.get_value(ref))

MyClass.increment_value(ref)    #self 로 주소 직접 전달함
print('인스턴스 안 필드 값 확인 : ', ref.value)
print('인스턴스 안 필드 값 확인 : ', ref.get_value())
print('인스턴스 안 필드 값 확인 : ', MyClass.get_value(ref))
