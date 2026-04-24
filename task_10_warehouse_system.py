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