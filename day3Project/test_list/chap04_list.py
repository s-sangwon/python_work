# chap04_list
# 리스트(list) 자료형
# 파이선이 제공하는 기본 군집자료형임.
# 개념 : 여러 종류의 값들을 순차적으로 저장하는 자료형
# 저장 용량에 제한은 없다.
# 값의 종류에도 제한이 없다.
# 저장 순서에 대한 순번(인덱스 : index)가 있음

# 리스트 정의(생성) 방법 1 : list() 함수 사용
list_1 = list()
print(list_1, type(list_1))

# 리스트 정의(생성) 방법 2 : [] 대괄호 사용
list_2 = []
print(list_2, type(list_2))

# list 자료형의 특징 1 : 문자열(str)과 같이 인덱싱, 슬라이싱 연산이 가능함
# index(순번 : 저장순서, 0부터
# 표현 : 리스트변수[순번]
list_3 = [1, 2, 3, 'python', 3.56, [11, 22, 33], True, False]
print('0번째 기록된 값 조회 : ', list_3[0])
print('3번째 기록된 값 조회 : ', list_3[3])
print('5번째 기록된 값 조회 : ', list_3[5])

# 슬라이싱 : 리스트에 저장된 데이터들 부분 추출
# 표현 : 리스트변수[시작인덱스:끝인덱스:간격]
# 시작인덱스부터 끝인덱스-1 위치까지 추출됨
# 간격 : 생량되면 기본값이 1임
print('0번 인덱스부터 3번 인덱스까지의 데이터 추출 : ',list_3[0:4])

# len(리스트변수) : 리스트에 저장된 데이터 갯수 조회 가능
print('list_3 에 저장된 값의 갯수 : ',len(list_3))
# len() 을 이용해서 마지막 위치의 값 조회할 수도 있음
print('list_3에 저장된 마지막 인덱스 : ',len(list_3) - 1)
print('list_3의 마지막 인덱스 위치의 값 조회 : ',list_3[len(list_3)-1],list_3[-1])

# list 자료형의 특징 2 : 요소(element) 값은 변경할 수 있음
# 변경할 값의 종류에는 제한이 없다.
# 인덱스(순번) 이용 : 리스트 변수[인덱스] = 바꿀값
print('변경전 : ', list_3)
list_3[0] = 77
print('변경후 : ', list_3)
list_3[1] = 'test'
print('변경후 : ', list_3)
list_3[2] = [1.2, 2.3, 4.5]
print('변경후 : ', list_3)

# list 자료형 특징 3 : 리스트를 다루는 함수(메소드) 들이 제공됨
# append() : 뒤에 추가
# insert() : 값 사이에 추가
# remove() : 값 삭제
# pop() : 꺼내면서 리스트에서 뺌(제거)
# reverse() : 리스트 안에 데이터 순서를 반대로 바꿈(뒤집기)
# clear() : 리스트 비움