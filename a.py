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
        if producto in self.productos:
            pass
        else:
            self.productos.append(producto)
    
    
for i in range(0, 2):
    a = input(f"Ingrese nombre del juego {i +1}: ")
    b = input(f"Ingrese precio del juego {i + 1}: ")
    a = Producto(a, b)
    carrito = CarritoDeCompra()
    carrito.agregar_item(a)


print(a.nombre)
a = input("ingrese nombre del juego: ")
print(isinstance(a,Producto))
