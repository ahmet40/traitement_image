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


libere_place("./codeB2_et_image/Imageout_steg_0.bmp")





def cacher_image(image_princip,image_a_cacher,rep_sortie):
    """
    fonction qui va cacher une image dans l'autre
    
    """
    sortie=image_princip.copy()
    for y in range(image_a_cacher.size[1]):
        #pour chaque ligne de l'image
        for x in range(image_a_cacher.size[0]):    #pour chaque colonne de l'image
            c= image_princip.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
            c1=image_a_cacher.getpixel( (x,y))
            nv_col=c1[0]**2+c1[1]**2+c1[2]**2      
            if nv_col > 255*255*3/2:          #on verifie si la nouvel couleur du pixel sera noir ou blanc
                sortie.putpixel((x,y),(cacher(c[0],1),c[1],c[2]))        
            else:
                sortie.putpixel((x,y),(cacher(c[0],0),c[1],c[2]))
    sortie.save(rep_sortie)        #on enregistre cela dans le fichier nommé Imageout3.bmp


image_principal=Image.open("./codeB2_et_image/Imageout_steg_0.bmp")
logo_a_cacher=Image.open("./codeB2_et_image/Imageout3.bmp")
cacher_image(image_principal,logo_a_cacher,"./codeB2_et_image/Imageout_steg_1.bmp")




def retrouver_image_cacher(image_princip,rep_sortie):
    """
    Fonction qui permet de retrouver une image cacher
    """
    
    sortie=image_princip.copy()
    for y in range(image_princip.size[1]):
        #pour chaque ligne de l'image
        for x in range(image_princip.size[0]):    #pour chaque colonne de l'image
            c= image_princip.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
            if trouver(c[0]) == 0:
                sortie.putpixel((x,y),(00,00,00))   
            else:
                sortie.putpixel((x,y),(255,255,255))  
        
        sortie.save(rep_sortie)        #on enregistre cela dans un fichier 

img_principal_avec_autre_img=Image.open("./codeB2_et_image/Imageout_steg_1.bmp")
retrouver_image_cacher(img_principal_avec_autre_img,"./codeB2_et_image/ImageB5_qui_etait_cacher.bmp")