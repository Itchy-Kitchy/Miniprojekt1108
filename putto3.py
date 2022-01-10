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
##    global talalatlista
##    global huzottlista
##    global megjatszottlista
    x=0
    y=0
    for i in range(0,len(huzottlista)):
        if i!=0:
            for a in range(1,len(megjatszottlista)):
                if (huzottlista[i]==megjatszottlista[a]):
                    talalatlista2.append(1)
                    x+=1
        if i==0:
            for b in range(0,1,1):
                if(huzottlista[i]==megjatszottlista[b]):
                    y=1
                
                    
    talalatlista.append(x)
    talalatlista.append(y)
    
        
    
    
    

print(in_putok2())
print(in_putok3())
print(talalat())


