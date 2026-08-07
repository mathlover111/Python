import sqlite3

# 連接資料庫
conn = sqlite3.connect("Step_09/shop.db")
cursor = conn.cursor()

# UPDATE(更新資料)：調整蘋果的價格與庫存
update_sql = "UPDATE products SET price = ?, stock = ? WHERE name = ?"
cursor.execute(update_sql, (35, 80, "蘋果"))
print(f"成功更新 {cursor.rowcount} 筆商品資料！（蘋果漲價至 35 元）")

# DELETE(刪除資料)：將香蕉從資料表中刪除
delete_sql = "DELETE FROM products WHERE name = ?"
cursor.execute(delete_sql, ("香蕉",))
print(f"成功刪除 {cursor.rowcount} 筆商品資料！（香蕉已下架）")

conn.commit()

# 印出目前最新的所有商品驗證結果
print("\n=== 目前最新商品清單 ===")
cursor.execute("SELECT id, name, price, stock FROM products")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | 品名: {row[1]} | 價格: {row[2]} 元 | 庫存: {row[3]} 個")

conn.close()