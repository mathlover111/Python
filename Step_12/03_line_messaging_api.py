import requests
# LINE Messaging API 設定參數
# 可在 LINE Developers Console 申請 Channel Access Token 與 User ID
LINE_CHANNEL_ACCESS_TOKEN = "LINE_ACCESS_TOKEN_HERE"
LINE_USER_ID = "LINE_USER_ID_HERE"

# 定義 LINE Push Message 函式
def send_line_push_message(text_message: str, access_token: str, user_id: str) -> bool:
    """
    透過 LINE Messaging API 主動發送 Push Message 給指定 User
    """
    # 未設定真實 Token 時，自動觸發模擬模式
    if access_token == "YOUR_LINE_ACCESS_TOKEN_HERE" or user_id == "YOUR_LINE_USER_ID_HERE":
        print("[模擬模式] 未偵測到有效的 LINE Credentials，進行發送模擬：")
        print(f"目標 LINE User ID: {user_id}")
        print(f"欲推播的訊息內容：\n{text_message}")
        print("✅[模擬模式] LINE 推播訊息模擬成功！\n")
        return True

    # 正式 LINE Messaging API Push Endpoint
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": text_message
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()

        print("[LINE API] 訊息成功推播至指定 LINE 帳號！")
        return True

    except requests.RequestException as e:
        print(f"[網絡異常] 發送 LINE 訊息時發生錯誤：{e}")
        return False

# 主程式測試
if __name__ == "__main__":
    line_notice = (
        "🟢 【LINE 系統通知】\n"
        "Python Step 12 自動化推播測試成功！\n"
        "----------------------------------\n"
        "今日自動化任務摘要：\n"
        "• 匯率監控：正常\n"
        "• 伺服器狀態：健康\n"
        "• 爬蟲任務：已完成"
    )
    print("正在嘗試發送 LINE 推播通知...")
    send_line_push_message(
        text_message=line_notice,
        access_token=LINE_CHANNEL_ACCESS_TOKEN,
        user_id=LINE_USER_ID
    )