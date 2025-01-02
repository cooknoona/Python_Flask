import json
from fileinput import close
from json import loads

# [] : 리스트, 시퀀스형 데이터를 관리, 크기를 지정하지 않아도 자동 크기 조절, Mutable(읽고 쓰기 가능)
# {} : 딕셔너리, 키와 값의 쌍으로 구성되어 있음
# () : 튜플, 시퀀스형 데이터, Immutable(읽기만 가능), Packing / Unpacking

person = 10, "M", "경기도 파주시", "이국형", True    # Packing
print(person)
age, gender, addr, name, adult = person # Unpacking
print(person)
# print(divmod(23, 5))

customer = {
    "id" : 100,
    "name" : "이국형",
    "history" : [
        {"date" : "2023-05-05", "Product" : "iPhone 14 Pro"},
        {"date" : "2024-04-01", "Product" : "iPhone 16 Pro"}
    ]
}
print(customer)

# Python 객체 -> JSON 문자열로 반환
# json.dumps : 객체를 JSON 문자열로 반환
# ensure_ascii = False : ASCII 문자가 아님을 의미
jsonString = json.dumps(customer, ensure_ascii = False, indent = 4)
print(jsonString)

dict = json.loads(jsonString)
print(dict["name"])
for e in dict["history"]:
    print(e["date"], e["Product"])

# 파이썬의 for문 range() 기반과, 시퀀스형 데이터를 순회하는 for문이 있음
for i in range(10): # range(시작인덱스, 종료인덱스, 증감값)
    print(f"{i}", end = " ")

cars = ["모델 Y", "X4", "폴스타4", "EV3", "마칸", "카이엔", "팬텀", "에어로시티"]
for e in cars:  # 시퀀스형(리스트, 튜플, 문자열, 입력) 데이터 순회
    print(f"{e}", end = " ")
print()
# 범위 기반 for 로 cars 출력하기
for i in range(0, len(cars)):
    print(f"{cars[i]}", end = " ")
    
# CSV 파일 : Comma-Separator-Value, 콤마로 구분된 텍스트 형태의 파일
import csv
f = open("output.csv", "w", encoding="utf-8", newline="")
wr = csv.writer(f)
wr.writerow([1, "안유진", "서울시 강남구 삼성동", "리더"])
wr.writerow([2, "장원영", "서울시 강남구 삼성동", "프론트엔드"])
wr.writerow([3, "이서", "서울시 강남구 삼성동", "백엔드"])
f.close()
