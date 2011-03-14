FE = input("Enter First Fibb element ")
SE = input("Enter Second Fibb element ")
 
n = input("Enter number of fibb element ")
 
i = 2 
while i < n:
    SUM = SE + FE
    FE = SE
    SE = SUM
    i += 1
 
print "Expected Element Value is",(SUM)