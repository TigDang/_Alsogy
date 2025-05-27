"""
Задача: Произведение массива кроме самого элемента

Дан целочисленный массив nums, верните массив answer такой, что answer[i] равен 
произведению всех элементов nums, кроме nums[i].

Произведение любого префикса или суффикса nums гарантированно помещается в 32-битное целое число.

Вы должны написать алгоритм, который работает за O(n) времени и без использования операции деления.

Примеры:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Ограничения:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- Произведение любого префикса или суффикса nums помещается в 32-битное целое число
"""


def product_of_array_except_self(nums: list[int]) -> list[int]:
    """
    Решение задачи "Произведение массива кроме самого элемента"
    
    Подсказки для решения:
    1. Можно использовать два прохода: слева направо и справа налево
    2. В первом проходе считаем произведения всех элементов слева от текущего
    3. Во втором проходе умножаем на произведения всех элементов справа
    4. Можно оптимизировать до O(1) дополнительной памяти
    
    Args:
        nums: список целых чисел
        
    Returns:
        список произведений всех элементов кроме текущего
    """

    result = []
    left = [1]
    right = [1]
    for i in range(1,len(nums)):
        right.append(right[i-1]*nums[i-1])
    for i in range(len(nums)-1, 0, -1):
        left.append(left[len(nums)-i-1]*nums[i])
    left.reverse()
    for i in range(len(nums)):
        result.append(left[i]*right[i])
    return result
    



def test_product_of_array_except_self():
    """Тесты для проверки решения"""
    
    # Тест 1: Базовый случай
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    result1 = product_of_array_except_self(nums1)
    assert result1 == expected1, f"Тест 1 не прошел: ожидалось {expected1}, получено {result1}"
    print("✅ Тест 1 прошел: [1,2,3,4] -> [24,12,8,6]")
    
    # Тест 2: Массив с нулем
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    result2 = product_of_array_except_self(nums2)
    assert result2 == expected2, f"Тест 2 не прошел: ожидалось {expected2}, получено {result2}"
    print("✅ Тест 2 прошел: [-1,1,0,-3,3] -> [0,0,9,0,0]")
    
    # Тест 3: Массив с отрицательными числами
    nums3 = [-1, -2, -3]
    expected3 = [6, 3, 2]
    result3 = product_of_array_except_self(nums3)
    assert result3 == expected3, f"Тест 3 не прошел: ожидалось {expected3}, получено {result3}"
    print("✅ Тест 3 прошел: [-1,-2,-3] -> [6,3,2]")
    
    # Тест 4: Минимальный случай
    nums4 = [2, 3]
    expected4 = [3, 2]
    result4 = product_of_array_except_self(nums4)
    assert result4 == expected4, f"Тест 4 не прошел: ожидалось {expected4}, получено {result4}"
    print("✅ Тест 4 прошел: [2,3] -> [3,2]")
    
    # Тест 5: Массив с единицами
    nums5 = [1, 1, 1, 1]
    expected5 = [1, 1, 1, 1]
    result5 = product_of_array_except_self(nums5)
    assert result5 == expected5, f"Тест 5 не прошел: ожидалось {expected5}, получено {result5}"
    print("✅ Тест 5 прошел: [1,1,1,1] -> [1,1,1,1]")
    
    print("\n🎉 Все тесты прошли успешно!")


def demonstrate_solution():
    """Демонстрация работы решения"""
    print("=== Демонстрация решения ===")
    
    test_cases = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
        [2, 3, 4, 5]
    ]
    
    for i, nums in enumerate(test_cases, 1):
        print(f"\nПример {i}:")
        print(f"Входной массив: {nums}")
        result = product_of_array_except_self(nums)
        print(f"Результат: {result}")
        
        # Показываем как вычисляется каждый элемент
        print("Объяснение:")
        for j, num in enumerate(nums):
            other_nums = [nums[k] for k in range(len(nums)) if k != j]
            product = 1
            for x in other_nums:
                product *= x
            print(f"  answer[{j}] = произведение {other_nums} = {product}")


if __name__ == "__main__":
    print("🚀 Начинаем тренировку с задачей от Яндекса!")
    print("\n📝 Описание задачи:")
    print("Нужно найти произведение всех элементов массива кроме текущего")
    print("Ограничения: O(n) время, без деления")
    
    print("\n💡 Для решения откройте функцию product_of_array_except_self() и замените pass на ваш код")
    
    try:
        test_product_of_array_except_self()
    except AssertionError as e:
        print(f"\n❌ {e}")
        print("💪 Продолжайте работать над решением!")
    except Exception as e:
        print(f"\n⚠️  Ошибка в коде: {e}")
        print("🔧 Проверьте реализацию функции")
    
    demonstrate_solution()