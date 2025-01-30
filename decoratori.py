


def decoratore(funzione):
    def wrapper():
        funzione()

        print("Ciao Massimo")

    return wrapper


@decoratore
def saluta():
    print("Benvenuto nel sistema")
    
saluta()

inp = int(input("Inserisci base"))
inp1 = int(input("Inserisci altezza"))

lato = int(input("Inserisci il lato1"))
lato2 = int(input("Inserisci lato2"))

def area_triangolo(funzione):
    def wrapper(base,altezza):
        
        risultato = funzione(base, altezza)
        
        return risultato
    return wrapper    
    

@area_triangolo
def CalcoloArea(inp, inp1):
    return inp * inp1 /2
print("ecco l'area del triangolo" , inp * inp1/2)

        
def area_rettangolo(funzione):
    def wrapper(base,altezza):
        
        risultato = funzione(base, altezza)
        
        return risultato
    return wrapper  


@area_rettangolo
def CalcoloAreaRettangolo(funzione):
        def wrapper(base,altezza):
              
         risultato = funzione(base, altezza)
         
         return risultato
        return wrapper
      

@area_rettangolo
def CalcoloAreaRett(inp, inp1):
    return(inp * inp1)
print("ecco l'area del rettangolo" , inp * inp1)



def area_quadrato(funzione):
    def wrapper(lato):
        
        risultato = funzione(lato)
        
        return risultato
    return wrapper  


@area_rettangolo
def CalcoloAreaQuadrato(lato):
    return(lato * lato)
print("ecco l'area del quadrato" , lato * lato)
ris = lato * lato


lista1 = []

lista1.append(ris)
print(lista1)


# def decoratore1(funzione):
#     def wrapper(*args, **kwargs):
#         print("Prima")
#         risultato = funzione(*args, **kwargs)

#         print("Dopo")
#         return risultato
#     return wrapper


# @decoratore1
# def somma(a,b,c,e,r):
#     return a + b + c + r + e

# print(somma(3,4,8,10,90))

# @decoratore1
# def somma1(a,b):
#     return a + b 

# print(somma1(3,4))     




