# Guess the Number Game
# Диапазон поиска
low = 1
high = 100

# Счётчик шагов
steps = 0

while True:
    guess = (low + high) // 2  # берём середину диапазона
    steps += 1
    print(guess, "is your guess?") # Выводим предположение
    secret = input("Is it correct? (y or l or h your number): ").strip().lower() #спрос на ответ
    
    if secret == 'y': #если угадали
        print("Congratulations! You guessed the number in", steps, "steps.")
        print(guess, "is the secret number!")
        break
    elif secret == 'l':
        low = guess + 1  # число больше, сужаем диапазон справа
    elif secret == 'h':
        high = guess - 1  # число меньше, сужаем диапазон слева
    else:
        print("Please answer with 'y', 'l', or 'h'.")