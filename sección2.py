nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}! Bienvenido al curso de Python!")
edad = int(input("Ingresa tu edad: "))
edad_ok = edad * 2
print(f"El doble de tu edad es {edad_ok} años ")
print("Ahora dame dos numeros enteros para sumarlos")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
suma = num1 + num2
print(f"El total es: {suma}")
print("Ahora dame un numero decimal")
num_decimal = float(input("Ingresa un número decimal: "))
num_deok = num_decimal / 2
print(f"La mitad de {num_decimal} es: {num_deok}")
edad = int(input("En que año naciste?: "))
anio_actual = 2025
anio_nacimiento = anio_actual - edad
print(f"Tu edad es: {anio_nacimiento}")
precio = float(input("Cual es el precio del producto que llevaste?: "))
cantidad = int(input("Cuantos productos compraste?: "))
total = precio * cantidad
print(f"El total a pagar es: {total}")
num_cuadrado = int(input("Dame un numero para calcular su cuadrado: "))
cuadrado = num_cuadrado ** 2
print(f"El cuadrado de {num_cuadrado} es: {cuadrado}")
print("Dame dos números para calcular su promedio:  ")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
prom = (num1 + num2) / 2
print(f"El promedio de {num1} y {num2} es: {prom}")
nombre = input("Cual es tu nombre : ")
edad = int(input("Cual es tu edad : "))
print(f"Hola, {nombre}. Tienes {edad} años.")