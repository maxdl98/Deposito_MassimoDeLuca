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

exit = False  

for i in range(1):
    user_input = input("Quale numero uscirà? (Scrivi 'esci' per uscire): ")

    if user_input.lower() == "esci":
        print("Sei uscito dal programma.")
        exit = True
        break  

    try:
        input_number = int(user_input)  
    except ValueError:
        print("Per favore, inserisci un numero valido o 'esci' per uscire.")
        continue  

    numero = random.randint(1, 100)

    if input_number == numero:
        print("Hai indovinato il numero!")
    elif numero >= 70 and numero <= 100 and input_number >= 70:
        print("Il numero era {numero}. ci sei andato vicino")
    else:
        print("Il numero era {numero}. Non hai indovinato.")

    risposta = input("Vuoi continuare? (Scrivi 'esci' per uscire): ").lower()

    if risposta == "esci":
        print("Sei uscito dal programma.")
        exit = True
        break  # Esce dal ciclo

    
  
    
    