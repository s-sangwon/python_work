# test_oracle.py
# 오라클에 update 문 실행 테스트

#1.
import cx_Oracle
import os

#2. 드라이브 등록은 프로젝트 실행시 한번만 처리하면 됨.
cx_Oracle.init_oracle_client("")

#3.
conn = cx_Oracle.connect("c##student/student@localhost:1521/xe")
print(conn)

# query = """update employee
#             set job_id = 'J5', dept_id = '30', emp_name='김철슉'
#             where emp_id = (select max(emp_id) from employee)"""

# 수정할 값을 키보드로 입력받아서 쿼리문에 적용 실행하는 경우
# 주의 : 쿼리문에 적용할 값들은 튜플로 저장함
emp_id = input("수정할 대상 직원의 사번 : ")
job_id = input("변경할 직급코드 : ").upper()
dept_id = input("변경할 부서콛 : ")
salary = int(input("변경할 급여 : "))
bonus_pct = float(input("변경할 보너스포인트 : "))

tp_value = (job_id, dept_id, salary, bonus_pct,emp_id )
# 주의 : 쿼리문 적용 순서대로 튜플에 저장되어야함
# 주의 : 튜플 적용 쿼리문일 때는 따옴표 3개 사용 안됨
query = "update employee set job_id = :1,  \
        dept_id = :2, salary=:3, bonus_pct=:4 \
        where emp_id = :5"

#4
cursor = conn.cursor()
# cursor.execute(query)
cursor.execute(query, tp_value)
conn.commit()

#5
cursor.close()
conn.close()