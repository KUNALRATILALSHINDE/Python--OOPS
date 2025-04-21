#initiating a class
class Employee:
    #constructor
    def __init__  (self):
        print("Whenever a non tech user comes to open an app, they did not want to connect anything like internet ,db setup, So constructor helps to do that")
        print("This data gets executed when an object is created")
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"

    def travel(self):
        print("This is executed manually when the function is called")
        print("Traveling to a new city")

#Creating an object/instance of the class
sam = Employee()

# print(sam.salary)
# sam.travel()

print(type(sam))