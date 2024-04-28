import random
from queue import Queue

"""
Імітуємо обробку черги в пенсійному фонді.
Щоб було цікавіше:
- є початкова черга з тих, хто прийшов до відкриття держустанови;
- хтось може не прийти на призначений час;
- може прийти герой капіталістичної праці з купою документів, які обробити можна тільки за два цикли
"""


# очистка екрана
print("\x1b[2J")

# створення черги заявок (клієнти пенсійного фонду)
queue = Queue()

# імітація створення початкової черги до відкриття пенсійного фонду (бабульки, які прийшли раніше за всіх)))
for i in range(1, 6):
    queue.put(i)

# лічільнк складних кейсів (відвідувач - герой капіталістичної праці, його документи вимагають два цикла обробки заявок, а не один, як у всіх)
DIFFICULT_CASE = 0


def generate_request():

    req = random.randint(0, 9)

    if req >= 1:
        queue.put(req)
        print(f"Додана заявка #{req}.")
        print(f"В черзі тепер {queue.qsize()} заявок: {'+' * queue.qsize()}.\n")
    else:
        # якщо випадає нуль - то ніхто не прийшов у цей цикл
        print(f"Ніхто не прийшов.")
        print(
            f"В черзі залишилося {queue.qsize()} необроблених заявок: {'+' * queue.qsize()}.\n"
        )


def process_request():

    global DIFFICULT_CASE

    # перевірка умови - чи не почалася обробка складного випадку. Якщо так - в цьому циклі завершується обробка складного випадку
    if DIFFICULT_CASE > 0:
        print(f"Обробка заявки #{DIFFICULT_CASE}. Додатковий час.")
        print(
            f"В черзі залишилось {queue.qsize()} необроблених заявок: {'+' * queue.qsize()}\n"
        )
        DIFFICULT_CASE = 0
        return

    # якщо перед цим не було складного випадку, то продовжуємо обробляти запити з черги
    if not queue.empty():
        processed_req = queue.get()
        print(f"Обробка заявки #{processed_req}.")
        print(
            f"В черзі залишилось {queue.qsize()} необроблених заявок: {'+' * queue.qsize()}\n"
        )

        # якщо запит складний (processed_req == 9), то на наступному циклі будемо продовжувати оброблювати його, а не запити з черги
        if processed_req == 9:
            DIFFICULT_CASE = processed_req
    else:
        print(f"Немає заявок для обробки!")


while True:
    print("\n" * 3)

    generate_request()
    process_request()

    if input("Press 'q' or 'й' for quit, any key + Enter for continue ->") in "qй":
        print("\n")
        break
