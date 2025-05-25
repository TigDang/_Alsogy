"""
Задача: Палиндром в односвязном списке

Дан head односвязного списка. Верните true, если список является палиндромом, 
иначе верните false.

Ограничения:
- Количество узлов в списке в диапазоне [1, 10^5]
- 0 <= Node.val <= 9

Follow up: Можете ли вы решить за O(n) времени и O(1) памяти?

Примеры:
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""


class ListNode:
    """Определение односвязного списка"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


def isPalindrome(head: ListNode) -> bool:
    """
    Ваше решение здесь.
    
    Args:
        head: ListNode - голова односвязного списка
    
    Returns:
        bool - True если список палиндром, False иначе
    """
    if not head or not head.next:
        return True
    
    # Этап 1: Найти середину списка (заяц и черепаха)
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # slow теперь указывает на конец первой половины
    
    # Этап 2: Развернуть вторую половину
    def reverse_list(node):
        prev = None
        current = node
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
    second_half = reverse_list(slow.next)
    
    # Этап 3: Сравнить первую и вторую половины
    first_half = head
    while second_half:  # Вторая половина может быть короче
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

# Вспомогательные функции для тестирования
def create_linked_list(values):
    """Создает односвязный список из массива значений"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def test_isPalindrome():
    """Тесты для проверки решения"""
    
    # Тест 1: Простой палиндром
    head1 = create_linked_list([1, 2, 2, 1])
    assert isPalindrome(head1) == True, "Тест 1 провален: [1,2,2,1] должен быть палиндромом"
    
    # Тест 2: Не палиндром
    head2 = create_linked_list([1, 2])
    assert isPalindrome(head2) == False, "Тест 2 провален: [1,2] не должен быть палиндромом"
    
    # Тест 3: Одиночный элемент
    head3 = create_linked_list([1])
    assert isPalindrome(head3) == True, "Тест 3 провален: [1] должен быть палиндромом"
    
    # Тест 4: Нечетное количество элементов - палиндром
    head4 = create_linked_list([1, 2, 3, 2, 1])
    assert isPalindrome(head4) == True, "Тест 4 провален: [1,2,3,2,1] должен быть палиндромом"
    
    # Тест 5: Нечетное количество элементов - не палиндром
    head5 = create_linked_list([1, 2, 3])
    assert isPalindrome(head5) == False, "Тест 5 провален: [1,2,3] не должен быть палиндромом"
    
    # Тест 6: Все одинаковые элементы
    head6 = create_linked_list([0, 0, 0])
    assert isPalindrome(head6) == True, "Тест 6 провален: [0,0,0] должен быть палиндромом"
    
    # Тест 7: Длинный палиндром
    head7 = create_linked_list([9, 1, 2, 9, 9, 2, 1, 9])
    assert isPalindrome(head7) == True, "Тест 7 провален: [9,1,2,9,9,2,1,9] должен быть палиндромом"
    
    # Тест 8: Длинный не палиндром
    head8 = create_linked_list([1, 0, 3, 4, 0])
    assert isPalindrome(head8) == False, "Тест 8 провален: [1,0,3,4,0] не должен быть палиндромом"
    
    print("✅ Все тесты пройдены!")


if __name__ == "__main__":
    print("🔍 Тестирование решения...")
    print("📝 Примеры списков для отладки:")
    
    # Демонстрация примеров
    example1 = create_linked_list([1, 2, 2, 1])
    print(f"Пример 1: {example1}")
    
    example2 = create_linked_list([1, 2])
    print(f"Пример 2: {example2}")
    
    print("\n🧪 Запуск тестов...")
    try:
        test_isPalindrome()
    except Exception as e:
        print(f"❌ Тесты провалены: {e}")
    
    print("\n💡 Подсказки для решения:")
    print("1. Простое решение: скопировать значения в массив и проверить палиндром")
    print("2. Оптимальное решение O(1) памяти:")
    print("   - Найти середину списка (быстрый/медленный указатель)")
    print("   - Развернуть вторую половину")
    print("   - Сравнить первую и вторую половины")
    print("   - Восстановить исходный список")