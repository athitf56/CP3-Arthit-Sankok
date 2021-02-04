class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " , self.name , " " , self.lastName  , "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Ba"
customer1.age = 8

customer1.addCart()

customer2 = Customer()
customer2.name = "Boy"
customer2.lastName = "Ba"
customer2.age = 8

customer2.addCart()

customer3 = Customer()
customer3.name = "Boyo"
customer3.lastName = "Ba"
customer3.age = 8

customer3.addCart()

customer4 = Customer()
customer4.name = "Bopo"
customer4.lastName = "Ba"
customer4.age = 8

customer4.addCart()