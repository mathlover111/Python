import json
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

data = response.json()

print(f"資料轉成字典後的型態：{type(data)}")

print("\n--- 提取特定欄位 ---")
print(f"待辦事項 ID: {data['id']}")
print(f"待辦事項標題: {data['title']}")
print(f"是否已完成: {data['completed']}")
