from collections import deque


def palindrome_check(input_string):

    if len(input_string) == 0:
        print("Слово для перевірки не введено!\n")
        return

    def word_check(d: deque):
        while len(d) > 1:
            if d.popleft() != d.pop():
                return len(d) + 2
        return len(d)

    d = deque()
    word = input_string.split(" ")[
        0
    ]  # якщо введено декілька слів, то перевіряється тільки перше слово, усі інші - ігноруються
    d.extend(word.lower())

    if word_check(d) <= 1:
        print(f"'{word}' є паліндромом.\n")
    else:
        print(f"'{word}' не є паліндромом.\n")


# завдання було тільки створити функцію, але для зручності перевірки додано і безкінечний ігровий цикл


while True:
    print("\n" * 3)

    palindrome_check(input("Введіть слово для перевірки ->"))

    if input("Press 'q' or 'й' for quit, any key + Enter for continue ->") in "qй":
        print("\n")
        break
