# except_sample.py
# 파이썬에서의 예외처리 (exception handling)
'''
예외 : 소스 코드로 해결할 수 있는 에러
에러의 종류
    - 시스템 에러 : 소스 코드로 해결 못 하는 에러임
            메모리 부족, 하드디스크(저장장치) 용량 부족, 배터리 양 부족
    - 구문(문법) 에러 : 잘못 작성된 경우의 에러임
            개발툰 IDE 에서 자동 검사함, 구문 수정해서 해결함
    - 런타임 에러 : 실행시 발생하는 에러 run time
            에러 발생이 되면 코드를 수정해서 해결함 = 예외 처리함
에러 처리 방법 :
    - if 조건문으로 에러 상황을 예측해서 미리 막음
        => 예외상황을 처리하는 별도의 구문이 있음
        => 예외 처리 구문 사용을 권장함
'''

def test_error():
    # 에러 발생 예시
    # print('exception # SyntaxError: invalid syntax 구문오류

    # a = 10
    # b = 0
    # c = a / b # ZeroDivisionError: division by zero, 실행시 확인되는 에러
    # Runtime Error(런타임 에러)

    # 4 + new * 3 # 구문 에러, nameError: name 'new' is not defined

    lst = [1, 2]
    # print(lst[2]) # IndexError: list index out of range, 런타임 에러

    dct = {'a': 100,'b': 200}
    # print(dct['c']) # KeyError: 'c', 런타임 에러

# 런타임 에러 중에 사용자가 입력값을 잘못 입력하는 경우
def test_input_error():
    # num = int(input('정수를 입력하세요 : '))    # ValueError
    # if 문으로 처리할 수 없는 에러 상황 발생하였음
    #   => 예외처리 구문으로 해결

    # 해결방법 1 : 입력시 조건문을 적용
    num = input('정수를 입력하세요 : ')
    if num.isdecimal(): # 정수 십진수냐?
        num = int(num)
        print(num, type(num))
    else:
        print('정수만 입력해야 됩니다. 다시 입력하세요.')

# 예외 처리 방법 2 : 예외 처리 전용 구문으로 작성
# try ~ except 문을 사용함 (자바의 try ~ catch 문과 같음)
'''
try:
    에러 발생 가능성이 있는 구문 또는 일반 구문
except:
    에러 발생했을 때 실행할 구문
'''
def test_input_error2():
    num = input('정수를 입력하세요 : ')
    try:
        num = int(num) # 에러 발생 가능성이 있는 구문
        print(num, type(num))
    except:
        print('정수만 입력해야 됩니다. 다시 입력하세요.')

# 예외 처리시 except: 에 pass 를 사용하면
# 오류 발생시 프로그램이 멈추지 않고 계속 동작되게 할 수 있음
def except_pass():
    lst = ['3', '예외처리', 4, 2, 67.5, 'python']
    digit_num = []
    digit_num2 = []
    print(lst)
    # lst 에서 숫자만 골라내서 digit_num 에 기록 저장 처리
    for idx in range(len(lst)):
        try:
            digit_num.append(int(lst[idx]))
        except:
            pass
    for item in lst:
        try:
            digit_num2.append(int(item))
        except:
            pass
    print(digit_num)
    print(digit_num2)

def except_pass2():
    lst = ['3', '예외처리', 4, 2, 67.5, 'python']
    digit_num = []
    digit_num2 = []
    a = 1

    print(lst)
    # lst 에서 숫자만 골라내서 digit_num 에 기록 저장 처리
    for idx in range(len(lst)):

        if(is_digit(str(lst[idx]))): # isdecimal() - 문자형 값에 적용하는 함수임
            digit_num.append(int(lst[idx]))

        else:
            continue

    print(digit_num)


def except_pass3():
    lst = ['3', '예외처리', 4, 2, 67.5, 'python', '67.12.5', 'NaN']
    digit_num = []

    print(lst)
    # lst 에서 숫자만 골라내서 digit_num 에 기록 저장 처리
    for item in lst:
        print(str(item).replace('.','',1))
        result = str(item).replace('.','',1).isdigit()
        if result:
            digit_num.append(int(item))

    print(digit_num)

def is_digit(str): #가장 직관적으로 처리할 수 있는 방법은 정규표현식을 이용하는 방법
    try:        #근대이거 try except쓰는데 ㅋㅋ?
        tmp = float(str)
        return True
    except ValueError:
        return False

# finally : 예외 발생 상관없이 반드시 실행할 코드를 작성하는 영역임
import math # 수학 관련 함수들을 제공하는 모듈임
def test_finally():
    # 원의 반지를을 실수형으로 입력 받음
    try:
        radius = float(input('반지름 : '))
    except: # 에러가 발생했을 때 처리할 구문 작성 영역
        print('숫자만 입력해야 합니다.')
    else:   #에러가 발생하지 않았을 때의 구문 작성 영역
        print('반지름 : ', radius)
        print(f'원의 면적 : {math.pi * radius ** 2}')
        print(f'원의 둘레 : {2 * math.pi * radius}')
    finally: # 반드시 실행되어야 되는 구문 작성 영역
        # 예외 처리 구문 가장 마지막에 작성성
        print('예외처리 구문을 종료합니다.')

# try 구동 -> 에러발생 -> except -> finally
# try 구동 -> 정상처리 -> else -> finally

# 파이선에서의 예외 처리 구문 조합 형태
# try: ~ except ~
# try: ~ except ~ else: ~
# try: ~ except ~ finally: ~
# try: ~ except ~ else: ~ finally: ~
# try: ~ finally: ~
# try: ~ else: ~ => 이건에러 잘못작성됨

# try 쪽에서 여러 경우에 대한 에러가 발생할 때
# except: 구문은 모든 종류의 에러를 다 처리하는 경우에 사용함
# 에러를 종류별로 따로 처리를 하고자 한다면
# except 에러 종류이름: 또는 except 에러클래스명 as 변수명:

def multi_except():
    try:
        # print(3 / 0)
        lst = []
        print(lst[0])
    except ZeroDivisionError:   # 나누기 0한 경우의 에러만 받아서 처리함
        print('0으로 나눌 수 없습니다.')
    except Exception as msg: # 모든 에러를 처리할 수 있는 클래스임
        print('에러가 발생했습니다.')
        print(msg)

# except 예외클래스명: 사용시 주의사항
# except 에 사용되는 예외클래스는 상속 계층 구조에 따라 사용해야 함
# 선조(super)클래스: Except > ArithmeticError > ZeroDivisonError : 훈솔
# 후손부터 먼저 작성해야 함. 선조는 후손 다음에 작성해야함

def multi_except2():
    try:
        # print(3 / 0)
        # print('2' + 2)
        lst = []
        print(lst[0])
    except ZeroDivisionError:
        print('0 나누기 못 함')
    except TypeError:
        print('계산식 오류 발생')
    except Exception as msg:
        print('에러 발생 : ', msg)
# 예외 처리 구문 총 정리
def try_except():
    lst = ['34', 'Hello', '4', 2, 47, 'apple']
    try:
        idx = int(input('조회할 순번 입력 : ')) # 정수가 아닌 값 입력시 에러 발생
        print(f'{idx} 번째 요소는 {lst[idx]} 이다.') # 없는 순번에 대한 에러 발생
    except IndexError as msg:
        print('잘못된 인덱스입니다.', msg)
    except ValueError as msg:
        print('숫자만 입력해야 됩니다.', msg)
    except Exception as msg:
        print('에러 발생 : ',msg)
    else:
        print('try 쪽 구문들이 정상 실행되었음')
    finally:
        print('다중 예외 처리 테스트 종료.')


# 함수실행
if __name__  == '__main__':
    # test_error()
    # test_input_error()
    # test_input_error2()
    # except_pass2()
    # test_finally()
    # except_pass3()
    # multi_except()
    multi_except2()