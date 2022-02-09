import abc
class car(abc.ABC):
    def __init__(self,name):
        self.name=name
    def description(self):
        print("description of class car.")
    def price(self,x):
        class new(car):
            def price(self,x):
                print(f"the{self.name}'s price is{x}lakhs.")
    obj=new("Honda City")