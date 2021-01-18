import sys
#récupérer le rectangle , les chiffres,
#depuis le fichier texte,
#il récupére une ligne à la fois,
#j'enlève les \n et je converti les
#èlements en int pour la suite

#peut être aurais je pu garder les string
file_1=open(sys.argv[1],"r")
list=[]
for item in file_1:
    list+= [item]
file_1.close()

file_2=open(sys.argv[2],"r")
list_2=[]
for item in file_2:
    list_2+= [item]
file_2.close()
# print(list)
# print(list_2)

#dimensionnement
longueur_rect_1=len(list[0])
print("la longueur de rect1 = "+ str(longueur_rect_1))
hauteur_rect_1=len(list)
print("hauteur liste1 = "+str(hauteur_rect_1))
longueur_rect_2=len(list_2[0])
print("la longueur de rect2 = "+str(longueur_rect_2))
hauteur_rect_2=len(list_2)
print("hauteur liste2 = "+str(hauteur_rect_2))

#parcours du grand tableau


# +#correction compteur car plus de triplets et \n
total=hauteur_rect_2*longueur_rect_2
print(total)
#récupére le triplet à un curseur donné
#ne prends pas les curseurs qui empeche triplet

# ça se construit mais à nouveau coincé , j'arrive pas à finir
def get_triplet(curseur,liste):
    ligne=curseur // longueur_rect_2
    colonne=curseur%longueur_rect_2
    if ((longueur_rect_2-(curseur%longueur_rect_2))>=longueur_rect_1):
        return liste[ligne][colonne:colonne+longueur_rect_1-1]
    # else:
    #     print("bonne nuit les petitss")
#print(get_triplet(8,list_2))

#je veux que cette fonction dise: ok ou non à ce curseur
def matching(curseur,list,list_bis):

    boule=True
    for z in range(longueur_rect_1-1):

        if (list[z][:-1]== get_triplet(curseur,list_bis)):
            curseur+=longueur_rect_2
        else:
            boule=False
    return boule
#ça y est fonction fonctionne
#la fonction créer l'organe
def is_there_match(list,list_2):
    for i in range(total):
        if matching(i,list,list_2):
            return True
def recherche(total, list,list_2):
    if is_there_match(list,list_2):
        for i in range(total):
            if matching(i,list,list_2):
                a=i

        return [a//longueur_rect_2,a%longueur_rect_2]
    else:
        return "désolé pas de concordance"
    #a est le curseur qui correspond
print(recherche(total,list,list_2))
    # if boule==True :
    #     return [(curseur // longueur_rect_2)-1,curseur%longueur_rect_2]
    # else :
    #     return "désolé"

    #////////////////////////////////
    #allez on tape dans l'algo
    #
    # #reste à dire quand il n'y a pas de solution..
    # ou qu'il y a des doublons dans tableau
    # ex 123 456 456 123 777
    #la compétence va venir avec l'expèrience ..
#version qui trouve le début , mais ne donne pas de rép si pas de solution
#ou suiter mauvaise.. o
#     largeur_rect_1=len(l1[0])
#     hauteur_rect_1=len(l1)
#     largeur_rect_2=len(l2[0])
#     hauteur_rect_2=len(l2)
#     #################"
#     ##############"
#     #coeur du probleme
#     coord=[0,0]
#     curseur=0
#     for i in range(hauteur_rect_2):
#
#         for j in range(largeur_rect_2-3):
#             for z in range(hauteur_rect_1):
#                 if l1[z][:-1]==l2[i][j:j+3]:
#                     coord[1]=j
#                 else:
# #                    j+=1
#     coord[0]=((hauteur_rect_2*(largeur_rect_2-1))%coord[1])
#     print(coord)
#     print(curseur)
# #coeur du problème ..


#            print('l2 triplet='+str(l2[i][j:j+3]))
#il y a bien 25 triplets            nb_triplet+=1
#    # print(l1[0][:-1]== l2[0][2:5])
#pb : comment faire s'arréter les boucles quand je veux
#comment revenir au début si besoin ?
#grand rectangle. grâce aux dimensions + curseur ?
#
# les èlements sont bien des strings print(type(list_2[0]))
# print(longueur)
# chiffre=['0','1','2','3','4','5','6','7','8','9']
# clean_list=[]
# for item_bis in list:
#     if item_bis in chiffre:
#         clean_list+=[item_bis]
# very_clean_list=[]
# for item_tierce in clean_list:
#     very_clean_list.append(int(item_tierce))
# #print(very_clean_list)
# #deuxieme texte à récupérer , classer
# #dans un tableau bi dimentionnel

# chiffre=['0','1','2','3','4','5','6','7','8','9']
# clean_list_2=[]
# for item_bis_2 in list_2:
#     if item_bis_2 in chiffre:
#         clean_list_2+=[item_bis_2]
# very_clean_list_2=[]
# for item_tierce_2 in clean_list_2:
#     very_clean_list_2.append(int(item_tierce_2))
# #print(very_clean_list_2)
