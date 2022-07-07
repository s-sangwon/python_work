# test_oracle2.py
# oracle 연동과 insert 문 실행 테스트

# 1.
import cx_Oracle
import os
location = "C:\instantclient_21_6"
os.environ["PATH"] = location + ";" + os.environ["PATH"]


cx_Oracle.init_oracle_client("C:\instantclient_21_6")

dbURL = "localhost:1521/xe"
dbUSER = "c##student"
dbPASSWORD = "student"

conn = cx_Oracle.connect(dbUSER, dbPASSWORD, dbURL)
print(conn)
query2 =  "insert into c##student.employee values('299', '홍길동', '123456-2345678', 'hong@kkk.com', SYSDATE(), \
         'J4', 2500000, NULL,'Y',NULL,20)"

query = "insert into employee  \
            values(seq_eid.nextval, '홍길동', '871125-1234567', 'hong77@test.org', '01012345678', default,  \
             'J7', 3800000, 0.05, default, null, '30')"

# insert 구문에 사용할 값을 외부 데이터 이용할 경우 (키보드 입력)
# 주의 외부 데이터는 튜플로 저장해야 함
# 키보드로 값 입력받아 튜플에 저장 처리 예 :
emp_name = input("직원 이름 : ")
emp_no = input("주민등록번호 : ")
email = input("이메일 : ")
phone = input("전화번호 [-빼고 입력] : ")
salary = int(input("급여 : "))

tp_value = (emp_name, emp_no, email, phone, salary)

# 외부값 적용 쿼리문 작성
query = "insert into employee \
            values (seq_eid.nextval, :1, :2, :3, :4, default, null, :5, null, default, null, null)"
#4
cursor = conn.cursor()
# cursor.execute(query)
# 쿼리문에 튜플의 값들을 적용해서 실행시킴
cursor.execute(query, tp_value)
print(cursor)

#5
cursor.close()
conn.commit()
conn.close()