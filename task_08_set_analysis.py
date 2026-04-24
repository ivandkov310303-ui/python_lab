"""
Задача 8. Анализ заказов.
Использование множеств для анализа материалов трёх подрядчиков.
Автор: Дьячков Иван Юрьевич
"""

# Списки материалов трёх подрядчиков
supplier1 = ["Кирпич", "Цемент", "Песок", "Бетон"]
supplier2 = ["Цемент", "Арматура", "Песок", "Доска"]
supplier3 = ["Кирпич", "Песок", "Гравий", "Цемент"]
def main() -> None:
    """Анализирует множества материалов подрядчиков."""
    # Преобразование в множества
    set1 = set(supplier1)
    set2 = set(supplier2)
    set3 = set(supplier3)

    print("=== АНАЛИЗ ЗАКАЗОВ ПОДРЯДЧИКОВ ===")
    print(f"Подрядчик 1: {supplier1}")
    print(f"Подрядчик 2: {supplier2}")
    print(f"Подрядчик 3: {supplier3}")

    # Все уникальные материалы
    all_unique = set1 | set2 | set3
    print(f"\n1. Все уникальные материалы: {sorted(all_unique)}")

    # Общие для всех
    common_all = set1 & set2 & set3
    print(f"2. Общие для всех трёх: {sorted(common_all)}")

    # Только у первого
    only_first = set1 - set2 - set3
    print(f"3. Только у первого подрядчика: {sorted(only_first)}")

    # Ровно у двух
    exactly_two = (set1 & set2) | (set1 & set3) | (set2 & set3) - common_all
    print(f"4. Ровно у двух подрядчиков: {sorted(exactly_two)}")

if __name__ == "__main__":
    main()