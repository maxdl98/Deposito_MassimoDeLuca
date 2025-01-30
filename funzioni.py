import random

# def somma(x,y):
#     return x + y



# print(somma(10,20))


# def NumeroMassimo(lista):
#     y = lista[0]
#     for numero in lista:
#        if(y < numero):
#            y = numero
           
#     return y





   
    
# list1 = [19,45,61,23,44]
    
# print(NumeroMassimo(list1))




# scrivi un programma che genera un numero casuale tra 1 e 100. 
# L'utente deve indovinare quale numero è stato generato. 
# Dopo ogni tentativo, il programma dovrebbe dire all'utente se il numero
# da indovinare è più alto o più basso rispetto al numero inserito. Il gioco termina
# quando l'utente indovina il numero o decide di uscire


cont = 0

import random

import random



# def indovinare(numero):
#    numeroCasuale = random.randint(1, 100)
#    continuo = False
#    while True:
#         if numero == numeroCasuale:
#             print("Bravo")
#             break  

#         if 80 <= numero <= 100 and 1 <= numeroCasuale <= 50:
#             print("Il numero casuale è inferiore a quello che hai scelto: {numeroCasuale}")
        
#         if 0 <= numero <= 50 and 51 <= numeroCasuale <= 100:
#             print(f"Il numero casuale è superiore rispetto a quello che hai scelto: {numeroCasuale}")
        
#         risposta = input("Vuoi continuare? scrivi esci ")
#         if risposta == "esci":
#             print("Sei uscito dal programma")
#             break  
#         else:
#             numero = int(input("Prova con un altro numero: "))  



# numeroScelto = int(input("Inserisci numero"))
# indovinare(numeroScelto)






# Scrivi un programma che chieda all'utente di inserire due numeri e quindi esegua
# una serie di operazioni matematiche su di essi (somma, sottrazione, moltiplicazione, divisione) 
# e visualizzi il risultato. Ogni volta che l'utente inserisce un'operazione,
# il programma deve mostrare il risultato dell'operazione corrispondente.
# Inoltre, dopo ogni calcolo, il programma deve chiedere all'utente
# se vuole continuare a fare altre operazioni con i numeri, oppure uscire dal programma.


def operazione(numero1, numero2):
    
    chiedere = input("Quale operazione vuoi effettuare? +? -? /? *? ")
    
    if(chiedere == "+"):
        return numero1 + numero2
    
    if(chiedere == "-"):
        return numero1 - numero2
    
    if(chiedere == "*"):
        return numero1 * numero2
    
    try:
            return numero1 / numero2
    except Exception:
            print(" non puoi dividere per 0")
            return None
        

        
        

print(operazione(5,5))


    
  
    
    
