# 변수 요약 정리 코드
# 파이썬에서 변수는 반드시 값을 기록해야 생성됨
# num
# print(num)   is not defined error
num =12 #변수명 = 기록할 값
print(num)

# 파이썬은 변수에 기록할 값의 종류(data type : 자료형)를 정하지 않음!
# 자료형 변수명 = 기록할값  standard 변수선언
# 변수방에 기록되는 값에 따라 자료형이 정해짐.
value = 100
print(value, type(value))

value = 'python'
print(value, type(value))

value = 3.14
print(value, type(value))

value = False
print(value, type(value))

value = -3j
print(value, type(value))

# 변수 제거 : del 변수명
del value
# print(value) # is not defined