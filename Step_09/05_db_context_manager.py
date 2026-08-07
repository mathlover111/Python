import sqlite3

db_path = "Step_09/shop.db"

print("===使用 with 安全地執行交易 ===")
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    # 新增一個測試商品
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ("麵包", 25, 60))
    print("成功插入麵包！(離開 with 區塊時會自動 commit)")

# 測試異常發生時的自動 Rollback 機制
print("\n===測試交易失敗與自動 Rollback ===")
try:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        # 先扣除蘋果的庫存
        cursor.execute("UPDATE products SET stock = stock - 10 WHERE name = ?", ("蘋果",))
        print("已扣除蘋果庫存...")

        # 故意引發除以零的錯誤
        error_trigger = 1 / 0

        cursor.execute("UPDATE products SET stock = stock - 10 WHERE name = ?", ("鮮奶",))
except Exception as e:
    print(f"發生錯誤：{e}！`with` 已自動執行 Rollback，取消剛剛未完成的操作！")


print("\n=== 3. 最終驗證資料庫狀態 ===")
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name, stock FROM products WHERE name IN ('蘋果', '麵包')")
    for name, stock in cursor.fetchall():
        print(f"商品：{name} | 庫存：{stock}")