# Резчик пицы
# Демонстрирует срезы строк
wod = "пицца"
print(
"""
  Памятка

  0   1   2   3   4   5
  +---+---+---+---+---+
  | п | и | ц | ц | а |
  +---+---+---+---+---+
 -5  -4  -3  -2  -1

"""
)
print("Введите начальный и конечныйиндекс для того среза \
    'пиццы', который хотите получить.")
print("Для выхода нажмите Enter, не вводя начальную позицию.")
start = None

while start != "":
    start = input("\nНачальная позиция: ")
    if start:
        start = int(start)
        finish = int(input("Конечная позиция: "))
        print("Срез word[", start, ":", finish, "] выглядит как", end=" ")
        print(wod[start:finish])
        
input("\nНажмите Enter, чтобы выйти.\n")