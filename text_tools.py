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