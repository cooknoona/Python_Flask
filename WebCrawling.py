from bs4 import BeautifulSoup

html = '''
<html>
    <table border=1> 
        <tr>
            <td> 항목 </td> 
            <td> 2013 </td> 
            <td> 2014 </td> 
            <td> 2015 </td>
        </tr> 
        <tr>
            <td> 매출액 </td> 
            <td> 100 </td> 
            <td> 200 </td>
            <td> 300 </td>
        </tr> 
    </table>
</html> 
'''
soup = BeautifulSoup(html, 'html.parser')
result = soup.select('td')
print(result)
for e in result :
    print(e.text, end = " ")

result2 = soup.select('ul li')
print(result2)
for e in result2 :
    print(e.text, end = " ")

# 특정 요소 찾기 (fin 와 find_all)
# find : 조건에 맞는 첫 번째 요소를 반환
# find_all : 조건에 맞는 모든 요소를 반환

import requests
response = requests.get("https://naver.com")
soup = BeautifulSoup(response.text, 'lxml')

print(soup.find(attrs={"class": "shopping_area"}))