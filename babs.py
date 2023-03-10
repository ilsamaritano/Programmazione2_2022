import tkinter as tk
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox


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
            print("Un termine non ?? un oggetto Libro")
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
            se l'iban ?? gi?? presente non modifica il catalogo
            :param: li oggetto libro da inserire
            :returns: True se il libro ?? stato inserito
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
        Ogni libro ?? separato dal successivo da "\n" """
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
        self.root.geometry("800x800")

        self.cat = Catalogo()

        #self.label = tk.Label(text=Catalogo.dizionario)
        # self.label.pack()

        # creazione dei bottoni
        self.btn_visualizzacatalogo = tk.Button(
            bg="white", text="Visualizza elementi nel catalogo", width=30, height=3)
        self.btn_inserisci = tk.Button(
            bg="white", text="Inserisci nuovo libro", width=30, height=3)
        self.btn_carica = tk.Button(
            bg="white", text="Carica un nuovo catalogo da file", width=30, height=3)
        self.btn_esporta = tk.Button(
            bg="white", text="Esporta il catalogo in un file", width=30, height=3)
        self.btn_exit = tk.Button(bg="red", text="Esci", width=30, height=2)

        # inseriamo i bottoni nella finestra
        self.btn_visualizzacatalogo.pack()
        self.btn_inserisci.pack()
        self.btn_esporta.pack()
        self.btn_carica.pack()
        self.btn_exit.pack()

        # label che conterr?? le risposte
        self.res = tk.Label(text=" ")
        self.res.pack()

        # ---------------------------------------------------------
        # task 3: associare eventi 'interessanti'
        # con i gestori di eventi.
        # tutti i bottoni sono associati al tasto di sinistra del mouse
        # ---------------------------------------------------------
        self.btn_visualizzacatalogo.bind("<Button-1>", self.handler_visualizza)
        self.btn_inserisci.bind("<Button-1>", self.handler_inserisci)
        self.btn_carica.bind("<Button-1>", self.handler_carica)
        self.btn_esporta.bind("<Button-1>", self.handler_esporta)
        self.btn_exit.bind("<Button-1>", self.handler_exit)

    # task 2: definizione dei gestori degli eventi

    def handler_visualizza(self, root):

        try:
            self.destroy_insert()
        except(AttributeError):
            pass

        numlibri = self.cat.n_books()

        self.res["text"] = "\n Numero di libri presenti nel catalogo: " + \
            str(numlibri)

        if(numlibri > 0):
            self.res["text"] = self.res["text"] + \
                "\n I libri presenti nel catalogo sono: \n" + str(self.cat)

    def destroy_insert(self):
        campi_inseriti = ["cognome", "nome", "titolo", "anno",
                          "collocazione-lettera", "collocazione-numero", "iban", "note"]
        for cam in campi_inseriti:
            self.rows[cam].destroy()
        self.label1.destroy()
        self.btn_submitBook.destroy()

    def inseriscilo(self):

        # controllo i tipi di elementi inseriti
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'???????????? "
        numbers = "1234567890"
        param = ["cognome", "nome", "collocazione-lettera",
                 "anno", "collocazione-numero", "iban"]
        for elem in param:
            if self.entrate[elem].get() != "":
                continue
            else:
                return messagebox.showerror("Errore", "Il campo "+elem.capitalize()+" non pu?? essere vuoto!")

        for el in ["cognome", "nome", "collocazione-lettera"]:
            for char in self.entrate[el].get():
                if char not in alphabet:
                    return messagebox.showerror("Errore", "Il campo "+el+" pu?? contenere solo lettere")
        for el in ["anno", "collocazione-numero", "iban"]:
            for char in self.entrate[el].get():
                if char not in numbers:
                    return messagebox.showerror("Errore", "Il campo "+el+" pu?? contenere solo numeri")

        # creo il libro e lo inserisco
        collocazione = (self.entrate["collocazione-lettera"].get().upper(),
                        int(float(self.entrate["collocazione-numero"].get())))
        newBook = Libro(self.entrate["cognome"].get(), self.entrate["nome"].get(), self.entrate["titolo"].get(),
                        int(self.entrate["anno"].get()), collocazione,
                        self.entrate["iban"].get(), self.entrate["note"].get())

        try:
            self.cat.inserisci(newBook)
        except(ValueError):
            self.res["text"] = "Errore nell'inserimento"
        else:
            self.res["text"] = "L'inserimento ?? avvenuto correttamente"
            self.destroy_insert()
        # evento.widget.delete(0,tk.END)   #cancella fra un inserimento e l???altro

    def handler_inserisci(self, root):
        self.res["text"] = " "
        self.label1 = tk.Label(text="\n Inserisci i dati del nuovo libro:")
        self.label1.pack()
        campi_inseriti = ["cognome", "nome", "titolo", "anno",
                          "collocazione-lettera", "collocazione-numero", "iban", "note"]
        self.entrate = {}
        self.rows = {}
        for campo in campi_inseriti:
            val = tk.StringVar()
            self.rows[campo] = tk.Frame(master=self.root)
            label = tk.Label(
                master=self.rows[campo], width=22, text=campo.capitalize()+": ", anchor='w', padx=20)
            self.entrate[campo] = tk.Entry(
                master=self.rows[campo], textvariable=val, width=30)
            self.rows[campo].pack(side=tk.TOP, fill=tk.X, pady=5)
            label.pack(side=tk.LEFT)
            self.entrate[campo].pack(
                side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=25)

        self.btn_submitBook = tk.Button(
            bg="white", text="Inserisci il libro", width=20, height=2, command=self.inseriscilo)
        self.btn_submitBook.pack()

    def handler_esporta(self, evento):
        # esporta il catalogo in formato txt
        files = [('Documento di testo', '*.txt')]
        file = asksaveasfile(title='Scegli dove esportare il catalogo',
                             filetypes=files, defaultextension=files)

        try:
            self.cat.store(file.name)
        except(FileExistsError, FileNotFoundError):
            return messagebox.showerror("Errore", "Il file non ?? presente.")
        except(AttributeError):
            return messagebox.showerror("Errore", "E' necessario selezionare un file.")
        else:
            risposta = messagebox.askyesno(
                "Domanda", "Desideri svuotare il catalogo dopo l'esportazione?")
            if risposta:
                self.cat = Catalogo()
                self.res["text"] = "Il caricamento ?? avvenuto correttamente ed il catalogo ?? stato svuotato."
            else:
                self.res["text"] = "Il caricamento ?? avvenuto correttamente, ora potrai continuare a lavorare sul catalogo."

    def handler_carica(self, evento):
        # carica un catalogo da file txt
        files = [('Documento di testo', '*.txt')]
        file = fd.askopenfilename(
            title='Carica un catalogo',
            filetypes=files)
        #print("file", file)
        if file != "":
            try:
                self.cat.load(file)
            except(FileExistsError, FileNotFoundError):
                return messagebox.showerror("Errore", "Il file non ?? presente")
            else:
                self.res["text"] = "Il caricamento ?? avvenuto correttamente."
        else:
            return messagebox.showerror("Errore", "Il file non ?? presente.")

    def handler_exit(self, evento):
        # chiude la finestra
        self.root.destroy()


# attivazione dell'interfaccia
root = tk.Tk()
Finestra(root)
# task 4: avvio del ciclo ascolto eventi
root.mainloop()
