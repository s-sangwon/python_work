# mission3.py
# 사용자 정의 예외 발생 실습문제

def calc_score(a, b):
    if not((a>=1 and a <=100) and (b>=1 and b<=100)):
        print('if 문 진입')
    if (a <1 or a > 100) or (b < 1 or b > 100):
        print('if 문 진입')
    if not ((1 <= a <= 100) and (1 <= b <= 100)):
        raise Exception('계산할 데이터는 반드시 1이상 100이하의 값이어야 합니다.')

    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a // b}')
    print(f'{a} % {b} = {a % b}')

def test_mission():
    try:
        a = int(input('첫번째 정수를 입력하시오 : '))
        b = int(input('두번째 정수를 입력하시오 : '))
        calc_score(a, b)
    except ValueError as msg:
        print('정수를 입력해야합니다.', msg)
    except Exception as msg:
        print(msg)
    finally:
        print('test_mission 종료')

if __name__ == '__main__':
    test_mission()