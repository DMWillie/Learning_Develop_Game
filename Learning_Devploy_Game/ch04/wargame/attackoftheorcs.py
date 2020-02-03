"""
    作者:北辰
    日期:13/05/2019
    版本:2.0.0
    功能:兽人之袭文本游戏,AttackOfTheOrcs类
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
from gameutils import print_bold
from hut import Hut
from knight import Knight
from orcrider import OrcRider

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