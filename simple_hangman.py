import random


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def correct_letter(letter):
    return (len(letter) == 1) and ("А" <= letter <= "Я")


def progress_completion(word_completion, letter, word):

    for i in range(len(word)):
        if word[i] == letter:
            word_completion = word_completion[:i] + word_completion[i + 1 :]
            word_completion = word_completion[:i] + letter + word_completion[i:]

    return word_completion


def play(word):

    word_completion = "_" * len(word)
    guessed_letters = []  # список уже названных букв
    tries = 6  # количество попыток
    print("Игра началась!")

    while tries != 0:

        print(display_hangman(tries))
        print(word_completion)

        if not "_" in word_completion:
            print("Вы победили!")
            break

        letter = input("Введите букву от А до Я: ").upper()

        while not correct_letter(letter):
            print("Некорректный ввод")
            letter = input("Введите букву от А до Я: ").upper()

        while letter in guessed_letters:
            print("Вы уже угадали эту букву, попробуйте другую")
            letter = input("Введите букву от А до Я: ").upper()

        if letter in word:
            guessed_letters.append(letter)
            word_completion = progress_completion(word_completion, letter, word)

        else:
            tries -= 1
            print("Такой буквы нет")

    else:
        print(display_hangman(tries))
        print(f"Вы проиграли!\nЗагаданное слово: {word}")


category_list = {
    1: ["лев", "волк", "осел", "корова", "крокодил"],
    2: ["бургер", "щавель", "борщ", "пицца"],
    3: ["стул", "стол", "лампа", "шкаф", "кровать"],
}

new_game = 1

while new_game == 1:

    print("Выберите категорию перед началом игры:")
    print("1) Животные\n2) Еда\n3) Мебель")
    category = input("Введите номер категории (1, 2 или 3): ")

    while category not in ["1", "2", "3"]:
        category = input("Нет такой категории\nВведите номер категории (1, 2 или 3): ")

    word_list = category_list.get(int(category))
    play(get_word())
    new_game = input("Хотите сыграть ещё разок? [д/н]: ").lower() == "д"

print("До новых встреч!")
