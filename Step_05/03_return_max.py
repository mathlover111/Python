
def find_max(num1, num2):
    if num1 > num2:
        return num1  
    else:
        return num2 

# 呼叫函式，並用一個外面的變數來「接住」回傳值
biggest_number = find_max(42, 99)

double_size = biggest_number * 2

print(f"biggest：{biggest_number}")
print(f"biggest*2：{double_size}")
