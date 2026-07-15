
age = int(input("請輸入你的年齡: "))

# 2. 使用 or 判斷：只要滿足「小於 6 歲」或者「大於等於 65 歲」其中之一
if age < 6 or age >= 65:
    print("免票入園")
else:
    print("全票 200 元")