car = int(input("\nВведите стоимость автомобиля: "))

tax = int(car * 13 / 100)
collecting = int(car * 10 / 100)
agential = 10000
delivery = 5000

result = tax + collecting + agential + delivery + car

print('Налог \t\trub.', tax, "\nАгенские \trub.", agential, "\nCбор \t\trub.", collecting, \
    "\nДоставка \trub.", delivery,"\n---------","\nИтого \t\trub.", result)