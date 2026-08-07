from fastapi import FastAPI, Depends, HTTPException, status, Security
from fastapi.security import APIKeyHeader
import uvicorn

app = FastAPI(
    title="Step 11 - API Key 身份驗證服務",
    description="實作資安控管，僅限帶有合法 API Key 的請求存取機密 API",
    version="1.0.0"
)

# 設定系統預設的合法 API Key (實務上通常存於環境變數 .env 或資料庫)
API_KEY_NAME = "X-API-KEY"
VALID_API_KEYS = {"secret-key-123", "admin-god-mode-999"}

# 定義 API Key Header 提取器
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# 定義驗證依賴項 (Dependency Function)
def verify_api_key(api_key: str = Security(api_key_header)):
    """驗證前端傳來的 Header 是否包含有效的 API Key"""
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="請求失敗：未提供 API Key (缺少 Header 'X-API-KEY')"
        )
    if api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="請求失敗：API Key 無效或已過期！"
        )
    return api_key

# 公開端點 (無需驗證)
@app.get("/public/info")
def public_info():
    """所有人都可以存取的公開資訊 API"""
    return {
        "status": "success",
        "message": "這是公開資訊，人人皆可存取。"
    }

# 受保護端點 (需經過 verify_api_key 驗證)
@app.get("/protected/secret-data")
def protected_data(user_key: str = Depends(verify_api_key)):
    """【機密 API】只有提供正確 X-API-KEY 的請求才能取得資料"""
    return {
        "status": "success",
        "message": "恭喜！身分驗證成功，順利存取機密商業數據！",
        "authorized_by_key": user_key,
        "secret_data": [
            {"id": 1, "confidential": "公司 2026 年度營收報告"},
            {"id": 2, "confidential": "內部系統管理員權限清單"}
        ]
    }
if __name__ == "__main__":
    uvicorn.run("05_api_auth:app", host="127.0.0.1", port=8000, reload=True)