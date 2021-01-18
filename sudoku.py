import sys

#méthode de l'inclusion
#candidat: chiffre possible vu les alentours, sur une case
#but: calculer candidats , donc besoin fonction qui affiche
#ligne(i) colonne(j) carré(k)(9 lignes, 9 carrès..)
#la case où il n'y a qu'un candidat vaut ce candidat
#puis recalcul jusqu'à terminer
enonce=open(sys.argv[1],"r")
full_copy=[]
for ligne in enonce:
    full_copy+=([ligne])
enonce.close()
#print(full_copy)

def cleaning_arr(full_arr):
    clean_copy=[]

    liste_chiffre=["0","1","2","3","4","5","6","7","8","9","_"]
    for item in full_arr:
        clean_line=[]
        for item_deep in item:
            if item_deep in liste_chiffre:
                clean_line.append(item_deep)
        clean_copy+=[clean_line]
    for everything in clean_copy:
        if everything==[]:
            clean_copy.remove(everything)
    return clean_copy
cleaned_array=cleaning_arr(full_copy)

def print_tab(_copy):
    for item in _copy:
        print(item)
        print("\n")
def line_pointer(i,clean_array):
    #give the array line i , from 0 to 9
    #operationnal
    return clean_array[i]
def column_pointer(j,clean_array):
    #give the column, number j , from 0 to 9
    #operationnal
    column=[]
    for item in clean_array:
        column.append(item[j])
    return column
# def square_pointer(k,l,clean_array):
#     square=[]
#     for i in range(3):
#         square.append(clean_array[k//3+i][l//3+i])
#     return square
carre_1=line_pointer(0,cleaned_array)[0:3]+line_pointer(1,cleaned_array)[0:3]+line_pointer(2,cleaned_array)[0:3]
carre_2=line_pointer(0,cleaned_array)[3:6]+line_pointer(1,cleaned_array)[3:6]+line_pointer(2,cleaned_array)[3:6]
carre_3=line_pointer(0,cleaned_array)[6:]+line_pointer(1,cleaned_array)[6:]+line_pointer(2,cleaned_array)[6:]
################"
carre_4=line_pointer(3,cleaned_array)[0:3]+line_pointer(4,cleaned_array)[0:3]+line_pointer(5,cleaned_array)[0:3]
carre_5=line_pointer(3,cleaned_array)[3:6]+line_pointer(4,cleaned_array)[3:6]+line_pointer(5,cleaned_array)[3:6]
carre_6=line_pointer(3,cleaned_array)[6:]+line_pointer(4,cleaned_array)[6:]+line_pointer(5,cleaned_array)[6:]
############""
carre_7=line_pointer(6,cleaned_array)[0:3]+line_pointer(7,cleaned_array)[0:3]+line_pointer(8,cleaned_array)[0:3]
carre_8=line_pointer(6,cleaned_array)[3:6]+line_pointer(7,cleaned_array)[3:6]+line_pointer(8,cleaned_array)[3:6]
carre_9=line_pointer(6,cleaned_array)[6:]+line_pointer(7,cleaned_array)[6:]+line_pointer(8,cleaned_array)[6:]
######carres ok


def  wich_square(i,j):
    #une fonction qui dit dans quel carré est la case
    #assert, stabiliser le code , une autre fois
    if (i<3 and j <3):
        return 1
    elif (i<3 and (j>2 and j<6)):
        return 2
    elif (i<3 and (j>=6)):
        return 3
    elif ((i>2 and i <6) and j<3):
        return 4
    elif ((i>2 and i <6) and (j>=3 and j<6)):
        return 5
    elif ((i>2 and i <6) and (j>=6)):
        return 6
    elif ((i>=6) and (j<3)):
        return 7
    elif ((i>=6) and (j>=3 and j<6)):
        return 8
    elif ((i>=6) and (j>=6)):
        return 9
#######" c'est fonctionnel"
##
# maintenant , une fonction qui assigne chaque carré à son chiffre
def which_square_transp(digit):
    if digit==1:
        return carre_1
    elif digit==2:
        return carre_2
    elif digit==3:
        return carre_3
    elif digit==4:
        return carre_4
    elif digit==5:
        return carre_5
    elif digit==6:
        return carre_6
    elif digit==7:
        return carre_7
    elif digit==8:
        return carre_8
    elif digit==9:
        return carre_9
## ok fonctionnel
###
## Maintenant une fonction qui donne la position de chaque inconnue
def tuple_unknown(clean_array):
    liste_tuple=[]
    i=0
    for item in clean_array:

        j=0
        for item_deep in item:
            if item_deep=="_":
                liste_tuple.append([i,j])
            j+=1
        i+=1
    return liste_tuple
#ok c'est fonctionnel
# print(tuple_unknown(cleaned_array))
# print("/n /n /////////////////")
########
#maintenant besoin de calculer les "candidats" pour chacune des inconnues
def find_candidates(i,j,clean_array):
    liste_chiffre=["1","2","3","4","5","6","7","8","9"]
    liste_candidat=[]
    for item in line_pointer(i,clean_array):
        if item in liste_chiffre:
            liste_candidat.append(item)
    for item in column_pointer(j,clean_array):
        if item  in liste_chiffre :
            liste_candidat.append(item)
    for item in which_square_transp(wich_square(i,j)):
        if item in liste_chiffre :
            liste_candidat.append(item)

    for item in liste_chiffre:
        doublon=liste_candidat.count(item)
        if doublon >1:
            for t in range(1,doublon):
                liste_candidat.remove(item)
#    liste_candidat.sort()
    liste_finale=["1","2","3","4","5","6","7","8","9"]
    for item in liste_candidat:
        if (item in liste_finale) and (item in liste_finale):
            liste_finale.remove(item)
    return liste_finale
####ok c'est fonctionnel
#################
##maintenant
print("--------------")
#print(candidate_unknown(2,4,cleaned_array))
#print("--------------")
#ok c'est fonctionnel.
########""
#maintenant une fonction qui fait le tour des inconnues et récupère les listes de
#candidats
def all_candidates(clean_array):
    all_candidates_list=[]
    for item in tuple_unknown(clean_array):
        all_candidates_list+=[find_candidates(item[0],item[1],clean_array)]
    return all_candidates_list
### fonction qui remplace les inconnues à candidat unique par ledit candidat
#####
def replace_candidate(clean_array):
    for item in tuple_unknown(clean_array):
        candidat=find_candidates(item[0],item[1],cleaned_array)
        if len(find_candidates(item[0],item[1],cleaned_array))==1:
            print(find_candidates(item[0],item[1],cleaned_array))
            clean_array[item[0]][item[1]]=find_candidates(item[0],item[1],clean_array)[0]
    #remplacer
    return clean_array
print_tab(replace_candidate(cleaned_array))
print("\n \n ")



print("--------------")
print_tab(cleaning_arr(full_copy))


#11h20: fichier récupéré . Besoin clean la donnée maintenant
#11h54: affichage et tableau presque nettoyés , me reste deux "]"
#de je ne sais où. ah ba en fait c'est bon
#premier objectif atteinds, je pensais aller plus vite,
#un peu mal au dos et moyen long à la détente
#13h12:pause guitare , reprise
#création fonction colonne , ligne , carré( carrré tricky ??)
#16h04: je bloque sur la formalisation du carré ,
#zizou me propose de réfléchir mais de les taper à la main dans un
#premier temps.. puis upgrade via vidéo Pierre. C'est parti..
#16h42: deux fonctions pour les carrès à  la main , fonctionnelles
#lendemain midi , je mange une po(ire)mme et je m'y remet , avec les conseils de zizou
#je viens de me rendre compte que j'avais perdu le fil ,
#c'est pas les candidats que j'ai c'est les voisins , je "reverse"
#12h54, je souhaite maitriser les raccourci clavier le plus tôt possible
#exemple pour remplacer un terme par exemple. Je risque de me mettre à vim après
#cette période d'atom.. sublime texte et vscode à tester également
#git à utiliser de toute urgence
#13h01 :je sature, j'ai pas la bonne liste de candidat je comprends pas pourquoi
#besoin de prendre du recul . peur de pas y arriver , je souhaite passer à la suite,
#besoin de persévérer
#16h10: je cherche à extraire la liste des candidats de la liste des voisins
#16h32! j'ai réussi !
#Maintenant fonction qui remplace "_" par le candidat si unique
