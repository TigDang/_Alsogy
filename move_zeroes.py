"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

def move_zeroes(nums):
    """
    Перемещает все нули в конец массива, сохраняя порядок остальных элементов.
    
    Args:
        nums: List[int] - массив целых чисел
    
    Returns:
        None - изменяет массив на месте
    """
    
    k = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
    for i in range(k, len(nums)):
        nums[i] = 0


def test_move_zeroes():
    """Тесты для функции move_zeroes"""
    
    print("Запуск тестов...")
    
    # Тест 1: Пример из условия
    nums1 = [0, 1, 0, 3, 12]
    expected1 = [1, 3, 12, 0, 0]
    move_zeroes(nums1)
    print(f"Тест 1: {nums1} == {expected1} -> {'PASS' if nums1 == expected1 else 'FAIL'}")
    
    # Тест 2: Один ноль
    nums2 = [0]
    expected2 = [0]
    move_zeroes(nums2)
    print(f"Тест 2: {nums2} == {expected2} -> {'PASS' if nums2 == expected2 else 'FAIL'}")
    
    # Тест 3: Нет нулей
    nums3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    move_zeroes(nums3)
    print(f"Тест 3: {nums3} == {expected3} -> {'PASS' if nums3 == expected3 else 'FAIL'}")
    
    # Тест 4: Все нули
    nums4 = [0, 0, 0]
    expected4 = [0, 0, 0]
    move_zeroes(nums4)
    print(f"Тест 4: {nums4} == {expected4} -> {'PASS' if nums4 == expected4 else 'FAIL'}")
    
    # Тест 5: Нули в начале
    nums5 = [0, 0, 1, 2, 3]
    expected5 = [1, 2, 3, 0, 0]
    move_zeroes(nums5)
    print(f"Тест 5: {nums5} == {expected5} -> {'PASS' if nums5 == expected5 else 'FAIL'}")
    
    # Тест 6: Нули в конце
    nums6 = [1, 2, 3, 0, 0]
    expected6 = [1, 2, 3, 0, 0]
    move_zeroes(nums6)
    print(f"Тест 6: {nums6} == {expected6} -> {'PASS' if nums6 == expected6 else 'FAIL'}")
    
    # Тест 7: Смешанный случай
    nums7 = [0, 1, 0, 2, 0, 3, 0]
    expected7 = [1, 2, 3, 0, 0, 0, 0]
    move_zeroes(nums7)
    print(f"Тест 7: {nums7} == {expected7} -> {'PASS' if nums7 == expected7 else 'FAIL'}")
    
    print("\nТесты завершены!")


def solution_hint():
    """Подсказка к решению"""
    print("""
    ПОДСКАЗКА К РЕШЕНИЮ:
    
    Эффективный подход - использовать два указателя:
    
    1. left - указывает на позицию, куда нужно поместить следующий ненулевой элемент
    2. right - перебирает все элементы массива
    
    Алгоритм:
    - Если nums[right] != 0, то меняем местами nums[left] и nums[right], увеличиваем left
    - Всегда увеличиваем right
    
    Временная сложность: O(n)
    Пространственная сложность: O(1)
    
    Попробуйте реализовать это решение!
    """)


if __name__ == "__main__":
    print("=== ЗАДАЧА: MOVE ZEROES ===")
    print("Реализуйте функцию move_zeroes() выше")
    print("\nДля запуска тестов раскомментируйте строку ниже:")
    print("# test_move_zeroes()")
    print("\nДля получения подсказки раскомментируйте:")
    print("# solution_hint()")
    
    # Раскомментируйте для запуска тестов:
    test_move_zeroes()
    
    # Раскомментируйте для получения подсказки:
    # solution_hint()
