import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
# 設定區 (可填入你的 Telegram Token & Chat ID，未填則自動啟用模擬推播)
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"

def fetch_latest_news() -> list:
    """模擬/實作抓取最新頭條新聞"""
    url = "https://news.ycombinator.com/" # Hacker News 示範網站
    headers = {"User-Agent": "Mozilla/5.0"}
    news_items = []

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            titles = soup.select(".titleline > a")[:3]  # 只取前 3 條最新新聞
            for idx, title in enumerate(titles, 1):
                news_items.append(f"{idx}. {title.text}")
    except Exception as e:
        print(f"爬蟲抓取失敗：{e}")

    # 若抓取失敗或無數據，提供預設備用新聞數據
    if not news_items:
        news_items = [
            "1. Python 3.12 效能大幅提升焦點解析",
            "2. AI 自動化機器人應用趨勢報告",
            "3. Web 爬蟲資安與防禦機制探討"
        ]
    
    return news_items

def send_telegram_push(message: str):
    """發送訊息至 Telegram 或在模擬模式列印"""
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or TELEGRAM_CHAT_ID == "YOUR_CHAT_ID_HERE":
        print("\n--------------------------------------------------")
        print("📱 【模擬 Telegram 推播通知】")
        print(message)
        print("--------------------------------------------------\n")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=5)
        print("[Telegram API] 自動情報已成功推播至手機！")
    except Exception as e:
        print(f"推播失敗：{e}")

# --------------------------------------------------
# 4. 核心三合一流程：定時發動的整合任務
def auto_reporter_job():
    """排程器會自動按時執行的總核心任務"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{current_time}] 觸發自動化任務：開始抓取最新新聞...")

    # Step A: 執行爬蟲
    news_list = fetch_latest_news()
    news_content = "\n".join(news_list)

    # Step B: 組合訊息
    report = (
        f"🤖 *【每日自動情報早報】*\n"
        f"⏰ *報告時間*：{current_time}\n"
        f"----------------------------------\n"
        f"📰 *焦點新聞頭條*：\n{news_content}\n"
        f"----------------------------------\n"
        f" _此訊息由 Python 背景排程器自動抓取發送_"
    )

    # Step C: 發送推播
    send_telegram_push(report)

# --------------------------------------------------
# 5. 主程式與排程啟動
if __name__ == "__main__":
    scheduler = BackgroundScheduler()

    # 設定每 10 秒自動執行一次「爬蟲+組合+推播」任務 (方便測試展示)
    scheduler.add_job(
        auto_reporter_job,
        trigger="interval",
        seconds=10,
        id="auto_reporter"
    )

    scheduler.start()
    print("【全自動情報祕書已上線】")
    print("排程設定：每 10 秒自動爬取最新新聞並發送推播報告。")
    print("按下 Ctrl + C 可隨時停止程式。\n")

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("\n自動監控系統已安全關閉！")