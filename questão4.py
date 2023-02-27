faturamento = {'SP': 67836.43 ,'RJ': 36678.66 ,
               'MG':29229.88,'ES':27165.48,'Outros' :19849.53}


indices = faturamento.keys()

soma = 0

#pega o valor de cada estado
for indices in faturamento:
  soma += float(faturamento[indices])



#realiza a soma 
for indices in faturamento:
  porcentagem = (float(faturamento[indices])/soma ) *100

  print(indices + " = " + str(porcentagem))
