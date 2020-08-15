# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 21:36:30 2020

@author: Giovanni
"""

#import sys
#import cplex
#from cplex.exceptions import CplexError
from math import sqrt
from docplex.mp.model import Model
#import numpy as np 
import matplotlib.pyplot as plt


def distancia2pontos(d1_X, d1_Y, d2_X, d2_Y):
    #print(d1_X)
    #print(d1_Y)
    #print(d2_X)
    #print(d2_Y)
    
    dist = sqrt(((d1_X - d2_X)**2) + ((d1_Y - d2_Y)**2))
    
    return dist

def main():
    # LEITURA DO ARQUIVO: 
    arquivo = open('entrada1.txt','r')    
    distritos = []

    numDistritos = int(arquivo.readline()) # N
    #print(numDistritos)
    
    dist_upa1 = int(arquivo.readline()) # K 
    #print(dist_upa1)

    dist_upa2 = int(arquivo.readline()) # Y 
    #print(dist_upa2)
    
    distanciaUPAS = int(arquivo.readline())
    #print(distanciaUPAS)

    file = arquivo.readlines() 
    aux = file[:]
    for i in aux:
        distritos.append([int(s) for s in i.split() if s.isdigit()])
        #print(distritos)
    # LEITURA DO ARQUIVO FEITA
    
    # CPLEX 
    prob = Model('Localizacao de UPAs')
    X = []
    for i in range(numDistritos):
        X.append(0)
    #X = np.zeros(numDistritos) 
    
    for i in range(numDistritos):
        X[i] = prob.binary_var(name="X"+str(i))

    # Função Objetivo
    prob.minimize(prob.sum(X[g] for g in range(numDistritos)))
        
    # Primeira Restrição:


    for j in range(numDistritos): 
            prob.add_constraint(prob.sum(X[i]  for i in range(numDistritos)
                   if distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]) <= dist_upa1 )   
                    >= 1 , ctname = "Primeira Restrição")                        
        

    # Segunda Restrição:   

    for j in range(numDistritos): 
            prob.add_constraint(prob.sum(X[i]  for i in range(numDistritos)
                   if distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]) <= dist_upa2  )   
                       >= 1 , ctname = "Segunda Restrição")                        

    # Terceira Restrição: 
    for i in range(numDistritos) :
        for j in range(numDistritos) : 
            #X[i] = int([X[i]])
            if i != j : 
                if distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]) <= distanciaUPAS: 
                    #print(distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]))
                    prob.add_constraint(X[i] + X[j] <= 1 , ctname="Terceira Restrição")  
                    
#    for i in range(numDistritos):
#        for j in range(numDistritos):
#            if i!=j :
#                if distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]) <= dist_upa1: 
#                    print("de", X[i], "para", X[j])
#                   print(distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]))
                    

    #print(prob.export_to_string()) # Comando que mostra a modelagem
    
 
    # Saída
    #prob.print_information() # Comando que mostra informações do modelo 
    
    solution = prob.solve(log_output=False) # Mudar para True para ver informações
    
    solution.display() # Mostra a Solução ótima 
    
    ar = prob.solution.get_all_values()    
    #print(ar[1])      
#    sol = prob.get_solve_status()
#    print("Solution status: " + str(sol))
    #distancias = []
    #distancias2 = []
    for i in range(numDistritos):    
        if ar[i] > 0:
            print("UPA localizada no distrito:", i)
#        else:            
#           for j in range(numDistritos):
#                if ar[j] > 0 : 
#                    if distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]) <= dist_upa1:
#                        if distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]) != 0:
#                            distancias.append(distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]))
#                            mais_prox = min(distancias)
           # print("Distância do distrito", i, "para a UPA mais próxima:", mais_prox )
#           for j in range(numDistritos):
#                if ar[j] > 0 : 
#                    if distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]) <= dist_upa2:
#                        if distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]) != 0:
#                            distancias2.append(distancia2pontos(distritos[i][0],distritos[i][1],distritos[j][0], distritos[j][1]))
#                            segund_mais_prox = min(distancias2)
#           print("Distância do distrito", i, "para a segunda UPA mais próxima:", segund_mais_prox )           
    
    # Plotar Sistema de Coordenadas
    
    # Fazer função de pegar maior Y e X 
    for i in range(numDistritos) :
        if ar[i] == True: 
            plt.plot(distritos[i][0], distritos[i][1],'o',color='red')
        else: 
            plt.plot(distritos[i][0], distritos[i][1],'o',color='black')
        
    plt.axis([0,100,0,100])    
    plt.show()
   

            
if __name__ == "__main__":
   main()
  