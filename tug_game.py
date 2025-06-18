def paver_turtle():
    import turtle

    # Create a turtle object
    paver = turtle.Turtle()
    paver.shape("turtle")
    paver.color("black")
    paver.speed(1)
    paver.penup()

    # Draw the big rectangle (court)
    start_x, start_y = -400, 200
    width, height = 800, 400

    paver.goto(start_x, start_y)
    paver.pendown()
    for _ in range(2):
        paver.forward(width)  # top and bottom sides
        paver.right(90)
        paver.forward(height)  # left and right sides
        paver.right(90)

    # Draw the circle at the center of the rectangle
    radius = height / 2
    center_x = start_x + width / 2
    center_y = start_y - height / 2

    paver.penup()
    # Go to the circle's bottom edge to start drawing the circle (turtle draws counter-clockwise)
    paver.goto(center_x, center_y - radius)
    paver.setheading(0)
    paver.pendown()
    paver.circle(radius)

    # Draw the tug of war line across the center horizontally
    paver.penup()
    paver.goto(start_x, center_y)
    paver.setheading(0)
    paver.pendown()
    paver.forward(width)

    # Draw a brown line on top between the team starting positions
    paver.penup()
    paver.color("chocolate4")  # Set color to brown
    paver.goto(-200, center_y)  # Position slightly above the main line
    paver.setheading(0)
    paver.pendown()
    paver.forward(400)  # Distance from -200 to 200
    paver.color("black")  # Reset color to black

    paver.penup()
    paver.goto(center_x, center_y)
    paver.color("chocolate4")
    paver.fillcolor("chocolate4")
    paver.setheading(0)

    # Ellipse drawing function (approximate by stretching circle)
    def draw_ellipse(t, radius_x, radius_y):
        t.penup()
        t.goto(center_x, center_y - radius_y)
        t.pendown()
        t.begin_fill()
        for angle in range(360):
            x = radius_x * turtle.cos(angle * 3.14159 / 180)
            y = radius_y * turtle.sin(angle * 3.14159 / 180)
            t.goto(center_x + x, center_y + y)
        t.end_fill()

    # The above uses turtle.cos and turtle.sin but these don't exist.
    # So use math module for cos/sin
    import math

    def draw_ellipse(t, radius_x, radius_y):
        t.penup()
        t.goto(center_x, center_y - radius_y)
        t.pendown()
        t.begin_fill()
        for angle in range(361):
            rad = math.radians(angle)
            x = radius_x * math.cos(rad)
            y = radius_y * math.sin(rad)
            t.goto(center_x + x, center_y + y)
        t.end_fill()

    draw_ellipse(paver, radius_x=100, radius_y=50)

    # Return color to black for further drawing (if needed)
    paver.color("black")
    paver.hideturtle()


def turtle_tug(bet, team):
    import random
    import time
    import turtle


    # Set up the screen
    screen = turtle.Screen()
    screen.title("Turtle Tug-of-War")
    screen.bgcolor("lightblue")

    paver_turtle()

    # Create turtles for each team
    team_mud = turtle.Turtle()
    team_grass = turtle.Turtle()

    # Set maximum speed for faster animation
    team_mud.speed(0)
    team_grass.speed(0)

    team_mud.color("chocolate4")
    team_grass.color("green")

    team_mud.shape("turtle")
    team_grass.shape("turtle")

    team_mud.penup()
    team_grass.penup()

    team_mud.setheading(180)

    team_mud.goto(-200, 0)
    team_grass.goto(200, 0)

    team_grass.setheading(180)
    team_mud.setheading(0)# Team Grass faces left

    team_mud.pendown()
    team_grass.pendown()

    # Tugging logic
    team_grass_push = 0
    team_mud_push = 0
    winner = None
    rope_position = 0  # 0 means the rope is in the center

    # For more exaggerated movement
    bounce_offset = 0
    direction = 1

    while not winner:
        # Add random push values to each team - increased range for more dramatic changes
        team_grass_push += random.randint(0, 15)
        team_mud_push += random.randint(0, 15)

        # Calculate the difference to determine which team is winning
        difference = team_grass_push - team_mud_push

        # More exaggerated movement - reduced divisor for larger movements
        new_position = difference / 5  

        # Add bouncing effect for more movement
        bounce_offset += 0.5 * direction
        if bounce_offset >= 10 or bounce_offset <= -10:
            direction *= -1

        # Move the turtles to show the current state of the tug-of-war with added vertical movement
        team_mud.goto(-200 + new_position, bounce_offset)
        team_grass.goto(200 + new_position, -bounce_offset)

        # Check if either team has a 50-point advantage
        if difference >= 50:
            winner = "grass"
        elif difference <= -50:
            winner = "mud"

        # No delay for faster animation

    # Display the winner
    result_turtle = turtle.Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0, 150)


    # Calculate bet result but don't print it
    bet_result = bet * 2 if (team == 0 and winner == "grass") or (team == 1 and winner == "mud") else -bet

    # Wait for user to click to close the window
    screen.exitonclick()

    # Return the winner instead of printing
    return winner

