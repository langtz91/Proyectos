import moral_games
inventario = moral_games.Inventario()
#juego = moral_games.Games_movil("pes", "", 2000, 3, "deportes")
juego = moral_games.Games_movil(5501, "fifa", "", 5000, 5, "deportes")
inventario.agregar_juego(juego)
# juego = moral_games.Games_consola("fifa", "Ps4", 5000, 5, "deportes", "B")
# inventario.agregar_juego(juego)
# juego = moral_games.Games_consola("fifa", "Xbox", 5000, 5, "deportes", "C")
# inventario.agregar_juego(juego)

# inventario.obtener_items()

juego = moral_games.Games_consola(5502, "pelea", "Ps4", 5000, 5, "deportes", "A")
inventario.agregar_juego(juego)
# inventario.obtener_items()

juego = moral_games.Games_pc(5503, "pelea", "", 5000, 5, "deportes", "(2GB de RAM, procesador core i5, tarjeta gráfica NVIDIA 1080, disco duro de 500GB)")
inventario.agregar_juego(juego)
# inventario.obtener_items()
print("_______________")
# try:
#     # inventario.eliminar_juego("fifa", "Xbox")
inventario.obtener_items()
#     # inventario.eliminar_juego("pelea", "Ps4")
# except Exception:
#     print("El juego a eliminar debe estar en el inventario")
print("_____")
juego_a_guardar = inventario.buscar_compra(5503)
carritocompra = moral_games.CarritoCompras()
print("_____________________________")
#n = int(input("Cuantos juegos desea llevar: "))
#for i in range(0, n):
    #carritocompra.agregar_juego_carrito(juego_a_guardar)
carritocompra.agregar_juego_carrito(juego_a_guardar, 5)
#carritocompra.eliminar_juego_carrito(5503)
#carritocompra.obtener_items_carrito()
for game in carritocompra.carrito:
    print(game.cantidad_stock)
    print(game.precio)

juego.mod_cantidad_stock(5503, 8)
#juego.resta_stock_compra()
juego.mod_precio(5503, 3000)
print("___________________")
for game in carritocompra.carrito:
    print(game.cantidad_stock)
    print(game.precio)

carritocompra.total_compra()
carritocompra.confimar_compra()
print("Y__________________Y")
for game in carritocompra.carrito:
    print(game.cantidad_stock)
    print(game.precio)
#for game in carritocompra.carrito:
    #print(game.titulo)
#inventario.buscar_juego("pelea") 
print("???") 
for game in carritocompra.carrito:
    print(game.cantidad_stock)
    print(game.precio)