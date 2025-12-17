from graphics import *
import math

#========= CONSTANTES =========
RAIO_TANQUE = 40
RAIO_BALA = 20

#========= CRIAR ÁREA DE COLISÃO ========
def criar_area_colisao(sprite, nome, largura, altura):

    x = sprite.getAnchor().x
    y = sprite.getAnchor().y

    return {
        "nome": nome,
        "sprite": sprite,
        "x1": x - largura / 2,
        "y1": y - altura / 2,
        "x2": x + largura / 2,
        "y2": y + altura / 2,
        "largura": largura,
        "altura": altura,
        "centro_x": x,
        "centro_y": y
    }

#========= VERIFICAR COLISÃO CÍRCULO-RETÂNGULO =========
def verificar_colisao_circulo_retangulo(cx, cy, raio, area):

    px = max(area["x1"], min(cx, area["x2"]))
    py = max(area["y1"], min(cy, area["y2"]))

    dx = cx - px
    dy = cy - py

    return (dx * dx + dy * dy) < (raio * raio)

#========= VERIFICAR COLISÃO CÍRCULO-CÍRCULO =========
def verificar_colisao_circulo_circulo(x1, y1, r1, x2, y2, r2):

    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx * dx + dy * dy) < (r1 + r2)


#========= VERIFICAR TANQUE X OBSTÁCULO =========
def verificar_colisao_tanque_obstaculo(tanque, obstaculos):
    if tanque is None:
        return False, None

    x = tanque.getAnchor().x
    y = tanque.getAnchor().y

    for obstaculo in obstaculos:
        if verificar_colisao_circulo_retangulo(x, y, RAIO_TANQUE, obstaculo):
            return True, obstaculo

    return False, None

#========= CORRIGIR TANQUE X OBSTÁCULO =========
def corrigir_colisao_tanque_obstaculo(tanque, obstaculo, direcao):
    if tanque is None or obstaculo is None:
        return

    tx = tanque.getAnchor().x
    ty = tanque.getAnchor().y

    ox = obstaculo["centro_x"]
    oy = obstaculo["centro_y"]

    vx = tx - ox
    vy = ty - oy

    distancia = math.sqrt(vx * vx + vy * vy)
    if distancia == 0:
        return

    vx /= distancia
    vy /= distancia

    sobreposicao = (obstaculo["largura"] / 2 + RAIO_TANQUE) - distancia

    if sobreposicao > 0:
        tanque.move(vx * sobreposicao, vy * sobreposicao)


#========= VERIFICAR COLISÃO TANQUES =========
def verificar_colisao_tanques(tanque1, tanque2):
    if tanque1 is None or tanque2 is None:
        return False

    x1 = tanque1.getAnchor().x
    y1 = tanque1.getAnchor().y
    x2 = tanque2.getAnchor().x
    y2 = tanque2.getAnchor().y

    return verificar_colisao_circulo_circulo(
        x1, y1, RAIO_TANQUE,
        x2, y2, RAIO_TANQUE
    )

#========= TANQUE X TANQUE =========
def corrigir_colisao_tanque_tanque(tanque1, tanque2, dir1, dir2):
    if tanque1 is None or tanque2 is None:
        return

    x1 = tanque1.getAnchor().x
    y1 = tanque1.getAnchor().y
    x2 = tanque2.getAnchor().x
    y2 = tanque2.getAnchor().y

    vx = x1 - x2
    vy = y1 - y2

    distancia = math.sqrt(vx * vx + vy * vy)
    distancia_min = RAIO_TANQUE * 2

    if 0 < distancia < distancia_min:
        vx /= distancia
        vy /= distancia

        ajuste = (distancia_min - distancia) / 2

        tanque1.move(vx * ajuste, vy * ajuste)
        tanque2.move(-vx * ajuste, -vy * ajuste)

#========= BALA X OBSTACULO =========
def verificar_colisao_bala_obstaculo(bala, obstaculos):
    if bala is None:
        return False, None

    x = bala.getAnchor().x
    y = bala.getAnchor().y

    for obstaculo in obstaculos:
        if verificar_colisao_circulo_retangulo(x, y, RAIO_BALA, obstaculo):
            return True, obstaculo

    return False, None