#Algoritimo Best First Search de busca

import numpy as np

#Le o labirinto do arquivo Labirinto.txt
labirinto = []
lab = []
f = open('Labirinto.txt')
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

#Teremos uma fila que armazena quais os proximos lugares do labirinto a serem visitados e uma fila auxiliar para ajudar a encontrar a ordem dos proximos a serem visitados
fila = []
fila.append(inicio)
fila_aux = []
fila_aux.append(inicio)


#Usaremos distancia euclidiana para determinar o proximo da fila
dist = []
dist.append(pow(pow(inicio[0] - fim[0],2) + pow(inicio[1] - fim[1],2),1/2))

dist = np.array(dist)
indices = []

#Descobrir se foi possivel chegar ao final
FINAL = 0

#Enquanto tiver alguem na fila faremos o processamento
while fila:
#Verifica se estamos no fim
    if labirinto[fila[0][0]][fila[0][1]] == '$':
        FINAL = 1
        break #saimos do loop, o resto da fila nao sera necessario verificar


#Filho 1, se for um lugar possivel de ir e ele nao esta presente na fila, calculamos a distancia entre ele e o final do labirinto e adicionamos ele a fila
#Caso esse filho seja possivel, colocamos ele como uma visita e o valor atual sera seu anterior
    if  fila[0][0] - 1 >= 0 and (labirinto[fila[0][0] - 1][fila[0][1]] == '*' or labirinto[fila[0][0] - 1][fila[0][1]] == '$') and ([fila[0][0] - 1,fila[0][1]] in fila) == 0:
        fila.append([fila[0][0] - 1, fila[0][1]])
        fila_aux.append([fila[0][0] - 1, fila[0][1]])
        distancia = (pow(pow(fila[0][0] -1 - fim[0],2) + pow(fila[0][1] - fim[1],2),1/2))
        dist = np.insert(dist,len(fila)-1,distancia)
        visitas.append([fila[0][0] - 1, fila[0][1]])
        anterior.append(fila[0])

#Filho 2
    if  fila[0][1] - 1 >= 0 and (labirinto[fila[0][0]][fila[0][1]-1] == '*' or labirinto[fila[0][0]][fila[0][1]-1] == '$') and ([fila[0][0],fila[0][1]-1] in fila) == 0:
        fila.append([fila[0][0], fila[0][1]-1])
        fila_aux.append([fila[0][0], fila[0][1]-1])
        distancia = (pow(pow(fila[0][0]- fim[0],2) + pow(fila[0][1] - 1 - fim[1],2),1/2))
        dist = np.insert(dist,len(fila)-1,distancia)
        visitas.append([fila[0][0], fila[0][1]-1])
        anterior.append(fila[0])

#Filho 3
    if  fila[0][0] + 1 < lin and (labirinto[fila[0][0] + 1][fila[0][1]] == '*' or labirinto[fila[0][0] + 1][fila[0][1]] == '$') and ([fila[0][0] + 1,fila[0][1]] in fila) == 0:
        fila.append([fila[0][0] + 1, fila[0][1]])
        fila_aux.append([fila[0][0] + 1, fila[0][1]])
        distancia = (pow(pow(fila[0][0] + 1- fim[0],2) + pow(fila[0][1] - fim[1],2),1/2))
        dist = np.insert(dist,len(fila)-1,distancia)
        visitas.append([fila[0][0] + 1, fila[0][1]])
        anterior.append(fila[0])
        

#Filho 4
    if  fila[0][1] + 1 < col and (labirinto[fila[0][0]][fila[0][1] + 1] == '*' or labirinto[fila[0][0]][fila[0][1] + 1] == '$') and ([fila[0][0],fila[0][1]+1] in fila) == 0:
        fila.append([fila[0][0], fila[0][1] + 1])
        fila_aux.append([fila[0][0], fila[0][1] + 1])
        distancia = (pow(pow(fila[0][0]- fim[0],2) + pow(fila[0][1] + 1 - fim[1],2),1/2))
        dist = np.insert(dist,len(fila)-1,distancia)
        visitas.append([fila[0][0], fila[0][1]+1])
        anterior.append(fila[0])

#Posicao atual passa a ser um lugar ja visitado, entao deletamos ele da fila, e a sua distancia
    labirinto[fila[0][0]][fila[0][1]] = 'Q'
    del(fila[0])
    del(fila_aux[0])
    dist = np.delete(dist,0)

#Entao processamos a fila para deixá-la em ordem
#Trabalhamos com o principio que os indices da distancia e os indices da fila sao equivalentes. Entao ordenamos 
#as distancias e mudamos a fila para que a distancia menor da fila passe a ser o primeiro valor da fila
    indices = np.argsort(dist)
    dist = np.sort(dist)
    for i in range(len(dist)):
        fila_aux[i] = fila[indices[i]]
    for i in range(len(dist)):
        fila[i] = fila_aux[i]
    

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

