"""
    作者:北辰
    日期:06/06/2019
    功能:Python多线程中的Pool类使用示例
"""

import multiprocessing

def get_result(num):
    """Trivial function used in multiprocessing example"""
    process_name = multiprocessing.current_process()
    print("Current process:",process_name,", Input Number:",num)
    return 10*num

if __name__ == '__main__':
    numbers = [2,4,6,8]
    # Create two worker processes.
    pool = multiprocessing.Pool(2)

    # Use Pool.map method to run the task using the pool of processes.
    # mylist = pool.map(func=get_result,iterable=numbers)

    # Use Pool.apply_async method to run the tasks
    results = [pool.apply_async(get_result,args=(num,))
               for num in numbers]
    # The elements of results list are instances of Pool.ApplyResult.
    # Use the object's get() method tp get the final values.
    mylist = [p.get() for p in results]

    # Use Pool.apply method to run the task using pool of processes
    # mylist = [pool.apply(get_result,args=(num,)) for num in numbers]

    # Stop the worker processes
    pool.close()
    # Join the processes
    pool.join()
    print("Output:",mylist)
