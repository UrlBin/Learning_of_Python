import pygame

number_of_fealds = 8
dim_of_rec = 80
width = dim_of_rec*number_of_fealds + 30
height = dim_of_rec*number_of_fealds + 30

pygame.init()

# Set up the drawing window
elephant = pygame.image.load("elephant2.png")
elephant = pygame.transform.scale(elephant, (dim_of_rec - 10, dim_of_rec - 10))

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Демонстрация ходов фигуры КОНЬ на доске')
pygame.display.set_icon(pygame.image.load("chess.png"))
clock = pygame.time.Clock()
FPS = 60
black = (0, 0, 0)
white = (255, 255, 255)


class myButton:

    circle_bool = False

    def __init__(self, screen, colour, count_x_i, count_y_i, count_x_j, count_y_j):

        self.screen = screen
        self.colour = colour
        self.count_x_i = count_x_i
        self.count_y_i = count_y_i
        self.count_x_j = count_x_j
        self.count_y_j = count_y_j
        self.coordinate = (count_x_i, count_y_i, dim_of_rec, dim_of_rec)
        self.coordinate_of_center = ((self.count_x_i + self.count_x_j) / 2, (self.count_y_i + self.count_y_j) / 2)
        self.internal_circle_bool = False

        # print('Создан новый объект класса myButton.')
        # print('Его координаты: первая точка - ', count_x_i, count_y_i, '; - вторая точка - ', count_x_j, count_y_j)

    def draw_rec(self):
        # pygame.draw.rect(self.screen, self.colour, self.coordinate)
        pygame.draw.rect(self.screen, self.colour, self.coordinate)
        # pygame.draw.circle(self.screen, (0, 255, 0), (self.count_x_i, self.count_y_i), 5)
        # pygame.draw.circle(self.screen, (0, 0, 255), (self.count_x_j, self.count_y_j), 5)

    def draw_border(self):
        focused_colour = (255, 0, 0)
        mouse_active = pygame.mouse.get_pos()
        # coordinate_of_center = ((self.count_x_i + self.count_x_j)/2, (self.count_y_i + self.count_y_j)/2)
        if self.count_x_i < mouse_active[0] < self.count_x_j:
            if self.count_y_i < mouse_active[1] < self.count_y_j:
                pygame.draw.rect(self.screen, focused_colour, self.coordinate, 5)

    def draw_circle(self):
        mouse_click = pygame.mouse.get_pressed()
        mouse_active = pygame.mouse.get_pos()
        if self.count_x_i < mouse_active[0] < self.count_x_j:
            if self.count_y_i < mouse_active[1] < self.count_y_j:
                if mouse_click[0] == True or mouse_click[2] == True:
                    pygame.time.delay(80)
                    if myButton.circle_bool == False and self.internal_circle_bool == False:
                        myButton.circle_bool = True
                        self.internal_circle_bool = True
                        pygame.time.delay(10)
                    elif myButton.circle_bool == True and self.internal_circle_bool == True:
                        myButton.circle_bool = False
                        self.internal_circle_bool = False
                        pygame.time.delay(10)
                    elif myButton.circle_bool == True and self.internal_circle_bool == False:
                        for o in list_of_buttons:
                            o.internal_circle_bool = False
                            o.draw_rec()
                            pygame.display.update()
                            pygame.time.delay(2)
                        self.internal_circle_bool = True
                    else:
                        self.internal_circle_bool = True
        if self.internal_circle_bool == True:
            # pygame.draw.circle(self.screen, (0, 255, 0), self.coordinate_of_center, 20)

            coordinates_of_elephant = self.coordinate_of_center
            screen.blit(elephant, (coordinates_of_elephant[0] - dim_of_rec/2 + 5, coordinates_of_elephant[1] - dim_of_rec/2 + 5))
            pygame.time.delay(5)

            if 0 < (self.coordinate_of_center[0] + dim_of_rec*2) < width:
                if 0 < (self.coordinate_of_center[1] + dim_of_rec) < height:
                    pygame.draw.circle(self.screen, (0, 255, 255),
                                       (self.coordinate_of_center[0] + dim_of_rec*2,
                                        self.coordinate_of_center[1] + dim_of_rec), 20)
                    # pygame.draw.line(screen, (0, 255, 255), (self.coordinate_of_center),
                    #                  (self.coordinate_of_center[0] + dim_of_rec,
                    #                   self.coordinate_of_center[1]), 5)
                    # pygame.draw.line(screen, (0, 255, 255), (self.coordinate_of_center),
                    #                  (self.coordinate_of_center[0] + dim_of_rec * 2,
                    #                   self.coordinate_of_center[1] + dim_of_rec), 5)

            if 0 < (self.coordinate_of_center[0] + dim_of_rec*2) < width:
                if 0 < (self.coordinate_of_center[1] - dim_of_rec) < height:
                    pygame.draw.circle(self.screen, (0, 255, 255),
                                       (self.coordinate_of_center[0] + dim_of_rec*2,
                                        self.coordinate_of_center[1] - dim_of_rec), 20)

            if 0 < (self.coordinate_of_center[0] - dim_of_rec*2) < width:
                if 0 < (self.coordinate_of_center[1] + dim_of_rec) < height:
                    pygame.draw.circle(self.screen, (0, 255, 255),
                                       (self.coordinate_of_center[0] - dim_of_rec*2,
                                        self.coordinate_of_center[1] + dim_of_rec), 20)

            if 0 < (self.coordinate_of_center[0] - dim_of_rec*2) < width:
                if 0 < (self.coordinate_of_center[1] - dim_of_rec) < height:
                    pygame.draw.circle(self.screen, (0, 255, 255),
                                       (self.coordinate_of_center[0] - dim_of_rec * 2,
                                        self.coordinate_of_center[1] - dim_of_rec), 20)

            if 0 < (self.coordinate_of_center[0] + dim_of_rec) < width:
                if 0 < (self.coordinate_of_center[1] + dim_of_rec*2) < height:
                    pygame.draw.circle(self.screen, (0, 255, 255),
                                       (self.coordinate_of_center[0] + dim_of_rec,
                                        self.coordinate_of_center[1] + dim_of_rec*2), 20)

            if 0 < (self.coordinate_of_center[0] + dim_of_rec) < width:
                if 0 < (self.coordinate_of_center[1] - dim_of_rec*2) < height:
                    pygame.draw.circle(self.screen, (0, 255, 255),
                                       (self.coordinate_of_center[0] + dim_of_rec,
                                        self.coordinate_of_center[1] - dim_of_rec*2), 20)

            if 0 < (self.coordinate_of_center[0] - dim_of_rec) < width:
                if 0 < (self.coordinate_of_center[1] + dim_of_rec*2) < height:
                    pygame.draw.circle(self.screen, (0, 255, 255),
                                       (self.coordinate_of_center[0] - dim_of_rec,
                                        self.coordinate_of_center[1] + dim_of_rec*2), 20)

            if 0 < (self.coordinate_of_center[0] - dim_of_rec) < width:
                if 0 < (self.coordinate_of_center[1] - dim_of_rec*2) < height:
                    pygame.draw.circle(self.screen, (0, 255, 255),
                                       (self.coordinate_of_center[0] - dim_of_rec,
                                        self.coordinate_of_center[1] - dim_of_rec*2), 20)


screen.fill((255, 255, 255))

# Draw a solid blue circle in the center
list_of_buttons = list()
for i in range(0, number_of_fealds):
    count_x_i = 15
    count_y_i = dim_of_rec*i + 15
    count_x_j = count_x_i + dim_of_rec
    count_y_j = count_y_i + dim_of_rec
    if i%2 == 0:
        for j in range(0, number_of_fealds):
            if j % 2 == 0:
                # print(count_x_i, count_y_i, '--', count_x_j, count_y_j)
                list_of_buttons.append(myButton(screen, black, count_x_i, count_y_i, count_x_j, count_y_j))
            else:
                # print(count_x_i, count_y_i, '--', count_x_j, count_y_j)
                list_of_buttons.append(myButton(screen, white, count_x_i, count_y_i, count_x_j, count_y_j))
            count_x_i += dim_of_rec
            count_x_j += dim_of_rec
    else:
        for j in range(0, number_of_fealds):
            if j % 2 == 0:
                # print(count_x_i, count_y_i, '--', count_x_j, count_y_j)
                list_of_buttons.append(myButton(screen, white, count_x_i, count_y_i, count_x_j, count_y_j))
            else:
                # print(count_x_i, count_y_i, '--', count_x_j, count_y_j)
                list_of_buttons.append(myButton(screen, black, count_x_i, count_y_i, count_x_j, count_y_j))
            count_x_i += dim_of_rec
            count_x_j += dim_of_rec

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white

    for m in list_of_buttons:
        m.draw_rec()

    # for n in list_of_buttons:
    #     n.draw_circle()

    pygame.draw.rect(screen, white, (0, 0, width, height), 30)
    pygame.draw.rect(screen, black, (15, 15, width - 30, height - 30), 3)

    count_of_text_place_x = dim_of_rec/2 + 15
    for k in range(0, number_of_fealds):
        f1 = pygame.font.Font(None, 25)
        text1 = f1.render('{}'.format(k), True,
                      (0, 0, 0))
        screen.blit(text1, (count_of_text_place_x, height - 15))
        count_of_text_place_x += dim_of_rec

    count_of_text_place_y = height - dim_of_rec / 2 - 15
    for k in range(0, number_of_fealds):
        f1 = pygame.font.Font(None, 25)
        text1 = f1.render('{}'.format(k), True,
                          (0, 0, 0))
        screen.blit(text1, (width - 10, count_of_text_place_y))
        count_of_text_place_y -= dim_of_rec

    for m in list_of_buttons:
        m.draw_border()

    for n in list_of_buttons:
        n.draw_circle()
        # if myButton.circle_bool == False and n.internal_circle_bool == False:
        #     n.internal_circle_bool = True
        #     myButton.circle_bool = True
        # else:
        #     n.internal_circle_bool = True
        #     myButton.circle_bool = True

    # Flip the display
    pygame.display.flip()
    clock.tick(FPS)

# Done! Time to quit.
pygame.quit()