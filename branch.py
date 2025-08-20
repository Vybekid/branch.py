import turtle
import colorsys

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cosmic Sunburst")

pen = turtle.Turtle()
pen.speed(0)      # Maximum drawing speed
pen.hideturtle()  # Hide the turtle arrow for a clean final image

# --- Initial variables ---
hue = 0.0         # Starting hue for the color cycle
num_lines = 150   # Total number of lines to draw in the sunburst

# --- Main loop to draw the pattern ---
pen.penup()
pen.goto(0, 0)    # Start at the center of the screen
pen.pendown()

for i in range(num_lines):
    # Convert HSV color to RGB and set the pen color
    # Hue cycles, while Saturation and Value are kept at max for vibrancy
    rgb_color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pen.pencolor(rgb_color)

    # Move the turtle forward to draw a line
    # The length of the line is determined by the loop variable
    pen.forward(i * 2.5)

    # --- Move back to the center without drawing ---
    pen.penup()
    pen.backward(i * 2.5) # Go back the same distance
    pen.pendown()

    # Turn the turtle slightly for the next line
    # Dividing 360 degrees by the number of lines gives an even spacing
    pen.left(360 / num_lines)

    # Increment the hue to shift the color for the next line
    hue += 1 / num_lines

# Keep the window open
turtle.done()