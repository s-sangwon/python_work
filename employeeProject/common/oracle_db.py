# common\oracle_db.py
# 모듈명 표현 : common.oracle_db
# 모듈이 제공하는 기능 :
# - 드라이브 등록
# - 오라클 연결기능
# - 트랙잭션 처리
# - 닫기

# 패키지 설치하고 임포트 선언
import cx_Oracle

# 사용자 정의 변수
dbURL = "localhost:1521/xe"
dbUSER = "c##student"
dbPASSWD = "student"

#각 기능별 함수 정의
# 오라클 드라이브 초기 등록 설정 함수
def oracle_init():
    #드라이브 등록 함수
    cx_Oracle.init_oracle_client(lib_dir="C:\instantclient_21_6")

# 오라클 연결 함수
def connect():
    try:
        conn = cx_Oracle.connect(dbUSER, dbPASSWD, dbURL)
        conn.autocommit(False) # 자동 커밋 해제
        return conn
    except Exception as msg:
        print("오라클 연결 에러 : ", msg)

# connection close

def close(conn):
    try:
        conn.close()
    except Exception as msg:
        print("오라클 연결 해제 에러 : ",msg)

# commit 함수
def commit(conn):
    try:
        conn.commit()
    except Exception as msg:
        conn.rollback()
        print("오라클 트랜잭션 커밋 에러 : ", msg)

# rollback 함수
def rollback(conn):
    try:
        conn.rollback()
    except Exception as msg:
        print("오라클 트랜잭션 롤백 에러 : ", msg)