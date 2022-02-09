casosPR=int(input(""))


for i in range (0,casosPR):
    dosentradas=input()
    a, b= dosentradas.split()
    a=str(a)
    b=str(b)
    if(a=="papel" and b=="piedra"):
        print("¡LaVidaEsdura!")
    if(a=="Piedra" and b=="lagarto"):
        print("¡LaVidaEsdura!")
    if(a=="tijeras" and b=="Papel"):
        print("¡LaVidaEsdura!")
    if(a=="lagarto" and b=="Holk"):
        print("¡LaVidaEsdura!")
    if(a=="Holk" and b=="Tijeras"):
        print("¡LaVidaEsdura!")
    if(a=="tijeras" and b=="lagarto"):
        print("¡LaVidaEsdura!")
    if(a=="lagarto" and b=="papel"):
        print("¡LaVidaEsdura!")
    if(a=="papel" and b=="Holk"):
        print("¡LaVidaEsdura!")
    if(a=="Holk" and b=="Piedra"):
        print("¡LaVidaEsdura!")
    if(a=="piedra" and b=="t"):
        print("¡LaVidaEsdura!")
    else:
        print("¡Siempre hay un proxiamo semestre!")
        

    

