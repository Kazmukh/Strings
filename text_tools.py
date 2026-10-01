# Задание №2
def clean_notice(text):
    return " ".join(text.split()) # данная строка уберает все проьелы и табуляции и с помощбю join соеденияет получивший ответ
print(clean_notice(" EKEB ждёт Т118! "))
print(clean_notice("Алматы\nАстана\tТараз"))


# Задание №3
# def has_bug(text):         изменил на такой вариант т.к. функция и так выдаст ответ True False
#     if text.find("BUG"):   и сделал просто проверку сообщения на нахождения собвдения по типу скана
#         return True
#     return False
def has_bug(text):
    return "bug" in text.lower()
print(has_bug("BUG найден"))
print(has_bug("найден bug"))
print(has_bug("DEBUG"))
print(has_bug("Все работает"))


# Задание №4
def valid_nickname(text):
    if not (4 <= len(text) <= 12):
        return False, "неверная длина (должна быть от 4 до 12 символов)"
    LETTERS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" # Я спросил ИИ что если использовать втроенную команду isalpha/isalnum нужно заново изобретать велосипед и просто всунул весь латинский алфавит
    ALLOWED_CHARS = LETTERS + "0123456789_"
    if text[0] not in LETTERS:
        return False, f"недопустимый первый символ '{text[0]}' (должна быть латинская буква)"
    for char in text[1:]:
        if char not in ALLOWED_CHARS:
            return False, f"недопустимый символ '{char}'"
    return True
print(valid_nickname("Aruzhan_7"))
print(valid_nickname("A123"))
print(valid_nickname("Abcdefghijkl"))

print(valid_nickname("A12"))
print(valid_nickname("Abcdefghijklm"))

print(valid_nickname("7Aruzhan"))
print(valid_nickname("Айдана"))
print(valid_nickname(" user"))
print(valid_nickname("User-1"))
print(valid_nickname(""))


# Задание №5
def preview(text, limit):
    clearned = clean_notice(text)
    if len(clearned) <= limit:
        return clearned
    return clearned[:limit - 3] + "..."
print(preview("EKEB приглашает", 10))
print(preview(" EKEB ", 4))
print(preview("Алматы", 3))
print(preview(" ", 3))
print(preview("ABC", 3))
print(preview("abc", 3))
print(preview("user", 4))
print(preview("plaeyr_one_1", 12))
print(preview("player_one_12", 13))
print(preview("123456789", 9))
print(preview("1234567890", 10))
print(preview("12345678901", 11))


# Задание №6
def parse_event(line):
    parts = line.split(";")
    if len(parts) != 3:
        return None
    group = parts[0].strip()
    status = parts[1].strip()
    message = parts[2].strip()
    group = group.upper()
    status = status.upper()
    if group not in ("Т118", "Т119"):
        return None
    if status not in ("PASS", "FAIL"):
        return None
    if not message:
        return None
    return [group, status, message]
print(parse_event(" т118 ; fail ; Ошибка входа "))
print(parse_event("Т119;PASS;Проверка завершена"))
print(parse_event("Т118;PASS;OK"))
print(parse_event("Т119;WAIT;OK"))
print(parse_event("Т118;FAIL; "))
print(parse_event("Т118;FAIL;"))
print(parse_event("Т118;FAIL;а;б"))


# Задание №7
def failures(lines, group):
    group = group.strip().upper()

    if group != "Т118" and group != "Т119":
        return []

    result = []

    for line in lines:
        event = parse_event(line)

        if event is not None:
            if event[0] == group and event[1] == "FAIL":
                result.append(event[2])

    return result
# Проверка
events = [
    "Т118;PASS;Вход работает",
    " т118 ; fail ; Ошибка входа ",
    "Т119;FAIL;Не открывается профиль",
    "Т118;FAIL;Ошибка входа",
    "Т118;FAIL;",
    "не запись"
]

print(failures(events, " т118 "))
print(failures(events, "Т119"))
print(failures(events, "Т120"))
print(failures([], "Т118"))


# Задание №8
def search_messages(lines, query):
    query = query.strip().casefold()

    if query == "":
        return []

    result = []

    for line in lines:
        event = parse_event(line)

        if event is not None:
            if query in event[2].casefold():
                result.append(event[2])

    return result


# Проверка
events = [
    "Т118;PASS;Вход работает",
    " т118 ; fail ; Ошибка входа ",
    "Т119;FAIL;Не открывается профиль",
    "Т118;FAIL;Ошибка входа",
    "Т118;FAIL;",
    "не запись"
]

print(search_messages(events, " ВХОД "))
print(search_messages(events, ""))
print(search_messages(events, "профиль"))

