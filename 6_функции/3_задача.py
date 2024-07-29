import random


def greeting():
    print('\tДобро пожаловать в игру "Отгодай число"')
    print('\nЯ загадал натуральное число из диапазона от 1 до 100')
    print('Посторайтесть отгодать его за минимальное число попыток.\n')


def ask_number(question):
    """Просит ввести число из диапозона."""
    response = None
    while response not in range(1, 100):
        response = int(input(question))
    return response


def guess():
    """Блок процесса угадывания"""
    tries = 1
    response = None
    while response != the_number:
        response = ask_number('Ваш вариант: ')
        if response > the_number:
            print('\nМеньше')
        else:
            print('\nБольше')
        tries += 1
    print('\nВам удалось угадать число! Это в самом деле', the_number)
    print(f'Вы затратили на отгадывание всего лишь {tries} попыток!\n')
    return response


# начальные значения/условие
the_number = random.randint(1, 100)


def main():
    greeting()
    while guess() != the_number:
        ask_number('Ваш вариант: ')
        guess()
    print('Игра окончена')


main()
input('\n\nНажмите Enter для выхода\n')