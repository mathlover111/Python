class Student:
    # 建構子 (Constructor)：創立物件時會自動執行的初始化函式
    def __init__(self, name, EQ, IQ):
        # self 代表「這個物件自己」，將傳進來的參數綁定給物件的屬性
        self.name = name
        self.EQ = EQ
        self.IQ = IQ

student1 = Student("AAA", 100, 120)
student2 = Student("Niger", 70, 90)

print("--- student ---")
print(f"Student 1：{student1.name} | {student1.EQ} | {student1.IQ}")
print(f"Student 2：{student2.name} | {student2.EQ} | {student2.IQ}")
