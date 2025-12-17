from graphics import *
from Playerone import get_active_sprite1
from Playertwo import get_active_sprite2
import Bulletone as BO
import Bullettwo as BT
import random

# ==================================================
# VIDA pickpup 
# ==================================================
LIFE_INTERVAL = 600
LIFE_MAX = 3
LIFE_RADIUS = 50

life_timer = 0
life_active = False



def _colidiu(a, b, raio=LIFE_RADIUS):
    ax, ay = a.getAnchor().x, a.getAnchor().y
    bx, by = b.getAnchor().x, b.getAnchor().y
    return ((ax - bx)**2 + (ay - by)**2) ** 0.5 < raio


def atualizar_vida_pickup(
    vw,
    life_pickup,
    sprit1, sprit2,
    life_red, life_blue,
    vidas_red, vidas_blue
):
    global life_timer, life_active

    # ===== SPAWN =====
    if not life_active:
        life_timer += 1

        if life_timer >= LIFE_INTERVAL:
            life_timer = 0
            life_active = True

            x = random.randint(200, int(vw.getWidth() - 200))
            y = random.randint(200, int(vw.getHeight() - 200))

            life_pickup.move(
                x - life_pickup.getAnchor().x,
                y - life_pickup.getAnchor().y
            )

    # ===== COLISÃO PLAYER RED =====
    if life_active:
        spr_red = get_active_sprite1(sprit1)

        if spr_red and _colidiu(spr_red, life_pickup):
            if vidas_red < LIFE_MAX:
                img = life_red[vidas_red]
                img.undraw()
                true_img = Image(img.getAnchor(), "Sprites/life1_true.png")
                true_img.draw(vw)
                life_red[vidas_red] = true_img
                vidas_red += 1

            life_pickup.move(-9999, -9999)
            life_active = False

    # ===== COLISÃO PLAYER BLUE =====
    if life_active:
        spr_blue = get_active_sprite2(sprit2)

        if spr_blue and _colidiu(spr_blue, life_pickup):
            if vidas_blue < LIFE_MAX:
                img = life_blue[vidas_blue]
                img.undraw()
                true_img = Image(img.getAnchor(), "Sprites/life2_true.png")
                true_img.draw(vw)
                life_blue[vidas_blue] = true_img
                vidas_blue += 1

            life_pickup.move(-9999, -9999)
            life_active = False
    return vidas_red, vidas_blue

# ==================================================
# MUNIÇÃO pickup
# ==================================================
AMMO_INTERVAL = 800
AMMO_BONUS = 2
AMMO_RADIUS = 50

ammo_timer = 0
ammo_active = False


def atualizar_ammo_pickup(vw, ammo_pickup, sprit1, sprit2):
    global ammo_timer, ammo_active

    # ===== SPAWN =====
    if not ammo_active:
        ammo_timer += 1
        if ammo_timer >= AMMO_INTERVAL:
            ammo_timer = 0
            ammo_active = True
            x = random.randint(200, int(vw.getWidth() - 200))
            y = random.randint(200, int(vw.getHeight() - 200))
            ammo_pickup.move(
                x - ammo_pickup.getAnchor().x,
                y - ammo_pickup.getAnchor().y
            )

    # ===== PLAYER 1 =====
    if ammo_active:
        spr1 = get_active_sprite1(sprit1)
        if spr1 and _colidiu(spr1, ammo_pickup, AMMO_RADIUS):
            limite_temp = 3 + AMMO_BONUS
            BO.ammo1 = min(BO.ammo1 + AMMO_BONUS, limite_temp)

            ammo_pickup.move(-9999, -9999)
            ammo_active = False

    # ===== PLAYER 2 =====
    if ammo_active:
        spr2 = get_active_sprite2(sprit2)
        if spr2 and _colidiu(spr2, ammo_pickup, AMMO_RADIUS):
            limite_temp = 3 + AMMO_BONUS
            BT.ammo2 = min(BT.ammo2 + AMMO_BONUS, limite_temp)

            ammo_pickup.move(-9999, -9999)
            ammo_active = False
    

# ==================================================
# MINA
# ==================================================
MINE_INTERVAL = 900
MINE_RADIUS = 50

mine_timer = 0
mine_active = False


def atualizar_mine_pickup(
    vw,
    mine_pickup,
    sprit1, sprit2,
    p1_mines, p2_mines
):
    global mine_timer, mine_active

    # ===== SPAWN =====
    if not mine_active:
        mine_timer += 1
        if mine_timer >= MINE_INTERVAL:
            mine_timer = 0
            mine_active = True
            x = random.randint(200, int(vw.getWidth() - 200))
            y = random.randint(200, int(vw.getHeight() - 200))
            mine_pickup.move(
                x - mine_pickup.getAnchor().x,
                y - mine_pickup.getAnchor().y
            )

    # ===== PLAYER 1 =====
    if mine_active:
        spr1 = get_active_sprite1(sprit1)
        if spr1 and _colidiu(spr1, mine_pickup, MINE_RADIUS):
            if p1_mines < 2:
                p1_mines += 1
            mine_pickup.move(-9999, -9999)
            mine_active = False

    # ===== PLAYER 2 =====
    if mine_active:
        spr2 = get_active_sprite2(sprit2)
        if spr2 and _colidiu(spr2, mine_pickup, MINE_RADIUS):
            if p2_mines < 2:
                p2_mines += 1
            mine_pickup.move(-9999, -9999)
            mine_active = False

    return p1_mines, p2_mines

