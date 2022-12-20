import tkinter as tk
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile


class Libro:
    def __init__(self, cognome, nome, titolo, anno, collocazione, iban, note=""):
        for el in [cognome, nome, titolo, iban, note]:
            if type(el) != str:
                raise TypeError("Il parametro " + str(el) +
                                " deve essere una stringa")
        if type(anno) != int:
            raise TypeError("Il parametro 'anno' deve essere un intero")
        if type(collocazione) != tuple or type(collocazione[0]) != str or type(collocazione[1]) != int:
            raise TypeError(
                "Il parametro 'collocazione' deve essere una tupla con una stringa e un intero")

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
        # libro = [self.cognome, self.nome, self.titolo,
        #   self.anno, self.coll, self.iban, self.note]
        if self.note == "":
            libro = str(self.cognome) + ", " + str(self.nome) + ", " + str(self.titolo) + \
                ", " + str(self.anno) + ", " + \
                str(self.coll) + ", " + str(self.iban)
        else:
            libro = str(self.cognome) + ", " + str(self.nome) + ", " + str(self.titolo) + ", " + \
                str(self.anno) + ", " + str(self.coll) + ", " + \
                str(self.iban) + ", " + str(self.note)

        return libro
        """ Serializza un libro rappresentandolo come una stringa. La stringa
        puo' usare un formato a scelta dello studente
        :return: una stringa che rappresenta il libro
        """
        # pass  # istruzione che non fa niente --> da sostituire con il codice

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

        # pass  # instruzione che non fa niente --> da sostituire con il codice


class Catalogo:
    def __init__(self):
        self.dizionario = {}

        """Crea un catalogo vuoto rappresentato come un dizionario di
           libri con chiave iban"""
        # pass  # instruzione che non fa niente --> da sostituire con il codice

    def n_books(self):
        return len(self.dizionario)
        """Ritorna il numero di libri nel catalogo """
        # pass  # instruzione che non fa niente --> da sostituire con il codice

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
        # pass  # instruzione che non fa niente --> da sostituire con il codice

    def __str__(self):
        cata = ""
        # ordino per iban crescente
        self.dizionario = dict(sorted(self.dizionario.items()))
        for lib in self.dizionario:
            cata = cata + str(self.dizionario[lib]) + "\n"
        self.cata = cata
        return cata
        """Serializza il catalogo in una stringa che contiene tutti i libri
        in ordine di IBAN crescente.
        Ogni libro è separato dal successivo da "\n" """
        # pass  # instruzione che non fa niente --> da sostituire con il codice

    def store(self, nomefile):
        cata = ""
        # ordino per iban crescente
        self.dizionario = dict(sorted(self.dizionario.items()))
        for lib in self.dizionario:
            cata = cata + str(self.dizionario[lib]) + "\n"
        with open(nomefile, "w") as f:
            f.write(cata)
        """Scrive il catalogo sul file "nomefile" -- > formato a scelta dello studente
         da specificare nei commenti"""
        # pass  # instruzione che non fa niente --> da sostituire con il codice

    def load(self, nomefile):
        try:
            f = open(nomefile, "r")
        except FileNotFoundError:
            print("Il file non esiste!")
        except OSError as e:
            print("Errore:" + e)
        else:
            self.dizionario = {}
            for aline in f:

                aline = aline.replace("\n", "")
                aline = aline.split(', ')
                del_char = "()',"
                for char in aline[4]:
                    if char in del_char:
                        aline[4] = aline[4].replace(char, "")
                new_coll_1 = aline[4]
                for char in aline[5]:
                    if char in del_char:
                        aline[5] = aline[5].replace(char, "")
                new_coll_2 = int(aline[5])
                new_collocazione = (new_coll_1, new_coll_2)
                if len(aline) > 7:  # se ha le note
                    new_libro = Libro(str(aline[0]), str(aline[1]), str(
                        aline[2]), int(aline[3]), new_collocazione, aline[6], aline[7])
                else:
                    new_libro = Libro(str(aline[0]), str(aline[1]), str(
                        aline[2]), int(aline[3]), new_collocazione, aline[6])
                self.inserisci(new_libro)
            f.close()
        """Legge il catalogo dal file "nomefile" nel formato a scelta dello studente
        e lo carica nel catalogo eliminando tutto il contenuto precedente
        del catalogo """
        # pass  # instruzione che non fa niente --> da sostituire con il codice

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
        # pass  # istruzione che non fa niente --> da sostituire con il codice


class Finestra:
    def __init__(self, root):
        """__init__ definisce l'aspetto (task1) e crea lo stato accessibile da tutti
        i metodi (finestra, widget etc...) """
        # creazione finestra e geometria
        self.root = root
        self.root.title("Biblioteca")
        self.root.geometry("600x600")

        cat = Catalogo()
        self.cat = cat
        numlibri = self.cat.n_books()
        self.label = tk.Label(
            text="I libri presenti nel catalogo sono: " + str(numlibri))
        self.label.pack()

        #self.label = tk.Label(text=Catalogo.dizionario)
        # self.label.pack()

        # creazione dei bottoni
        self.btn_inserisci = tk.Button(
            bg="white", text="Inserisci nuovo libro", width=30, height=3)
        self.btn_carica = tk.Button(
            bg="white", text="Carica un nuovo catalogo da file", width=30, height=3)
        self.btn_esporta = tk.Button(
            bg="white", text="Esporta il catalogo in un file", width=30, height=3)
        self.btn_exit = tk.Button(bg="red", text="Esci", width=30, height=2)

        # inseriamo i bottoni nella finestra
        self.btn_inserisci.pack()
        self.btn_esporta.pack()
        self.btn_carica.pack()
        self.btn_exit.pack()

        # label che conterrà le risposte
        self.res = tk.Label(text=" ")
        self.res.pack()

        # ---------------------------------------------------------
        # task 3: associare eventi 'interessanti'
        # con i gestori di eventi.
        # tutti i bottoni sono associati al tasto di sinistra del mouse
        # ---------------------------------------------------------
        self.btn_inserisci.bind("<Button-1>", self.handler_inserisci)
        self.btn_carica.bind("<Button-1>", self.handler_carica)
        self.btn_esporta.bind("<Button-1>", self.handler_esporta)
        self.btn_exit.bind("<Button-1>", self.handler_exit)

    # task 2: definizione dei gestori degli eventi

    def insert(self, evento):
        nuovolibro = evento.widget.get()
        nuovolibro = nuovolibro.replace("\"", "")
        nuovolibro = nuovolibro.replace("\'", "")
        nuovolibro = nuovolibro.split(",")
        # if len(nuovolibro)<6 o >8 scrivere "Inserire il numero corretto di elementi"
        new_coll1 = nuovolibro[4].replace("(", "").strip()
        new_coll2 = nuovolibro[5].replace(")", "").strip()
        newcollocazione = (new_coll1, int(new_coll2))
        if len(nuovolibro) > 7:
            new_book = Libro(nuovolibro[0].strip(), nuovolibro[1].strip(), nuovolibro[2].strip(
            ), int(nuovolibro[3]), newcollocazione, nuovolibro[6].strip(), nuovolibro[7].strip())
        else:
            new_book = Libro(nuovolibro[0].strip(), nuovolibro[1].strip(), nuovolibro[2].strip(
            ), int(nuovolibro[3]), newcollocazione, nuovolibro[6].strip())

        self.cat.inserisci(new_book)

        evento.widget.delete(0, tk.END)

    def handler_inserisci(self, evento):
        # inserisce il libro nel catalogo

        label1 = tk.Label(text="\n Inserisci un libro nel seguente formato:")
        label2 = tk.Label(
            text='"Cognome", "Nome", "Titolo", anno, collocazione es:("G",22),"iban", "note (facoltativo)"')
        label3 = tk.Label(text="poi clicca Invio \n")
        entry = tk.Entry(self.root, bg="white", width=60)

        # inseriamo il widget nella finestra pack() fa il resize includendo i widget in ordine
        label1.pack()
        label2.pack()
        label3.pack()
        entry.pack()
        entry.bind("<Return>", self.insert)

        self.res.destroy()
        self.res = tk.Label(
            text=" ", height=5, width=20)
        self.res.pack()

    def handler_esporta(self, evento):
        # esporta il catalogo in formato txt
        files = [('Documento di testo', '*.txt')]
        file = asksaveasfile(title='Scegli dove esportare il catalogo',
                             filetypes=files, defaultextension=files)
        print("file", file.name)
        self.cat.store(file.name)
        print(self.cat)
        self.res.destroy()
        self.res = tk.Label(text=" ", height=5, width=20)
        self.res.pack()

    def handler_carica(self, evento):
        # carica un catalogo da file txt
        files = [('Documento di testo', '*.txt')]
        file = fd.askopenfilename(
            title='Carica un catalogo',
            filetypes=files)
        #print("file", file)
        self.cat.load(file)
        self.res.destroy()
        self.res = tk.Label(
            text=" ", height=5, width=20)
        self.res.pack()

    def handler_exit(self, evento):
        # chiude la finestra
        self.root.destroy()


# attivazione dell'interfaccia
root = tk.Tk()
Finestra(root)
# task 4: avvio del ciclo ascolto eventi
root.mainloop()
