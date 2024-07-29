specifications = {
    "здоровье" : 0,
    "сила" : 0,
    "ловкость" : 0,
    "мудрость" : 0
}
menu_character = (
     """
            Меню
        0 - Выход.
        1 - Ваши характеристики
        2 - Распределить очки.
        3 - Обнулить результаты.
     """
 )

choice = None
points = 30
skil = None

while choice != 0:
    print(menu_character)
    choice = int(input("Ваш выбор: "))
    print()
    if choice == 0:
        print("До свидание.")
    elif choice == 1:
        """
        Метод items() в Python возвращает список кортежей с парами всех ключей и значений словаря.
        """
        for key, value in specifications.items():
            print(f'{key} -- {value}')
        input('\nНажмите Enter, чтобы выйти из меню.\n')
    elif choice == 2:
        while skil != "":
            print("\nМеню распределение очков.\n")
            for key, value in specifications.items():
                print(f'{key} -- {value}')
            skil = input("\nКакой характеристики Вы хотите добавить очков? ")
            if skil in specifications:
                point = int(input('Сколько очков вы хотите потратить?: '))
                specifications[skil] = point
                print(f'Вы добавили {point} очков в навак: {skil}')
                points -= point
                print(f'У вас осталось {points} очка(ов)')
            else:
                print('Некорректный ввод! Попробуйте еще раз.')
    elif choice == 3:
        specifications = {k: v * 0 for k, v in specifications.items()}
        print('Ваши навыки сброшены.')
    else:
        print('Извините, в меню нет пнкта', choice)
        
input("\nНажмите Enter, чтобы выйти.\n")
