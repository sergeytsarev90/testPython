import random


words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', 'шайба', 'олимпиада']


def print_list_as_str(arg):
    print(''.join(arg))
    return True


secret_word = random.choice(words_list)
print(secret_word)

user_word = ['*'] * len(secret_word)
# print(user_word)
print_list_as_str(user_word)
# print(''.join(user_word))

user_word[0] = 'б'

print_list_as_str(user_word)

