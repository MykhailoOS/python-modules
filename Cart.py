import Logger
import logging
import Discount
import Product

class Cart(Logger.LoggingMixin):
    def __init__(self, discount: Discount.Discount = None):
        super(Cart, self).__init__()
        self.__products = []
        self.__quantities = []
        self.discount = discount

    def add_product(self, product: Product.Product, quantity: int | float = 1):
        if isinstance(product, Product.Product) and isinstance(quantity, int | float):
            self.log('Add product to Cart')
            self.__products.append(product)
            self.__quantities.append(quantity)
        else:
            self.log(f'Customer can not add {product}', logging.WARNING)

    def total(self):
        summa = sum(product.price * quantity for product, quantity in zip(self.__products, self.__quantities))
        summa = summa * self.discount.discount() if self.discount else summa
        self.log(f'Customer pay {summa}', logging.INFO)
        return summa

    def __str__(self):
        return '\n'.join(map(lambda items: f'{items[0]} x {items[1]} = {items[0].price * items[1]} UAH',
                          zip(self.__products, self.__quantities))) + f'\nTotal: {self.total():.2f} UAH\n'