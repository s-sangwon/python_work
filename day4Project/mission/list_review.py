# list_review.py
# list 자료형 복습문제

def func():
    sungjuk_list=[int(input('번호 : ')),
                      input('이름 : '),
                  int(input('국어 : ')),
                  int(input('영어 : ')),
                  int(input('수학 : ')),]
    sungjuk_list.append(sum(sungjuk_list[2:5]))
    sungjuk_list.append(sungjuk_list[5] / 3)

    print(f'{sungjuk_list[0]}번 {sungjuk_list[1]}의 총점은 {sungjuk_list[5]} 점, 평균은 {sungjuk_list[6]} 점.')
    print(f'국어 : {sungjuk_list[2]} 점, 영어 : {sungjuk_list[3]} 점, 수학 : {sungjuk_list[4]} 점 입니다.')

    # print('%d번 %s의 총점은 %d 점, 평균은 %f 점.' %(sungjuk_list[0],sungjuk_list[1],sungjuk_list[5],sungjuk_list[6]))
    # print('국어 : %d 점, 영어 : %d 점, 수학 : %d 점입니다.' %(sungjuk_list[2], sungjuk_list[3], sungjuk_list[4]))
    #
    # print('{}번 {}의 총점은 {} 점, 평균은 {}점.'.format(sungjuk_list[0], sungjuk_list[1], sungjuk_list[5], sungjuk_list[6]))
    # print('국어 : {} 점, 영어 : {} 점, 수학 : {} 점입니다.'.format(sungjuk_list[2], sungjuk_list[3], sungjuk_list[4]))
