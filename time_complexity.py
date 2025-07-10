def constant(n: int) -> int:
    """常数时间复杂度 O(1)"""
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count


def linear(n: int) -> int:
    """线性时间复杂度 O(n)"""
    count = 0
    for _ in range(n):
        count += 1
    return count


def array_traversal(nums: list[int]) -> int:
    """线性数组遍历 O(n)"""
    count = 0
    for num in nums:
        count += 1
    return count


def quadratic(n: int) -> int:
    """平方时间复杂度 O(n^2)"""
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def bubble_sort(nums: list[int]) -> int:
    """冒泡排序 O(n^2)"""
    # 计数器
    count = 0
    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            count += 1
    return count


def exponential(n: int) -> int:
    """指数(循环实现)时间复杂度 O(2^n)"""
    count = 0
    base = 1
    # 细胞分裂模拟
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    return count


def exponential_recursive(n: int) -> int:
    """指数(递归实现)时间复杂度 O(2^n)"""
    if n == 1:
        return 1
    else:
        return exponential_recursive(n - 1) + exponential_recursive(n - 1) + 1
    

def logiarithmic(n: int) -> int:
    """对数(循环实现)时间复杂度 O(log n)"""
    count = 0
    while n > 1:
        n /= 2
        count += 1
    return count


def logarithmic_recursive(n: int) -> int:
    """对数(递归实现)时间复杂度 O(log n)"""
    if n <= 1:
        return 0
    else:
        return logarithmic_recursive(n / 2) + 1
    


def linear_log_recursive(n: int) -> int:
    """线性(嵌套循环)对数时间复杂度 O(n log n)"""
    if n <= 1:
        return 1
    count = linear_log_recursive(n // 2) + linear_log_recursive(n // 2)
    for _ in range(n):
        count += 1
    return count


def factorial_recursive(n: int) -> int:
    """阶乘(递归实现) O(n!)"""
    if n == 0:
        return 1
    count = 0
    for i in range(1, n + 1):
        count += factorial_recursive(n - 1)
    return count



"""Driver code"""
if __name__ == "__main__":
    print("常数阶的操作数量:", constant(100000))
    print("线性阶的操作数量:", linear(100000))
    print("数组遍历的操作数量:", array_traversal([0] * 8))
    print("二次阶的操作数量:", quadratic(8))
    print("冒泡排序的操作数量:", bubble_sort([5, 3, 8, 6, 2, 7, 4, 1]))
    print("指数阶的操作数量:", exponential(8))
    print("指数阶(递归)的操作数量:", exponential_recursive(8))
    print("对数阶的操作数量:", logiarithmic(8))
    print("对数阶(递归)的操作数量:", logarithmic_recursive(8))
    print("线性(嵌套循环)对数阶的操作数量:", linear_log_recursive(8))
    print("阶乘(递归)的操作数量:", factorial_recursive(5))