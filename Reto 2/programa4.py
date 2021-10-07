
import math

def guardarNumero (numeroTresCifras):
    if (numeroTresCifras>=100 and numeroTresCifras<1000):
        cientos=math.trunc(numeroTresCifras/100)
        decenas=math.trunc((numeroTresCifras-(cientos*100))/10)
        unidades=(numeroTresCifras-((cientos*100)+(decenas*10)))
        if (cientos<decenas and decenas<unidades):
            maxDosDigitos=((unidades*10)+decenas)
            minDosDigitos=((cientos*10)+decenas)
        if (cientos<unidades and unidades<decenas):
            maxDosDigitos=((decenas*10)+unidades)
            minDosDigitos=((cientos*10)+unidades)
        if (decenas<cientos and cientos<unidades):
            maxDosDigitos=((unidades*10)+cientos)
            minDosDigitos=((decenas*10)+cientos)
        if (decenas<unidades and unidades<cientos):
            maxDosDigitos=((cientos*10)+unidades)
            minDosDigitos=((decenas*10)+unidades)
        if (unidades<cientos and cientos<decenas):
            maxDosDigitos=((decenas*10)+cientos)
            minDosDigitos=((unidades*10)+cientos)
        if (unidades<decenas and decenas<cientos):
            maxDosDigitos=((cientos*10)+decenas)
            minDosDigitos=((unidades*10)+decenas)
        if (unidades==decenas and decenas==cientos):
            maxDosDigitos=((unidades*10)+decenas)
            minDosDigitos=((cientos*10)+decenas)
        print ("numero correcto, el máximo valor de dos dígitos con esos dígitos es ",
               maxDosDigitos, " y el mínimo valor de dos dígitos con esos números es ",minDosDigitos)
    else:
        print ("numero incorrecto")
        quit()






#--------------------------------------------
#main

numeroTresCifras = int(input("Digite un numero de tres cifras."))

guardarNumero (numeroTresCifras)

