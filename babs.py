import tkinter as tk


class Libro:
    def __init__(self, cognome, nome, titolo, anno, collocazione, iban, note=""):
        if type(cognome) != str or type(nome) != str or type(titolo) != str or type(iban) != str or type(note) != str:
            raise TypeError("Parametri errati")
        if type(anno) != int:
            raise TypeError("Parametri errati")
        if type(collocazione) != tuple or type(collocazione[0]) != str or type(collocazione[1]) != int:
            raise TypeError("Parametri errati")

        self.cognome = cognome
        self.nome = nome
        self.titolo = titolo
        self.anno = anno
        self.coll = collocazione
        self.iban = iban
        self.note = note
        """ Crea un nuovo oggetto Libro
        :param cognome: cognome dell'autore
        :param nome: nome dell'autore
        :param titolo: titolo del libro
        :param anno: anno di pubblicazione
        :param collocazione: tupla (stringa,intero positivo)
        :param iban: IBAN (stringa) unico per ogni libro
        :param note: stringa eventualmente vuota
        """
        # pass #instruzione che non fa niente --> da sostituire con il codice

    def __str__(self):
        libro = [self.cognome, self.nome, self.titolo,
                 self.anno, self.coll, self.iban, self.note]

        return str(libro)
        """ Serializza un libro rappresentandolo come una stringa. La stringa
        puo' usare un formato a scelta dello studente
        :return: una stringa che rappresenta il libro
        """
        pass  # istruzione che non fa niente --> da sostituire con il codice

    def __eq__(self, a):
        uguali = True
        try:
            if self.cognome != a.cognome or self.nome != a.nome or self.titolo != a.titolo or self.anno != a.anno or self.iban != a.iban:
                uguali = False
        except AttributeError:
            print("Un termine non è un oggetto Libro")
        else:
            return uguali
        """ stabilisce se self e a sono uguali -- due libri sono cosiderati uguali
            se hanno esattamente gli stessi campi (eccetto le note e la collocazione)  """

        pass  # instruzione che non fa niente --> da sostituire con il codice


class Catalogo:
    def __init__(self):
        self.dizionario = {}

        """Crea un catalogo vuoto rappresentato come un dizionario di
           libri con chiave iban"""
        pass  # instruzione che non fa niente --> da sostituire con il codice

    def n_books(self):
        return len(self.dizionario)
        """Ritorna il numero di libri nel catalogo """
        pass  # instruzione che non fa niente --> da sostituire con il codice

    def inserisci(self, li):
        if li.iban in self.dizionario:
            return False
        else:
            self.dizionario[li.iban] = li
            return True

        """Inserisce un nuovo libro nel catalogo:
            se l'iban è già presente non modifica il catalogo
            :param: li oggetto libro da inserire
            :returns: True se il libro è stato inserito
            :returns: False altrimenti """
        pass  # instruzione che non fa niente --> da sostituire con il codice

    def __str__(self):
        cata = ""
        for lib in self.dizionario:
            cata = cata + str(self.dizionario[lib]) + "\n"
        self.cata = cata
        return cata
        """Serializza il catalogo in una stringa che contiene tutti i libri
        in ordine di IBAN crescente.
        Ogni libro è separato dal successivo da "\n" """
        pass  # instruzione che non fa niente --> da sostituire con il codice

    def store(self, nomefile):
        with open(nomefile, "w") as f:
            f.write(self.cata)
        """Scrive il catalogo sul file "nomefile" -- > formato a scelta dello studente
         da specificare nei commenti"""
        pass  # instruzione che non fa niente --> da sostituire con il codice

    def load(self, nomefile):
        try:
            f = open(nomefile, "r")
        except FileNotFoundError:
            print("Il file non esiste!")
        except OSError as e:
            print(e)
        else:
            self.dizionario = {}
            for aline in f:
                self.dizionario.inserisci(Libro(aline))
                char_del = [",", ".", "[", "]", "\'", "\""]
                for carattere in aline:
                    if carattere in char_del:
                        aline.replace(carattere, "")
                print(aline)
                print(self.dizionario)
            f.close()
        """Legge il catalogo dal file "nomefile" nel formato a scelta dello studente
        e lo carica nel catalogo eliminando tutto il contenuto precedente
        del catalogo """
        pass  # instruzione che non fa niente --> da sostituire con il codice

    def __eq__(self, cat2):
        if self.dizionario == cat2.dizionario:
            return True
        else:
            return False
        """stabilisce se due cataloghi contengono
        esattamente gli stessi libri
        :param cat2: secondo catalogo da confrontare
        :return: True se sono uguali, False altrimenti
        """
        pass  # istruzione che non fa niente --> da sostituire con il codice


class finestra:
    def __init__(self, root):
        """__init__ definisce l'aspetto (task1) e crea lo stato accessibile da tutti
        i metodi (finestra, widget etc...) """
        # creazione finestra e geometria
        self.root = root
        self.root.title("Biblioteca")
        self.root.geometry("1000x1000")

        self.label = tk.Label(text="I libri presenti nel catalogo sono:")
        self.label.pack()

        # creazione dei bottoni
        self.btn_animale = tk.Button(
            bg="yellow", text="Animale", width=25, height=3)
        self.btn_minerale = tk.Button(
            bg="pink", text="Minerale", width=25, height=3)
        self.btn_vegetale = tk.Button(
            bg="light green", text="Vegetale", width=25, height=3)
        self.btn_exit = tk.Button(bg="red", text="EXIT", width=25, height=2)

        # inseriamo i bottoni nella finestra
        self.btn_animale.pack()
        self.btn_vegetale.pack()
        self.btn_minerale.pack()
        self.btn_exit.pack()

        # label che conterrà le risposte
        self.res = tk.Label(text=" ")
        self.res.pack()

        # ---------------------------------------------------------
        # task 3: associare eventi 'interessanti'
        # con i gestori di eventi.
        # tutti i bottoni sono associati al tasto di sinistra del mouse
        # ---------------------------------------------------------
        self.btn_animale.bind("<Button-1>", self.handler_animale)
        self.btn_minerale.bind("<Button-1>", self.handler_minerale)
        self.btn_vegetale.bind("<Button-1>", self.handler_vegetale)
        self.btn_exit.bind("<Button-1>", self.handler_exit)

    # task 2: definizione dei gestori degli eventi

    def handler_animale(self, evento):
        # restituisce la risposta
        self.res.destroy()
        self.res = tk.Label(
            text="Non è un animale: ritenta", height=5, width=20)
        self.res.pack()

    def handler_vegetale(self, evento):
        # restituisce la risposta
        self.res.destroy()
        self.res = tk.Label(text="Bravo!!! Hai indovinato", height=5, width=20)
        self.res.pack()

    def handler_minerale(self, evento):
        # restituisce la risposta
        self.res.destroy()
        self.res = tk.Label(
            text="Non è un minerale: ritenta", height=5, width=20)
        self.res.pack()

    def handler_exit(self, evento):
        # chiude la finestra
        self.root.destroy()


# attivazione dell'interfaccia
root = tk.Tk()
finestra(root)
# task 4: avvio del ciclo ascolto eventi
root.mainloop()
