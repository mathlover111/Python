import requests

# 向 API 發送網路請求
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# HTTP 狀態碼 (200成功、404找不到、500伺服器錯誤等)
print(f"網路連線狀態碼：{response.status_code}")

if response.status_code == 200:
    print("【成功從網路抓取到的資料】")
    print(response.text)
else:
    print("連線失敗！")