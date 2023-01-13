from PIL import Image


def cacher(i,b):
    return i-(i%2)+b

def trouver(i):
    return i%2



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


libere_place("./codeB2_et_image/Imageout_steg_out0_partie_b6.bmp")


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
            
    

mot_a_cacher=input("Veuillez entrer votre mot à cacher: ")
image_non_code=Image.open("./codeB2_et_image/Imageout_steg_out0_partie_b6.bmp")
cacher_texte(image_non_code,"./codeB2_et_image/Imageout_steg_out1_partie_b6.bmp",mot_a_cacher)




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
    print(cache)            
                
        
image_avec_code=Image.open("./codeB2_et_image/Imageout_steg_out1_partie_b6.bmp")
retrouver_texte_cacher(image_avec_code)
 
"""
"Bonus"
B=42  0100 0010
o=6F  0110 1111
n=6E  0110 1110
u=75  0111 0101
s=73  0111 0011
"""

#print(ord('s'),chr(115))