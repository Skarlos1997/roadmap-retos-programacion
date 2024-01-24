# /*
#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
#  *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
#  *   interpolación, verificación...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas
#  */
# Locnar


cadena_1 = "Hola"
cadena_2 = " "
cadena_3 = "Mundo"
cadena_4 = "Hola Mundo"

# Operaciones con cadenas de caracteres
# Acceso a caracteres especificos
print(cadena_1[0])
# Subcadenas
print(cadena_4.find("Mundo"))
# Longitud
print(len(cadena_1))
# Concatenacion
print(cadena_1 + cadena_2 + cadena_3)
# Repeticion
print(cadena_1 * 3)
# Recorrido
for i in cadena_1:
    print(i)
# Conversión a mayúsculas
print(cadena_1.upper())
# Conversión a minúsculas
print(cadena_1.lower())
# Reemplazo
print(cadena_1.replace("o", "a"))
# División
print(cadena_4.split(" "))
# Unión
print(cadena_3.join(cadena_4))
# Interpolación
print(f"{cadena_1} {cadena_3}")
# Verificación
print(cadena_1.isalpha())

# Actividad adicional
input_1 = input("Ingrese una palabra: ")
input_2 = input("Ingrese otra palabra: ")

# Palíndromos
if input_1 == input_2[::-1]:
    print("Las palabras son palíndromos")
# Anagramas
if sorted(input_1) == sorted(input_2):
    print("Las palabras son anagramas")
# Isogramas
if len(input_1) == len(set(input_2)):
    print("Las palabras son isogramas")
