import math

# n: pits m: balls
def get(n,m) :
    t = [[None]*(m+1) for i in range(0,n+1)]

    for i in range(0,m+1) :
        t[1][i] = 1

    for i in range(2,n+1) :
        for j in range(0,m+1) :
            tot =0;
            for k in range(0,j+1) :
                tot += t[i-1][j-k]
            t[i][j] = tot

    return t[n][m]

def endgame(b) :
    tot = 0;
<<<<<<< HEAD
    for i in range(0,b+1,2):
        tot += (get(12, i))*16
=======
    for i in range(2,b+1,2):
        tot += (get(12, i))*15
>>>>>>> 92f1a07f71c391e7fde6511da39048f8863245cf
        print("With",i,"beans on the board, there are",tot,"endgames.")
        print("Which is 10 to the",math.log10(tot),"or 2 to the",math.log2(tot))
        print("Which is",tot/1000000,"megabytes")

<<<<<<< HEAD
=======
#endgame(72)
#print(get(12,20)-get(6,20))
#print(get(10,99))
#print(2**31)
#print(10**10)
#print(2**63)
>>>>>>> 92f1a07f71c391e7fde6511da39048f8863245cf
#endgame(20)
#print(get(12,20)-get(6,20))
print(get(10,99))
#print(2**31)
