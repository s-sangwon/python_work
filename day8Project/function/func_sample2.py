# func_sample.2py
# 함수의 매개변수 다루기

# 함수의 매개변수(parameter)는 전달받은 값은 변경할 수 없다.
# 전달받은 객체가 군집형일때는 요소는 변경할 수 있다.

def list_func(plist):
    print('plist 가 받은 주소 : ', id(plist))
    print('before : ', plist)
    plist[1] = 10
    print('after : ', plist)

# 함수 사용
def test_parameter():
    lst = [1, 2, 3]
    print('lst 가 참조하는 객체의 주소 : ', id(lst))
    print('lst : ', lst)
    list_func(lst) # call by reference
    print('lst : ', lst)



if __name__ == '__main__':
    test_parameter()