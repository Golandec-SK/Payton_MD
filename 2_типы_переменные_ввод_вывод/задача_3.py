# Расчет чаевых
lettuce = 30
steak = 100
coffee = 50

total_sum = lettuce + steak + coffee
tips = 20 * total_sum / 100
result = total_sum + tips

print(f"Вы заказали на {total_sum} руб. плюс чаевые {tips} руб. К омлате {result} руб.")