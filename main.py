import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#E8F9FD"
BROWN = '#876445'
timer = None


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    if count > 0:
        global timer
        timer = window.after(1000, counter, count - 1)
    else:
        # Cancel the timer after 10 seconds
        window.after_cancel(timer)

        # Clear the entered text
        text_area.delete(1.0, 'end')


def reset_timer():
    # Cancel the timer
    window.after_cancel(timer)


def click(key):
    # print the key that was pressed
    try:
        reset_timer()
    except ValueError:
        pass
    counter(5)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Disappearing Text Writing App")
window.minsize(width=800, height=200)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

# Show app name
app_name = tk.Label(window, text="Disappearing Text Writing App", font=('Arial', 20, 'italic'), fg=BROWN, bg=BACKGROUND_COLOR)
app_name.grid(column=0, row=0, columnspan=4, sticky='we')

text_area = tk.Text(window, width=90, height=8, font=('Arial', 14, 'bold'))
text_area.grid(column=0, row=1, columnspan=4)
# Bind entry to any keypress
text_area.bind("<Key>", click)


window.mainloop()