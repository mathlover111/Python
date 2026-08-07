import requests
# Telegram Bot 設定參數
# 請替換成你從 @BotFather 拿到的 Token 與 @userinfobot 拿到的 Chat ID
TELEGRAM_BOT_TOKEN = " "  # 範例："123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ"
TELEGRAM_CHAT_ID = ""     # 範例："987654321"
# 定義發送訊息的函式
def send_telegram_message(message: str, token: str, chat_id: str) -> bool:
    """
    透過 Telegram Bot API 發送文字訊息至指定的 Chat ID
    """
    # 如果使用者還沒填入真實的 Token，切換為模擬測試模式
    if token == "YOUR_BOT_TOKEN_HERE" or chat_id == "YOUR_CHAT_ID_HERE":
        print("⚠️  [模擬模式] 未偵測到有效的 Telegram Credentials，進行發送模擬：")
        print(f"📱 欲發送的目標 Chat ID: {chat_id}")
        print(f"💬 訊息內容：\n{message}")
        print("✅  [模擬模式] 訊息模擬發送成功！\n")
        return True

    # 正式 API 發送邏輯
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"  # 支援 Markdown 粗體、斜體格式
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        res_data = response.json()

        if res_data.get("ok"):
            print("[Telegram API] 訊息成功發送到手機 Telegram！")
            return True
        else:
            print(f"[Telegram API] 發送失敗：{res_data}")
            return False

    except requests.RequestException as e:
        print(f"[網絡異常] 發送 Telegram 訊息時發生錯誤：{e}")
        return False
# 主程式測試
if __name__ == "__main__":
    # 組合一段結構化的推播訊息 (支援 Markdown 語法)
    test_notice = (
        "*Python 自動化通知系統*\n"
        "------------------------------\n"
        "🟢 *系統狀態*：正常運作中\n"
        "📊 *今日爬蟲數據*：已成功抓取 20 筆最新新聞\n"
        "⏰ *發送時間*：即時推播\n"
        "------------------------------\n"
        "_這是一則來自 Python Step 12 的自動推播測試訊息！_"
    )

    print("正在嘗試發送 Telegram 推播通知...")
    send_telegram_message(
        message=test_notice,
        token=TELEGRAM_BOT_TOKEN,
        chat_id=TELEGRAM_CHAT_ID
    )