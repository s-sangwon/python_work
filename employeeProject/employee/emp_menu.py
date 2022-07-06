# employee\emp_menu.py
# 모듈 표기 : employee.emp_menu
import employee.emp_controller as econtroll

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
            econtroll.insert_emp(input_employee())
        elif eno == 2:
            emp_list = econtroll.select_list()
            print("현재 직원 전체 수 : ", len(emp_list))
            emp_print(emp_list)
        elif eno == 3:
            # empid = input("조회할 직원 사번 : ")
            # tp_value = (empid, )
            # emp = econtroll.select_emp(tp_value)
            # print(emp)
            print(econtroll.select_emp((input("조회할 직원 사번 : "), )))
        elif eno == 4:
            econtroll.update_emp(modify_employee())
        elif eno == 5:
            emp_id = input('삭제할 직원의 사번 : ')
            econtroll.delete_emp((emp_id, ))
        elif eno == 6:
            empname = input("조회할 직원 이름 (이름 패턴): ")
            tp_value = (empname, )
            emp_list = econtroll.search_name(tp_value)
            emp_print(emp_list)
            # print(econtroll.search_name((input("조회할 직원 이름 (이름 패턴): "),)))
        elif eno == 7:
            empid = input("조회할 직원 직급 : ")
            tp_value = (empid, )
            emp_list = econtroll.search_job(tp_value)
            emp_print(emp_list)
            # print(econtroll.search_job((input("조회할 직원 직급 : "),)))
        elif eno == 8:
            empid = input("조회할 직원 부서코드 : ")
            tp_value = (empid, )
            emp_list = econtroll.search_deptid(tp_value)
            emp_print(emp_list)
            # print(econtroll.search_deptid((input("조회할 직원 부서코드 : "),)))
        elif eno == 0:
            return
        else:
            print("올바른 메뉴를 선택하세요\n")
# ---------------------------------------------------

# 리턴받은 전체 직원 출력용 함수
def emp_print(elist):
    for emp in elist:
        # print(emp)
        # 컬럼값 개별 출력 처리
        for col in emp:
            print(col,end=", ")
        print()

# 새로 등록할 직원정보 입력받는 함수
def input_employee():
    print('새로 등록할 직원 정보를 순서대로 입력하세요.')
    emp_name = input('직원 이름 : ')
    emp_no = input('주민등록번호 : ')
    email = input('이메일 : ')
    phone = input('전화번호 [- 빼고 입력]: ')
    job_id = input('직급코드 : ').upper()
    salary = int(input('급여 : '))
    bonus = float(input('보너스포인트 : '))
    marriage = input('결혼여부 [기혼:Y, 미혼:N]: ').upper()
    mgr_id = input('관리자 사번 : ')
    dept_id = input('부서코드 : ')
    #tp_value = (emp_name, emp_no, email, phone, job_id, salary, bonus, marriage, mgr_id, dept_id)
    return (emp_name, emp_no, email, phone, job_id, salary, bonus, marriage, mgr_id, dept_id)
def modify_employee():
    print('변경할 직원 정보를 순서대로 입력하세요.')
    empid = input('대상 직원 사번 : ')
    email = input('이메일 : ')
    phone = input('전화번호 [- 빼고 입력]: ')
    job_id = input('직급코드 : ').upper()
    dept_id = input('부서코드 : ')
    salary = int(input('급여 : '))
    bonus = float(input('보너스포인트 : '))
    marriage = input('결혼여부 [기혼:Y, 미혼:N]: ').upper()
    mgr_id = input('관리자 사번 : ')

    # tp_value = (emp_name, emp_no, email, phone, job_id, salary, bonus, marriage, mgr_id, dept_id)
    return (email, phone, job_id, dept_id, salary, bonus, marriage, mgr_id, empid)