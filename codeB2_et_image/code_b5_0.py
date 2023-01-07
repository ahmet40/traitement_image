from PIL import Image


hall=Image.open("/home/baba/iut1/sae_image/sae_image/hall-mod_0.bmp")
sortie=hall.copy()
for y in range(hall.size[1]):
    #pour chaque ligne de l'image
    for x in range(hall.size[0]):    #pour chaque colonne de l'image
        c= hall.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
        valeur_r=c[0]-(c[0]%2)      #on va dégrader la couleur rouge du pixel
        sortie.putpixel((x,y),(valeur_r,c[1],c[2]))       

        

sortie.save("/home/baba/iut1/sae_image/sae_image/Imageout_steg_0.bmp")        #on enregistre cela dans un fichier 
