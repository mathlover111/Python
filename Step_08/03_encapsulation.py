class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 

    # 提供公開的存款方法
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner} 成功存款 {amount} 元！")
        else:
            print("❌ 存款金額必須大於 0！")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} 成功提款 {amount} 元！")
        else:
            print("❌ 提款失敗：餘額不足或金額不合法！")

    # 提供公開的「查詢餘額」方法
    def get_balance(self):
        return self.__balance


account = BankAccount("野獸先輩", 1000)

account.deposit(500)
account.withdraw(200)
print(f"目前最新餘額為：{account.get_balance()} 元")

print("\n--- 嘗試私自修改 private 屬性 ---")
# 這行不會改變真正的 __balance，Python 會在內部進行名稱改寫 (Name Mangling)
account.__balance = 9999999
print(f"真正的餘額：{account.get_balance()} 元")