# chap02_builtin.py
# 파이썬이 제공하는 내장함수 : 기본으로 제공됨
# 별도로 import 선언하지 않고 사용
# max, min, type, len, range, str, int, float, print, input 등~

# type(값 또는 변수명) : 값의 자료형을 return
a = 12
b = 'text'
c = 1 + 4j
for i in a,b,c:
    print(type(i),end=' ')
print()
# len(값 또는 변수) : 길이(저장된 값의 갯수) 리턴
d = 'abcd'
e = [1,2,3,4,5]
print(len(d),len(e))

# max(값들 또는 변수) : 최대값(가장 큰 값), min() : 최소값(가장 작은 값)
print(max('abcdefg'))
print(max('123456789'))
print(min('abcdefg'))
print(min('123456789'))

x=4
y=4
x<<=5
y>>=1
print(y)