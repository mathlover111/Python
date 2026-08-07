from fastapi import FastAPI
import uvicorn

# 建立 FastAPI 應用程式實例
app = FastAPI(
    title="Step 11 - 第一個 Web API",
    description="使用 FastAPI 打造現代化 Python 後端服務",
    version="1.0.0"
)

# 定義首頁路由 (GET /)
@app.get("/")
def read_root():
    """首頁歡迎訊息 API"""
    return {
        "status": "success",
        "message": "歡迎來到 Python Web API 服務！",
    }

# 定義系統健康檢查 API (GET /health)
@app.get("/health")
def health_check():
    """檢查伺服器運作狀態"""
    return {
        "status": "healthy",
        "server": "Uvicorn",
        "framework": "FastAPI"
    }

# 啟動伺服器 (若直接執行此 Python 檔案)
if __name__ == "__main__":
    # 本地開發測試伺服器，啟動在 http://127.0.0.1:8000
    uvicorn.run("01_first_api:app", host="127.0.0.1", port=8000, reload=True)