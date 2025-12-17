from graphics import *
import time

#========= TROCA DE DIREÇÃO DO PLAYER 2 =========
def ch_dir2(sprites, dir_atual, dir_nova):

    if dir_atual == dir_nova:
        return dir_atual

    anchor = sprites[dir_atual].getAnchor()
    x, y = anchor.x, anchor.y

    sprites[dir_atual].move(-9999 - x, -9999 - y)

    nx = sprites[dir_nova].getAnchor().x
    ny = sprites[dir_nova].getAnchor().y
    sprites[dir_nova].move(x - nx, y - ny)

    return dir_nova


#========= MOVIMENTO DO PLAYER 2 =========
def mov_pl2(vw, sprites, dir_atual, keys):

    dir2 = dir_atual
    x = sprites[dir2].getAnchor().x
    y = sprites[dir2].getAnchor().y

    velocidade = 5
    raio = 50

    maxX = vw.getWidth()  - raio
    maxY = vw.getHeight() - raio

    if "8" in keys:
        if y - velocidade >= raio:
            sprites[dir2].move(0, -velocidade)
            dir2 = ch_dir2(sprites, dir2, "up")

    elif "5" in keys:
        if y + velocidade <= maxY:
            sprites[dir2].move(0, velocidade)
            dir2 = ch_dir2(sprites, dir2, "down")

    elif "4" in keys:
        if x - velocidade >= raio:
            sprites[dir2].move(-velocidade, 0)
            dir2 = ch_dir2(sprites, dir2, "left")

    elif "6" in keys:
        if x + velocidade <= maxX:
            sprites[dir2].move(velocidade, 0)
            dir2 = ch_dir2(sprites, dir2, "right")

    return dir2


#========= SPRITE ATIVA DO PLAYER 2 =========
def get_active_sprite2(sprites):
    for spr in sprites.values():
        if spr.getAnchor().x > -5000:
            return spr
    return None
