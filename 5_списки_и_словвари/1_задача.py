import random
roster = ['Конь', 'Жук', 'Собака', 'Эльф']
"""
Метод random.shuffle() используется для перемешивания данных
списка или другой последовательности. Метод shuffle() смешивает
элементы списка на месте.
"""
random.shuffle(roster)
for i in roster:
    print(i)