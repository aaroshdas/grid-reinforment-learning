N = 5
GOALS = [0]
QUICKSAND = [1,6,11,16]
MAGIC_ITEMS = [9,14,19]
NUM_MAGIC_ITEMS_NEEDED = 2
#(row, col) = {(up/down/left/right) = q val}
def create_tuples(lsOfTuples, currentTuple, length):
    if(len(currentTuple) == length):
        lsOfTuples.append(currentTuple)
    else:
        create_tuples(lsOfTuples, (False,) + currentTuple, length)
        create_tuples(lsOfTuples, (True,) + currentTuple, length)

t_f_tuples = []
create_tuples(t_f_tuples, (), len(MAGIC_ITEMS))

qVals = {}
for i in range(N*N):
    #row, col, tuples
    for t in t_f_tuples:
        state = (i//N, i%N) +t

        qVals[state]=  {}
        if(state[0] > 0):
            qVals[state]["up"] = 0
        if(state[0] < N-1):
            qVals[state]["down"] = 0
        if(state[1] > 0):
            qVals[state]["left"] = 0
        if(state[1] < N-1):
            qVals[state]["right"] = 0
def getMagicTuple(position, curTuple):
    new_tuple = ()
    if(position in MAGIC_ITEMS):
        for index in range(len(MAGIC_ITEMS)):
            if(MAGIC_ITEMS[index] == position):
                new_tuple = new_tuple + (True,)
            else:
                new_tuple = new_tuple + (curTuple[index],)
        return new_tuple
    return curTuple
            

def updateQVals():
    valsChanged = False
    for i in qVals.keys():
        if(i[0]*N+i[1] not in GOALS):
            coeff = -1
            if(i[0]*N+i[1] in QUICKSAND):
                coeff-=99

            for moves in qVals[i]:
                
                if(moves == "left"):

                    val = max(qVals[(i[0], i[1]-1) + getMagicTuple(i[0]*N+i[1], i[2:])].values())+coeff
                    if(val!= qVals[i]["left"]):
                        valsChanged = True
                
                    qVals[i]["left"] = val
                
                if(moves == "right"):
                    val = max(qVals[(i[0], i[1]+1)+ getMagicTuple(i[0]*N+i[1], i[2:])].values() )+coeff
                    if(val!= qVals[i]["right"]):
                        valsChanged = True
                    qVals[i]["right"] = val

                if(moves == "up"):
                    val = max(qVals[(i[0]-1, i[1])+ getMagicTuple(i[0]*N+i[1], i[2:])].values())+coeff
                    if(val!= qVals[i]["up"]):
                        valsChanged = True
                    qVals[i]["up"] = val

                if(moves == "down"):
                    val = max(qVals[(i[0]+1, i[1])+ getMagicTuple(i[0]*N+i[1], i[2:])].values())+coeff
                    if(val!= qVals[i]["down"]):
                        valsChanged = True
                    qVals[i]["down"] = val
        else:
            needed = NUM_MAGIC_ITEMS_NEEDED
            for k in i[2:]:
                if(k == True):
                    needed -=1
            if(needed>0):
                 for moves in qVals[i]:
                     qVals[i][moves] = -100000000
    return valsChanged

def print_nicely():
    maxQStates = []
    for i in qVals:
        if(True not in i[2:]):
            maxQStates.append(i)
    maxQVals = []
    for moves in maxQStates:
        val = max(qVals[moves].values())
        spacesStr = "" 
        for spaces in range(5-len(str(val))):
            spacesStr+=" "
        if(val<0):
            if(val <-100000):
                maxQVals.append(" x   ")
            else:
                maxQVals.append(str(val)+spacesStr)
        else:
            maxQVals.append(" "+str(val)+spacesStr[:-1])
    rowStr = ""
    for i in range(len(maxQVals)):
        rowStr+=str(maxQVals[i]) +" "
        if(i%N ==N-1):
            print(rowStr)
            print('')
            rowStr = ""
    print("")


changed = True
while changed == True:
    changed=updateQVals()


print_nicely()
