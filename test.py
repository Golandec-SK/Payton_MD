import random 
 
WORDS = ("простая", "ответ", "подстаканник") 
word = random.choice(WORDS) 
correct = len(word) 
attempts = 5 
guessed_letters = set() 
 
while attempts > 0: 
    print(f"\nУгадай слово, в нем {correct} букв, за {attempts} попыток:") 
    guess = input('Назовите букву или слово целиком: ') 
    attempts -= 1 
 
    if guess in word: 
        guessed_letters.add(guess) 
        guessed_word = ''.join([c if c in guessed_letters else '_' for c in word]) 
        print('Такая буква есть в слове!', guessed_word) 
 
        if set(word) == guessed_letters: 
            print("Поздравляю!!! Вы угадали слово!!!") 
            break 
    else: 
        print("Попробуй еще.\n") 
 
print('Увы, Вы не угадали. Слово было:', word)