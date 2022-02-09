class Base:
    def __init__(self):
        self._a=19
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of a Base class.",self._a)
        self._a=83
        print("Calling updated protected member outside of class.",self._a)

Derived()
Base()
