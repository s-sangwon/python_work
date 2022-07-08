import common.oracle_db as oradb


def insert(tp_value):
    conn = oradb.connect()
    query = "insert into notice values (seq_notice_no.nextval, \
            :1, :2, default, :3, :4, default)"
    cursor = ''
    try:
        # c##student.employee 테이블에 새 행 추가 처리
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        oradb.commit(conn)
        print("새로운 notice가 등록되었습니다.")
    except Exception as msg:
        print("insert() 쿼리 실행 에러 : ", msg)
        conn.rollback()
    finally:
        cursor.close()
        oradb.close(conn)

def select_all():
    conn = oradb.connect()
    query = "select * from notice"
    result = []
    try:
        # c##student.notice 테이블 전체 조회해 와서,
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

def update(tp_value):
    conn = oradb.connect()
    print(tp_value)
    query = "update notice set notice_title=:1, notice_content=:2, notice_upfile=:3 where notice_no=:4"
    cursor = ''
    try:
        # c##student.notice 테이블에 내용 수정 처리
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        oradb.commit(conn)
        print("notice 수정 완료.")
    except Exception as msg:
        print("update() 쿼리 실행 에러 : ", msg)
        conn.rollback()
    finally:
        cursor.close()
        oradb.close(conn)

def delete_notice(tp_value):
    conn = oradb.connect()
    query = "delete from notice where notice_no = :1"
    cursor = ''
    try:
        # c##student.notice 테이블에 notice 삭제 처리
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        oradb.commit(conn)
        print(tp_value[0], "번 notice 삭제 완료.")
    except Exception as msg:
        print("delete() 쿼리 실행 에러 : ", msg)
        conn.rollback()
    finally:
        cursor.close()
        oradb.close(conn)

def select_search_title(tp_value):
    conn = oradb.connect()
    query = "select * from notice where notice_title LIKE '%'||:1||'%'"
    result = []
    cursor = ''
    try:
        # c##student.notice 테이블 제목에 해당하는
        # notice를 조회해서 결과에 담기
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        result = cursor.fetchall()
    except Exception as msg:
        print("select_search_title() 쿼리 실행 에러 : ", msg)
    finally:
        cursor.close()
        oradb.close(conn)
    return result

def select_search_date(tp_value):
    conn = oradb.connect()
    query = "select * from notice where TRUNC(notice_date) = TO_DATE(:1,'YYYY-MM-DD')"
    result = []
    cursor = ''
    try:
        # c##student.notice 테이블 날짜에 해당하는
        # notice를 조회해서 결과에 담기
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        result = cursor.fetchall()
    except Exception as msg:
        print("select_search_date() 쿼리 실행 에러 : ", msg)
    finally:
        cursor.close()
        oradb.close(conn)
    return result

def select_search_writer(tp_value):
    conn = oradb.connect()
    query = "select * from notice where notice_writer LIKE '%'||:1||'%'"
    result = []
    cursor = ''
    try:
        # c##student.notice 테이블 작성자아이디에 해당하는
        # notice를 조회해서 결과에 담기
        cursor = conn.cursor()
        cursor.execute(query, tp_value)
        result = cursor.fetchall()
    except Exception as msg:
        print("select_search_writer() 쿼리 실행 에러 : ", msg)
    finally:
        cursor.close()
        oradb.close(conn)
    return result