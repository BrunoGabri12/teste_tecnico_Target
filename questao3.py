
import json 


#carregando o arquivo .json 
with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

menorValor = dados[0]['valor']
maiorValor = dados[0]['valor']
mediaValor = 0 
quantidade_dias_trabalhados= 0 
dias_com_faturamento_superior = 0 

for i in dados:

  #realiza o calculo do maior valor
   if(i['valor'] > maiorValor):
    maiorValor = i['valor']

  #realiza o calculo do menor valor do mês, desconsiderando os dias não trabalhados e feriados
   if(i['valor'] < menorValor and i['valor'] != 0 ):
    menorValor = i['valor']


  #desconsiderando os dias não trabalhos e feriados
   if(i['valor'] != 0):
    mediaValor = mediaValor + i['valor']
    quantidade_dias_trabalhados += 1

#calculo da média 
mediaValor = mediaValor/quantidade_dias_trabalhados


for i in dados:
  if(i['valor'] > mediaValor):
    dias_com_faturamento_superior += 1



print("O menor faturamento do mês foi de = " + str(menorValor))
print("O maior faturamento do mês foi de = " + str(maiorValor))
print("A médica de faturamento do mês foi de = " + str(mediaValor))
print("Os dias com rendimento superior que a média foi de = "+ str(dias_com_faturamento_superior))