def unique_sorted_words():
    user_input = input("Введите строку: ")
    words = user_input.split()
    unique_words = sorted(set(words))
    print("Уникальные слова в алфавитном порядке:")
    for word in unique_words:
        print(word)

unique_sorted_words()
