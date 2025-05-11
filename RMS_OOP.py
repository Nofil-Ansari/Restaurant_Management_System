import random as rd
class RestaruantManagementSystem:
    def __init__(self,name,contact_num):
        self.name = name
        self.contact_num = contact_num
        self.employees = [] # One to many relationship of Restaurant with Employees
        self.customers = [] # One to many relationship of Restaurant with Customers
        self.tables = [] # One to many relationship of Restaurant with Tables
        self.reservations = [] # One to many relationship of Restaurant with Reservations
        
        pass
class Employees(RestaruantManagementSystem):
    def __init__(self, employeeID, name, age, salary,Contact_num,hire_date):
        super().__init__(name,Contact_num)
        self.employeeID = employeeID
        self.name = name       
        self.age = age
        self.salary = salary
        self.Contact_num = Contact_num
        self.hire_date = hire_date
        self.__validate_age()
        self.__validate_contact_num()
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    def __repr__(self):
        return f"Employees({self.name!r}, {self.age!r}, {self.salary!r})"
    def __validate_age(self):
        if self.age < 18 or self.age > 60:
            raise ValueError(f"Invalid age: {self.age}. Age must be between 18 and 60.")
    def __validate_contact_num(self):
        if len(str(self.Contact_num)) != 11:
            raise ValueError(f"Invalid contact number: {self.Contact_num}. Contact number must be 11 digits long.")
class Customer():
    def __init__(self,customerID,name,contact_num,email):
        self.customerID = customerID
        self.name = name
        self.contact_num = contact_num
        self.email = email
        self.__validate_contact_num()
        self.reservations = [] #One to many relationship of Customers with Reservations
    def __str__(self):
        return f"Customer ID: {self.customerID}, Name: {self.name}, Contact Number: {self.contact_num}, Email: {self.email}"
    def __repr__(self): 
        return f"Customer({self.customerID!r}, {self.name!r}, {self.contact_num!r}, {self.email!r})"
    def __validate_contact_num(self):
        if len(str(self.contact_num)) != 11:
            raise ValueError(f"Invalid contact number: {self.contact_num}. Contact number must be 11 digits long.")
class Tables:
    def __init__(self,tableID,table_num,capacity,status):
        self.tableID = tableID
        self.table_num = table_num
        self.capacity = capacity
        self.status = status
    def is_available(self):
        return self.status == "Available"
    def __str__(self):
        return f"Table ID: {self.tableID}, Table Number: {self.table_num}, Capacity: {self.capacity}, Status: {self.status}"
    def __repr__(self):
        return f"Tables({self.tableID!r}, {self.table_num!r}, {self.capacity!r}, {self.status!r})"
class Reservations:
    def __init__(self,ReservationID,customerID,tableID,reservation_date,status):
        self.ReservationID = ReservationID
        self.customerID = customerID
        self.tableID = tableID
        self.reservation_date = reservation_date
        self.status = status
    def __str__(self):
        return f"Reservation ID: {self.ReservationID}, Customer ID: {self.customerID}, Table ID: {self.tableID}, Reservation Date: {self.reservation_date}, Status: {self.status}"
    def __repr__(self):
        return f"Reservations({self.ReservationID!r}, {self.customerID!r}, {self.tableID!r}, {self.reservation_date!r}, {self.status!r})"
class Menu:
    def __init__(self,menuID,menu_item_name,price,availability=True):
        self.availability = availability
        self.menuID = menuID
        self.menu_item_name = menu_item_name
        self.price = price
    def __str__(self):
        return f"Menu ID: {self.menuID}, Menu Item: {self.menu_item}, Price: {self.price}"
    def __repr__(self):
        return f"Menu({self.menuID!r}, {self.menu_item!r}, {self.price!r})"
class Orders:
    def __init__(self,orderID,customerID,tableID,menuID,order_date,total_amount,status):
        self.orderID = orderID
        self.customerID = customerID
        self.tableID = tableID
        self.menuID = menuID
        self.order_date = order_date
        self.total_amount = total_amount
        self.status = status
        self.order_details = [] #One to many relationship of Orders with Order Details
        self.payment = None  # One-to-one relationship with Payment
    def add_order_detail(self, order_detail):
        self.order_details.append(order_detail)

    def add_payment(self, payment):
        self.payment = payment
    def __str__(self):
        return f"Order ID: {self.orderID}, Customer ID: {self.customerID}, Table ID: {self.tableID}, Menu ID: {self.menuID}, Order Date: {self.order_date}, Total Amount: {self.total_amount}, Status: {self.status}"
    def __repr__(self):
        return f"Orders({self.orderID!r}, {self.customerID!r}, {self.tableID!r}, {self.menuID!r}, {self.order_date!r}, {self.total_amount!r}, {self.status!r})"
class Payment:
    #Payment ID, Order ID, Payment Type, Amount Paid, Payment Date.
    def __init__(self,paymentID,orderID,payment_type,amount_paid,payment_date):
        self.paymentID = paymentID
        self.orderID = orderID
        self.payment_type = payment_type
        self.amount_paid = amount_paid
        self.payment_date = payment_date
    def __str__(self):
        return f"Payment ID: {self.paymentID}, Order ID: {self.orderID}, Payment Type: {self.payment_type}, Amount Paid: {self.amount_paid}, Payment Date: {self.payment_date}"
    def __repr__(self):
        return f"Payment({self.paymentID!r}, {self.orderID!r}, {self.payment_type!r}, {self.amount_paid!r}, {self.payment_date!r})"
class OrderDetails:
    def __init__(self,Order_Detail_ID, Order_ID, Item_ID, Quantity, Price ):
        self.Order_Detail_ID = Order_Detail_ID
        self.Order_ID = Order_ID
        self.Item_ID = Item_ID
        self.Quantity = Quantity
        self.Price = Price
    def __str__(self):
        return f"Order Detail ID: {self.Order_Detail_ID}, Order ID: {self.Order_ID}, Item ID: {self.Item_ID}, Quantity: {self.Quantity}, Price: {self.Price}"
    def __repr__(self):
        return f"OrderDetails({self.Order_Detail_ID!r}, {self.Order_ID!r}, {self.Item_ID!r}, {self.Quantity!r}, {self.Price!r})"




# Creating a Customer
def customer_procedure():
    input_customerID = f'24K- {str(rd.randint(1000, 6000))}'
    input_name = input("Enter Customer Name: ")
    input_contact_num = '03'+''.join(rd.choice('0123456789') for _ in range(9))

    input_email = f'k24{rd.randint(1000, 6000)}@nu.edu.pk'
    customer = Customer(customerID=input_customerID, name=input_name, contact_num=input_contact_num, email=input_email)
    #print(f'Customer created: {customer}')
    return customer

customer1 = customer_procedure()    

# Creating Tables
def table_procedure():
    input_tableID = rd.randint(1, 100)
    input_table_num = rd.randint(1, 7)
    input_capacity = rd.randint(1,4)
    input_status = rd.choice(["Available", "Reserved"])
    table = Tables(tableID=input_tableID, table_num=input_table_num, capacity=input_capacity, status=input_status)
    return table
#creating table objects
table1 = table_procedure()

# Creating Reservations
def reservation_procedure():
    input_reservationID = rd.randint(1, 1000)
    input_customerID = customer1.customerID
    input_tableID = table1.tableID
    input_reservation_date = f"2025-{rd.randint(1,12)}-{rd.randint(1,31)}"
    input_status = f"Enter Reservation Status {rd.choice(["Available", "Reserved"])}: "
    reservation = Reservations(ReservationID=input_reservationID, customerID=input_customerID, tableID=input_tableID, reservation_date=input_reservation_date, status=input_status)
    return reservation
reservation1 = reservation_procedure()
#customer1.add_reservation(reservation1)

# Creating Menu Items
menu_item1 = Menu(menuID=1, menu_item_name="Pasta", price=12.99)
menu_item2 = Menu(menuID=2, menu_item_name="Pizza", price=15.99)

# Creating an Order
order1 = Orders(orderID=1, customerID=customer1.customerID, tableID=table1.tableID, menuID=menu_item1.menuID, order_date="2025-05-04", total_amount=25.98, status="Completed")

# Adding Order Details
order_detail1 = OrderDetails(Order_Detail_ID=1, Order_ID=order1.orderID, Item_ID=menu_item1.menuID, Quantity=1, Price=12.99)
order_detail2 = OrderDetails(Order_Detail_ID=2, Order_ID=order1.orderID, Item_ID=menu_item2.menuID, Quantity=1, Price=15.99)
order1.add_order_detail(order_detail1)
order1.add_order_detail(order_detail2)

# Creating a Payment
payment1 = Payment(paymentID=1, orderID=order1.orderID, payment_type="Credit Card", amount_paid=25.98, payment_date="2025-05-04")
order1.add_payment(payment1)


# Printing the objects to verify relationships using __str__ and __repr__
#print(str(customer1))
#print(str(customer1.reservations))
#print(str(order1))
#print(str(order1.order_details))
#print(str(order1.payment))
print('-------------------------------------------------------------------------------')
print(repr(customer1))
print(repr(customer1.reservations))
print(repr(order1))
print(repr(order1.order_details))
print(repr(order1.payment))
# Printing the objects to verify relationships
print(customer1)
print(customer1.reservations)
print(order1)
print(order1.order_details)
print(order1.payment)

