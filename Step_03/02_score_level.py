score = float(input("請輸入分數 (0~100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("不及格")