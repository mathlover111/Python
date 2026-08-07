class Hero:
    # 建構子 (Constructor)：創立物件時會自動執行的初始化函式
    def __init__(self, name, hp, attack):
        # self 代表「這個物件自己」，將傳進來的參數綁定給物件的屬性
        self.name = name
        self.hp = hp
        self.attack = attack

hero1 = Hero("亞瑟", 100, 25)
hero2 = Hero("妮歌", 70, 40)

print("=== 英雄角色資料 ===")
print(f"英雄 1：{hero1.name} | 血量：{hero1.hp} | 攻擊力：{hero1.attack}")
print(f"英雄 2：{hero2.name} | 血量：{hero2.hp} | 攻擊力：{hero2.attack}")