from graphics import *
import time
from Playertwo import get_active_sprite2
from Sounds import tocar_tiro

# ========= CONFIGURAÇÕES DO PLAYER 1 =========
ammo_base1 = 3
ammo_bonus1 = 0

max_ammo1 = ammo_base1
ammo1 = ammo_base1

rel_tm1 = 1.5
shot_cld1 = 0.25
bul_spd1 = 20

lst_tm1 = 0
rel1 = False
rel_sta1 = 0

bullet1 = []


# ========= FUNÇÃO PARA DISPARAR =========
def sh_bul1(bul_spr1, tnk_spr1, dir1):
    global ammo1, lst_tm1, rel1, bullet1

    now1 = time.time()
    if rel1 or ammo1 <= 0:
        return
    if now1 - lst_tm1 < shot_cld1:
        return

    lst_tm1 = now1
    ammo1 -= 1

    lista = bul_spr1[dir1]
    bala = None
    for spr in lista:
        if spr.getAnchor().x < -5000:
            bala = spr
            break
    if bala is None:
        return
    tocar_tiro()
    bx = tnk_spr1.getAnchor().x
    by = tnk_spr1.getAnchor().y

    bx0 = bala.getAnchor().x
    by0 = bala.getAnchor().y
    bala.move(bx - bx0, by - by0)

    dx, dy = 0, 0
    if dir1 == "up": dy = -bul_spd1
    if dir1 == "down": dy = bul_spd1
    if dir1 == "left": dx = -bul_spd1
    if dir1 == "right": dx = bul_spd1

    bullet1.append({"sprite": bala, "dx": dx, "dy": dy})


# ========= MOVIMENTO DAS BALAS =========
def mov_bul1(vw, sprit2=None):
    global bullet1, ammo1, rel1, rel_sta1
    global ammo_bonus1, max_ammo1

    target = None
    if sprit2:
        target = get_active_sprite2(sprit2)

    novas = []
    hit = False

    for b in bullet1:
        spr = b["sprite"]
        spr.move(b["dx"], b["dy"])

        x = spr.getAnchor().x
        y = spr.getAnchor().y

        if target:
            tx = target.getAnchor().x
            ty = target.getAnchor().y
            dist = ((x - tx)**2 + (y - ty)**2)**0.5

            if dist < 40:
                spr.move(-9999 - x, -9999 - y)
                hit = True
                continue

        if 0 <= x <= vw.getWidth() and 0 <= y <= vw.getHeight():
            novas.append(b)
        else:
            spr.move(-9999 - x, -9999 - y)

    bullet1 = novas

    # ========= RECARGA AUTOMÁTICA =========
    if rel1 and time.time() - rel_sta1 >= rel_tm1:
        ammo_bonus1 = 0            # REMOVE bônus
        max_ammo1 = ammo_base1
        ammo1 = ammo_base1
        rel1 = False

    return hit


# ========= INICIAR RECARGA =========
def sta_rel1(keys):
    global rel1, rel_sta1
    if ("r" in keys or "R" in keys) and not rel1:
        if ammo1 < max_ammo1:
            rel1 = True
            rel_sta1 = time.time()


# ========= RECARGA FORÇADA (opcional) =========
def reload1():
    global ammo1, max_ammo1, ammo_bonus1
    ammo_bonus1 = 0
    max_ammo1 = ammo_base1
    ammo1 = ammo_base1
