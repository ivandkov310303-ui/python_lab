"""
Задача 10. Система учёта склада.
Контроль критических остатков, выдача материалов.
Автор: Дьячков Иван Юрьевич
"""

# Данные склада
warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

# Данные для выдачи материала
issue_material_name = "Цемент"
issue_quantity = 25
def print_table(data: dict) -> None:
    """Печатает таблицу материалов с основными показателями."""
    print("\n" + "=" * 75)
    print(f"{'Материал':<15} | {'Кол-во':>6} | {'Цена':>9} | {'Мин.':>4} | {'Стоимость':>12} | Статус")
    print("-" * 75)

    for material, info in data.items():
        quantity = info["quantity"]
        price = info["price"]
        min_quantity = info["min_quantity"]
        total_value = quantity * price
        status = "КРИТИЧНО!" if quantity < min_quantity else "норма"

        print(f"{material:<15} | {quantity:>6} | {price:>9.2f} | "
              f"{min_quantity:>4} | {total_value:>12.2f} | {status}")

def main() -> None:
    """Печатает сводку по складу и моделирует выдачу материала."""
    print("СИСТЕМА УЧЁТА СКЛАДА")
    print_table(warehouse)

    # Общая стоимость
    total_cost = sum(info["quantity"] * info["price"] for info in warehouse.values())
    print(f"\nОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")

    # Самый дорогой материал
    most_expensive = max(
        warehouse.items(),
        key=lambda item: item[1]["quantity"] * item[1]["price"]
    )
    most_expensive_name = most_expensive[0]
    most_expensive_value = most_expensive[1]["quantity"] * most_expensive[1]["price"]
    print(f"Самый дорогой материал: {most_expensive_name} ({most_expensive_value:.2f} руб)")

    # Критические остатки
    critical_items = [
        (material, info)
        for material, info in warehouse.items()
        if info["quantity"] < info["min_quantity"]
    ]
    print(f"\nКРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
    for material, info in critical_items:
        print(f"  - {material}: {info['quantity']} < {info['min_quantity']}")

    # Выдача материала
    print("\n" + "=" * 50)
    print("ВЫДАЧА МАТЕРИАЛА")
    print("=" * 50)

    if issue_material_name not in warehouse:
        print(f"Ошибка: материал '{issue_material_name}' не найден.")
        return

    current_quantity = warehouse[issue_material_name]["quantity"]
    if issue_quantity > current_quantity:
        print(f"Нельзя выдать {issue_quantity} ед. '{issue_material_name}': "
              f"на складе только {current_quantity} ед.")
        return

    # Выполняем выдачу
    warehouse[issue_material_name]["quantity"] -= issue_quantity
    new_quantity = warehouse[issue_material_name]["quantity"]

    print(f"Выдано: {issue_quantity} ед. '{issue_material_name}'")
    print(f"Остаток: {current_quantity} → {new_quantity}")

    # Обновлённая таблица
    print("\nОБНОВЛЁННАЯ ТАБЛИЦА ПОСЛЕ ВЫДАЧИ:")
    print_table(warehouse)

if __name__ == "__main__":
    main()