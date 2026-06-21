
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def show_info(self):
        return(f"{self.name} ({self.age}) - {self.email}")

anna = User("Anna", 28, "anna@x.com")

print(anna.show_info())