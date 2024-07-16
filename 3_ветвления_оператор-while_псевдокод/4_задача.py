import random

low = 1 
high = 100 
tries = 0

while True:
    computer = random.randint(low,high)
    guess = int(input(f'{computer} больше(3), меньше(2) или я угадал(1): '))
    if guess == 1:
        print('\nВам удалось угадать число!')
        print(f'Вы затратили на отгадывание {tries} попыток(и)!')
        break
    elif guess == 2:
        high = computer - 1
        print('Меньше')
    else:
        low = computer + 1
        print('Больше')
    tries += 1

input('\n\nНажмите Enter для выхода\n')