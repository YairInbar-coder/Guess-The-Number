import customtkinter as ctk
import random


ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

def temporery_label(parent, text, duration_ms=1000):
    label = ctk.CTkLabel(parent, text=text)
    label.place(x=114, y=152)
    parent.after(duration_ms, label.destroy)
    return label

def check_guess(guess, number):
    if guess == number:
        return "Correct!"
    elif guess < number:
        return "Too low!"
    else:
        return "Too high!"

def main():
    app = ctk.CTk()
    app.title("Guess The Number")
    app.geometry('400x250')
    number = random.randint(1, 100)
    label = ctk.CTkLabel(app, text="Guess The Number between 1 and 100")
    label.pack(pady= 30)

    text = ctk.CTkTextbox(app, height=30, width=50, fg_color='darkgray')
    text.place(x=175, y=90)

    #guess_number = int(text.get("0.0", "end-1c").strip())

     

    enter = ctk.CTkButton(app, text="Enter", command=lambda: 
    temporery_label(app, check_guess(int(text.get("0.0", "end-1c").strip()) if text.get("0.0", "end-1c").strip().isdigit() else "Invalid Input", number)))
    enter.place(x=175, y=150)

    app.mainloop()

if __name__ == "__main__":
    main()
