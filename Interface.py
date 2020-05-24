
#in the future will recive this as a arguent
def readFromFile(fileName):
    labirinto = []
    lab = []
    f = open(fileName)
    linha = f.readline()
    linha = linha.split()
    lin = int(linha[0])
    col = int(linha[1])
    for i in range(lin):
        linha = f.readline()
        for j in range(col):
            lab.append(linha[j])
        labirinto.append(lab)
        lab=[]
    f.close()
    return labirinto

def showInterfaceFromFile(FileName,NomeAlgoritmo = "Algoritmo"):
    #pygame Init
    import pygame
    pygame.init()
    pygame.display.set_caption(NomeAlgoritmo)


    #input
    inputMatrix = readFromFile(FileName)
    rows = len(inputMatrix)
    col = len(inputMatrix[0])
    print(rows,col)



    #colors
    color_wall = pygame.Color(0,0,0)
    color_space = pygame.Color(255,255,255)
    color_path = pygame.Color(0,255,0)
    color_start = pygame.Color(170,255,170)
    color_objective = pygame.Color(255,0,0)
    color_true_objective = pygame.Color(200,100,10)

    # Set up the drawing window
    screen_widht = 720
    screen_height = 720
    screen = pygame.display.set_mode([screen_widht, screen_height],pygame.RESIZABLE)
    running = True

    #figure out rect sizes
    rect_widht = screen_widht/col
    rect_height = screen_height/rows

    #game loop
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screen_widht = event.w
                screen_height = event.h
                rect_widht = screen_widht/col
                rect_height = screen_height/rows
                screen = pygame.display.set_mode([screen_widht, screen_height],pygame.RESIZABLE)


        # Fill the background with white
        screen.fill(color_wall)

        for i in range(rows):
            for j in range(col):
                drawRect = pygame.Rect((j*rect_widht,i*rect_height,rect_widht,rect_height))
                if(inputMatrix[i][j] == '-'):
                    pygame.draw.rect(screen, color_wall,drawRect)
                elif(inputMatrix[i][j] == '#'):
                    pygame.draw.rect(screen, color_path,drawRect)
                elif(inputMatrix[i][j] == 'Q'):
                    pygame.draw.rect(screen, color_start,drawRect)
                elif(inputMatrix[i][j] == '$'):
                    pygame.draw.rect(screen, color_objective,drawRect)
                elif(inputMatrix[i][j] == 'M'):
                    pygame.draw.rect(screen, color_true_objective,drawRect)
                else:
                    pygame.draw.rect(screen, color_space,drawRect)
        # Flip the display and delay
        pygame.display.flip()
        pygame.time.delay(15)
    #end game loop

    print("Thanks for using")
    pygame.quit()









