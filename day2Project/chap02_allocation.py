# chap02_allocation.py
# 2022-05-27
# developoer : 서상원

'''
파이썬에서의 변수 공간에 값 기록하는 메모리 할당(memory allocation) :
파이썬에서의 변수 할당은 동적 할당임.
동적(실행시 : Run 구동시) 메모리(RAM)에 변수 공간을 만들고
만들어진 변수 공간에 값을 기록하는 것
코드 구문 : 변수이름 = 기록할값 또는 변수이름 = 계산식
주의사항 : 변수명 (= 값 이 없으면 에러임, 할당 안됨
'''

num = 1 + 2
# 계산 결과 3이 num 변수 공간에 기록 할당됨
print('num 변수가 가진 값 : ',num)

# 변수 할당시 = (대입연산자) 사용함
# 대입연산자는 반드시 왼쪽에는 변수를, 오른쪽에는 값 또는 계산식이 위치
# 값 = 변수 : 에러
# 100 = a # error

# 한번에 여러 개의 변수에 값을 할당할 수도 있음
# x = 10
# y = 20
# z = 30
x, y, z = 10, 20, 30
print(x,y,z, sep=' | ') # sep (seperator) : 구분자(구분할 기호)

# 한 개의 값을 여러 변수에 할당할 수도 있음
k = m = n = 77
print('k : ', k, 'm : ', m, 'n : ', n, sep=', ')

# 한 줄에 여러 변수 할다구문을 작성한다면 새미콜론(;)으로 구분함
# num1 = 12
# num2 = 24
num1 = 12; num2 = 24
print('num1 :', num1, ', num2 : ', num2)

# 두 변수 값 교환 가능함
first = 123
second = 345
print('first : ', first, ', second : ', second)

first, second = second, first
print('first : ', first, ', second : ', second)

# = (순수대입연산자)
# 복합대입연산자 : 산술대입연산자가 주로 사용됨
# 산술연산자 : +, -, *, /, **, //, %(mod)
# +=, -=, *=, /=, %=, **=, //=
# 메모리의 변수공간의 값에 직접 연산하므로 연산속도가 빠름 (사용 권장)
value = 10
print('value : ', value)

value += 10 # value = value + 10
print('value : ', value)

value -= 5 # value 변수 방의 값을 5 감소시켜라
# value = value - 5
print('value : ', value)

value *= 2 # value 변수 방의 값을 2배 증가시켜라
# value = value *2
print('value : ', value)

value /= 2 # 15.0 --> 나누기한 몫을 구함, 결과값이 실수형 숫자
print('value : ', value)

value //= 2 # 15 --> 나누기한 몫을 구함, 결과값이 정수형 숫자
print('value : ', value)

value **= 2 # ** : 제곱
print('value : ', value)

value %= 30 # 나머지
print('value : ', value)

# 파이선 코드 문장은 한 줄로 작성이 원칙임
# 문장이 길어서 한 줄 작성이 불편할 경우에는 여러 줄로 나눌 수 있음
# 줄 끝에 반드시 백슬러시(\)를 표시해야 함
print('파이선은 인터프리터 언어이다.\
      , 스크립트 언어이기도 하다.',
      '한 줄로 구문 작성해야한다.')