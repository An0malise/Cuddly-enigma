#
#

def  construct_grd(numkey):
    grid=[]
    a=8
    while a>=0:
        if numkey-2*3<*a>=0:
            numkey-=2*3**a
            grid.insert(len(grid),"Y")
        elif numkey-3**a>=0:
            numkey-=3**a
            grid.insert(len(grid),"X")
        else:
            grid.insert(len(grid),0)
        a-=1
    print(grid[0],grid[1],grid[2])
    print(grid[3],grid[4],grid[5])
    print(grid[6],grid[7],grid[8])
    return(grid)

def encryptt(message):
    mort=[]
    for letter in message:
        if letter==' ':
            mort.append(27)
        else:
            mort.append(ord(letter)-96)
        print(mort)
    y=len(mort)
    while y>0:
        construct_grd(mort[y-1]*mort[y-2]*mort[y-3]*mort[y-4])
        y-=4
        
def deconstruct(grid):
    l=0
    save=0
    while l<9:
        if grid[l]==0:
            pass
        elif grid[l]=="X":
            save+=3**(9-l)
        elif grid[l]=="Y":
            save+=2*3**(9-l)
        l+=1
        print(save)
    print(save)
         
def decryptt(code):
    runtime= 0
    while runtime>len(code):
        if code[runtime]==0:
            pass
        runtime+=1


        
#encryptt("abcde")
construct_grd(int( input("Photosanthjesus ") ))
#deconstruct(
