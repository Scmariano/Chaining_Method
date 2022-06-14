class User:
    def __init__ (self, first_name, last_name, email, age):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.age = age
        self.rewards_member = False
        self.gold_card_points = 0

    
    def display_info(self):
        # your code
        print()
        print(f"Name : {self.firstName} {self.lastName} \nEmail: {self.email} \nAge: {self.age}")
        print(f"Member : {self.rewards_member}\nPoints : {self.gold_card_points}")
    	# new return statement, returns this same object
        return self

    def enroll(self):
        self.rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        return self
    
    def birthday(self):
        self.age += 1
        return self

User_Stephen = User("Stephen", "Mariano", "stephen@gmail.com", 32)

User_Stephen.display_info().enroll().display_info().spend_points(20).birthday().display_info()