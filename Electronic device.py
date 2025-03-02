class Device:
    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period
    
    def display_info(self):
        return f"{self.name} - ${self.price} | Stock: {self.stock} | Warranty: {self.warranty_period} months"
    
    def __str__(self):
        return self.display_info()
    
    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)
    
    def is_available(self, amount):
        return self.stock >= amount
    
    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
            return True
        return False

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life
    
    def __str__(self):
        return f"{super().__str__()} | Screen: {self.screen_size} inches | Battery: {self.battery_life} hrs"
    
    def make_call(self):
        return f"Making a call from {self.name}"
    
    def install_app(self):
        return f"Installing an app on {self.name}"

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed
    
    def __str__(self):
        return f"{super().__str__()} | RAM: {self.ram_size}GB | CPU: {self.processor_speed}GHz"
    
    def run_program(self):
        return f"Running a program on {self.name}"
    
    def use_keyboard(self):
        return f"Typing on {self.name}"

class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight
    
    def __str__(self):
        return f"{super().__str__()} | Resolution: {self.screen_resolution} | Weight: {self.weight}g"
    
    def browse_internet(self):
        return f"Browsing internet on {self.name}"
    
    def use_touchscreen(self):
        return f"Using touchscreen on {self.name}"

class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0
    
    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
        else:
            print(f"Not enough stock for {device.name}")
    
    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device and item[1] >= amount:
                self.items.remove(item)
                self.total_price -= device.price * amount
                device.stock += amount
                break
    
    def print_items(self):
        if not self.items:
            print("Cart is empty.")
        for item in self.items:
            print(f"{item[0].name} x {item[1]}")
    
    def checkout(self):
        print("Checkout successful! Total price: $", self.total_price)
        self.items = []
        self.total_price = 0

devices = [
    Smartphone("iPhone 13", 999, 10, 24, 6.1, 20),
    Laptop("MacBook Pro", 1999, 5, 36, 16, 3.2),
    Tablet("iPad Air", 699, 8, 12, "2360x1640", 460)
]

cart = Cart()
while True:
    print("\n1. Show Devices\n2. Show Cart\n3. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        for index, device in enumerate(devices):
            print(f"{index+1}. {device}")
        selection = int(input("Select a device to add to cart (0 to cancel): ")) - 1
        if 0 <= selection < len(devices):
            quantity = int(input("Enter quantity: "))
            cart.add_device(devices[selection], quantity)
    
    elif choice == "2":
        cart.print_items()
    
    elif choice == "3":
        break
