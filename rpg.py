from random import random

class ユニット:

    def __init__(self, kind):
        self.kind = kind
        self.たいりょく = 0
        self.ちから = 0
        print(f"{self.kind}がたんじょうした。")


    def ステータス(self):
        print("-"*20)
        print(f"しょくぎょう : {self.kind: >5}")
        print(f"たいりょく　 : {self.たいりょく: >5}")
        print(f"ちから　　　 : {self.ちから: >5}")
        print("-"*20)


    def たたかう(self, target):
        if self.たいりょく <= 0:
            print(f"{self.kind}はしんでいるのでたたかえない。")
            return

        if target.たいりょく <= 0:
            print(f"{target.kind}はしんでいる。これいじょうはかわいそうだ。")
            return

        damage_mine = int(target.ちから*(random()/2+0.5))
        damage_targets = int(self.ちから*(random()/2+0.5))
        self.たいりょく -= damage_mine
        target.たいりょく -= damage_targets
        print(f"{self.kind}と{target.kind}がたたかった。")
        print(f"{self.kind}が{target.kind}に{damage_targets}のダメージをあたえた。")

        if target.たいりょく <= 0:
            print(f"{self.kind}は{target.kind}をたおした！")
            return

        print(f"{target.kind}が{self.kind}に{damage_mine}のダメージをあたえた。")

        if self.たいりょく <= 0:
            print(f"{self.kind}は{target.kind}にたおされてしんでしまった。")


class Unit:

    def __init__(self, kind):
        self.kind = kind
        self.hitpoint = 0
        self.strength = 0
        print(f"{self.kind} was born.")


    def status(self):
        print("-"*20)
        print(f"Occupation : {self.kind: >5}")
        print(f"Hitpoint   : {self.hitpoint: >5}")
        print(f"Strength   : {self.strength: >5}")
        print("-"*20)


    def fight(self, target):
        if self.hitpoint <= 0:
            print(f"{self.kind} has been already dead.")
            return

        if target.hitpoint <= 0:
            print(f"{target.kind} had died.")
            return

        damage_mine = int(target.strength*(random()/2+0.5))
        damage_targets = int(self.strength*(random()/2+0.5))
        self.hitpoint -= damage_mine
        target.hitpoint -= damage_targets
        print(f"{self.kind} fought with {target.kind}.")
        print(f"{self.kind} gave {damage_targets} damage to {target.kind}.")

        if target.strength <= 0:
            print(f"{self.kind} beat {target.kind} !")
            return

        print(f"{target.kind} gave {damage_mine} damage to {self.kind}.")

        if self.hitpoint <= 0:
            print(f"{self.kind} has been defeated by {target.kind}.")
