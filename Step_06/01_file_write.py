# 使用 open() 開啟檔案
# 檔名 "note.txt"
# "w" 代表 寫入模式
file = open("note.txt", "w", encoding="utf-8")

# 文字寫入檔案
file.write("114514")


# 關閉檔案，釋放系統資源
file.close()

print("寫入成功")
