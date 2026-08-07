import sqlite3
import time
import requests

# 定義資料庫路徑與 API 目標網址
DB_PATH = "Step_10/scraped_quotes.db"
API_URL = "https://quotes.toscrape.com/api/quotes?page=1"

def init_db():
    """初始化資料表"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                content TEXT UNIQUE NOT NULL,
                tags TEXT
            )
        """)
        conn.commit()
    print("資料庫與 quotes 資料表已準備就緒！")


def fetch_and_save_data():
    """抓取資料並存入資料庫"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    print("開始爬取 API 資料...")
    time.sleep(1)  # 禮貌延遲

    response = requests.get(API_URL, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()
    raw_quotes = data.get("quotes", [])

    # 連接資料庫準備寫入
    saved_count = 0
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        for item in raw_quotes:
            content = item.get("text", "").strip()
            author = item.get("author", {}).get("name", "Unknown").strip()
            tags = ", ".join(item.get("tags", []))

            # 使用 INSERT OR IGNORE 避免重複存入相同的名言 (依據 content UNIQUE)
            cursor.execute(
                """
                INSERT OR IGNORE INTO quotes (author, content, tags)
                VALUES (?, ?, ?)
            """,
                (author, content, tags),
            )

            if cursor.rowcount > 0:
                saved_count += 1

        conn.commit()

    print(f"成功寫入 {saved_count} 筆新資料到資料庫！")


def verify_saved_data():
    """驗證資料庫內容"""
    print("\n=== 🔍 查詢資料庫中的名言紀錄 ===")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, author, content FROM quotes LIMIT 3")
        rows = cursor.fetchall()
        for row in rows:
            q_id, author, content = row
            print(f"[{q_id}] {author}：\n    {content}\n")

# 執行主程序
if __name__ == "__main__":
    init_db()
    fetch_and_save_data()
    verify_saved_data()