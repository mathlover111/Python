target = 77
guess = 0

while guess != target:
    guess = int(input("請猜一個 1 到 100 的數字: "))
    
    if guess != target:
        print("猜錯了，再試一次！")

print("恭喜猜對了！")