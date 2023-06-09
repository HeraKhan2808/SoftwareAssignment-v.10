# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tNfYHxZZGCQrRwgpurAb9L_EQh8mUb0h
"""

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the form data
    $orderItems = $_POST['order_items'];

    // Convert the order items string to an array the Python code
    $command = pizza('python3 -c '
        . '\'from pizza import Item, Order;'
        . 'orderItemArray = [' . implode(',', array_map(function ($item) {
            return 'Item("'.trim($item).'")';
        }, $orderItemArray)) . '];'
        . 'order = Order(orderItemArray);'
        . 'total = order.calculateTotal();'
        . 'print("Total cost of the order: ${0:.2f}".format(total));\'');

    $output = shell_exec($command);
    
    // Display the output
    echo "<pre>$output</pre>";
}


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $contactNumber = $_POST['contact_number'];
    $items = $_POST['items'];

    // Convert the items string to an array
    $itemArray = explode(',', $items);

    // Include the Python code
    $command = escapeshellcmd('python3 -c '
        . '\'from pizza import Customer, Item, Order, YummyPizza;'
        . 'customer = Customer("'.$name.'", "'.$email.'", "'.$contactNumber.'");'
        . 'itemArray = [' . implode(',', array_map(function ($item) {
            return 'Item("'.trim($item).'")';
        }, $itemArray)) . '];'
        . 'order = Order(itemArray);'
        . 'yummyPizza = YummyPizza({"Pizza": 50, "Garlic Bread": 75, "Coke": 140});'
        . 'customer.placeOrder(order);'
        . 'total = order.calculateTotal();'
        . 'yummyPizza.updateInventory(order);'
        . 'print("Order placed by {0} for {1}".format(customer.name, order));'
        . 'print("Yummy Pizza Customer name {0} email id {1} contact number {2}".format(customer.name, customer.email, customer.contact_number));'
        . 'print("Total bill generated for the order: ${0:.2f}".format(total));'
        . 'print("Updated inventory after order is placed: {0}".format(yummyPizza.inventory));\'');

    $output = shell_exec($command);
    
    // Display the output
    echo "<pre>$output</pre>";
}
?>

<html>
<head>
    <title>Yummy Pizza Order</title>
    <style>
        /* Add some basic styling */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        label {
            display: block;
            margin-top: 10px;
        }

        input[type="text"] {
            width: 300px;
            padding: 5px;
        }

        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }

        .result {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Yummy Pizza Order</h1>
    
    <h2>Place Order</h2>
    <form action="place_order.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="text" id="email" name="email" required>
        
        <label for="contact_number">Contact Number:</label>
        <input type="text" id="contact_number" name="contact_number" required>
        
        <label for="items">Items (comma-separated):</label>
        <input type="text" id="items" name="items" required>
        
        <button type="submit">Place Order</button>
    </form>
    
    <h2>Calculate Total</h2>
    <form action="calculate_total.php" method="post">
        <label for="order_items">Order Items (comma-separated):</label>
        <input type="text" id="order_items" name="order_items" required>
        
        <button type="submit">Calculate Total</button>
    </form>
    
    <h2>Update Inventory</h2>
    <form action="update_inventory.php" method="post">
        <label for="inventory">Inventory (JSON format):</label>
        <input type="text" id="inventory" name="inventory" required>
        
        <label for="order_items">Order Items (comma-separated):</label>
        <input type="text" id="order_items" name="order_items" required>
        
        <button type="submit">Update Inventory</button>
    </form>

    <!-- Display the result here -->
    <div class="result">
        <?php
        if (isset($_GET['result'])) {
            echo $_GET['result'];
        }
        ?>
    </div>

    <script>
        // Add any additional JavaScript code here
    </script>
</body>
</html>


Description of the code: 

In this code, the Customer class has the placeOrder() method, which is used to place an order.
The Order class has the calculateTotal() method to calculate the total cost of the order. 
The YummyPizza class has the updateInventory() method to update the inventory based on the order.

The code creates instances of these classes and demonstrates how the methods can be called and utilized


# 3.6 To solve question 3.6 [target script: pizza_crud.py, 
    Before executing the python script, follow the steps to setup mysql locally]

1. Download the script.
2. run "pip install mysql-connector-python" and run "sudo apt-get update" followed by "sudo apt-get install mysql.connector"
3. Install mysql server if you dont have (check with "which mysql") 

    - sudo apt update
    - sudo apt install mysql-server
    - sudo systemctl start mysql.service

4. check with "sudo mysql"
5. sudo mysql -u root -p [Press Enter]
6. SELECT user,authentication_string,plugin,host FROM mysql.user;
7. ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin@1234';
8. FLUSH PRIVILEGES;
9. CREATE DATABASE customers;
10.CREATE TABLE customers (name VARCHAR(50),email VARCHAR(50),phone VARCHAR(50));
11. exit

Now you are ready to use the database.
Directly run "python3 pizza_crud.py"


SAVE, UPDATE, GET  are the operations that is implemented on "customers" class.

#3.7 - Design interface - download the index.html and open it on browser. The PHP files must be on the same path


    def __init__(self, name, email, contact_number):
        self.name = name
        self.email = email
        self.contact_number = contact_number

    def placeOrder(self, order):
        # Place the order 
        print(f"Order placed by {self.name} for {order}")

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, items):
        self.items = items

    def calculateTotal(self):
        # Code for calculating the total cost of the order
        total = 0
        for item in self.items:
            total += item.price
        return total

class YummyPizza:
    def __init__(self, inventory):
        self.inventory = inventory

    def updateInventory(self, order):
        # Code for updating the inventory based on the order
        for item in order.items:
            self.inventory[item.name] -= 1

# Create customer object of the Customer class
customer = Customer("Anubhav Jana", "anubhav.jana@example.com", "987651234")

#Instantiate items with their cost 
item1 = Item("Pizza", 260)
item2 = Item("Garlic Bread", 80)
item3 = Item("Coke", 60)

print("Menu: {} Amount: {}".format(item1.name,item1.price))
print("Menu: {} Amount: {}".format(item2.name,item2.price))
print("Menu: {} Amount: {}".format(item3.name,item3.price))

#Order the item using Order class
order = Order([item1, item2, item3])

#Instantiate inventory
yummyPizza = YummyPizza({"Pizza": 50, "Garlic Bread": 75, "Coke": 140})

print(f"Current inventory before placing order: {yummyPizza.inventory}")


#customer now places the order
customer.placeOrder(order)

#calculate order total to generate bill
total = order.calculateTotal()


# update inventory after order
yummyPizza.updateInventory(order)


#print details
print("Yummy Pizza Customer name {} email id {} contact number {}".format(customer.name,customer.email,customer.contact_number))
print(f"Total bill generated for the order: ${total:.2f}")
print(f"Updated inventory after order is placed: {yummyPizza.inventory}")


class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def save_to_database(self):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            user='root',
            password='admin@1234',
            host='localhost',
            database='customers'
        )
        cursor = db.cursor()

        # Prepare the SQL query to insert the employee data
        query = "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"
        values = (self.name, self.email, self.phone)

        try:
            # Execute the query and commit the changes
            cursor.execute(query, values)
            db.commit()
            print("Customer data saved to the database.")
        except mysql.connector.Error as error:
            # Handle any errors that occur during the execution
            db.rollback()
            print("Error occurred:", error)
        finally:
            # Close the database connection
            cursor.close()
            db.close()

    @staticmethod
    def get_all_customers():
        # Connect to the MySQL database 'customers'
        db = mysql.connector.connect(
            user='root',
            password='admin@1234',
            host='localhost',
            database='customers'
        )
        cursor = db.cursor()

        # Prepare the SQL query to retrieve all employees
        query = "SELECT * FROM customers"

        try:
            # Execute the query
            cursor.execute(query)
            results = cursor.fetchall()

            # Print the retrieved employee data
            for row in results:
                name = row[0]
                email = row[1]
                phone = row[2]
                print(f"Customer Name: {name}, Email: {email}, Phone: {phone}")
        except mysql.connector.Error as error:
            print("Error occurred:", error)
        finally:
            # Close the database connection
            cursor.close()
            db.close()

    def update_phone_number(self, new_phone):
        # Connect to the MySQL database
        db = mysql.connector.connect(
            user='root',
            password='admin@1234',
            host='localhost',
            database='customers'
        )
        cursor = db.cursor()

        # Prepare the SQL query to update the employee's salary
        query = "UPDATE customers SET phone = %s WHERE name = %s"
        values = (new_phone, self.name)

        try:
            # Execute the query and commit the changes
            cursor.execute(query, values)
            db.commit()
            print("Customer phone updated.")
        except mysql.connector.Error as error:
            # Handle any errors that occur during the execution
            db.rollback()
            print("Error occurred:", error)
        finally:
            # Close the database connection
            cursor.close()
            db.close()


# Example usage
customer1 = Customer("Anubhav Jana", "abc@gmail.com", "123456")
customer1.save_to_database()

customer2 = Customer("Tutpor Point", "tutor@gmail.com", "678901")
customer2.save_to_database()

Customer.get_all_customers()

customer1.update_phone_number("123445")

print("Fetching Updated Customer Information\n")

Customer.get_all_customers()



if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the form data
    $inventoryJSON = $_POST['inventory'];
    $orderItems = $_POST['order_items'];

    // Convert the inventory JSON to an associative array
    $inventory = json_decode($inventoryJSON, true);

    // Convert the order items string to an array
    $orderItemArray = explode(',', $orderItems);

    // Include the Python code
    $command = escapeshellcmd('python3 -c '
        . '\'from pizza import Item, Order, YummyPizza;'
        . 'inventory = ' . $inventoryJSON . ';'
        . 'orderItemArray = [' . implode(',', array_map(function ($item) {
            return 'Item("'.trim($item).'")';
        }, $orderItemArray)) . '];'
        . 'order = Order(orderItemArray);'
        . 'yummyPizza = YummyPizza(inventory);'
        . 'yummyPizza.updateInventory(order);'
        . 'print("Updated inventory: {0}".format(yummyPizza.inventory));\'');

    $output = shell_exec($command);
    
    // Display the output
    echo "<pre>$output</pre>";
}
?>

