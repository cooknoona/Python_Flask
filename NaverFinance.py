import requests  # HTTP 프로토콜 웹페이지 문서 불러오기
from bs4 import BeautifulSoup  # HTML 파싱
import pandas as pd  # 2차원 데이터를 가공하기 위해 사용
from flask import Flask

app = Flask(__name__)

@app.route("/stock/<code>")
def crawl(code):
    try:
        url = f"https://finance.naver.com/item/main.naver?code={code}"
        res = requests.get(url)
        res.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        bs_obj = BeautifulSoup(res.text, "html.parser")

        # 현재가
        div_today = bs_obj.find("div", {"class": "today"})
        em = div_today.find("em")
        price = em.find("span", {"class": "blind"}).text

        # 회사 정보
        h_company = bs_obj.find("div", {"class": "h_company"})
        name = h_company.a.text.strip()
        div_description = h_company.find("div", {"class": "description"})
        code = div_description.span.text.strip()

        # 거래량
        table_no_info = bs_obj.find("table", {"class": "no_info"})
        tds = table_no_info.find_all("td")
        volume = tds[2].find("span", {"class": "blind"}).text

        # HTML 반환
        html = f"""
        <html>
            <head><title>주식 정보</title></head>
            <body>
                <h1>이름: {name}</h1>
                <h3>가격: {price}</h3>
                <h3>코드: {code}</h3>
                <h3>거래량: {volume}</h3>
            </body>
        </html>
        """
        return html, 200, {'Content-Type': 'text/html'}

    except Exception as e:
        return f"<h1>주식 정보를 가져오는 중 오류가 발생했습니다: {e}</h1>", 500

if __name__ == "__main__":
    app.run(debug=True)

#         # 결과 딕셔너리 생성
#         dic = {"price": price, "name": name, "code": code, "volume": volume}
#         return dic
#     except Exception as e:
#         print(f"코드 {code} 크롤링 중 오류 발생: {e}")
#         return None
#
# # 주식 코드 리스트
# codes = ["035720", "005930", "051910", "000660"]
# rst_list = []
#
# # 크롤링 수행
# for e in codes:
#     rst = crawl(e)
#     if rst:  # None이 아닌 경우에만 추가
#         rst_list.append(rst)
#
# # 데이터프레임 생성 및 엑셀 저장
# if rst_list:
#     df = pd.DataFrame(rst_list)
#     df.to_excel("주식_거래_정보.xlsx", index=False)
#     print("엑셀 파일 저장 완료: 주식_거래_정보.xlsx")
# else:
#     print("크롤링 결과가 없습니다.")
