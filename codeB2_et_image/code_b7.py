

def code_vernam(mot_a_cacher,clef="coder"):
    dico_alph={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    indice=0
    mot_a_retourner=""
    for lettre in mot_a_cacher:
        if indice == len(clef):
            indice=0
        val=dico_alph[lettre]+dico_alph[clef[indice]]
        val=val%26
        indice+=1
        for lettre,valeur in dico_alph.items():
            if valeur == val:
                mot_a_retourner += lettre
                break
    return mot_a_retourner

cle="khusiopkdwebzqkphuvcko"
mot_a_cacher=input("veuillez entrer le message que vous vouler cacher: ")
print(code_vernam(mot_a_cacher,"zskjltubsy"))

def code_vernam_retrouver(mot__jacher,clef):
    dico_alph={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    indice=0
    mot_a_retourner=""
    for lettre in mot__jacher:
        if indice == len(clef):
            indice=0
        val=dico_alph[lettre]-dico_alph[clef[indice]]
        print(val,dico_alph[lettre],dico_alph[clef[indice]])
        val=val%26
        indice+=1
        for lettre,valeur in dico_alph.items():
            if valeur == val:
                mot_a_retourner += lettre
                break
    return mot_a_retourner


#print(code_vernam_retrouver("euueqejsykytuueikowkob","khusiopkdwebzqkphuvcko"))