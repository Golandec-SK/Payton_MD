# Только согласные
# Демонстрирует, как создовать новую строки из исходных с помощью цикла for
message = input("\nВведите текст: ")
new_message = ""
"""
Константа — это постоянная переменная, значение которой нельзя изменить.
Представьте, что это контейнер, в котором содержится информация, менять
которую мы не можем. 
"""
VOWELS = "aeiouaаеёиоуыэюя"
print()

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Созданная новая строка:", new_message)
print("\nВот ваш текст с изьятыми гласными буквами:", new_message)

input("\n\nНажмите Enter, чтобы выйти.")