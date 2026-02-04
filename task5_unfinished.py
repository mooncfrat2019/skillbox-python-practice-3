import random


def rock_paper_scissors():
    moves = ['камень', 'ножницы', 'бумага']

    while True:
        user_move = input("Введите ваш выбор (камень/ножницы/бумага) или 'выход' для выхода: ").lower()

        if user_move == 'выход':
            print("Выход из игры.")
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


def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Компьютер загадал число от 1 до 100. Попробуйте угадать!")

    while True:
        try:
            user_guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if user_guess < secret_number:
                print("Загаданное число больше.")
            elif user_guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")


def main_menu():
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Игра 'Камень, ножницы, бумага'")
        print("2. Игра 'Угадай число'")
        print("0. Выход")

        choice = input("Выберите игру: ")

        if choice == '1':
            print("\n=== КАМЕНЬ, НОЖНИЦЫ, БУМАГА ===")
            rock_paper_scissors()
        elif choice == '2':
            print("\n=== УГАДАЙ ЧИСЛО ===")
            guess_the_number()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 0.")

main_menu()