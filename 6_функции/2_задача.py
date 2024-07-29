# Отгодай число
# Компьютер выбирает случайное число в диапозоне от 1 до 100
# Игрок пытаеться отгодать число, и компьютер говорит, 
# предложение больше/меньше, чем загадонное число,
# или попало в точку

import random

def ask_number(question, low, high, step = 1):
    """Просит ввести число из диапозона."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

print("Добро пожалловать в игру 'Отгодай число'!")
print("\nЯ загадал натуральное число в диапазоне от 1 до 100.")
print("Отгодайти число за минимальное количество попыток")
# начальные значения
theNumber = random.randint(1, 100)
low = 1
high = 100
guess = ask_number("Ваш вариант: ", low, high) 
attempt = 1

while guess != theNumber:
    if guess > theNumber:
        print("Меньше")
    else:
        print("Бльше")
    guess = ask_number("Ваш вариант: ", low, high)
    attempt += 1
print("Поздравляю, вы отгодали чило.")
print('Вы затратилти', attempt, "попыток.")

input("\nНажмите Enter, чтобы выйти.")