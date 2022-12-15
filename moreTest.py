from testMy import *
from babs import *

print("==========> Test classe Libro ")
# parametri corretti
c = Libro("Adams", "Douglas", "Guida galattica per gli autostoppisti", 1980, ("F", 212), "89876",
            "Traduzione Laura Serra")
print(c)

#parametri errati
try:
    b = Libro("Adams", "Douglas", "Guida galattica per gli autostoppisti", 1980, ("F", 212), 89876,
                "Traduzione Laura Serra")
    print(b)
except:
    print("Paramentri errati")

# uguaglianza fra libri
c1 = Libro("Adams", "Douglas", "Guida galattica per gli autostoppisti", 1980, ("F", 213), "89876","Seconda Copia")
print(c1)

c2 = 12

# i libri sono uguali
if c2 != c:
    print("sono diversi")
else:
    print("I libri",c,"\ne ",c1, "\nsono uguali")

# test inserisci
cat = Catalogo()
cat.inserisci(Libro("Dexter", "Colin", "Il mondo silenzioso di Nicholas Quinn", 2012, ("G", 15),"334455"))
print(cat)