# test_oracle.py
# 오라클과 파이썬 연동

# 패키지 설치 : cx-Oracle
# 오라클 사에서 제공하는 파이썬과 오라클을 연동하기 위한 드라이버
# 파일 다운받아야 함 인스턴트클라이언트
# 폴도 경로를 짧게 하기 위해서 폴더 이동 시킴
# c#\\instantclient_21_6

# 1. 사용할 패키지(모듈) 임포트함
# 설치 패키지 : cs-Oracle, 임포트할 모듈명 : cx_Oracle
import cx_Oracle
import os

# 2. 오라클 드라이버(instantclient) 등록
# 방법 1 : 환경변수 path 에 등록 (파이썬 코드로 등록할 수 있음)
location = "C:\instantclient_21_6"
os.environ["PATH"] = location + ";" + os.environ["PATH"]


# 방법 2 : 오라클 코드 초기 설정으로 지정
cx_Oracle.init_oracle_client(lib_dir="C:\instantclient_21_6")

# 3. 오라클 연결하기 위한 값 준비하고 연결 실행
dbURL = "localhost:1521/xe"
dbUSER = "c##student"
dbPASSWORD = "student"

conn = cx_Oracle.connect(dbUSER, dbPASSWORD, dbURL)
# conn = cx_Oracle.connect("c##student", "student", "localhost:1521/xe")
# conn = cx_Oracle.connect("c##student/student@localhost:1521/xe")
print(conn) # 연결 확인

# 4 쿼리문 준비하기
query = 'select * from c##student.employee'

# 5. 쿼리문 실행시키기 위한 객체 준비하고 실행 처리
# cursor : 준비된 쿼리문을 연결된 db로 전송해서 실행시키는 객체임
cursor = conn.cursor()      # 연결된 db 정보로 커서 객체를 생성함
cursor.execute(query)   # 쿼리문 보내서 실행
#result = cursor.fetchall() # 조회된 모든 결과를 받음
# 커서가 실행된 쿼리문의 결과를 받음
# select 쿼리문을 실행시켰다면, 결과집함(ResultSet)을 커서가 받음
# DML 문은 처리된 행갯수를 커서가 받음


for row in cursor:
    print("행이 가진 컬럼 갯수 : ", len(row), type(row))
    # 컬럼별로 데이터 추출 처리
    emp_id = row[0]
    emp_name = row[1]
    emp_no = row[2]
    email = row[3]
    phone = row[4]
    hire_date = row[5]
    job_id = row[6]
    salary =row[7]
    bonus_pct =row[8]
    marriage =row[9]
    mgr_id =row[10]
    dept_id =row[11]

    # print(emp_id, emp_name, emp_no, email, phone, hire_date ...)
    # index 를 이용해서 출력 처리
    for i in range(len(row)): # 0~11
        print(row[i], end=", ")
    print()

# 작업이 끝나면 반드시 clolse() 함
cursor.close()
conn.close()