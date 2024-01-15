from products_data import products
from product import Product
from cart import Cart
from user import User
from order import Order

cart = Cart(products)
products_list = [Product(item["product_id"], item["name"], item["price"],
                   item["description"], item["quantity_in_stock"]) for item in products]
print("Available products:")
for prod in products:
    print(prod['name'])

def display_menu():
    print("\nOnline Shopping Menu:")
    print("1. View Available Products")
    print("2. Log In")
    print("3. View user profile")
    print("4. Order a Products")
    print("5. Add to cart")
    print("6. Remove from cart")
    print("7. View items in cart list")
    print("8. Exit")


def run():

    current_user = None
    while True:

        display_menu()
        user_choice = input("Choose number what you want to do! ")
        if user_choice == "1":
            print("Here is products below")
            for prod in products_list:
                print(prod.get_product_details())
                print("")

        elif user_choice == "2":
            user_id = int(input("Enter your ID: "))
            user_name = input("Enter your name: ")
            current_user = User(user_id, user_name)

        elif user_choice == "3":
            if current_user:
                current_user.view_user_profile()
            else:
                print("Log In first!")

        elif user_choice == "4":
            if current_user:
                # Allow the user to select a product to order
                product_index = int(input("Enter the product index to order: "))
                selected_product = products_list[product_index - 1]
                order = Order(current_user, selected_product.name, selected_product.price)
                order_details = order.view_order_details()
                print(order_details)
            else:
                print("Please log in first.")

        elif user_choice == "5":
            product_name = input("Enter product name to add to cart: ")
            # Find the product instance based on the name
            selected_product = next((prod for prod in products_list if prod.name == product_name), None)
            if selected_product:
                cart.add_items(selected_product)
            else:
                print("Product not found.")

        elif user_choice == "6":
            product_name_to_remove = input("Enter product name to remove from cart: ")
            # Find the product instance based on the name
            product_to_remove = next((prod for prod in products_list if prod.name == product_name_to_remove), None)
            if product_to_remove:
                cart.remove_item(product_to_remove)
            else:
                print("Product not found in cart.")

        elif user_choice == "7":
            cart.view_items_in_cart()
            cart.calculate_total_price()

        elif user_choice == "8":
            print("Good bye! ")
            break

run()










