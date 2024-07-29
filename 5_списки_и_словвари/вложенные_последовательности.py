# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None

while choice != 0:
    print(
    """
            Рекорды
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    3 - Удалить рекорд
    """
    )
    choice = int(input("Ваш выбор: "))
    print()
    # выход
    if choice == 0:
        print("До свидание.")
    # вывод лучштх результатов на экран
    elif choice == 1:
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    # добавление рекорда как вложенного кортежа
    elif choice == 2:
        name = input("Впиштите имя игрока: ")
        score = int(input("Впишите свой рекорд: "))
        entry = (score, name)
        # Метод append() в Python добавляет в конец списка элемент,
        # переданный ему в качестве аргумента.
        scores.append(entry)
        # сортировка рекордов
        scores.sort(reverse=True)
        scores = scores[:5] # в списке остаеться только 5 рекордов
    elif choice == 3:
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
        entry = int(input("Какой из рекордов удалить?: "))
        if entry in scores:
            scores.remove(entry)
        else:
            print(f"Результат {entry} не содержиться в списке рекордов.")
    else:
        print("Извините, в меню нет пункта", choice)
    
input("\nНажмите Enter, чтобы выйти.\n")