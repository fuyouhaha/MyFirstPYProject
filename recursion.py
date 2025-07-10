def recur(n : int) -> int:
    """普通递归"""
    # 终止条件
    if n == 1:
        return 1
    else:
        # 普通递归调用 + 返回结果
        return n + recur(n - 1)
    

def tail_recur(n: int, res: int = 0) -> int:
    """尾递归"""
    # 终止条件
    if n == 0:
        return res
    else:
        # 尾递归调用 + 返回结果
        return tail_recur(n - 1, res + n)


def fib(n: int) -> int:
    """斐波那契数列：递归"""
    # 终止条件 f(1) = 0, f(2) = 1
    if n == 1 or n == 2:
        return n - 1
    else:
        return fib(n - 1) + fib(n - 2)


def for_loop_recur(n: int) -> int:
    """使用迭代模拟递归"""
    # 使用一个显示的栈来模拟系统调用栈
    stack = []  
    res = 0
    for i in range(n, 0, -1):
        # 通过“入栈操作”来模拟“递”
        stack.append(i)
    while stack:
        # 通过“出栈操作”来模拟“归”
        res += stack.pop()
    return res


"""Driver code"""
if __name__ == "__main__":
    n = 5
    res = recur(n)
    print(f"普通递归的结果是：{res}")
    res = tail_recur(n, 0)
    print(f"尾递归的结果是：{res}")
    res = fib(n)
    print(f"斐波那契数列的结果是：{res}")
    res = for_loop_recur(n)
    print(f"使用迭代模拟递归求和的结果是：{res}")