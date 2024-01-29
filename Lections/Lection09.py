
class Skeleton:
    hp = 20

    def was_attacked(self, damage: int):
        print(f"Skeleton was attacked. Hp = {self.hp}, damage = {damage}")
        self.hp = self.hp - damage
        if self.hp <=0:
            self.died()

    def died(self):
        print("Skeleton died")


class Hero:
    hp = 100
    force = 50

    def attack(self, enemy: Skeleton):
        enemy.was_attacked(damage = self.force)


def main():
    hero = Hero()
    skeleton = Skeleton()
    print("Hero vs Skeleton")
    hero.attack(skeleton)


if __name__ == '__main__':
    main()