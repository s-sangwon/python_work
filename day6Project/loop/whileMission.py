# whileMission.py
# while 문 실습문제

def sungjuk_process():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
    prompt = ''' 
*** 원하는 메뉴 번호를 선택하세요 ***

1. 추가
2. 삭제
3. 출력
4. 끝내기

번호 입력 : \
'''
    while True:
        no = int(input(prompt))
        if no == 1:
            sno = int(input('번호 : '))
            sname = input('이름 : ')
            score = int(input('점수 : '))
            buf = [sno, sname, score]
            print('==> 리스트에 추가 처리함')
            sungjuk_list.append(buf)
            print('==> 새로운 학생정보가 추가되었습니다.',sungjuk_list[len(sungjuk_list)-1])
        elif no == 2:
            print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
            index = int(input('제거할 아이템의 순번 : '))
            if(0 <= index < len(sungjuk_list)):
                print('==> 입력받은 인덱스 위치의 아이템 제거함')
                sungjuk_list.pop(index)
                print(f'==> {index}번 위치의 아이템이 제거되었습니다.')
                print(f'==> 현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
            else:
                print('유효한 인덱스를 입력하세요. 처음으로 돌아갑니다.')
                continue
        elif no == 3:
            # i=0
            # for item in sungjuk_list:
            #     print(f'{i} : {item}')
            #     i += 1 아래처럼 해야지 ㅋㅋ
            for idx in range(len(sungjuk_list)):
                print(f'{idx} : {sungjuk_list[idx]}')
        elif no == 4:
            print('성적관리 프로그램이 종료되었습니다.')
            break

    print('==== end ====')



if __name__ == '__main__':
    sungjuk_process()
    pass