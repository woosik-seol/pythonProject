from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

counter = 0
for location in soup.select("location"):
    counter += 1
    print(counter)
# 39
# 40
# 41

print(type(soup.select("location")))
# <class 'bs4.element.ResultSet'>