from graphics import Point, Image
from colisao import criar_area_colisao

def carregar_sprites(vw):

    #========= POSIÇÕES E BACKGROUND =========
    wx = vw.getWidth() / 2
    wy = vw.getHeight() / 2

    bg = Image(Point(wx, wy), "Sprites/Background.png")

    pos1 = Point(484, 404)
    pos2 = Point(1400, 404)

    Image(pos1, "Sprites/red_up.png")
    Image(pos2, "Sprites/blue_up.png")

    # ========= HUD – Vidas / Munição =========
    life_red = [
        Image(Point(50,  50), "Sprites/life1_true.png"),
        Image(Point(125, 50), "Sprites/life1_true.png"),
        Image(Point(200, 50), "Sprites/life2_true.png")
    ]

    ammo_red = [
        Image(Point(50,  125), "Sprites/slot1_true.png"),
        Image(Point(125, 125), "Sprites/slot1_true.png"),
        Image(Point(200, 125), "Sprites/slot1_true.png")
    ]

    life_blue = [
        Image(Point(1870, 50), "Sprites/life2_true.png"),
        Image(Point(1795, 50), "Sprites/life2_true.png"),
        Image(Point(1720, 50), "Sprites/life2_true.png")
    ]

    ammo_blue = [
        Image(Point(1870, 125), "Sprites/slot2_true.png"),
        Image(Point(1795, 125), "Sprites/slot2_true.png"),
        Image(Point(1720, 125), "Sprites/slot2_true.png")
    ]

    bg.draw(vw)
    for spr in life_red:  spr.draw(vw)
    for spr in ammo_red:  spr.draw(vw)
    for spr in life_blue: spr.draw(vw)
    for spr in ammo_blue: spr.draw(vw)

    #========= SPRITES DAS BALAS =========
    def criar_balas(qtd, prefixo):
        dirs = ["up", "down", "left", "right"]
        balas = {d: [] for d in dirs}

        for d in dirs:
            for _ in range(qtd):
                balas[d].append(
                    Image(Point(-9999, -9999), f"Sprites/{prefixo}_{d}.png")
                )
        return balas

    QTD = 5
    bllt1 = criar_balas(QTD, "bul1")
    bllt2 = criar_balas(QTD, "bul2")

    for L in bllt1.values():
        for b in L:
            b.draw(vw)

    for L in bllt2.values():
        for b in L:
            b.draw(vw)

    #========= LIFE PICKUP =========
    life_pickup = Image(Point(-9999, -9999), "Sprites/life.png")
    life_pickup.draw(vw)

    #========= AMMO PICKUP =========
    ammo_pickup = Image(Point(-9999, -9999), "Sprites/ammunition.png")
    ammo_pickup.draw(vw)

    #========= SPRITES DOS TANQUES =========
    sprit1 = {
        "up":    Image(pos1, "Sprites/red_up.png"),
        "down":  Image(Point(-9999, -9999), "Sprites/red_down.png"),
        "left":  Image(Point(-9999, -9999), "Sprites/red_left.png"),
        "right": Image(Point(-9999, -9999), "Sprites/red_right.png")
    }

    sprit2 = {
        "up":    Image(pos2, "Sprites/blue_up.png"),
        "down":  Image(Point(-9999, -9999), "Sprites/blue_down.png"),
        "left":  Image(Point(-9999, -9999), "Sprites/blue_left.png"),
        "right": Image(Point(-9999, -9999), "Sprites/blue_right.png")
    }

    for spr in sprit1.values(): spr.draw(vw)
    for spr in sprit2.values(): spr.draw(vw)

    #========= SPRITES DOS OBSTÁCULOS =========
    casa_x = vw.getWidth() / 2
    casa_y = vw.getHeight() / 2
    casa_pos = Point(casa_x, casa_y)
    
    pedra1_x = vw.getWidth() - 300
    pedra1_y = vw.getHeight() - 300
    pedra1_pos = Point(pedra1_x, pedra1_y)
    
    pedra2_x = 300
    pedra2_y = 300
    pedra2_pos = Point(pedra2_x, pedra2_y)
    
    casa_sprite = Image(casa_pos, "Sprites/obstaculo.png")
    pedra1_sprite = Image(pedra1_pos, "Sprites/pedra.png")
    pedra2_sprite = Image(pedra2_pos, "Sprites/pedra.png")
    
    casa_sprite.draw(vw)
    pedra1_sprite.draw(vw)
    pedra2_sprite.draw(vw)
    
    casa_colisao = criar_area_colisao(casa_sprite, "casa", 150, 150)
    pedra1_colisao = criar_area_colisao(pedra1_sprite, "pedra1", 90, 90)
    pedra2_colisao = criar_area_colisao(pedra2_sprite, "pedra2", 90, 90)
    
    obstaculos = [casa_colisao, pedra1_colisao, pedra2_colisao]
    
    #========= RETORNO =========
    return (bg, bllt1, bllt2, sprit1, sprit2,
 life_red, life_blue, ammo_red, ammo_blue, life_pickup, ammo_pickup, obstaculos)