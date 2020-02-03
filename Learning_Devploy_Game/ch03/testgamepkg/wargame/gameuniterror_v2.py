"""
    作者:北辰
    日期:12/05/2019
    版本:2.0
    功能:兽人之袭文本游戏的顶层代码的异常类
    2.0改进之处:将GameUnitError类作为一个基础的异常类,为不同特定异常继承基类
"""

class GameUnitError(Exception):
    """Custom exceptions class for the 'AbstractGameUnit' and its subclass"""
    def __init__(self,message=''):
        super().__init__(message)
        self.padding = '-'*50 + '\n'
        self.error_message = "Unspecified Error!"

class HealthMeterException(GameUnitError):
    """Custom exception to report Health Meter related problems"""
    def __init__(self,message=''):
        super().__init__(message)
        self.error_message = (self.padding+
                              "ERROR: Health Meter Problem"+
                              '\n'+self.padding)