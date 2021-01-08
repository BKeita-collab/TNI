import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import cv2
from skimage.io import imread
from skimage.io import imsave
from skimage.color import rgb2gray
from skimage import filters
import statistics as st





####################################################
#-------------------------Exercice 2.3------------------------------------
####################################################

KoLanta_segmentation = imread('KoLanta_segmentation.tif')
KoLanta_classification = imread('KoLanta_classification.tif')


### Determination de nbc
KoLanta_classification_ligne , KoLanta_classification_colonne = KoLanta_classification.shape
liste_class = []
for i in range(KoLanta_classification_ligne) :
    for j in range(KoLanta_classification_colonne):
        liste_class.append(KoLanta_classification[i][j])

### liste_classe_unique contient les différentes classes dans IRC_classif
### nbc contient le nombre de classes dans IRC_classif
liste_classe_unique = np.unique(liste_class)
nbc = len(liste_classe_unique)






### Determination de nbs
KoLanta_segmentation_ligne , KoLanta_segmentation_colonne = KoLanta_segmentation.shape
liste_segment = []

for i in range(KoLanta_segmentation_ligne) :
    for j in range(KoLanta_segmentation_colonne):
        liste_segment.append( KoLanta_segmentation[i][j])

### liste_segment_unique contient les identifiants de tous les segments contenus dans IRC_Segmentation
### nbs contient le nombre d'identifiant de segment contenu dans l'image IRC_Segmentation
liste_segment_unique = np.unique(liste_segment)
liste_segment_unique = list(liste_segment_unique)
nbs = len(liste_segment_unique)



        
### Determination de M 
M = np.zeros((nbs , nbc))

#####Parcours et remplissage de la matrice M
for i in range(KoLanta_segmentation_ligne) :
    for j in range(KoLanta_segmentation_colonne) :
        p_segment , classe = liste_segment_unique.index(KoLanta_segmentation[i , j]) , KoLanta_segmentation[i, j] -1
        M[ p_segment , KoLanta_classification[i, j] -1] += 1
        

####---------------------------------------##
#### Création de la nouvelle classe avec la méthode du maximum de classe par segment
##----------------------------------------------#



##L = []
##L1 = []
##for i in range(M.shape[0]) :
##    for j in range(M.shape[1]):
##        L.append(M[i,j])
##    L1.append(max(L))
##    del L[:]
##V = np.asarray(L1)


##----------------------------------------------#
#### Création de nouvelles classes#####
##----------------------------------------------#

L_class = []
L1_class = []
new_class = []

for i in range(M.shape[0]) :
    for j in range(M.shape[1]):
        ##L prendra tous les élements de la matrice M
        L_class.append(M[i,j])
        
    ## maxi_classe contient la classe max au niveau du segment i   
    maxi_classe = max(L_class)

    ## on va parcourir tous les élements du segment i
    ## ensuite s'il y'a des élements qui ont des valeurs entre [max-1 , max+1]
    ### alors on prend leur moyenne comme une nouvelle classe du segment i
    ###Sinon on prend la valeur max comme classe sur le segment i 
    for element in L_class :
        if element >= maxi_classe-1 or element <= maxi_classe+1 :
            L1_class.append(element)
        else :
            L1_class_append(max(L_class))

    ## la liste new_classe contient la nouvelle classe qui est soit la moyenne soit la valeur max 
    new_class.append(st.mean(L1_class))

    ## on supprime ensuite L et L1 pour pouvoir effectuer la même opération sur le segment i+1
    del L1_class[:]
    del L_class[:]




##----------------------------------------------#
#### Création de la matrice V#####
##----------------------------------------------#

V = np.asarray(new_class)






##----------------------------------------------#
#### Création de l'image avec la nouvelle méthode utilisé
##----------------------------------------------#
### Création de la nouvelle image avec valeur de pixel les lignes de la matrice V 
im_vide = np.zeros((KoLanta_segmentation_ligne , KoLanta_segmentation_colonne))

for i in range(KoLanta_segmentation_ligne) :
    for j in range( KoLanta_segmentation_colonne) :
        im_vide[i][j] = V[liste_segment_unique.index(KoLanta_segmentation[i , j])]


### Enregistrement de l'image im_vide
image_result = imsave("image_result.tif",  im_vide)

### Affichage de l'image
##plt.figure(1)
##plt.imshow(im_vide)
        

    
        
        
                













