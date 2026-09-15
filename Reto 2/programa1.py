# Denominaciones disponibles, de mayor a menor
DENOMINACIONES = [
    100000,
    50000,
    20000,
    10000,
    5000,
    2000,
    1000,
    500,
    200,
    100,
    50,
    20,
    10
]


def verificar_cedula(numero_cedula):
    if 10000000 <= numero_cedula <= 99999999:
        print("Cédula válida.")
        return True

    print("Cédula inválida.")
    return False


def cajero(plata):
    if plata <= 0:
        print("El monto debe ser mayor que cero.")
        return

    print(f"Tu dinero es: {plata:,} pesos")

    restante = plata
    entrega = {}

    # Calcular billetes y monedas
    for denominacion in DENOMINACIONES:
        cantidad = restante // denominacion

        if cantidad > 0:
            entrega[denominacion] = cantidad
            restante %= denominacion

    print("\nDinero entregado:")

    for denominacion, cantidad in entrega.items():
        tipo = "billete" if denominacion >= 1000 else "moneda"

        if cantidad != 1:
            tipo += "s"

        print(f"{cantidad} {tipo} de {denominacion:,} pesos")

    # Mostrar si queda un valor que no se puede entregar
    if restante > 0:
        print(f"\nNo se pudo entregar: {restante} pesos")

    # Bono de 10.000 pesos
    billetes100k = entrega.get(100000, 0)
    billetes20k = entrega.get(20000, 0)

    if plata >= 220000 and billetes100k > 1 and billetes20k >= 1:
        total_mas_bono = plata + 10000

        print(
            f"\nAgregamos 10.000 pesos a tu dinero. "
            f"Ahora tu dinero es: {total_mas_bono:,}"
        )


# Main
numero_cedula = int(input("Digite su cédula: "))

if verificar_cedula(numero_cedula):
    plata = int(input("Indica el dinero que deseas sacar: "))
    cajero(plata)
