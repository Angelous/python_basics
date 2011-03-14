FE = 1
SE = 1
 
n = input("Enter number of fibb element ")
 
i = 2 
while i < n:
    SUM = SE + FE
    FE = SE
    SE = SUM
    print SUM
    i += 1