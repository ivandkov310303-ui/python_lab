"""
Задача 9. Очистка адресов.
Приведение адресов к стандартному формату.
Автор: Дьячков Иван Юрьевич
"""

import re

# Тестовые адреса
addresses = [
    "  г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100  "
]
def clean_address(address: str) -> str:
    """Приводит адрес к стандартному виду."""
    # Удаляем лишние пробелы по краям строки
    result = address.strip()
    # Убираем лишние пробелы вокруг запятых и ставим ровно один пробел после запятой
    result = re.sub(r"\s*,\s*", ", ", result)
    # Ставим пробел после сокращений, если его нет
    result = re.sub(r"г\.([А-Я])", r"г. \1", result)
    result = re.sub(r"ул\.([А-Я])", r"ул. \1", result)
    result = re.sub(r"д\.([0-9])", r"д. \1", result)
    # Убираем повторные пробелы
    result = re.sub(r"\s+", " ", result)
    return result.strip()

def main() -> None:
    """Выводит сравнение исходных и очищенных адресов."""
    print("=== СРАВНЕНИЕ АДРЕСОВ ===")
    for index, address in enumerate(addresses, start=1):
        cleaned = clean_address(address)
        print(f"#{index}")
        print(f"ДО: '{address}'")
        print(f"ПОСЛЕ: '{cleaned}'")
        print()

if __name__ == "__main__":
    main()