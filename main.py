from devices import Smartphone, Laptop, Tablet, Cart

def main():
    devices = [
        Smartphone("iPhone 13", 999, 10, 24, 6.1, 20),
        Laptop("MacBook Pro", 1999, 5, 36, 16, 3.2),
        Tablet("iPad Air", 699, 7, 12, "2048x1536", 460)
    ]

    cart = Cart()
    
    while True:
        print("\n1. Show Devices\n2. Show Cart\n3. Checkout\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            for i, device in enumerate(devices, start=1):
                print(f"{i}. {device}")
            device_choice = int(input("Select a device to add to cart: ")) - 1
            amount = int(input("Enter quantity: "))
            print(cart.add_device(devices[device_choice], amount))

        elif choice == "2":
            cart.print_items()
            print(cart.get_total_price())

        elif choice == "3":
            print(cart.checkout())

        elif choice == "4":
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
