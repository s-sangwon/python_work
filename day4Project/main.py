# This is a start project script.
# day4Project 시작 시키는 스크립트


# 모듈 : 함수를 가지고 있는 파이선 파일
# 다른 파이썬 파일에서 모듈이 가진 함수를 사용하고자 한다면
# import 문을 사용해서 임포트 선언하면 됨
# import 파일명 (같은 디렉토리에 있는 파일일 때)
# improt 디렉토리명.파일명
import mission.list_review

# 모듈명이 길거나 복잡하면 줄임말을 지정할 수 있음
# import 모듈명 as 줄임말
#import test_set.set_sample as ts
import test_dict.dict_sample as td


# def loop(a):
#     print('recursive call parameter = ',a)
#     a += 1
#     if a>=125:
#         print('recursive call end')
#         return 0;
#     loop(a)
#     loop(a)

#Run 버튼 클릭 | Shift + F10 누르면 실행됨
# if __name__ == '__main__':
    # 임포트한 모듈(파일)이 가진 함수를 사용(실행)하려면
    #mission.list_review.func()
    #ts.test1()
    #ts.test2()
    #ts.test3()
    #ts.test4()
    #ts.test5()
    #ts.test6()
    #ts.test7()

    # dict (사전) 자료형 테스트 함수 실행

    # td.test1()
    # td.test2()
    # td.test3()
    # td.test4()
    #td.test5()
    #td.test6()
    # td.test7()
    #td.test8()
    #td.test9()

#import mission.dict_review as mr
#import mission.dict_review2 as mr2

#if __name__ == '__main__':
    #mr.dictfunc()
    # mr.dictfunc2()
    # mr2.dictfunc()
    # mr2.dictfunc2()

import test_logic.chap07_conditional as logic

if __name__ == '__main__':
    #logic.func_bool()
    # logic.func_compare()
    logic.func_logical()

