from Product import Product

import json

class Inventory():
    def __init__(self, json_file='inventario.json'):    # Le ingresa el archivo JSON al constructor
        self.products = {}  # Diccionario de productos
        self.json_file = json_file
        self.load_inventory()   # Carga el inventario desde el archivo JSON

    # Cargar inventario desde JSON
    def load_inventory(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                for item in data['Productos']:
                    product = Product(**item)
                    self.products[product.id] = product
        except FileNotFoundError:
            print("El archivo JSON no se encontró, iniciando con un inventario vacío.")

            
    # Guardar inventario a JSON
    def save_inventory(self):
        with open(self.json_file, 'w') as file: # Abre el archivo en modo escritura
            # Crea un diccionario con los productos
            data = {'Productos': [product.product_to_dict() for product in self.products.values()]}
            json.dump(data, file, indent=4)   # Escribe el diccionario en el archivo JSON

    # Agrega productos al inventario
    def add_product(self, product):
        if product.id in self.products:   # Verifica si el producto ya existe
            print('Product already exists')
            return False
        else:
            self.products[product.id] = product  # Agrega el producto al diccionario
            self.save_inventory()   # Guarda el inventario en el archivo JSON
            print('Product added successfully')

    # Muestra los productos del inventario
    def show_products(self):
        print('Products in inventory')
        for product in self.products.values():  # Recorre los productos del inventario
            print(product, "\n")    # Imprime el producto

    # Busca un producto en el inventario
    def search_product(self, id):
        if id in self.products:  # Verifica si el producto existe
            print(self.products.get(id))    # Imprime el producto
            return self.products.get(id)    # Retorna el producto
        else:
            print('Product not found')
            return False
    
    # Cambia el stock de un producto
    def change_stock(self, id, change_stock):
        product = self.search_product(id)
        if product:
            product.stock = change_stock    # Cambia el stock del producto
            self.save_inventory()   # Guarda el inventario en el archivo JSON
            print('Stock updated successfully')
            return True
        return False

    # Actualiza un producto del inventario
    def update_product(self, id, name, price, stock):
        product = self.search_product(id)   # Busca el producto
        if product:
            # Actualiza los datos del producto
            product.name = name
            product.price = price
            product.stock = stock
            self.save_inventory()   # Guarda el inventario en el archivo JSON
            print('Product updated successfully')
            return True
        return False
    
    # Elimina un producto del inventario
    def delete_product(self, id):
        product = self.search_product(id)   # Busca el producto
        if product:
            self.products.pop(id)   # Elimina el producto del diccionario
            self.save_inventory()   # Guarda el inventario en el archivo JSON
            print('Product deleted successfully')
            return True
        return False
