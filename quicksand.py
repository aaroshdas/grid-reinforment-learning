N = 5
GOALS = [0]
QUICKSAND = [1,6,11,16,23,18,13,8]
#(row, col) = {(up/down/left/right) = q val}
qVals = {}
for i in range(N*N):
    #row, col
    position = (i//N, i%N)

    qVals[position]=  {}
    if(position[0] > 0):
        qVals[position]["up"] = 0
    if(position[0] < N-1):
        qVals[position]["down"] = 0
    if(position[1] > 0):
        qVals[position]["left"] = 0
    if(position[1] < N-1):
        qVals[position]["right"] = 0
def updateQVals():
    valsChanged = False
    for i in qVals.keys():
        if(i[0]*N+i[1] not in GOALS):
            coeff = -1
            if(i[0]*N+i[1] in QUICKSAND):
                coeff-=100
            for moves in qVals[i]:
                
                if(moves == "left"):
                    val = max(qVals[(i[0], i[1]-1)].values())+coeff
                    if(val!= qVals[i]["left"]):
                        valsChanged = True
                    qVals[i]["left"] = val
                
                if(moves == "right"):
                    val = max(qVals[(i[0], i[1]+1)].values())+coeff
                    if(val!= qVals[i]["right"]):
                        valsChanged = True
                    qVals[i]["right"] = val

                if(moves == "up"):
                    val = max(qVals[(i[0]-1, i[1])].values())+coeff
                    if(val!= qVals[i]["up"]):
                        valsChanged = True
                    qVals[i]["up"] = val

                if(moves == "down"):
                    val = max(qVals[(i[0]+1, i[1])].values())+coeff
                    if(val!= qVals[i]["down"]):
                        valsChanged = True
                    qVals[i]["down"] = val
    return valsChanged

def print_nicely():
    lowestQVals = []
    for moves in qVals:
        val = max(qVals[moves].values())
        spacesStr = "" 
        for spaces in range(5-len(str(val))):
            spacesStr+=" "
        if(val<0):
            lowestQVals.append(str(val)+spacesStr)
        else:
            lowestQVals.append(" "+str(val)+spacesStr[:-1])
    rowStr = ""
    for i in range(len(lowestQVals)):
        rowStr+=str(lowestQVals[i]) +" "
        if(i%N ==N-1):
            print(rowStr)
            print('')
            rowStr = ""
    print("")


changed = True
while changed == True:
    changed=updateQVals()


print_nicely()
