def brackets_check(string: str):

    # словник відповідностей закриваючих та відкриваючих дужок
    brackets_dict = {")": "(", "]": "[", "}": "{"}

    # виключення зайвих (які не є дужками) символів
    brackets_string = ""
    for char in string:
        if (char in brackets_dict) or (char in brackets_dict.values()):
            brackets_string += char

    # створюємо чергу (на базі списку) і наповнюємо її рядком для аналізу
    d = list(brackets_string)

    # перевірка чи є дужка відкриваючою
    def isopened(br):
        nonlocal brackets_dict
        return br in brackets_dict.values()

    # перевірка чи є дужка закриваючою
    def isclosed(br):
        nonlocal brackets_dict
        return br in brackets_dict

    # перевірка чи відповіє тип закриваючої дужки відкриваючій
    def sameopened(br):
        nonlocal brackets_dict
        return brackets_dict[br]

    # створюємо стек для тимчасового зберігання відкриваючих дужок
    stack = []

    while len(d) > 0:

        # берем перший елемент з черги
        item = d.pop(0)

        # як відкриваюча - в стек
        if isopened(item):
            stack.append(item)

        # якщо закриваюча
        if isclosed(item):
            # перевіряємо чи стек не пустий
            if len(stack) <= 0:
                return False
            # якщо не пустий, то перевіряємо відповідність відкриваючих та закриваючих дужок
            if sameopened(item) != stack.pop():
                return False

    # якщо в стеку щось залишилося, то ці дужки не закриті
    return not bool(len(stack))


while True:
    print("\n" * 3)

    if brackets_check(input("Введіть рядок для перевірки ->")):
        print("Сіметрично")
    else:
        print("Несиметрично.")

    if input("Press 'q' or 'й' for quit, any key + Enter for continue ->") in "qй":
        print("\n")
        break
