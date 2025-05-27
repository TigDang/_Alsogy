"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 
"""


def is_subsequence(s: str, t: str) -> bool:
    """
    Проверяет, является ли строка s подпоследовательностью строки t.
    
    Args:
        s: строка-кандидат на подпоследовательность
        t: исходная строка
    
    Returns:
        True если s является подпоследовательностью t, иначе False
    """
    if len(s) == 0:
        return True
    
    s_symbol = 0
    for t_symbol in range(len(t)):
        if t[t_symbol] == s[s_symbol]:
            s_symbol += 1
            if s_symbol == len(s):
                return True
    return False




def test_is_subsequence():
    """Тесты для функции is_subsequence"""
    
    # Базовые случаи
    assert is_subsequence("ace", "abcde") == True, "ace должно быть подпоследовательностью abcde"
    assert is_subsequence("aec", "abcde") == False, "aec НЕ должно быть подпоследовательностью abcde"
    
    # Пустые строки
    assert is_subsequence("", "") == True, "Пустая строка является подпоследовательностью пустой строки"
    assert is_subsequence("", "abc") == True, "Пустая строка является подпоследовательностью любой строки"
    assert is_subsequence("abc", "") == False, "Непустая строка НЕ является подпоследовательностью пустой строки"
    
    # Идентичные строки
    assert is_subsequence("abc", "abc") == True, "Строка является подпоследовательностью себя"
    
    # Одинаковые символы
    assert is_subsequence("aaa", "aaabaaacaaa") == True, "Повторяющиеся символы"
    assert is_subsequence("abc", "aabbcc") == True, "Символы присутствуют в правильном порядке"
    
    # Крайние случаи
    assert is_subsequence("b", "abc") == True, "Один символ в середине"
    assert is_subsequence("c", "abc") == True, "Один символ в конце"
    assert is_subsequence("a", "abc") == True, "Один символ в начале"
    assert is_subsequence("d", "abc") == False, "Символ отсутствует"
    
    # Длинные строки
    assert is_subsequence("abc", "axbxcxdxexfx") == True, "Разреженная подпоследовательность"
    assert is_subsequence("xyz", "abcdefghijk") == False, "Символы отсутствуют"
    
    # Порядок имеет значение
    assert is_subsequence("bac", "abcde") == False, "Неправильный порядок символов"
    assert is_subsequence("cab", "abcde") == False, "Неправильный порядок символов"
    
    print("Все тесты пройдены! ✅")


if __name__ == "__main__":
    # Запуск тестов
    try:
        test_is_subsequence()
    except AssertionError as e:
        print(f"Тест не пройден: {e}")
    except Exception as e:
        print(f"Ошибка при выполнении: {e}")
    
    # Примеры для отладки
    print("\nПримеры:")
    print(f'is_subsequence("ace", "abcde") = {is_subsequence("ace", "abcde")}')
    print(f'is_subsequence("aec", "abcde") = {is_subsequence("aec", "abcde")}')

