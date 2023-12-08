import pygame
import random


# Bouche infini, Menu
while True:
    print("1. Jouer au pendu")
    print("2. Ajouter un mot au fichier 'mots.txt'")
    print("3. Quitter")
    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "1":
        # Initialisation de Pygame
        pygame.init()
        # Définition des couleurs
        BLANC = (255, 255, 255)
        GRIS = (130,130,130)
        NOIR = (0, 0, 0)

        # Définition de la taille de la fenêtre
        largeur_fenetre = 800
        hauteur_fenetre = 600
        fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
        pygame.display.set_caption("Jeu du Pendu")

        # Chargement des images du pendu
        images_pendu = []
        for i in range(7):
            image = pygame.image.load(f"images/pendu{i}.png")
            images_pendu.append(image)

        # Lecture du  fichier "mots.txt"
        mots = []
        with open("mots.txt", "r") as fichier:
            for ligne in fichier:
                mots.append(ligne.strip())

        # Choix aléatoire d'un mot
        mot_choisi = random.choice(mots)

        # Initialisation des variables
        lettres_trouvees = []
        lettres_proposees = []
        erreurs = 0



        # Boucle principale du jeu
        running = True
        while running:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                        lettre = chr(event.key)
                        if lettre not in lettres_proposees:
                            lettres_proposees.append(lettre)
                            if lettre in mot_choisi:
                                lettres_trouvees.append(lettre)
                            else:
                                erreurs += 1


            # Effacement de l'écran
            fenetre.fill(GRIS)

            # Affichage du mot à deviner
            mot_affiche = ""
            for lettre in mot_choisi:
                if lettre in lettres_trouvees:
                    mot_affiche += lettre + " "
                else:
                    mot_affiche += "_ "
            font = pygame.font.Font(None, 25)
            text = font.render(mot_affiche, True, NOIR)
            fenetre.blit(text, (300, 250))

            # Affichage des lettres proposées
            lettres_affichees = "Lettres proposées : "
            for lettre in lettres_proposees:
                lettres_affichees += lettre + " "
            text = font.render(lettres_affichees, True, NOIR)
            fenetre.blit(text, (25, 400))

            # Affichage de l'image du pendu
            if erreurs < len(images_pendu):
                fenetre.blit(images_pendu[erreurs], (5, 100))

            # Vérification de la fin du jeu
            if erreurs == len(images_pendu):
                fenetre.fill(GRIS)
                lose = f"Malheureusement vous avez épuisé toutes vos vies, le mot était {mot_choisi}"
                text = font.render(lose, True, NOIR)
                rect_text = text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
                fenetre.blit(text, rect_text)
            elif all(lettre in lettres_trouvees for lettre in mot_choisi):
                fenetre.fill(GRIS)
                win = f"Félicitations vous avez trouvé le mot: {mot_choisi}"
                text = font.render(win, True, NOIR)
                rect_text = text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
                fenetre.blit(text, rect_text)

            # Mise à jour de l'affichage
            pygame.display.flip()

        # Fermeture de Pygame
        pygame.quit()
    elif choix == "2":
        print("PS: N'utilisez pas d'accents lors de la création de nouveau mots")
        nouveau_mot = input("Entrez un nouveau mot : ").lower()
        if all(lettre.isalpha() for lettre in nouveau_mot):
            with open("mots.txt", "a", encoding="utf-8") as file:
                file.write("\n" + nouveau_mot)
            print("Le mot a été ajouté avec succès.")
        else:
            print("Veuillez entrer un mot valide.")
    elif choix == "3":
        break
    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
