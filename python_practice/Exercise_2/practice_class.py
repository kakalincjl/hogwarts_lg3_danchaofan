# -*- coding:utf-8 -*-

"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""


class Vehicle:
    classification = '交通工具类别'

    def __init__(self, wheel, horsepower, *args, speed=0, brand=None, fuel_type=None, model=None, **kwargs):
        """
        :param wheel: 车轮数，传整型
        :param horsepower: 马力，传整型
        :param args:
        :param speed: 车速，默认为0
        :param brand: 品牌，默认为None
        :param fuel_type: 能源类型，默认为None
        :param model: 型号，同品牌下不同规格的产品，用此字段区分，默认为None
        :param kwargs:
        """
        self.wheel = wheel
        self.horsepower = horsepower
        self.speed = speed
        self.brand = brand
        self.fuel_type = fuel_type
        self.model = model

    def accelerate(self, *args, **kwargs):
        """加速方法，未重写该方法的子类调用时进行简单的输出操作"""
        print('加一下速吧~')

    def brake(self, *args, **kwargs):
        """制动，未重写该方法的子类调用时进行简单的输出操作"""
        print('踩个刹车~')


class Car(Vehicle):
    """
    Car基类，暂未做啥特别处理
    """
    classification = '汽车类别'

    def __init__(self, wheel, horsepower, *args, **kwargs):
        super().__init__(wheel, horsepower, *args, **kwargs)


class Bike(Vehicle):
    """
    Bike基类，实例化时wheel、fuel_type传默认值。
    实现了静态方法bell，调用时输出一段文字。
    """
    classification = '单车类别'

    def __init__(self, horsepower, fuel_type='燃烧你的卡里路', **kwargs):
        """
        调用父类实例化时，wheel默认给传2，即两个车轮
        :param horsepower:
        :param fuel_type: 传默认值
        :param kwargs:
        """
        super().__init__(2, horsepower, fuel_type=fuel_type, **kwargs)

    @staticmethod
    def bell():
        """静态方法，可直接用类对象直接调用，无需实例化"""
        print('Ring Ring Ring , 这是自行车的铃铛')


class Benz(Car):
    """
    奔驰的汽车类
    定义了类私有变量__special_technology，只能在类内部通过类或者类实例化的对象进行访问，调用类方法bell和实例方法accelerate中会用到
    定义了公有变量slogan，类的内部、外部的类对象都可访问
    """
    __special_technology = '这是奔驰独家科技'
    slogan = '这是奔驰,这是奔驰'

    def __init__(self, horsepower, fuel_type='gasoline', **kwargs):
        """
        :param pattern: 加速模式，调用accelerate方法时会用到
        :param horsepower:
        :param kwargs:
        """
        # 实例的模式属性，若没有传值则给个默认值V0。 通过形参给默认值也可以。
        self.pattern = kwargs.get('pattern', 'V0')

        super().__init__(4, horsepower, brand='Benz', fuel_type=fuel_type, **kwargs)

    @classmethod
    def bell(cls, mode='Car'):
        """
        mode为单车时调用Bike的静态方法bell
        :param mode:
        :return:
        """
        if mode == 'Car':
            print(cls.slogan)
        elif mode == 'Bike':
            print('*****', cls.__special_technology, '*****')
            print('假装自己是辆单车。。', end=' ')
            Bike.bell()

    def accelerate(self):
        """
        根据不同模式进行加速的方法
        :return:
        """
        if self.pattern == 'V2':
            print('*****', self.__special_technology, '*****')
            self.speed += self.horsepower * 1.2

        elif self.pattern == 'V1':
            self.speed += self.horsepower * 1.1

        elif self.pattern == 'V0':
            self.speed += self.horsepower

        else:
            pass


class Tesla(Car):
    """
    pass
    """
    def __init__(self, horsepower, fuel_type='electric', **kwargs):
        super().__init__(4, horsepower, brand='Tesla', fuel_type=fuel_type, **kwargs)

    def brake(self):
        print("智能刹车")


if __name__ == '__main__':
    # 简单调试下
    Benz.bell('Bike')
    Benz.bell('Car')

    bz = Benz(10)
    # print(bz.model)
    # bz_1 = Benz(20, pattern='V1')
    # print(bz——1.pattern)

    t = Tesla(50)
    t.brake()
