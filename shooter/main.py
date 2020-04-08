import pygame
from game import Game

pygame.init()

# generer la fenêtre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importation du background du jeu
background = pygame.image.load('assets/bg.jpg')

# charger le jeu
game = Game()

running = True

# boucle tant que cette condition est vrai

while running:

    # appliquer le background du jeu
    screen.blit(background, (0, -200))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Récuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # récupérere les monstres du jeu
    for monster in game.all_monsters:
        monster.forward()

    # appliquer à l'écran les projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des monstres à l'écran
    game.all_monsters.draw(screen)

    # vérifie rsi le jouerur veut aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        # détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecter si la touche espace est appuyé pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.lunch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
