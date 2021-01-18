import sys

string_init=sys.argv[1]
#   print(string1[0]) on peut indexer string en python

list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
full_list= list.copy()
for letter in list:
    full_list+=letter.upper()
full_list+=["é","è","ô","à"]
# liste avec les majuscules . print(full_list)
bool=True
string_finished=""
for item in string_init:
    if (item in full_list):
        if (bool==True):
            string_finished+=item.upper()
    #        print(type(item)) type str
            bool=False
        else:
            string_finished+= item.lower()
            bool=True
    else :
        string_finished += item
print (string_finished)
