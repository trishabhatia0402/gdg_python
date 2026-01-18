import tkinter as tk
import turtle

# -------------------------------------------------
# L-SYSTEM STRING EXPANSION
# -------------------------------------------------
def expand_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for ch in current:
            if ch in rules:
                next_string += rules[ch]
            else:
                next_string += ch
        current = next_string
    return current


# -------------------------------------------------
# DRAWING / COMMAND PARSER
# -------------------------------------------------
def draw_lsystem(t, instructions, angle):
    stack = []

    screen.tracer(0, 0)

    for i, cmd in enumerate(instructions):
        # ✅ FIXED RGB COLOR (3 values)
        green = 0.3 + (i / len(instructions)) * 0.7
        t.pencolor(0.0, green, 0.0)

        if cmd == "F":
            t.forward(5)

        elif cmd == "+":
            t.right(angle)

        elif cmd == "-":
            t.left(angle)

        elif cmd == "[":
            stack.append((t.position(), t.heading()))

        elif cmd == "]":
            pos, heading = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

    screen.update()


# -------------------------------------------------
# GENERATE BUTTON
# -------------------------------------------------
def generate():
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    axiom = axiom_entry.get()
    angle = float(angle_entry.get())
    iterations = int(iter_entry.get())

    rules = {}
    for rule in rules_entry.get().split(","):
        left, right = rule.split(":")
        rules[left.strip()] = right.strip()

    final_string = expand_lsystem(axiom, rules, iterations)
    draw_lsystem(t, final_string, angle)


# -------------------------------------------------
# TKINTER GUI + EMBEDDED TURTLE
# -------------------------------------------------
root = tk.Tk()
root.title("L-System Fractal Architect")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(side=tk.LEFT)

screen = turtle.TurtleScreen(canvas)
screen.colormode(1.0)   # allows 0.0–1.0 colors

t = turtle.RawTurtle(screen)
t.speed(0)
t.hideturtle()

panel = tk.Frame(root)
panel.pack(side=tk.RIGHT, padx=10)

tk.Label(panel, text="Axiom").pack()
axiom_entry = tk.Entry(panel)
axiom_entry.insert(0, "F")
axiom_entry.pack()

tk.Label(panel, text="Rules (Example: F:F+F-F)").pack()
rules_entry = tk.Entry(panel)
rules_entry.insert(0, "F:F+F-F")
rules_entry.pack()

tk.Label(panel, text="Angle").pack()
angle_entry = tk.Entry(panel)
angle_entry.insert(0, "90")
angle_entry.pack()

tk.Label(panel, text="Iterations").pack()
iter_entry = tk.Entry(panel)
iter_entry.insert(0, "4")
iter_entry.pack()

tk.Button(panel, text="Generate", command=generate).pack(pady=10)

root.mainloop()
