# emp_controller.py
# 모듈 표기 : employee.emp_controller

# View --> Controller ->> Model
# View 에서 Controller 기능 사용 : import
# Controller 에서 Model 기능 사용 : import

# Controller 가 하는 일:
# 뷰에서 전달온 데이터의 검사 또는 가공 처리 담당
# 모델의 기능 연결 실행 : 뷰에서 받은 값 전달함
# 모델의 처리 결과 리턴 받아서, 뷰로 다시 리턴함
import employee.emp_model as model

# model 의 select_all() 구동용 함수
def select_list():
    emp_list = model.select_all()
    return emp_list

# model 의 select_one() 구동용 함수
def select_emp(tp_value):
    emp_tp = model.select_one(tp_value)
    return emp_tp

# model 의 insert() 구동용 함수
def insert_emp(tp_value):
    model.insert(tp_value)
    print("새로운 직원 정보가 등록되었습니다.")
    return

# model 의 update() 구동용 함수
def update_emp(tp_value):
    model.update(tp_value)
    print("직원 정보가 수정되었습니다.")
    return

# model 의 delete() 구동용 함수
def delete_emp(tp_value):
    model.delete(tp_value)
    print("직원 정보가 삭제되었습니다.")
    return

# model 의 select_search_name() 구동용 함수
def search_name(tp_value):
    emp_list = model.select_search_name(tp_value)
    return emp_list

# model 의 select_search_job() 구동용 함수
def search_job(tp_value):
    emp_list = model.select_search_job(tp_value)
    return emp_list


# model 의 select_search_dept() 구동용 함수
def search_deptid(tp_value):
    emp_list = model.select_search_deptid(tp_value)
    return emp_list