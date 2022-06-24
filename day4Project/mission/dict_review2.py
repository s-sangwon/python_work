# mission\dict_review2.py
# mission.dict_review2
# dict 자료형 복습문제 2

def dictfunc():
    sungjuk_dict = {
        'sno': int(input('번호 : ')),
        'sname': input('이름 : '),
        'kor': int(input('국어 : ')),
        'eng': int(input('영어 : ')),
        'mat': int(input('수학 : '))
    }
    sungjuk_dict['tot'] = sungjuk_dict['kor'] + sungjuk_dict['eng'] + sungjuk_dict['mat']
    sungjuk_dict['avg'] = sungjuk_dict['tot'] / 3

    print('%d번 %s의 총점은 %d 점, 평균은 %f 점.'
          %(sungjuk_dict['sno'], sungjuk_dict['sname'], sungjuk_dict['tot'], sungjuk_dict['avg']))
    print('국어 : %d 점, 영어 : %d 점, 수학 : %d 점입니다.'
          %(sungjuk_dict['kor'], sungjuk_dict['eng'], sungjuk_dict['mat']))


def dictfunc2():

    sno = int(input('번호 : '))
    sname = input('이름 : ')
    kor = int(input('국어 : '))
    eng = int(input('영어 : '))
    mat = int(input('수학 : '))

    tot = kor + eng + mat
    avg = tot / 3

    #s_list = [sname, kor, eng, mat, tot, avg]
    #sungjuk_dict = {sno : s_list}

    sungjuk_dict = {sno : [sname, kor, eng, mat, tot, avg]}

    print('{}번 {}의 총점은 {} 점, 평균은 {} 점.'\
          .format(sno, sungjuk_dict[sno][0], sungjuk_dict[sno][4], sungjuk_dict[sno][5]))
    print('국어 : {} 점, 영어 {} 점, 수학 : {} 점입니다.'\
          .format(sungjuk_dict[sno][1], sungjuk_dict[sno][2], sungjuk_dict[sno][3]))
    # print(s_list, type(s_list))
    # print(sungjuk_dict, type(sungjuk_dict))
    # sungjuk_dict.get(sno)[0]