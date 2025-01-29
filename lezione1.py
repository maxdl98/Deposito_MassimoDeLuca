

# password1 = "1234"

# password2 = "5678"



# print(password2)

# if(password1 == password2):
#     print("Sono uguali")
# else:
#     print("Sono diversi")

# #nome = input("Inserisci nome")

# #eta = (int(input("Inserisci età")))

# #sono un commento


# stringa1 = "Matteo"
# stringa2= "Massimo"

# print(stringa1 + " " +  stringa2)


# lista1 = [1,2,3,4,5]

# print(lista1)

# lista1[3] = 10

# print(lista1)


# lista1.append(20)

# lista1.insert(2,40)
# lista1.sort

# print(lista1)



#start, stop , step. Da dove iniziamo, dove ci fermiamo, e quanti passi alla volta fare

# for i in range(3,12,4):
#     print(i)  
    
    
# #Esercizio 1
# numero = int(input("Inserisci un numero: "))

# if numero % 2 == 0:
#     print("{numero} è pari")
# else:
#     print("{numero} è dispari")



#Esercizio2 
#Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i numeri da 
#n a compreso, decrementando di 1.Deve potersi ripetere all'infinito



#numero1 = int(input("Inserisci un numero"))

#for i in range(numero1, -1, -1): 
 #   print(i)
 
    
    


# n = int(input("Quanti numeri vuoi inserire nella lista? "))


# lista1 = []

# for i in range(n):
#     numero = int(input(f"Inserisci il numero {i+1}: "))
#     lista1.append(numero)

# for numero in lista1:
#     print(numero ** 2)


# inp = input("Inserisci numeri separati da spazio: ")  

# lista1 = []  

# for numero in inp.split():
#     lista1.append(int(numero))  

# for numero in lista1:
#     operazione = numero ** 2
#     print(operazione)



# Scrivi un programma che conti il numero di vocali
# (a, e, i, o, u) in una stringa inserita dall'utente.

# vocali = input("Inserisci delle vocali")

# cont = 0

# for vocale in vocali.split():
#     if vocale == "a" or vocale == "e" or vocale == "i" or vocale == "o" or vocale == "u":
#         cont += 1
#         print(cont)
    
    

# lista = [10, 20, 30, 40, 50]

# for i in range(len(lista) - 1, -1, -1):  # Partiamo dall'ultimo elemento e arriviamo al primo
#     print(lista[i])
    
    
    

lista = input("Scrivi una lista di numeri separati")

numeri = [int(i) for i in lista.split()]

elemento = numeri[0]

for i in numeri:
    if i > elemento:
        elemento = i
        
        
print("il numero massimo è : ", elemento)

contare = 0
continuareAcontare = True
while continuareAcontare == True:
    for i in numeri:
        contare+=1
        print(contare)
        continuareAcontare = False

if(i == 0):
            print("La lista è vuota")
else:
            print("il numero massimo della lista è ", elemento)
            print("ecco quanti elementi contiene: ", contare)
            
        
    
        
        


   
    
    
    









   



    
   
    
    
    









   


