import random

def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices)
    user_choice = input("Сделайте ваш выбор (камень, ножницы, бумага): ").lower()
    
    if user_choice not in choices:
        print("Неправильный выбор. Попробуйте снова.")
        return
    
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы выиграли!")
    else:
        print("Компьютер выиграл!")

rock_paper_scissors()
