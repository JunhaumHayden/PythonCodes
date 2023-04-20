##Aluno: Carlos Benedito Hayden de Albuquerque Junior
##matricula: 23100455
##Questao 02


print("="*30)
print("    Questao 02")
print("="*30)

n = int(input("Informe o numero de pessoas detectadas: "))
  
tempo_inicial = 0
tempo_total_ligada = 0

for i in range(n):
    t = int(input("Informe o instante que a pessoa passou pelo sensor: "))
    
    if i == 0:
        tempo_inicial = t
    # Se a escada estava ligada, adiciona ao tempo total o tempo 
    # decorrido desde o último instante em que alguém passou pelo sensor
    elif t - tempo_inicial <= 10:
        tempo_total_ligada += t - tempo_inicial
       
    # Se a escada estava desligada, não faz nada
    else:
        pass
    
    # Atualiza o tempo inicial para o instante em que a pessoa atual passou pelo sensor
    tempo_inicial = t

# Se a última pessoa a passar pelo sensor deixou a escada ligada, adiciona ao tempo total o tempo decorrido desde então até o final do período de medição (100 segundos)
if t - tempo_inicial <= 10:
    tempo_total_ligada += t - tempo_inicial + 10

print(tempo_total_ligada)
   
print("="*30)
print("    Fim do programa")
print("="*30)    
