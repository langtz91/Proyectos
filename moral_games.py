class Games_movil:
    def __init__(self, titulo, plataforma, precio, cantidad_stock, genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.genero = genero   

class Inventario:
    def __init__(self):
        self.inventario = []

    def agregar_juego(self, juego):
        duplicado = 0
        for i in self.inventario:
            if juego.titulo == i.titulo and juego.plataforma == i.plataforma:
                duplicado += 1
        if duplicado == 0:
            self.inventario.append(juego)
        
    #def eliminar_item(self, titulo, plataforma):
        #for juego in self.inventario:
            #if titulo == i.titulo and plataforma == i.plataforma:
        # self.inventario.remove(juego)
        

    def obtener_items(self):
        k = 1
        for i in self.inventario:
            if isinstance(i, Games_consola):
                print(f"{k}-{i.titulo}, {i.plataforma}, {i.precio}, {i.cantidad_stock}, {i.genero}, {i.clasificacion}")
            elif isinstance(i, Games_pc):
                print(f"{k}-{i.titulo}, {i.plataforma}, {i.precio}, {i.cantidad_stock}, {i.requisitos_minimos}")
            else:
                print(f"{k}-{i.titulo}, {i.plataforma}, {i.precio}, {i.cantidad_stock}, {i.genero}")
            k += 1
    


class Games_consola(Games_movil):
    def __init__(self, titulo, plataforma, precio, cantidad_stock, genero, clasificacion):
        super().__init__(titulo, plataforma, precio, cantidad_stock, genero)
        self.clasificacion = clasificacion

class Games_pc(Games_movil):
    def __init__(self, titulo, plataforma, precio, cantidad_stock, genero, requisitos_minimos):
        super().__init__(titulo, plataforma, precio, cantidad_stock, genero)
        self.requisitos_minimos = requisitos_minimos