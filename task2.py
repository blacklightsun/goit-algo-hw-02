from collections import deque


def palindrome_check(string: str):

    if len(string) < 1:
        raise ValueError

    clear_string = ""
    for char in string:
        if char.isalnum():
            clear_string += char

    d = deque()
    d.extend(clear_string.lower())

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


# завдання було тільки створити функцію, але для зручності перевірки додано і безкінечний ігровий цикл з перевіркою даних


while True:
    print("\n" * 3)

    input_string = input("Введіть слово для перевірки ->")

    try:
        result = "" if palindrome_check(input_string) else " не"
        print(f"'{input_string}'{result} є паліндромом.\n")

    except ValueError:
        print('Помилка введення. Спробуйте ще раз')
        continue

    if input("Press 'q' or 'й' for quit, any key + Enter for continue ->") in "qй":
        print("\n")
        break
