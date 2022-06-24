#chap02_ex1.py

num1 = input('첫번째 정수 : ')
num2 = input('두번째 정수 : ')

#int(input()) 이 더좋음
int_num1 = int(num1)
int_num2 = int(num2)
print(num1, '+', num2,' =', int_num1 + int_num2)
print(num1, '-', num2,' =', int_num1 - int_num2)
print(num1, '*', num2,' =', int_num1 * int_num2)
print(num1, '//', num2,' =', int_num1 // int_num2)
print(num1, '%', num2,' =', int_num1 % int_num2)
print(num1, '** 2 = ', int_num1 ** 2)
print(num2, '** 2 = ', int_num2 ** 2)
op = ['+', '-', '*', '//', '%', '**']

# name = input('이름 : ')
# age =  int(input('나이 : '))
# gen = input('성별 : ')
# tall = float(input('키 : '))
# wei = float(input('몸무게 : '))
# print(name +'은',age,'세',
#       gen+'이고, 키는 ', tall
#       ,'cm 몸무게는 ',wei,'kg 입니다.')
