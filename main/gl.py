import random

def tr():
    n = list(range(1,46))
    gamesets = []
    
    while len(n) >= 3:
        gameset=[]
        while len(gameset) <6:
    
            if len(n) > 3:
                i = random.randrange(0,len(n))
                gameset.append(n[i])
                n.pop(i)
              
        gameset.sort()
        gamesets.append(gameset)
        #print(gameset)
    
        if len(n) == 3:
    
            new_n = list(set(range(1,46)) - set(n))     
    
            for i in range(0,3):
                j = random.randrange(1,len(new_n))
                n.append(new_n[j])
                new_n.pop(j)
    
    
            #print(n)
            gamesets.append(n)
    
            break

#    return gamesets
    outputlist = []
    for game in gamesets:
        outputlist.append(str(game))

    return '\n'.join(outputlist)

if __name__ =='__main__':
    print(tr())

