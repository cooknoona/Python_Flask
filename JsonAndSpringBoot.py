import requests # http 통신을 위한 모듈
import json

member = {
    "email" : "test1234",
    "pw" : "test123456",
    "name" : "이국형",
    "imgPath" : ""
}

# 서버 URL 및 헤더 설정
url = "http://localhost:8111/auth/signUp"
headers = {"Content-Type" : "application/json"}

# POST 요청 보내기
response = requests.post(url, data = json.dumps(member), headers = headers)

# 응답 처리
if response.status_code == 200:
    data = response.json()
    print(f"아이디 : {data['userId']}")
    print(f"이름 : {data['name']}")
    print(f"가입일 : {data['createdAt']}")
else:
    print("회원 가입에 실패 했습니다.")