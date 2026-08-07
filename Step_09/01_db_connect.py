import sqlite3
# 連接到資料庫檔案
conn = sqlite3.connect("Step_09/shop.db")

# 建立游標 (Cursor) 物件，用來執行 SQL 指令
cursor = conn.cursor()

# 建立一個名為 products 的商品資料表
# TEXT, INTEGER, REAL 是 SQLite 的常見資料型態
create_table_sql = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    stock INTEGER DEFAULT 0
);
"""
cursor.execute(create_table_sql)

conn.commit()
conn.close()

print("✅ 成功連線資料庫並建立 products 資料表")