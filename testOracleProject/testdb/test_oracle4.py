# test_oracle4.py
# oracle 연동 & delete 쿼리문 테스트

# 1.
import cx_Oracle


# 2.
conn = cx_Oracle.connect("c##student/student@localhost:1521/xe")
print(conn)

# 3.
# 삭제할 직원의 사번을 키보드로 입력받아 쿼리문에 적용 처리
emp_id = input("삭제한 직원의 사번 입력 : ")
tp_value = (emp_id,)


query = "delete from employee where emp_id = :1"

# 4.
cursor = conn.cursor()
cursor.execute(query, tp_value)
print(cursor)
conn.commit

cursor.close()
conn.close()
