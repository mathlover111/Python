import time
import requests
from fastapi import FastAPI, Query, HTTPException, status
import uvicorn

app = FastAPI(
    title="Step 11 - 即時爬蟲 API 微服務",
    description="提供即時爬取網路名言與數據的 API 服務",
    version="1.0.0"
)

# 模擬爬蟲邏輯 (封裝成函式)
def scrape_quotes_by_page(page: int = 1):
    """即時呼叫外部 API 或爬取網頁數據"""
    target_url = f"https://quotes.toscrape.com/api/quotes?page={page}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        quotes_list = []
        for item in data.get("quotes", []):
            quotes_list.append({
                "author": item.get("author", {}).get("name"),
                "content": item.get("text"),
                "tags": item.get("tags", [])
            })

        return {
            "page": page,
            "has_next": data.get("has_next", False),
            "total_fetched": len(quotes_list),
            "data": quotes_list
        }
    except requests.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"目標網站爬取失敗，原因：{str(e)}"
        )
    
# API 端點定義
@app.get("/api/v1/live-quotes")
def get_live_quotes(
    page: int = Query(1, ge=1, description="想要爬取的頁碼 (預設第 1 頁)")
):
    """
    【即時爬蟲 API 端點】
    前端呼叫此 API，Python 會立刻發起網路請求爬取最新名言數據並傳回。
    """
    start_time = time.time()
    
    # 執行即時爬蟲
    result = scrape_quotes_by_page(page=page)
    
    execution_time = round(time.time() - start_time, 3)
    
    return {
        "status": "success",
        "execution_time_seconds": execution_time,
        "result": result
    }

if __name__ == "__main__":
    uvicorn.run("04_crawler_api:app", host="127.0.0.1", port=8000, reload=True)