from PIL import Image

i=Image.open("/home/baba/iut1/sae_image/sae_image/hall-mod_0.bmp")  #l'image que l'on veut ouvrir
sortie=i.copy()   #on copie cette image dans une variable nommé sortie
width=i.width -1
#récupere la largeur du fichier (le nombre de pixel que l'on trouve dans le fichier)
for y in range(i.size[1]):
    #pour chaque ligne de l'image
    for x in range(i.size[0]):    #pour chaque colonne de l'image
        c= i.getpixel( (x,y))
        # on recuper le code rvb du pixel à la position x,y
        
        sortie.putpixel((width-x,y),c)
        #on change le pixel de le pixel avec le dernier (le premier pixel avec le dernier, le deuxieme avec l'avant dernier...)
        
sortie.save("/home/baba/iut1/sae_image/sae_image/Imageout1.bmp")
