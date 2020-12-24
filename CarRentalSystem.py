# store customer deatils in list so we can use that  later to display the billing information
class Manager:

    def __init__(self):
        self.users = []


    def register_user(self, user):
        self.users.append(user)

    def verify_user(self, user):
        return user in self.users  # True or False

    def get_users(self):
        return self.users
#get all the user inforamtion
class User:

    def __init__(self, first_name, last_name, cars_rented, bill_amt=0):
        self.first_name = first_name
        self.last_name = last_name
        self.cars_rented = cars_rented
        self.bill_amt = bill_amt

    def set_cars_rented(self, cars):
        self.cars_rented += cars

    def get_cars_rented(self):
        return self.cars_rented

    def set_bill_amt(self, bill_amt):
        self.bill_amt += bill_amt

    def get_bill_amt(self):
        return self.bill_amt

#after customre entering all the dtails go for rent and return function
class Customer:

    def __init__(self, Stock, user_obj):
        self.stock = Stock
        self.user = user_obj

    def CustomerDetails(self):

        cars=RentCar(self.stock,self.user)
        cars.RentORReturn()

#change the number of car as per rent and return of car
class Stock:
    def __init__(self, stock_no):
        self.stock_no = stock_no

    def reduce_stock(self, modifier):
        self.stock_no -= modifier

class RentCar:
    def __init__(self,stock, user):
        self.stock = stock
        self.user = user

    def RentORReturn(self):

        try:
          type =  int(input("Enter 1 for Rent the car and 2 for return the car:  "))
          if type > 2 or type < 1:
                 raise Exception("Invalid input range")
                 self.RentORReturn()
        except:
            print("Invalid input type")
            self.RentORReturn()
        if type == 1:
            self.showStock()
        elif type == 2:

            self.customer_exit()
            print("Thank you for returning ", self.user.get_cars_rented(), " cars! Hope you enjoyed the experience")
            self.stock.stock_no = self.stock.stock_no + self.user.get_cars_rented()
            self.user.cars_rented -= self.user.get_cars_rented()




    def customer_exit(self):


            print("Total bill amount is ", self.user.get_bill_amt())

    def showStock(self):

        if self.stock.stock_no > 0:
            print("we have ", self.stock.stock_no, "Cars available")
            self.requestCar()
        else:
            print("We don't have any more cars for rent.Thank you for visiting us.You can try after some time.Have a good day ahead!!!")


    def Hrbasis(self,car,hours):
        bill_amt = 20*car*hours
        print("As per $20 per hour your total bill amount will be: $",bill_amt)
        self.user.set_bill_amt(bill_amt)
        self.stock.reduce_stock(car)

    def DailyBasis(self,car,day):
        bill_amt = 80 * car * day
        print("As per $80 per day your total bill amount will be: $",bill_amt)
        self.user.set_bill_amt(bill_amt)
        self.stock.reduce_stock(car)

    def WeeklyBasis(self,car,week):
        bill_amt = 300 * car * week
        print("As per $300 per hour your total bill amount will be: $",bill_amt)
        self.user.set_bill_amt(bill_amt)
        self.stock.reduce_stock(car)
    def requestCar(self):
        car =int( input("Enter number of Car you want to rent: "))
        # try catch for number of cars entered
        if car > self.stock.stock_no:
            print("we don't have that much cars available please enter less number of cars")
            self.requestCar()
        else:
            self.user.set_cars_rented(car)
            self.requestBasis(car)

    def requestBasis(self,car):
         print("You can rent car on following three bases:")
         print("For Hourly Basis($20/hr) enter 1 ")
         print("For Daily Basis($80/day) enter 2 ")
         print("For weekly Basis($300/week) enter 3 ")
         try:
            basis = int(input("Select on which basis you want to rent the car: "))
            if basis > 3 or basis < 1:
                raise Exception("Invalid input range")
                self.requestBasis(car)
         except:
             print("Invalid input type")
             self.requestBasis(car)


         # rentCar = RentCar()
         if basis == 1:
             hours = float(input("Select for how many hours you want to rent the car: "))
             self.Hrbasis(car, hours)
             print("You have rented total ", self.user.get_cars_rented()," cars")
         elif basis == 2:
             day = int(input("Select for how many day/s you want to rent the car: "))
             self.DailyBasis(car, day)
             print("You have rented total ", self.user.get_cars_rented(), " cars")
         elif basis == 3:
             week = int(input("Select for how  many week/s you want to rent the car: "))
             self.WeeklyBasis(car, week)
             print("You have rented total ", self.user.get_cars_rented(), " cars")


def main():
    stock_obj = Stock(10)
    manager = Manager()
    for i in range (10):
        print("Hi There,Welcome to RentCar Bazar")
        firstname = (input("Enter your first name: "))
        lastname = (input("Enter your last name: "))

        # check for returning users
        flag = 0
        for user in manager.get_users():
            if user.first_name == firstname:
                user_obj = user
                flag = 1
                print("Hey User Welcome back!!!")
                break
        if flag != 1:
            print("Hello New user!!!")
            user_obj = User(firstname, lastname, 0)
            manager.register_user(user_obj)
         # initialised as static val
        customer = Customer(stock_obj, user_obj)
        customer.CustomerDetails()



main()