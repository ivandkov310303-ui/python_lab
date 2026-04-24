"""
Задача 5. Калькулятор скидки.
Расчёт стоимости покупки с прогрессивной системой скидок.
Автор: Дьячков Иван Юрьевич
"""

# Данные покупки
price = 850.0      # цена за единицу (руб)
quantity = 7       # количество
def get_discount_rate(total_cost: float) -> float:
    """
    Возвращает процент скидки в виде десятичной дроби.
    < 1000 руб → 0%
    1000-5000 руб → 5%
    > 5000 руб → 10%
    """
    if total_cost < 1000:
        return 0.00
    if total_cost <= 5000:
        return 0.05
    return 0.10

def main() -> None:
    """Рассчитывает и выводит стоимость покупки со скидкой."""
    total_cost = price * quantity
    discount_rate = get_discount_rate(total_cost)
    discount_value = total_cost * discount_rate
    final_cost = total_cost - discount_value

    print("=== КАЛЬКУЛЯТОР СКИДКИ ===")
    print(f"Цена за единицу: {price:.2f} руб")
    print(f"Количество: {quantity}")
    print(f"Стоимость без скидки: {total_cost:.2f} руб")
    print(f"Скидка: {discount_rate * 100:.0f}%")
    print(f"Размер скидки: {discount_value:.2f} руб")
    print(f"Итоговая стоимость: {final_cost:.2f} руб")

if __name__ == "__main__":
    main()