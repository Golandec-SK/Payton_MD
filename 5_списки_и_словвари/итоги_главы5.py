# Весилица
# Красивая игра "Виселица". Компьютер случайным оброзом выбирает словою,
# которое должен угодать игрок букву за буквой. Если игрок не сумеет
# отгодать за отведенное количество попыток, на экране появиться
# фигура повешенного.
# импорт модуля
import random
# создаем константы
HANGMAN = (""" 
    
|\
|_\_____""", """
|     
|     
|
|    
|     
|    
|   
|\
|_\_____""", """
------.
|     |
|     
|
|    
|     
|    
|   
|\
|_\_____""", """
------.
|     |
|     O
|    
|   
|   
|   
|   
|\
|_\_____""", """
------.
|     |
|     O
|    /|\\
|   
|   
|   
|   
|\
|_\_____""", """
------.
|     |
|     O
|    /|\\
|    |||
|     
|    
|   
|\
|_\_____""", """
------.
|     |
|     O
|    /|\\
|    |||
|     |
|    
|    
|\
|_\_____""", """
------.
|     |
|     O
|    /|\\
|    |||
|     |
|    | |
|    | |
|\
|_\_____
""")
# константа максимальное количество ошибок, дозволеных игроку
MAX_WRONG = len(HANGMAN) - 1
# кортеж
WORDS = ('питон', 'змея', 'фиолетовый', 'лень', 'гроза')
# инициализация переменных
# слово для отгадывания
word = random.choice(WORDS)
# по одному дефису на каждое букву, которую надо отгодать
so_far = '-'*len(word)
# количество ошибок, который сделал игрок
wrong = 0
# буквы, который игрок уже предлагал
used = []
# создаем основной цикл
print('\n\t\tДобро пожаловать в игру "Виселица". Удачи вам!\n')
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print('\nВы уже предлогали следующу букву: \n\t\t', used)
    print('Отгаданное вами в слове сейчас выглядит так:\n\t\t', so_far)
    guess = input('\nВведите букву: ')
    while guess in used:
        print('Вы уже предлагали букву:', guess)
        guess = input('\nВведите букву: ')
    used.append(guess)
    if guess in word:
        print(f'\nДа! буква {guess} есть в слове!')
        # новая строка so_far с отгаданной буквой или буквами
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print(f'\nК сожелению, буквы {guess} нет в слове')
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print('\nВас повесили!')
else:
    print('\nВы отгодали!')
print('\nБыло загадано слово', word)
input('\nНажмите Enter для выхода\n')