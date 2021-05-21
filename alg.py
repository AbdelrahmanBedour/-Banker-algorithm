def safety(N,M,Aval,Alloc,Need):
    work= Aval.copy()
    finish = []
    seq=[]
    for i in range(N):
        finish.append(False)
    while(True):
        Bcond=1
        for i in range (N):
            cond=1
            for j in range(M):
                if Need[i][j]>work[j]:
                    cond=0


            if finish[i] == False and cond :
                Bcond=0
                for j in range(M):
                    work[j] += Alloc[i][j]
                finish[i]=True
                seq.append(i)

        if Bcond:
            break

    safe = 1
    for i in range(N):
        if finish[i] == False:
            safe = 0
            break
    return safe,seq

def request(N,M, Aval, Alloc, Need,Index,Req):
    safe=0
    seq=[]
    result=1
    cond=1
    for i in range(M):
        if not (Req[i]<=Need[Index][i]):
            cond=0
            result=-1

    if cond==1 :
        for i in range(M):
            if not (Req[i] <= Aval[i]):
                cond = 0
                result = 0
    if cond==1:
        for i in range(M):
            Aval[i]-= Req[i]
            Alloc[Index][i] += Req[i]
            Need[Index][i] -= Req[i]
        safe,seq=safety(N,M, Aval, Alloc, Need)
    return result,safe,seq