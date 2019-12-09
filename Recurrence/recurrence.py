def findParticularSolution(C,b):
    #insert code here
    n = 0
    k = 0

    for i in range(len(C)):
        k += C[i] * (b**(n+i))
    k = (b**n) / k

    return k









#
#
#
#
#
# findParticularSolution([2,-3,1], 3)