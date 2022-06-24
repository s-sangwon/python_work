# sample_module.py
# 파이썬에서 모듈 만들어서 사용하기

# 모듈(module) : 파이썬 소스 파일(파일명.py) 이다.
# 파일명이 모듈명이 됨
# 모듈용 소스파일에는 함수와 변수가 저장되면 됨
# 모듈이 제공하는 함수와 변수를 사용하려면, import 모듈명 선언하면 됨
# import 후에 모듈명.함수명() 또는 모듈명.변수명 으로 사용하면 됨
#import pickle
#import keyword

# keyword.py 파일

# print(kwlist)  # 예약어 리스트 출력

# 모듈은 다른 파이선 파일에서 사용할 수 있도록 함수(기능)와 변수(값)들을
# 따로 저장해서 제고하는 목적의 소스파일

# 모듈 임포트시에 모듈명에 대한 줄임말을 같이 선언할 수 있다.
# import 모듈명 as 줄임말                  as(alias)
import keyword as k

print(k.kwlist)
print(k.__file__) # 해당 모듈(파일)의 위치가 출력됨

# 모듈 활용법 확인 help('모듈이름')
# noinspection PyArgumentList

#help('math')

# 파이썬이 제공하는 표준 모듈들 ------------
import os

print(os.getcwd())

import time

print(time.localtime()) # 현재 날짜와 시간정보 출력
time.sleep(1) # 1초 멈춤
print(time.localtime())

import random # 임의의 숫자를 발생시키는 기능 제공

print(random.random()) # 0.0 <= 임의의 난수 < 1.0
print(random.randint(1,5)) # 1<= 임의의 정수 < 5
print(random.randrange(1, 10, 2)) # 1<= 2간격의 정수 하나 < 10
# 1 3 5 7 9 중의 하나

import math  # 수학과녈ㄴ기능

#print(f'원주율 : {math.pi:0.99f}')
print('5! : ', math.factorial(5))

import calendar

calendar.prmonth(2021, 11) # 해당 년, 월의 달력 출력
# B = True
# result = 4
# i = 4.0
# j = 3
# while True:
#
#     if B:
#         result -= 4 / j
#         B = False
#     else:
#         result += 4 / j
#         B = True
#
#     j += 2
#     print(f'{result:0.999f}')

#-------------------------------
# 사용자 모듈 사용하기
import mymodule as my

print('더하기 : ', my.sum(10,20))
print('빼기 : ', my.sub(15,7))
print('곱하기 : ', my.mul(15,3))
print('나누기한 몫 : ', my.divide(12,3))
try:
    print('나누기한 몫 : ', my.divide(12,0))
except Exception as msg:
    print(msg)
    pass
print('나누기한 나머지 : ', my.mod(12,7))
try:
    print('나누기한 나머지 : ', my.mod(a=12,b=0))
except Exception as msg:
    print(msg)
    pass
print('가장 큰 값 : ', my.max())
print('가장 큰 값 : ', my.max(10))
print('가장 큰 값 : ', my.max(1,2,3,4,5,6,7,8,9))
print('가장 작은 값 : ', my.min())
print('가장 작은 값 : ', my.min(10))
print('가장 작은 값 : ', my.min(1,2,3,4,5,6,7,8,9))
print('글자 갯수 : ', my.strlen())
print('글자 갯수 : ', my.strlen('module test'))
print('원주율 : ', my.pi)
print('카운트 : ', my.count)

# __name__ : 현재 실행되고 있는 모듈 이름 확인할 때 사용함
print(__name__)
# 프로그램을 실행하면, 기본 파일은 main 모듈이 됨
# 다르게 표현하면, main 만 실행할 수 있다는 의미임

if __name__ == '__main__':
    print('이 파일(모듈)이 직접 실행이 되면, 자동 메인이 됨')

# 파이썬에서는 소스파일을 직접 실행시키면 자동으로 해당 소스파일을
# __main__ 모듈로 설정하는 것을 확인할 수 있음음