
def guardar_numero(numero_seis_cifras):
    # Validar que el número tenga exactamente seis cifras
    if not 100000 <= numero_seis_cifras <= 999999:
        print("Boleta inválida")
        return

    # Extraer las cifras del número
    cien_miles = numero_seis_cifras // 100000
    diez_miles = (numero_seis_cifras // 10000) % 10
    miles = (numero_seis_cifras // 1000) % 10
    cientos = (numero_seis_cifras // 100) % 10
    decenas = (numero_seis_cifras // 10) % 10
    unidades = numero_seis_cifras % 10

    # Calcular el horario
    horario = miles + cientos

    # Validar la boleta
    if unidades + cien_miles > 5:
        print("Tu boleta es válida")

    # Determinar el tipo de entrada
    if 0 < diez_miles < 7:
        print("El tipo de entrada es gramilla")
    else:
        print("El tipo de entrada es general")

    # Determinar la puerta y el horario de entrada
    if horario % 2 == 1:
        print("Debes entrar por la puerta 2 a partir de las 8pm")
    else:
        print("Debes entrar por la puerta 1 a partir de las 7pm")


# Main
numero_seis_cifras = int(input("Digite un número de seis cifras: "))

guardar_numero(numero_seis_cifras)
