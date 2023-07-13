from random import random
from click_certo_007.view import click_certo


class MainWindow(click_certo):



def gerar_placar():
    gols_casa = random.randint(0, 5)
    gols_vistante = random.randint(0, 5)

    placar = [
        {"time": "Time da casa", "gols": gols_casa},
        {"time": "Time Visitante", "gols": gols_vistante}
    ]

    return placar

def exibir_placar(placar):
    print("Placar final:")
    for resultado in placar:
        print(f"{resultado['time']}: {resultado['gols']}")

def validar_vencedor(placar):
    if placar[0]['gols'] > placar[1]['gols']:
        return placar[0]['time']
    elif placar[1]['gols'] > placar[0]['gols']:
        return placar[1]['time']
    else:
        return "Empate"

placar = gerar_placar()
exibir_placar(placar)

ganhador = validar_vencedor(placar)
print(f"Vencedor: {ganhador} ganhou")
