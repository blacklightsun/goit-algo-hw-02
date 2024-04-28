from collections import deque


def palindrome_check(string: str):

    if len(string) < 1:
        raise ValueError

    d = deque()
    d.extend(string.lower())

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


# завдання було тільки створити функцію, але для зручності перевірки додано і безкінечний ігровий цикл з перевіркою даних


while True:
    print("\n" * 3)

    input_string = input("Введіть слово для перевірки ->")

    try:
        word = input_string.strip(' ').split(" ")[
            0
        ]  # якщо введено декілька слів, то перевіряється тільки перше слово, усі інші - ігноруються

        result = "" if palindrome_check(word) else " не"
        print(f"'{word}'{result} є паліндромом.\n")

    except ValueError:
        print('Помилка введення. Спробуйте ще раз')
        continue

    if input("Press 'q' or 'й' for quit, any key + Enter for continue ->") in "qй":
        print("\n")
        break
