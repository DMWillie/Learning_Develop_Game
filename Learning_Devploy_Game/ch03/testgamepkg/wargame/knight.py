"""
    作者:北辰
    日期:13/05/2019
    版本:2.0.0
    功能:兽人之袭文本游戏,knight类
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

from abstractgameunit import AbstractGameUnit
from gameutils import print_bold

class Knight(AbstractGameUnit):
    """ Class that represents the game character 'Knight'

    The player instance in the game is a Knight instance. Other Knight
    instances are considered as 'friends' of the player and is
    indicated by the attribute `self.unit_type` .
    """
    def __init__(self,name='Sir Foo'):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self): # 这里子类必须实现抽象基类的抽象方法
        """Print basic information about this character"""
        print("I  am a Knight!")

    def acquire_hut(self,hut):
        """Fight the combat (command line) to acquire the hut"""
        print_bold("Entering hut %d..."%hut.number,end=' ')
        # 判断占有者是否是敌人的逻辑
        is_enemy = (isinstance(hut.occupant,AbstractGameUnit)
                    and hut.occupant.unit_type == 'enemy')
        continue_attack = 'y'
        if is_enemy:
            print_bold("Enemy sighted!")
            self.show_health(bold=True,end=' ')
            hut.occupant.show_health(bold=True,end=' ')
            while continue_attack:
                continue_attack = input("......continue attack?(y/n): ")

                if continue_attack !='y' and continue_attack !='n': #输入不合理
                    print("Invalid input! input must 'y' or 'n',Please input again.")
                    continue

                if continue_attack == 'n':
                    self.run_away()
                    break

                self.attack(hut.occupant)

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break
                if self.health_meter <= 0:
                    print("")
                    break
        else:
            if hut.get_occupant_type() == 'unoccupied':
                print_bold("Hut is unoccupied")
            else:
                print_bold("Friend sighted!")
            # 用该类的一个实例来更新木屋的occupant属性
            hut.acquire(self)
            self.heal()

    def run_away(self):
        """Abandon the battle.

        .. see also:: `self.acquire_hut`
        """
        print_bold("RUNNING AWAY...")
        self.enemy = None