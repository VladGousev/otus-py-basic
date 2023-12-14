"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import List


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    elif num in {2, 3}:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True


def power_numbers(*args) -> List[int]:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    return [x**2 for x in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(num_list: List[int], filter_name: str) -> List[int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    if filter_name == ODD:
        return list(filter(lambda x: x % 2 != 0, num_list))
    elif filter_name == EVEN:
        return list(filter(lambda x: x % 2 == 0, num_list))
    elif filter_name == PRIME:
        return list(filter(lambda x: is_prime(x), num_list))
    else:
        print("Wrong filter name!")
        return []
