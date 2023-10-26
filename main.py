import Discount
import Logger
import logging
import Product
import Cart


class RegularDiscount(Discount.Discount):
    def discount(self):
        return 0.9


class SilverDiscount(Discount.Discount):
    def discount(self):
        return 0.85


class GoldDiscount(Discount.Discount):
    def discount(self):
        return 0.8



pr_1 = Product.Product('banana', 50)
pr_2 = Product.Product('apple', 51)
pr_3 = Product.Product('orange', 52)


cart_1 = Cart.Cart()
cart_2 = Cart.Cart(SilverDiscount())


cart_1.add_product(pr_1)
cart_1.add_product('keyboard')
cart_1.add_product(pr_2)
cart_1.add_product(pr_3)

cart_2.add_product(pr_1, 5)

print(cart_1)
print(cart_2)
