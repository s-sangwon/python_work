# mssion.py
# 다중 if 문 실습문제

def practice4():
    name = input('학생이름 : ')
    score = int(input('점수 : '))
    #grade = None 파이썬에서는 필요없음
    if (score >= 90):
        grade = 'A'
    elif (score >= 80):
        grade = 'B'
    elif (score >= 70):
        grade = 'C'
    elif (score >= 60):
        grade = 'D'
    else:
        grade = 'F'
    print(f'{name}의 점수는 {score}이고, 등급은 {grade} 입니다.')

# 중첩nested if 실습문제

def practice5():
    num1 = int(input('첫번째 수 : '))
    num2 = int(input('두번째 수 : '))

    if (num1 > 0 and num2 > 0):
        #if(1 < num1 and num1 < 100 and 1 < num2 and num2 < 100):
        #if(1 < num1 < 100 and 1 < num2 < 100):
        if(num1 < 100 and num2 < 100):
            print(f'합 = {num1 + num2}, 차 = {num1-num2}, 곱 = {num1 * num2}, 몫 = {num1 // num2}, 나머지 = {num1 % num2}')
        else:
            print('1~100 사이의 값만 입력하세요')
    else:
        print('양수만 입력해야 됩니다.')
    print('프로그램이 종료되었습니다.')



