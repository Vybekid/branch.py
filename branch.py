import turtle

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.bgcolor("#101010")  # Use a very dark grey for a sleek look
screen.title("Hypnotic Tunnel")

pen = turtle.Turtle()
pen.speed(0)        # Maximum drawing speed
pen.hideturtle()    # Hide the turtle for a clean look
pen.width(2)        # Set a nice, visible line width

# --- Define a list of colors for a cool, modern palette ---
colors = ["#00FFFF", "#48D1CC", "#008B8B", "#20B2AA", "#4682B4", "#5F9EA0"]
#          Cyan,    MediumTurquoise, DarkCyan, LightSeaGreen, SteelBlue, CadetBlue

# --- Function to draw a single square ---
def draw_square(size):
    """Draws a square of a given size."""
    for _ in range(4):
        pen.forward(size)
        pen.left(90)

# --- Main loop to draw the nested, rotating squares ---
initial_size = 400  # Starting size of the largest square

for i in range(120):
    # Set the color for the current square, cycling through the palette
    pen.pencolor(colors[i % len(colors)])

    # Draw the square with its current size
    draw_square(initial_size - i * 3)

    # Rotate the turtle slightly for the next, smaller square
    pen.left(5)

# Keep the window open
turtle.done()