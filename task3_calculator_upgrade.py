def sum_of_digits(number):
    total = 0
    num = abs(number)

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total


def max_digit(number):
    num = abs(number)

    if num == 0:
        return 0

    max_digit_value = 0

    while num > 0:
        digit = num % 10
        if digit > max_digit_value:
            max_digit_value = digit
        num //= 10

    return max_digit_value


def min_digit(number):
    num = abs(number)

    if num == 0:
        return 0

    min_digit_value = 9

    while num > 0:
        digit = num % 10
        if digit < min_digit_value:
            min_digit_value = digit
        num //= 10

    return min_digit_value


while True:
    number = int(input("Введите число: "))

    print("\nВведите номер действия:")
    print("1 - сумма цифр")
    print("2 - максимальная цифра")
    print("3 - минимальная цифра")
    print("0 - выход")

    action = int(input(": "))

    if action == 0:
        print("Выход из калькулятора.")
        break
    elif action == 1:
        result = sum_of_digits(number)
        print(f"Сумма цифр: {result}")
    elif action == 2:
        result = max_digit(number)
        print(f"Максимальная цифра: {result}")
    elif action == 3:
        result = min_digit(number)
        print(f"Минимальная цифра: {result}")
    else:
        print("Неверный номер действия. Попробуйте снова.")

    print()