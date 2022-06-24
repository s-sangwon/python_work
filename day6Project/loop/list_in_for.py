# list_in_for.py
# 리스트 내포 확인용

# 리스트 내포 (내부에 포함)
# 리스트 내에 값 추가를 위한 for문을 포함하는 구문
# [아이템 for 아이템 in 시퀀스객체]
# 주의 : 아이템은 이름이 같아야 함
# 시퀀스객체(iterable) : 순차적으로 값을 저장하는 객체(str, list, tuple, set)

def list_append():
    sample_list = list()
    for n in range(1, 6):
        sample_list.append(n)
    print(sample_list)

# 리스트 내포로 바꾼다면
def list_append2():
    # sample_list = list()
    # for n in range(1, 6):
    #     sample_list.append(n)
    # print(sample_list)
    print([n for n in range(1,6)])

# 리스트 내포시에 if 문과 같이 포함할 수 있음

def list_append3():
    sample_list = []
    for k in range(1,11):
        if(k % 2 == 0):
            sample_list.append(k)
    print(sample_list)

def list_append4():
    # sample_list = []
    # for k in range(1,11):
    #     if(k % 2 == 0):
    #         sample_list.append(k)
    # print(sample_list)
    sample_list = [k for k in range(1,11) if k % 2 == 0]
    print(sample_list)

# for 문 안에 for 문이 사용되는 경우 (다중 for 문)
def list_append5():
    sameple_list = []
    for k in range(1,6):
        for m in range(1,6):
            sameple_list.append(k+m)
    print(sameple_list)

def list_append6():
    # sameple_list = []
    # for k in range(1,6):
    #     for m in range(1,6):
    #         sameple_list.append(k+m)
    sameple_list = [k+m for k in range(1,6) for m in range(1,6)]
    print(sameple_list)

# 구구단 2단부터 9단까지 곱하기한 결과값을 리스트에 저장 처리함
# 리스트 내포로 저장후 출력

def print_99dan():
    list_99dan = [i*j for i in range(2,10) for j in range(1,10)]
    print(list_99dan)



if __name__ == '__main__':
    # list_append()
    # list_append2()
    # list_append3()
    # list_append4()
    # list_append5()
    # list_append5()
    print_99dan()




