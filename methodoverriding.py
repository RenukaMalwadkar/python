class parent():
    def __init__(self):
        self.value="Inside Parent"
    def show(self):
        print(self.value)
class child(parent):
    def __init__(self):
        self.value="Inside Child"
    def show(self):
        print(self.value)

obj1=parent()
obj2=child()
obj1.show()
obj2.show()