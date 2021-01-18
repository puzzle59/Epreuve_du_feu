import sys
i=1
list_to_be_sorted=[]
while i<len(sys.argv) :

    list_to_be_sorted.append(int(sys.argv[i]))
    i+=1
# ok récupéré liste print(list_to_be_sorted)
# longueur argumentslen(sys.argv)
#print(list_to_be_sorted)
def tri(list):
    #ex pour mise en perspective 
    # for if (list[0] < list[1]):
    #     cache=list[0]
    #     list[0]=list[1]
    #     list[1]=cache
    # print(list)
    for compt_1 in range (len(list)):
        print(compt_1)
        for compt_2 in range (compt_1+1,len(list)):
            if list[compt_1]< list[compt_2]:
                cache=list[compt_1]
                list[compt_1]=list[compt_2]
                list[compt_2]=cache
    print(list)
tri(list_to_be_sorted)
