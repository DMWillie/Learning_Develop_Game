"""
    作者:北辰
    日期:12/05/2019
    版本:1.1.0
    功能:兽人之袭文本游戏
    1.0.0版本改进之处:使用面向对象编程,并使用抽象基类
    1.0.0新增功能: 1.新的使命是获得所有木屋并击败所有的敌人
                  2.可以在同伴的木屋或者空闲的木屋治疗
                  3.引入一个或者多个骑士来帮助Foo先生,他们可以轮流占领木屋
                  4.木屋的数量是可配置的,例如增加到10个
                  5.每个木屋中可以存放一些黄金或者武器,这样Foo先生和他的同伴们可以捡起来
    1.1.0新增功能:增加异常处理
"""

import random
from abc import ABCMeta,abstractmethod

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

class OrcRider(AbstractGameUnit):
    """Class that represents the game character Orc Rider"""
    def __init__(self,name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        """Print basic information about this character"""
        print("Grrrr..I am an Orc Wolf Rider. Don't mess with me.")

class Hut:
    """Class to create hut object(s) in the game Attack of the Orcs"""
    def __init__(self,number,occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self,new_occupant):
        """Update the occupant of this hut"""
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold("GOOD JOB! Hut %d acquired" % self.number)

    def get_occupant_type(self):
        """Return a string giving info on the hut occupant"""
        if self.is_acquired:
            occupant_type = 'ACQUIRED'
        elif self.occupant is None:
            occupant_type = 'unoccupied'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type

class AttackOfTheOrcs:
    """Main class to play Attack of The Orcs game"""
    def __init__(self):
        self.huts = [] #用来存储稍后创建的Hut类实例
        self.player = None

    def get_occupants(self):
        """Return a list of occupant types for all huts.

        .. todo::
             Prone to bugs if self.huts is not populated.
             Chapter 2 talks about catching exceptions
        """
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        """Print the game mission in the console"""
        print_bold("Mission:")
        print("  1. Fight with the enemy.")
        print("  2. Bring all the huts in the village under your control")
        print("---------------------------------------------------------\n")

    def _process_user_choice(self):
        """Process the user input for choice of hut to enter"""
        verifying_choice = True
        idx = 0
        print("Current occupants: %s" % self.get_occupants())
        while verifying_choice:
            user_choice = input("Choose a hut number to enter (1-5): ")
            try:
                idx = int(user_choice)
            except ValueError as e:
                print("Invalid input, args: %s \n" % e.args)
                continue

            try:
                if idx < 1: # 用户输入的数不会引发异常但是不正确
                    print("Number should be in the range 1-5. Try again")
                    continue

                if self.huts[idx - 1].is_acquired:
                    print("You have already acquired this hut. Try again."
                          "<INFO: You can NOT get healed in already acquired hut.>")
                else:
                    verifying_choice = False
            except IndexError:
                print("Invalid input : ",idx)
                print("Number should be in the range 1-5. Try again")
                continue

        return idx

    def _occupy_huts(self):
        """Randomly occupy the huts with one of: friend, enemy or 'None'"""
        for i in range(5):
            choice_lst = ['enemy','friend',None]
            computer_choice = random.choice(choice_lst)
            if computer_choice == 'enemy':
                name = 'enemy-' + str(i+1)
                # 创建一个Hut类的实例,因为第2个参数是Hut类的,所以我们创建了一个GameUnit
                # 类的实例
                self.huts.append(Hut(i+1,OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'Knight-' + str(i+1)
                self.huts.append(Hut(i+1,Knight(name)))
            else:
                self.huts.append(Hut(i+1,computer_choice))

    def play(self):
        """Workhorse method to play the game.

        Controls the high level logic to play the game. This is called from
        the main program to begin the game execution.
        """
        self.player = Knight() # 创建一个Knight的实例
        self._occupy_huts()
        acquired_hut_counter = 0

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_hut_counter < 5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <=0:
                print_bold("YOU LOSE :( Better luck next time")
                break

            if self.huts[idx-1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == 5:
            print_bold("Congratulations! YOU WIN!!!")

if __name__ == '__main__':
    game = AttackOfTheOrcs() # 创建实例
    game.play() # 调用play()方法
