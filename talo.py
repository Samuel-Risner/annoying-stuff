from tkinter import Tk, Button, PhotoImage, TclError
import random

from pynput.mouse import Controller

if __name__ == "__main__":
    root = Tk()
    root.attributes("-topmost", True)
    root.config(bg="white", bd=0, highlightthickness=0)
    root.attributes('-fullscreen',True)
    # root.overrideredirect(True)
    root.withdraw()

    SCREEN_WIDTH = root.winfo_screenwidth()
    SCREEN_HEIGHT = root.winfo_screenheight()
    AUS_X = SCREEN_WIDTH - SCREEN_WIDTH / 8
    AUS_Y = SCREEN_HEIGHT / 20
    BUTTON_WIDTH = 5
    BUTTON_HEIGHT = 5

    def get_button_pos() -> tuple[int, int]:
        return random.randint(0, SCREEN_WIDTH - BUTTON_WIDTH), random.randint(0, SCREEN_HEIGHT - BUTTON_HEIGHT)

    pixel = PhotoImage(width=1, height=1)
    mouse = Controller()
    random.seed()

    while True:
        x, y = mouse.position
        if (x > AUS_X) and (y < AUS_Y):
            root.deiconify()

            button = Button(root, text="", image=pixel, command=root.quit, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, compound="c", padx=0, pady=0, border=0, highlightthickness=0, bg="white")
            x2, y2 = get_button_pos()
            button.place(x=x2, y=y2)
            mouse.move(x2-x+int(BUTTON_WIDTH/2), y2-y+int(BUTTON_HEIGHT/2))

            root.mainloop()

            try:
                button.destroy()
                root.withdraw()
            except TclError:
                break