import math      
import datetime 

print("--- math 數學模組 ---")
print(f"圓周率 π 的數值：{math.pi}")
print(f"16 的平方根是：{math.sqrt(16)}")

print("\n---datetime 時間模組 ---")
now = datetime.datetime.now()
print(f"現在的完整時間：{now}")
print(f"格式化時間：{now.strftime('%Y-%m-%d %H:%M:%S')}")