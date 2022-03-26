class Item:
    # pay rate after 20% discount
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >=0, f"price {price} is not greater than or equal to zero"
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero" 

        # Assigning to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item('Phone', 100, 1)
item1.apply_discount()
print(item1.calculate_total_price())
print(item1.price)








