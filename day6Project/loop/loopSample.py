# loop\\loopSample.py
# 모듈표현 : loop.loopSample

# def recursion(x):
#     if(x==0):
#         print('exit')
#         return 0;
#     print(f'recursion({x})')
#     recursion((x-1))

# 반복이 반복될 때 for 문 안에 for 문 사용할 수 있음
def doubleFor():
    for dan in range(2, 10): # 2단부터 9단 까지 8번 반복처리
        for su in range(1,10): # 하나의 단에 대한 구문 9번 출력
            print(f'{dan} * {su} = {dan * su}')
        print('--------------------------------')

# 리스트(튜플, 셋) 안의 리스트(튜플, 셋)가 저장된 경우
# 첫번쨰 추출은 아느이 리스트 전체 추출임
# 안의 리스트가 가진 값들을 하나씩 처리해야 하는 경우
# 이중 for 문 사용할 수 있음
def list_in_list():
    fruits_list = \
        [['apple', 10, 500], ['banana', 3, 2500], ['orange', 15, 350]]
    for fname, famount, fprice in fruits_list:
        print(f'{fname}은 {fprice}원이고, 구매수량은 {famount} 개이므로, 구매가격은 {famount*fprice} 이다  ')

# 리스트 안의 리스트의 값 갯수나 기록형태가 제각각인 경우
# 안의 리스트의 값들을 각각 처리해야 하는 경우는 이중 for문 사용

def list_in_list2():
    nlist = [['a', 'bb', 'cde'], [10,20], [1.2, 3.5, 33, 78.90]]

    for item in nlist:
        print(item)
        for data in item:
            print(data)
        print('-----------')

def list_in_list3():
    nlist = [['a', 'bb', 'cde'], [10,20], [1.2, 3.5, 33, 78.90]]

    for index in range(len(nlist)):# range(3) : 0~2
        print(nlist[index]) # 안의 리스트
        for j in range(len(nlist[index])): #안의 리스트의 값의 갯수
            print(f'nlist[{index}][{j}] :{nlist[index][j]}')
        print('-----------')

# 필요한 경우 반복문 안에 조건문을 사용할 수도 있음
# 예 : 문자열에서 특정 문자의 포함갯수를 조회하고자 한다면
# 문자열과 찾을 문자를 입력받고, 문자열 안의 찾는 문자의 갯수 조회
def loop_in_conditional():
    st = input('문자열 입력 : ')
    ch = input('찾는 문자 입력 : ')
    cnt = 0

    for c in st:
        if c == ch:
            cnt += 1

    print(f'{st} 안에 포함된 {ch}의 갯수느 {cnt} ')

# 문자열 안의 찾는 문자를 제외한 글자 갯수 조회
def loop_in_conditional2():
    st = input('문자열 입력 : ')
    ch = input('찾는 문자 입력 : ')
    cnt = 0

    for c in st:
        if c == ch: # c!= ch
            cnt += 1

    print(f'{st} 안에 포함된 {ch} 를 제외한 글자는 {len(st)-cnt} ') # cnt

'''
제어(처리) 문: 조건문, 반복문, 분기문
분기문 : 실행의 흐름을 바꾸는 구문 - continue, break
    => 제한 1 : if 문과 함께 사용함
       
        for | while 반복조건:
            if 조건식:
                continue # 반복문 중간생략
            반복 처리 구문들
            
        for | while 반복조건:
            if 조건식:
                break   # 반복문을 강제로 종료시킴
            반복 처리 구문들
            
    => 제한 2 : 반복문 내에서만 사용할 수 있음
'''

# 1부터 100까지 정수 중에서 짝수들의 합게만 구하는 경우
# range() 이용, continue 이용
# continue 이용
def sum_even_1to100():
    sum = 0
    for n in range(1,101):
        if(n % 2 != 0):
            continue
        print(n, '+', end='')
        sum += n
    print(f'\n1부터 100까지 짝수들의 합계 : {sum}')

# 리스트 안의 튜플이 가진 값에 대한 변수 지정시에는
# (변수명, 변수명, ...) 소괄호로 묶어서 변수 지정함
def list_in_tuple():
    nlist = [(12, 45), (90, 32), (56, 19)]
    # for item in nlist:
    #     print(item)
    # for a, b in nlist:
    #     print(a,b)

    for (a,b) in nlist:
        print(a,b,type(a),type(b))

def list_comprehension():
    l = [i for i in range(101) if i%2 == 1]
    l = [i*j for i in range(2,10) for j in range(1,10) if j==9 ]
    print(l)

# while 문 ----------------------------------
'''
while (반복을 위한 조건식): => 조건의 결과가 참일 동안 계속 반복됨
    반복 실행 구문
조건의 결과가 거짓이면 반복은 종료되고 다음 구문으로 넘어감
주의사항 : 반복의 조건식 결과가 계속 True 이면 무한루프에 빠짐
'''

def test_while():
    num = 5
    while(num > 0 ):
        print(num)
        num -= 1

# 반복에 대한조건식에 True 를 사용할 수도 있음
# 주의 : 무한루프가 되지 않게 if조건문과 break 문을 반복문 안에 작성
def test_while2():
    num = 5
    while(True):
        print(num)
        num -= 1
        if num == 0:
            break

# 반복 횟수가 정해지지 않은 경우 while 을 주로 사용함
# 문자 하나를 입력받아서, 그 문자의 유니코드를 출력하는 처리를 반복함
# 단, 0 문자가 입력되면 반복이 종료됨
def print_unicode():
    ch = input('문자하나를 입력하시오(0 종료) : ')
    while(ch != '0'):
        print(f'{ch} 의 unicode는 {ord(ch)}')
        ch = input('문자하나를 입력하시오(0 종료) : ')



def print_unicode1():
    while(True):
        ch=input('문자하나를 입력하시오(0 종료) : ')
        if(ch=='0'):
            break
        print(f'{ch} 의 unicode는 {ord(ch)}')

# 파이선에서는 여러 줄의 문자열을 표현할 때 3쌍의 따옴표를 이용할 수 있다.

def display_menu():
    prompt = ''' 
    *** 원하는 메뉴 번호를 선택하세요 ***
    
    1. 추가
    2. 삭제
    3. 출력
    4. 끝내기
    
    번호 입력 : \
'''

    # print(prompt)

    while True:
        no = int(input(prompt))

        if no == 4:
            break
    print('==== end ====')