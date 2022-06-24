# mission\dict_review.py
# mission.dict_review
# 사전 자료형 복습문제

"""
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.
"""
from typing import Dict, Union


def dictfunc():
    name = input('학생이름 : ')
    grade = int(input('학년 : '))
    s_class = int(input('반 : '))
    s_no = int(input('번호 : '))
    score = float(input('점수 : '))

    student_dict = {
        'name': name,
        'grade': grade,
        's_class': s_class,
        's_no': s_no,
        'score': score
    }
    print('{}학년 {}반 {}번 {}의 점수는 {:0.2f} 입니다.'
          .format(student_dict['grade'], student_dict['s_class'], student_dict['s_no'], student_dict['name'],
                  student_dict['score']))


# 방법 2
def dictfunc2():
    # name = input('학생이름 : ')
    # grade = int(input('학년 : '))
    # s_class = int(input('반 : '))
    # s_no = int(input('번호 : '))
    # score = float(input('점수 : '))
    student_dict: dict[str, Union[str, int, float]] = {'name': input('학생이름 : '), 'grade': int(input('학년 : ')), 's_class': int(input('반 : ')), 's_no': int(input('번호 : ')), 'score': float(input('점수 : '))}
    # student_dict = {
    #     'name': name,
    #     'grade': grade,
    #     's_class': s_class,
    #     's_no': s_no,
    #     'score': score
    # }

    print('{}학년 {}반 {}번 {}의 점수는 {:0.2f} 입니다.'
          .format(student_dict.get('grade'), student_dict.get('s_class'), student_dict.get('s_no'), student_dict.get('name'), student_dict.get('score')))
