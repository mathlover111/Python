import requests
from bs4 import BeautifulSoup

# 設定要爬取的目標網址
url = "https://news.ycombinator.com/"

# 設定 Request Headers，加入 User-Agent 偽裝成一般的 Chrome 瀏覽器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    # 3. 發送 GET 請求取得網頁內容
    print(f"📡 正在連線至：{url} ...")
    response = requests.get(url, headers=headers, timeout=10)

    # 檢查 HTTP 狀態碼是否成功
    if response.status_code == 200:
        print("成功存取網頁，開始解析標題...\n")
        
        # 解析 HTML 原始碼
        soup = BeautifulSoup(response.text, "html.parser")

        # 使用 CSS Selector 抓取所有新聞標題 (Hacker News 的標題 class 為 .titleline > a)
        news_items = soup.select(".titleline > a")

        print("=== 今日熱門技術新聞 (前 10 則) ===")
        for index, item in enumerate(news_items[:10], start=1):
            title = item.text
            link = item["href"]
            print(f"{index:2d}. {title}")
            print(f"    🔗 連結：{link}\n")

    else:
        print(f"連線失敗，HTTP 狀態碼：{response.status_code}")

except Exception as e:
    print(f"發生錯誤：{e}")