import pygame


number_of_fealds = 8
dim_of_rec = 80

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([dim_of_rec*number_of_fealds, dim_of_rec*number_of_fealds])

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    for i in range(0, number_of_fealds):
        count_x = dim_of_rec*i
        count_y = dim_of_rec*i + dim_of_rec
        count_x_1 = count_x
        count_y_1 = count_y
        for j in range(0, number_of_fealds):
            if j % 2 == 0:
                pygame.draw.rect(screen, (0, 0, 0), (count_x, count_x_1, count_y, count_y_1))
                count_x += dim_of_rec
                count_y += dim_of_rec
            else:
                pygame.draw.rect(screen, (255, 255, 255), (count_x, count_x_1, count_y, count_y_1))
                count_x += dim_of_rec
                count_y += dim_of_rec

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()