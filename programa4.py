def guardar_numero(numero_tres_cifras):
    if not 100 <= numero_tres_cifras <= 999:
        print("Número incorrecto")
        return

    # Extraer las cifras del número
    cientos = numero_tres_cifras // 100
    decenas = (numero_tres_cifras // 10) % 10
    unidades = numero_tres_cifras % 10

    # Ordenar las cifras de menor a mayor
    cifras = sorted([cientos, decenas, unidades])

    # Formar el número máximo y mínimo de dos dígitos
    max_dos_digitos = cifras[2] * 10 + cifras[1]
    min_dos_digitos = cifras[0] * 10 + cifras[1]

    print(
        "Número correcto.",
        "El máximo valor de dos dígitos con esos dígitos es",
        max_dos_digitos,
        "y el mínimo valor de dos dígitos es",
        min_dos_digitos
    )


# Main
try:
    numero_tres_cifras = int(
        input("Digite un número de tres cifras: ")
    )

    guardar_numero(numero_tres_cifras)

except ValueError:
    print("Debe ingresar un número entero válido.")
