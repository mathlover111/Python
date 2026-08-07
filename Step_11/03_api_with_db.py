import sqlite3
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

DB_PATH = "Step_11/app.db"

app = FastAPI(title="Step 11 - SQLite 整合 CRUD API")

# Pydantic 數據模型定義
class ItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass  # 用於建立時傳入的資料型態


class ItemResponse(ItemBase):
    id: int  # 用於回傳時包含資料庫自動產生的 ID

    class Config:
        orm_mode = True

# 資料庫初始化 (自動建立資料表)
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT
            )
        """)
        conn.commit()


init_db()  # 啟動時自動檢查建立資料表


# CRUD 端點實作

# 【Create】新增商品 (POST)
@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, price, description) VALUES (?, ?, ?)",
            (item.name, item.price, item.description),
        )
        conn.commit()
        item_id = cursor.lastrowid

    return {**item.dict(), "id": item_id}


# 【Read All】查詢所有商品 (GET)
@app.get("/items", response_model=List[ItemResponse])
def get_all_items():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row  # 讓欄位可以用名稱存取
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, description FROM items")
        rows = cursor.fetchall()

    return [dict(row) for row in rows]


# 【Read One】查詢單一商品 (GET)
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, description FROM items WHERE id = ?", (item_id,))
        row = cursor.fetchone()

    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"找不到 ID 為 {item_id} 的商品",
        )

    return dict(row)


# 【Update】修改商品 (PUT)
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE items SET name = ?, price = ?, description = ? WHERE id = ?",
            (item.name, item.price, item.description, item_id),
        )
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"找不到 ID 為 {item_id} 的商品，無法更新",
            )

    return {**item.dict(), "id": item_id}


# 【Delete】刪除商品 (DELETE)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"找不到 ID 為 {item_id} 的商品，無法刪除",
            )

    return {"status": "success", "message": f"成功刪除 ID 為 {item_id} 的商品"}

if __name__ == "__main__":
    uvicorn.run("03_api_with_db:app", host="127.0.0.1", port=8000, reload=True)