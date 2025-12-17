from graphics import *
import time

#========= TROCA DE DIREÇÃO DO PLAYER 1 =========
def ch_dir1(sprites, dir_atual, dir_nova):

    if dir_atual == dir_nova:
        return dir_atual

    anchor = sprites[dir_atual].getAnchor()
    x, y = anchor.x, anchor.y

    sprites[dir_atual].move(-9999 - x, -9999 - y)

    nx, ny = sprites[dir_nova].getAnchor().x, sprites[dir_nova].getAnchor().y
    sprites[dir_nova].move(x - nx, y - ny)

    return dir_nova


#========= MOVIMENTO DO PLAYER 1 =========
def mov_pl1(vw, sprites, dir_atual, keys):

    dir1 = dir_atual
    x = sprites[dir1].getAnchor().x
    y = sprites[dir1].getAnchor().y

    velocidade = 5
    raio = 50

    maxX = vw.getWidth()  - raio
    maxY = vw.getHeight() - raio

    if "w" in keys or "W" in keys:
        if y - velocidade >= raio:
            sprites[dir1].move(0, -velocidade)
            dir1 = ch_dir1(sprites, dir1, "up")

    elif "s" in keys or "S" in keys:
        if y + velocidade <= maxY:
            sprites[dir1].move(0, velocidade)
            dir1 = ch_dir1(sprites, dir1, "down")

    elif "a" in keys or "A" in keys:
        if x - velocidade >= raio:
            sprites[dir1].move(-velocidade, 0)
            dir1 = ch_dir1(sprites, dir1, "left")


    elif "d" in keys or "D" in keys:
        if x + velocidade <= maxX:
            sprites[dir1].move(velocidade, 0)
            dir1 = ch_dir1(sprites, dir1, "right")

    return dir1

#========= SPRITE ATIVA DO PLAYER 1 =========
def get_active_sprite1(sprites):
    for spr in sprites.values():
        if spr.getAnchor().x > -5000:
            return spr
    return None
