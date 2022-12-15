class Libro:
    def __init__(self,cognome,nome,titolo,anno,collocazione,iban,note=""):
        """ Crea un nuovo oggetto Libro
        :param cognome: cognome dell'autore
        :param nome: nome dell'autore
        :param titolo: titolo del libro
        :param anno: anno di pubblicazione
        :param collocazione: tupla (stringa,intero positivo)
        :param iban: IBAN (stringa) unico per ogni libro
        :param note: stringa eventualmente vuota
        """
         pass #instruzione che non fa niente --> da sostituire con il codice


    def __str__ (self):
        """ Serializza un libro rappresentandolo come una stringa. La stringa
        puo' usare un formato a scelta dello studente
        :return: una stringa che rappresenta il libro
        """
        pass #istruzione che non fa niente --> da sostituire con il codice



    def __eq__(self,a):
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

