from PIL import Image

def trouver(i):
    return i%2


hall=Image.open("/home/baba/iut1/sae_image/sae_image/Imageout_steg_1.bmp")
sortie=hall.copy()
for y in range(hall.size[1]):
    #pour chaque ligne de l'image
    for x in range(hall.size[0]):    #pour chaque colonne de l'image
        c= hall.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
        if trouver(c[0]) == 0:
            sortie.putpixel((x,y),(00,00,00))   
        else:
            sortie.putpixel((x,y),(255,255,255))  
        

sortie.save("/home/baba/iut1/sae_image/sae_image/Imageout3bis.bmp")        #on enregistre cela dans un fichier 
