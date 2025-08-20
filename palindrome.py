# объявление функции
def is_palindrome(text):
    letters = [ch.lower() for ch in text if ch.isalpha()]
    j = len(letters) - 1  # последний индекс
    for i in range(len(letters) // 2):  # достаточно проверять половину
        if letters[i] != letters[j - i]:  # сравниваем с зеркальным индексом
            return False
    return True


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))