# mission2.py
# 리스트 실습문제 2

"""
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.

3명학생의 국영수 점수
각 리스트에 [국, 영, 수, 총점, 평균] 저장하기
계산한 리스트를 리스트안에 저장
3명 총점과 전체평균도 계산
총합과 평균계산
소수점둘째자리까지 표시
format() 사용
"""
s1 = []
s1.append(float(input('국어 점수 : ')))
s1.append(float(input('영어 점수 : ')))
s1.append(float(input('수학 점수 : ')))
s1.append(sum(s1))
s1.append(s1[3]/3)

s2 = []
s2.append(float(input('국어 점수 : ')))
s2.append(float(input('영어 점수 : ')))
s2.append(float(input('수학 점수 : ')))
s2.append(sum(s2))
s2.append(s2[3]/3)

s3 = []
s3.append(float(input('국어 점수 : ')))
s3.append(float(input('영어 점수 : ')))
s3.append(float(input('수학 점수 : ')))
s3.append(sum(s3))
s3.append(s3[3]/3)
print(s3)

sungjuk_list = []
sungjuk_list.append(s1)
sungjuk_list.append(s2)
sungjuk_list.append(s3)
print(sungjuk_list)

total_score = int(sungjuk_list[0][3] + sungjuk_list[1][3] + sungjuk_list[2][3])
average_score = total_score / 3 / 3
print('학생1 국어점수 : {}, 영어점수 : {}, 수학점수 : {}, 총점 : {}, 평균 : {}'
      .format(sungjuk_list[0][0], sungjuk_list[0][1], sungjuk_list[0][2], sungjuk_list[0][3], sungjuk_list[0][4]))
print('학생2 국어점수 : {}, 영어점수 : {}, 수학점수 : {}, 총점 : {}, 평균 : {}'
      .format(sungjuk_list[1][0], sungjuk_list[1][1], sungjuk_list[1][2], sungjuk_list[1][3], sungjuk_list[1][4]))
print('학생3 국어점수 : {}, 영어점수 : {}, 수학점수 : {}, 총점 : {}, 평균 : {}'
      .format(sungjuk_list[2][0], sungjuk_list[2][1], sungjuk_list[2][2], sungjuk_list[2][3], sungjuk_list[2][4]))
print('전체총점은 {}이고, 전체평균은 {}이다.'.format(total_score, average_score))
