import notice.notice_controller as ncontroll

def display():
    prompt="""
    ***** notice_project *****
    1. insert notice
    2. select all
    3. update notice
    4. delete notice
    5. select search title
    6. select search date
    7. select search writer
    0. exit
    """
    while True:
        print(prompt)
        eno = int(input("Please select a menu : "))

        if eno == 1:
            ncontroll.insert(input_notice())
        elif eno == 2:
            notice_list = ncontroll.select_all()
            print("현재 notice 수 : ", len(notice_list))
            notice_print(notice_list)
        elif eno == 3:
            ncontroll.update(modify_notice())
        elif eno == 4:
            notice_no = input('삭제할 notice 공지번호 : ')
            ncontroll.delete_notice((notice_no, ))
        elif eno == 5:
            notice_list = ncontroll.select_search_title(input_title())
            notice_print(notice_list)
        elif eno == 6:
            notice_list = ncontroll.select_search_date(input_date())
            notice_print(notice_list)
        elif eno == 7:
            notice_list = ncontroll.select_search_writer(input_writer())
            notice_print(notice_list)
        elif eno == 0:
            return
        else:
            print("올바른 메뉴를 선택하세요\n")

# 새로 등록할 notice 입력받는 함수
def input_notice():
    print('새로 등록할 notice 정보를 순서대로 입력하세요.')
    title = input('공지 제목 : ')
    writer = input('작성자아이디 : ')
    content = input('공지 내용 : ')
    upfile = input('첨부 파일: ')
    return (title, writer, content, upfile)

# 리턴받은 전체 noitce 출력용 함수
def notice_print(nlist):
    for n in nlist:
        # print(n)
        # 컬럼값 개별 출력 처리
        for col in n:
            print(col,end=", ")
        print()

def modify_notice():
    print('변경할 notice 정보를 순서대로 입력하세요.')
    no = int(input('변경할 공지 번호 : '))
    title = input('공지 제목 :')
    content = input('공지 내용 : ')
    upfile = input('첨부 파일 : ')
    return (title, content, upfile, no)

def input_title():
    return (input('조회할 공지 제목을 입력하세요 : '), )

def input_date():
    return (input('조회할 날짜를 입력하세요 [YYYY-MM-DD형식]: '), )

def input_writer():
    return (input('조회할 작성자 아이디를 입력하세요 : '), )