"""
    作者:北辰
    日期:13/05/2019
    版本:2.0.0
    功能:兽人之袭文本游戏,AbstractGameUnit抽象类
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
from abc import ABCMeta, abstractmethod
from gameutils import weighted_random_selection,print_bold
from gameuniterror_v2 import HealthMeterException

class AbstractGameUnit(metaclass=ABCMeta):
    """A base class for creating various game characters"""
    def __init__(self,name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        """Information on the unit (MUST be overridden in subclasses)"""
        pass

    def attack(self,enemy):
        """The main logic to determine injured unit and amount of injury

        .. todo:: Check if enemy exists!
        """
        injured_unit = weighted_random_selection(self,enemy)
        injury = random.randint(10,15)
        injured_unit.health_meter = max(injured_unit.health_meter-injury,0)
        print("Attack! ",end='')
        self.show_health(end=' ')
        enemy.show_health(end=' ')

    def heal(self,heal_by=2,full_healing=True):
        """Heal the unit replenishing all the hit points"""
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            # TODO: Do you see a bug here? it can exceed max hit points!
            self.health_meter += heal_by

        # raise a custom exception. Refer to the chapter on exception handling
        if self.health_meter > self.max_hp:
            raise HealthMeterException("health_meter > max_hp!")
            # raise GameUnitError("health_meter > max_hp!",101)

        print_bold("You are HEALED!",end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Reset the `health_meter` (assign default hit points)"""
        self.health_meter = self.max_hp

    def show_health(self,bold=False,end='\n'):
        """Show the remaining hit points of the player and the enemy"""
        # TODO: what if there is no enemy?
        msg = "Health: %s: %d" % (self.name,self.health_meter)

        if bold:
            print_bold(msg,end=end)
        else:
            print(msg,end=end)