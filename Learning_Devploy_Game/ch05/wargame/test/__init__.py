"""
    作者:北辰
    日期:17/05/2019
    功能:创建python包的__init__.py文件
"""

import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

#print("in __init__.py sys.path:\n ",sys.path)