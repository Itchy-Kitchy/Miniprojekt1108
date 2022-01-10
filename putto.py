talalatlista=[]
talalatlista2=[]
huzottlista=[]
megjatszottlista=[]
##def in_putok():
##    for i in range(9):
##        a=int(input("Add meg a megjaszott szamokat, elöször 4-bol az 1-et majd a 20-bol 8-at"))
##        megjatszottlista.append(a)
##    for a in range(9):
##        b=int(input("Add meg a huzott szamokat, elöször 4-bol az 1-et majd a 20-bol 8-at"))
##        huzottlista.append(b)

def in_putok2():
    a=str(input("Megjatszott szamok: "))
    huzottlista=a.split(" ")
    for i in range(0, len(huzottlista)):
       huzottlista[i] = int(huzottlista[i])
    return huzottlista

def in_putok3():    
    b=str(input("Huzott szamok: "))
    megjatszottlista=b.split(" ")
    for i in range(0, len(megjatszottlista)):
       megjatszottlista[i] = int(megjatszottlista[i])
    return megjatszottlista

def talalat():
    global talalatlista
    global huzottlista
    global megjatszottlista
    x=0
    for i in range(1,len(huzottlista)):
        for a in range(1,len(megjatszottlista)):
            if (huzottlista[i]==megjatszottlista[a]):
                talalatlista2.append(1)
                x+=1
            else:
                pass
    talalatlista.append(x)
    if(huzottlista[0]==megjatszottlista[0]):
        talalatlista.append(1)
    else:
        talalatlista.append(0)

    
    

print(in_putok2())
print(in_putok3())
print(talalat())


