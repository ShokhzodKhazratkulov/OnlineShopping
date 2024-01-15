from product import Product

class Cart:

    def __init__(self, all_prods):
        self.cart_list = []
        self.all_products = all_prods

    def add_items(self, item_name):
        """Adds items to the cart"""
        # Check if the item is available in the product list
        item_found = next((prod for prod in self.all_products if prod['name'] == item_name.name), None)
        if item_found:
            self.cart_list.append(item_found)  # Assuming item_found is a Product instance
            print(f"{item_name.name} has been successfully added to the cart!")
        else:
            print(f"{item_name.name} is not available in the product list.")

    def remove_item(self, item_name):
        """Removes items from cart"""
        # Check if the item is in the cart
        item_to_remove = next((prod for prod in self.cart_list if prod['name'] == item_name.name), None)
        if item_to_remove:
            self.cart_list.remove(item_to_remove)
            print(f"{item_name.name} has been successfully removed from the cart!")
        else:
            print(f"{item_name.name} isn't in the cart.")

    def view_items_in_cart(self):
        """Displays all items in the cart"""

        for item in self.cart_list:
            print(
                f"Product ID: {item["product_id"]}\nName: "
                f"{item["name"]}\nPrice: {item["price"]}\nDescription: "
                f"{item["description"]}")


    def calculate_total_price(self):
        """Calculates total price of products in the cart"""
        total_price = 0 #sum(item.price for item in self.cart_list)
        for each_item in self.cart_list:
            total_price += each_item["price"]
        print(f"Total price: {total_price}")


