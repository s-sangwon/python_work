# mission1.py
# 리스트 실습문제

"""
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.

입력받은 값들을 리스트에 순서대로 저장처리

리스트에 저장된 값들을 출력
"""
# 방법 1
# name = input('학생이름 : ')
# grade = int(input('학년 : '))
# s_class = int(input('반 : '))
# s_no = int(input('번호 : '))
# score = float(input('점수 : '))
#
# student_list = [name, grade, s_class, s_no, score]
# s_list = []
# print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 점입니다.'
#       .format(student_list[1],student_list[2],student_list[3],student_list[0],student_list[4]))
#
# for i in [grade, s_class, s_no, name, score]:
#     s_list.append(i)
# print(s_list)

# 방법 2 : 입력받은 값들을 리스트에 append() 사용해서 저장
#
# name = input('학생이름 : ')
# grade = int(input('학년 : '))
# s_class = int(input('반 : '))
# s_no = int(input('번호 : '))
# score = float(input('점수 : '))
#
# student_list = []
# # student_list[0] = name # 값이 저장되지 않으면, 인덱스는 없음, 에러
# student_list.append(name)
# student_list.append(grade)
# student_list.append(s_class)
# student_list.append(s_no)
# student_list.append(score)
#
# print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 점입니다.'
#        .format(student_list[1],student_list[2],student_list[3],student_list[0],student_list[4]))


# 방법 3 : 방법2 코드 줄 수 줄이기
student_list = []

student_list.append(input('학생이름 : '))
student_list.append(int(input('학년 : ')))
student_list.append(int(input('반 : ')))
student_list.append(int(input('번호 : ')))
student_list.append(float(input('점수 : ')))

# student_list = [input('학생이름 : '),int(input('학년 : ')),int(input('반 : ')),int(input('번호 : ')),float(input('점수 : '))]

print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 점입니다.'.format(student_list[1],student_list[2],student_list[3],student_list[0],student_list[4]))