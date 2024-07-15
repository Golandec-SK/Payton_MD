# Симулятор пирожка с "сюрпризом "
import random

surprise = random.randint(1, 5)

if surprise == 1:
    print("Пирожок с котятами))")
elif surprise == 2:
    print("Пирожок с малиной.")
elif surprise == 3:
    print("Пирожок с тапочками.")
elif surprise == 4:
    print("Пирожок за шкафом.")
else:
    print("Ура ты выиграл больничный!!!")
    
input("\nНажмите Enter, чтобы выйти.")