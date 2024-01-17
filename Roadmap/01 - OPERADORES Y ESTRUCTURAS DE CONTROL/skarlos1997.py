# Retos de programación Roadmap 2024 - Reto #01, Python - Skarlos1997

# Operadores y estructuras de control

# Operadores aritméticos
suma = 5 + 5
print(suma)
resta = 10 - 5
print(resta)
multiplicacion = 5 * 5
print(multiplicacion)
division = 10 / 2
print(division)
potencia = 5 ** 2
print(potencia)
modulo = 10 % 2
print(modulo)
division_entera = 10 // 3
print(division_entera)

# Operadores logicos
operador_and = True and True
print(operador_and)
operador_or = True or False
print(operador_or)
operador_not = not False
print(operador_not)

# Operadores de comparación
menor_que = 5 < 10
print(menor_que)
mayor_que = 10 > 5
print(mayor_que)
menor_o_igual_que = 5 <= 10
print(menor_o_igual_que)
mayor_o_igual_que = 10 >= 5
print(mayor_o_igual_que)
igual_que = 5 == 5
print(igual_que)
diferente_que = 5 != 10
print(diferente_que)

# Operadores de asignación
igual = 5
print(igual)
suma_igual = 5
suma_igual += 5
print(suma_igual)
resta_igual = 5
resta_igual -= 5
print(resta_igual)
multiplicacion_igual = 5
multiplicacion_igual *= 5
print(multiplicacion_igual)
division_igual = 5
division_igual /= 5
print(division_igual)
potencia_igual = 5
potencia_igual **= 5
print(potencia_igual)
modulo_igual = 5
modulo_igual %= 5
print(modulo_igual)
division_entera_igual = 5
division_entera_igual //= 5
print(division_entera_igual)

# Operadores de identidad
operador_is = 5 is 5
print(operador_is)
is_not = 5 is not 10
print(is_not)

# Operadores de pertenencia
operador_in = 5 in [1, 2, 3, 4, 5]
print(operador_in)
not_in = 5 not in [1, 2, 3, 4, 5]
print(not_in)

# Operadores de bits
and_bit = 5 & 5
print(and_bit)
or_bit = 5 | 5
print(or_bit)
xor_bit = 5 ^ 5
print(xor_bit)
not_bit = ~5
print(not_bit)
desplazamiento_izquierda = 5 << 2
print(desplazamiento_izquierda)
desplazamiento_derecha = 5 >> 2
print(desplazamiento_derecha)

# Estructuras de control
# Condicionales
# if elif else
if 5 > 10:
    print("5 es mayor que 10")
elif 5 < 10:
    print("5 es menor que 10")
else:
    print("5 es igual que 10")

# assert
assert 5 < 10, "5 no es menor que 10"

# Iterativas
# for
for i in range(10):
    print(i)

# while
i = 0
while i < 10:
    print(i)
    i += 1

# Excepciones
# try except
try:
    print(5 / 0)
except:
    print("Error al dividir entre 0")

# Otras
# with
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola mundo")

# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
