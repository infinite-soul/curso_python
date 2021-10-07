
import math

def guardarNumero (numeroSeisCifras):
    if (numeroSeisCifras<100000 or numeroSeisCifras>999999):
        print ("Boleta inválida")
        quit()
    if (numeroSeisCifras>=100000 and numeroSeisCifras<1000000):        
        cienMiles=math.trunc(numeroSeisCifras/100000)
        diezMiles=math.trunc((numeroSeisCifras-(cienMiles*100000))/10000)
        miles=math.trunc((numeroSeisCifras-((cienMiles*100000)+(diezMiles*10000)))/1000)
        cientos=math.trunc((numeroSeisCifras-((cienMiles*100000)+(diezMiles*10000)+(miles*1000)))/100)
        decenas=math.trunc((numeroSeisCifras-((cienMiles*100000)+(diezMiles*10000)+(miles*1000)+(cientos*100)))/10)
        unidades=math.trunc((numeroSeisCifras-((cienMiles*100000)+(diezMiles*10000)+(miles*1000)+(cientos*100)+(decenas*10))))
        horario=(miles+cientos)
    if ((unidades+cienMiles)>5):
        print ("tu boleta es válida")
    if (diezMiles>0 and diezMiles<7):
        print (", el tipo de entrada es gramilla")        
    if (diezMiles==0 or (diezMiles>6 and diezMiles<=9)):
        print (", el tipo de entrada es general")        
    if (horario==1 or horario==3 or horario==5 or horario==7 or horario==9 or horario==11 or horario==13 or horario==15 or horario==17):
        print (", debes entrar por la puerta 2 a partir de las 8pm")
    if (horario==2 or horario==4 or horario==6 or horario== 8 or horario== 10 or horario== 12 or horario== 14 or horario== 16 or horario==18 or horario==0):
        print (", debes entrar por la puerta 1 a partir de las 7pm")            
    







#--------------------------------------------
#main

numeroSeisCifras = int(input("Digite un numero de seis cifras."))

guardarNumero (numeroSeisCifras)
