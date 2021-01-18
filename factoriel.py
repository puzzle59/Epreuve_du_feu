import sys 

facto=int(sys.argv[1])
def factor(n):
    if n >0:
        if n==1:

            return 1
        else:
            return n*factor(n-1)

print(factor(facto))        
