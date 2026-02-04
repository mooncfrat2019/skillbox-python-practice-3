def summa_n(N):
    total = 0
    for number in range(1, N + 1):
        total += number
    return total

N = int(input("Введите число: "))
result = summa_n(N)
print(f"Сумма чисел от 1 до {N} равна {result}")