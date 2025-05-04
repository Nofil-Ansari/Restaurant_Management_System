class Employees:
    def __init__(self, employeeID, name, age, salary,Contact_num,hire_date):
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
        