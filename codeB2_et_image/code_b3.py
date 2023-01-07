from PIL import Image

i=Image.open("/home/baba/iut1/sae_image/sae_image/IUT-Orleans.bmp")
#i est l'image que l'on veut ouvrir (ici c'est le logo de l'iut)
sortie=i.copy()
#on copie cette image dans une variable nommé sortie
for y in range(i.size[1]):
    #pour chaque ligne de l'image
    for x in range(i.size[0]):    #pour chaque colonne de l'image
        c= i.getpixel( (x,y))       #on prend le code rvb du pixel à la position x,y
        nv_col=(c[0]+c[1]+c[2])//3      # on met le pixel dans un niveau de gris
        sortie.putpixel((x,y),(nv_col,nv_col,nv_col))
        #on change (le pixel) la couleur du pixel
        
sortie.save("/home/baba/iut1/sae_image/sae_image/Imageout2.bmp") #on enregistre cela dans le fichier nommé Imageout2.bmp
