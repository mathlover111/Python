file = open("note.txt", "r", encoding="utf-8")

content = file.read()

file.close()

print("【檔案內容如下】")
print(content)
