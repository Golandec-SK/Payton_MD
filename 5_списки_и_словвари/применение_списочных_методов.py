# Рекорды
# Демонстрирует списочные методы
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
    4 - Сортировать список
    """
    )
    choice = int(input("Ваш выбор: "))
    print()
    # выход
    if choice == 0:
        print("До свидание.")
    # вывод лучштх результатов на экран
    elif choice == 1:
        print("Рекорды")
        for score in scores:
            print(score)
    # добавление рекорда
    elif choice == 2:
        score = int(input("Впишите свой рекорд: "))
        # Метод append() в Python добавляет в конец списка элемент,
        # переданный ему в качестве аргумента.
        scores.append(score)
    elif choice == 3:
        score = int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(f"Результат {score} не содержиться в списке рекордов.")
    # сортировка рекордов
    elif  choice == 4:
        scores.sort(reverse=True)
    # непонятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта", choice)
    
input("\nНажмите Enter, чтобы выйти.\n")