# 全域變數：宣告在所有函式的外面
msg = 5

def my_function():
    # 區域變數：宣告在函式的裡面
    local_msg = 3
    
    # 在函式內部，都可以存取
    print("【函式內部】", msg)
    print("【函式內部】", local_msg)


my_function()


print("【函式外部】", msg)


