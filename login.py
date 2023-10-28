import requests
import json

def send_api(path, method):
    API_HOST = "http://kwebsite.kr/__api/_login/login.check.php"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "id": "value1",
        "password": "value2",
        "ip": "value3",
    }
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)
  

# 호출 예시
send_api("/test", "POST")