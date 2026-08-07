from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Step 11 - 參數接收與 Pydantic 驗證")

# 定義資料結構模型 (Pydantic Model)
# FastAPI 會自動驗證前端傳過來的 JSON 欄位型態與格式
class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int = 0                  # 預設值為 0
    description: Optional[str] = None  # 可選欄位

# 接收路徑參數 (Path Parameter)
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int = Path(..., description="商品的指定 ID (必須是整數)")):
    """根據商品 ID 獲取商品詳細資訊"""
    return {
        "status": "success",
        "product_id": product_id,
        "detail": f"這是 ID 為 {product_id} 的商品細節"
    }

# 接收查詢參數 (Query Parameter)
@app.get("/search")
def search_products(
    keyword: str = Query(..., description="搜尋關鍵字"),
    page: int = Query(1, ge=1, description="頁碼 (預設為 1，最小為 1)"),
    limit: int = Query(10, le=50, description="每頁筆數 (預設 10，最大 50)")
):
    """商品搜尋 API (支援分頁與關鍵字過濾)"""
    return {
        "status": "success",
        "query": {
            "keyword": keyword,
            "page": page,
            "limit": limit
        },
        "results": [f"符合 '{keyword}' 的結果 1", f"符合 '{keyword}' 的結果 2"]
    }


# 接收 JSON Body (POST 請求)
@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    """新增商品 API (接收 JSON 格式資料)"""
    return {
        "status": "created",
        "message": f"成功建立商品：{product.name}",
        "data": product.dict()
    }


if __name__ == "__main__":
    uvicorn.run("02_request_params:app", host="127.0.0.1", port=8000, reload=True)