# -*- coding:utf-8 -*-

"""
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""

"""
基类：
初始：血量，武力值

对打方法

血量比较：重写内置比较的方法

TongLao类，继承自基类

see_people方法，入参name
根据入参判断不同的输出值，未在判断条件内的，输出对应的参数名


fight_zms方法，入参enemy
调用者武力值翻倍，血量，并对打一回合。
比较血量的操作不在此方法中实现

XuZhu类，

see_people、fight_zms方法需要外部调用，不适合定义成私有方法，故进行重写，调用自身的read方法
read方法
"""


class Role:
    def __init__(self, power, hp):
        # self.power = float(power)
        # self.hp = float(hp)
        self.power = power
        self.hp = hp

    def __gt__(self, other):
        print("执行大于", self.hp, other.hp)
        print(self.hp > other.hp)
        if not hasattr(other, 'hp'):
            raise AttributeError("{}对象缺少hp属性".format(other))
        return self.hp > other.hp

    def __eq__(self, other):
        print("执行等于")
        if not hasattr(other, 'hp'):
            raise AttributeError("{}对象缺少hp属性".format(other))
        return self.hp == other.hp

    # def __lt__(self, other):
    #     print("执行小于", other)
    #     if not hasattr(other, 'hp'):
    #         raise AttributeError("{}对象缺少hp属性".format(other))
    #     return self.hp < other.hp

    def fight(self, other):
        """对打方法"""
        if not hasattr(other, 'power'):
            raise AttributeError("{}对象缺少power属性".format(other))
        if not hasattr(other, 'hp'):
            raise AttributeError("{}对象缺少hp属性".format(other))
        self.hp -= other.power
        other.hp -= self.power
        return other.hp


class TongLao(Role):
    def __init__(self, power, hp):
        super().__init__(power, hp)

    def see_people(self, name):

        if name == 'WYZ':
            print("师弟！！！！")

        elif name == '李秋水':
            print("呸，贱人")

        elif name == '丁春秋':
            print("叛徒！我杀了你")

        # 兼容未知输入的情况
        else:
            print("你说啥？", name)

    def fight_zms(self, enemy):
        """
        调用者武力值翻倍，血量
        传入enemy对象，调用父类fight方法对打一回合。
        """
        self.power = self.power * 10  # 武力值乘以10
        self.hp = round(self.hp / 2, 1)  # 血量除以2，保留小数点后一位
        self.fight(enemy)


class XuZhu(TongLao):
    def __init__(self, power, hp):
        super().__init__(power, hp)

    def read(self):
        print("罪过罪过")

    def see_people(self, name):
        """
        重写父类方法，调用自身的read方法
        不对enemy进行操作
        """
        return self.read()

    def fight_zms(self, enemy):
        """
        重写父类方法，调用自身的read方法。
        不对enemy进行操作
        """
        return self.read()


if __name__ == '__main__':
    # 简单调试下

    xz = XuZhu(50, 100)
    # xz.see_people('ss')
    # xz.fight_zms()
    # xz.read()

    tl = TongLao(10, 120)
    # tl.see_people('WYZ')
    tl.fight_zms(xz)

    # print(tl.hp)
    # print(xz.hp)
    if tl > xz:
        print("童姥赢")
    elif xz > tl:
        print("虚竹赢")
    else:
        print("打成平手")
