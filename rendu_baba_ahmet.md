Bonjour,

A0 :
    	Les deux premiers octets que nous pouvons lire dans ce fichier (42 4D en hexadécimal) correspond au type de fichier que nous somme en train d’analyser. Dans notre cas cela signifie que c’est un fichier BMP (image).
    Les quatre octets suivant correspond a la taille du fichier. Ici ce-dernier est représenter en little indian, il faut donc inverser les octets ( donc 99 73 0C 00 va devenir 00 0C 73 99 ) lorsqu’on le calcule, cela nous donne 816025 (qui est la taille de notre fichier). 
    Les quatre octets suivant correspond à des champs réserver. 
    Puis les quatre autre octets correspond à l’adresse de la zone de définition de l’image (00 00 00 1A en tenant compte de l’indiannes). Tout ceci est l’en-tête du fichier Bmp que nous sommes en-train d’analyser. Il est codé sur 14 octets.


    Maintenant nous allons analyser l’en-tête du bitmap. Sur 4 octets se trouve la taille en octets de cet en-tête, dans ce fichier cela correspond à (0C 00 00 00) mais nous devons l’inverser car ,nous somme en little indian donc cela devient (00 00 00 0C) qui vaut 11.
    Les 4 octets suivants sont la largeur de l’image en pixels, (80 02 A9 01) qui vaut 01 A9 02 80 = 27 853 440 pixels.
    Les 4octets suivants (01 00 18 00) sont la hauteur de l’image en pixels.  00 18 00 01 = 1 572 865   Donc notre image a une hauteur de 1 572 865 pixels.

    Les octets suivants sont les octets de l’image rapellons nous qu’à 1A nous obtenions  l’adresse de la zone de définition de l’image et nous y sommes arriver nous sommes en l’adresse 1A.


    Lorsque nous affichons l’image avec display nous obtenons une erreur. Cela est du à la taille du fichier. En effet dans le fichier la taille entrer est de  00 0C 73 99 qui vaut 816 025
    . alors que lorsque nous faisons ls -l  pour avoir la taille du fichier dans le terminale cela nous donne  816 026. Ce problème est du au fait que nous oublions de calculer l’octet à l’adresse 0. (de 0 à 5 il y a 5 valeur 1, 2, 3, 4 et 5 cela est compter par ce que l’on entre dans le fichier tandis que dans le terminal et pour la taille du fichier de 0 à 5 nous trouvons les valeurs 0, 1, 2, 3, 4 et 5). 

    Pour résoudre se problème nous devons ajouter 1 à 00 0C 73 99  cela nous donne donc : 00 0C 73 9A. Et entrer cette nouvelle valeur à la place de l’ancienne.


A3:
    0) Nous somme passe d'un fichier de 74 octets à 102. Le calcule est simple nous faisons 74-12(enlever le poid du codage du BITMAPCOHEADER)
    donc 62+40 = 102 
    (40 est le poid du codage en BITMAPINFOHEADER)

    1) On utilise 24 bits par pixels.Soit 3 octets par pixels
    
    2)le fichier à une taille de 102 octets

    3)Il y une compression utilisé lorsque nous passons de BITMAPINFOHEADER à BITMAPCOREHEADER car nous réduissons la taille de l'en-tête du fichier.

    4)



A4:
    1)il n'y a qu'un seul bits utilisé.
    2)le fichier a une taille de 78 octets.
    3)
