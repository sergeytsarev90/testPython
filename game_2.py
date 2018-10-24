import random
MAX_ERRORS = 8


words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', 'шайба', 'олимпиада']


def print_list_as_str(arg):
    print(''.join(arg))


secret_word = random.choice(words_list)
print(secret_word)

user_word = ['*'] * len(secret_word)
print_list_as_str(user_word)
errors_counter = 0
while True:
    letter = input('Ввведите букву: ').lower()

    if len(letter) != 1 or not letter.isalpha() or not 1040 <= ord(letter) <= 1103:
        continue

    if letter in secret_word:

        for idx, char in enumerate(secret_word):
            if char == letter:
                user_word[idx]=letter
        if '*' not in user_word:
            print('Вы выиграли')
            break
    else:
        errors_counter += 1
        print('Ошибок: ', errors_counter)
        if errors_counter == MAX_ERRORS:
            print('Вы проиграли')
            break

    print_list_as_str(user_word)

print('Пока')
