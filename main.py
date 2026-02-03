def summa_n():
    N = int(input("Введите число: "))

    total = N * (N + 1) // 2

    print(f"Сумма чисел от 1 до {N} равна {total}")
    print()

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def test():
    number = int(input("Введите число: "))

    if number >= 0:
        positive()
    else:
        negative()

    print()


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

def calculator():
    while True:
        try:
            number = int(input("Введите число: "))

            print("\nВведите номер действия:")
            print("1 - сумма цифр")
            print("2 - максимальная цифра")
            print("3 - минимальная цифра")
            print("0 - выход")

            action = int(input(": "))

            if action == 0:
                print("Выход из калькулятора.")
                print()
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

        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")
            print()


def count_letters():
    text = input("Введите текст: ")
    digit_to_search = input("Какую цифру ищем? ")
    letter_to_search = input("Какую букву ищем? ")

    if len(digit_to_search) != 1 or not digit_to_search.isdigit():
        print("Ошибка! Введите одну цифру.")
        print()
        return

    if len(letter_to_search) != 1 or not letter_to_search.isalpha():
        print("Ошибка! Введите одну букву.")
        print()
        return

    digit_count = 0
    for char in text:
        if char == digit_to_search:
            digit_count += 1

    letter_count = 0
    for char in text:
        if char.lower() == letter_to_search.lower():
            letter_count += 1

    print(f"Количество цифр {digit_to_search}: {digit_count}")
    print(f"Количество букв {letter_to_search}: {letter_count}")
    print()


import random

def rock_paper_scissors():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Правила: камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.")
    print("Введите ваш выбор: 'камень', 'ножницы' или 'бумага'.")
    print("Для выхода введите 'выход'.")
    print()

    moves = ['камень', 'ножницы', 'бумага']

    while True:
        user_move = input("Ваш ход: ").lower()

        if user_move == 'выход':
            print("Выход из игры 'Камень, ножницы, бумага'.")
            print()
            break

        if user_move not in moves:
            print("Неверный ввод. Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")
            continue


        computer_move = random.choice(moves)
        print(f"Компьютер выбрал: {computer_move}")

        if user_move == computer_move:
            print("Ничья!")
        elif (user_move == 'камень' and computer_move == 'ножницы') or \
                (user_move == 'ножницы' and computer_move == 'бумага') or \
                (user_move == 'бумага' and computer_move == 'камень'):
            print("Вы победили!")
        else:
            print("Вы проиграли!")

        print()

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Компьютер загадал число от 1 до 100. Попробуйте угадать!")
    print("Для выхода введите '0'.")
    print()

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = input("Введите ваше предположение (1-100): ")

            if user_guess == '0':
                print(f"Вы вышли из игры. Загаданное число было: {secret_number}")
                print()
                break

            guess = int(user_guess)

            if guess < 1 or guess > 100:
                print("Пожалуйста, введите число от 1 до 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
                print()
                break

        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")

    print()

def main_menu():
    """Главное меню игр"""
    while True:
        print("=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Игра 'Камень, ножницы, бумага'")
        print("2. Игра 'Угадай число'")
        print("0. Выход")

        choice = input("Выберите игру (введите номер): ")

        if choice == '1':
            print()
            rock_paper_scissors()
        elif choice == '2':
            print()
            guess_the_number()
        elif choice == '0':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите 0, 1 или 2.")
            print()


def main():
    print("=" * 50)
    print("ВЫПОЛНЕНИЕ ЗАДАЧ ПО ПРОГРАММИРОВАНИЮ")
    print("=" * 50)

    while True:
        print("\nВыберите задачу для выполнения:")
        print("1. Сумма чисел")
        print("2. Функция в функции")
        print("3. Апгрейд калькулятора")
        print("4. Текстовый редактор")
        print("5. Недоделка (игры)")
        print("0. Выход")

        task_choice = input("Введите номер задачи (0-5): ")

        if task_choice == '1':
            print("\n" + "=" * 30)
            print("Задача 1. Сумма чисел")
            print("=" * 30)
            summa_n()
        elif task_choice == '2':
            print("\n" + "=" * 30)
            print("Задача 2. Функция в функции")
            print("=" * 30)
            test()
        elif task_choice == '3':
            print("\n" + "=" * 30)
            print("Задача 3. Апгрейд калькулятора")
            print("=" * 30)
            calculator()
        elif task_choice == '4':
            print("\n" + "=" * 30)
            print("Задача 4. Текстовый редактор")
            print("=" * 30)
            count_letters()
        elif task_choice == '5':
            print("\n" + "=" * 30)
            print("Задача 5. Недоделка")
            print("=" * 30)
            main_menu()
        elif task_choice == '0':
            print("\nПрограмма завершена. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 0 до 5.")

if __name__ == "__main__":
    main()