class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def show_info(self):
        print(f"英雄：{self.name} | 血量：{self.hp} | 攻擊力：{self.attack}")

class Mage(Hero):
    def __init__(self, name, hp, attack, mp):
        # 使用 super() 呼叫父類別 Hero 的 __init__，繼承 name, hp, attack
        super().__init__(name, hp, attack)
        self.mp = mp  # 屬性：魔力值

    def cast_spell(self, target_name):
        if self.mp >= 20:
            self.mp -= 20
            damage = self.attack * 2
            print(f"✨ {self.name} 對 {target_name} 吟唱火球術！造成 {damage} 點爆擊傷害（剩餘 MP: {self.mp}）")
        else:
            print(f"❌ {self.name} 魔力不足，無法施展魔法！")

mage = Mage("甘道夫", 80, 30, 50)
# 子類別可以直接使用父類別的方法
mage.show_info()

# 呼叫子類別獨有的方法
mage.cast_spell("哥布林")
mage.cast_spell("哥布林")
mage.cast_spell("哥布林")