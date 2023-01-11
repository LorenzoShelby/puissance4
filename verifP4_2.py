def verifh(M,a=0,b=0):
    for j in range(a,6):
        for i in range(b,4):
                if M[j][i]==M[j][i+1] and M[j][i]==M[j][i+2]  and M[j][i] != 0:
                    print('verifh',M[j][i],M[j][i+1],M[j][i+2])
                    print(j,i)
                    if j!=5 :
                        if M[j+1][i+3]==0:
                            return verifh2(M,j,i+1)
                        elif M[j+1][i-1]==0:
                            return verifh2(M,j,i+1)
                    else:
                            if M[j][i+3] == 0:
                                return i+3
                            elif M[j][i-1] == 0:
                                return i-1
    return None

def verifh2(M,a=0,b=0):
    for j in range(a,6):
        for i in range(b,4):
                if M[j][i]==M[j][i+1] and M[j][i]==M[j][i+2]  and M[j][i] != 0:
                    print(j,i)
                    if j!=5 :
                        if M[j+1][i+3]!=0 and  i!=4:
                            return i+3
                        elif M[j+1][i-1]!=0:
                            return i-1
                    else:
                            if M[j][i+3] == 0:
                                return i+3
                            elif M[j][i-1] == 0:
                                return i-1
    return None

def verifv(M):
    for j in range(len(M)):
        for i in range(7):
                if M[j][i] == M[j-1][i] and M[j][i]== M[j-2][i] and M[j][i] != 0 and M[j-3][i] ==0 :
                    print('verifv')
                    return i
    return None

def verifdd(M):
    for j in range(len(M)):
        for i in range(4):
                if M[j][i]==M[j-1][i+1] and M[j][i]==M[j-2][i+2]  and M[j][i] != 0 and M[j-2][i+3] != 0:
                    print('verifdd')
                    return i+3
    return None

def verifdg(M):
    for j in range(len(M)):
        for i in range(3,7):
                if M[j][i]==M[j-1][i-1] and M[j][i]==M[j-2][i-2] and M[j][i] != 0 and M[j-2][i-3] != 0:
                    print('verifdg')
                    return i-3
    return None


def verif(M):
    if verifh(M) != None:
        return verifh(M)*100
    elif verifv(M) != None:
        return verifv(M)*100
    elif verifdd(M) != None:
        return verifdd(M)*100
    elif verifdg(M) != None:
        return verifdg(M)*100
    return None