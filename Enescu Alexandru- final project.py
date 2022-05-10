#Enescu Alexandru
#Proiect final catalog produse


class Catalog:
    '''Clasa parinte pentru Electrocasnice mari si Electrocasnice mici'''
    clase = list()
    subclase = list()
    lista_produse = list()

    def __init__(self, pret, consum, producator, cod_produs, clasa, subclasa):
        ''''''
        Catalog.lista_produse.append(self)
        Catalog.clase.append(clasa, )
        Catalog.subclase.append(subclasa, )
        self.pret = pret
        self.consum = consum
        self.producator = producator
        self.cod_produs = cod_produs

    def sorteaza(obj, pret=False, consum=False):
        '''Functia sorteaza dupa pret sau consum'''
        dictionar_produse = dict()
        for produs, tuplu in zip(Catalog.lista_produse, zip(Catalog.clase, Catalog.subclase)):
            dictionar_produse.update({produs: tuplu})

        if consum:
            print('\nSortare dupa consum:')
            for obiect in sorted(dictionar_produse.keys(), key=lambda obj: obj.consum):
                obj.print_produs(obiect, dictionar_produse[obiect][0], dictionar_produse[obiect][1])
        elif pret:
            print('\nSortare dupa pret:')
            for obiect in sorted(dictionar_produse.keys(), key=lambda obj: obj.pret):
                obj.print_produs(obiect, dictionar_produse[obiect][0], dictionar_produse[obiect][1])

    def get_products_for_producator(self, producator):
        '''Ne gaseste in functie de numele producatorului'''
        produse_gasite = []
        dictionar_produse = dict()
        for produs, tuplu in zip(Catalog.lista_produse, zip(Catalog.clase, Catalog.subclase)):
            dictionar_produse.update({produs: tuplu})
        gasit = False
        for produs in Catalog.lista_produse:
            if produs.producator.upper() == producator.upper().strip():
                gasit = True
                tuplu = dictionar_produse[produs]
                produse_gasite.append([produs, tuplu[0], tuplu[1]])
        if gasit:
            print('\nProduse pentru producatorul', producator)
            for lista in produse_gasite:
                self.print_produs(produs=lista[0], clasa=lista[1], subclasa=lista[2])
        else:
            print('Producatorul nu este in lista')

    def get_products_for_subclasa(self, subclasa):
        '''Afiseaza produsele din subclase'''
        produse_gasite = []
        dictionar_produse = dict()
        for produs, tuplu in zip(Catalog.lista_produse, zip(Catalog.clase, Catalog.subclase)):
            dictionar_produse.update({produs: tuplu})
        gasit = False
        for produs, tuplu in dictionar_produse.items():
            if tuplu[1].upper() == subclasa.upper().strip():
                gasit = True
                produse_gasite.append([produs, tuplu[0], tuplu[1]])
        if gasit:
            print('\nProduse pentru subclasa', subclasa)
            for lista in produse_gasite:
                self.print_produs(lista[0], lista[1],lista[2])
        else:
            print('Nu exista produse din aceasta subclasa')

    def print_produs(self, produs, clasa, subclasa):
        '''Printeaza in functie de ce i se cere'''
        print('clasa:', clasa, 'sublclasa:', subclasa, "pret:",
              produs.pret, "=>consum:", produs.consum, "producator", produs.producator, 'cod produs:',
              produs.cod_produs)


class Electrocasnice_mari(Catalog):
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, subclasa):
        super().__init__(pret, consum, producator, cod_produs, 'Electrocasnice mari', subclasa)
        self.adancime = adancime
        self.latime = latime
        self.inaltime = inaltime


class Electrocasnice_mici(Catalog):
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, subclasa):
        super().__init__(pret, consum, producator, cod_produs, clasa='Electrocasnice mici', subclasa=subclasa)
        self.lungime_cablu = lungime_cablu
        self.baterie = baterie


class Frigider(Electrocasnice_mari):
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, capacitate_frigider,
                 capacitate_congelator):
        super().__init__(pret, consum, producator, cod_produs, adancime, latime, inaltime, subclasa='frigider')
        self.capacitate_frigider = capacitate_frigider
        self.capacitate_congelator = capacitate_congelator


class Aragaz(Electrocasnice_mari):
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, nr_arzatoare):
        super().__init__(pret, consum, producator, cod_produs, adancime, latime, inaltime, 'aragaz')
        self.nr_arzatoare = nr_arzatoare


class Mixer(Electrocasnice_mici):
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, rotatii_min):
        super().__init__(pret, consum, producator, cod_produs, lungime_cablu, baterie, 'Mixer')
        self.rotatii_min = rotatii_min


class Fier_calcat(Electrocasnice_mici):
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, rezervor):
        super().__init__(pret, consum, producator, cod_produs, lungime_cablu, baterie, 'Fier calcat')
        self.rezervor = rezervor


def main():
    '''Aici am creat obiectele'''
    frigider = Frigider(1200, 50, 'Arctic', 123, 70, 50, 150, 250, 50)
    Frigider(600, 80, 'Samsung', 123, 70, 50, 150, 250, 50)
    Aragaz(800, 100, 'Zanussi', 345, 50, 60, 120, 4)
    Mixer(200, 170, 'Zanussi', 566, 30, 100, 300)
    Aragaz(800, 800, 'Indesit', 432, 30, 50, 80, 6)
    Mixer(300, 80, 'Bosh', 674, 2, 150,1000)
    Fier_calcat(500, 200, 'Tefal', 985, 3, 200, 2)
    Fier_calcat(600, 250, 'Phillips', 386, 4, 150, 3)

    print('\nCatalog produse')
    while True:
        print('\nSelectati o optiune:')
        print('1 - Afiseaza dupa pret', '\n2 - Sorteaza dupa consum''\n3 - Afiseaza dupa producator',
              '\n4 - Afiseaza dupa subclasa', '\n5 - Exit\n')
        optiune = input().strip()
        if optiune not in ['1', '2', '3', '4', '5']:
            print('Va rugam introduceti 1,2 3, 4, sau 5!')

        elif optiune == '1':
            frigider.sorteaza(pret=True)
        elif optiune == '2':
            frigider.sorteaza(consum=True)
        elif optiune == '3':
            producator = input('Introduceti numele producatorului: ')
            frigider.get_products_for_producator(producator=producator)
        elif optiune == '4':
            subclasa = input('Introduceti numele subclasei: ')
            frigider.get_products_for_subclasa(subclasa)
        else:
            return


if __name__ == '__main__':
    main()
