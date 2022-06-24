# ifelse_mission3.py
# ifelse 실습문제

def practice3():
    tno = input('수험번호 : ')
    database = int(input('데이터베이스 : '))
    program = int(input('프로그래밍언어 : '))
    software = int(input('소프트웨어공학 : '))

    tot = database + program + software
    avg = tot // 3
    a = (database, program, software) >= (40,40,40)
    print(a)
    if(avg >= 60 and database >= 40 and program >= 40 and software >= 40):
        print(f'수험번호 : {tno} 합격입니다.')
    else:
        print(f'수험번호 : {tno} 불합격입니다.')