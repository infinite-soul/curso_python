#metrocine---------------------

precioAdulto=12000
precioNiño=10000
salaConSubtitulosEspañol=0
salaConSubtitulosIngles=0
peliculasHD=0
peliculas3D=0
cuantasBoletasNiñosEsp=0
cuantasBoletasNiñosIng=0
cuantasBoletasNiñosHD=0
cuantasBoletasNiños3D=0
cuantasBoletasAdultosEsp=0
cuantasBoletasAdultosIng=0
cuantasBoletasAdultosHD=0
cuantasBoletasAdultos3D=0

def sala(sala1,sala2,sala3,sala4):
    print('''
        1. Sala con subtitulos en español
        2. Sala con subtitulos en inglés
        3. Películas HD
        4. Películas 3D
        ''')
    while salaConSubtitulosEspañol<361 and salaConSubtitulosIngles<361 and peliculasHD<361 and peliculas3D<361:
        opcionesCartelera=int(input("Por favor seleccione un tipo de boleta "))

        if (salaConSubtitulosEspañol>359 and opcionesCartelera==1):
            print("La sala está llena")
        elif opcionesCartelera==1:    
            añoNacimiento=int(input("¿en qué año naciste? "))
            edad = (2021-añoNacimiento)
            if (edad<18 and edad>0):
                cuantasBoletasSubEsp=int(input("¿cuántas boletas vas a comprar? "))
                precioBoletas=(cuantasBoletasSubEsp*precioNiño)
                cuantasBoletasNiñosEsp=(cuantasBoletasNiñosEsp+cuantasBoletasSubEsp)
                salaConSubtitulosEspañol=(salaConSubtitulosEspañol+cuantasBoletasSubEsp)
                print ("El precio de tus boletas es ", precioBoletas)
            if (edad>17 and edad<100):
                cuantasBoletasSubEsp=int(input("¿cuántas boletas vas a comprar? "))
                precioBoletas=(cuantasBoletasSubEsp*precioAdulto)
                cuantasBoletasAdultosEsp=(cuantasBoletasAdultosEsp+cuantasBoletasSubEsp)
                salaConSubtitulosEspañol=(salaConSubtitulosEspañol+cuantasBoletasSubEsp)
                print ("El precio de tus boletas es ", precioBoletas)
            if (edad<1 or edad>100):
                print ("Edad no válida")
        
        if (salaConSubtitulosIngles>359 and opcionesCartelera==2):
            print("La sala está llena")    
        elif opcionesCartelera==2:
            añoNacimiento=int(input("¿en qué año naciste? "))
            edad = (2021-añoNacimiento)
            if (edad<18 and edad>0):
                cuantasBoletasSubIng=int(input("¿cuántas boletas vas a comprar? "))
                precioBoletas=(cuantasBoletasSubIng*precioNiño)
                salaConSubtitulosIngles=(salaConSubtitulosIngles+cuantasBoletasSubIng)
                cuantasBoletasNiñosIng=(cuantasBoletasNiñosIng+cuantasBoletasSubIng)
                print ("El precio de tus boletas es ", precioBoletas)
            if (edad>17 and edad<100):
                cuantasBoletasSubIng=int(input("¿cuántas boletas vas a comprar? "))
                precioBoletas=(cuantasBoletasSubIng*precioAdulto)
                cuantasBoletasAdultosIngles=(cuantasBoletasAdultosIngles+cuantasBoletasSubIng)
                salaConSubtitulosIngles=(salaConSubtitulosIngles+cuantasBoletasSubIng)
                print ("El precio de tus boletas es ", precioBoletas)
            if (edad<1 or edad>100):
                print ("Edad no válida")

        if (peliculasHD>359 and opcionesCartelera==3):
            print("La sala está llena")
        elif opcionesCartelera==3:
            añoNacimiento=int(input("¿en qué año naciste? "))
            edad = (2021-añoNacimiento)
            if (edad<18 and edad>0):
                cuantasBoletasPeliHD=int(input("¿cuántas boletas vas a comprar? "))
                precioBoletas=(cuantasBoletasPeliHD*precioNiño)
                cuantasBoletasNiñosHD=(cuantasBoletasNiñosHD+cuantasBoletasPeliHD)
                peliculasHD=(peliculasHD+cuantasBoletasPeliHD)
                print ("El precio de tus boletas es ", precioBoletas)
            if (edad>17 and edad<100):
                cuantasBoletasPeliHD=int(input("¿cuántas boletas vas a comprar? "))
                precioBoletas=(cuantasBoletasPeliHD*precioAdulto)
                cuantasBoletasAdultosHD=(cuantasBoletasAdultosHD+cuantasBoletasPeliHD)
                peliculasHD=(peliculasHD+cuantasBoletasPeliHD)
                print ("El precio de tus boletas es ", precioBoletas)
            if (edad<1 or edad>100):
                print ("Edad no válida ")

        if (peliculas3D>359 and opcionesCartelera==4):
            print("La sala está llena ")
        elif opcionesCartelera==4:        
            añoNacimiento=int(input("¿en qué año naciste? "))
            edad = (2021-añoNacimiento)
            if (edad<18 and edad>0):
                cuantasBoletasPeli3D=int(input("¿cuántas boletas vas a comprar? "))
                precioBoletas=(cuantasBoletasPeli3D*precioNiño)
                cuantasBoletasNiños3D=(cuantasBoletasNiños3D+cuantasBoletasPeli3D)
                peliculas3D=(peliculas3D+cuantasBoletasPeli3D)
                print ("El precio de tus boletas es ", precioBoletas)
            if (edad>17 and edad<100):
                cuantasBoletasPeli3D=int(input("¿cuántas boletas vas a comprar? "))
                precioBoletas=(cuantasBoletasPeli3D*precioAdulto)
                cuantasBoletasAdultos3D=(cuantasBoletasAdultos3D+cuantasBoletasPeli3D)
                peliculas3D=(peliculas3D+cuantasBoletasPeli3D)
                print ("El precio de tus boletas es ", precioBoletas)
            if (edad<1 or edad>100):
                print ("Edad no válida ")
        recaudoBoletasNiñosEsp=(cuantasBoletasNiñosEsp*precioNiño)
        recaudoBoletasNiñosIng=(cuantasBoletasNiñosIng*precioNiño)
        recaudoBoletasNiñosHD=(cuantasBoletasNiñosHD*precioNiño)
        recaudoBoletasNiños3D=(cuantasBoletasNiños3D*precioNiño)
        recaudoBoletasAdultosEsp=(cuantasBoletasAdultosEsp*precioAdulto)
        recaudoBoletasAdultosIng=(cuantasBoletasAdultosIng*precioAdulto)
        recaudoBoletasAdultosHD=(cuantasBoletasAdultosHD*precioAdulto)
        recaudoBoletasAdultos3D=(cuantasBoletasAdultos3D*precioAdulto)
        dineroEspañol=(recaudoBoletasNiñosEsp+recaudoBoletasAdultosEsp)
        dineroIngles=(recaudoBoletasNiñosIng+recaudoBoletasAdultosIng)
        dineroHD=(recaudoBoletasNiñosHD+recaudoBoletasAdultosHD)
        dinero3D=(recaudoBoletasNiños3D+recaudoBoletasAdultos3D)
        recaudoTotalNiños=(recaudoBoletasNiñosEsp+recaudoBoletasNiñosIng+recaudoBoletasNiñosHD+recaudoBoletasNiños3D)
        recaudoTotalAdultos=(recaudoBoletasAdultosEsp+recaudoBoletasAdultosIng+recaudoBoletasAdultosHD+recaudoBoletasAdultos3D)
        recaudoTotal=(recaudoTotalNiños+recaudoTotalAdultos)
        recaudoSala1=(recaudoBoletasNiñosEsp+recaudoBoletasAdultosEsp)
        recaudoSala2=(recaudoBoletasNiñosIng+recaudoBoletasAdultosIng)
        recaudoSala3=(recaudoBoletasNiñosHD+recaudoBoletasAdultosHD)
        recaudoSala4=(recaudoBoletasNiños3D+recaudoBoletasAdultos3D)
        totalNiños=(cuantasBoletasNiñosEsp+cuantasBoletasNiñosIng+cuantasBoletasNiñosHD+cuantasBoletasNiños3D)
        totalAdultos=(cuantasBoletasAdultosEsp+cuantasBoletasAdultosIng+cuantasBoletasAdultosHD+cuantasBoletasAdultos3D)

    if (salaConSubtitulosEspañol>=360 and salaConSubtitulosIngles>=360 and peliculasHD>=360 and peliculas3D>=360) or (añoNacimiento==0):        
        break
        return (recaudoBoletasNiñosEsp,recaudoBoletasNiñosIng,recaudoBoletasNiñosHD,recaudoBoletasNiños3D,recaudoBoletasAdultosEsp,recaudoBoletasAdultosIng,recaudoBoletasAdultosHD,recaudoBoletasAdultos3D,dineroEspañol,dineroIngles,dineroHD,dinero3D,recaudoTotalNiños,recaudoTotalAdultos,recaudoTotal,recaudoSala1,recaudoSala2,recaudoSala3,recaudoSala4,totalNiños,totalAdultos
            print ("El número de niños que entraron a la sala 1 fueron ", cuantasBoletasNiñosEsp,", en la sala 2 es ", cuantasBoletasNiñosIng, ", en la sala 3 es ", cuantasBoletasNiñosHD, " y en la sala 4 es ", cuantasBoletasNiños3D)
            print ("La cantidad de dinero recaudado por niños en la sala 1 fue ", recaudoBoletasNiñosEsp,", en la sala 2 es ", recaudoBoletasNiñosIng, ", en la sala 3 es ", recaudoBoletasNiñosHD, " y en la sala 4 es ", recaudoBoletasNiños3D)
            print ("El total de dinero recaudado entre niños fue ", recaudoTotalNiños)
            print ("El número de adultos que entraron a la sala 1 fueron ", cuantasBoletasAdultosEsp,", en la sala 2 es ", cuantasBoletasAdultosIng, ", en la sala 3 es ", cuantasBoletasAdultosHD, " y en la sala 4 es ", cuantasBoletasAdultos3D)
            print ("La cantidad de dinero recaudado por adultos en la sala 1 fue ", recaudoBoletasAdultosEsp,", en la sala 2 es ", recaudoBoletasAdultosIng, ", en la sala 3 es ", recaudoBoletasAdultosHD, " y en la sala 4 es ", recaudoBoletasAdultos3D)
            print ("El total de dinero recaudado entre adultos fue ", recaudoTotalAdultos)
            print ("El total recaudado en la sala 1 es ", recaudoSala1,", en la sala 2 es ", recaudoSala2,", en la 3 es ",recaudoSala3," y en la 4 es ",recaudoSala4)
            print ("El total recaudado es ", recaudoTotal)
            print ("El total de niños que ingresaron es ", totalNiños)
            print ("El total de adultos que ingresaron es ", totalAdultos)

