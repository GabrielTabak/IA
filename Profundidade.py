#Algoritmo Busca em profundidade
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
    #Usamos uma fila para decidir qual o proximo a ser visitado
    fila = []
    fila.append(inicio)

    #Verificar se encontramos a saida do labirinto
    FINAL = 0

    #Enquanto tiver alguem na fila vamos processar a fila
    while fila:

    #Verifica se estamos no fim
        if labirinto[fila[0][0]][fila[0][1]] == '$':
            FINAL = 1
            break

    #Filho 1, se for um lugar possivel de ir e ele nao esta presente na fila, ele sera inserido na fila como o proximo da fila
    #Caso esse filho seja possivel, colocamos ele como uma visita e o valor atual sera seu anterior
        if  fila[0][0] - 1 >= 0 and (labirinto[fila[0][0] - 1][fila[0][1]] == '*' or labirinto[fila[0][0] - 1][fila[0][1]] == '$'  and ([fila[0][0] - 1,fila[0][1]] in fila) == 0):
            fila.insert(1,[fila[0][0] - 1, fila[0][1]])
            visitas.append([fila[0][0] - 1, fila[0][1]])
            anterior.append(fila[0])

    #Filho 2
        if  fila[0][1] - 1 >= 0 and (labirinto[fila[0][0]][fila[0][1]-1] == '*' or labirinto[fila[0][0]][fila[0][1]-1] == '$')  and ([fila[0][0],fila[0][1]-1] in fila) == 0:
            fila.insert(1,[fila[0][0], fila[0][1]-1])
            visitas.append([fila[0][0], fila[0][1]-1])
            anterior.append(fila[0])

    #Filho 3
        if  fila[0][0] + 1 < lin and (labirinto[fila[0][0] + 1][fila[0][1]] == '*' or labirinto[fila[0][0] + 1][fila[0][1]] == '$')  and ([fila[0][0] + 1,fila[0][1]] in fila) == 0:
            fila.insert(1,[fila[0][0] + 1, fila[0][1]])
            visitas.append([fila[0][0] + 1, fila[0][1]])
            anterior.append(fila[0])

    #Filho 4
        if  fila[0][1] + 1 < col and (labirinto[fila[0][0]][fila[0][1] + 1] == '*' or labirinto[fila[0][0]][fila[0][1] + 1] == '$')  and ([fila[0][0],fila[0][1]+1] in fila) == 0:
            fila.insert(1,[fila[0][0], fila[0][1] + 1])
            visitas.append([fila[0][0], fila[0][1]+1])
            anterior.append(fila[0])

    #Lugar da fila atual ja visitado, portanto sai da fila e seu valor no labirinto muda
        labirinto[fila[0][0]][fila[0][1]] = 'Q'
        del(fila[0])

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
