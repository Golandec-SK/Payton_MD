# Привередливая считалка
# Демонстрирует работу команды break и continue
count = 0
# намеренное создание бесконечного цикла
while True:
    count += 1
    # завершить цикл, если count принимает значение больше 10
    if count > 10:
        break # оператор используется для немедленной остановки цикла
    # пропустить 5
    if count == 5:
        continue # пропуск определенных элементов последовательности, но без завершения цикла
    print(count)
    
    input("\nНажмите Enter, чтобы выйти.")