nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto que llevaste: ")
precio = float(input(f"Ingresa el precio de {producto}: "))
print(f"Hola {nombre}! el precio de {producto} es: {precio}")
nombre_ok = input("Ingresa tu nombre: ")
país = input("Ingresa el país donde vives: ")
print(f"Hola {nombre_ok} de {país}. Bienvenido!")
nombre_1 = input("Cual es tu nombre?:")
edad_1 = int(input("Cual es tu edad?:"))
ciudad_1 = input("Cual es tu ciudad?:")
print(f" Nombre: {nombre_1} Edad: {edad_1} Ciudad: {ciudad_1}")

print("Ahora vamos a calcular el área de un rectángulo")
largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
area = round((largo * ancho), 2)
print(f"El área del rectángulo es: {area}")

producto = "Pan"
precio = 1.50
cantidad = 4
total = precio * cantidad

print(f"'Producto' | 'Precio':<10| 'Cantidad':<10 | 'Total':<10")
print("----------------------------------------------------------")
print(f"{producto} | ${precio:} | {cantidad:   }  | ${total:} ")




