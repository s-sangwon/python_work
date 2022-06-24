# func_mission1.py
# 함수 만들고 사용하기 실습문제1

# 함수 만들기
def tsum(a, b):
    return a + b
def tsub(a, b):
    return a - b
def tmul(a, b):
    return a * b
def tdiv(a, b):
    return a // b , a % b

def simple_calculator():
    try:
        first = int(input('첫번째 정수 : '))
        second = int(input('두번째 정수 : '))
        print(f'{first} + {second} = {tsum(first, second)}')
        print(f'{first} - {second} = {tsub(first, second)}')
        print(f'{first} * {second} = {tmul(first, second)}')
        print(f'{first} // {second} = {tdiv(first, second)[0]}')
        print(f'{first} % {second} = {tdiv(first, second)[1]}')
    except ValueError as msg:
        print('정수만 입력해!!!!!!!!!!!', msg)
    except ZeroDivisionError as msg:
        print('0으로 못나눠 수학시간에 안배웠어???????', msg)
    except Exception as msg:
        print('처리했는데 몰루는? 예외임 나도 몰?루', msg)
    finally:
        print('끗')

# 함수 호출
if __name__ == '__main__':
    simple_calculator()
