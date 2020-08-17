# -*- coding:utf-8 -*-

"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。



"""

"""
-交通工具类

-属性
-- 公有
-- 私有

-方法
-- 公有
-- 私有

-子类（汽车）

-属性
-- 公有
-- 私有

- 方法
-- 类方法
-- 实例方法
-- 静态方法

"""


class Vehicle:
    classification = '交通工具类别'

    def __init__(self, brand, power, *args, **kwargs):
        self.brand = brand
        self.power = power

    def accelerate(self, *args, **kwargs):
        """加速"""
        pass

    def brake(self, *args, **kwargs):
        """制动"""
        pass


class Car(Vehicle):
    classification = '汽车类别'

    def __init__(self, brand, power, *args, **kwargs):
        super().__init__(brand, power, *args, **kwargs)


class Bike(Vehicle):
    classification = '单车类别'

    def __init__(self, brand, power, *args, **kwargs):
        super().__init__(brand, power, *args, **kwargs)

    @staticmethod
    def bell():
        """静态方法，可直接用类对象直接调用，无需实例化"""
        print('Ring Ring Ring , 这是自行车的铃铛')


class Benz(Car):
    """
    pass
    """
    __special_technology = '这是奔驰独家科技'
    slogan = '这是奔驰,这是奔驰'

    def __init__(self, power, speed=0, brand='Benz', **kwargs):
        if brand != 'Benz':
            raise ValueError("不是奔驰啊啊啊啊")
        if 'model' in kwargs:
            self.model = kwargs.get('model', None)

        self.speed = speed
        super().__init__(brand, power, **kwargs)

    @classmethod
    def bell(cls, mode='Car'):
        if mode == 'Car':
            print(cls.slogan)
        elif mode == 'Bike':
            Bike.bell()

    def accelerate(self):
        if self.model == 'V2':
            self.speed += self.power * 1.2

        elif self.model == 'V1':
            self.speed += self.power * 1.1

        else:
            pass





class Benz_1(Benz):
    pass

# Benz.bell('Bike')
# Benz.bell('Car')
