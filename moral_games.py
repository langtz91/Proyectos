class Game:
    def __init__(self, codigo, titulo, plataforma, precio, cantidad_stock, genero,):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.genero = genero 
        self.codigo = codigo  

    def modificar_cantidad_stock(self, codigo, cantidad_nueva):
        if codigo == self.codigo:
            self.cantidad_stock = cantidad_nueva
    
    def modificar_precio(self, codigo, precio_nuevo):
        if codigo == self.codigo:
            self.precio = precio_nuevo
        
    def resta_stock_compra(self):
        self.cantidad_stock -= 1


class Inventario:
    def __init__(self):
        self.inventario = []

    def agregar_juego(self, juego):
        duplicado = 0
        for game in self.inventario:
            if juego.titulo == game.titulo and juego.plataforma == game.plataforma:
                duplicado += 1
        if duplicado == 0:
            self.inventario.append(juego)
        else:
            raise Exception("El juego ya se encuentra en el inventario")
        
    def eliminar_juego(self, titulo, plataforma):
        duplicado = 0
        for game in self.inventario:
            if titulo == game.titulo and plataforma == game.plataforma:             
                self.inventario.remove(game)
                duplicado += 1          
        if duplicado == 0:
            raise Exception("El juego no se encuentra en el inventario")
        
    def buscar_juego(self, titulo_o_genero):
        print("Resultado de la busqueda: ")
        k = 1
        for game in self.inventario:
            if titulo_o_genero == game.titulo or titulo_o_genero == game.genero:
                print(k)
                game.mostrar_info()
                k += 1
    
    def buscar_compra(self, codigo):
        for game in self.inventario:
            if codigo == game.codigo:
                return game
    
    def obtener_items(self):
        print("Lista de juegos en el inventario: ")
        k = 1
        for game in self.inventario:
            print(k)
            game.mostrar_info()
            k += 1


class GamesMovil(Game):
    def __init__(self, codigo, titulo, plataforma, precio, cantidad_stock, genero):
        super().__init__(codigo, titulo, plataforma, precio, cantidad_stock, genero)
        self.plataforma = "movil"

    def mostrar_info(self):
        print(f"Código: {self.codigo}, Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Cantidad en stock: {self.cantidad_stock}, Género: {self.genero}")
    
    def mostrar_compra(self):
        print(f"Código: {self.codigo}, Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Género: {self.genero}")

  
class GamesConsola(Game):
    def __init__(self, codigo, titulo, plataforma, precio, cantidad_stock, genero, clasificacion):
        super().__init__(codigo, titulo, plataforma, precio, cantidad_stock, genero)
        self.clasificacion = clasificacion
        
    def mostrar_info(self):
        print(f"Código: {self.codigo}, Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Cantidad en stock: {self.cantidad_stock}, Género: {self.genero}, Clasificación: {self.clasificacion}") 

    def mostrar_compra(self):
        print(f"Código: {self.codigo}, Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Género: {self.genero}, Clasificación: {self.clasificacion}")


class GamesPc(Game):
    def __init__(self, codigo, titulo, plataforma, precio, cantidad_stock, genero, requisitos_minimos):
        super().__init__(codigo, titulo, plataforma, precio, cantidad_stock, genero)
        self.plataforma = "PC"
        self.requisitos_minimos = requisitos_minimos
    
    def mostrar_info(self):
        print(f"Código: {self.codigo}, Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Cantidad en stock: {self.cantidad_stock}, Género: {self.genero}, Requisitos mínimos: {self.requisitos_minimos}") 

    def mostrar_compra(self):
        print(f"Código: {self.codigo}, Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Género: {self.genero}, Requisitos mínimos: {self.requisitos_minimos}")
        

class CarritoCompras:
    def __init__(self):
        self.carrito = []

    def agregar_juego_carrito(self, juego, unidades):
        for i in range(0, unidades):
            self.carrito.append(juego)

    def eliminar_juego_carrito(self, codigo):
        for game in self.carrito:
            while game.codigo == codigo:
                self.carrito.remove(game)

                #else:
                #raise Exception("El juego no se encuentra en el carrito de compras")
    
    def total_compra(self):
        total = 0
        for game in self.carrito:
            total += game.precio
        return print(f"Total costo de los productos del carrito = {total}")

    def confimar_compra(self):
        for game in self.carrito:
            game.resta_stock_compra()
        self.carrito.clear()

    def carrito_2(self):
        self.carrito_nuevo = []


    def obtener_items_carrito(self):
        print("Lista de elementos en el carrito: ")
        k = 1
        for game in self.carrito:
            print(k)
            game.mostrar_compra()
            k += 1