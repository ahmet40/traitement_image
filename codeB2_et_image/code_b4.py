from PIL import Image

mon_image=Image.open("./IUT-Orleans.bmp")
#i est l'image que l'on veut ouvrir (ici c'est le logo de l'iut)
def noir_blanc(i,rep_sortie):
    """
    met les pixels de l'image en noir et blanc.
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
            c= i.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
            nv_col=c[0]**2+c[1]**2+c[2]**2      
            if nv_col > 255*255*3/2:          #on verifie si la nouvel couleur du pixel sera noir ou blanc
                sortie.putpixel((x,y),(255,255,255))        # nouvelle couleur (du pixel):couleur blanc
            else:
                sortie.putpixel((x,y),(00,00,00))           # nouvelle couleur (du pixel):couleur noir
            
    sortie.save(rep_sortie)        #on enregistre cela dans le fichier nommé Imageout3.bmp

noir_blanc(mon_image,"./codeB2_et_image/Imageout3.bmp")