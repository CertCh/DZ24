from collections import Counter
import re

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    
    for word, count in word_counts.most_common():
        print(f'{word}: {count}')

file_path = 'example.txt'
analyze_text(file_path)
