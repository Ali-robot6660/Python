import turtle

# Настройка окна
window = turtle.Screen()
window.bgcolor("black")

# Настройка "черепашки"
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Цикл рисования
for i in range(120):
    pen.color(colors[i % 6])       # Меняем цвет по кругу
    pen.forward(i * 3)             # Делаем шаг больше каждый раз
    pen.right(59)                  # Поворачиваем

# Завершение
turtle.done()
