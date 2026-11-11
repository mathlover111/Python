target = 77
guess = 0

while guess != target:
    guess = int(input("猜一個 1 到 100 的數字: "))
    
    if guess != target:
        print("猜錯了，哈哈！")

print("猜對了！")
