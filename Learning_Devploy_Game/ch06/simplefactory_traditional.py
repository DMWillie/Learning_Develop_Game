"""
    作者:北辰
    日期:26/05/2019
    功能:兽人之袭游戏设计模式之简单工厂:使用传统方法来实现创建新的招募角色
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
    """A simple factory to create and return instances of game units

    .. seealso:: `Kingdom` class and various classes like `ElfRider`, `Knight`
    """
    def create_unit(self,unit_type):
        """The work horse method to create and return instances of a game unit.

        :arg string unit_type: The type of unit requested by the client.
        :return: An instance of a game unit such as ElfRider, Knight, Dwarf etc

        .. todo:: Make this method more robust. e.g. change the string to all
            lower case, add exception handling.
        """
        unit = None

        if unit_type == 'ElfRider':
            unit = ElfRider()
        elif unit_type == 'Knight':
            unit = Knight()
        elif unit_type == 'DwarfFighter':
            unit = DwarfFighter()
        elif unit_type == 'OrcRider':
            unit = OrcRider()
        elif unit_type == 'Fairy':
            unit = Fairy()
        elif unit_type == 'Wizard':
            unit = Wizard()
        elif unit_type == 'ElfLord':
            unit = ElfLord()
        elif unit_type == 'OrcFighter':
            unit = OrcFighter()

        return unit

class Kingdom:
    """Class that uses a 'factory' to get an instance of a game character.

    :arg UnitFactory factory: A factory instance used to create new units.
    :ivar UnitFactory factory: Represents a factory instance used to create new
          game units.

    .. seealso:: class `UnitFactory`
    """
    def __init__(self,factory):
        self.factory = factory

    def recruit(self,unit_type):
        """Recruit a new game unit, creating it first using a factory.

        This method recruits a new unit for the 'kingdom'. First it 'orders' a
        unit from the factory instance, then pays the price and updates some
        record. The pay_gold and update_record methods are dummy, they just
        print some information.

        :arg string unit_type:  The type (name) of unit requested.
        :return: A game unit instance returned by the factory.
        """
        unit = self.factory.create_unit(unit_type)
        self.pay_gold(unit)
        self.update_records(unit)
        return unit

    def pay_gold(self,something):
        print("GOLD PAID")

    def update_records(self,something):
        print("Some logic (not shown) to update database of units")

if __name__ == '__main__':
    factory = UnitFactory()
    k = Kingdom(factory)
    elf_unit = k.recruit("ElfRider")
    print(elf_unit)
