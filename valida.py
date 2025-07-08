import customtkinter as ctk
import perguntas
import nota

def nota_final(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text= f'Sua nota final foi de {nota.pontos} pontos', font=('impact', 30))
    label_2.pack(pady=105)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: fim(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def fim(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='Feito por:\nLuiz Augusto Souza de Mesquita\nIsaque de Araújo do Nascimento\nDavi Santos de Almeida Xavier\nDavi Marques dos Santos', font=('impact', 30))
    label_2.pack(pady=25)
    
    #Botão para fechar o jogo
    btn = ctk.CTkButton(
        master=app,
        text="Sair do Jogo",
        font=('Impact', 25),
        command=app.destroy
    )
    btn.pack(pady=200)

#----pergunta_1----#
def errou_p1(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a primeira questão\n\n\nA resposta correta era "Desmatamento, queimadas, expansão agropecuária e mineração ilegal."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_2(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
   
def acertou_p1(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 20),
                                  command=lambda: perguntas.pergunta_2(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1

#----pergunta_2----#
def errou_p2(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a segunda questão\n\n\nA resposta correta era "Porque a água potável é limitada e essencial para a sobrevivência dos seres vivos."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_3(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p2(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_3(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1
    
#----pergunta_3----#
def errou_p3(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a terceira questão\n\n\nA resposta correta era "Porque reduz o desperdício de materiais, economiza recursos naturais e diminui a poluição."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_4(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p3(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_4(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1

#----pergunta_4----#
def errou_p4(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a quarta questão\n\n\nA resposta correta era "Derretimento do permafrost, liberando metano armazenado — um gás do efeito estufa ainda mais potente que o CO₂."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_5(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p4(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_5(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1
    
#----pergunta_5----#
def errou_p5(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a quinta questão\n\n\nA resposta correta era "Instalar filtros em lavadoras de roupas (fonte de fibras sintéticas)."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_6(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p5(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_6(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1
    
#----pergunta_6----#
def errou_p6(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a sexta questão\n\n\nA resposta correta era "Todas as alternativas anteriores estão corretas."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_7(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p6(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_7(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1

#----pergunta_7----#
def errou_p7(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a sétima questão\n\n\nA resposta correta era "Substituir árvores por palmeiras, que consomem menos água."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_8(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p7(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_8(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1

#----pergunta_8----#
def errou_p8(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a oitava questão\n\n\nA resposta correta era "Plantar flores nativas no jardim ou em vasos."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_9(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p8(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_9(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1

#----pergunta_9----#
def errou_p9(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a nona questão\n\n\nA resposta correta era "Promover o uso racional de recursos e energia."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_10(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p9(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: perguntas.pergunta_10(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1

#----pergunta_10----#
def errou_p10(app, label, btn):
    label.pack_forget()
    btn.pack_forget()
    
    label_2 = ctk.CTkLabel(app, text='voce errou a décima questão\n\n\nA resposta correta era "Promover o uso racional de recursos e energia."',
                           wraplength=700,
                           justify='center',
                           font=('impact', 25),)
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: nota_final(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    
def acertou_p10(app, label, btn):
    
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(app, text='Parabéns, você acertou\n\n\nVocê ganhou 1 ponto', 
                           wraplength=700,
                           justify='center',
                           font=('impact', 25))
    label_2.pack(pady=20)

    btn_continuar = ctk.CTkButton(app, text="Continuar", font=('impact', 30),
                                  command=lambda: nota_final(app, label_2, btn_continuar))
    btn_continuar.pack(pady=10)
    nota.pontos +=1

