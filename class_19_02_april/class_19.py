class cow:
    def __init__(self,a,b):
        self.cowname = a
        self.bullname = b
    
    def gaushala(self):
        print("Good Morning")

class calf(cow):
    def student(self):
        print("Good Morning2")

obj1 = cow('girl','boy')
obj1.gaushala()
obj2 = calf('Women', 'Man')
obj2.gaushala()
obj2.student()



