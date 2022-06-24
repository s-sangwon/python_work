# chap02_example2.py
# 복습문제 2

"""
키보드로 값을 입력받아 요구조건대로 처리하고 출력되게 코드를 작성하시오.
"""

total_point = 12500
custom_name = input('고객 이름 : ')
price = int(input('결재 금액 : '))
point = price * 0.05
total_point += point

print('{} 고객님의 사용금액은 {} 원, 발생 포인트는 {}'.format(custom_name,\
                                              price, point))
print('현재 이용하실 수 있는 누적포인트는 {} 점 입니다.'.format(total_point))

print(f'{custom_name} 고객님의 사용금액은 {price} 원, 발생 포인트는 {int(point)}')
print(f'현재 이용하실 수 있는 누적포인트는 {int(total_point)} 점 입니다.')

a = """ㅋㅋㅋ


ㅋㅋ 웃겨~"""
print(a)

