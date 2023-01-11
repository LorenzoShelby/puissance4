def verifh(M):
    for j in range(len(M)):
        for i in range(4):
                if M[j][i]==M[j][i+1] and M[j][i]==M[j][i+2] and M[j][i]==M[j][i+3] and M[j][i] != 0:
                    return 1

def verifv(M):
    for j in range(len(M)):
        for i in range(7):
                if M[j][i]==M[j-1][i] and M[j][i]==M[j-3][i] and M[j][i]==M[j-2][i] and M[j-1][i] != 0:
                    return 1

def verifdd(M):
    for j in range(len(M)):
        for i in range(4):
                if M[j][i]==M[j-1][i+1] and M[j][i]==M[j-2][i+2] and M[j][i]==M[j-3][i+3] and M[j][i] != 0:
                    return 1

def verifdg(M):
    for j in range(len(M)):
        for i in range(3,7):
                if M[j][i]==M[j-1][i-1] and M[j][i]==M[j-2][i-2] and M[j][i]==M[j-3][i-3] and M[j][i] != 0:
                    return 1

def verifnull(M):
    if M[0][0] != 0 and M[0][1] != 0 and M[0][2] != 0 and M[0][3] != 0 and M[0][4] != 0 and M[0][5] != 0 and M[0][6] != 0  :
        return 4

def verif(M):
    if verifh(M)==1:
        return True
    elif verifv(M)==1:
        return True
    elif verifdd(M)==1:
        return True
    elif verifdg(M)==1:
        return True
    elif verifnull(M)==4:
        return 4
