import turtle
import random

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)          # Set the drawing speed to the maximum
pen.hideturtle()      # Hide the turtle for a clean look
pen.setheading(90)    # Start the turtle pointing straight up
pen.color("white")

# --- The Recursive Function to Draw the Tree ---
def draw_tree(branch_len, pen):
    """
    Recursively draws a branch of the fractal tree.
    """
    if branch_len > 8:
        # --- Make branches thinner and greener as they get smaller ---
        if branch_len < 30:
            pen.pensize(2)
            pen.color("#2ECC71") # Green for leaves/twigs
        elif branch_len < 60:
            pen.pensize(4)
            pen.color("#AF601A") # Medium brown for smaller branches
        else:
            pen.pensize(7)
            pen.color("#A0522D") # Dark brown for the trunk

        # Draw the main branch
        pen.forward(branch_len)

        # Save the current position and angle
        current_pos = pen.pos()
        current_heading = pen.heading()
        
        # --- Create the right sub-branch ---
        # Introduce some randomness for a more natural look
        angle = random.randint(15, 30)
        pen.right(angle)
        draw_tree(branch_len - random.randint(12, 18), pen)

        # --- Create the left sub-branch ---
        # Restore position and angle to branch from the same spot
        pen.setpos(current_pos)
        pen.setheading(current_heading)
        pen.left(angle)
        draw_tree(branch_len - random.randint(12, 18), pen)
        
        # --- Return to the base of the branch to allow parent to continue ---
        pen.setpos(current_pos)
        pen.setheading(current_heading)

# --- Start the Drawing ---
# Position the turtle at the bottom center
pen.penup()
pen.goto(0, -300)
pen.pendown()

# Call the function to draw the tree with an initial branch length
draw_tree(100, pen)

# Keep the window open
turtle.done()