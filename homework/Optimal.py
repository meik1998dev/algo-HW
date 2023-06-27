# Optimal Solution

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
def checkPriority1(i, X1,X2, used):
        
        R = True
   #     print(len(X2))
        for j in range(len(X2)):
           
            if int(X2[j]) == i:
                
                if used[int(X1[j])-1][1] == 0: # Rawad was here
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

def F(i, used):
   
    if used[i-1][1] == 1:
        return False
    if not checkPriority(i,"tasks_links.txt",used):
        return False
    return True
def F1(i, used,X1,X2):
   # print(i) 
    if used[i-1][1] == 1:
        return False
    if not checkPriority1(i,X1,X2,used):
        return False
      
   # print("wjjew")
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
def getbranch1(i, X1,X2):
    P = []
    
    for j in range(len(X1)):
            # split before and after ',' in each line of text
           
            if X1[j] == str(i):
                P.append(int(X2[j]))
    return P


def checkLen(pathLen, i, N,maxL):
    #print("111111")
    #print(maxL)
    if pathLen >= maxL:
        return False
    if i == N:
        return False
    return True

def update(usedNodes,usedPaths,steps):
    maxL = ((N - usedNodes) / 2 -(steps - usedPaths)) * 2 + 2
    #print(usedNodes)
    #print(usedPaths)
    #print(maxL)
    return maxL,usedNodes,usedPaths

import numpy as np
def G(i, currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol):
   # print(maxL)
    currentPath = currentPath+str(i)+","
    # add node i to current path
    usedNodes += 1
    pathLen += 1
    #print(maxL)
    used[i-1][1]= 1
    if not checkLen(pathLen,  i, N,maxL):
        #print("4444")
        currentPath = currentPath+";"
    #    print(currentPath) #path is complete
        CP=''.join(currentPath.split())
        allSol = allSol+CP
        usedPaths += 1
        currentPath = ""
        #begin new path
        #print(maxL)
        [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia) # update max length for paths after completing one.
        
        #print("0")
        return usedNodes,usedPaths, maxL,allSol
    P = getbranch(i, 'tasks_links.txt')
   
    # get the following nodes exporting from current node
    if len(P) == 1:
        if F(P[0], used):
            [usedNodes,usedPaths, maxL,allSol]= G(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
        else:
            #print("-----")
            currentPath = currentPath+";"
     #       print(currentPath) #path is complete
            CP=''.join(currentPath.split())
            allSol = allSol+CP
            usedPaths += 1
            currentPath = ""
            #print(maxL)
            [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia)
            
            return usedNodes,usedPaths, maxL,allSol
    elif len(P) == 2:
        
        if F(P[0], used) and F(P[1], used):            
            a=np.argmin((time[P[0]-1], time[P[1]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
        elif F(P[0], used) and not F(P[1], used):                       
            [usedNodes,usedPaths, maxL,allSol]= G(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
        elif F(P[1], used) and not F(P[0], used):                      
            [usedNodes,usedPaths, maxL,allSol]= G(P[1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
    elif len(P) == 3:
        if F(P[0], used) and F(P[1], used) and F(P[2], used):
            a=np.argmin((time[P[0]-1], time[P[1]-1],time[P[2]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
        elif F(P[0], used) and not F(P[1], used) and not F(P[2], used):
            [usedNodes,usedPaths, maxL,allSol]= G(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
        elif F(P[1], used) and not F(P[0], used) and not F(P[2], used):
            [usedNodes,usedPaths, maxL,allSol]= G(P[1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
        elif F(P[2], used) and not F(P[0], used) and not F(P[1], used):
            [usedNodes,usedPaths, maxL,allSol]= G(P[2], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
        elif F(P[0], used) and F(P[1], used) and not F(P[2], used):
            a=np.argmin((time[P[0]-1], time[P[1]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
        elif F(P[2], used) and F(P[1], used) and not F(P[0], used):
            a=np.argmin((time[P[1]-1], time[P[2]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G(P[a+1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            
        elif F(P[0], used) and F(P[2], used) and not F(P[1], used):
            if (time[P[0]-1] < time[P[2]-1]):
                [usedNodes,usedPaths, maxL,allSol]= G(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
            else:
                [usedNodes,usedPaths, maxL,allSol]= G(P[2], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol)
        else:                 
            currentPath = currentPath+";"
           # print(currentPath) #path is complete
            CP=''.join(currentPath.split())
            allSol = allSol+CP
            usedPaths += 1            
            #print(maxL)
            [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia)           
            currentPath = ""
    return usedNodes,usedPaths, maxL,allSol
def G1(i, currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol,X1,X2,time):
    #print(maxL)
    print(i)
    currentPath = currentPath+str(i)+","
    # add node i to current path
    usedNodes += 1
    pathLen += 1
    #print(maxL)
    used[i-1][1]= 1
    if not checkLen(pathLen,  i, N,maxL):
        #print("4444")
        currentPath = currentPath+";"
      #  print(currentPath) #path is complete
        CP=''.join(currentPath.split())
        print("CP")
        print(CP)
        allSol = allSol+CP
        usedPaths += 1
        currentPath = ""
        #begin new path
        #print(maxL)
        [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia) # update max length for paths after completing one.
        
        #print("0")
        return usedNodes,usedPaths, maxL,allSol
    P = getbranch1(i, X1,X2)
    print(P)
   
    # get the following nodes exporting from current node
    if len(P) == 1:
        if F1(P[0], used, X1,X2):
            [usedNodes,usedPaths, maxL,allSol]= G1(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
        else:
            #print("-----")
            currentPath = currentPath+";"
            #print(currentPath) #path is complete
            CP=''.join(currentPath.split())
            allSol = allSol+CP
            usedPaths += 1
            currentPath = ""
            #print(maxL)
            [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia)
            
            return usedNodes,usedPaths, maxL,allSol
    elif len(P) == 2:
        #print(used)
        if F1(P[0], used, X1,X2) and F1(P[1], used, X1,X2):            
            a=np.argmin((time[P[0]-1], time[P[1]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G1(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            
            
        elif F1(P[0], used, X1,X2) and not F1(P[1], used, X1,X2):                       
            [usedNodes,usedPaths, maxL,allSol]= G1(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            
            
        elif F1(P[1], used, X1,X2) and not F1(P[0], used, X1,X2):                      
            [usedNodes,usedPaths, maxL,allSol]= G1(P[1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
           # print("Bbb")
            
    elif len(P) == 3:
        if F1(P[0], used, X1,X2) and F1(P[1], used, X1,X2) and F1(P[2], used, X1,X2):
            a=np.argmin((time[P[0]-1], time[P[1]-1],time[P[2]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G1(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            
        elif F1(P[0], used, X1,X2) and not F1(P[1], used, X1,X2) and not F1(P[2], used, X1,X2):
            [usedNodes,usedPaths, maxL,allSol]= G1(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            
        elif F1(P[1], used, X1,X2) and not F1(P[0], used, X1,X2) and not F1(P[2], used, X1,X2):
            [usedNodes,usedPaths, maxL,allSol]= G1(P[1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            
        elif F1(P[2], used, X1,X2) and not F1(P[0], used, X1,X2) and not F1(P[1], used, X1,X2):
            [usedNodes,usedPaths, maxL,allSol]= G1(P[2], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            
        elif F1(P[0], used, X1,X2) and F1(P[1], used, X1,X2) and not F1(P[2], used, X1,X2):
            a=np.argmin((time[P[0]-1], time[P[1]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G1(P[a], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            
        elif F1(P[2], used, X1,X2) and F1(P[1], used, X1,X2) and not F1(P[0], used, X1,X2):
            a=np.argmin((time[P[1]-1], time[P[2]-1]))
            [usedNodes,usedPaths, maxL,allSol]= G1(P[a+1], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            
        elif F1(P[0], used, X1,X2) and F1(P[2], used, X1,X2) and not F1(P[1], used, X1,X2):
            if (time[P[0]-1] < time[P[2]-1]):
                [usedNodes,usedPaths, maxL,allSol]= G1(P[0], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
            else:
                [usedNodes,usedPaths, maxL,allSol]= G1(P[2], currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
        else:                 
            currentPath = currentPath+";"
          #  print(currentPath) #path is complete
            CP=''.join(currentPath.split())
            allSol = allSol+CP
            usedPaths += 1            
            #print(maxL)
            [maxL,usedNodes,usedPaths] = update(usedNodes,usedPaths,wardia)           
            currentPath = ""
    return usedNodes,usedPaths, maxL,allSol


#time = readTime("tasks.txt",8)
N=8
wardia=3

def optimal(time,N,wardia, X1,X2):
        #print(N)
        n=1
        usedNodes=0
        usedPaths=0
        maxL=((N/2 - wardia)) * 2 + 2
        w, h = 2, N
        used = [[0 for x in range(w)] for y in range(h)]
        allSol = ""
        while n<=N:    
              #  print(N)
                pathLen=0
                currentPath=""
                if F1(n,used, X1,X2)==True:        
                        [usedNodes,usedPaths, maxL,allSol]=G1(n, currentPath, usedNodes, pathLen, used, maxL, usedPaths, N,allSol, X1,X2,time)
                n=n+1
                #print(n)
                Paths = allSol
        return Paths
#print(optimal(time,8,wardia))
