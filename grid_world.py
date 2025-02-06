N = 4
GOALS = [0,15]
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
            for moves in qVals[i]:
                
                if(moves == "left"):
                    val = -1+max(qVals[(i[0], i[1]-1)].values())
                    if(val!= qVals[i]["left"]):
                        valsChanged = True
                    qVals[i]["left"] = val
                
                if(moves == "right"):
                    val = -1+max(qVals[(i[0], i[1]+1)].values())
                    if(val!= qVals[i]["right"]):
                        valsChanged = True
                    qVals[i]["right"] = val

                if(moves == "up"):
                    val = -1+max(qVals[(i[0]-1, i[1])].values())
                    if(val!= qVals[i]["up"]):
                        valsChanged = True
                    qVals[i]["up"] = val

                if(moves == "down"):
                    val = -1+max(qVals[(i[0]+1, i[1])].values())
                    if(val!= qVals[i]["down"]):
                        valsChanged = True
                    qVals[i]["down"] = val
    return valsChanged

def print_nicely():
    lowestQVals = []
    for moves in qVals:
        val = max(qVals[moves].values())
        if(val>=0):
            lowestQVals.append(" " + str(val))
        else:
            lowestQVals.append(str(val))
    rowStr = ""
    for i in range(len(lowestQVals)):
        rowStr+=str(lowestQVals[i]) +" "
        if(i%N ==N-1):
            print(rowStr)
            rowStr = ""
    print("")


changed = True
while changed == True:
    changed=updateQVals()


print_nicely()
