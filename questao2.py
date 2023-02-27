# Questão 2 do desafio  

def calcula__fibonacci(numero__informado):

    sequencia_fibo = 0 
    primeiro_anterior = 0
    segundo_anterior = 1

    while(sequencia_fibo < numero__informado):
     
        sequencia_fibo = primeiro_anterior + segundo_anterior
        segundo_anterior = primeiro_anterior
        primeiro_anterior = sequencia_fibo

    if(numero__informado == sequencia_fibo):
        print("O numero " + str(numero__informado) + " pertence a sequencia")
    else: 
        print("O numero " + str(numero__informado) + " não pertence a sequencia")


calcula__fibonacci(6)