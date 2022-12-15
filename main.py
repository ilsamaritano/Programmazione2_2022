# Script di test Assegnamento 2 622AA 2022/23 (non modificare)
from testMy import *
from babs_implementazione import *

def test_finale():
    #contiamo i test falliti
    testFalliti=0
    print("==========> Inizio nuovo test <=============\n\n")

    # creo un libro: test __init__ e __str__
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

    # i libri sono uguali
    if c1 != c:
        testFalliti +=1
    else:
        print("I libri",c,"\ne ",c1, "\nsono uguali")

    # test creazione catalogo e n_books
    print("==========> Test classe Catalogo ")
    cat = Catalogo()
    if cat.n_books() != 0:
        testFalliti+=1
    print("Il catalogo contiene ",cat.n_books()," libri")

    # test inserisci
    testFalliti += testEqual(cat.inserisci(Libro("Dexter", "Colin", "Il mondo silenzioso di Nicholas Quinn", 2012, ("G", 15),"334455")),True)
    if cat.n_books() != 1:
        testFalliti += 1
    #
    testFalliti += testEqual(cat.inserisci(Libro("Adams", "Douglas", "Guida galattica per gli autostoppisti",1980,("F",212),"89876","Traduzione Laura Serra. ")), True)
    if cat.n_books() != 2:
        testFalliti += 1
    testFalliti += testEqual(cat.inserisci(Libro("Dexter", "Colin", "L'ultima corsa per Woodstock", 2010, ("G", 14),"113377")), True)
    testFalliti += testEqual(cat.inserisci(Libro("Dexter", "Colin", "Niente vacanze per l'ispettore Morse", 2012, ("G", 16),"345678")),True)
    testFalliti += testEqual(cat.inserisci(Libro("Simenon", "Georges", "Gli intrusi", 2015, ("T", 33),"998867", "Donazione Giachi")),True)
    testFalliti += testEqual(cat.inserisci(Libro("Simenon", "Georges", "Gli intrusi", 2015, ("T", 33),"998867")), False)
    if cat.n_books() != 5:
        testFalliti += 1

    # test __str__
    print(cat)

    #test store/load
    b = str(cat)
    cat.store("File1.txt")
    cat1 = Catalogo()
    cat1.load("File1.txt")
    b1 = str(cat1)
    if b != b1:
        print("Load/Store non compatibili")
    else:
        print("Load/Store compatibili")
    # test file inesistente
    cat1.load("__XXFile1.txt")

    # test __eq__
    testFalliti +=testEqual(cat == cat1,True)
    cat1.inserisci(Libro("Dexter","Colin","Le figlie di Caino",2017,("G",22),"453678", "Copia danneggiata. "))
    print(cat1)
    testFalliti += testEqual(cat1==cat, False)


    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- creare e testare la GUI ed effettuare la consegna come da README")
    else:
        print("Test falliti: ",testFalliti)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_finale()
