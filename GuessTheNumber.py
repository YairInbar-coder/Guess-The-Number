import customtkinter as ctk
import random


ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

def temporery_label(parent, text, duration_ms=1000):
    label = ctk.CTkLabel(parent, text=text)
    label.place(x=89, y=152)
    parent.after(duration_ms, label.destroy)
    return label

def main():
    app = ctk.CTk()
    app.title("Guess The Number")
    app.geometry('400x250')

    number = random.randint(1, 100)

    attempt = 0

    def handle_click():
        nonlocal number
        nonlocal attempt

        user_input = text.get("0.0", "end-1c").strip()

        def delete():
            text.delete('0.0', 'end-1c')
        
        if user_input.isdigit():
            guess = int(user_input)

        if guess == number:
            temporery_label(app, f'{user_input} Is Correct!')
            number = random.randint(1, 100)
            delete()
            attempt = -1
        elif attempt == 4:
            temporery_label(app, f'To Many Attempts')
            delete()
            attempt = -1
            number = random.randint(1, 100)
        elif guess < number:
            temporery_label(app, f'{user_input} Is Too low!')
            delete()
        else:
            temporery_label(app, f'{user_input} Is Too high!')
            delete()
        
        attempt += 1
        attempt_count.configure(text=f'Attempts: {attempt}')

    label = ctk.CTkLabel(app, text="Guess The Number between 1 and 100")
    label.pack()

    attempt_count = ctk.CTkLabel(app, text=f'Attempts: {attempt}')
    attempt_count.pack(pady=10)

    text = ctk.CTkTextbox(app, height=30, width=50, fg_color='darkgray')
    text.place(x=175, y=90)

    enter = ctk.CTkButton(app, text="Enter", width=60, command=handle_click)
    enter.place(x=200, y=150)

    app.mainloop()

if __name__ == "__main__":
    main()
