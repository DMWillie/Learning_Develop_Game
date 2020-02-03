"""
    作者:北辰
    日期:26/05/2019
    功能:兽人之袭游戏设计模式之策略模式:使用传统方法来实现与跳跃功能相关的策略
"""

from abc import ABCMeta,abstractmethod

class AbstractGameUnit(metaclass=ABCMeta):
    def __init__(self,name,jump_object=None):
        self.jump_strategy = None
        self.name = name
        self.set_jump_strategy(jump_object)

    def set_jump_strategy(self,jump_object=None):
        """Set the object that defines the jump strategy(algorithm)"""
        if isinstance(jump_object,JumpStrategy):
            self.jump_strategy = jump_object
        else:
            self.jump_strategy = JumpStrategy()

    def jump(self):
        """Perform jump operation (delegated)"""
        try:
            self.jump_strategy.jump()
        except AttributeError as e:
            print("Error: AbstractGameUnit.jump:",e.args)

    @abstractmethod
    def info(self):
        pass


class DwarfFighter(AbstractGameUnit):
    def info(self):
        print("I am a great dwarf of the eastern foo mountain!")

class JumpStrategy:
    """Set up the object that defines the jump strategy."""
    def jump(self):
        print("--> JumpStrategy.jump: Default jump")

class CanNotJump(JumpStrategy):
    def jump(self):
        print("--> CanNotJump.jump: I can not jump")

class PowerJump(JumpStrategy):
    def jump(self):
        print("--> PowerJump.jump: I can jump 100 feet from the ground!")

class HorseJump(JumpStrategy):
    def jump(self):
        print("--> HorseJump.jump: Jumping my horse.")

if __name__ == '__main__':
    jump_strategy = CanNotJump()
    dwarf = DwarfFighter("Dwarf",jump_strategy)
    print("\n{STRATEGY-I} Dwarf trying to jump:")
    dwarf.jump()
    print("-"*56)

    # Optionally change the jump strategy later
    print("\n{STRATEGY-II} Dwarf given a 'magic potion' to jump:")
    dwarf.set_jump_strategy(PowerJump())
    dwarf.jump()
    print("-"*56)