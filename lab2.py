import turtle

def draw_snake_explicit():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    segment_length = 50

    # 1. Первый шаг - вниз
    t.setheading(270)
    t.forward(segment_length)

    for _ in range(2):
        # Шаг влево
        t.setheading(180)
        t.forward(segment_length)

        # Шаг вверх
        t.setheading(90)
        t.forward(segment_length)

        # Шаг влево
        t.setheading(180)
        t.forward(segment_length)

        # Шаг вниз
        t.setheading(270)
        t.forward(segment_length)

    t.shape("arrow")
    t.stamp()
    turtle.done()

if __name__ == "__main__":
    draw_snake_explicit()

