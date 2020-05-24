#Algoritimo Hill climbing de busca

import numpy as np

def calculate(fileName):

    #Le o labirinto do arquivo Labirinto.txt
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
            if linha[j] == '#':
                inicio = [i,j]
            if linha[j] == '$':
                fim = [i,j]
            lab.append(linha[j])
        labirinto.append(lab)
        lab=[]
    f.close()


    #Criamos uma estrutura de visitas atuais e qual seu anterior (aqui iremos sempre ter uma posicao do labirinto em que estamos, e a sua anterior- de onde viemos)
    visitas = []
    anterior = []
    visitas.append(inicio)
    anterior.append(inicio)


    #Teremos uma fila que armazena quais os proximos lugares do labirinto a serem visitados
    fila = []
    fila.append(inicio)
    fila_aux = []


    #Usaremos uma distancia euclidiana para determinar qual o proximo valor da fila a ser visitado
    dist = []
    dist.append(pow(pow(inicio[0] - fim[0],2) + pow(inicio[1] - fim[1],2),1/2))
    #Como estamos com o Hill CLimbing, sempre faremos a analise entre os filhos (que podem no maximo ser 4) de suas distancias para coloca-los na fila na ordem do menor para o maior
    dist = np.array([dist,0,0,0])
    #Estrutura para armazenar os indices da ordem dos filhos
    indices = []

    #Descobrir se foi possivel chegar ao final
    FINAL = 0

    #Enquanto tiver alguem na fila faremos o processamento
    while fila:
    #Verifica se estamos no fim
        if labirinto[fila[0][0]][fila[0][1]] == '$':
            FINAL = 1
            break #saimos do loop, o resto da fila nao sera necessario verificar

    #Colocamos a posicao dos filhos na nossa fila auxiliar
        fila_aux.append([fila[0][0] - 1, fila[0][1]])
        fila_aux.append([fila[0][0], fila[0][1]-1])
        fila_aux.append([fila[0][0] + 1, fila[0][1]])
        fila_aux.append([fila[0][0], fila[0][1] + 1])
        j=0

    #Filho 1, se for um lugar possivel de ir e ele nao esta presente na fila, calculamos a distancia entre ele e o final do labirinto, e dizemos que um filho foi usado (j++)
    #Caso esse filho seja possivel, colocamos ele como uma visita e o valor atual sera seu anterior
        if  fila[0][0] - 1 >= 0 and (labirinto[fila[0][0] - 1][fila[0][1]] == '*' or labirinto[fila[0][0] - 1][fila[0][1]] == '$') and ([fila[0][0] - 1,fila[0][1]] in fila) == 0:
            distancia = (pow(pow(fila[0][0] -1 - fim[0],2) + pow(fila[0][1] - fim[1],2),1/2))
            dist[0] = distancia
            j = j +1
            visitas.append([fila[0][0] - 1, fila[0][1]])
            anterior.append(fila[0])
        else:
    #Se o filho nao foi usado, colocamos a distancia dele como muito grande
            dist[0] = 800000

    #Filho 2
        if  fila[0][1] - 1 >= 0 and (labirinto[fila[0][0]][fila[0][1]-1] == '*' or labirinto[fila[0][0]][fila[0][1]-1] == '$')and ([fila[0][0],fila[0][1]-1] in fila) == 0:
            distancia = (pow(pow(fila[0][0]- fim[0],2) + pow(fila[0][1] - 1 - fim[1],2),1/2))
            dist[1] = distancia
            j = j +1
            visitas.append([fila[0][0], fila[0][1]-1])
            anterior.append(fila[0])
        else:
            dist[1] = 800000

    #Filho 3
        if  fila[0][0] + 1 < lin and (labirinto[fila[0][0] + 1][fila[0][1]] == '*' or labirinto[fila[0][0] + 1][fila[0][1]] == '$') and ([fila[0][0] +1,fila[0][1]] in fila) == 0:
            distancia = (pow(pow(fila[0][0] + 1- fim[0],2) + pow(fila[0][1] - fim[1],2),1/2))
            dist[2] = distancia
            j = j +1
            visitas.append([fila[0][0] + 1, fila[0][1]])
            anterior.append(fila[0])  

        else:
            dist[2] = 800000
            
    #Filho 4
        if  fila[0][1] + 1 < col and (labirinto[fila[0][0]][fila[0][1] + 1] == '*' or labirinto[fila[0][0]][fila[0][1] + 1] == '$')  and ([fila[0][0],fila[0][1] + 1] in fila) == 0:
            distancia = (pow(pow(fila[0][0]- fim[0],2) + pow(fila[0][1] + 1 - fim[1],2),1/2))
            dist[3] = distancia
            j = j +1
            visitas.append([fila[0][0], fila[0][1]+1])
            anterior.append(fila[0])
        else:
            dist[3] = 800000

    #A posicao que acabamos de visitar passa a ser parte dos lugares que ja visitamos e tiramos ela da fila
        labirinto[fila[0][0]][fila[0][1]] = 'Q'
        del(fila[0])

    #Entao descobrimos a ordem dos filhos, para pegar o menor
        indices = np.argsort(dist)
        fila_aux2 = []
    #Ordenamos os filhos e colocamos eles na fila como os proximos a serem visitados, observe que colocaremos apenas filho que existem, isso eh determinado pelo tamanho de j    
        for i in range(j):
            fila_aux2.append(fila_aux[indices[i]])
        fila = fila_aux2 + fila 
        fila_aux = []

    #Descobriremos qual caminho foi percorrido ate chegar no final (caso o final tenha sido alcancado)
    ants = fim
    if FINAL == 1:
        while(ants != inicio):
            x = visitas.index(ants)        
            ants = anterior[x]
            labirinto[ants[0]][ants[1]] = 'M'
    else:
        print('Labirinto sem Saida')    

    labirinto[inicio[0]][inicio[1]] = '#'

    #Retornamos o labirinto para um arquivo texto Result.txt
    init = str(lin) + ' ' + str(col)
    f = open('Result.txt','w')
    f.write(init)
    f.write('\n')
    for i in range(lin):
        for j in range(col):
            f.write(labirinto[i][j])
        f.write('\n')

    f.close()

