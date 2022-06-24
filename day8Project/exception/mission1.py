# mission1.py
# 예외처리 실습문제 1

def gugudan():
    try:
        dan = int(input('단수를 입력하세요 : '))


    except ValueError as msg:
        print('정수를 입력하세요.', msg)
    except Exception as msg:
        print('예상치 못한 에러 발생', msg)
    else:
        if (dan < 2):
            dan = 2
        elif (dan > 9):
            dan = 9
            
        for i in range(1,10):
            print(f'{dan} * {i} = {dan * i}')
    finally:
        print('예외처리 구문이 종료되었습니다.')


if __name__ == '__main__':
    gugudan()