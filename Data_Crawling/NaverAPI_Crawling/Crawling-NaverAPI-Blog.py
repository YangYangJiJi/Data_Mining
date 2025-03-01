import os
import sys
import urllib.request

client_id = "(client ID)"
client_secret = "(client Secret)"
encText = urllib.parse.quote("월드컵") #검색할 단어

url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

#url접속과 검색 요청하기 
response = urllib.request.urlopen(request) 
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
