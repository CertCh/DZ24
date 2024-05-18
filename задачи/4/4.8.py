class Crossword:
    def __init__(self, words):
        self.words = sorted(words, key=lambda x: -len(x))  
        self.size = max(len(word) for word in words) + 2   
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.create_grid()

    def create_grid(self):
        for word in self.words:
            placed = False
            for row in range(self.size):
                for col in range(self.size):
                    if self.can_place_horizontally(word, row, col):
                        self.place_horizontally(word, row, col)
                        placed = True
                        break
                    if self.can_place_vertically(word, row, col):
                        self.place_vertically(word, row, col)
                        placed = True
                        break
                if placed:
                    break

    def can_place_horizontally(self, word, row, col):
        if col + len(word) > self.size:
            return False
        if col > 0 and self.grid[row][col-1] != ' ':
            return False
        if col + len(word) < self.size and self.grid[row][col+len(word)] != ' ':
            return False
        for i in range(len(word)):
            if self.grid[row][col+i] != ' ' and self.grid[row][col+i] != word[i]:
                return False
        return True

    def place_horizontally(self, word, row, col):
        for i in range(len(word)):
            self.grid[row][col+i] = word[i]

    def can_place_vertically(self, word, row, col):
        if row + len(word) > self.size:
            return False
        if row > 0 and self.grid[row-1][col] != ' ':
            return False
        if row + len(word) < self.size and self.grid[row+len(word)][col] != ' ':
            return False
        for i in range(len(word)):
            if self.grid[row+i][col] != ' ' and self.grid[row+i][col] != word[i]:
                return False
        return True

    def place_vertically(self, word, row, col):
        for i in range(len(word)):
            self.grid[row+i][col] = word[i]

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))

    def solve(self):
        self.display_grid()

words = ["cat", "dog", "bird", "fish"]
crossword = Crossword(words)
crossword.solve()
