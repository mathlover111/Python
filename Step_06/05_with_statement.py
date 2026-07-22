# with open() as 檔案變數名稱
with open("Step_06/note.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("【使用 with 語法讀取到的內容】")
    print(content)

try:
    with open("Step_06/safe_note.txt", "w", encoding="utf-8") as safe_file:
        safe_file.write("這是一份檔案")
    print("\n新檔案 safe_note.txt 建立並寫入成功")
except Exception as e:
    print(f"發生未知的錯誤：{e}")