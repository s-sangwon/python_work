# mission2.py
def calculator():
    try:
        x = int(input('가로크기를 입력하세요 : '))
        y = int(input('세로크기를 입력하세요 : '))
        perimeter = 2 * (x + y)
        area = x * y
        print(f'면적 : {area}, 둘레 : {perimeter}')
    except ValueError as msg:
        print('숫자만 입력해야 합니다.', msg)
    except Exception as msg:
        print('에러발생!', msg)

    finally:
        print('도형 계산 처리 완료')
#===============================================
#else문 추가
def calculator2():
    try:
        x = int(input('가로크기를 입력하세요 : '))
        y = int(input('세로크기를 입력하세요 : '))

    except ValueError as msg:
        print('숫자만 입력해야 합니다.', msg)
    except Exception as msg:
        print('에러발생!', msg)
    else:
        perimeter = 2 * (x + y)
        area = x * y
        print(f'면적 : {area}, 둘레 : {perimeter}')
    finally:
        print('도형 계산 처리 완료')

# 예외를 강제로 발생시키기 ------------------------------
# raise 예외클래스명 또는 raise 예외클래스명('에러메세지')
# 주로 함수나 멤버함수(클래스에 속한 함수 : 메소드) 정의시에 이용
# 코드상 지정하는 조건일 때 에러 발생시키고, 해당 함수 사용에서
# 예외처리하게 함

def ndiv(a, b):
    if b==0:
        raise Exception('0 나누기 못 함')
    else:
        return a / b

# 함수 사용시 예외처리로 작성
def test_raise():
    try:
        # 예외 발생 코드를 가진 함수 사용
        result = ndiv(12, 0)
        print(result)
    except Exception as msg:
        print(msg)
if __name__  == '__main__':
    # calculator2()
    test_raise()