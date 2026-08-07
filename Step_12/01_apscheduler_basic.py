import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def interval_job():
    """【固定間隔任務】每隔數秒自動執行一次"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[固定間隔] 任務執行中... 當前時間：{current_time}")

def cron_job():
    """【Cron 定時任務】在指定的秒數/分鐘自動觸發"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[Cron 定時] 整點/指定時間觸發！當前時間：{current_time}")

# 背景排程器會在獨立線程中運作，不會阻塞主程式的執行
scheduler = BackgroundScheduler()

# 觸發模式 A：interval (每隔 3 秒執行一次)
scheduler.add_job(
    interval_job,
    trigger="interval",
    seconds=3,
    id="my_interval_job"
)

# 觸發模式 B：cron (Cron 模式：設定每分鐘的第 00 秒執行一次)
# 參數說明：second="0" 代表每到第 0 秒觸發（即每整分鐘觸發一次）
scheduler.add_job(
    cron_job,
    trigger="cron",
    second="0",
    id="my_cron_job"
)

# 啟動排程器與主程式監聽
if __name__ == "__main__":
    # 啟動排程器
    scheduler.start()
    print("排程器已啟動！按下 Ctrl + C 可結束程式。\n")

    try:
        # 讓主程式維持存活狀態，否則背景排程會跟著主程式結束而中斷
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        # 捕捉 Ctrl + C 訊號，優雅地關閉排程器
        scheduler.shutdown()
        print("\n排程器已安全關閉！")