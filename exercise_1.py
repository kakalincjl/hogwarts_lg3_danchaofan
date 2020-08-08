# -*- coding:utf-8 -*-

import random


def fight(hp=1000, enemy_power=200):
    """
    1、每个回合随机决定先手--平衡先手优势
    2、攻击力加上随机值--增加结果的不确定性
    3、先手在攻击后，先判断后手角色血量是否大于0，若小于等于0则结束战斗--血量小于等于0的角色不应再发起攻击
    4、记录回合数--输出显示优化
    5、while循环兼容异常处理
    """
    my_hp = enemy_hp = hp  # 定义角色血量初始值，入参未传则使用默认值1000。
    my_power = enemy_power = enemy_power  # 定义角色攻击力初始值，入参未传则使用默认值200。
    rounds = 1  # 回合数初始值
    role = ('我方', '敌方')  # 回合中的两种角色
    while True:
        try:
            print("====================round {}====================".format(rounds))
            print("当前回合我方剩余血量为{}，敌方剩余血量为{}".format(my_hp, enemy_hp))
            first_role = random.choice(role)  # 每回合开始前随机选择先出击的角色
            print("该回合先出手的是：{}".format(first_role))
            # 若先手为我方则进入此段代码逻辑
            if first_role == '我方':
                my_tmp_power = my_power + random.randint(-100, 20)  # 我方此回合的攻击力，增加攻击力随机性
                enemy_hp -= my_tmp_power  # 敌方此回合受到攻击后剩余的血量
                print("我方全力一击，对敌方造成了{}点伤害。\n敌方剩余血量为{}".format(my_tmp_power, enemy_hp))
                # 若敌方血量低于等于0，则跳出while循环结束战斗回合
                if enemy_hp <= 0:
                    print("我方胜利！")
                    break
                enemy_tmp_power = enemy_power + random.randint(-100, 20)  # 敌方此回合的攻击力，增加攻击力随机性
                my_hp -= enemy_tmp_power  # 我方此回合受到攻击后剩余的血量
                print("敌方全力一击，对我方造成了{}点伤害。\n我方剩余血量为{}".format(enemy_tmp_power, my_hp))
                # 若我方血量低于等于0，则跳出while循环结束战斗回合
                if my_hp <= 0:
                    print("敌方胜利!")
                    break
            # 若先手为敌方则进入此段代码逻辑
            elif first_role == '敌方':
                enemy_tmp_power = enemy_power + random.randint(-100, 20)  # 敌方此回合的攻击力，增加攻击力随机性
                my_hp -= enemy_tmp_power  # 我方此回合受到攻击后剩余的血量
                print("敌方全力一击，对我方造成了{}点伤害。\n我方剩余血量为{}".format(enemy_tmp_power, my_hp))
                # 若我方血量低于等于0，则跳出while循环结束战斗回合
                if my_hp <= 0:
                    print("战斗结束，敌方胜利!")
                    break
                my_tmp_power = my_power + random.randint(-100, 20)  # 我方此回合的攻击力，增加攻击力随机性
                enemy_hp -= my_tmp_power  # 敌方此回合受到攻击后剩余的血量
                print("我方全力一击，对敌方造成了{}点伤害。\n敌方剩余血量为{}".format(my_tmp_power, enemy_hp))
                # 若敌方血量低于等于0，则跳出while循环结束战斗回合
                if enemy_hp <= 0:
                    print("战斗结束，我方胜利！")
                    break
            else:
                raise NameError("混入了奇奇怪怪的角色")  # role对象中出现了未知的角色时触发此异常

            # 防止进入死循环增加的一个粗暴判断
            if rounds == 300:
                raise RuntimeError("大战300回合还未分出胜负")
            rounds += 1  # 回合结束后回合数加1
        except Exception as e:
            raise ("有未知异常啦~~~", e)


if __name__ == '__main__':
    fight()  # 执行主函数
