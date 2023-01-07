from PIL import Image
def cacher(i,b):
    return i-(i%2)+b





hall=Image.open("/home/baba/iut1/sae_image/sae_image/Imageout_steg_0.bmp")
logo=Image.open("/home/baba/iut1/sae_image/sae_image/Imageout3.bmp")
sortie=hall.copy()
for y in range(logo.size[1]):
    #pour chaque ligne de l'image
    for x in range(logo.size[0]):    #pour chaque colonne de l'image
        c= hall.getpixel( (x,y))   #on prend le code rvb du pixel à la position x,y
        c1=logo.getpixel( (x,y))
        nv_col=c1[0]**2+c1[1]**2+c1[2]**2      
        if nv_col > 255*255*3/2:          #on verifie si la nouvel couleur du pixel sera noir ou blanc
            sortie.putpixel((x,y),(cacher(c[0],1),c[1],c[2]))        
        else:
            sortie.putpixel((x,y),(cacher(c[0],0),c[1],c[2]))
        

sortie.save("/home/baba/iut1/sae_image/sae_image/Imageout_steg_1.bmp")        #on enregistre cela dans le fichier nommé Imageout3.bmp



