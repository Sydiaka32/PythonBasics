import math


def get_input():
    return int(input("Введіть додатне число: "))


def validate_input(number):
    if number < 0:
        raise ValueError("Введене число повинно бути додатнім.")


def calculate_square_root(number):
    return math.sqrt(number)


def display_result(number, result):
    print(f"Квадратний корінь від числа {number} дорівнює {result}")


def main():
    try:
        user_input = get_input()
        validate_input(user_input)

        result = round(calculate_square_root(user_input), 3)
        display_result(user_input, result)

    except ValueError as e:
        print(e)


# Викликаємо функцію main для запуску основної логіки програми
if __name__ == "__main__":
    main()