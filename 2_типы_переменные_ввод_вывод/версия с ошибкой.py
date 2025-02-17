"""
Функция int() - конвертирует другой тип данных в целое число.
Функция float() - конвертация данных из других типов в тип числа с плавающей точкой.
Функция str() - конвертирует данные в строку из любого другого типа.
"""

# "Рантье" версия с ошибкой
# Демонстрирует логическую ошибку
print(
    """
                                    Рантье
    
    Программа подсчитывает выши ежемесячные доходы. Эту статистику нужно знать,
    чтобы у вас не закончились деньги и вам не пришлось искать работу.
    Введите сумму расходов по всем статьям, перечислинным ниже.
    вы богаты - так не мелочитесь.
    """
    )
car = int(input("\nТехническое обслуживание вашей машины: "))
rent = int(input("Съем квартиры в Питере: "))
get = int(input("Аренда самолета: "))
gifts = int(input("Подарки: "))
food = int(input("Обед и ужины в ресторанах: "))
staff = int(input("Жалование прислуги (дворецкий, повар, водитель, секритарь): "))
guru = int(input("Плата личному психиатору: "))
games = int(input("Компьютерные игры: "))

total = car + rent + get + gifts + food + staff + guru + games
print("\nОбщая сумма", total)

input("\nНажмите Enter, чтобы выйти.\n")