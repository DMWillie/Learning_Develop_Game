"""
    作者:北辰
    日期:13/05/2019
    版本:2.0.0
    功能:兽人之袭文本游戏,工具类函数
    1.0.0版本改进之处:使用面向对象编程,并使用抽象基类
    1.0.0新增功能: 1.新的使命是获得所有木屋并击败所有的敌人
                  2.可以在同伴的木屋或者空闲的木屋治疗
                  3.引入一个或者多个骑士来帮助Foo先生,他们可以轮流占领木屋
                  4.木屋的数量是可配置的,例如增加到10个
                  5.每个木屋中可以存放一些黄金或者武器,这样Foo先生和他的同伴们可以捡起来
    1.1.0新增功能:增加异常处理
    1.1.5改进之处:定义一个异常处理类
    2.0.0 代码模块化
"""

import random

def weighted_random_selection(obj1,obj2):
    """Randomly select between two objects based on assigned 'weight'

    .. todo:: How about creating a utility module for common functionality?
    """
    weighted_list = 3*[id(obj1)] + 7*[id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1
    else:
        return obj2

def print_bold(msg, end='\n'):
    """以粗体形式打印文本"""
    print("\033[1m" + msg + "\033[0m", end=end)