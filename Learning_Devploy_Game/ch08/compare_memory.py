"""
    作者:北辰
    日期:02/06/2019
    功能:比较内存效率,从命令行运行: python -m memory_profiler compare_memory.py
"""

from itertools import chain


@profile
def list_comp_memory():
    """使用普通的列表"""
    sample_size = 10000
    my_data = [i for i in range(sample_size)]

@profile
def generator_expr_memory():
    """使用生成器"""
    sample_size = 10000
    my_data = (i for i in range(sample_size))

# Create some lists. these will be 'chained' together
data_1 = ['x']*10000
data_2 = ['y']*10000
data_3 = ['z']*10000

@profile
def chain_memory():
    mychain = chain(data_1,data_2,data_3)
    for i in mychain:
        pass

@profile
def list_memory():
    mylist = data_1 + data_2 + data_3
    for i in mylist:
        pass

if __name__ == '__main__':
    list_comp_memory()
    generator_expr_memory()
    chain_memory()
    list_memory()