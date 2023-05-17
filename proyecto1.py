import moral_games
juegos = moral_games.Inventario()
#juego = moral_games.Games_movil("pes", "", 2000, 3, "deportes")
juego = moral_games.Games_movil("fifa", "", 5000, 5, "deportes")
juegos.agregar_juego(juego)
juego = moral_games.Games_consola("fifa", "Ps4", 5000, 5, "deportes", "B")
juegos.agregar_juego(juego)
juego = moral_games.Games_consola("fifa", "Xbox", 5000, 5, "deportes", "C")
juegos.agregar_juego(juego)

# juegos.obtener_items()

juego = moral_games.Games_consola("pelea", "Ps4", 5000, 5, "deportes", "A")
juegos.agregar_juego(juego)
# juegos.obtener_items()

juego = moral_games.Games_pc("pelea", "", 5000, 5, "deportes", "(2GB de RAM, procesador core i5, tarjeta gráfica NVIDIA 1080, disco duro de 500GB)")
juegos.agregar_juego(juego)
juegos.obtener_items()
print("_______________")
try:
    juegos.eliminar_juego("fifa", "Xbox")
    juegos.obtener_items()
    juegos.eliminar_juego("pelea", "Ps4")
except Exception:
    print("El juego a eliminar debe estar en el inventario")
juegos.buscar_juego("deportes")
carrito = moral_games.carrito_compra()
carrito.agregar_compra("pelea", "PC")


