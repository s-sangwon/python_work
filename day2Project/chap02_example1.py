"""
키보드 입력받아
출력과 같은 프로그램 코드 작성

"""


student_name = str(input('학생이름 입력 : '))
student_no = int(input('학생번호 입력 : '))
kor = int(input('국어점수 입력 : '))
eng = int(input('영어점수 입력 : '))
mat = int(input('수학점수 입력 : '))

tot = kor + eng + mat
avg = tot / 3

print('{}번 {}의 과목총점은 {}점이고 평균은 {:0.2f}점'.format(student_no,\
                                                student_name, tot, avg))
