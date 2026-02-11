import customtkinter as ctk
from customtkinter import ctk2
import random



def temporery_label(parent, text, duration_ms=7500):
    label = ctk2.CTkLabel(parent, text=random.randint(1, 10))
    label.pack()
    parent.after(duration_ms, label.destroy)
    return label
def main():
    app = ctk.CTk()
    app.title("Guess The Number")
    app.geometry('500x650')

    frame = ctk2.CTkFrame(app)
    frame.pack()

    app.mainloop()

if __name__ == "__main__":
    main()
