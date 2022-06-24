
# loopMission.py

# 리스트의 안의 튜플아이템의 값들에 대해
# 둘 중의 큰값과 작은값을 분류해서 출력처리
def practice1():
    nlist = [(12, 45), (90, 32), (56, 19)]
    #for 문 안에 if else 문 사용
    for (x,y) in nlist:
        if x > y:
            max = x
            min = y
        else:
            max = y
            min = x
        print(f'큰값 : {max}, 작은값 : {min}')
def practice11():
    nlist = [(12, 45), (90, 32), (56, 19)]
    for a in nlist:
        ma = max(a)
        mi = min(a)
        print(f'큰값 : {ma}, 작은값 : {mi}')
def practice2():
    nlist = [(12, 45), (90, 32), (56, 19)]
    #for 문 안에 if else 문 사용
    for (x,y) in nlist:
        tmax = max(x,y)
        tmin = min(x,y)

        print(f'큰값 : {tmax}, 작은값 : {tmin}')

# 활용 실습
# 리스트 안의군집아이템들이 가진 값들 중 각각 가장 큰 값을 골라 내서
# 별도의 리스트에 저장 처리하고 출력 확인
def practice3():
    lists = [[43, 1, 20], (22, 41, 10, 73), {12, 32, 45, 3, 9}]
    max_list = []

    for item in lists:
        if set == type(item):
            slist = list(item)
            max = slist[0]
        else:
            max = item[0]
        for a in item:
            #print(a)
            if max < a:
                max = a
        max_list.append(max)
    print(max_list)

def practice4():
    lists = [[43, 1, 20], (22, 41, 10, 73), {12, 32, 45, 3, 9}]
    max_list = []

    for item in lists:
        print(item, type(item))
        max_list.append(max(item))
    print(max_list)


def practice_while():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
    i=0
    while i<3:
        if sungjuk_list[i][2] >= 60:
            print('{}번 {} 학생은 합격입니다.'.format(sungjuk_list[i][0], sungjuk_list[i][1]))
        else:
            print('{}번 {} 학생은 불합격입니다.'.format(sungjuk_list[i][0], sungjuk_list[i][1]))
        i += 1

# 2; for 문 안에 continue를 사용해서 합격정보만 출력도게 처리하시오
def practice_continue():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

    for student in sungjuk_list:
        if (student[2] >=60 ):
            print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1]))
        else:
            continue

# 3. while 문 안에 continue 를 사용해서 합격정보만 출력되게
def practice_continue2():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

    i = 0
    while i < len(sungjuk_list):

        if sungjuk_list[i][2] >= 60:
            print('{}번 {} 학생은 합격입니다.'.format(sungjuk_list[i][0], sungjuk_list[i][1]))
        else:
            i += 1
            continue
        i += 1
            #print('{}번 {} 학생은 불합격입니다.'.format(sungjuk_list[i][0], sungjuk_list[i][1]))

def practice_short_if():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

    for student in sungjuk_list:
        #print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1])) if student[2] >= 60 else print('{}번 {} 학생은 불합격입니다.'.format(student[0], student[1]))
        print(f'{student[0]}번 {student[1]} 학생은 합격입니다.' if student[2] >= 60 else f'{student[0]}번 {student[1]} 학생은 불합격입니다.')


    # -----------------------------------------------------------------

import random

# 랜덤 : 임의의 숫자(랜덤값)를 발생시키고자 할 때
# random 모듈이 제공하는 함수를 사용할 수 있다

def test_random():
    print('임의의 랜던값 : ', random.random())
    # 0.0 <= 랜덤값 < 1.0 범위의 임의의 실수형 숫자

    print('랜덤값 확인 : ', random.randrange(1,11))
    # start <= 랜덤값 < end 범위의 임의의 정수형 숫자가 발생함

def display_lotto():
    #print('랜덤값 확인 : ', random.randrange(1, 46))
    loto = set()

    while (len(loto)<6):
        rd = random.randrange(1, 46)
        loto.add(rd)

    loto_list = list(loto)
    loto_list.sort()
    print(loto_list)










