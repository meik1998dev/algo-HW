# Optimal Solution_Final

def checkPriority(i, txt, used):
    with open(txt) as file:
        R = True
        for line in file:
            # split before and after ',' in each line of text
            #X1 = line.split('\n')
            #print(X1)
            X = line.split(',')
            
            if int(X[1]) == i:
                
                if used[int(X[0])-1][1] == 0: # Rawad was here
                    R = False
                    break
        # if the priority not ready in matrix used, return R
        return R


def readTime(txt, N):
    time = [0 for x in range(N)] 
    i=0
    with open(txt) as file:
        for line in file:
            X1 = line.split('\n')
            X = X1[0].split(',')                        
            time[i] = int(X[1])
            i=i+1
    return time

def F(i, used,tasks_links):
   
    if used[i-1][1] == 1:
        return False
    if not checkPriority(i,tasks_links,used):
        return False
    return True

def getbranch(i, txt):
    P = []
    with open(txt) as file:
        for line in file:
            # split before and after ',' in each line of text
            X1 = line.split('\n')
            X = X1[0].split(',')
            #print(X[0])
            if X[0] == str(i):
                P.append(int(X[1]))
    return P

def checkLen(pathLen, i, N,maxL):
    #print("111111")
    #print(maxL)
    if pathLen >= maxL:
        return False
    if i == N:
        return False
    return True

def update(usedNodes,usedPaths,steps,N):
    maxL = ((N - usedNodes) / 2 -(steps - usedPaths)) * 2 + 2
    #print(usedNodes)
    #print(usedPaths)
    #print(maxL)
    return maxL,usedNodes,usedPaths

import numpy as np
def G(i, currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia):
    currentPath = currentPath+str(i)+","
    # add node i to current path
    usedNodes += 1
    pathLen += 1
    #print(maxL)
    used[i-1][1]= 1
    if not checkLen(pathLen,  i, N,maxL):
        #print("4444")
        currentPath = currentPath+";"
        print(currentPath) #path is complete
        CP=''.join(currentPath.split())
        allSol = allSol+CP
        usedPaths += 1
        currentPath = ""
        #begin new path
        #print(maxL)
        [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia,N) # update max length for paths after completing one.
        
        #print("0")
        return usedNodes,usedPaths, maxL,allSol
    P = getbranch(i, tasklink)
   
    # get the following nodes exporting from current node
    if len(P) == 1:
        if F(P[0], used,tasklink):
            [usedNodes,usedPaths, maxL,allSol]= G(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
        else:
            #print("-----")
            currentPath = currentPath+";"
            print(currentPath) #path is complete
            CP=''.join(currentPath.split())
            allSol = allSol+CP
            usedPaths += 1
            currentPath = ""
            #print(maxL)
            [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia,N)
            
            return usedNodes,usedPaths, maxL,allSol
    elif len(P) == 2:
        
        if F(P[0], used,tasklink) and F(P[1], used,tasklink):            
            a=np.argmin((time[P[0]-1], time[P[1]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
        elif F(P[0], used,tasklink) and not F(P[1], used,):                       
            [usedNodes,usedPaths, maxL,allSol]= G(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
        elif F(P[1], used,tasklink) and not F(P[0], used,tasklink):                      
            [usedNodes,usedPaths, maxL,allSol]= G(P[1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
    elif len(P) == 3:
        if F(P[0], used,tasklink) and F(P[1], used,tasklink) and F(P[2], used,tasklink):
            a=np.argmin((time[P[0]-1], time[P[1]-1],time[P[2]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
        elif F(P[0], used,tasklink) and not F(P[1], used,tasklink) and not F(P[2], used,tasklink):
            [usedNodes,usedPaths, maxL,allSol]= G(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
        elif F(P[1], used,tasklink) and not F(P[0], used,tasklink) and not F(P[2], used,tasklink):
            [usedNodes,usedPaths, maxL,allSol]= G(P[1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
        elif F(P[2], used,tasklink) and not F(P[0], used,tasklink) and not F(P[1], used,tasklink):
            [usedNodes,usedPaths, maxL,allSol]= G(P[2], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
        elif F(P[0], used,tasklink) and F(P[1], used,tasklink) and not F(P[2], used,tasklink):
            a=np.argmin((time[P[0]-1], time[P[1]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
        elif F(P[2], used,tasklink) and F(P[1], used,tasklink) and not F(P[0], used,tasklink):
            a=np.argmin((time[P[1]-1], time[P[2]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G(P[a+1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            
        elif F(P[0], used,tasklink) and F(P[2], used,tasklink) and not F(P[1], used,tasklink):
            if (time[P[0]-1] < time[P[2]-1]):
                [usedNodes,usedPaths, maxL,allSol]= G(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            else:
                [usedNodes,usedPaths, maxL,allSol]= G(P[2], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
        else:                 
            currentPath = currentPath+";"
            print(currentPath) #path is complete
            CP=''.join(currentPath.split())
            allSol = allSol+CP
            usedPaths += 1            
            #print(maxL)
            [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia,N)           
            currentPath = ""
    return usedNodes,usedPaths, maxL,allSol





def run(N,wardia,task,tasklink):
        usedNodes=0
        usedPaths=0
       
        
        maxL=((N/2 - wardia)) * 2 + 2
        w, h = 2, N
        used = [[0 for x in range(w)] for y in range(h)]

        time = readTime(task,N)
        TotalTime = np.sum(time)
        TimeOneStep = TotalTime / wardia
        n=1
        allSol = ""
        while n<=N:    
            pathLen=0
            currentPath=""
            if F(n,used,tasklink)==True:        
                [usedNodes,usedPaths, maxL,allSol]=G(n, currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,tasklink,time,wardia)
            n=n+1
        Paths = allSol.split(';')
        with open('Optimal.txt', 'w') as file:
            tot_dif = 0
            wardiaTime = []
            for line in Paths:
                file.write(line+"\t")
                if line != '':                    
                    X=line[0:len(line)-1].split(',')
                    T = [time[int(i)-1] for i in X]
                    wardiaTime.append(sum(T))
                    file.write("Total Time= "+str(sum(T))+"\t") 
                    file.write("dif=  {:.2f}".format(abs(sum(T)-TimeOneStep))+"\n") 
                    tot_dif = tot_dif + abs(sum(T)-TimeOneStep)
            file.write("\n")
            file.write("Total Time = "+str(TotalTime)+"\n")
            file.write("Total_Time/Steps = {:.2f}".format(TotalTime/wardia)+"\n")
            file.write("Total differences = {:.2f}".format(tot_dif)+"\n")
            file.write("Average differences = {:.2f}".format(tot_dif/wardia)+"\n")
            file.write("Max Time = "+str(max(wardiaTime))+"\n")
            file.write("Min Time = "+str(min(wardiaTime))+"\n")
            file.write("------------------------------------\n") 
#run(8,3,"tasks.txt","tasks_links.txt")
         


                       
