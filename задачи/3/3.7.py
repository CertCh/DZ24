def analyze_text_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    
    words = text.split()
    word_count = len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    average_word_length = sum(len(word) for word in words) / word_count if word_count != 0 else 0

    print(f"Количество слов: {word_count}")
    print(f"Количество предложений: {sentence_count}")
    print(f"Средняя длина слова: {average_word_length:.2f}")

analyze_text_file("large_text.txt")
