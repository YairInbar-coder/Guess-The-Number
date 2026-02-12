import customtkinter as ctk
import random


ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

def temporery_label(parent, text, duration_ms=1000):
    label = ctk.CTkLabel(parent, text=random.randint(1, 10))
    label.place(x=126, y=152)
    parent.after(duration_ms, label.destroy)
    return label
def main():
    app = ctk.CTk()
    app.title("Guess The Number")
    app.geometry('400x250')

    label = ctk.CTkLabel(app, text="Guess The Number between 1 and 10")
    label.pack(pady= 30)

    text = ctk.CTkTextbox(app, height=30, width=50, fg_color='darkgray')
    text.place(x=175, y=90)

    enter = ctk.CTkButton(app, text="Enter", command=lambda: temporery_label(app, text.get("0.0", "end-1c")))
    enter.place(x=175, y=150)

    app.mainloop()

if __name__ == "__main__":
    main()
    