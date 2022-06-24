#chap02_input.py

# 파이선에서 실행시 키보드로 입력받기
# input() 함수 사용함
# 변수이름 = input('입력을 위한 메세지 문장')

# 입력을 위한 메세지 없이 실행 테스트

num = input('숫자를 입력하세요 : ')
print('num : ',num)
print('num 에 저장된 값의 종류 : ', type(num))
# 파이썬의 input() 함수로 입력되는 값은 모두 문자형(str) 이다.
# 숫자와 문자는 계산할 수 없음

# 숫자형으로 바꾸고자 한다면,
# 정수는 int('정수문자'), 실수는 float('실수문자') 사용함
int_num = int(num)
print('int_num ', int_num, type(int_num))
print('더하기 확인 : ', int_num + 100)


# #ex1
#
# num1 = input('첫번째 정수 : ')
# num2 = input('두번째 정수 : ')
#
# int_num1 = int(num1)
# int_num2 = int(num2)
# print(num1, '+', num2,' =', int_num1 + int_num2)
# print(num1, '-', num2,' =', int_num1 - int_num2)
# print(num1, '*', num2,' =', int_num1 * int_num2)
# print(num1, '//', num2,' =', int_num1 // int_num2)
# print(num1, '%', num2,' =', int_num1 + int_num2)
# print(num1, '** 2 = ', int_num1 ** 2)
# print(num2, '** 2 = ', int_num2 ** 2)

