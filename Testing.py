class A:
    def __init__(self):
        print("This is A's constructor")

    @classmethod
    def testMethod(self):
        print("This is a test method")

class B(A):
    def __init__(self):
        print("This is B's constructor")
        A.testMethod()
        # A.__init__(self)

class C(B):
    def __init__(self):
        print("This is C's constructor")
        self.testMethod()

class D(C):
    def __init__(self):
        print("This is D's constructor")
        B.__init__(self)

obj = D()

