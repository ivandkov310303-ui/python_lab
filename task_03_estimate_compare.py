"""
Задача 3. Конвертер температур.
Перевод из Цельсия в Фаренгейты и определение состояния воды.
Автор: Дьячков Иван Юрьевич
"""

# Температура в градусах Цельсия
temperature_c = 36.0
def get_water_state(temp_c: float) -> str:
    """Определяет состояние воды по температуре в °C."""
    if temp_c <= 0:
        return "Лёд"
    elif temp_c < 100:
        return "Жидкость"
    else:
        return "Пар"

def main() -> None:
    """Переводит температуру в °F и выводит состояние воды."""
    temperature_f = temperature_c * 9 / 5 + 32
    water_state = get_water_state(temperature_c)

    print("=== КОНВЕРТЕР ТЕМПЕРАТУР ===")
    print(f"Температура: {temperature_c:.2f} °C")
    print(f"Температура: {temperature_f:.2f} °F")
    print(f"Состояние воды: {water_state}")

if __name__ == "__main__":
    main()