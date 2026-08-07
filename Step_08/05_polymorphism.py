# 父類別
class Hero:
    def __init__(self, name):
        self.name = name

    def attack(self):
        # 定義介面，子類別應該要覆寫 (Override) 這個方法
        pass

class Warrior(Hero):
    def attack(self):
        print(f"🗡️戰士 {self.name} 揮舞巨劍進行近戰砍擊！")

class Archer(Hero):
    def attack(self):
        print(f"🏹弓箭手 {self.name} 拉弓射出一發精準箭矢！")

class Mage(Hero):
    def attack(self):
        print(f"🔮法師 {self.name} 揮動杖柄發射一枚能量法球！")

# 將不同類別的物件放入同一個清單
party = [
    Warrior("亞瑟"),
    Archer("羅賓漢"),
    Mage("甘道夫")
]
print("=== 隊伍發動全員進攻 ===")
# 統一用相同的指令 attack()，各物件會表現各自行為
for hero in party:
    hero.attack()