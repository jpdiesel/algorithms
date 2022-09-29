from collections import Counter


def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    for number in nums:
        if type(number) is not int or number < 0:
            return False

    repeated_values = Counter(nums)
    result = [number for number, value in repeated_values.items() if value > 1]

    if result == []:
        return False
    else:
        return result[0]

# feito a partir do link:
# https://stackoverflow.com/questions/52072381/how-to-print-only-the-duplicate-elements-in-python-list
