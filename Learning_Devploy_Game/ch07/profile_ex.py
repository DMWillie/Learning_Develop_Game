"""
    作者:北辰
    日期:30/05/2019
    功能:使用Cprofile模块进行代码分析(从命令提示符输入:python -m cProfile profile_ex.py)
"""

def test_1():
    return 100*100

def test_2():
    x = []
    for i in range(10000):
        temp = i/1000.0
        x.append(temp*temp)
    return x

def test_3(condition=False):
    """Trivial recursion example"""
    if condition:
        test_3()

if __name__ == '__main__':
    a = test_1()
    b = test_2()
    c = test_3(True)