"""
    作者:北辰
    日期:26/05/2019
    功能:兽人之袭游戏设计模式之策略模式:使用python特有的方法来实现与跳跃功能相关的策略
"""

from abc import ABCMeta, abstractmethod
from collections import Callable

class AbstractGameUnit(metaclass=ABCMeta):
    def __init__(self,name,jump_strategy):
        # 确保jump_strategy是一个函数
        assert(isinstance(jump_strategy,Callable))
        self.name = name
        self.jump = jump_strategy

    @abstractmethod
    def info(self):
        pass

class DwarfFighter(AbstractGameUnit):
    def info(self):
        print("I am a great dwarf of the eastern foo mountain!")

def can_not_jump():
    print("--> CanNotJump.jump: I can not jump")

def power_jump():
    print("--> PowerJump.jump: I can jump 100 feet from the ground!")

def horse_jump():
    print("--> HorseJump.jump: Jumping my horse.")


if __name__ == '__main__':
    dwarf = DwarfFighter("Dwarf",can_not_jump)
    print("\n{STRATEGY-I} Dwarf trying to jump:")
    dwarf.jump()
    print("-" * 56)

    # Optionally change the jump strategy later
    print("\n{STRATEGY-II} Dwarf given a 'magic potion' to jump:")
    dwarf.jump = power_jump
    dwarf.jump()
    print("-" * 56)