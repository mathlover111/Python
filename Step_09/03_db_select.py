import sqlite3

conn = sqlite3.connect("Step_09/shop.db")
cursor = conn.cursor()

# 查詢所有商品資料 (SELECT *)
print("=== 1. 所有商品清單 ===")
cursor.execute("SELECT id, name, price, stock FROM products")
all_products = cursor.fetchall()

for prod in all_products:
    prod_id, name, price, stock = prod  # 解構 Tuple
    print(f"ID: {prod_id} | 品名: {name:<4} | 價格: {price:3d} 元 | 庫存: {stock} 個")

print("\n=== 2. 價格 > 30 元的商品 ===")
cursor.execute("SELECT name, price FROM products WHERE price > ?", (30,))
expensive_products = cursor.fetchall()

for name, price in expensive_products:
    print(f"高單價商品：{name} (NT$ {price})")

conn.close()