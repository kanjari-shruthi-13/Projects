from tkinter import *
import math

# ---------------- GLOBALS ---------------- #
exp = ""

# ---------------- FUNCTIONS ---------------- #
def press(num):
    global exp
    exp += str(num)
    equation.set(exp)

def equal_press():
    global exp
    try:
        total = str(eval(exp))
        equation.set(total)
        exp = total
    except:
        equation.set("Error")
        exp = ""

def clear():
    global exp
    exp = ""
    equation.set("")

def delete_char():
    global exp
    exp = exp[:-1]
    equation.set(exp)

def sqrt():
    global exp
    try:
        result = str(math.sqrt(float(exp)))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def pi_value():
    global exp
    exp += str(math.pi)
    equation.set(exp)

def percentage():
    global exp
    try:
        result = str(float(exp) / 100)
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def log10():
    global exp
    try:
        result = str(math.log10(float(exp)))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def ln():
    global exp
    try:
        result = str(math.log(float(exp)))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def sin_func():
    global exp
    try:
        result = str(math.sin(math.radians(float(exp))))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def cos_func():
    global exp
    try:
        result = str(math.cos(math.radians(float(exp))))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def tan_func():
    global exp
    try:
        result = str(math.tan(math.radians(float(exp))))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def factorial_func():
    global exp
    try:
        result = str(math.factorial(int(float(exp))))
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""

def square_func():
    global exp
    try:
        result = str(float(exp)**2)
        equation.set(result)
        exp = result
    except:
        equation.set("Error")
        exp = ""


# ---------------- UI ---------------- #
root = Tk()
root.title("Smart Calculator")
root.geometry("420x620")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

equation = StringVar()
entry_frame = Frame(root, bg="#1e1e2f")
entry_frame.pack(expand=True, fill="both")

txt = Entry(entry_frame, textvariable=equation, font=("Arial", 28), bg="#2e2e3f", fg="white",
            bd=0, justify='right', insertbackground="white")
txt.pack(ipady=15, pady=20, padx=10, fill="x")

# Button creation helper
def create_button(text, command, row, col, bg="#33334d", fg="white"):
    btn = Button(btn_frame, text=text, fg=fg, bg=bg, command=command,
                 font=("Arial", 16, "bold"), height=2, width=6, bd=0, relief="flat")
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Enter>", lambda e: btn.config(bg="#44445e"))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg))
    return btn

btn_frame = Frame(root, bg="#1e1e2f")
btn_frame.pack()

# Row 1
create_button("C", clear, 0, 0, "#ff4d4d")
create_button("⌫", delete_char, 0, 1)
create_button("(", lambda: press("("), 0, 2)
create_button(")", lambda: press(")"), 0, 3)

# Row 2
create_button("7", lambda: press("7"), 1, 0)
create_button("8", lambda: press("8"), 1, 1)
create_button("9", lambda: press("9"), 1, 2)
create_button("/", lambda: press("/"), 1, 3, "#ff9933")

# Row 3
create_button("4", lambda: press("4"), 2, 0)
create_button("5", lambda: press("5"), 2, 1)
create_button("6", lambda: press("6"), 2, 2)
create_button("*", lambda: press("*"), 2, 3, "#ff9933")

# Row 4
create_button("1", lambda: press("1"), 3, 0)
create_button("2", lambda: press("2"), 3, 1)
create_button("3", lambda: press("3"), 3, 2)
create_button("-", lambda: press("-"), 3, 3, "#ff9933")

# Row 5
create_button("0", lambda: press("0"), 4, 0)
create_button(".", lambda: press("."), 4, 1)
create_button("%", percentage, 4, 2)
create_button("+", lambda: press("+"), 4, 3, "#ff9933")

# Row 6 (Scientific)
create_button("√", sqrt, 5, 0)
create_button("x²", square_func, 5, 1)
create_button("π", pi_value, 5, 2)
create_button("=", equal_press, 5, 3, "#00cc99")

# Row 7 (Advanced)
create_button("sin", sin_func, 6, 0)
create_button("cos", cos_func, 6, 1)
create_button("tan", tan_func, 6, 2)
create_button("log", log10, 6, 3)

# Row 8
create_button("ln", ln, 7, 0)
create_button("!", factorial_func, 7, 1)

# ---------------- Run App ---------------- #
root.mainloop()
