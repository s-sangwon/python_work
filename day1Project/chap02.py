#식별자 : 프로그래머가 지어주는 이름을 말함
#변수(variable) : 프로그램 구동시 메모리(RAM)에 값 기록하는 공간(방)
#함수(function) : 반복 사용되는 코드의 이름을 정의한것
#모듈(module)   : 함수들을 따로 모아놓은 파일
#클래스(class)  : 파이썬은 객체지향형 스크립트 언어임

# 파이썬의 이름 작성 규칙 (식별자의 조건, Naming Rule)
# 1. 대소문자 구분함 : name != Name
NAME = '홍길동'
name = '이순신'
Name = '황지니'
print(NAME, name, Name)

# 2. 이름의 첫번쨰로 숫자 사용 불가 : 1num(에러)
# 1num = 100
# print(1num) # syntax error

# 3. 이름의 첫글자는 문자 또는 언도스코어(_)만 사용 가능
_score = 100.0
print(_score)

# 4. 숫자는 중간 위치나 뒤에는 사용 가능. : num1, first1_menu
num1 = 10
num2 = 20
print(num1 > num2)

# 5. 언더스코어를 제외한 특수문자나 공백 사용 불가 : $menu, all* 에러!
# num& = 12
# print(num&) # syntax error

# 6. 예약어(프로그램 언어가 별도로 사용하려고 정해놓은 단어들)는 이름으로 사용할 수 없다.
#true = 1 (ok),    True = 1 (에러!)

# 파이썬이 제공하는 예약어 확인
# keyword 모듈에서 제공됨 : import 해서 사용함
import keyword
print(len(keyword.kwlist)) # 36갠대? 왜 33개임?
print(keyword.kwlist)
