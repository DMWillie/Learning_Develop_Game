"""
    作者:北辰
    日期:27/05/2019
    功能:兽人之袭游戏设计模式之抽象工厂:使用python特有的方法来实现生产各种定制化的装备
"""

# Some dummy classes to represent factory products (not documented)
class IronJacket:
    pass
class PowerSuit:
    pass
class MithrilArmor:
    pass
class GoldLocket:
    pass
class SuperLocket:
    pass
class MagicLocket:
    pass
class DwarfIronJacket:
    pass
class DwarfPowerSuit:
    pass
class DwarfMithrilArmor:
    pass
class DwarfGoldLocket:
    pass
class DwarfSuperLocket:
    pass
class DwarfMagicLocket:
    pass

class AccessoryFactory:
    """A factory base class to create various game accessories.

    This is an example that shows how we can use Python classes (which are
    first-class objects) and a class method to represent a simple factory. In
    this example, the client does not instantiates factory. See the book
    mentioned at the top of this file for detailed explanation.

    :cvar armor_dict: Python dictionary created as a class variable. This
            dictionary holds names of the armor accessories as its keys and
            the corresponding values are the concrete classes representing the
            armor accessory for the game units. This class variable may be
            overridden in subclasses.
    :cvar armor_dict: Similar to `armor_dict` , a dictionary created as a class
            variable to hold concrete classes representing the 'locket'
            accessory. This class variable may be
            overridden in subclasses.

    .. seealso:: `Kingdom.buy_accessories` , `DwarfKingdom`
                 Also review the code in `simplefactory_pythonic.py`
    """
    armor_dict = {
        'ironjacket': IronJacket,
        'powersuit': PowerSuit,
        'mithril': MithrilArmor
    }
    locket_dict = {
        'goldlocket': GoldLocket,
        'superlocket': SuperLocket,
        'magiclocket': MagicLocket
    }

    @classmethod
    def create_armor(cls,armor_type):
        """Return an instance of an armor accessory

        This is a class method and it uses the class variable armor_dict to
        create and return an instance of an armor accessory (e.g. IronJacket(),
        PowerSuit() etc.

        :arg string armor_type: A string representing the armor type
        :return: Instance of an armor accessory such as IronJacket().
        """
        return cls.armor_dict.get(armor_type)()

    @classmethod
    def create_locket(cls,locket_type):
        """Return an instance of a locket accessory

        This is a class method and it uses the class variable locket_dict to
        create and return an instance of an armor accessory (e.g. GoldLocket(),
        DwarfGoldLocket() etc.

        :arg string armor_type: A string representing the armor type
        :return: Instance of an armor accessory such as GoldLocket().
        """
        return cls.locket_dict.get(locket_type)()

class DwarfAccessoryFactory(AccessoryFactory):
    """A factory for creating accessories customized for Dwarf game character.

    Redefines the class variables, armor_dict and locket_dict.

    .. seealso:: the superclass for more details.
    """
    # Redefine the accessory dictionaries.
    armor_dict = {
        'ironjacket': DwarfIronJacket,
        'powersuit': DwarfPowerSuit,
        'mithril': DwarfMithrilArmor
    }
    locket_dict = {
        'goldlocket': DwarfGoldLocket,
        'superlocket': DwarfSuperLocket,
        'magiclocket': DwarfMagicLocket
    }


class Kingdom:
    """Class that uses a 'factory' to create the desired accessory.

    :cvar factory: This is a class variable that represents
             AccessoryFactory class or its subclass.

    .. seealso:: class `AccessoryFactory`
    """
    # Define which factory class you want to use. (Redefined in subclasses)
    factory = AccessoryFactory

    def buy_accessories(self,armor_type,locket_type):
        """Create accessories using factories, pay gold and update record.

        Demonstrates how to use concrete factory classes to create accessory
        objects (without instantiating the factories)

        The pay_gold and update_records are just dummy methods.

        :arg string armor_type: Armor type to be created.
        :arg string locket_type: Locket type to be created
        .. seealso:: simplefactory_pythonic.py
        """
        # ----------------------------------------------------------------------
        # For Python 2.7, type(self) is not same as self.__class__. So just to
        # make the code compatible with both Python 2.7 and 3.5 we will use
        # self.__class__ (supported even by v3.5) to retrieve the class.
        # ----------------------------------------------------------------------
        ## armor = type(self).factory.create_armor(armor_type)  # disabled
        ## locket = type(self).factory.create_locket(locket_type) # disabled
        armor = self.__class__.factory.create_armor(armor_type)
        locket = self.__class__.factory.create_locket(locket_type)
        accessories = [armor,locket]
        self.pay_gold(accessories)
        self.update_records(accessories)
        self.print_info(armor,locket)

    def pay_gold(self,accessories):
        """Pay gold for the new accessories (dummy method)."""
        print("GOLD PAID")

    def update_records(self,accessories):
        """Update some record to reflect new accessories (dummy method)."""
        print("Updated database of accessories")

    def print_info(self,armor,locket):
        """Print some information on the newly created accessories

        :arg armor: Should be an instance of an armor class e.g. IronJacket()
        :arg locket: Should be an instance of an armor class e.g. GoldLocket()
        """
        print("Done with shopping in        :",self.__class__.__name__)
        print("  concrete class for armor   :",armor.__class__.__name__)
        print("  concrete class for locket  :",locket.__class__.__name__)

class DwarfKingdom(Kingdom):
    """Class that represents imaginary Kingdom of The Great Dwarfs."""
    # Define which factory you want to use for this kingdom.
    factory = DwarfAccessoryFactory()

if __name__ == '__main__':
    print("Buying accessories in default Kingdom...")
    k = Kingdom()
    k.buy_accessories("ironjacket","goldlocket")
    print("-"*56)
    print("Buying accessories in DwarfKingdom...")
    dwarf_kingdom = DwarfKingdom()
    dwarf_kingdom.buy_accessories("ironjacket","goldlocket")
