import sys

n=int(sys.argv[1])
for number in range(n+1):
    print( (n-number)*" " + number* "#")
