import random

def lanzar_dados():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

def jugar_partida():
    print("🎲 Comienza el juego...")
    lanzamiento_inicial = lanzar_dados()
    print(f"Primer lanzamiento: {lanzamiento_inicial}")

    if lanzamiento_inicial in [7, 11]:
        print("🎉 ¡Ganaste en el primer lanzamiento!")
        return "Gana"
    elif lanzamiento_inicial in [2, 3, 12]:
        print("❌ Perdiste en el primer lanzamiento.")
        return "Pierde"
    else:
        punto = lanzamiento_inicial
        print(f"🔁 Se establece el punto en: {punto}")

        while True:
            lanzamiento = lanzar_dados()
            print(f"Lanzamiento: {lanzamiento}")

            if lanzamiento == punto:
                print("🎉 ¡Volviste a sacar el punto! ¡Ganas!")
                return "Gana"
            elif lanzamiento == 7:
                print("❌ Salió un 7. Pierdes.")
                return "Pierde"
            # cualquier otro número → continúa

# Ejecutar una partida
resultado = jugar_partida()
print(f"\nResultado final: {resultado}")
