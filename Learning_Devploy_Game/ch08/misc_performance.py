"""
    作者:北辰
    日期:01/06/2019
    功能:性能优化的一些事项
"""

import timeit
from collections import deque
from collections import defaultdict

sample_size_1 = 1000000
sample_size_2 = 100

def no_list_comprehension_ex1():
    """使用普通的for循环来产生列表"""
    mylist = []
    for i in range(sample_size_1):
        mylist.append(i*i)

def list_comprehension_ex1():
    """使用列表推导式来改善性能"""
    mylist = [i*i for i in range(sample_size_1)]

def no_list_comprehension_ex2():
    """使用嵌套循环来产生列表"""
    mylist = []
    for i in range(sample_size_2):
        for j in range(sample_size_2):
            mylist.append(i*j)

def list_comprehension_ex2():
    """使用列表推导式改善嵌套循环的性能"""
    mylist = [i*j for i in range(sample_size_2) for j in range(sample_size_2)]

def no_dict_comprehension():
    """使用循环来产生字典元素"""
    d = {}
    for i in range(sample_size_1):
        d[i] = i*i

def dict_comprehension():
    """使用字典推导式来产生字典的元素"""
    d = {i:i*i for i in range(sample_size_1)}

def no_if_condition_loop_opt():
    """for循环里面包含if..else语句"""
    num = 1000
    val = 0
    for i in range(sample_size_1):
        if num < 100:
            val += i*i
        else:
            val += i*i*i
    return val

def if_condition_loop_opt():
    """交换for循环和if..else代码块来编写相同的逻辑"""
    num = 1000
    val = 0
    if num < 100:
        for i in range(sample_size_1):
            val += i*i
    else:
        for i in range(sample_size_1):
            val += i*i*i
    return val

def not_using_try():
    mylist = []
    val = 1
    for i in range(sample_size_1):
        if(i==0):
            val /= 10
        else:
            val /= i
        mylist.append(val)

def using_try():
    """使用try...except子句来替换if...else子句"""
    mylist = []
    val = 1
    for i in range(sample_size_1):
        try:
            val /= i
        except ZeroDivisionError:
            val /= 10
    mylist.append(val)

#mylist = [i*i for i in range(1000)] 提前创建列表,因此函数只比较for循环内的操作
def data_struct_choice_list():
    """使用列表作为数据结构"""
    mylist = [i*i for i in range(1000)]
    val = 0
    for j in range(100000):
        if(j in mylist):
            val += j
        else:
            val += j*2
    return val

#myset = {i*i for i in range(1000)} 提前创建集合,因此函数只比较for循环内的操作
def data_struct_choice_set():
    """使用集合作为数据结构"""
    # Python 'set' comprehension just like a dict or list
    myset = {i*i for i in range(1000)}
    val = 0
    for j in range(100000):
        if (j in myset):
            val += j
        else:
            val += j*2
    return val

# Create the list and deque objects
lst = list(range(sample_size_1))
dq = deque(range(sample_size_1))

def list_example():
    """使用普通的队列的pop方法"""
    for i in range(sample_size_1):
        lst.pop()

def deque_example():
    """使用deque双端队列的pop方法"""
    for i in range(sample_size_1):
        dq.pop()

def dict_counter():
    """使用标准字典并计算每个元素出现的次数"""
    unit_headcount = {}
    game_characters = [
        'elf','knight','orc',
        'orc','knight','knight']*sample_size_1
    # Loop over the list
    for unit in game_characters:
        # Count the occurance of each character and store
        # the result in the dictionary object unit_headcount
        if unit in unit_headcount:
            unit_headcount[unit] += 1
        else:
            unit_headcount[unit] = 1

    return unit_headcount

def defaultdict_counter():
    """使用defaultdict类计算字典中每个元素出现的次数"""
    unit_headcount = defaultdict(int)
    game_characters = [
                          'elf', 'knight', 'orc',
                          'orc', 'knight', 'knight'] * sample_size_1
    for unit in game_characters:
        unit_headcount[unit] += 1

    return unit_headcount


def run_timeit(func_1,func_2,num=1):
    """Run timeit.timeit for the given function names (input args)"""

    t1 = timeit.timeit("%s()"%func_1,         #number参数代表给定的函数将被执行的次数
        setup="from __main__ import %s"%func_1,number=num)
    t2 = timeit.timeit("%s()" % func_2,
                       setup="from __main__ import %s" % func_2, number=num)

    print("Function: {func}, time: {t}".format(func=func_1,t=t1))
    print("Function: {func}, time: {t}".format(func=func_2,t=t2))

if __name__ == '__main__':
    # t1 = timeit.timeit(
    #     "no_list_comprehension_ex1()",
    #     setup="from __main__ import no_list_comprehension_ex1"
    # )
    #
    # t2 = timeit.timeit(
    #     "list_comprehension_ex1()",
    #     setup="from __main__ import list_comprehension_ex1"
    # )
    #
    # t_11 = timeit.timeit(
    #     "no_list_comprehension_ex2()",
    #     setup="from __main__ import no_list_comprehension_ex2"
    # )
    #
    # t_21 = timeit.timeit(
    #     "list_comprehension_ex2()",
    #     setup="from __main__ import list_comprehension_ex2"
    # )
    # print("Without list comprehension :",t1)
    # print("With list comprehension    :",t2)
    # print("="*100)
    # print("Without list comprehension :", t_11)
    # print("With list comprehension    :", t_21)
    # print("=" * 100)
    # run_timeit("dict_comprehension","no_dict_comprehension")
    # print("=" * 100)
    # run_timeit("no_if_condition_loop_opt","if_condition_loop_opt")
    # run_timeit("not_using_try","using_try")
    # print("=" * 100)
    # run_timeit("data_struct_choice_list","data_struct_choice_set")
    print("=" * 100)
    run_timeit("list_example","deque_example")
    print("=" * 100)
    run_timeit("dict_counter","defaultdict_counter")