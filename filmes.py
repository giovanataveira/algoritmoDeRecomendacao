import scipy
from scipy import stats
import numpy as np

#criação dos dados 
matrix = np.array([[8,0,3,4,6],[5,6,1,8,9],[8,0,0,5,10]])
novoUser = [8,0,2,3,0]
nao_assistidos = [0,1,0,0,1]
print(matrix)
nomeFilmes= ['A Múmia', 'A Invocação do Mal','Frozen','Adoráveis Mulheres' ,'Venom']

#criando um vetor com 3 posições e preencher com zero
similarity = [0] * 3
print(matrix[0][0])
print(matrix[1][0])
print(matrix[1,:])

#para cada usuário no sistema
for i in range(0,3):
  #dados desse usuário
  temp = matrix[i,:]

  print(i, temp)
  #COMPARAR OS DADOS QUE O NOVO USER ASSISTIU (OU SEJA... QUE NOVOUSER != 0)
  tempUser= [t for n,t in zip(novoUser,temp) if n != 0]
  tempNovoUser= [n for n in novoUser if n != 0] 

  #para verificar o processo
  print('user:',i)
  print(tempUser, tempNovoUser)      

  
  similarity[i] = scipy.stats.pearsonr(tempUser,tempNovoUser)[0] 
print()

print(similarity)

nota_peso = np.zeros((3,5))

for nUser in range(3):
  for nFilme in range(5):
   
    nota_peso[nUser][nFilme] = nao_assistidos[nFilme] * matrix[nUser][nFilme] * similarity[nUser]

print(nota_peso)

notas_acumuladas = np.sum(nota_peso.T,axis=1)
print(notas_acumuladas)

temp_peso = nota_peso
temp_peso[nota_peso > 0] = 1
print(temp_peso) 

temp_similaridade = np.zeros((3,5)) 
for nUser in range(3):
  for nFilme in range(5):
    temp_similaridade[nUser][nFilme] = temp_peso[nUser][nFilme] * similarity[nUser]

print(temp_similaridade)

similaridade_acumulada = np.sum(temp_similaridade.T,axis=1)
print(similaridade_acumulada)

nota_final =[0] * 5
#(similaridade)
for nFilme in range(5):
  if(similaridade_acumulada[nFilme] > 0):
    nota_final[nFilme] =  notas_acumuladas[nFilme] / similaridade_acumulada[nFilme]
  else:
    nota_final[nFilme] = 0

print(nota_final)
nAssistidos = sum(nao_assistidos)

notasOrdenadasIndex = sorted(range(len(nota_final)),key=nota_final.__getitem__)[::-1][0:nAssistidos]
print(notasOrdenadasIndex)

for i in notasOrdenadasIndex:
  print(nomeFilmes[i], 'nota: ', nota_final[i])