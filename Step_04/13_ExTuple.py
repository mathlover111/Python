input_name = input("輸入不可修改欄位名稱(逗號分隔): ")
input_data = input("輸入欄位資料(逗號分隔): ")

list_name = [item.strip() for item in input_name.split(",")]
list_data = [item.strip() for item in input_data.split(",")]

listData = list_name + list_data

listToTuple = tuple(listData)
print("\n")
print(listToTuple)
