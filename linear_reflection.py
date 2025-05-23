"""
    Описание
    Даны n точек на двумерной плоскости, найдите, существует ли такая прямая, параллельная оси y, которая симметрично отражает данные точки, другими словами, ответьте, существует ли такая прямая, что после отражения всех точек через данную прямую множество исходных точек совпадает с множеством отраженных.
    Обратите внимание, что могут существовать повторяющиеся точки.
"""

def has_reflection_symmetry(points):
    """
    Определяет, существует ли вертикальная прямая (параллельная оси y),
    которая симметрично отражает все данные точки.
    
    Args:
        points: список кортежей (x, y) - координаты точек
        
    Returns:
        bool: True, если существует ось симметрии, False иначе
    """
    
    if len(points) == 0:
        return True

    def get_reflection(line, points):
        reflection_points = []
        for point in points:
            if point[0] == line:
                reflection_points.append(point)
            else:
                reflection_points.append((2 * line - point[0], point[1]))
        return reflection_points
    
    sorted_by_x = sorted(points, key=lambda x: x[0])

    if len(points)%2 == 0: # если четное количество точек
        symmetry_candidate = (sorted_by_x[len(points)//2][0] + sorted_by_x[len(points)//2 - 1][0])/2
    else: # если нечетное количество точек
        symmetry_candidate = sorted_by_x[len(points)//2][0]
    
    symmetry_set = set(get_reflection(symmetry_candidate, points))
    if symmetry_set == set(points):
        return True
    else:
        return False



def test_has_reflection_symmetry():
    """Тесты для проверки решения"""
    
    # Тест 1: Простая симметрия относительно x = 0
    points1 = [(-1, 0), (1, 0), (-2, 1), (2, 1)]
    assert has_reflection_symmetry(points1) == True, "Тест 1 не прошел: должна быть симметрия относительно x = 0"
    
    # Тест 2: Симметрия относительно x = 1
    points2 = [(0, 0), (2, 0), (0, 1), (2, 1)]
    assert has_reflection_symmetry(points2) == True, "Тест 2 не прошел: должна быть симметрия относительно x = 1"
    
    # Тест 3: Нет симметрии
    points3 = [(0, 0), (1, 0), (2, 1)]
    assert has_reflection_symmetry(points3) == False, "Тест 3 не прошел: не должно быть симметрии"
    
    # Тест 4: Одна точка (всегда симметрична)
    points4 = [(5, 3)]
    assert has_reflection_symmetry(points4) == True, "Тест 4 не прошел: одна точка всегда симметрична"
    
    # Тест 5: Две точки с одинаковой y-координатой
    points5 = [(1, 2), (3, 2)]
    assert has_reflection_symmetry(points5) == True, "Тест 5 не прошел: две точки должны быть симметричны"
    
    # Тест 6: Две точки с разными y-координатами
    points6 = [(1, 2), (3, 4)]
    assert has_reflection_symmetry(points6) == False, "Тест 6 не прошел: две точки с разными y не могут быть симметричны"
    
    # Тест 7: Дублирующиеся точки
    points7 = [(1, 1), (1, 1), (3, 1), (3, 1)]
    assert has_reflection_symmetry(points7) == True, "Тест 7 не прошел: дублирующиеся точки должны быть симметричны"
    
    # Тест 8: Точка на оси симметрии
    points8 = [(0, 0), (2, 0), (2, 1), (0, 1), (1, 2)]
    assert has_reflection_symmetry(points8) == True, "Тест 8 не прошел: точка на оси симметрии x = 1"
    
    # Тест 9: Пустой список
    points9 = []
    assert has_reflection_symmetry(points9) == True, "Тест 9 не прошел: пустое множество симметрично"
    
    # Тест 10: Сложный случай с несколькими повторениями
    points10 = [(-2, 1), (-1, 0), (0, 1), (1, 0), (2, 1), (0, 1)]
    assert has_reflection_symmetry(points10) == True, "Тест 10 не прошел: симметрия относительно x = 0"
    
    # Тест 11: Несимметричный сложный случай
    points11 = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 2)]
    assert has_reflection_symmetry(points11) == False, "Тест 11 не прошел: нет симметрии"
    
    # Тест 12: Дробные координаты
    points12 = [(0.5, 1), (1.5, 1), (0.5, 2), (1.5, 2)]
    assert has_reflection_symmetry(points12) == True, "Тест 12 не прошел: симметрия относительно x = 1"
    
    print("Все тесты пройдены! ✅")


if __name__ == "__main__":
    # Запуск тестов
    test_has_reflection_symmetry()
    
    # Пример использования
    print("\nПример использования:")
    example_points = [(-1, 0), (1, 0), (-2, 1), (2, 1)]
    result = has_reflection_symmetry(example_points)
    print(f"Точки {example_points} {'имеют' if result else 'не имеют'} ось симметрии")
    
    # КОНТРПРИМЕР - демонстрация ошибки в алгоритме
    print("\n🚨 КОНТРПРИМЕР:")
    counter_example = [(0, 0), (2, 0), (3, 0), (5, 0)]  # Симметричны относительно x = 2.5
    print(f"Точки: {counter_example}")
    print("Эти точки симметричны относительно x = 2.5:")
    print("  (0,0) <-> (5,0), (2,0) <-> (3,0)")
    
    # Ваш алгоритм выберет ось x = 2.5 (между средними точками)
    sorted_points = sorted(counter_example, key=lambda x: x[0])
    print(f"Отсортированные: {sorted_points}")
    chosen_axis = (sorted_points[len(counter_example)//2][0] + sorted_points[len(counter_example)//2 - 1][0])/2
    print(f"Ваш алгоритм выбирает ось: x = {chosen_axis}")
    
    # И это ПРАВИЛЬНО!
    result_counter = has_reflection_symmetry(counter_example)
    print(f"Ваш алгоритм говорит: {result_counter}")
    
    if result_counter:
        print("✅ Это правильно! Возможно ваш алгоритм корректен!")
    else:
        print("❌ Ошибка в алгоритме!")
    
    print(f"\n💡 Хм... может быть ваш подход действительно работает?")
    print("Теоретически, если точки симметричны, то:")
    print("- При четном количестве: ось между двумя средними")  
    print("- При нечетном количестве: ось через медиану")
