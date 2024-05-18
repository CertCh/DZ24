def create_and_write_file():
    with open("example.txt", "w", encoding="utf-8") as file:
        file.write("Первая строка текста.\n")
        file.write("Вторая строка текста.\n")
        file.write("Третья строка текста.\n")

create_and_write_file()

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

read_file("example.txt")
