# adv_funtion\\func_sample.py
# adv_funtion.func_sample
# 파이썬 함수 만들기(정의)와 함수 사용(call)

# 매개변수(parameter)와 전달인자(argument) 관계
# 매개변수 : 함수 실행(호출)시 전달값을 받는 변수
#       함수 실행시 전달값에 따라 자료형이 결정됨
# 전달인자 : 함수쪽으로 전다로디는 값 또는 주소
#          함수명(전달값, 전달값, 전달객체, ...)
# 주의 : 함수 사용시 매개변수 갯수와 전달인자의 갯수가 반드시 일치해야 함
def tmax(a, b):
    '두 개의 값을 전달받아서, 둘 중 큰 값을 알아내서 리턴 처리함'
    print(f'a : {a}, b : {b}, type : {type(a)}, {type(b)}')
    try:
        return a if a>b else b
    except TypeError as msg:
        print('같은 타입만 비교가능함', msg)

def func_param_args():
    '매개변수와 전달인자 갯수 맞추기 테스트용 함수'
    print('큰값 : ', tmax(10, 20))
    print('큰값 : ', tmax(44.6, 12.3))
    print('큰값 : ', tmax('M', 'm'))
    # result = tmax(123) # 에러 발생 : 전달값과 매개변수 갯수가 다름
    # result = tmax(10, 20, 30)

# ----------------------------------------------------------
def tmax2(a, b):
    '두 개의 값을 전달받아서, 둘 중 큰 값을 알아내서 리턴 처리함'
    print(f'a : {a}, b : {b}, type : {type(a)}, {type(b)}')
    try:
        max_value =  a if a>b else b
    except TypeError as msg:
        print('같은 타입만 비교가능함', msg)
    a = 100 # 매개변수가 받은 값 변경
    b = 200
    print(f'a : {a}, b : {b}, type : {type(a)}, {type(b)}') # 변경 확인
    return max_value

def func_call_value():
    ' 함수로 값 전달 확인용 함수'
    num1 = 10
    num2 = 20
    print(f'num1 : {num1}, num2 : {num2}')
    result = tmax2(num1, num2)
    print(f'큰값 : {result}')
    # 함수쪽에서 변경한 값이 호출부의 변수에 영향을 줬는지 확인
    print(f'num1 : {num1}, num2 : {num2}')
#--------------------------------------------------------
# 파이썬에서는 군집자료형을 전달받는 매개변수는 기본으로 주소를 받음
def list_in_max(plist):
    '리스트 객체를 전달받아서, 저장된 값중에 가장 큰값 리턴'
    print(f'plist : {plist}, 주소 : {id(plist)}')
    max_value = max = plist[0] # 첫번째 값을 변수에 저장
    for item in plist:
        if max_value < item:
            max_value = item
    # 파이썬에서는 전달받은 객체의 요소는 변경할 수 있음
    max = [value for value in plist if max<value]
    plist[0] = 100
    print(f'plist : {plist}, 주소 : {id(plist)}')
    return max_value, max[-1]

def func_call_reference():
    nlist = [45, 1, 33, 12, 90, 123, 7]
    print(f'nlist : {nlist}, 주소 : {id(nlist)}') # 함수 실행전 확인
    result = list_in_max(nlist)
    print(f'가장 큰 값 : {result}') # 함수 실행후 확인
    print(f'nlist : {nlist}')

# ------------------------------------------------

# 기본default 매개변수 : 기본값(default)을 가진 매개변수
# 함수 만들 때 매개변수에 기본값을 지정할 수 있음
# def 함수면(매개변수=기본값, 매개변수=기본값):
# 뒤쪽 매개변수부터 기본값을 지정해야 함 :
# def 함수명(매개변수, 매개변수=기본값):
# 뒤부터 줘야함 아니면 다주던가 아래형식은 에러.
# 에러 주의 : def 함수명(매개변수 = 기본값, 매개변수)
# 에러 주의 : def 함수명(매개변수, 매개변수=기본값, 매개변수)

# 함수 실행시 기본 매개변수에 전달값 생략할 수 있음
# 전달값이 없으면 준비된 기본값을 사용함
# def tmin(a, b, c = 0):
# def tmin(a, b = 0, c = 0):
def tmin(a=0, b=0, c=0):
    '세 개의 값을 전달받아서, 가장 작은값을 찾아서 리턴하는 함수'
    print(f'a : {a}, b : {b}, c : {c}')
    return a if a<b and a<c else b if b<c else c

def func_default_param():
    # 사용할 함수가 기본값이 없는 매개변수이면, 갯수 맞춰야함
    print(f'가장 작은 값 : {tmin(12, 3, 90)}') #개
    # 전달값 갯수 맞지않으면 에러
    print(f'가장 작은 값 : {tmin(12, 3)}')
    print(f'가장 작은 값 : {tmin(12)}')
    print(f'가장 작은 값 : {tmin()}') # 전달값 0개
# -------------------------------------------------------------

# 키워드 매개변수
# 함수 사용할 때(함수 호출시) 매개변수=전달값 의 형태를 사용할 수 있음
# 함수명(매개변수명=전달값)
# 순서상관 x
def num_calc(a, b, c, d, e):
    return (a + b - c * d / e)

def func_keyword_call():
    result = num_calc(10, 9, 8, 7, 6) # 10 + 9 - 8 * 7 / 6
    print('result : ', result)
    result = num_calc(c=8, b=9, e=6, a=10, d=7)
    print('result : ', result)
#-----------------------------------------------------

# 가변 매개변수 : 전달받을 값의 갯수를 정하지 않는 매개변수임
# 함수 만들 때 매개변수 이름 앞에 * 표시함
# def 함수면(*매개변수): 전달값은 0 개 ~ N 개(여러개)
# 가변 매개 변수의 자료형은 tuple 임
def dynamic_param(*args):
    '가변 매개변수가 받은 값들을 확인하는 함수.'
    print(f'args : {args}, 자료형 : {type(args)}')
    for idx in range(len(args)):
        print(f'[{idx}]번째 전달값 : {args[idx]}')
#----------------------------------------------------
def func_dynamic():
    '가변 매개변수를 가진 함수 사용 테스트'
    dynamic_param()
    dynamic_param(10)
    dynamic_param(2,3)
    dynamic_param(4,3,23,6,5,9,78,10)
#------------------------------------------------------

# 전역변수(Global Vaiable) : 함수 밖에 선언한 변수
# 선언한 위치 아래쪽 코드 어디서나 사용할 수 있는 변수임
message = '전역변수'
print('message : ', message)

def func_variable():
    global message
    print('함수안 : ', message)
    # 지역변수(Local Vailable) : 함수 안에서 선언한 변수
    # 매개변수도 지역변수임
    value = '지역변수'
    print('value : ', value)

    # 함수 안에서 전역변수 값 변경하려면
    # 먼저, 전역변수 사용을 선언해야 함
    # global 전역변수명 => 전역변수 사용 전에 선언해야함
    message = '함수 안에서 값 변경'

#-----------------------------------

# 지역변수는 함수 밖에서 사용 못 함
# print('value : ', value) error


# 작성된 함수 실행 테스트용 함수
def test_fuction():
    prompt = '''
    ***** 파이썬 함수 정의와 사용 테스트 *****
    1. 매개변수와 전달인자의 관계 확인
    2. call by value (값 전달 방식) 확인
    3. call by reference (call by address : 주소 전달 방식) 확인
    4. 기본 매개변수
    5. 키워드 매개변수
    6. 가변 매개변수
    7. 지역변수와 전역변수 확인
    0. 끝내기
    '''
    while True:
        try:
            print(prompt)
            no = int(input('번호 선택 : '))
        except:
            print('숫자만 입력하세요.')
        else:
            if no == 1:
                func_param_args()
            elif no == 2:
                func_call_value()
            elif no == 3:
                func_call_reference()
            elif no == 4:
                func_default_param()
            elif no == 5:
                func_keyword_call()
            elif no == 6:
                func_dynamic()
            elif no == 7:
                func_variable()
                # 전역변수 값 변경 확인
                print('어디서나 사용 가능 - message : ', message)
            elif no == 0:
                print('함수 테스트 종료')
                break
            else:
                print('잘못 입력하셨습니다. 다시 확인하고 입력하세요.')

# 프로그램 구동 -------------------------------------------------
if __name__ == '__main__':
    test_fuction()
