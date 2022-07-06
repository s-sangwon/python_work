# employee\emp_menu.py
# 모듈 표기 : employee.emp_menu
import common.oracle_db

def emp_display():
    emp_prompt="""
    ***** 직원 정보 관리 부메뉴 *****
    1. 직원 정보 새로 등록
    2. 전체 직원 정보 조회
    3. 사번으로 직원 정보 조회
    4. 직원 정보 변경
    5. 직원 삭제
    6. 이름으로 직원 조회
    7. 직급으로 직원 조회
    8. 부서코드로 직원 조회
    0. 이전 메뉴로 가기
    

    """
    while True:
        print(emp_prompt)
        eno = int(input("메뉴 번호 선택 : "))

        if eno == 1:
            pass
        elif eno == 2:
            pass
        elif eno == 3:
            pass
        elif eno == 4:
            pass
        elif eno == 5:
            pass
        elif eno == 6:
            pass
        elif eno == 7:
            pass
        elif eno == 8:
            pass
        elif eno == 0:
            return
        else:
            print("올바른 메뉴를 선택하세요\n")
