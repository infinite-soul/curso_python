def calcularVentasAdultos (boletasAdultosCompradas):
    gananciasBoletasAdultos = boletasAdultosCompradas * 12000
    return gananciasBoletasAdultos

def calcularVentasNiños (boletasNiñosCompradas):
    gananciasBoletasNiños = boletasNiñosCompradas * 10000
    return gananciasBoletasNiños

def calcularGananciasTotales (gananciasBoletasNiños, gananciasBoletasAdultos):
    gananciasTotales= (gananciasBoletasNiños + gananciasBoletasAdultos)
    return gananciasTotales

def imprimirReporte (gananciasBoletasNiños, gananciasBoletasAdultos, gananciasTotales):
    print("las ganancias de boletas de niños fue ", gananciasBoletasNiños,", las ganancias de adultos fueron", gananciasBoletasAdultos, " y las ganancias totales fueron ", gananciasTotales)

def main():

    boletasAdultosCompradas= int(input("¿cuántas boletas de adulto vas a comprar?"))
    boletasNiñosCompradas=int(input("¿cuántas boletas de niño vas a comprar?"))
    print()
    gananciasBoletasAdultos = calcularVentasAdultos(boletasAdultosCompradas)
    gananciasBoletasNiños = calcularVentasNiños(boletasNiñosCompradas)
    gananciasTotales=calcularGananciasTotales(gananciasBoletasNiños,gananciasBoletasAdultos)
    imprimirReporte(gananciasBoletasNiños, gananciasBoletasAdultos, gananciasTotales)

main()
