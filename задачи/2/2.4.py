class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]
    
    def is_triangle(self):
        if any(side <= 0 for side in self.sides):
            return "С отрицательными числами ничего не выйдет!"
        if any(not isinstance(side, (int, float)) for side in self.sides):
            return "Нужно вводить только числа!"
        a, b, c = sorted(self.sides)
        if a + b > c:
            return "Ура, можно построить треугольник!"
        return "Жаль, но из этого треугольник не сделать."


checker = TriangleChecker(3, 4, 5)
print(checker.is_triangle())  