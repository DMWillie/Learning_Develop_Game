"""
    作者:北辰
    日期:27/05/2019
    功能:兽人之袭游戏设计模式之简单工厂:使用传统方法来实现生产各种装备
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

class Kingdom:
    def buy_accessories(self,armor_type,locket_type):
        if armor_type == 'ironjacket':
            armor = IronJacket()
        elif armor_type == 'powersuit':
            armor = PowerSuit()
        elif armor_type == 'mithril':
            armor = MithrilArmor()

        if locket_type == 'goldlocket':
            locket = GoldLocket()
        elif locket_type == 'superlocket':
            locket = SuperLocket()
        elif locket_type == 'magiclocket':
            locket = MagicLocket()

        accessories = [armor,locket]
        self.pay_gold(accessories)
        self.update_records(accessories)

    def pay_gold(self,accessories):
        print("GOLD PAID")

    def update_records(self,accessories):
        print("Some logic (not shown) to update database of accessories")

if __name__ == '__main__':
    k = Kingdom()
    k.buy_accessories("mithril","magiclocket")

