familys = {
    'Артем': 'отец - Генадий',
    'отец - Генадий': 'дед - Абдул',
    'Петр': 'отец - Эдуард',
    'Николай': 'отец - Игнат'
}
menu = ("""
            Родственники
        0 - Выход.
        1 - Кто твой родственник.
        2 - Добавить пару 'сын - отец'.
        3 - Изменить пару 'сын - отец'.
        4 - Родословное древо
        """)
choice = None

while choice != 0:
    print(menu)
    choice = int(input('Ваш выбор: '))
    if choice == 0:
        print('До свидане.')
    elif choice == 1:
        for key in familys.keys():
            print(key)
        name = input('\nВведите имя?: ')
        if name in familys:
            family = familys[name]
            print(f'\nРодственик {name} являеться: {family}')
    elif choice == 2:
        name = input('\nВведите новое имя: ')
        if name not in familys:
            family = input('Введите родственника: ')
            familys[name] = family
            print(f'\nВы добавили новую пару: {name} - {family}.')
        else:
            print('\nТакой термин уже есть!')
    elif choice == 3:
        print('Что вы хотите изменить?')
        print("""
              0 - Выйти в основное меню.
              1 - Изменить имя.
              2 - Изменить родственника.
              3 - Удалить пару 'сын - отец'.
              """)
        choice = int(input('Ваш выбор: '))
        if choice == 0:
            if choice == 0:
                print(menu)
                choice = int(input('Ваш выбор: '))
        elif choice == 1:
            print('\n\tИзменить имя.\n')
            for key in familys.keys():
                print(key)
            name = input('\nВедите имя которое вы хотите заменить: ')
            new_name = input('Введите новое имя: ')
            if name in familys:
                # Использоем метод pop(), который удаляет элемент из словаря и
                # возвращает его значение.
                familys[new_name] = familys.pop(name)
            else:
                print(f'Такого имени - {name} нет в словаре')
        elif choice == 2:
            name = input('\nУ какого имени вы хотите изменить родственника?: ')
            if name in familys:
                family = input('Введите родственника: ')
                familys[name] = family
                print(f'\nВы изменили родственника - {family} у {name}.')
            else:
                print('\nТакого имени пока нет!\
                    Попробуй добавить его в словарь')
        elif choice == 3:
            name = input('\nКакой термин вы хотите удалить?: ')
            if name in familys:
                del familys[name]
                print(f'Пара - {name}, удалена.')
            else:
                print('\nТакого имени нет! Попробуйте добавить его в словарь')
        else:
            print('Извините, в меню нет пнкта', choice)
    elif choice == 4:
        name = input('\nВведите имя?: ')
        if name in familys:
            father = familys[name]
            grandf = familys[father]
            print(f'Родословное древо состоит из:\
                Сын - {name}, отец - {father}, дед - {grandf}')
        else:
            print("Ошибка, такого человека нет в базе данных")
    else:
        print('Извините, в меню нет пнкта', choice)
input('\nНажмите Enter, чтобы выйти\n')