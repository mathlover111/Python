class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
 
    def take_damage(self, damage):
        self.hp -= damage
        # 血量不會扣到負數
        if self.hp < 0:
            self.hp = 0
        print(f"💥 {self.name} 受到了 {damage} 點傷害！剩餘血量：{self.hp}")

    # 攻擊
    def attack_target(self, target_hero):
        print(f"\n⚔️ {self.name} 發動攻擊，揮刀砍向 {target_hero.name}！")
        # 呼叫對方的 take_damage 方法
        target_hero.take_damage(self.attack)

hero1 = Hero("亞瑟", 100, 25)
hero2 = Hero("妮歌", 70, 40)

hero1.attack_target(hero2) 
hero2.attack_target(hero1) 
hero2.attack_target(hero1)  