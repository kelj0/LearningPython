polje=[5][9]

# 012345678XY
# X | X | X 0
# --+---+-- 1
# X | X | X 2
# --+---+-- 3 
# X | X | X 4


for y in range(0,5):
    for x in range(0,9):
        if ((y==0 or y==2 or y==4) and (x==2 or x==6)): 
            polje[y][x]='|'
        elif ((y==0 or y==2 or y==4) and (x==0 or x==4 or x==8)):
            polje[y][x]='X'
        elif ((y==1 or y==3)):
            if x==2 or x==6:
                polje[y][x]='+'
            else:
                polje[y][x]='-'
        else:
            polje[y][x]=' '

for y in range(0,5):
    for x in range(0,9):
        print(polje[y][x])
        