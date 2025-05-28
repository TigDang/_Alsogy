"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""

def generateParenthesis(n):
    """
    Генерирует все возможные корректные комбинации n пар скобок.
    
    Args:
        n (int): Количество пар скобок
    
    Returns:
        List[str]: Список всех корректных комбинаций скобок
    """
    # TODO: Реализуйте решение здесь
    
    # ПОДСКАЗКА: Рекурсивное решение с backtracking
    # 
    # Идея: строим строку посимвольно, отслеживая:
    # - open_count: сколько открывающих скобок уже добавили
    # - close_count: сколько закрывающих скобок уже добавили
    #
    # Правила:
    # 1. Можем добавить '(' если open_count < n
    # 2. Можем добавить ')' если close_count < open_count
    # 3. Базовый случай: open_count == close_count == n
    #
    # Пример работы для n=2:
    # ""
    # ├─ "(" (open=1, close=0)
    # │  ├─ "((" (open=2, close=0)
    # │  │  └─ "(()" (open=2, close=1)
    # │  │     └─ "(())" ✓ (open=2, close=2)
    # │  └─ "()( (open=1, close=1)
    # │     └─ "()()" ✓ (open=2, close=2)


    def backtrack(current_string, open_count, close_count):
        if open_count == close_count == n:
            result.append(current_string)
            return
        
        if open_count < n:
            backtrack(current_string + "(", open_count + 1, close_count)
        
        if close_count < open_count:
            backtrack(current_string + ")", open_count, close_count + 1)
    
    result = []
    backtrack("", 0, 0)
    return result


def test_generateParenthesis():
    """Тесты для функции generateParenthesis"""
    
    # Тест 1: n = 1
    result1 = generateParenthesis(1)
    expected1 = ["()"]
    assert sorted(result1) == sorted(expected1), f"Test 1 failed: expected {expected1}, got {result1}"
    print("✅ Тест 1 (n=1) пройден")
    
    # Тест 2: n = 2
    result2 = generateParenthesis(2)
    expected2 = ["(())", "()()"]
    assert sorted(result2) == sorted(expected2), f"Test 2 failed: expected {expected2}, got {result2}"
    print("✅ Тест 2 (n=2) пройден")
    
    # Тест 3: n = 3 (основной пример)
    result3 = generateParenthesis(3)
    expected3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(result3) == sorted(expected3), f"Test 3 failed: expected {expected3}, got {result3}"
    print("✅ Тест 3 (n=3) пройден")
    
    # Тест 4: n = 0 (краевой случай)
    result4 = generateParenthesis(0)
    expected4 = [""]
    assert sorted(result4) == sorted(expected4), f"Test 4 failed: expected {expected4}, got {result4}"
    print("✅ Тест 4 (n=0) пройден")
    
    # Тест 5: n = 4 (дополнительный тест)
    result5 = generateParenthesis(4)
    # Проверяем что количество результатов соответствует числу Каталана: C_n = C_4 = 14
    expected_count = 14
    assert len(result5) == expected_count, f"Test 5 failed: expected {expected_count} combinations, got {len(result5)}"
    print("✅ Тест 5 (n=4, проверка количества) пройден")
    
    print("🎉 Все тесты пройдены!")


if __name__ == "__main__":
    print("=" * 50)
    print("ЗАДАЧА: Генерация корректных скобочных последовательностей")
    print("=" * 50)
    print()
    
    print("📝 Описание:")
    print("Нужно сгенерировать все возможные корректные комбинации n пар скобок")
    print()
    
    print("💡 Подсказки для решения:")
    print("1. Используйте рекурсию с отслеживанием количества открытых/закрытых скобок")
    print("2. Открывающую скобку можно добавить, если их меньше n")
    print("3. Закрывающую скобку можно добавить, если открытых больше чем закрытых")
    print("4. Базовый случай: когда добавили n открытых и n закрытых скобок")
    print()
    
    print("🧪 Запуск тестов:")
    try:
        test_generateParenthesis()
    except Exception as e:
        print(f"❌ Тесты не пройдены: {e}")
        print()
        print("Реализуйте функцию generateParenthesis и запустите тесты снова!")