"""
    作者:北辰
    日期:12/05/2019
    版本:1.0
    功能:兽人之袭文本游戏的顶层代码的异常类
"""

class GameUnitError(Exception):
    """Custom exceptions class for the 'AbstractGameUnit' and its subclass"""
    def __init__(self,message='',code=000):
        super().__init__(message)
        self.error_message = '-'*50 + '\n'
        self.error_dict = { #保存错误代码信息
            000: "ERROR-000: Unspecified Error!",
            101: "ERROR-101: Health Meter Problem!",
            102: "ERROR-102: Attack issue! Ignored",
        }
        try:  #编辑错误信息
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '-'*50