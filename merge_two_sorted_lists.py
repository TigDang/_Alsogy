"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""


class ListNode:
    """Класс для узла связанного списка"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


def merge_two_lists(list1, list2):
    """
    Объединяет два отсортированных связанных списка в один отсортированный список.
    
    Args:
        list1 (ListNode): Голова первого отсортированного списка
        list2 (ListNode): Голова второго отсортированного списка
    
    Returns:
        ListNode: Голова объединенного отсортированного списка
    
    Примеры алгоритмов решения:
    1. Итеративный подход с dummy node
    2. Рекурсивный подход
    3. In-place слияние
    """

    result = ListNode()
    result_head = result
    
    while list1 and list2:
        if list1.val < list2.val:
            result.next = list1
            list1 = list1.next
        else:
            result.next = list2
            list2 = list2.next
        result = result.next
    
    result.next = list1 if list1 else list2
    return result_head.next



def create_linked_list(values):
    """Вспомогательная функция для создания связанного списка из массива"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_array(head):
    """Вспомогательная функция для преобразования связанного списка в массив"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def test_merge_two_lists():
    """Тесты для функции merge_two_lists"""
    
    print("Запуск тестов...")
    
    # Тест 1: Обычный случай
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = merge_two_lists(list1, list2)
    expected = [1, 1, 2, 3, 4, 4]
    actual = linked_list_to_array(result)
    print(f"Тест 1: {actual} == {expected} -> {'✅' if actual == expected else '❌'}")
    
    # Тест 2: Один пустой список
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = merge_two_lists(list1, list2)
    expected = [0]
    actual = linked_list_to_array(result)
    print(f"Тест 2: {actual} == {expected} -> {'✅' if actual == expected else '❌'}")
    
    # Тест 3: Оба пустых списка
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = merge_two_lists(list1, list2)
    expected = []
    actual = linked_list_to_array(result)
    print(f"Тест 3: {actual} == {expected} -> {'✅' if actual == expected else '❌'}")
    
    # Тест 4: Списки разной длины
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6, 7, 8])
    result = merge_two_lists(list1, list2)
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    actual = linked_list_to_array(result)
    print(f"Тест 4: {actual} == {expected} -> {'✅' if actual == expected else '❌'}")
    
    # Тест 5: Один элемент в каждом списке
    list1 = create_linked_list([1])
    list2 = create_linked_list([2])
    result = merge_two_lists(list1, list2)
    expected = [1, 2]
    actual = linked_list_to_array(result)
    print(f"Тест 5: {actual} == {expected} -> {'✅' if actual == expected else '❌'}")
    
    # Тест 6: Отрицательные числа
    list1 = create_linked_list([-10, -1, 0])
    list2 = create_linked_list([-5, 2, 3])
    result = merge_two_lists(list1, list2)
    expected = [-10, -5, -1, 0, 2, 3]
    actual = linked_list_to_array(result)
    print(f"Тест 6: {actual} == {expected} -> {'✅' if actual == expected else '❌'}")


if __name__ == "__main__":
    test_merge_two_lists()
    
    print("\n" + "="*50)
    print("ПОДСКАЗКИ ДЛЯ РЕШЕНИЯ:")
    print("="*50)
    print("1. Итеративный подход:")
    print("   - Создай dummy node для упрощения")
    print("   - Используй два указателя для обхода списков")
    print("   - Сравнивай значения и присоединяй меньший узел")
    print("   - Не забудь присоединить оставшиеся узлы")
    print()
    print("2. Рекурсивный подход:")
    print("   - Базовый случай: если один из списков пуст")
    print("   - Сравни головы списков")
    print("   - Рекурсивно вызови функцию для остальной части")
    print()
    print("3. Временная сложность: O(m + n)")
    print("4. Пространственная сложность: O(1) для итеративного, O(m + n) для рекурсивного")