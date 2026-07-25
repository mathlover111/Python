import os

print("=== Python 專案套件管理示範 ===")

# 教導如何產生與安裝 requirements.txt
instructions = """
【如何導出目前專案安裝的套件清單？】
請在終端機輸入：
  pip freeze > requirements.txt

【當拿到別人的專案時，如何一鍵安裝清單上的所有套件？】
請在終端機輸入：
  pip install -r requirements.txt
"""

print(instructions)

# 檢查專案目錄下是否有 requirements.txt 檔案
if os.path.exists("requirements.txt"):
    print("找到 requirements.txt 檔案！")
else:
    print("目前尚未建立 requirements.txt，可以在終端機產生一個喔！")