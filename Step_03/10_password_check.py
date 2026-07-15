correct_password = "1234"
max_attempts = 3

for i in range(1, max_attempts + 1):
    password = input(f"請輸入密碼 (第 {i} 次嘗試): ")

    if password == correct_password:
        print("登入成功！")
        break  
    else:
        remaining = max_attempts - i
        
        if remaining > 0:
            print(f"密碼錯誤！還剩 {remaining} 次機會。")
        else:
            print("嘗試次數過多，帳號被鎖定！")