lista_compras = []

def agregar_producto():
    producto = input("Ingrese su lista producto por preducto,cuando no tenga mas escriba "finalizar" y se le mostrara su lista")
    return producto.lower()

while True:
    producto = agregar_producto()
    
    if producto == "finalizar":
        break 
    else:
        lista_compras.append(producto)  

print("Lista de compras:")
for index, producto in enumerate(lista_compras, start=1):
    print(f"{index}. {producto}")