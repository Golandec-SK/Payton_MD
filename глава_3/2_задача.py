# Орел или решко
import random

eagle = 0
resko = 0
attempt = 0

while attempt != 100:
    coin = random.randint(1, 2)
    attempt += 1
    if coin == 1:
        eagle += 1
    else:
        resko += 1
print("Орел выпал:", eagle, 'раз, а решко выпвло', resko, "раз.")

input("\nНажмите Enter, чтобы выйти.")