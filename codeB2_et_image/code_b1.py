from PIL import Image
import os
nom_fichier = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Imagetest.bmp") 
#permet d'ouvrir l'image de n'importe quel repertoire
mon_image=Image.open(nom_fichier)
#i est l'image que l'on veut ouvrir (ici c'est l'image test)

def tourner_image(image,position_sortie):
    """
    Fonction qui va faire la transposer de notre image (la trouner de 90° cela fait la même chose)
    parametre:
        entrer:
            image: ceci est l'image que l'on va utiliser
            position_sortie: l'endroit ou mon image modifié va être enregistrer
    
    """
    sortie=image.copy()
    #on copie cette image dans une variable nommé sortie
    for y in range(image.size[1]):
        #pour chaque ligne de l'image
        for x in range(image.size[0]):    #pour chaque colonne de l'image
            c= image.getpixel( (x,y))
            # on recuper le code rvb du pixel à la position x,y
            
            sortie.putpixel((y,x),c)
            #on change le pixel de la position colonne ligne à la position ligne colonne 
    sortie.save(position_sortie)

tourner_image(mon_image,"./Imageout0.bmp")