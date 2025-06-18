def paver_turtle():
    import turtle

    drawer = turtle.Turtle()
    drawer.shape("turtle")
    drawer.speed(0)
    drawer.penup()
    drawer.color("black")

    start_x = -400
    finish_x = 400
    start_y = 115
    spacing = 30
    num_turtles = 10
    line_length = 20  # length of the race marker lines

    # Draw title text above the lanes
    drawer.goto(0, start_y + 40)
    drawer.write("TURTLE RACE", align="center", font=("Arial", 24, "bold"))

    # Draw horizontal lines for lanes
    for i in range(num_turtles + 1):
        y = start_y - i * spacing
        drawer.goto(start_x, y)
        drawer.pendown()
        drawer.forward(finish_x - start_x)
        drawer.penup()

    # Draw start and finish vertical lines
    drawer.goto(start_x, start_y)
    drawer.setheading(-90)
    drawer.pensize(3)
    drawer.pendown()
    drawer.forward(spacing * num_turtles)
    drawer.penup()

    drawer.goto(finish_x, start_y)
    drawer.pendown()
    drawer.forward(spacing * num_turtles)
    drawer.penup()

    # Draw some vertical decoration lines (like race markers) across the lanes
    marker_spacing = 40
    for x in range(start_x + marker_spacing, finish_x, marker_spacing):
        drawer.goto(x, start_y)
        drawer.setheading(-90)
        drawer.pensize(1)
        drawer.pendown()
        for i in range(num_turtles):
            drawer.forward(line_length)
            drawer.penup()
            drawer.forward(spacing - line_length)
            drawer.pendown()
        drawer.penup()

    drawer.pensize(1)
    drawer.color("black")
    drawer.hideturtle()


def turtle_race(bet, turtle_choice):
    import turtle
    import random

    screen = turtle.Screen()
    screen.bgcolor("burlywood")
    screen.title("Turtle Race")

    paver_turtle()

    # Setup turtles
    red = turtle.Turtle()
    blue = turtle.Turtle()
    green = turtle.Turtle()
    yellow = turtle.Turtle()
    orange = turtle.Turtle()
    purple = turtle.Turtle()
    pink = turtle.Turtle()
    brown = turtle.Turtle()
    black = turtle.Turtle()
    white = turtle.Turtle()
    turtles = [red, blue, green, yellow, orange, purple, pink, brown, black, white]
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]

    start_x = -400  # race start x-position
    start_y = 100   # vertical layout start
    spacing = 30    # distance between turtles vertically

    for index, (t, color) in enumerate(zip(turtles, colors)):
        t.shape("turtle")
        t.color(color)
        t.penup()
        t.goto(start_x, start_y - index * spacing)
        t.pendown()

    finish_line_x = 400
    winner = None

    # Race logic loop
    while not winner:
        for t in turtles:
            t.forward(random.randint(1, 10))
            if t.xcor() >= finish_line_x:
                winner = t.color()[0]
                break

    screen.bye()  # Close the screen automatically after race ends
    return winner

# Example usage:
