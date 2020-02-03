"""
    作者:北辰
    日期:27/05/2019
    功能:兽人之袭游戏设计模式之简单工厂:使用python特有的方法来实现生产各种装备
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

class AccessoryFactory:
    armor_dict = {
        'ironjacket':IronJacket,
        'powersuit':PowerSuit,
        'mithril':MithrilArmor
    }
    locket_dict = {
        'goldlocket':GoldLocket,
        'superlocket':SuperLocket,
        'magiclocket':MagicLocket
    }

    @classmethod
    def create_armor(cls,armor_type):
        return cls.armor_dict.get(armor_type)()

    @classmethod
    def create_locket(cls,locket_type):
        return cls.locket_dict.get(locket_type)()

class Kingdom:
    def __init__(self,factory):
        self.factory = factory

    def buy_accessories(self,armor_type,locket_type):
        armor = self.factory.create_armor(armor_type)
        locket = self.factory.create_locket(locket_type)
        print("kingdom armor:",armor)
        print("kingdom locket:",locket)
        accessories = [armor,locket]
        self.pay_gold(accessories)
        self.update_records(accessories)

    def pay_gold(self,accessories):
        print("GOLD PAID")

    def update_records(self,accessories):
        print("Some logic (not shown) to update database of accessories")

if __name__ == '__main__':
    factory = AccessoryFactory()
    k = Kingdom(factory)
    k.buy_accessories("mithril","magiclocket")

