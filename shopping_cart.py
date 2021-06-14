class ShoppingCart:
    # write your code here
    def __init__(self, total = 0, employee_discount=None, items = []):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
    def add_item(self, name, price, quantity=1):
        for i in range(quantity):
            self.items.append(price)
        self.total+=(price*quantity)
        return self.total
    def mean_item_price(self):
        return sum(self.items)/len(self.items)

    def median_item_price(self):
        if len(self.items)%2==0:
            median = (self.items[((len(self.items)/2)+1)] + self.items[((len(self.items)/2)-1)])/2
        else:
            median = self.items[int((len(self.items)/2)+0.5)]
        return median

    def apply_discount(self):
        if self.employee_discount == None:
            print("Sorry, there is no discount to apply to your cart :(")
        else:
            self.total = self.total*(100-self.employee_discount)/100
            return self.total

    def void_last_item(self):
        self.total-=self.items[-1]
        self.items.pop()
        return self.total