"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

def two_sum(nums, target):
    """
    Найти индексы двух чисел, которые в сумме дают target.
    
    Args:
        nums: List[int] - массив целых чисел
        target: int - целевая сумма
        
    Returns:
        List[int] - список из двух индексов
    """

    hashmap = {}
    for i, num in enumerate(nums):
        hashmap[target-num] = i
    
    for i, num in enumerate(nums):
        if num in hashmap and hashmap[num] != i:
            return [hashmap[num], i]

    return []


def test_two_sum():
    """Тесты для функции two_sum"""
    
    # Тест 1: Базовый случай
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    expected1 = [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
    assert sorted(result1) == sorted(expected1), f"Тест 1 не прошёл: ожидался {expected1}, получен {result1}"
    print("✅ Тест 1 прошёл: базовый случай")
    
    # Тест 2: Числа в конце массива
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    expected2 = [1, 2]  # nums[1] + nums[2] = 2 + 4 = 6
    assert sorted(result2) == sorted(expected2), f"Тест 2 не прошёл: ожидался {expected2}, получен {result2}"
    print("✅ Тест 2 прошёл: числа в конце массива")
    
    # Тест 3: Одинаковые числа
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    expected3 = [0, 1]  # nums[0] + nums[1] = 3 + 3 = 6
    assert sorted(result3) == sorted(expected3), f"Тест 3 не прошёл: ожидался {expected3}, получен {result3}"
    print("✅ Тест 3 прошёл: одинаковые числа")
    
    # Тест 4: Отрицательные числа
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    result4 = two_sum(nums4, target4)
    expected4 = [2, 4]  # nums[2] + nums[4] = -3 + -5 = -8
    assert sorted(result4) == sorted(expected4), f"Тест 4 не прошёл: ожидался {expected4}, получен {result4}"
    print("✅ Тест 4 прошёл: отрицательные числа")
    
    # Тест 5: Большой массив
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target5 = 19
    result5 = two_sum(nums5, target5)
    expected5 = [8, 9]  # nums[8] + nums[9] = 9 + 10 = 19
    assert sorted(result5) == sorted(expected5), f"Тест 5 не прошёл: ожидался {expected5}, получен {result5}"
    print("✅ Тест 5 прошёл: большой массив")
    
    # Тест 6: Нуль в массиве
    nums6 = [0, 4, 3, 0]
    target6 = 0
    result6 = two_sum(nums6, target6)
    expected6 = [0, 3]  # nums[0] + nums[3] = 0 + 0 = 0
    assert sorted(result6) == sorted(expected6), f"Тест 6 не прошёл: ожидался {expected6}, получен {result6}"
    print("✅ Тест 6 прошёл: нуль в массиве")
    
    print("\n🎉 Все тесты прошли успешно!")


if __name__ == "__main__":
    print("Запуск тестов для задачи Two Sum:")
    print("=" * 40)
    
    try:
        test_two_sum()
    except Exception as e:
        print(f"❌ Ошибка при выполнении тестов: {e}")
        print("\n💡 Совет: реализуйте функцию two_sum для прохождения тестов")
    
    print("\n" + "=" * 40)
    print("Подсказки для решения:")
    print("1. Наивный подход: O(n²) - два вложенных цикла")
    print("2. Оптимальный подход: O(n) - используйте hashmap/словарь")
    print("3. Не забудьте обработать краевые случаи")