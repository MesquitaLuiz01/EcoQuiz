import customtkinter as ctk
import valida

# As estruturas das funções são repetidas até o fim das perguntas e dos textos

def pergunta_1(app, label, btn):
    # Label e botão anteriores são apagados
    label.pack_forget()
    btn.pack_forget()

    # label novo com a pergunta
    label_2 = ctk.CTkLabel(
        app,
        text='A Amazônia é a maior floresta tropical do mundo, cobrindo boa parte do Brasil, e outras partes da América do Sul, ela abriga milhares de espécies de plantas e animais, e ainda ajuda no equilíbrio climático do planeta. Apesar disso enfrenta diversos riscos em relação a sua preservação.\n\nQuais são esses riscos?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    # lista com alternativas da pergunta
    alternativas = [
        "Desmatamento, mudanças climáticas, poluição sonora\n e aumento do turismo.",
        "Desmatamento, queimadas, expansão agropecuária e\n mineração ilegal.",
        "Derretimento das geleiras, poluição dos oceanos,\n urbanização e pesca predatória.",
        "Aumento da biodiversidade, reflorestamento em massa,\n redução da pecuária e crescimento sustentável."
    ]

    resposta_correta = "Desmatamento, queimadas, expansão agropecuária e\n mineração ilegal."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    
    # frame para organizar os botões das alternativas na esquerda da tela
    # Quando o frame fica junto com a parte 'botões de cada alternativa sendo criados' fica um espaço muito grande entre a pergunta e os botões, não sei o motivo do por que
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    # função que valida a resposta e tranca os botões
    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p1(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p1(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    # botões de cada alternativa sendo criados
    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()
    
def pergunta_2(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='A água é um recurso natural essencial para a vida de todos os seres vivos. Ela está presente em rios, lagos, oceanos e no subsolo, sendo usada para beber, produzir alimentos e gerar energia. Apesar de abundante, a água potável é limitada e deve ser usada com consciência para evitar o desperdício.\n\nPor que é importante usar a água de forma consciente, mesmo sendo um recurso abundante na natureza?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Porque a maior parte da água disponível é salgada\n e não pode ser consumida diretamente.",
        "Porque o desperdício de água aumenta o preço desse\n recurso no mercado..",
        "Porque a água potável é limitada e essencial para\n a sobrevivência dos seres vivos.",
        "Porque os governos multam quem gasta água além do\n limite permitido."
    ]

    resposta_correta = "Porque a água potável é limitada e essencial para\n a sobrevivência dos seres vivos."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p2(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p2(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

def pergunta_3(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='Reciclagem é o processo de transformar materiais usados em novos produtos. Ela ajuda a reduzir o lixo, economizar recursos naturais e diminuir a poluição. Reciclar papel, plástico, vidro e metal é uma forma de cuidar do meio ambiente.\n\nPor que a reciclagem é importante para o meio ambiente?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Porque aumenta a quantidade de lixo\n nos aterros sanitários.",
        "Porque reduz o desperdício de materiais, economiza\n recursos naturais e diminui a poluição.",
        "Porque torna os produtos mais caros para\n os consumidores.",
        "Porque elimina completamente a necessidade\n de extração de novos recursos."
    ]

    resposta_correta = "Porque reduz o desperdício de materiais, economiza\n recursos naturais e diminui a poluição."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p3(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p3(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

def pergunta_4(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='As mudanças climáticas são alterações no clima da Terra causadas, em grande parte, pelas atividades humanas. O aumento da emissão de gases poluentes intensifica o efeito estufa, aquecendo o planeta. Isso provoca secas, enchentes, derretimento das calotas polares e desequilíbrios ecossistêmicos.\n\nAlém do aquecimento global direto, qual é um dos efeitos indiretos das mudanças climáticas que pode desencadear um ciclo de retroalimentação positiva (feedback loop), agravando ainda mais o problema?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Aumento da fotossíntese vegetal devido ao excesso de CO₂,\n que sequestra mais carbono da atmosfera.",
        "Derretimento do permafrost, liberando metano armazenado\n — um gás do efeito estufa ainda mais potente que o CO₂.",
        "Redução da atividade industrial em países desenvolvidos,\n diminuindo temporariamente as emissões.",
        "Crescimento acelerado de florestas tropicais, compensando\n as emissões humanas."
    ]

    resposta_correta = "Derretimento do permafrost, liberando metano armazenado\n — um gás do efeito estufa ainda mais potente que o CO₂."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p4(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p4(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

def pergunta_5(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='Microplásticos (partículas <5mm) já foram encontrados no ar, água potável e até em órgãos humanos. Eles absorvem poluentes químicos e podem entrar na cadeia alimentar.\n\n\nQual medida é mais eficaz para reduzir microplásticos nos oceanos?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Proibir apenas sacolas plásticas em supermercados.",
        "Substituir garrafas PET por vidro em todos os países.",
        "Remover manualmente os plásticos das praias.",
        "Instalar filtros em lavadoras de roupas\n(fonte de fibras sintéticas)."
    ]

    resposta_correta = "Instalar filtros em lavadoras de roupas\n(fonte de fibras sintéticas)."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p5(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p5(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

def pergunta_6(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='A economia circular propõe a reutilização infinita de materiais, diferentemente do modelo linear (extrair-produzir-descartar). Vidro e alumínio são exemplos de materiais 100% recicláveis, mas plásticos têm taxa de reciclagem global de apenas 9%.\n\n\nPor que a reciclagem de plásticos é menos eficiente que a de vidro e alumínio?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Plásticos se degradam quimicamente após o primeiro\nuso, perdendo qualidade.",
        "Existem mais de 7 tipos de plásticos, e misturá-los\ninviabiliza a reciclagem.",
        "O processo consome mais energia que a produção den\nplástico virgem",
        "Todas as alternativas anteriores estão corretas."
    ]

    resposta_correta = "Todas as alternativas anteriores estão corretas."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p6(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p6(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

def pergunta_7(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='Cidades como São Paulo podem ter temperaturas 5°C mais altas que áreas rurais próximas. Isso se deve ao asfalto, concreto e falta de vegetação, que absorvem calor, somado à poluição do ar que retém radiação.\n\n\nQual medida NÃO é eficaz para reduzir ilhas de calor urbanas?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Pintar telhados de branco para refletir luz solar.",
        "Expandir parques lineares ao longo de rios e avenidas.",
        "Substituir árvores por palmeiras, que consomem menos água.",
        "Criar corredores de ventilação entre prédios."
    ]

    resposta_correta = "Substituir árvores por palmeiras, que consomem menos água."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p7(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p7(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

def pergunta_8(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='Abelhas e outros polinizadores são responsáveis por 75% das culturas agrícolas globais. Seu declínio está ligado a agrotóxicos (como neonicotinoides), perda de habitat e mudanças climáticas.\n\n\nQual ação individual contribui MAIS para a proteção de polinizadores?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Comprar mel orgânico de produtores locais.",
        "Plantar flores nativas no jardim ou em vasos.",
        "Eliminar todos os insetos vistos próximos a residências.",
        "Usar apenas pesticidas 'verdes' em hortas caseiras."
    ]

    resposta_correta = "Plantar flores nativas no jardim ou em vasos."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p8(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p8(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

def pergunta_9(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='Sustentabilidade é um conceito que busca o equilíbrio entre o crescimento econômico, a preservação ambiental e o bem-estar social. Ela propõe um modelo de desenvolvimento que atenda às necessidades do presente sem comprometer as gerações futuras, através de práticas mais conscientes e responsáveis.\n\n\nQual das ações abaixo está alinhada com o princípio da sustentabilidade?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Explorar ao máximo os recursos naturais disponíveis.",
        "Incentivar o consumo desenfreado para movimentar a\n economia.",
        "Priorizar sempre o lucro das empresas, independentemente\n do impacto ambiental.",
        "Promover o uso racional de recursos e energia."
    ]

    resposta_correta = "Promover o uso racional de recursos e energia."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p9(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p9(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

def pergunta_10(app, label, btn):
    label.pack_forget()
    btn.pack_forget()

    label_2 = ctk.CTkLabel(
        app,
        text='O efeito estufa é um fenômeno natural e essencial para a manutenção da temperatura da Terra. No entanto, com o aumento da emissão de gases como o dióxido de carbono (CO₂) devido à atividade humana, esse fenômeno tem se intensificado, causando mudanças climáticas e aquecimento global.\n\n\nQual das atividades humanas mais contribui para o agravamento do efeito estufa?',
        font=('impact', 23),
        wraplength=700,
        justify='left',
    )
    label_2.pack(pady=10)

    alternativas = [
        "Queima de combustíveis fósseis em veículos e indústrias.",
        "Uso de bicicletas como transporte principal",
        "Plantio de florestas para recuperação de áreas degradadas.",
        "Construção de casas sustentáveis com materiais ecológicos."
    ]

    resposta_correta = "Queima de combustíveis fósseis em veículos e indústrias."

    resultado = ctk.CTkLabel(app, text="", font=('impact', 20))
    resultado.pack(pady=5)
    
    frame_alternativas = ctk.CTkFrame(app, fg_color="transparent")
    frame_alternativas.pack(pady=10, padx=50, anchor='w')

    def validar_resposta(resposta):
        if resposta == resposta_correta:
            resultado.configure(text="Resposta correta!", text_color="green")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.acertou_p10(app, label_2, btn_continuar)))   
        
        else:
            resultado.configure(text="Resposta incorreta!", text_color="red")
            btn_continuar.configure(
                command=lambda: (
                label_2.pack_forget(),
                resultado.pack_forget(),
                btn_continuar.pack_forget(),
                frame_alternativas.pack_forget(),
                valida.errou_p10(app, label_2, btn_continuar)
            )
        )
        btn_continuar.pack(pady=10)
        btn_continuar.configure(state="normal")
        #botões sendo trancados
        for btn in botoes_alternativas:
            btn.configure(state="disabled")

    botoes_alternativas = []

    for alternativa in alternativas:
        btn_alt = ctk.CTkButton(
            frame_alternativas,
            text=alternativa,
            font=('impact', 20),
            width=500,
            anchor='w',
            command=lambda alt=alternativa: validar_resposta(alt)
        )
        btn_alt.pack(pady=5)
        botoes_alternativas.append(btn_alt)

    # Botão para continuar
    btn_continuar = ctk.CTkButton(
        app,
        text="Continuar",
        font=('impact', 20),
        state="disabled",)
    btn_continuar.pack_forget()

