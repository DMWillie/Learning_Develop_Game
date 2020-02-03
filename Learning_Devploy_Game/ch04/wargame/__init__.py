"""
    作者:北辰
    日期:13/05/2019
    版本:2.0.0
    功能:兽人之袭文本游戏,__init__.py表示一个python包
"""

import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path) #添加当前目录的路径到环境变量中,防止报模块找不到的错误
#  optionally print the sys.path for debugging
#print("in __init__.py sys.path:\n ",sys.path)