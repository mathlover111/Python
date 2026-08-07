import time
import requests

# 這是該網站背後真實提供數據的 API 網址 (回傳 JSON 格式)
api_url = "https://quotes.toscrape.com/api/quotes?page=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    print(f"正在請求動態 API 數據：{api_url} ...")

    # 模擬做個有禮貌的爬蟲，請求前稍微等待 1 秒
    time.sleep(1)

    response = requests.get(api_url, headers=headers, timeout=10)
    response.raise_for_status()

    # 將回傳的 JSON 字串直接解析為 Python 的字典 (dict) 或列表 (list)
    data = response.json()

    print("成功取得 API 資料！開始解析 JSON...\n")

    # 解析 JSON 內容
    quotes = data.get("quotes", [])
    has_next = data.get("has_next", False)

    print(f"=== 名人名言清單 (共 {len(quotes)} 則) ===")
    for idx, item in enumerate(quotes[:5], start=1):
        text = item.get("text")
        author = item.get("author", {}).get("name")
        tags = ", ".join(item.get("tags", []))

        print(f"{idx}. 「{text}」")
        print(f"作者：{author}")
        print(f"標籤：{tags}\n")

    print(f"是否還有下一頁資料？{'有' if has_next else '沒有'}")

except requests.exceptions.RequestException as e:
    print(f"API 請求失敗：{e}")
except Exception as e:
    print(f"解析資料時發生錯誤：{e}")