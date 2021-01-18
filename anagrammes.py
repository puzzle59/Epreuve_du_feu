import sys
mot_recherche=sys.argv[1]
file=open(sys.argv[2],'r')
liste_botte_de_paille=[]
for mot_ in file:
    liste_botte_de_paille.append(mot_)
file.close()
# print(mot_recherche)
# print(liste_botte_de_paille)
#ok bon mot , bonne liste
def is_anagramme(mot,liste):
    liste_rendu=[]
    liste_fabrication=[]
    for lettre in mot :
        liste_fabrication.append(lettre)
    #print(liste_fabrication)
    for element in liste:
        liste_fabrication_temp=liste_fabrication.copy()
        if (len(mot)+1)!=len(element):
            None
            #print("pas le même nombre de lettre ?")

        else:
            #print("je rentre dans l'algo")
            for lettre in element:
#                print(liste_fabrication_temp)
                if lettre in liste_fabrication_temp:
                    liste_fabrication_temp.remove(lettre)
                else:
                    None
            if liste_fabrication_temp==[]:
                liste_rendu.append(element)
    liste_rendu_fignoler=[]
    for every_item in liste_rendu:
        liste_rendu_fignoler.append(every_item[:-1])
    return liste_rendu_fignoler
print(is_anagramme(mot_recherche,liste_botte_de_paille))
