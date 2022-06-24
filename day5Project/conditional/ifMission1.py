# ifMission1.py
# if 문 실습문제

def practice():
    num1 = int(input('첫번쨰 정수 : '))
    num2 = int(input('두번쨰 정수 : '))

    #if 0< num1 and 0 < num2:
    
    if (0 < num1 and 0 < num2):
        print(f'합 = {num1 + num2}, 차 = {num1 - num2}, 곱 = {num1 * num2}, 몫 = {num1 // num2}, 나머지 = {num1 % num2}')
