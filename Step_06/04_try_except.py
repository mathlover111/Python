try:
    # 嘗試開不存在的檔案
    file = open("Step_06/ghost_file.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("找不到指定的檔案，請確認檔案路徑是否正確")

print("系統持續運作中")