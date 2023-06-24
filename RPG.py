# 現在時刻は 6月5日 13時

### MEMBER ###
# ちんぽ
# イツキ

### TODO ### 
# 1.まちゃいとコード共有するために Github 導入
# 2.無効なコマンドですっていう表示になった時にもう一度コマンドを打ち直させるという動作を入れる
# 3.ダメージを与えた時、回復をした時にそれぞれの HP の操作
# 4.魔王の行動をコマンド辞書からランダムに取り出す
# 5.最初はルールベースAIを用いて魔王の行動を決める,その後、ユーティリティベースAIを用いる

import random

#魔王
MAOU_HP = 10000
#勇者
PLAYER_HP = 2000

import random

class RPG(object):
    def __init__(self):
        self.PLAYER_NAME = self.PLAYER_name()
        self.MAOU_NAME = self.MAOU_name()
        self.PLAYER_COMMAND = self.create_PLAYER_COMMAND()
        self.MAOU_COMMAND = self.create_MAOU_COMMAND()
        

    def PLAYER_name(self):
        name = input("あなたの名前を教えてください : ")
        while True:
            print("一度決めると再度変更は不可です。この名前でよろしいですか")
            answer = input("yesかnoを入力してください: ")
            print(" ")

            if answer == "yes":
                break
            elif answer == "no":
                name = input("あなたの名前を教えてください : ")
            else:
                print("無効な入力です。")
        return name
    
    def MAOU_name(self):    
        name = input("最後にあなたが倒す魔王の名前を決めてください : ")
        while True:
            print("一度決めると再度変更は不可です。この名前でよろしいですか")
            answer = input("yesかnoを入力してください: ")
            print(" ")

            if answer == "yes":
                break
            elif answer == "no":
                name = input("魔王の名前を決めてください : ")
            else:
                print("無効な入力です。")
        return name

    def create_PLAYER_COMMAND(self):
        command = {
            '斬る': self.PLAYER_ATTACK_DAMAGE,
            '魔法攻撃': self.PLAYER_MAGIC_DAMAGE,
            '回復': self.PLAYER_HEAL
        }
        return command

    def create_MAOU_COMMAND(self):
        command = {
            '斬る': self.maou_attack_damage,
            '魔法攻撃': self.maou_magic_damage,
            '回復': self.maou_heal
        }
        return command

    def player_init(self):
        print("勇者" + self.PLAYER_NAME + " : ")
        print("HP : " + str(PLAYER_HP))
        for key, value in self.PLAYER_COMMAND.items():
            print(f"{key}: {value()}")
        print(" ")
    
    def maou_init(self):
        print("魔王" + self.MAOU_NAME + " : ")
        print("HP : " + str(MAOU_HP))
        for key, value in self.MAOU_COMMAND.items():
            print(f"{key}: {value()}")
        print(" ")

    def player_judge_command(self, key):
        if key in self.PLAYER_COMMAND:
            return self.PLAYER_COMMAND[key]()
        else:
            return "無効なコマンドです"

    def maou_judge_command(self, key):
        if key in self.MAOU_COMMAND:
            return self.MAOU_COMMAND[key]()
        else:
            return "無効なコマンドです"

    def choice_command(self):
        user_input = input("コマンドを選択してください : ")
        result = self.player_judge_command(user_input)
        print("魔王" + self.MAOU_NAME + "へ" + str(result) + "のダメージ")

    def PLAYER_ATTACK_DAMAGE(self):
        return random.randint(100, 200)

    def PLAYER_MAGIC_DAMAGE(self):
        return random.randint(200, 300)

    def PLAYER_HEAL(self):
        return random.randint(500, 600)

    def maou_attack_damage(self):
        return random.randint(100, 200)

    def maou_magic_damage(self):
        return random.randint(200, 300)

    def maou_heal(self):
        return random.randint(3000, 4000)


if __name__ == "__main__":
    rpg = RPG()
    print("これは勇者" + rpg.PLAYER_NAME + "が魔王" + rpg.MAOU_NAME + "を倒す物語です")
    rpg.player_init()
    rpg.maou_init()
    rpg.choice_command()

