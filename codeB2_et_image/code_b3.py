from PIL import Image

mon_image=Image.open("./IUT-Orleans.bmp")
#i est l'image que l'on veut ouvrir (ici c'est le logo de l'iut)
def niveau_de_gris(i,repertoire_sortie):
    """
    met les pixels de l'image dans un niveaux de gris.
    Parametre:
        entrer:
            i: une image bmp
            repertoire_sortie: le repertoir ou l'on va enregistre l'image de sortie
    """
    sortie=i.copy()
    #on copie cette image dans une variable nommé sortie
    for y in range(i.size[1]):
        #pour chaque ligne de l'image
        for x in range(i.size[0]):    #pour chaque colonne de l'image
            c= i.getpixel( (x,y))       #on prend le code rvb du pixel à la position x,y
            nv_col=(c[0]+c[1]+c[2])//3      # on met le pixel dans un niveau de gris
            sortie.putpixel((x,y),(nv_col,nv_col,nv_col))
            #on change (le pixel) la couleur du pixel
            
    sortie.save(repertoire_sortie) #on enregistre cela dans le fichier nommé Imageout2.bmp
niveau_de_gris(mon_image,"./codeB2_et_image/Imageout2.bmp")