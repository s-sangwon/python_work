# ifelse_mission2.py
# if else 실습문제


def practice2():
    value = int(input('나눌 값 : '))
    div_num = int(input('나누기할 수 : '))

    if (div_num != 0):
        print(f'{value} / {div_num} = {value // div_num}')
    else:
        print('0으로 나눌 수 없습니다.')

    print('프로그램이 종료 되었습니다.')