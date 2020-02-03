"""
    作者:北辰
    日期:26/05/2019
    功能:兽人之袭游戏设计模式之简单工厂:使用python特有的方法来实现创建新的招募角色
"""


# Some dummy classes to represent factory products (not documented)
class ElfRider:
    pass
class Knight:
    pass
class OrcRider:
    pass
class DwarfFighter:
    pass
class Fairy:
    pass
class Wizard:
    pass
class ElfLord:
    pass
class OrcFighter:
    pass

class UnitFactory:
    """A factory class to create game units.

    This is an example that shows how we can use Python classes (which are
    first-class objects) and a class method to represent a simple factory. In
    this example, the client does not instantiates factory. See the book
    mentioned at the top of this file for detailed explanation.

    :cvar units_dict: Python dictionary created as a class variable. This
            dictionary holds names (types) of the game units as its keys and
            the corresponding values are the concrete classes representing the
            game character.
    .. seealso:: `Kingdom` class and various classes like `ElfRider`, `Knight`
    """
    units_dict = {
        'elfrider':ElfRider,
        'knight':Knight,
        'dwarffighter':DwarfFighter,
        'orcrider':OrcRider,
        'fairy':Fairy,
        'wizard':Wizard,
        'elflord':ElfLord,
        'orcfighter':OrcFighter
    }

    @classmethod
    def create_unit(cls,unit_type):
        """Return an instance of a game unit.

        This is a class method and it uses the class variable unit_dict to
        create and return an instance of a game unit class (e.g. ElfRider(),
        Knight(), Dwarf() and so on.

        :arg unit_type: A string representing the unit type (e.g. 'elfrider')
        :return:Instance of a game unit.
        """
        key = unit_type.lower()
        return cls.units_dict.get(key)()

class Kingdom:
    """Class that uses a 'factory' to get an instance of a game character.

    :cvar UnitFactory factory: This is a class variable that represents
             UnitFactory class.

    .. seealso:: class `UnitFactory`
    """
    factory = UnitFactory # 工厂被声明为一个类变量

    def recruit(self,unit_type):
        """Recruit a new game unit, creating it first using a factory.

        This method recruits a new unit for the 'kingdom'. First it 'orders' a
        unit from the 'factory' which is a 'class variable'. Then pays the
        price and updates some record. The pay_gold and update_record methods
        are dummy, they just print some information.

        :arg string unit_type:  The type (name) of unit requested.
        :return: A game unit instance returned by the factory.
        """
        # ----------------------------------------------------------------------
        # For Python 2.7, type(self) is not same as self.__class__. So just to
        # make the code compatible with both Python 2.7 and 3.5, we will use
        # self.__class__ (supported even by v3.5) to retrieve the class.
        # ----------------------------------------------------------------------
        ## unit = type(self).factory.create_unit(unit_type) # disabled
        unit = self.__class__.factory.create_unit(unit_type)
        self.pay_gold(unit)
        self.update_records(unit)
        return unit

    def pay_gold(self, something):
        print("GOLD PAID")

    def update_records(self, something):
        print("Some logic (not shown) to update database of units")

if __name__ == '__main__':
    # 不需要创建任何工厂实例
    k = Kingdom()
    elf_unit = k.recruit("ElfRider")
    print(elf_unit)
