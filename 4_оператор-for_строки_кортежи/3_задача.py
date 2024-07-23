# Анаграммы
# Компьютер выбирает какое-либо слово  и хаотично переставляет его буквы
# Задача игрока - востановить исходное слово
# создадим константу с последовательностью слов, из которых компьютер будет выбирать
import random

WORDS = ("питон",
         "анаграмма",
         "простая",
         "сложная",
         "ответ")
HINTS =  ("язык", 
         "игра",
         "сложная",
         "простая",
         "вопрос")
# рандомное слово для анаграммы
index = random.randint(0, len(WORDS))
word = WORDS[index]
hint = HINTS[index]
# сравненение варианта игрока с оригиналом
correct = word
# пустая строка для анаграммы
jumble = ''
# оценка за подсказку
points_min = 3
points_max = 10
amount_points = 0
# количество попыток
attempt = 5
# создаем смешанную версию слова
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("\t\tДобро пожаловать в игру 'Анаграммы'!")
print(f'\nУгадайте слово: {jumble} , за {attempt} попыток.')

given_hin = input('Вам нужна подсказка Да или Нет: ')
if given_hin == 'Да':
    print('Ваша подсказка:', hint)
    amount_points += points_min
else:
    print('Вы черезчур самоуверены, но удачи!')
    amount_points += points_max

guess = input('\nПопробуйте отгадать исходное слово: ')

while guess != correct and guess != '' and attempt > 0:
    print('К сожелению, вы не угодали.\n')
    guess = input('Попробуйте еще раз: ')
    attempt -= 1

if guess == correct:
    print(f'Да, именно так! Вы угодали, вам начислили {amount_points} очка(ов)')
    print('У вас осталось:', attempt, 'попыток')

print('Спасибо за игру.')
input('\nnНажмите Enter для выхода\n')