#desastres de if:

import math



def verificarCedula (numeroCedula):

   if (numeroCedula<10000000 or numeroCedula>99999999):
      print ("Cédula inválida.")
      quit()
   if (numeroCedula>=10000000 and numeroCedula<=99999999):
      print ("Cédula válida.")   

def cajero (plata):
   print ("Tu dinero es ",plata)
   if (plata>=100000):
     billetes100k=math.trunc(plata/100000)     
     diezKs=(plata-(billetes100k*100000))
     print (" y te hemos entregado ",billetes100k, "billetes de 100mil")
     if (diezKs>=90000 and diezKs<100000):
         billetes50k=1
         billetes20k=2
         billetes10k=0
     if (diezKs>=80000 and diezKs<90000):
         billetes50k=1
         billetes20k=1
         billetes10k=1
     if (diezKs>=70000 and diezKs<80000):
         billetes20k=1
         billetes50k=1
         billetes10k=0
     if (diezKs>=60000 and diezKs<70000):
         billetes10k=1
         billetes20k=0
         billetes50k=1
     if (diezKs>=50000 and diezKs<60000):
         billetes50k=1
         billetes20k=0
         billetes10k=0
     if (diezKs>=40000 and diezKs<50000):
         billetes20k=2
         billetes50k=0
         billetes20k=0
     if (diezKs>=30000 and diezKs<40000):
         billetes20k=1
         billetes10k=1
         billetes50k=0
     if (diezKs>=20000 and diezKs<30000):
         billetes20k=1
         billetes50k=0
         billetes10k=0
     if (diezKs>=10000 and diezKs<20000):
         billetes10k=1
         billetes50k=0
         billetes20k=0
     if (diezKs<10000):
         billetes10k=0
         billetes50k=0
         billetes20k=0
     unidadKs=(diezKs-((math.trunc(diezKs/10000))*10000))
     print (billetes50k," billetes de 50mil, ",billetes20k,
           " billetes de 20mil, ", billetes10k, " billetes de 10mil")        
     if (unidadKs>=9000 and unidadKs<10000):
         billetes5k=1
         billetes2k=2
         billetes1k=0
     if (unidadKs>=8000 and unidadKs<9000):
         billetes5k=1
         billetes2k=1
         billetes1k=1
     if (unidadKs>=7000 and unidadKs<8000):
         billetes2k=1
         billetes5k=1
         billetes1k=0
     if (unidadKs>=6000 and unidadKs<7000):
         billetes1k=1
         billetes5k=1
         billetes2k=0
     if (unidadKs>=5000 and unidadKs<6000):
         billetes5k=1
         billetes2k=0
         billetes1k=0
     if (unidadKs>=4000 and unidadKs<5000):
         billetes2k=2
         billetes5k=0
         billetes1k=0
     if (unidadKs>=3000 and unidadKs<4000):
         billetes2k=1
         billetes1k=1
         billetes5k=0
     if (unidadKs>=2000 and unidadKs<3000):
         billetes2k=1
         billetes5k=0
         billetes1k=0
     if (unidadKs>=1000 and unidadKs<2000):
         billetes1k=1
         billetes5k=0
         billetes2k=0
     if (unidadKs<1000):
         billetes5k=0
         billetes2k=0
         billetes1k=0
     cientosPesos=(unidadKs-((math.trunc(unidadKs/1000))*1000))
     print (billetes5k," billetes de 5mil, ", billetes2k, " billetes de 2mil, ",billetes1k,
          " billetes de mil, ")
     if (cientosPesos>=900 and cientosPesos<1000):
         monedas500=1
         monedas200=2
         monedas100=0
     if (cientosPesos>=800 and cientosPesos<900):
         monedas500=1
         monedas200=1
         monedas100=1
     if (cientosPesos>=700 and cientosPesos<800):
         monedas200=1
         monedas500=1
         monedas100=0
     if (cientosPesos>=600 and cientosPesos<700):
         monedas100=1
         monedas500=1
         monedas200=0
     if (cientosPesos>=500 and cientosPesos<600):
         monedas500=1
         monedas200=0
         monedas100=0
     if (cientosPesos>=400 and cientosPesos<500):
         monedas200=2
         monedas500=0
         mondeas100=0
     if (cientosPesos>=300 and cientosPesos<400):
         monedas200=1
         monedas100=1
         monedas500=0
     if (cientosPesos>=200 and cientosPesos<300):
         monedas200=1
         monedas500=0
         monedas100=0
     if (cientosPesos>=100 and cientosPesos<200):
         monedas100=1
         monedas500=0
         monedas200=0
     if (cientosPesos<100):
         monedas500=0
         monedas200=0
         monedas100=0
     decenasPesos=(cientosPesos-((math.trunc(cientosPesos/100))*100))
     print  (monedas500, " monedas de 500, ", monedas200,
              " monedas de 200, ", monedas100, " monedas de 100")
     if (decenasPesos>=90 and decenasPesos<100):
         monedas50=1
         monedas20=2
         monedas10=0
     if (decenasPesos>=80 and decenasPesos<90):
         monedas50=1
         monedas20=1
         monedas10=1
     if (decenasPesos>=70 and decenasPesos<80):
         monedas20=1
         monedas50=1
         monedas10=0
     if (decenasPesos>=60 and decenasPesos<70):
         monedas10=1
         monedas50=1
         monedas20=0
     if (decenasPesos>=50 and decenasPesos<60):
         monedas50=1
         monedas20=0
         monedas10=0
     if (decenasPesos>=40 and decenasPesos<50):
         monedas20=2
         monedas10=0
         monedas50=0
     if (decenasPesos>=30 and decenasPesos<40):
         monedas20=1
         monedas10=1
         monedas50=0
     if (decenasPesos>=20 and decenasPesos<30):
         monedas20=1
         monedas50=0
         monedas10=0
     if (decenasPesos>=10 and decenasPesos<20):
         monedas10=1
         monedas50=0
         monedas20=0
     if (decenasPesos<10):
         monedas50=0
         monedas20=0
         monedas10=0
     print (monedas50," monedas de 50, ", monedas20, "monedas de 20, ",monedas10, "monedas de 10.")

   if (plata<100000):
     diezKs=(plata)     
     if (diezKs>=90000 and diezKs<100000):
         billetes50k=1
         billetes20k=2
         billetes10k=0
     if (diezKs>=80000 and diezKs<90000):
         billetes50k=1
         billetes20k=1
         billetes10k=1
     if (diezKs>=70000 and diezKs<80000):
         billetes20k=1
         billetes50k=1
         billetes10k=0
     if (diezKs>=60000 and diezKs<70000):
         billetes10k=1
         billetes20k=0
         billetes50k=1
     if (diezKs>=50000 and diezKs<60000):
         billetes50k=1
         billetes20k=0
         billetes10k=0
     if (diezKs>=40000 and diezKs<50000):
         billetes20k=2
         billetes50k=0
         billetes20k=0
     if (diezKs>=30000 and diezKs<40000):
         billetes20k=1
         billetes10k=1
         billetes50k=0
     if (diezKs>=20000 and diezKs<30000):
         billetes20k=1
         billetes50k=0
         billetes10k=0
     if (diezKs>=10000 and diezKs<20000):
         billetes10k=1
         billetes50k=0
         billetes20k=0
     if (diezKs<10000):
         billetes10k=0
         billetes50k=0
         billetes20k=0
     unidadKs=(diezKs-((math.trunc(diezKs/10000))*10000))
     print ("y te hemos entregado ",billetes50k," billetes de 50mil, ",billetes20k,
           " billetes de 20mil, ", billetes10k, " billetes de 10mil")        
     if (unidadKs>=9000 and unidadKs<10000):
         billetes5k=1
         billetes2k=2
         billetes1k=0
     if (unidadKs>=8000 and unidadKs<9000):
         billetes5k=1
         billetes2k=1
         billetes1k=1
     if (unidadKs>=7000 and unidadKs<8000):
         billetes2k=1
         billetes5k=1
         billetes1k=0
     if (unidadKs>=6000 and unidadKs<7000):
         billetes1k=1
         billetes5k=1
         billetes2k=0
     if (unidadKs>=5000 and unidadKs<6000):
         billetes5k=1
         billetes2k=0
         billetes1k=0
     if (unidadKs>=4000 and unidadKs<5000):
         billetes2k=2
         billetes5k=0
         billetes1k=0
     if (unidadKs>=3000 and unidadKs<4000):
         billetes2k=1
         billetes1k=1
         billetes5k=0
     if (unidadKs>=2000 and unidadKs<3000):
         billetes2k=1
         billetes5k=0
         billetes1k=0
     if (unidadKs>=1000 and unidadKs<2000):
         billetes1k=1
         billetes5k=0
         billetes2k=0
     if (unidadKs<1000):
         billetes5k=0
         billetes2k=0
         billetes1k=0
     cientosPesos=(unidadKs-((math.trunc(unidadKs/1000))*1000))
     print (billetes5k," billetes de 5mil, ", billetes2k, " billetes de 2mil, ",billetes1k,
          " billetes de mil, ")
     if (cientosPesos>=900 and cientosPesos<1000):
         monedas500=1
         monedas200=2
         monedas100=0
     if (cientosPesos>=800 and cientosPesos<900):
         monedas500=1
         monedas200=1
         monedas100=1
     if (cientosPesos>=700 and cientosPesos<800):
         monedas200=1
         monedas500=1
         monedas100=0
     if (cientosPesos>=600 and cientosPesos<700):
         monedas100=1
         monedas500=1
         monedas200=0
     if (cientosPesos>=500 and cientosPesos<600):
         monedas500=1
         monedas200=0
         monedas100=0
     if (cientosPesos>=400 and cientosPesos<500):
         monedas200=2
         monedas500=0
         mondeas100=0
     if (cientosPesos>=300 and cientosPesos<400):
         monedas200=1
         monedas100=1
         monedas500=0
     if (cientosPesos>=200 and cientosPesos<300):
         monedas200=1
         monedas500=0
         monedas100=0
     if (cientosPesos>=100 and cientosPesos<200):
         monedas100=1
         monedas500=0
         monedas200=0
     if (cientosPesos<100):
         monedas500=0
         monedas200=0
         monedas100=0
     decenasPesos=(cientosPesos-((math.trunc(cientosPesos/100))*100))
     print  (monedas500, " monedas de 500, ", monedas200,
              " monedas de 200, ", monedas100, " monedas de 100")
     if (decenasPesos>=90 and decenasPesos<100):
         monedas50=1
         monedas20=2
         monedas10=0
     if (decenasPesos>=80 and decenasPesos<90):
         monedas50=1
         monedas20=1
         monedas10=1
     if (decenasPesos>=70 and decenasPesos<80):
         monedas20=1
         monedas50=1
         monedas10=0
     if (decenasPesos>=60 and decenasPesos<70):
         monedas10=1
         monedas50=1
         monedas20=0
     if (decenasPesos>=50 and decenasPesos<60):
         monedas50=1
         monedas20=0
         monedas10=0
     if (decenasPesos>=40 and decenasPesos<50):
         monedas20=2
         monedas10=0
         monedas50=0
     if (decenasPesos>=30 and decenasPesos<40):
         monedas20=1
         monedas10=1
         monedas50=0
     if (decenasPesos>=20 and decenasPesos<30):
         monedas20=1
         monedas50=0
         monedas10=0
     if (decenasPesos>=10 and decenasPesos<20):
         monedas10=1
         monedas50=0
         monedas20=0
     if (decenasPesos<10):
         monedas50=0
         monedas20=0
         monedas10=0
     print (monedas50," monedas de 50, ", monedas20, "monedas de 20, ",monedas10, "monedas de 10.")

   if (plata<10000):
     unidadKs=(plata)       
     if (unidadKs>=9000 and unidadKs<10000):
         billetes5k=1
         billetes2k=2
         billetes1k=0
     if (unidadKs>=8000 and unidadKs<9000):
         billetes5k=1
         billetes2k=1
         billetes1k=1
     if (unidadKs>=7000 and unidadKs<8000):
         billetes2k=1
         billetes5k=1
         billetes1k=0
     if (unidadKs>=6000 and unidadKs<7000):
         billetes1k=1
         billetes5k=1
         billetes2k=0
     if (unidadKs>=5000 and unidadKs<6000):
         billetes5k=1
         billetes2k=0
         billetes1k=0
     if (unidadKs>=4000 and unidadKs<5000):
         billetes2k=2
         billetes5k=0
         billetes1k=0
     if (unidadKs>=3000 and unidadKs<4000):
         billetes2k=1
         billetes1k=1
         billetes5k=0
     if (unidadKs>=2000 and unidadKs<3000):
         billetes2k=1
         billetes5k=0
         billetes1k=0
     if (unidadKs>=1000 and unidadKs<2000):
         billetes1k=1
         billetes5k=0
         billetes2k=0
     if (unidadKs<1000):
         billetes5k=0
         billetes2k=0
         billetes1k=0
     cientosPesos=(unidadKs-((math.trunc(unidadKs/1000))*1000))
     print (billetes5k," billetes de 5mil, ", billetes2k, " billetes de 2mil, ",billetes1k,
          " billetes de mil, ")
     if (cientosPesos>=900 and cientosPesos<1000):
         monedas500=1
         monedas200=2
         monedas100=0
     if (cientosPesos>=800 and cientosPesos<900):
         monedas500=1
         monedas200=1
         monedas100=1
     if (cientosPesos>=700 and cientosPesos<800):
         monedas200=1
         monedas500=1
         monedas100=0
     if (cientosPesos>=600 and cientosPesos<700):
         monedas100=1
         monedas500=1
         monedas200=0
     if (cientosPesos>=500 and cientosPesos<600):
         monedas500=1
         monedas200=0
         monedas100=0
     if (cientosPesos>=400 and cientosPesos<500):
         monedas200=2
         monedas500=0
         mondeas100=0
     if (cientosPesos>=300 and cientosPesos<400):
         monedas200=1
         monedas100=1
         monedas500=0
     if (cientosPesos>=200 and cientosPesos<300):
         monedas200=1
         monedas500=0
         monedas100=0
     if (cientosPesos>=100 and cientosPesos<200):
         monedas100=1
         monedas500=0
         monedas200=0
     if (cientosPesos<100):
         monedas500=0
         monedas200=0
         monedas100=0
     decenasPesos=(cientosPesos-((math.trunc(cientosPesos/100))*100))
     print  (monedas500, " monedas de 500, ", monedas200,
              " monedas de 200, ", monedas100, " monedas de 100")
     if (decenasPesos>=90 and decenasPesos<100):
         monedas50=1
         monedas20=2
         monedas10=0
     if (decenasPesos>=80 and decenasPesos<90):
         monedas50=1
         monedas20=1
         monedas10=1
     if (decenasPesos>=70 and decenasPesos<80):
         monedas20=1
         monedas50=1
         monedas10=0
     if (decenasPesos>=60 and decenasPesos<70):
         monedas10=1
         monedas50=1
         monedas20=0
     if (decenasPesos>=50 and decenasPesos<60):
         monedas50=1
         monedas20=0
         monedas10=0
     if (decenasPesos>=40 and decenasPesos<50):
         monedas20=2
         monedas10=0
         monedas50=0
     if (decenasPesos>=30 and decenasPesos<40):
         monedas20=1
         monedas10=1
         monedas50=0
     if (decenasPesos>=20 and decenasPesos<30):
         monedas20=1
         monedas50=0
         monedas10=0
     if (decenasPesos>=10 and decenasPesos<20):
         monedas10=1
         monedas50=0
         monedas20=0
     if (decenasPesos<10):
         monedas50=0
         monedas20=0
         monedas10=0
     print (monedas50," monedas de 50, ", monedas20, "monedas de 20, ",monedas10, "monedas de 10.")

   if (plata<1000):
     cientosPesos=(plata)
     if (cientosPesos>=900 and cientosPesos<1000):
         monedas500=1
         monedas200=2
         monedas100=0
     if (cientosPesos>=800 and cientosPesos<900):
         monedas500=1
         monedas200=1
         monedas100=1
     if (cientosPesos>=700 and cientosPesos<800):
         monedas200=1
         monedas500=1
         monedas100=0
     if (cientosPesos>=600 and cientosPesos<700):
         monedas100=1
         monedas500=1
         monedas200=0
     if (cientosPesos>=500 and cientosPesos<600):
         monedas500=1
         monedas200=0
         monedas100=0
     if (cientosPesos>=400 and cientosPesos<500):
         monedas200=2
         monedas500=0
         mondeas100=0
     if (cientosPesos>=300 and cientosPesos<400):
         monedas200=1
         monedas100=1
         monedas500=0
     if (cientosPesos>=200 and cientosPesos<300):
         monedas200=1
         monedas500=0
         monedas100=0
     if (cientosPesos>=100 and cientosPesos<200):
         monedas100=1
         monedas500=0
         monedas200=0
     if (cientosPesos<100):
         monedas500=0
         monedas200=0
         monedas100=0
     decenasPesos=(cientosPesos-((math.trunc(cientosPesos/100))*100))
     print  (monedas500, " monedas de 500, ", monedas200,
              " monedas de 200, ", monedas100, " monedas de 100")
     if (decenasPesos>=90 and decenasPesos<100):
         monedas50=1
         monedas20=2
         monedas10=0
     if (decenasPesos>=80 and decenasPesos<90):
         monedas50=1
         monedas20=1
         monedas10=1
     if (decenasPesos>=70 and decenasPesos<80):
         monedas20=1
         monedas50=1
         monedas10=0
     if (decenasPesos>=60 and decenasPesos<70):
         monedas10=1
         monedas50=1
         monedas20=0
     if (decenasPesos>=50 and decenasPesos<60):
         monedas50=1
         monedas20=0
         monedas10=0
     if (decenasPesos>=40 and decenasPesos<50):
         monedas20=2
         monedas10=0
         monedas50=0
     if (decenasPesos>=30 and decenasPesos<40):
         monedas20=1
         monedas10=1
         monedas50=0
     if (decenasPesos>=20 and decenasPesos<30):
         monedas20=1
         monedas50=0
         monedas10=0
     if (decenasPesos>=10 and decenasPesos<20):
         monedas10=1
         monedas50=0
         monedas20=0
     if (decenasPesos<10):
         monedas50=0
         monedas20=0
         monedas10=0
     print (monedas50," monedas de 50, ", monedas20, "monedas de 20, ",monedas10, "monedas de 10.")

   if (plata<100):
     decenasPesos=(plata)     
     if (decenasPesos>=90 and decenasPesos<100):
         monedas50=1
         monedas20=2
         monedas10=0
     if (decenasPesos>=80 and decenasPesos<90):
         monedas50=1
         monedas20=1
         monedas10=1
     if (decenasPesos>=70 and decenasPesos<80):
         monedas20=1
         monedas50=1
         monedas10=0
     if (decenasPesos>=60 and decenasPesos<70):
         monedas10=1
         monedas50=1
         monedas20=0
     if (decenasPesos>=50 and decenasPesos<60):
         monedas50=1
         monedas20=0
         monedas10=0
     if (decenasPesos>=40 and decenasPesos<50):
         monedas20=2
         monedas10=0
         monedas50=0
     if (decenasPesos>=30 and decenasPesos<40):
         monedas20=1
         monedas10=1
         monedas50=0
     if (decenasPesos>=20 and decenasPesos<30):
         monedas20=1
         monedas50=0
         monedas10=0
     if (decenasPesos>=10 and decenasPesos<20):
         monedas10=1
         monedas50=0
         monedas20=0
     if (decenasPesos<10):
         monedas50=0
         monedas20=0
         monedas10=0
     print (monedas50," monedas de 50, ", monedas20, "monedas de 20, ",monedas10, "monedas de 10.")
   if (plata>=220000 and billetes100k>1 and billetes20k>=1):
         totalMasBono=(plata+10000)
         print ("agregamos 10mil pesos a tu dinero, ahora tu dinero es", totalMasBono)
   

#--------------------------------------------
#main

numeroCedula = int(input("Digite su cédula."))

verificarCedula(numeroCedula)

plata = int(input("Indica el dinero que deseas sacar."))

cajero (plata)

