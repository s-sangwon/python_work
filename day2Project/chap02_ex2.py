name = input('이름 : ')
age =  int(input('나이 : '))
gen = input('성별 [남/여] : ')
height = float(input('키 : '))
weight = float(input('몸무게 : '))
print(name +'은 ',age,'세',
      gen+'이고, 키는', height
      ,'cm 몸무게는 ',weight,'kg 입니다.')

print('{}은 {}새 {}자이고, 키는 {}cm, 몸무게는 {}kg 입니다:'.format(\
      name,age,26,gen,weight, height))