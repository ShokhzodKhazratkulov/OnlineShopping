import random
from datetime import datetime

class Order:

    def __init__(self, user, product_n, prod_price,):
        self.order_id = None #random id beriladi
        self.user = user #user.pydan user malumotlarini olinadi
        self.prod_name = product_n #product classdan name and price olinadi
        self.prod_price = prod_price
        self.order_date = None    #datetime module ishlatiladi
        self.saved_id = []

    def view_order_details(self):
        """Displays order details"""
        self.order_id = random.randint(100, 999)
        today = datetime.now()
        self.order_date = today
        return (f"Order ID: {self.order_id}\nName: {self.prod_name}\nTotal price: {self.prod_price}\n"
                f"Ordered date: {self.order_date}")

    def track_order(self, order_id):
        """Track orders by entering the item order_ID"""
        if order_id in self.saved_id:
            return "Your item is on the way."
        else:
            return "The Order ID is not found"