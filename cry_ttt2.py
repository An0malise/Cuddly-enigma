
def  lgrd(number):
    grid=[]
    for a in range(0,9):
        if number-2*3**(8-a)>=0:
            number-=2*3**(8-a)
            grid.append(2)
        elif number-3**(8-a)>=0:
            number-=3**(8-a)
            grid.append(1)
        else:
            grid.append(0)
    return(grid)
#test1: successful
#for i in range(0,100):
#    print(lgrd(i),i)
def cgrd(sth):
    re=[]
    if type(sth)==list:
        for a in sth:
            if a==0:
                re.append(0)
            elif a==1:
                re.append("x")
            elif a==2:
                re.append("o")
        print(re[0],re[1],re[2])
        print(re[3],re[4],re[5])
        print(re[6],re[7],re[8])
            
def encryptt(message,key=None):
    remort=[]
    for letter in message.lower():
        if letter==' ':
            remort.append(27)
        else:
            remort.append(ord(letter)-96)
    saves=[]
    if key:
        if not type(key)==str:
            key=str(key)
        for a in key:
            pass
    elif not key:
        b=0
        while b< len(remort):
            if b+2<len(remort)-1:
                #print(b,len(remort))
                saves.append(remort[b]*remort[b+1]*remort[b+2])
            elif b+1<len(remort)-1:
                saves.append(remort[b]*remort[b+1])
            else:
                 saves.append(remort[b])
            b+=3
        
        return saves

    
    #y=len(mort)
    #while y>0:
    #    return construct_grd(mort[y-1]*mort[y-2]*mort[y-3])
    
for z in (encryptt("Hallo ich wuensche euch gleuck bei english")):
    cgrd(lgrd(z))
