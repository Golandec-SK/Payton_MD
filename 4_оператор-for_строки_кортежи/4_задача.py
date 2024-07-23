import random
# кортеж со соловами и подсказками для игры
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
# рандомное слово и подсказка для анаграммы
index = random.randint(0, len(WORDS))
word = WORDS[index]
hint = HINTS[index]
# пустая строка для букв
letter = ''
# закрытая строка с рандомным словом
letters = len(word) * '-'
# количество попыток
attempt = 5
# оценка за подсказку
points_min = 3
points_max = 10
amount_points = 0

print("\t\tДобро пожаловать в игру!")
print(f'\nУгадайте слово из {len(word)} букв , за {attempt} попыток.')
print('Теперь ты можешь 5 раз спросить меня, есть ли какая-то буква в этом слове?\n')

while attempt > 0:
    print(f'\nУ вас {attempt} попыток(и)')
    print('\t\t', letters)
    letter = input('Назовите букву: ')
    if letter in word:
        letters = letters[:word.find(letter)] + letter + letters[word.find(letter)+1:]
        print('\nТакая буква есть в слове!')
    else:
        print("\nТакой буквы нет в этом слове. Попробуй еще.")
    attempt -= 1
    print('\t\t', letters)

given_hint = input('Вам нужна подсказка Да или Нет: ')
if given_hint == 'Да':
    print('Ваша подсказка:', hint)
    amount_points += points_min
else:
    print('Вы черезчур самоуверены, но удачи!')
    amount_points += points_max

answer = input('Какое слово было загадано? ')

if answer == word:
    print("\nПоздравляю!!! Вы угадали слово!!!")
    print(f'Вам начислили {amount_points} очка(ов)')
else:
    amount_points = 0
    print('Увы, Вы не угадали. Слово было:', word)
    print(f'У вас {amount_points} очка(ов)')

print('\tСпасибо за игру.')
input('\nНажмите Enter для выхода\n')