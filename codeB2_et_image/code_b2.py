from PIL import Image

mon_image=Image.open("./hall-mod_0.bmp")
#i est l'image que l'on veut ouvrir (ici c'est l'image test)

def inverse_image_miroir(image,repertoir_sortie):
    """
    Fonction qui va echanger les pixels de la colonnes du début avec ce de la fin 
    Parmaetre:
    entrer:
        image: une image bmp
        repertoire de sortie: l'endroit ou l'image de sortie sera enregistrer. 
    
    """
    sortie=image.copy()   #on copie cette image dans une variable nommé sortie
    width=image.width -1
    #récupere la largeur du fichier (le nombre de pixel que l'on trouve dans le fichier)
    for y in range(image.size[1]):
        #pour chaque ligne de l'image
        for x in range(image.size[0]):    #pour chaque colonne de l'image
            c= image.getpixel( (x,y))
            # on recuper le code rvb du pixel à la position x,y
            
            sortie.putpixel((width-x,y),c)
            #on change le pixel de le pixel avec le dernier (le premier pixel avec le dernier, le deuxieme avec l'avant dernier...)
            
    sortie.save(repertoir_sortie)

inverse_image_miroir(mon_image,"./codeB2_et_image/Imageout1.bmp")