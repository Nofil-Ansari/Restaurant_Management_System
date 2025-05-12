import random as rd
class Customer():
    def __init__(self,customerID,name,contact_num,email):
        self.customerID = customerID
        self.name = name
        self.contact_num = contact_num
        self.email = email
        self.__validate_contact_num()
        self.reservations = [] #One to many relationship of Customers with Reservations
    
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
    
    def __repr__(self):
        return f"Tables({self.tableID!r}, {self.table_num!r}, {self.capacity!r}, {self.status!r})"
class Reservations:
    def __init__(self,ReservationID,customerID,tableID,reservation_date,status):
        self.ReservationID = ReservationID
        self.customerID = customerID
        self.tableID = tableID
        self.reservation_date = reservation_date
        self.status = status
    
    def __repr__(self):
        return f"Reservations({self.ReservationID!r}, {self.customerID!r}, {self.tableID!r}, {self.reservation_date!r}, {self.status!r})"
class Menu:
    def __init__(self,menuID,menu_item_name,price,availability=True):
        self.availability = availability
        self.menuID = menuID
        self.menu_item_name = menu_item_name
        self.price = price
    
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
    
    def __repr__(self):
        return f"Payment({self.paymentID!r}, {self.orderID!r}, {self.payment_type!r}, {self.amount_paid!r}, {self.payment_date!r})"
class OrderDetails:
    def __init__(self,Order_Detail_ID, Order_ID, Item_ID, Quantity, Price ):
        self.Order_Detail_ID = Order_Detail_ID
        self.Order_ID = Order_ID
        self.Item_ID = Item_ID
        self.Quantity = Quantity
        self.Price = Price
    
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
    input_status = f"Reservation Status is : {rd.choice(["Available", "Reserved"])}: "
    reservation = Reservations(ReservationID=input_reservationID, customerID=input_customerID, tableID=input_tableID, reservation_date=input_reservation_date, status=input_status)
    return reservation
reservation1 = reservation_procedure()
#customer1.add_reservation(reservation1)

# Creating Menu Items
def menu_procedure():
    input_menuID = rd.randint(60, 100)
    menu_items = ["Pasta", "Pizza", "Burger", "Salad", "Sushi", "Steak", "Tacos"]
    input_menu_item = rd.choice(menu_items)
    input_price = round(rd.uniform(5.0, 50.0), 2)
    menu_item = Menu(menuID=input_menuID, menu_item_name=input_menu_item, price=input_price)
    return menu_item
menu_item1 = menu_procedure()
menu_item2 = menu_procedure()

# Creating an 
def order_procedure():
    orderID = rd.randint(1, 1000)
    customerID = customer1.customerID
    tableID = table1.tableID
    menuID = menu_item1.menuID
    order_date = f"2025-{rd.choice(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])}-{rd.randint(1,31)}"
    total_amount = menu_item1.price + menu_item2.price
    status = rd.choice(["Pending", "Completed", "Cancelled"])
    order = Orders(orderID=orderID, customerID=customerID, tableID=tableID, menuID=menuID, order_date=order_date, total_amount=total_amount, status=status)
    return order
    
order1 = order_procedure()
# Adding Order Details
def order_detail_procedure():
    Order_Detail_ID = rd.randint(1, 1000)
    Order_ID = order1.orderID
    Item_ID = menu_item1.menuID
    Quantity = rd.randint(1, 5)
    Price = menu_item1.price * Quantity
    order_detail = OrderDetails(Order_Detail_ID=Order_Detail_ID, Order_ID=Order_ID, Item_ID=Item_ID, Quantity=Quantity, Price=Price)
    return order_detail 
order_detail1 = order_detail_procedure()
order_detail2 = order_detail_procedure()
order1.add_order_detail(order_detail1)
order1.add_order_detail(order_detail2)

# Creating a Payment
def payment_procedure():
    paymentID = rd.randint(1, 1000)
    orderID = order1.orderID
    payment_type = rd.choice(["Credit Card", "Debit Card", "Cash"])
    amount_paid = order1.total_amount
    payment_date = f"2025-{rd.randint(1,12)}-{rd.randint(1,31)}"
    payment = Payment(paymentID=paymentID, orderID=orderID, payment_type=payment_type, amount_paid=amount_paid, payment_date=payment_date)
    return payment  
payment1 = payment_procedure()
order1.add_payment(payment1)
print('-------------------------------------------------------------------------------')
print(f'details of the customer: {customer1}')
print(f'details of the table: {table1}')
print(f'details of the reservation: {reservation1}')
print(f'details of the menu item: {menu_item1.menu_item_name} and {menu_item2.menu_item_name}')
print(f'details of the order: {order1}')
print(f'details of the order detail: {order_detail1}')
print(f'details of the payment: {payment1}')
print('-------------------------------------------------------------------------------')
def display_all_customers(customers):
    print("Customer ID\tName\tContact Number\tEmail")
    print("-------------------------------------------------")
    for customer in customers:
        print(f"CustomerID: {customer.customerID}\n Customer Name: {customer.name}\n Customer Phone Number: {customer.contact_num}\n Customer Emaill address: {customer.email}")
    print("-------------------------------------------------")
display_all_customers([customer1])
def display_all_tables(tables):
    print("Table ID\tTable Number\tCapacity\tStatus")
    print("-------------------------------------------------")
    for table in tables:
        print(f"Table ID: {table.tableID}\n Table Number: {table.table_num}\n Table Capacity: {table.capacity}\n Table Status: {table.status}")
    print("-------------------------------------------------")
display_all_tables([table1])
def display_all_reservations(reservations):
    print("Reservation ID\tCustomer ID\tTable ID\tReservation Date\tStatus")
    print("-------------------------------------------------")
    for reservation in reservations:
        print(f"Reservation ID: {reservation.ReservationID}\n Customer ID: {reservation.customerID}\n Table ID: {reservation.tableID}\n Reservation Date: {reservation.reservation_date}\n Reservation Status: {reservation.status}")
    print("-------------------------------------------------")
display_all_reservations([reservation1])
def display_all_menu_items(menu_items):
    print("Menu ID\tMenu Item Name\tPrice")
    print("-------------------------------------------------")
    for menu_item in menu_items:
        print(f"Menu ID: {menu_item.menuID}\n Menu Item Name: {menu_item.menu_item_name}\n Menu Item Price: {menu_item.price}")
    print("-------------------------------------------------")
display_all_menu_items([menu_item1, menu_item2])
def display_all_orders(orders):
    print("Order ID\tCustomer ID\tTable ID\tMenu ID\tOrder Date\tTotal Amount\tStatus")
    print("-------------------------------------------------")
    for order in orders:
        print(f"Order ID: {order.orderID}\n Customer ID: {order.customerID}\n Table ID: {order.tableID}\n Menu ID: {order.menuID}\n Order Date: {order.order_date}\n Total Amount: {order.total_amount}\n Order Status: {order.status}")
    print("-------------------------------------------------")
display_all_orders([order1])
def display_all_order_details(order_details):
    print("Order Detail ID\tOrder ID\tItem ID\tQuantity\tPrice")
    print("-------------------------------------------------")
    for order_detail in order_details:
        print(f"Order Detail ID: {order_detail.Order_Detail_ID}\n Order ID: {order_detail.Order_ID}\n Item ID: {order_detail.Item_ID}\n Quantity: {order_detail.Quantity}\n Price: {order_detail.Price}")
    print("-------------------------------------------------")
display_all_order_details([order_detail1, order_detail2])
def display_all_payments(payments):
    print("Payment ID\tOrder ID\tPayment Type\tAmount Paid\tPayment Date")
    print("-------------------------------------------------")
    for payment in payments:
        print(f"Payment ID: {payment.paymentID}\n Order ID: {payment.orderID}\n Payment Type: {payment.payment_type}\n Amount Paid: {payment.amount_paid}\n Payment Date: {payment.payment_date}")
    print("-------------------------------------------------")
display_all_payments([payment1])
