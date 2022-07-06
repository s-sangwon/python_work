# employee\emp_model.py
# 모듈 표기 : employee.emp_model
# 애플리케이션(프로젝트) 구조 지정시, 디자인 패턴(개발 방법론) 적용함
# MVC 패턴 일반적임
# M (Model) : 데이터베이스 연동 후 쿼리문 실행 처리와 관련된 파일(클래스)
#           database access 담당
# V (View) : 프로그램이 실행될 때 보여지는 화면 처리 담당 하는 파일(클래스)
# C (Controller) : 뷰와 모델의 중간 연결자
# 실행 흐름 : view --> controller --> model : db 전송 처리
#           model 처리 결과 리턴 --> controller 리턴-> view 출력처리

# 모델(Model)이 하는 일(기능)
# db 연결, 커서 객체 생성, 쿼리문 작성, 쿼리문 db로 전송 실행,
# select 조회 결과 리턴

import common.oracle_db as oradb

# 전체 직원 조회용 함수
def select_all():
    conn = oradb.connect()
    query = "select * from employee"
    result = []
    #cursor = None
    try:
        # c##student.employee 테이블 전체 조회해 와서,
        # result 에 결과 담기
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception as msg:
        print("select_all() 쿼리 실행 에러 : ", msg)
        return result # 빈 리스트가 리턴됨
    finally:
        cursor.close()
        oradb.close(conn)

    return result

def select_one(tp_value):
    conn = oradb.connect()
    query = "select * from employee where emp_id=:1"
    result = ()
    # cursor = None
    try:
        # c##student.employee 테이블 사번에 해당하는,
        # 직원 조회해서 result 에 결과 담기
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        result = cursor.fetchone()
    except Exception as msg:
        print("select_one() 쿼리 실행 에러 : ", msg)
        return result
    finally:
        cursor.close()
        oradb.close(conn)

    return result



def insert(tp_value):
    conn = oradb.connect()
    query = "insert into employee values (seq_eid.nextval, \
            :1, :2, :3, :4, default, :5, :6, :7, :8, :9, :10)"
    cursor = ''
    try:
        # c##student.employee 테이블에 새 행 추가 처리
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        oradb.commit(conn)
    except Exception as msg:
        print("insert() 쿼리 실행 에러 : ", msg)
        conn.rollback()
    finally:
        cursor.close()
        oradb.close(conn)


def update(tp_value):
    conn = oradb.connect()
    query = "update employee set email=:1, phone = :2,  \
            job_id = :3, dept_id = :4, salary = :5, \
            bonus_pct = :6, marriage = :7, mgr_id= :8 " \
            "where emp_id = :9"
    cursor = ''
    try:
        # c##student.employee 테이블 직원 정보 수정 처리
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        oradb.commit(conn)
    except Exception as msg:
        print("update() 쿼리 실행 에러 : ", msg)
        conn.rollback()
        return
    finally:
        cursor.close()
        oradb.close(conn)


# 사번으로 직원 삭제 처리용 함수
def delete(tp_value):
    conn = oradb.connect()
    query = "delete from employee where emp_id=:1"
    try:
        # c##student.employee 테이블 직원 정보 삭제 처리
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        oradb.commit(conn)
    except Exception as msg:
        print("delete() 쿼리 실행 에러 : ", msg)
        conn.rollback()
        return
    finally:
        cursor.close()
        oradb.close(conn)
    return

# 이름으로 검색 처리용 함수
def select_search_name(tp_value):
    conn = oradb.connect()
    query = "select * from employee " \
            "where emp_name like '%'||:1||'%'"
    result = []
    cursor = ''
    try:
        # c##student.employee 테이블 이름에 해당되는
        # 직원들 조회해 와서, result 에 결과 담기
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        result = cursor.fetchall()
    except Exception as msg:
        print("select_search_name() 쿼리 실행 에러 : ", msg)
    finally:
        cursor.close()
        oradb.close(conn)

    return result

# 직급으로 검색 처리용 함수
def select_search_job(tp_value):
    conn = oradb.connect()
    query = "select * from employee where job_id= :1 "
    result = []
    cursor = ''
    try:
        # c##student.employee 테이블 직급으로 직원들 조회해 와서,
        # result 에 결과 담기
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        result = cursor.fetchall()
    except Exception as msg:
        print("select_search_job() 쿼리 실행 에러 : ", msg)
    finally:
        cursor.close()
        oradb.close(conn)

    return result

# 직급으로 검색 처리용 함수
def select_search_deptid(tp_value):
    conn = oradb.connect()
    query = "select * from employee where dept_id = :1"
    result = []
    cursor = ''
    try:
        # c##student.employee 테이블 부서에 해당하는
        # 직웓늘 조회해 와서, result 에 결과 담기
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        result = cursor.fetchall()
    except Exception as msg:
        print("select_search_deptid() 쿼리 실행 에러 : ", msg)
    finally:
        cursor.close()
        oradb.close(conn)

    return result