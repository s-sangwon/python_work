# mymodule.py
# 사용자 정의 모듈
# 모듈 표현 : modules.mymodule

# 함수(기능)들과 변수(전역변수)들 작성

# 변수
pi = 3.14159
count = 10

# 함수(기능) -------------------------------

# 두 수를 전달받아서 더하기 결과 리턴
def sum(a, b):
    return a + b

# 두 수를 전달받아서 빼기 결과 리턴
def sub(a, b):
    return a - b
# 두 수를 전달받아서 곱하기 결과 리턴
def mul(a, b):
    return a * b

# 두 수를 전달받아서 나누기한 몫을 리턴
# 단, 나눌 수가 0이면 Exception 발생시킴 : '0으로 나눌 수 없음'
def divide(a, b):
    if b == 0:
        raise Exception('0으로 나눌 수 없음')
    else:
        return a / b

    # try:
    #     if b==0:
    #         raise Exception('0으로 나눌 수 없음')
    # # except ZeroDivisionError as msg:
    # #     print('0으로 나눌 수 없음')
    # except Exception as msg:
    #     print(msg)
    # else:
    #     return a / b

# 두 수를 전달받아서 나누기한 나머지를 리턴
# 단, 나눌 수가 0이면 Exception 발생시킴 : '0으로 나눌 수 없음'
def mod(a, b):
    if b == 0:
        raise Exception('0으로 나눌 수 없음')
    else:
        return a % b

    # try:
    #     if b==0:
    #         raise Exception('0으로 나눌 수 없음')
    # except Exception as msg:
    #     print(msg)
    # else:
    #     return a % b
# 가변매개변수를 사용해서, 전달받은 수들 중 가장 큰 값을 리턴
def max(*l):
    try:
        f = l[0]
        for value in l:
            if f < value:
                f = value
        return f
    except:
        print('처리할 데이터가 없습니다.')

# 가변매개변수를 사용해서, 전달받은 수들 중 가장 작은값을 리턴
def min(*l):
    try:
        f = l[0]
        for value in l:
            if f > value:
                f = value
        return f
    except:
        print('처리할 데이터가 없습니다.')

# 문자열을 전달받아서, 글자 갯수를 리턴
# 기본 매개변수 지정: None 지정
# 매개변수가 None 이면 0리턴
def strlen(s = None):
    if s == None:
        return 0
    count = 0
    for len in s:
        count += 1
    return count

