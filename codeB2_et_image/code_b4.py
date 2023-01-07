from PIL import Image

i=Image.open("/home/baba/iut1/sae_image/sae_image/IUT-Orleans.bmp")
#i est l'image que l'on veut ouvrir (ici c'est le logo de l'iut)
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
        
sortie.save("/home/baba/iut1/sae_image/sae_image/Imageout3.bmp")        #on enregistre cela dans le fichier nommé Imageout3.bmp
