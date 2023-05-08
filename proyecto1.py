import moral_games
inventario = moral_games.Inventario()
juego = moral_games.Games_movil("fifa", "Xbox", 5000, 5, "deportes")
inventario.agregar_juego(juego)
juego = moral_games.Games_movil("fifa", "Ps4", 5000, 5, "deportes")
inventario.agregar_juego(juego)
juego = moral_games.Games_movil("softbol", "Xbox", 5000, 5, "deportes")
inventario.agregar_juego(juego)
# inventario.obtener_items()

juego = moral_games.Games_consola("pelea", "Ps4", 5000, 5, "deportes", "A")
inventario.agregar_juego(juego)
# inventario.obtener_items()

juego = moral_games.Games_pc("pelea", "pc", 5000, 5, "deportes", "(2GB de RAM, procesador core i5, tarjeta gráfica NVIDIA 1080, disco duro de 500GB)")
inventario.agregar_juego(juego)
inventario.obtener_items()
print("_______________")
inventario.obtener_items()