class vehicle:
    name="ktm"
    milage=25
    model=390
    cost=200000
    def __init__(self):
        print("object created")
    def print_details(self):
        print(f"name:{self.name},\nmilage:{self.milage},\nmodel:{self.model},\ncost:{self.cost}")
ob1=vehicle()