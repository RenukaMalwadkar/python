class Base(object):
    def __init__(self):
        self.str="Renuka"
        print("Base")
class Base1(object):
    def __init__(self):
        self.str1="Malwadkar"
        print("Base1")
class Derived(Base,Base1):
    def __init__(self):
        Base.__init__(self)
        Base1.__init__(self)
        print("Derived")
    def printstr2(self):
        print(self.str,self.str1)
ob=Derived()
ob.printstr2()
