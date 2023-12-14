import pygame 

pygame.init()

fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("LE PENDU")

def afficher_image():
    bouton_play_image = pygame.image.load('boutonplay.jpg').convert()
    fenetre.blit(bouton_play_image, (250, 250))

erreur = 6
start = True

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner la colline en arrière-plan
    fenetre.blit(pygame.image.load('colline.jpg').convert(), (0, 0))

    if start:
        afficher_image()
        
        pygame.draw.line(fenetre, 'white', (700, 500), (500, 500), 20)  # barre horizontal du bas
        pygame.draw.line(fenetre, 'white', (600, 200), (600, 500), 15)  # barre vertical
        pygame.draw.line(fenetre, 'white', (750, 200), (593, 200), 15)  # barre vertical du haut
        pygame.draw.line(fenetre, 'white', (650, 200), (600, 300), 15)  # barre diagonale
        pygame.draw.line(fenetre, 'white', (730, 195), (730, 250), 15)  # corde
        pygame.draw.circle(fenetre, 'red', (730, 250), 20)  # tête
        pygame.draw.line(fenetre, 'red', (729, 270), (729, 320), 10)  # corps
        pygame.draw.line(fenetre, 'red', (730, 280), (760, 300), 10)  # bras droit
        pygame.draw.line(fenetre, 'red', (700, 299), (730, 280), 10)  # bras gauche
        pygame.draw.line(fenetre, 'red', (700, 399), (730, 280), 10)  # pied gauche
        pygame.draw.line(fenetre, 'red', (755, 399), (730, 300), 10)  # pied droit
        pygame.draw.circle(fenetre, 'yellow', (790, 40), 100)  # soleil
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start = False
    else :
        pygame.draw.circle(fenetre, 'yellow', (790, 40), 100)  # soleil
    # Dessiner le pendu par-dessus
        
        pygame.draw.line(fenetre, 'white', (700, 500), (500, 500), 20)  # barre horizontal du bas
        pygame.draw.line(fenetre, 'white', (600, 200), (600, 500), 15)  # barre vertical
        pygame.draw.line(fenetre, 'white', (750, 200), (593, 200), 15)  # barre vertical du haut
        pygame.draw.line(fenetre, 'white', (650, 200), (600, 300), 15)  # barre diagonale
        pygame.draw.line(fenetre, 'white', (730, 195), (730, 250), 15)  # corde
        
        # modifier ce code pour afficher ce code en fonction des erreurs 
        if erreur < 6 :
            pygame.draw.circle(fenetre, 'red', (730, 250), 20)  # tête
        if erreur < 5 :
            pygame.draw.line(fenetre, 'red', (729, 270), (729, 320), 10)  # corps
        if erreur < 4 :
            pygame.draw.line(fenetre, 'red', (730, 280), (760, 300), 10)  # bras droit
        if erreur <3 : 
            pygame.draw.line(fenetre, 'red', (700, 299), (730, 280), 10)  # bras gauche
        if erreur < 2 :
            pygame.draw.line(fenetre, 'red', (700, 399), (730, 280), 10)  # pied gauche
        if erreur < 1 :
            pygame.draw.line(fenetre, 'red', (755, 399), (730, 300), 10)  # pied droit
    



#     # # Vérifier si le bouton gauche de la souris est enfoncé et si les coordonnées sont à l'intérieur du bouton
#         # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#         #     x_souris, y_souris = pygame.mouse.get_pos()
#         #     if bouton_play_image.collidepoint(x_souris, y_souris):
#         #         print("Clic sur le bouton Play pour!")
# fenetre2 = pygame.display.set_mode((800, 800))
# pygame.display.set_caption("LE PENDU") #permet de créer la fenêtre pygame
    pygame.display.flip() # cette commande permet de mettre à jour la boucle while et afficher le contenue

pygame.quit()



# def lire_fichier(nom_fichier):
#     with open(nom_fichier, 'r') as fichier:
#         return [ligne.strip() for ligne in fichier.readlines()]

# def choisir_mot_aleatoire(nom_fichier):
#     mots = lire_fichier(nom_fichier)
#     return random.choice(mots)

# def underscore(mot, lettres_correctes):
#     affichage = '_'
#     for lettre in mot:
#         if lettre in lettres_correctes:
#             affichage += ' ' + lettre + ' '
#         else:
#             affichage += ' _ '
#     return affichage.strip()

# def saisie():
#     lettre_proposee = []
#     mot_choisi = choisir_mot_aleatoire('pendu/mot.txt')
#     lettres_correctes = set()
#     affichage = underscore(mot_choisi, lettres_correctes)
#     print('Mot à deviner :', affichage)
#     erreurs = 0

#     while erreurs < 6:
#         lettre_proposee = str(input("Insérer une lettre : "))

#         if lettre_proposee in lettres_correctes:
#             print("Vous avez déjà proposé cette lettre. Réessayez.")
#             continue

#         if lettre_proposee in mot_choisi:
#             lettres_correctes.add(lettre_proposee)
#         else:
#             erreurs += 1
#             print(f"Erreur ! Il vous reste {6 - erreurs} essais.")

#         affichage = underscore(mot_choisi, lettres_correctes)
#         print('Mot à deviner :', affichage)

#         if set(mot_choisi) == lettres_correctes:
#             print("Félicitations ! Vous avez deviné le mot :", mot_choisi)
#             break

#     if erreurs == 6:
#         print("Désolé, vous avez épuisé tous vos essais. Le mot était :", mot_choisi)

# def lettre_proposee():
#     lettres_proposees = set()
#     while True:
#         lettre_proposee = str(input("Insérer une lettre : "))
#         lettres_proposees.add(lettre_proposee)
#         print("Lettres proposées :", lettres_proposees)

# # Appel des fonctions
# saisie()
# lettre_proposee()
