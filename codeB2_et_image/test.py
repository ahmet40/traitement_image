import string, random 

def code_vernam(mot_a_cacher):
    clef=""
    dico_alph={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    for i in range(len(mot_a_cacher)):          #parcour le mot à cacher
        lettre_aleatoire=random.choice(string.ascii_letters)       #choisis une lettre de l'alphabet de façon aleatoire
        clef+=lettre_aleatoire.lower()                             #met cette lettre en petit caractere
    #j'ai fait les 3 lignes precedente pour avoir une cle de meme taille que mon mot et d'avoir des lettres aleatoires
    indice=0
    mot_a_retourner=""
    for lettre in mot_a_cacher:         #parcours les lettre du mot à cacher
        val=dico_alph[lettre]+dico_alph[clef[indice]]
        val=val%26
        indice+=1
        for lettre,valeur in dico_alph.items():
            if valeur == val:
                mot_a_retourner += lettre
                break
    return mot_a_retourner,clef

print(code_vernam("planterunefleur"))