# func_mission3.py
# 함수 실습문제 3

def person_security(pno):
    if (pno.find('-') == -1) or (len(pno) != 14):
        raise Exception('1234567-1234567 형식으로 입력해주세요.')
    return pno[:8] + '*' * (len(pno)-8)
def enroll():
    try:
        name = input('이름 : ')
        person_no = input('주민등록번호 : ')
        print(f'이름 : {name}, 주민번호 : {person_security(person_no)}')
    except Exception as msg:
        print(msg)
    finally:
        print('함수종료')

if __name__ == '__main__':
    enroll()