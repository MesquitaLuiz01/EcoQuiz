import customtkinter as ctk
import perguntas


ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('EcoQuiz')

label = ctk.CTkLabel(app,
                     text=('EcoQuiz\n\n\n'
                    'Olá, seja bem-vindo ao EcoQuiz\n um jogo de perguntas com tématica ambiental\n\n'),
                     
                     font=('Impact', 25),)
label.pack(pady=20)


btn = ctk.CTkButton(app, text="JOGAR", font=('Impact', 40),
                    command=lambda: perguntas.pergunta_1(app, label, btn))
btn.pack(pady=20)

app.geometry('900x700')
app.resizable(False, False)
app.configure(fg_color="#799447")
app.mainloop()
