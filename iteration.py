def for_loop(n: int) -> int:
    """for循环"""
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


def while_loop(n: int) -> int:
    """while循环"""
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res


def while_loop_ii(n: int) -> int:
    """while循环"""
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
        i *= 2
    return res


def nested_for_loop(n: int) -> int:
    """嵌套for循环"""
    res = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"{i , j} "
    return res


"""Driver code"""
if __name__ == "__main__":
    n=5
    res = for_loop(n)
    print(f"for循环的结果是：{res}")
    res = while_loop(n)
    print(f"while循环的结果是：{res}")
    res = while_loop_ii(n)
    print(f"while两次循环的结果是：{res}")
    res = nested_for_loop(n)
    print(f"嵌套for循环的结果是：{res}")