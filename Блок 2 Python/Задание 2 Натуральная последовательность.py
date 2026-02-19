def missing_number(nums):
    """Возвращает единственное отсутствующее число в последовательности
    натуральных чисел от 1 до n, где n = len(nums) + 1"""
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(missing_number(nums))