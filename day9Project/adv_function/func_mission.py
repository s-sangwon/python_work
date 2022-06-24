# func_mission.py
# 재귀함수, 람다함수, 내장함수 실습문제

def factorial_recurisve(n):
    return n * factorial_recurisve(n-1) if n != 0 else 1
def for_factorial(n):
    f=1
    for i in range(n,1,-1):
        f *= i
    return f

def gugudan():
    '4. 리스트 내포 : 구구단 2단~9단까지 곱하기 결과 저장 출력'
    #gu = [dan*su for dan in range(2,10) for su in range(1,10)]
    igu = [[dan*su for su in range(1,10)] for dan in range(2,10)] # 단하나에 리스트하나씩
    print(igu)
    for idx in range(len(igu)):
        print(igu[idx])

def test1():
    try:
        print('재귀 함수 이용 팩토리얼 :',factorial_recurisve(int(input('정수를 입력하세요 : '))))
    except:
        print('정수만 입력하세요.')
    finally:
        print('test1 끝')

def test2():
    lf = lambda n: n * lf(n-1) if n > 0 else 1
    lf2 = lambda n: n == 0 and 1 or n * lf2(n-1)  # (lambda n: n == 0 and 1 or n * factorial(n-1))(n)
    try:
        print('람다 함수 이용 팩토리얼 :',lf(int(input('정수를 입력하세요 : '))))
        print('람다 함수 이용 팩토리얼 :',lf2(int(input('정수를 입력하세요 : '))))
    except:
        print('정수만 입력하세요.')
    finally:
        print('test2 끝')
def test3():
    try:
        print('반복문 이용 팩토리얼 :',for_factorial(int(input('정수를 입력하세요 : '))))
    except:
        print('정수를 입력해')
    finally:
        print('test3() 끝')

def test4():
    print('리스트 내포 이용 구구단')
    gugudan()

def test5():
    print('람다 함수 이용 구구단')
    result = (lambda : [[dan*su for su in range(1,10)] for dan in range(2,10)])()
    print([(lambda d,s: f'{d} * {s} = {d * s}')(dan,su) for dan in range(2,10) for su in range(1,10)])
    for idx in range(len(result)):
        print(result[idx])

# 6. 람다함수로 바꾸기 실습
# def test_func(a):
#     if a > 10:
#         return 'a가 10보다 크다.'
#     else:
#         return 'a가 10보다 작거나 같다.'

def test6():
    # print(test_func(14))
    print((lambda a: 'a가 10보다 크다' if a > 10 else 'a가 10보다 작거나 같다.')(14))

# 7. map() 함수와 람다함수 사용으로 바꾸기 실습
# def test_func2(a):
#     ls = []
#     for i in range(a):
#         ls.append(i ** 2)
#     return ls

def test7():
    # print(test_func2(5))
    print(list(map(lambda x: x ** 2,range(5))))

# 함수 실행 ------------------------------
def func_mission():
    prompt = '''
    ***** 함수 활용 테스트 *****
    1. 재귀함수 : 입력받은 정수의 펙토리얼 구하기
    2. 람다함수 : 입력받은 정수의 펙토리얼 구하기
    3. 반복문 사용 : 입력받은 정수의 펙토리얼 구하기
    4. 리스트 내포 : 구구단 2단~9단까지 곱하기 결과 저장 출력
    5. 람다함수와 리스트 내포 : 구구단 2단~9단까지 곱하기 결과 저장 출력
    6. 람다함수로 바꾸기 실습
    7. map() 함수와 람다함수 사용으로 바꾸기 실습
    0. 끝내기
    '''
    while True:
        try:
            print(prompt)
            no = int(input('번호 입력 : '))
        except:
            print('숫자를 입력해주세요.')
        else:
            if no == 1:
                test1()
            elif no == 2:
                test2()
            elif no == 3:
                test3()
            elif no == 4:
                test4()
            elif no == 5:
                test5()
            elif no == 6:
                test6()
            elif no == 7:
                test7()
            elif no == 0:
                break
            else:
                print('잘못 입력하셨습니다. 다시입력하세요.')
        finally:
            print('함수 활용 테스트 종료.')




# 실습문제 실행 테스트 ---------------------
if __name__ == '__main__':
    func_mission()
