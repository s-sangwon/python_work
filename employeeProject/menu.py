# menu.py
# 프로젝트 실행시  출력될 메뉴 화면을 구성

import employee.emp_menu as menu

def display():
    prompt = """
    *** 회사 정보 관리 프로그램 ***
    1. 직원 정보 관리
    2. 부서 정보 관리
    3. 직급 정보 관리
    0. 프로그램 끝내기
    
    
"""
    while True:
        print(prompt)
        no = int(input("메뉴 번호 선택 : "))
        if no == 1:
            menu.emp_display()
            # 직원 관리 메뉴 출력
        if no == 2:
            pass
        if no == 3:
            pass
        if no == 0:
            print("프로그램을 종료합니다.")
            return
        else:
            print("번호가 잘못 입력되었습니다.")