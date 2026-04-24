"""
Задача 2. Параметры помещения.
Расчёт площади пола, стен, объёма и стоимости покраски.
Автор: Дьячков Иван Юрьевич
"""

# Размеры помещения (в метрах)
length = 6.40
width = 4.20
height = 2.80

# Стоимость покраски (руб/м²)
paint_price_per_m2 = 125.0
def main() -> None:
    """Рассчитывает и выводит параметры помещения."""
    # Расчёты
    floor_area = length * width
    wall_area = 2 * (length + width) * height
    volume = length * width * height
    paint_cost = wall_area * paint_price_per_m2

    # Вывод с округлением до 2 знаков
    print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
    print(f"Длина: {length:.2f} м")
    print(f"Ширина: {width:.2f} м")
    print(f"Высота: {height:.2f} м")
    print("-" * 36)
    print(f"Площадь пола: {floor_area:.2f} м²")
    print(f"Площадь стен: {wall_area:.2f} м²")
    print(f"Объём помещения: {volume:.2f} м³")
    print(f"Стоимость покраски: {paint_cost:.2f} руб")

if __name__ == "__main__":
    main()