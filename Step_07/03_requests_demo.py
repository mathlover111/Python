import requests

# ask for API
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# HTTP  (200success、404notfound、500serverwhrong)
print(f"網路連線狀態碼：{response.status_code}")

if response.status_code == 200:
    print("【success catch】")
    print(response.text)
else:
    print("fail！")
