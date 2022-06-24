# loopMission.py
# 반복문 실습문제


'''
    키보드로 문자열을 입력받아서, 요구대로 처리하고 출력되게 하시오.
    실행 :
            문자열 입력 : apple (value : str)

    처리내용 :
        for 문 사용 : 글자의 유니코드 출력이 반복되게 함
    출력 :
            a is unicode 97

'''

def practice1():
    value = input('문자열 입력 : ')

    for ch in value:
        print(f'{ch} is unicode {ord(ch)}')

# for in 문, range() 실습문제
'''
키보드로 구구단의 단수를 입력받아서, 해당 단의 구구단을 출력하시오.
입력 내용 :
    단수 : 3 (dan : int)
출력 내용 :
    3 * 1 = 3
    3 * 2 = 6
    ...
'''

def print_99dan():
    dan = int(input('단수 : '))

    for i in range(1,10):
        print(f'{dan} * {i} = {dan * i}')
