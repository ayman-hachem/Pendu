import pygame
import random
import sys
import pygame.time

pygame.init()

fenetre = pygame.display.set_mode((950, 800))
pygame.display.set_caption("LE PENDU")

text_color = (0,0,0)
police = pygame.font.SysFont("arialblack", 30)


def afficher_image():
    bouton_play_image = pygame.image.load('boutonplay.jpg').convert()
    fenetre.blit(bouton_play_image, (250, 350))


def afficher_mot(mot, lettre_devinees):
    x_position = 150  # Position initiale
    y_position = 700 
    message = " ".join([lettre if lettre in lettre_devinees else '_' for lettre in mot])
    police = pygame.font.SysFont("arialblack", 40)

    for caractere in message:
        if caractere == ' ':
            x_position += 15  # Ajustez la valeur selon votre préférence
        else:
            texte = police.render(caractere, 1, text_color)
            fenetre.blit(texte, (x_position, 200))
            x_position += 30  # Ajustez la valeur selon votre préférence

def afficher_message(message):
    fenetre.blit(pygame.image.load('colline.jpg').convert(), (0, 0))
    texte = police.render(message, 1, text_color)
    fenetre.blit(texte, (100, 400))
    pygame.display.flip()
   
 
def afficher_bouton_rejouer():

    bouton_rejouer = pygame.image.load('rejouer.jpg').convert()
    fenetre.blit(bouton_rejouer, (250, 500))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            rejouer()
    pygame.display.flip()
    

    
def rejouer():
    global fin_de_partie, max_erreur, lettre_devinees, mot_solution
    fin_de_partie = False
    max_erreur = 6
    lettre_devinees = set()
    mot_solution = random.choice(mots).upper()
    

with open("mot.txt", "r") as fichier:
    mots = fichier.read().splitlines()

mot_solution = random.choice(mots).upper()

max_erreur = 6
lettre_devinees = set()

start = True
fin_de_partie = False  #fin de la partie si il y a 6 erreurs

def jeux():
    global max_erreur, lettre_devinees, mot_solution, start

    fenetre.blit(pygame.image.load('colline.jpg').convert(), (0, 0))

    if start:
        
        afficher_image()  # image d'accueil
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
        
    else:
        afficher_mot(mot_solution, lettre_devinees)
        lettre_texte = police.render(f"lettres devinées: { ' '.join(sorted(lettre_devinees))}", 1, text_color)
        fenetre.blit(lettre_texte, (150, 100))

        pygame.draw.circle(fenetre, 'yellow', (900, 40), 100)  # soleil
        pygame.draw.line(fenetre, 'white', (900, 600), (600, 600), 20)  # barre horizontal du bas
        pygame.draw.line(fenetre, 'white', (650, 300), (650, 600), 15)  # barre vertical
        pygame.draw.line(fenetre, 'white', (643, 300), (850, 300), 15)  # barre vertical du haut
        pygame.draw.line(fenetre, 'white', (649, 400), (700, 300), 15)  # barre diagonale
        pygame.draw.line(fenetre, 'white', (760, 300), (760, 350), 15)  # corde

        # modifier ce code pour afficher ce code en fonction des erreurs
        if max_erreur < 6:
            pygame.draw.circle(fenetre, 'red', (760, 350), 20)  # tête
        if max_erreur < 5:
            pygame.draw.line(fenetre, 'red', (760, 360), (760, 450), 10)  # corps
        if max_erreur < 4:
            pygame.draw.line(fenetre, 'red', (760, 380), (730, 390), 10)  # bras droit
        if max_erreur < 3:
            pygame.draw.line(fenetre, 'red', (760, 380), (790, 390), 10)  # bras gauche
        if max_erreur < 2:
            pygame.draw.line(fenetre, 'red', (760, 440), (720, 480), 10)  # pied gauche
        if max_erreur < 1:
            pygame.draw.line(fenetre, 'red', (760, 440), (790, 480), 10)  # pied droit

    if max_erreur <= 0:
            
            afficher_message("Vous avez perdu, un innocent est mort !")
            afficher_bouton_rejouer()   
            
             
    elif set(lettre_devinees) >= set(mot_solution):
            afficher_message("Vous avez gagné, vous avez sauvé un innocent !")
            afficher_bouton_rejouer()
            
            
    pygame.display.flip()  # cette commande permet de mettre à jour la boucle while et afficher le contenu


running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                lettre = event.unicode.upper()
                if lettre not in lettre_devinees:
                    lettre_devinees.add(lettre)
                    if lettre not in mot_solution:
                        max_erreur -= 1

    
            
                                                                              
    jeux()

   
pygame.quit()