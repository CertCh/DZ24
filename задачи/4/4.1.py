import itertools

def generate_combinations(word):
    combinations = set()
    for i in range(1, len(word) + 1):
        for combo in itertools.permutations(word, i):
            combinations.add(''.join(combo))
    return combinations

word = "abc"
combinations = generate_combinations(word)
print(combinations)
