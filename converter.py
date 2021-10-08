valor = float(input('Insira o valor: '))

if valor*4>=1:
    quarters=valor*4
    print("Quartes: ",int(quarters))
    valor2=(valor-int(quarters)*0.25)
    
    valor2 = float("%.2f" % round(valor2,2))
if float("%.2f" % round((valor-int(valor*4)*0.25),2))/0.1>=1:
    dimes=float("%.2f" % round((valor-int(valor*4)*0.25),2))/0.1
    print("Dimes: ", int(dimes))

if float("%.2f" % round((valor-(int(valor*4)*0.25+int(float("%.2f" % round((valor-int(valor*4)*0.25),2))/0.1)*0.1)),2))/0.05>=1:
    nickels=float("%.2f" % round((valor-(int(valor*4)*0.25+int(float("%.2f" % round((valor-int(valor*4)*0.25),2))/0.1)*0.1)),2))/0.05
    print("Nickels: ",int(nickels))
if float("%.2f" % round((valor-(int(valor*4)*0.25+int(float("%.2f" % round((valor-int(valor*4)*0.25),2))/0.1)*0.1+int(float("%.2f" % round((valor-(int(valor*4)*0.25+int(float("%.2f" % round((valor-int(valor*4)*0.25),2))/0.1)*0.1)),2))/0.05)*0.05)),2))/0.01>=1:
    pennies=float("%.2f" % round((valor-(int(valor*4)*0.25+int(float("%.2f" % round((valor-int(valor*4)*0.25),2))/0.1)*0.1+int(float("%.2f" % round((valor-(int(valor*4)*0.25+int(float("%.2f" % round((valor-int(valor*4)*0.25),2))/0.1)*0.1)),2))/0.05)*0.05)),2))/0.01
    print("Pennies: ",int(pennies))
                
Totalcents=valor*100
print("Total cents: ",int(Totalcents))
    
        
