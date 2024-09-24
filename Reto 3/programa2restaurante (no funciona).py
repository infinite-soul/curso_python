# Inicialización de variables
mesas = {i: {"acumulado": 0, "pedidos": []} for i in range(1, 21)}
IMPUESTO_IMPOCONSUMO = 0.08  # 8%

def registrar_pedido(mesa):
    while True:
        pedido = float(input(f"Mesa {mesa}, ingresa el precio de tu pedido (0 para terminar): "))
        if pedido <= 0:
            break
        impuesto = pedido * IMPUESTO_IMPOCONSUMO
        total_pedido = pedido + impuesto
        mesas[mesa]["acumulado"] += total_pedido
        mesas[mesa]["pedidos"].append(total_pedido)
        print(f"Factura actual para mesa {mesa}: ${mesas[mesa]['acumulado']:.2f}")

def mostrar_resumen():
    for mesa, datos in mesas.items():
        if datos["acumulado"] > 0:
            print(f"Mesa {mesa}:")
            print(f"  Número de pedidos: {len(datos['pedidos'])}")
            print(f"  Total facturado: ${datos['acumulado']:.2f}")
    print(f"Total facturado en el restaurante: ${sum(mesa['acumulado'] for mesa in mesas.values()):.2f}")

# Programa principal
for mesa in range(1, 21):
    registrar_pedido(mesa)

mostrar_resumen()
