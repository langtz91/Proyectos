# Moral de Perro S.A. desea crear un comercio electrónico, pero no cuentan con el
# software para lograrlo, ayúdelos creando: una clase Producto y una clase
# CarritoDeCompras , con las siguientes especificaciones:
# a. La clase Producto debe tener dos atributos: nombre , y precio
# Ejercicios POO Python 2
# b. La clase Producto debe tener un método que permita modificar el nombre del
# producto.
# c. La clase CarritoDeCompras debe tener un atributo llamado productos que será
# una lista de elementos en el carrito.
# d. La clase CarritoDeCompras debe tener los siguientes métodos:
# agregar_item(self, producto) - un método que permita agregar un producto
# al carrito si éste aún no está en la lista.
# eliminar_item(self, producto) - un método que permita eliminar un producto
# del carrito si éste está en la lista. Si el producto no está en la lista, el
# método debe imprimir un mensaje de error.
# obtener_items(self) - un método que devuelve la lista de productos en el
# carrito.
# obtener_total(self) - un método que calcula y devuelve el costo total de
# todos los productos en el carrito.
# NOTA: Los elementos en la lista del carrito de compras deben ser productos, es decir,
# objetos creados con la clase Product

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def modif_nombre(self, nombre_actual, nombre_nuevo):
        if self.nombre == nombre_actual:
            self.nombre = nombre_nuevo
    
class CarritoDeCompra:
    def __init__(self):
        self.productos = []

    def agregar_item(self, producto):
        if not producto in self.productos:
            self.productos.append(producto)
    
    def eliminar_item(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
           raise Exception("El producto no se encuentra en el carrito")
    
    def obtener_items(self):
        for i in self.productos:
            print(f"{i.nombre} = {i.precio}")

    def obtener_total(self):
        total = 0
        for i in self.productos:
            total += i.precio
        return print(f"Total costo de los productos del carrito = {total}")
    
producto = Producto("Manzana", 2000)
print(producto.nombre)

producto1 = Producto("Uva", 8000)
print(producto1.nombre)

producto2 = Producto("Arroz", 1500)
print(producto2.nombre)

producto3 = Producto("Aceite", 10000)
print(producto3.nombre)

producto4 = Producto("Coca Cola", 2500)
print(producto4.nombre)

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
producto.modif_nombre("Manzana", "Pera")
print(producto.nombre)

carrito = CarritoDeCompra()
carrito.agregar_item(producto1)
carrito.agregar_item(producto2)

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
carrito.obtener_items()

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
try:
    carrito.eliminar_item(producto4)
    carrito.eliminar_item(producto1)
except Exception:
    print("El producto a eliminar debe estar en el carrito")
carrito.obtener_items()
carrito.obtener_total()
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
try:
    carrito.eliminar_item(producto4)
except Exception:
    print("El producto a eliminar debe estar en el carrito")
carrito.obtener_items()
carrito.obtener_total()       

