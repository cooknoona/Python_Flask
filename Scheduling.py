# Scheduling? : 특정 시간에 작업을 예약하고 실행하는 프로세스
import schedule # 스케쥴
import time     # 시간
import requests # http 요청
from bs4 import BeautifulSoup   # 파싱

def perform_web_crawling():
    response = requests.get("http://www.naver.com")
    soup = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("스케쥴링을 시작 합니다")