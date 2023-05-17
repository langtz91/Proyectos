class Games:
    def __init__(self, titulo, plataforma, precio, cantidad_stock, genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.genero = genero   

class Inventario:
    def __init__(self):
        self.juegos = []

    def agregar_juego(self, juego):
        duplicado = 0
        for game in self.juegos:
            if juego.titulo == game.titulo and juego.plataforma == game.plataforma:
                duplicado += 1
        if duplicado == 0:
            self.juegos.append(juego)
        else:
            raise Exception("El juego ya se encuentra en el inventario")
        
    def eliminar_juego(self, titulo, plataforma):
        duplicado = 0
        for game in self.juegos:
            if titulo == game.titulo and plataforma == game.plataforma:             
                self.juegos.remove(game)
                duplicado += 1          
        if duplicado == 0:
            raise Exception("El juego no se encuentra en el inventario")
        
    def buscar_juego(self, titulo_o_genero):
        conteo_juego = 0
        for game in self.juegos:
            if titulo_o_genero == game.titulo or titulo_o_genero == game.genero:
                game.mostrar_info()
                conteo_juego += 1 
        if conteo_juego == 0:
             print("No se encontraron resultados en la busqueda")
            
    def obtener_items(self):
        k = 1
        for game in self.juegos:
            print(k)
            game.mostrar_info()
            k += 1
    

class Games_movil(Games):
    def __init__(self, titulo, plataforma, precio, cantidad_stock, genero):
        super().__init__(titulo, plataforma, precio, cantidad_stock, genero)
        self.plataforma = "movil"

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Cantidad en stock: {self.cantidad_stock}, Género: {self.genero}")
            
class Games_consola(Games):
    def __init__(self, titulo, plataforma, precio, cantidad_stock, genero, clasificacion):
        super().__init__(titulo, plataforma, precio, cantidad_stock, genero)
        self.clasificacion = clasificacion
        

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Cantidad en stock: {self.cantidad_stock}, Género: {self.genero}, Clasificación: {self.clasificacion}") 

class Games_pc(Games):
    def __init__(self, titulo, plataforma, precio, cantidad_stock, genero, requisitos_minimos):
        super().__init__(titulo, plataforma, precio, cantidad_stock, genero)
        self.plataforma = "PC"
        self.requisitos_minimos = requisitos_minimos

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Plataforma: {self.plataforma}, Precio: ${self.precio}, Cantidad en stock: {self.cantidad_stock}, Género: {self.genero}, Requisitos mínimos: {self.requisitos_minimos}") 

class juegos_comprados:
    def __init__(self, titulo, plataforma, cantidad):
        self.titulo = titulo
        self.plataforma = plataforma
        self.cantidad = cantidad


class carrito_compra:
    def __init__(self):
        self.carrito = []
    
    def agregar_compra(self, titulo , plataforma):
        for game in self.juegos:
            if game.titulo == titulo and game.plataforma == plataforma:
                self.carrito.append(game)
                

                

   