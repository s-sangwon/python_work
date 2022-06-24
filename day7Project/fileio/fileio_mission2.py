# fileio_mission2.py
# 파일 입출력 실습문제2
def simple_memo():
    prompt_menu = '''
    파이썬 메모장이 실행되었습니다.\n
    1. 새로 만들기
    2. 저장하기
    3. 불러오기
    4. 끝내기
    '''
    while True:
        print(prompt_menu)
        no = int(input('번호를 입력하세요 : '))

        if no == 1:
            print('내용을 입력하세요')
            contents = ''
            while True:
                line = input()
                if(line == '--end--'):
                    break
                #line += '\n'
                contents += line + '\n'
        elif no == 2:
            fname = input('저장할 파일명 : ')
            f = open(fname, 'w', encoding='utf-8')
            f.write(contents)
            f.close()

        elif no == 3:
            fname = input('불러올 파일명 : ')
            f = open(fname, 'r', encoding='utf-8')
            print(f.read())
            f.close()

        elif no == 4:
            break
        else:
            print('잘못된 번호입니다. 다시입력 하세요.\n')

    print('파이썬 메모장을 종료합니다.')

if __name__ == '__main__':
    simple_memo()