from fakturoid import Fakturoid

fa = Fakturoid(slug='mergadobackend1', email='peter.smatana@mergado.com',
               api_key='bd5a4ef76c536c15c7a2ed835af4e78f7397fb08',
               )


#   NEJSEM UCETNI, TAGZE TO TU POJMENOVAVAM SVYM JAZYKEM


def account(fa):
    """Toto mi vypise Mergado Backend tedy
     firmu na kterou je fakturoid zalozeny.
    """
    print fa.account()

# account(fa)


def subject(fa):
    """i dont know why?
     AttributeError: 'Fakturoid' object has no attribute 'subject_id'

     pritom toto id existuje, viz metoda subjects()
    """
    print fa.subject_id(2023409)

# subject(fa)


def subjects(fa):
    """todle mi vraci list subjektu na ktery mam
     danou fakturu
    """
    for subject in fa.subjects(since=None):
        print 'subject = ', subject, ' id = ', subject.id
        print dir(subject)

# subjects(fa)


def invoices(fa):
    """seznam faktur, v tomto pripade vsechny. jinak
    se ostatni veci daji specifikovat v argumentu
    fa.invoices(...)
    """
    for invoice in fa.invoices():
        print 'faktura = ', invoice

invoices(fa)
