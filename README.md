# assignment5
# Electronic Device Store

## Description
This project is a simple shopping cart system for an electronic device store, implementing Object-Oriented Programming (OOP) principles such as inheritance and encapsulation.

## Features
- View available devices (Smartphones, Laptops, Tablets)
- Add devices to the shopping cart
- Remove devices from the shopping cart
- Checkout and purchase devices
- Apply discounts to items

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/electronic-device-store.git
   ```
2. Navigate to the project directory:
   ```bash
   cd electronic-device-store
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Usage
When you run `main.py`, you will see the following menu:
```
1. Show Devices
2. Show Cart
3. Checkout
4. Exit
```
- Select `1` to view available devices and add them to the cart.
- Select `2` to see your cart and total price.
- Select `3` to proceed to checkout and finalize your purchase.
- Select `4` to exit the program.


## Sample Input/Output

### Sample Input
```
1  # Show Devices
1  # Select first device (Smartphone)
2  # Enter quantity
2  # Show Cart
3  # Checkout
```
### Sample Output
```
iPhone 13 - $999 - Stock: 10 - Warranty: 24 months - Screen: 6.1" - Battery: 20h
Added 2 iPhone 13 to cart.
iPhone 13 - Quantity: 2
Total price: $1998
Purchase successful! Total price: $1998
```

## Files Structure
```
/ electronic-device-store
   ├── devices.py  # Contains classes for devices and cart
   ├── main.py     # Runs the program and provides a menu
   ├── README.md   # Documentation
   ├── sample_input_output.txt  # Example inputs and outputs
```

## License
This project is licensed under the MIT License.
## UML Class Diagram
*Down below is the uml picture*

![uml electronic devices](https://github.com/user-attachments/assets/ebd7173a-0917-430c-a4e9-ddd6c3860d3c)
