# func_advance.py
# 함수의 활용

# 재귀함수 (재귀적 호출 함수 : Recursive call funtion)
# 함수 안에서 자신을 호출(실행)하는 함수 (반복문과 유사함)
# 무한루프가 되지 않도록 종료 조건을 반드시 기술해야 함
# 파이썬은 무한루프에 빠지면 자동으로 일정구간 반복 후에 에러 발생시킴

#
import math
count=0
list = []
def factorial(n):

    if n == 0:
        return 1
    else:
        print(n, '*', end=' ')
        return n * factorial(n-1)
def fct(n):
    global count, list
    list.append()
    count += 1
    return n*fct(n-1)*fct(n-2) if n > 0 else 1

def fct2(n):
    return 1 if n == 0 else n*fct2(n-1)

lf = lambda n : 1 if n==0 else n * lf(n-1)

if __name__ == '__main__':
    print(fct(10))
    print(count)
    print(list)
    # print(fct2(6))
    # print('\n10! : ', factorial(996))
    # print(lf(997))