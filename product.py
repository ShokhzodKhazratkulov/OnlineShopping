class Product:

    def __init__(self, id, name, price, description, in_stock):
        self.product_id = id
        self.name = name
        self.price = price
        self.description = description
        self.quantity_in_stock = in_stock

    def get_product_details(self):
        return (f"Product ID: {self.product_id}\nName: {self.name}\nPrice: {self.price}\nDescription: {self.description}"
                f"\nQuantity in Stock: {self.quantity_in_stock}")