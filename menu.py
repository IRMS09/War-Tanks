from graphics import *
import time

#========= ÁREA DE INTERAçÃO =========
def clique_na_area(px, py, x1, y1, x2, y2):
    return x1 <= px <= x2 and y1 <= py <= y2

#========= MENU INICIAL =========
def menu_inicial(janela):
    for item in janela.items[:]:
        item.undraw()
    
    janela.update()
    time.sleep(0.05)

    W = janela.getWidth()
    H = janela.getHeight()

    #========= TENTAR CARREGAR IMAGEM DE FUNDO =========
    try:
        img = Image(Point(W/2, H/2), "Sprites/menu.png")
        img.draw(janela)
        janela.update()
        
    #========= SE FALHAR, DESENHAR TELA SIMPLES =========
    except Exception as e:
        bg = Rectangle(Point(0, 0), Point(W, H))
        bg.setFill("darkblue")
        bg.draw(janela)
        
        #========= TÍTULO E BOTÕES =========
        titulo = Text(Point(W/2, H/4), "WAR TANKS")
        titulo.setSize(36)
        titulo.setFill("yellow")
        titulo.draw(janela)
        
        #========= BOTÕES =========
        btn_start = Rectangle(Point(800, 550), Point(1090, 650))
        btn_start.setFill("green")
        btn_start.draw(janela)
        txt_start = Text(Point(945, 600), "START GAME")
        txt_start.setSize(36)
        txt_start.setFill("white")
        txt_start.draw(janela)
        
        #========= BOTÃO EXIT =========
        btn_exit = Rectangle(Point(820, 805), Point(1095, 900))
        btn_exit.setFill("red")
        btn_exit.draw(janela)
        txt_exit = Text(Point(958, 853), "EXIT")
        txt_exit.setSize(24)
        txt_exit.setFill("white")
        txt_exit.draw(janela)
        
        #========= CRÉDITOS =========
        creditos = Text(Point(W/2, H - 50), "Created by: Pablo Farias and Izac Rios")
        creditos.setSize(18)
        creditos.setFill("lightgray")
        creditos.draw(janela)

    #========= ESPERAR INTERAÇÃO DO JOGADOR =========
    while True:
        #========= VERIFICAR TECLAS E CLIQUES =========
        try:

            tecla = janela.checkKey()
            if tecla == "Return" or tecla == "space":
                return "START"
            
            if tecla == "Escape":
                return "EXIT"

            clique = janela.checkMouse()
            if clique:
                px, py = clique.getX(), clique.getY()

                if clique_na_area(px, py, 800, 550, 1090, 650):
                    return "START"

                if clique_na_area(px, py, 820, 805, 1095, 900):
                    return "EXIT"

            time.sleep(0.01)

        #========= TRATAR ERRO DE GRÁFICOS =========
        except GraphicsError:
            
            return "EXIT"

#========= TELA DE VITÓRIA PLAYER 2 =========
def tela_vitoria_azul(janela):
    for item in janela.items[:]:
        item.undraw()
    
    janela.update()
    time.sleep(0.05)

    W = janela.getWidth()
    H = janela.getHeight()

    #======== TENTAR CARREGAR IMAGEM DE FUNDO =========
    try:
        img = Image(Point(W/2, H/2), "Sprites/blue_win.png")
        img.draw(janela)
        janela.update()
    
    #======== SE FALHAR, DESENHAR TELA SIMPLES =========
    except Exception as e:
        bg = Rectangle(Point(0, 0), Point(W, H))
        bg.setFill("blue")
        bg.draw(janela)
        
        #========= TÍTULO E INSTRUÇÕES =========
        titulo = Text(Point(W/2, H/3), "VICTORY!")
        titulo.setSize(36)
        titulo.setFill("yellow")
        titulo.setStyle("bold")
        titulo.draw(janela)

        #========= SUBTÍTULO =========
        subtitulo = Text(Point(W/2, H/2), "PLAYER 2 WINS!")
        subtitulo.setSize(24)
        subtitulo.setFill("white")
        subtitulo.setStyle("bold")
        subtitulo.draw(janela)

        #========= INSTRUÇÕES =========
        instrucoes = Text(Point(W/2, H * 2/3), "return - Restart Game\nESC - Exit Game")
        instrucoes.setSize(18)
        instrucoes.setFill("lightgray")
        instrucoes.setStyle("italic")
        instrucoes.draw(janela)

    #========= ESPERAR INTERAÇÃO DO JOGADOR =========
    while True:
        #========= VERIFICAR TECLAS E CLIQUES =========
        try:

            tecla = janela.checkKey()
            if tecla == "Return" or tecla == "space":
                return "RESTART"
            
            if tecla == "Escape":
                return "EXIT"

            time.sleep(0.01)

        #========= TRATAR ERRO DE GRÁFICOS =========
        except GraphicsError:

            return "EXIT"

#========= TELA DE VITÓRIA PLAYER 1 =========
def tela_vitoria_vermelho(janela):
    for item in janela.items[:]:
        item.undraw()
    
    janela.update()
    time.sleep(0.05)

    W = janela.getWidth()
    H = janela.getHeight()

    #======== TENTAR CARREGAR IMAGEM DE FUNDO =========
    try:
        img = Image(Point(W/2, H/2), "Sprites/red_win.png")
        img.draw(janela)
        janela.update()
    
    #======== SE FALHAR, DESENHAR TELA SIMPLES =========
    except Exception as e:
        bg = Rectangle(Point(0, 0), Point(W, H))
        bg.setFill("red")
        bg.draw(janela)
        
        #========= TÍTULO E INSTRUÇÕES =========
        titulo = Text(Point(W/2, H/3), "VICTORY!")
        titulo.setSize(72)
        titulo.setFill("yellow")
        titulo.setStyle("bold")
        titulo.draw(janela)
        
        #========= SUBTÍTULO =========
        subtitulo = Text(Point(W/2, H/2), "PLAYER 1 WINS!")
        subtitulo.setSize(48)
        subtitulo.setFill("white")
        subtitulo.setStyle("bold")
        subtitulo.draw(janela)

        #========= INSTRUÇÕES =========
        instrucoes = Text(Point(W/2, H * 2/3), "return - Restart Game\nESC - Exit Game")
        instrucoes.setSize(36)
        instrucoes.setFill("lightgray")
        instrucoes.setStyle("italic")
        instrucoes.draw(janela)

    #========= ESPERAR INTERAÇÃO DO JOGADOR =========
    while True:
        #========= VERIFICAR TECLAS E CLIQUES =========
        try:
            tecla = janela.checkKey()
            if tecla == "Return" or tecla == "space":
                return "RESTART"
            
            if tecla == "Escape":
                return "EXIT"

            time.sleep(0.01)

        #========= TRATAR ERRO DE GRÁFICOS =========
        except GraphicsError:

            return "EXIT"