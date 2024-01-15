from order import Order
class User():

    def __init__(self, id, name):
        self.user_id = id
        self.user_name = name
        self.address = None
        self.gmail = None
        self.user_list = []
        self.check_user()

    def check_user(self):
        if self.user_id and self.user_name not in self.user_list:
            self.user_list.append(self.user_id)
            self.user_list.append(self.user_name)
        else:
            print(f"{self.user_id} or {self.user_name} is already exist.")

    def view_user_profile(self):
        """Displays User profile"""
        print(f"Costumer ID: {self.user_id}\nCostumer name: {self.user_name}\nAddress: {self.address}\n"
              f"Gmail: {self.gmail}")

    def place_order(self, product_name, product_price):
        """Places an order for a product"""
        if self.address and self.gmail:
            order = Order(user=self, product_n=product_name, prod_price=product_price)
            return order.view_order_details()
        else:
            return "Please provide your address and Gmail before placing an order."