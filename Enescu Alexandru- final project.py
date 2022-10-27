# Enescu Alexandru
# Final project - Products catalogue


class Catalogue:
    '''Parent class for Large Appliances and Small Appliances'''
    classes = list()
    subclasses = list()
    product_list = list()

    def __init__(self, price, consumption, manufacturer, product_code, clasa, subclass):

        Catalogue.product_list.append(self)
        Catalogue.classes.append(clasa, )
        Catalogue.subclasses.append(subclass, )
        self.price = price
        self.consumption = consumption
        self.manufacturer = manufacturer
        self.product_code = product_code

    def sorts(obj, price=False, consumption=False):
        '''The function sorts by price or consumption'''
        dictionary_products = dict()
        for product, tuplu in zip(Catalogue.product_list, zip(Catalogue.classes, Catalogue.subclasses)):
            dictionary_products.update({product: tuplu})

        if consumption:
            print('\nSorting by consumption:')
            for obiect in sorted(dictionary_products.keys(), key=lambda obj: obj.consumption):
                obj.print_product(
                    obiect, dictionary_products[obiect][0], dictionary_products[obiect][1])
        elif price:
            print('\nSorting by price:')
            for obiect in sorted(dictionary_products.keys(), key=lambda obj: obj.price):
                obj.print_product(
                    obiect, dictionary_products[obiect][0], dictionary_products[obiect][1])

    def get_products_for_manufacturer(self, manufacturer):
        '''It finds us according to the name of the manufacturer'''
        products_found = []
        dictionary_products = dict()
        for product, tuplu in zip(Catalogue.product_list, zip(Catalogue.classes, Catalogue.subclasses)):
            dictionary_products.update({product: tuplu})
        found = False
        for product in Catalogue.product_list:
            if product.manufacturer.upper() == manufacturer.upper().strip():
                found = True
                tuplu = dictionary_products[product]
                products_found.append([product, tuplu[0], tuplu[1]])
        if found:
            print('\nProducts for manufacturer', manufacturer)
            for lista in products_found:
                self.print_product(
                    product=lista[0], clasa=lista[1], subclass=lista[2])
        else:
            print('The manufacturer is not in the list')

    def get_products_for_subclass(self, subclass):
        '''Show products from subclasses'''
        products_found = []
        dictionary_products = dict()
        for product, tuplu in zip(Catalogue.product_list, zip(Catalogue.classes, Catalogue.subclasses)):
            dictionary_products.update({product: tuplu})
        found = False
        for product, tuplu in dictionary_products.items():
            if tuplu[1].upper() == subclass.upper().strip():
                found = True
                products_found.append([product, tuplu[0], tuplu[1]])
        if found:
            print('\nProducts for the subclass', subclass)
            for lista in products_found:
                self.print_product(lista[0], lista[1], lista[2])
        else:
            print('There are no products in this subclass')

    def print_product(self, product, clasa, subclass):
        '''It prints according to what is asked of it'''
        print('clasa:', clasa, 'sublclasa:', subclass, "price:",
              product.price, "=>consumption:", product.consumption, "manufacturer", product.manufacturer, 'product code:',
              product.product_code)


class Large_appliances(Catalogue):
    def __init__(self, price, consumption, manufacturer, product_code, depth, width, height, subclass):
        super().__init__(price, consumption, manufacturer,
                         product_code, 'Large_appliance', subclass)
        self.depth = depth
        self.width = width
        self.height = height


class Small_appliances(Catalogue):
    def __init__(self, price, consumption, manufacturer, productc_cod, cable_length, battery, subclass):
        super().__init__(price, consumption, manufacturer, productc_cod,
                         clasa='Small appliances', subclass=subclass)
        self.cable_length = cable_length
        self.battery = battery


class Refrigerator(Large_appliances):
    def __init__(self, price, consumption, manufacturer, product_cod, depth, width, height, refrigerator_capacity,
                 freezer_capacity):
        super().__init__(price, consumption, manufacturer, product_cod,
                         depth, width, height, subclass='Refrigerator')
        self.refrigerator_capacityr = refrigerator_capacity
        self.freezer_capacity = freezer_capacity


class Gas_cooker(Large_appliances):
    def __init__(self, price, consumption, manufacturer, product_cod, depth, width, height, nr_burners):
        super().__init__(price, consumption, manufacturer,
                         product_cod, depth, width, height, 'Gas_cooker')
        self.nr_burners = nr_burners


class Mixer(Small_appliances):
    def __init__(self, price, consumption, manufacturer, product_cod, cable_length, batery, min_rotations):
        super().__init__(price, consumption, manufacturer,
                         product_cod, cable_length, batery, 'Mixer')
        self.min_rotations = min_rotations


class Iron(Small_appliances):
    def __init__(self, price, consumption, manufacturer, product_cod, cable_length, batery, rezervoir):
        super().__init__(price, consumption, manufacturer,
                         product_cod, cable_length, batery, 'Iron')
        self.rezervoir = rezervoir


def main():
    '''This is where I created the objects'''
    refrigerator = Refrigerator(1200, 50, 'Arctic', 123, 70, 50, 150, 250, 50)
    Refrigerator(600, 80, 'Samsung', 123, 70, 50, 150, 250, 50)
    Gas_cooker(800, 100, 'Zanussi', 345, 50, 60, 120, 4)
    Mixer(200, 170, 'Zanussi', 566, 30, 100, 300)
    Gas_cooker(800, 800, 'Indesit', 432, 30, 50, 80, 6)
    Mixer(300, 80, 'Bosh', 674, 2, 150, 1000)
    Iron(500, 200, 'Tefal', 985, 3, 200, 2)
    Iron(600, 250, 'Phillips', 386, 4, 150, 3)

    print('\nProduct catalog')
    while True:
        print('\nSelect an option:')
        print('1 - Display by price', '\n2 - Sort by consumption''\n3 - Display by manufacturer',
              '\n4 - Display by subclass', '\n5 - Exit\n')
        optiune = input().strip()
        if optiune not in ['1', '2', '3', '4', '5']:
            print('Va rugam introduceti 1,2 3, 4, sau 5!')

        elif optiune == '1':
            refrigerator.sorts(price=True)
        elif optiune == '2':
            refrigerator.sorts(consumption=True)
        elif optiune == '3':
            manufacturer = input('Enter the name of the manufacturer: ')
            refrigerator.get_products_for_manufacturer(
                manufacturer=manufacturer)
        elif optiune == '4':
            subclass = input('Enter the name of subclass: ')
            refrigerator.get_products_for_subclass(subclass)
        else:
            return


if __name__ == '__main__':
    main()
