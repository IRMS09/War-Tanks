from graphics import *
import time
from Playerone import get_active_sprite1
from Sounds import tocar_tiro

# ========= CONFIGURAÇÕES DO PLAYER 2 =========
ammo_base2 = 3
ammo_bonus2 = 0 

max_ammo2 = ammo_base2
ammo2 = ammo_base2

rel_tm2 = 1.5
shot_cld2 = 0.25
bul_spd2 = 20

lst_tm2 = 0
rel2 = False
rel_sta2 = 0

bullet2 = []


# ========= FUNÇÃO PARA DISPARAR =========
def sh_bul2(bul_spr2, tnk_spr2, dir2):
    global ammo2, lst_tm2, rel2, bullet2

    now2 = time.time()
    if rel2 or ammo2 <= 0:
        return
    if now2 - lst_tm2 < shot_cld2:
        return

    lst_tm2 = now2
    ammo2 -= 1

    lista = bul_spr2[dir2]
    bala = None
    for spr in lista:
        if spr.getAnchor().x < -5000:
            bala = spr
            break
    if bala is None:
        return
    tocar_tiro()
    bx = tnk_spr2.getAnchor().x
    by = tnk_spr2.getAnchor().y

    bx0 = bala.getAnchor().x
    by0 = bala.getAnchor().y
    bala.move(bx - bx0, by - by0)

    dx, dy = 0, 0
    if dir2 == "up": dy = -bul_spd2
    if dir2 == "down": dy = bul_spd2
    if dir2 == "left": dx = -bul_spd2
    if dir2 == "right": dx = bul_spd2

    bullet2.append({"sprite": bala, "dx": dx, "dy": dy})


# ========= MOVIMENTO DAS BALAS =========
def mov_bul2(vw, sprit1=None):
    global bullet2, ammo2, rel2, rel_sta2
    global ammo_bonus2, max_ammo2

    target = None
    if sprit1:
        target = get_active_sprite1(sprit1)

    novas = []
    hit = False

    for b in bullet2:
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

    bullet2 = novas

    # ========= RECARGA AUTOMÁTICA =========
    if rel2 and time.time() - rel_sta2 >= rel_tm2:
        ammo_bonus2 = 0
        max_ammo2 = ammo_base2
        ammo2 = ammo_base2
        rel2 = False

    return hit


# ========= INICIAR RECARGA =========
def sta_rel2(keys):
    global rel2, rel_sta2
    if "9" in keys and not rel2:
        if ammo2 < max_ammo2:
            rel2 = True
            rel_sta2 = time.time()


# ========= RECARGA FORÇADA =========
def reload2():
    global ammo2, max_ammo2, ammo_bonus2
    ammo_bonus2 = 0
    max_ammo2 = ammo_base2
    ammo2 = ammo_base2
