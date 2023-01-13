from PIL import Image
import string, random 

def cacher(i,b):
    return i-(i%2)+b
cacher
def trouver(i):
    return i%2

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
        val=dico_alph[lettre]+dico_alph[clef[indice]]       #additionne les indices de mon mot à cacher et celle de la clef
        val=val%26      #met cette valeur modulo 26
        indice+=1
        for lettre,valeur in dico_alph.items():     #parcour le dictionnaire de lettre
            if valeur == val:
                mot_a_retourner += lettre           #prend la lettre à laquelle l'indice correspond
                break
    return mot_a_retourner,clef




def code_vernam_retrouver(mot,clef):
    dico_alph={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    indice=0
    mot_a_retourner=""
    for lettre in mot:      #je parcour mon mot 
        
        val=dico_alph[lettre]-dico_alph[clef[indice]]  #je soustrait les indices de la lettre de mon mot et de la clef
        val=val%26          #je met ses indices modulo 26
        indice+=1
        for lettre,valeur in dico_alph.items():     #je parcour mon dictionnaire
            if valeur == val:
                mot_a_retourner += lettre       #je recupere la lettre à laquelle elle correspond
                break
    return mot_a_retourner



def libere_place(rep_sortie):
    """
    Fonction qui permet de liberer de la place sur le Rouge de chaque pixel pour liberer un peu de place
    """
    hall=Image.open("./hall-mod_0.bmp")     
    sortie=hall.copy()
    for y in range(hall.size[1]):
        #pour chaque ligne de l'image
        for x in range(hall.size[0]):    #pour chaque colonne de l'image
            c= hall.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
            valeur_r=c[0]-(c[0]%2)      #on va dégrader la couleur rouge du pixel
            sortie.putpixel((x,y),(valeur_r,c[1],c[2]))       
    sortie.save(rep_sortie)        #on enregistre cela dans un fichier 





def cacher_texte(image,rep_sortie,texte):
    """
    Fonction qui permet de cacher un texte dans une image.
    entrer:
        image: une image dans lequel nous allons cacher notre texte.
        rep_sortie: un chemin pour la sortie de notre nouveaux fichier
    """
    liste_bin_lettre=[]
    
    for lettre in texte:            #pour chaque lettre dans le mot
        texte = "".join(["{:08b}".format(ord(lettre))])    
        #texte = les lettres du texte que nous passons en hexadecimale via la table ASCII puis que nous convertissons en binaire sur 1 octets
        texte = [int(chiffre) for chiffre in texte] #nous convertissont en int chaque chiffre codés en str "00000001"-> [0,0,0,0,0,0,0,1]
        for chiffre in texte:
            liste_bin_lettre.append(chiffre)
    indice=0
    sortie=image.copy()
    for y in range(image.size[1]):
    #pour chaque ligne de l'image
        for x in range(image.size[0]):    #pour chaque colonne de l'image
            c= image.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
            if liste_bin_lettre[indice] == 1:
                sortie.putpixel((x,y),(cacher(c[0],1),c[1],c[2]))
            else:
                sortie.putpixel((x,y),(cacher(c[0],0),c[1],c[2]))    
            indice+=1
            if indice >= len(liste_bin_lettre):     #verifie que la liste binaire des lettres est fini
                sortie.save(rep_sortie)     #on enregistre cela dans un fichier 
                return                          #on sort de la fonction
            

def retrouver_texte_cacher(image_princip):
    """
    Fonction qui permet de retrouver une image cacher
    """
    pixel_image=[]
    cache=""
    for y in range(image_princip.size[1]):
        #pour chaque ligne de l'image
        for x in range(image_princip.size[0]):    #pour chaque colonne de l'image
            c= image_princip.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
            if trouver(c[0]) == 1:      #si la couleur rouge est impaire alors on met un 1 sinon un 0
                pixel_image.append("1")
            else:
                pixel_image.append("0")
            if len(pixel_image) == 8:       #on verifie si nos chiffre font 1 octet
                if pixel_image == ['0', '0', '0', '0', '0', '0', '0', '0']:     #si la valeur d'un octet vaut ['0','0','0','0','0','0','0','0']
                    break       #alors on arrete le parcours
                val=0
                for chiffre in range(len(pixel_image)):
                    puissance=(len(pixel_image)-chiffre-1)
                    val+=int(pixel_image[chiffre])*(2**puissance)
                cache+=chr(val)
                pixel_image=[]
    return code_vernam_retrouver(cache,clef)            
                

libere_place("./codeB2_et_image/Imageout_steg_out0_partie_b8.bmp")

mot_a_cacher=input("veuillez entrer le message que vous vouler cacher: ")
mot_a_placer_dans_image,clef=code_vernam(mot_a_cacher)
print("le mot que nous avons obtenu apres le passage par le code de vername est: {}, ".format(mot_a_placer_dans_image))
print("voici la clef utiliser pour coder ce mot: {}".format(clef))


image_non_code=Image.open("./codeB2_et_image/Imageout_steg_out0_partie_b8.bmp")
cacher_texte(image_non_code,"./codeB2_et_image/Imageout_steg_out1_partie_b8.bmp",mot_a_placer_dans_image)

image_avec_code=Image.open("./codeB2_et_image/Imageout_steg_out1_partie_b8.bmp")
mot_depart=retrouver_texte_cacher(image_avec_code)
print("Voici le texte que nous avons retrouver dans l'image: {}".format(mot_depart))
