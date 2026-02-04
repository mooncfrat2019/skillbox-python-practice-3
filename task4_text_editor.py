def count_letters(text, digit_to_search, letter_to_search):
    digit_count = 0
    letter_count = 0

    # Подсчет цифр
    for char in text:
        if char == digit_to_search:
            digit_count += 1

    letter_to_search_lower = letter_to_search.lower()
    for char in text:
        if char.lower() == letter_to_search_lower:
            letter_count += 1

    return digit_count, letter_count


text = input("Введите текст: ")
digit_to_search = input("Какую цифру ищем? ")
letter_to_search = input("Какую букву ищем? ")

digit_count, letter_count = count_letters(text, digit_to_search, letter_to_search)

print(f"Количество цифр {digit_to_search}: {digit_count}")
print(f"Количество букв {letter_to_search}: {letter_count}")