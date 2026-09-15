
def guardar_numero(numero_tres_cifras):
    # Validar que el número tenga exactamente tres cifras
    if not 100 <= numero_tres_cifras <= 999:
        print("Número incorrecto")
        return

    # Extraer las cifras
    cientos = numero_tres_cifras // 100
    decenas = (numero_tres_cifras // 10) % 10
    unidades = numero_tres_cifras % 10

    # Ordenar las cifras de menor a mayor
    cifras = sorted([cientos, decenas, unidades])

    # Construir los números de dos dígitos
    min_dos_digitos = cifras[0] * 10 + cifras[1]
    max_dos_digitos = cifras[2] * 10 + cifras[1]

    print(
        "Número correcto.",
        f"El máximo valor de dos dígitos con esos dígitos es {max_dos_digitos}",
        f"y el mínimo valor de dos dígitos con esos números es {min_dos_digitos}"
    )


# Main
numero_tres_cifras = int(input("Digite un número de tres cifras: "))

guardar_numero(numero_tres_cifras)
