"""
    作者:北辰
    日期:12/05/2019
    功能:兽人之袭文本游戏的简化版本(顶层代码),提供一个带有bug的版本用来测试异常类
"""

from AttackOfTheOrcs_v1_1_5 import Knight
#from gameuniterror import GameUnitError
from gameuniterror_v2 import GameUnitError,HealthMeterException

if __name__ == '__main__':
    print("Creating a Knight..")
    knight = Knight("Sir Bar")
    # Assume the knight has sustained injuries in the combat.
    knight.health_meter = 10
    knight.show_health()
    # Heal the knight by 100 hit points. This is the 'artificial bug'!
    # The Knight can have a maximum of 40 hit points.
    try:
        knight.heal(heal_by=100,full_healing=False)
    except GameUnitError as e:
        print(e)
        print(e.error_message)
    knight.show_health()