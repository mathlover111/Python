import sqlite3

# 連接資料庫
conn = sqlite3.connect("Step_09/shop.db")
cursor = conn.cursor()

# 單筆新增資料 (使用 ? 做佔位符)
insert_single_sql = "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)"
single_product = ("蘋果", 30, 100)

cursor.execute(insert_single_sql, single_product)
print(f"✅ 成功新增單筆商品，最新的 ID 是：{cursor.lastrowid}")

# 多筆批量新增資料 (executemany)
multiple_products = [
    ("香蕉", 20, 150),
    ("鮮奶", 85, 30),
    ("咖啡", 55, 50)
]

cursor.executemany(insert_single_sql, multiple_products)
print(f"✅ 成功批量新增 {len(multiple_products)} 筆商品！")

conn.commit()
conn.close()