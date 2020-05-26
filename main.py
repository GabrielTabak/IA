
import sys
import AE
import Best
import Hill
import Largura
import Profundidade
import time


if(len(sys.argv) <= 2):
    print("Erro: argumentos faltando, uso: \n ")
    print("python3 main.py algoritmo input.txt")
    print("algoritmo = { AE, Best, Hill, Largura, Profundidade}\n")
    exit()

algoritmo_usado = sys.argv[1]
inputFile = sys.argv[2]


if(algoritmo_usado == "AE"):
    funcAlgo = AE.calculate 
elif(algoritmo_usado == "Best"):
    funcAlgo = Best.calculate 
elif(algoritmo_usado == "Hill"):
    funcAlgo = Hill.calculate 
elif(algoritmo_usado == "Largura"):
    funcAlgo = Largura.calculate 
elif(algoritmo_usado == "Profundidade"):
    funcAlgo = Profundidade.calculate 
else:
    print("Erro: algoritmo " + algoritmo_usado + " não reconhecido")
    print("algoritmo = { AE, Best, Hill, Largura, Profundidade}\n")
    exit()


print("Usando algoritmo: " + algoritmo_usado)
print("Input file: " + inputFile)

start = time.time()
funcAlgo(str(inputFile))
end = time.time()

elapsedTime = end - start

print("Tempo de execuçaõ: " + str(elapsedTime))


print("\n\nAbrindo interface, info: ")
import Interface
Interface.showInterfaceFromFile("Result.txt",algoritmo_usado)