# Считалка
# Демонстрирует использование функции ramge
print("Посчитаем: ")
for i in range(10):
    print(i, end=" ")
print("\n\nПеречислим кратное пяти:")
for i in range(0, 50, 5):
    print(i, end=" ")
print("\n\nПосчитаем в обратном порядке:")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nНажмите Enter, чтобы выйти.")

"""
range() позволяет вам генерировать ряд чисел в рамках заданного
диапазона. В зависимости от того, как много аргументов вы передаете
функции, вы можете решить, где этот ряд чисел начнется и закончится,
а также насколько велика разница будет между двумя числами.

Есть три способа вызова range():

range(стоп) берет один аргумент
range(старт, стоп) берет два аргумента
range(старт, стоп, шаг) берет три аргумента
"""