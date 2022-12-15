class Libro:
    def __init__(self,cognome,nome,titolo,anno,collocazione,iban,note=""):
        if type(cognome) != str or type(nome) != str or type(titolo) != str or type(iban) != str or type(note) != str:
            raise TypeError("Parametri errati")
        if type(anno) != int:
            raise TypeError("Parametri errati")
        if type(collocazione) != tuple or type(collocazione[0]) != str or type (collocazione[1]) != int:
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
        #pass #instruzione che non fa niente --> da sostituire con il codice


    def __str__ (self):
        libro = [self.cognome, self.nome, self.titolo, self.anno, self.coll, self.iban, self.note]
        
        return str(libro)
        """ Serializza un libro rappresentandolo come una stringa. La stringa
        puo' usare un formato a scelta dello studente
        :return: una stringa che rappresenta il libro
        """
        pass #istruzione che non fa niente --> da sostituire con il codice

    def __eq__(self,a):
        uguali = True
        try:
            if self.cognome != a.cognome or self.nome!=a.nome or self.titolo!=a.titolo or self.anno!=a.anno or self.iban!=a.iban:
                uguali = False
        except AttributeError:
            print("Il termine non è un oggetto Libro")
        else:
            return uguali
        """ stabilisce se self e a sono uguali -- due libri sono cosiderati uguali
            se hanno esattamente gli stessi campi (eccetto le note e la collocazione)  """

        pass #instruzione che non fa niente --> da sostituire con il codice


class Catalogo:
    def __init__(self):
        """Crea un catalogo vuoto rappresentato come un dizionario di
           libri con chiave iban"""
        pass #instruzione che non fa niente --> da sostituire con il codice


    def n_books(self):
        """Ritorna il numero di libri nel catalogo """
        pass #instruzione che non fa niente --> da sostituire con il codice


    def inserisci(self,li):
        """Inserisce un nuovo libro nel catalogo:
            se l'iban è già presente non modifica il catalogo
            :param: li oggetto libro da inserire
            :returns: True se il libro è stato inserito
            :returns: False altrimenti """
        pass #instruzione che non fa niente --> da sostituire con il codice


    def __str__(self):
        """Serializza il catalogo in una stringa che contiene tutti i libri
        in ordine di IBAN crescente.
        Ogni libro è separato dal successivo da "\n" """
        pass #instruzione che non fa niente --> da sostituire con il codice


    def store(self,nomefile):
        """Scrive il catalogo sul file "nomefile" -- > formato a scelta dello studente
         da specificare nei commenti"""
        pass #instruzione che non fa niente --> da sostituire con il codice


    def load(self,nomefile):
        """Legge il catalogo dal file "nomefile" nel formato a scelta dello studente
        e lo carica nel catalogo eliminando tutto il contenuto precedente
        del catalogo """
        pass #instruzione che non fa niente --> da sostituire con il codice


    def __eq__(self,cat2):
        """stabilisce se due cataloghi contengono
        esattamente gli stessi libri
        :param cat2: secondo catalogo da confrontare
        :return: True se sono uguali, False altrimenti
        """
        pass  # istruzione che non fa niente --> da sostituire con il codice

