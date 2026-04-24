import os

# ******************************************************************************************
# Operaciones Aritméticas y Repetición de Cálculos
# Uso de condicionales anidados, operador ternario, validación de datos y bucles
# ******************************************************************************************


# Función para mostrar el menú al usuario en la consola
def mostrar_menu():
    print("\n************ MENÚ DE OPERACIONES ***************")
    print(" 1. Suma")
    print(" 2. Resta")
    print(" 3. Multiplicación")
    print(" 4. División")
    print(" 5. Limpiar consola")
    print(" 6. Salir")
    print("************************************************\n")


# Función para mostrar el resultado en formato tabla
def imprimir_tabla(encabezados, filas):
    # Convertir todos los datos a texto
    filas = [[str(dato) for dato in fila] for fila in filas]

    # Calcular el ancho de cada columna
    anchos = []
    for i in range(len(encabezados)):
        ancho_maximo = len(encabezados[i])
        for fila in filas:
            if len(fila[i]) > ancho_maximo:
                ancho_maximo = len(fila[i])
        anchos.append(ancho_maximo)

    # Crear separador
    separador = "+-" + "-+-".join("-" * ancho for ancho in anchos) + "-+"

    # Imprimir encabezados
    print(separador)
    print("| " + " | ".join(f"{encabezados[i]:<{anchos[i]}}" for i in range(len(encabezados))) + " |")
    print(separador)

    # Imprimir filas
    for fila in filas:
        print("| " + " | ".join(f"{fila[i]:<{anchos[i]}}" for i in range(len(fila))) + " |")

    print(separador)


# Función para capturar el núimero ingresado por el usuario
def leer_numero(mensaje):
    while True:
        dato = input(mensaje).lower()

        if dato == "salir":
            print("Programa finalizado. Gracias por usar el menú.")
            raise SystemExit

        try:
            numero = float(dato)
            return numero
        except ValueError:
            print("Error: debe ingresar un número válido.")


# Inicio del programa
print("\nEscriba 'salir' en cualquier momento para cerrar el programa.")

try:
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción del 1 al 6: ").lower()

        if opcion == "salir" or opcion == "6":
            print("Programa finalizado. Gracias por usar el menú.")
            break

        elif opcion == "5":
            os.system("cls")
            print("Consola limpiada correctamente.")

        elif opcion in ["1", "2", "3", "4"]:

            repetir = "s"

            while repetir == "s":
                numero1 = leer_numero("Ingrese el primer número: ")
                numero2 = leer_numero("Ingrese el segundo número: ")

                # Condicionales anidados para seleccionar la operación
                if opcion == "1":
                    operacion = "Suma"
                    signo = "+"
                    resultado = numero1 + numero2

                elif opcion == "2":
                    operacion = "Resta"
                    signo = "-"
                    resultado = numero1 - numero2

                elif opcion == "3":
                    operacion = "Multiplicación"
                    signo = "*"
                    resultado = numero1 * numero2

                elif opcion == "4":
                    operacion = "División"
                    signo = "/"

                    if numero2 == 0:
                        print("Error: no se puede dividir para cero.")
                        continue
                    else:
                        resultado = numero1 / numero2

                # Operador ternario para mostrar si el resultado es positivo, negativo o cero
                tipo_resultado = "Cero" if resultado == 0 else "Positivo" if resultado > 0 else "Negativo"

                print(f"\nResultado de la operación: {operacion}")

                imprimir_tabla(
                    ["Número 1", "Operador", "Número 2", "Resultado", "Tipo de resultado"],
                    [[f"{numero1:.2f}", signo, f"{numero2:.2f}", f"{resultado:.2f}", tipo_resultado]]
                )

                while True:
                    repetir = input("\n¿Desea realizar otro cálculo con esta misma operación? (s/n): ").lower()

                    if repetir == "salir":
                        print("Programa finalizado. Gracias por usar el menú.")
                        raise SystemExit

                    if repetir == "s" or repetir == "n":
                        break
                    else:
                        print("Error: debe ingresar 's' para sí o 'n' para no.")

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

except KeyboardInterrupt:
    print("\nCierre realizado correctamente.")