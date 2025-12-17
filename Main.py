#========= IMPORTAÇÕES =========
from graphics import *
from Sprites import *
from Playerone import *
from Playertwo import *
import Bulletone as BO
import Bullettwo as BT
from habilidades import *
from Sounds import *
from colisao import *
from menu import *
import time
import sys

#========= JANELA DO JOGO =========
vw = GraphWin("WarTanks", 1920, 1080)
vw.master.attributes("-fullscreen", True)

#========= FUNÇÃO PARA REINICIAR O JOGO =========
def reiniciar_jogo():

    for item in vw.items[:]:
        item.undraw()

    try:
        vw.master.unbind("<KeyPress>")
        vw.master.unbind("<KeyRelease>")
    except:
        pass
    
    BO.ammo1 = BO.max_ammo1
    BO.rel1 = False
    BO.rel_sta1 = 0
    BO.bullet1 = []
    
    BT.ammo2 = BT.max_ammo2
    BT.rel2 = False
    BT.rel_sta2 = 0
    BT.bullet2 = []
    
    escolha = menu_inicial(vw)
    if escolha == 'EXIT':
        vw.close()
        sys.exit()

    for item in vw.items[:]:
        item.undraw()
    
    iniciar_partida()

#========= FUNÇÃO PARA INICIAR UMA PARTIDA =========
def iniciar_partida():

    #========= LIMPAR TELA DO MENU =========
    for item in vw.items[:]:
        item.undraw()

    #========= TECLAS =========
    keys = set()

    def key_press(e): 
        keys.add(e.keysym)

    def key_release(e): 
        keys.discard(e.keysym)

    vw.master.bind("<KeyPress>", key_press)
    vw.master.bind("<KeyRelease>", key_release)

    #========= CARREGAR SPRITES =========
    (bg, bllt1, bllt2, sprit1, sprit2,
    life_red, life_blue, ammo_red, ammo_blue,
    life_pickup, ammo_pickup, obstaculos
    ) = carregar_sprites(vw)

    #========= ESTADO INICIAL =========
    vidas_red = 3
    vidas_blue = 3
    cooldown_red = 0
    cooldown_blue = 0


    last_ammo1 = BO.ammo1
    last_ammo2 = BT.ammo2

    dir1 = "up"
    dir2 = "up"

    life_timer = 0
    LIFE_INTERVAL = 600
    life_active = False

    tocar_tema()
    #========= LOOP PRINCIPAL =========
    while not vw.isClosed():

        # ===== COOLDOWN SEMPRE ATUALIZANDO =====
        if cooldown_red > 0:
            cooldown_red -= 1

        if cooldown_blue > 0:
            cooldown_blue -= 1

        #========= MOVIMENTAÇÃO DOS JOGADORES =========
        dir_antes1 = dir1
        dir_antes2 = dir2
        
        tanque1_antes = get_active_sprite1(sprit1)
        tanque2_antes = get_active_sprite2(sprit2)

        pos1_antes = tanque1_antes.getAnchor() if tanque1_antes else None
        pos2_antes = tanque2_antes.getAnchor() if tanque2_antes else None

        #========= ATUALIZAR MOVIMENTO DOS JOGADORES =========
        dir1 = mov_pl1(vw, sprit1, dir1, keys)
        dir2 = mov_pl2(vw, sprit2, dir2, keys)

        #========= OBSTÁCULOS =========
        tanque1 = get_active_sprite1(sprit1)
        tanque2 = get_active_sprite2(sprit2)
        
        #========= VERIFICAR COLISÕES COM OBSTÁCULOS =========
        colisao_obstaculo1, obstaculo1 = verificar_colisao_tanque_obstaculo(tanque1, obstaculos)
        colisao_obstaculo2, obstaculo2 = verificar_colisao_tanque_obstaculo(tanque2, obstaculos)
        
        #========= CORRIGIR COLISÕES COM OBSTÁCULOS =========
        if colisao_obstaculo1:
            corrigir_colisao_tanque_obstaculo(tanque1, obstaculo1, dir1)
        
        if colisao_obstaculo2:
            corrigir_colisao_tanque_obstaculo(tanque2, obstaculo2, dir2)
        
        #========= CORRIGIR COLISÃO ENTRE TANQUES =========
        colisao_tanques = verificar_colisao_tanques(tanque1, tanque2)
        if colisao_tanques:
            corrigir_colisao_tanque_tanque(tanque1, tanque2, dir1, dir2)

        #========= TIRO PLAYER 1 (tecla E) =========
        if "e" in keys or "E" in keys:
            BO.sh_bul1(bllt1, sprit1[dir1], dir1)

        #========= MOVIMENTO / COLISÃO DAS BALAS DO PLAYER 1 =========
        hit_blue = BO.mov_bul1(vw, sprit2)
        BO.sta_rel1(keys)

        #========= Verifica colisão das balas do player 1 com obstáculos =========
        for bala in BO.bullet1[:]:
            colisao_bala, obstaculo = verificar_colisao_bala_obstaculo(bala["sprite"], obstaculos)
            if colisao_bala:
                x = bala["sprite"].getAnchor().x
                y = bala["sprite"].getAnchor().y
                bala["sprite"].move(-9999 - x, -9999 - y)
                BO.bullet1.remove(bala)

        #========= SE O PLAYER BLUE FOR ATINGIDO =========
        if hit_blue and cooldown_blue == 0:
            vidas_blue -= 1
            cooldown_blue = 30

            if 0 <= vidas_blue < len(life_blue):
                life_blue[vidas_blue].undraw()
                false_img = Image(life_blue[vidas_blue].getAnchor(), "Sprites/life2_false.png")
                false_img.draw(vw)
                life_blue[vidas_blue] = false_img

            if vidas_blue <= 0:
                #========= Tanque azul perdeu (vermelho venceu) =========
                parar_tema()
                resultado = tela_vitoria_vermelho(vw)
                
                if resultado == "RESTART":
                    reiniciar_jogo()
                    return
                elif resultado == "EXIT":
                    vw.close()
                    sys.exit()
                
                break

        #========= TIRO PLAYER 2 (tecla 7) =========
        if "7" in keys:
            BT.sh_bul2(bllt2, sprit2[dir2], dir2)

        #========= MOVIMENTO / COLISÃO DAS BALAS DO PLAYER 2 =========
        hit_red = BT.mov_bul2(vw, sprit1)
        BT.sta_rel2(keys)

        #========= Verifica colisão das balas do player 2 com obstáculos =========
        for bala in BT.bullet2[:]:
            colisao_bala, obstaculo = verificar_colisao_bala_obstaculo(bala["sprite"], obstaculos)
            if colisao_bala:
                #==== Remove a bala =====
                x = bala["sprite"].getAnchor().x
                y = bala["sprite"].getAnchor().y
                bala["sprite"].move(-9999 - x, -9999 - y)
                BT.bullet2.remove(bala)

        #========= SE O PLAYER RED FOR ATINGIDO =========
        if hit_red and cooldown_red == 0:
            vidas_red -= 1
            cooldown_red = 30

            if 0 <= vidas_red < len(life_red):
                life_red[vidas_red].undraw()
                false_img = Image(life_red[vidas_red].getAnchor(), "Sprites/life1_false.png")
                false_img.draw(vw)
                life_red[vidas_red] = false_img

            if vidas_red <= 0:
                #========= Tanque vermelho perdeu (azul venceu) =========
                parar_tema()
                resultado = tela_vitoria_azul(vw)
                
                if resultado == "RESTART":
                    reiniciar_jogo()
                    return
                elif resultado == "EXIT":
                    vw.close()
                    sys.exit()
                
                break
        #======== AMMO PICKUP =========
        atualizar_ammo_pickup(vw, ammo_pickup, sprit1, sprit2
        )

        #========= VIDA PICKUP =========
        vidas_red, vidas_blue = atualizar_vida_pickup(
            vw,
            life_pickup,
            sprit1, sprit2,
            life_red, life_blue,
            vidas_red, vidas_blue
        )

        #========= ATUALIZAR HUD — AMMO PLAYER 1 =========
        if BO.ammo1 != last_ammo1:

            if BO.ammo1 < last_ammo1:
                idx = BO.ammo1

                if 0 <= idx < len(ammo_red):
                    posicoes_red = [
                        Point(50, 125),
                        Point(125, 125),
                        Point(200, 125)
                    ]

                    ammo_red[idx].undraw()
                    false_img = Image(posicoes_red[idx], "Sprites/slot1_false.png")
                    false_img.draw(vw)
                    ammo_red[idx] = false_img

        #========= ATUALIZAR HUD — AMMO PLAYER 2 =========
        if BT.ammo2 != last_ammo2:

            if BT.ammo2 < last_ammo2:
                idx = BT.ammo2

                if 0 <= idx < len(ammo_blue):
                    posicoes_blue = [
                        Point(1870, 125),
                        Point(1795, 125),
                        Point(1720, 125)
                    ]

                    ammo_blue[idx].undraw()
                    false_img = Image(posicoes_blue[idx], "Sprites/slot2_false.png")
                    false_img.draw(vw)
                    ammo_blue[idx] = false_img

        #========= RECARREGAR HUD PLAYER 1 =========
        if BO.ammo1 == BO.max_ammo1 and last_ammo1 < BO.max_ammo1:

            posicoes_red = [
                Point(50, 125),
                Point(125, 125),
                Point(200, 125)
            ]

            for i in range(len(ammo_red)):
                ammo_red[i].undraw()
                img = Image(posicoes_red[i], "Sprites/slot1_true.png")
                img.draw(vw)
                ammo_red[i] = img

        #========= RECARREGAR HUD PLAYER 2 =========
        if BT.ammo2 == BT.max_ammo2 and last_ammo2 < BT.max_ammo2:

            posicoes_blue = [
                Point(1870, 125),
                Point(1795, 125),
                Point(1720, 125)
            ]

            for i in range(len(ammo_blue)):
                ammo_blue[i].undraw()
                img = Image(posicoes_blue[i], "Sprites/slot2_true.png")
                img.draw(vw)
                ammo_blue[i] = img

        #========= SINCRONIZAR last_ammo NO FINAL DO FRAME =========
        last_ammo1 = BO.ammo1
        last_ammo2 = BT.ammo2

        #========= ATUALIZAR TELA =========
        update()
        time.sleep(0.016)
        
#========= INICIAR O JOGO =========
escolha = menu_inicial(vw)
if escolha == 'EXIT':
    vw.close()
    sys.exit()

for item in vw.items[:]:
    item.undraw()

iniciar_partida()