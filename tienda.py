class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def actualizar_precio(self, cambio_porcentaje, elevando):
        if elevando:
            self.precio += self.precio * cambio_porcentaje / 100
        else:
            self.precio -= self.precio * cambio_porcentaje / 100
    
    def print_info(self):
        print(f"{self.nombre} ({self.categoria}): ${self.precio:.2f}")

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto_nuevo):
        self.productos.append(producto_nuevo)

    def vender_producto(self, id):
        producto = self.productos.pop(id)
        producto.print_info()
    
    def inflación(self,aumento):
        for producto in self.productos:
            producto.actualizar_precio(aumento, True)

    def hacer_liquidación(self, category,descuento):
        for producto in self.productos:
            if producto.categoria == category:
                producto.actualizar_precio(descuento, True)
                
tienda = Tienda("Mi tienda")

producto1 = Producto("Libro", 10.99, "Oficina")
producto2 = Producto("poleron", 15.99, "Ropa")
producto3 = Producto("pesas", 249.99, "Deportes")
producto4 = Producto("monitor", 429.99, "Tecnologia")
producto5 = Producto("pc", 399.99, "Tecnologia")
producto6 = Producto("Mouse", 534.99, "Tecnologia")
producto7 = Producto("localizador", 149.99, "Tecnologia")
producto8 = Producto("huarache black", 557.282, "Calzado")
producto9 = Producto("teclado",699.990, "Tecnologia")


tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
tienda.agregar_producto(producto4)
tienda.agregar_producto(producto5)
tienda.agregar_producto(producto6)
tienda.agregar_producto(producto7)
tienda.agregar_producto(producto8)
tienda.agregar_producto(producto9)

producto1.print_info()
producto2.print_info()
producto3.print_info()
producto4.print_info()
producto5.print_info()
producto6.print_info()
producto7.print_info()
producto8.print_info()
producto9.print_info()

tienda.hacer_liquidación("Tecnologia", 20)
tienda.hacer_liquidación("Oficina", 20)

tienda.inflación(2)


