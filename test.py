class Aa:
    def a(self):
        print('this is 000000')

    def b(self):
        print('1')
    
    def getOperand(self, myop):
        mydict = {'0':self.a, '1':self.b}
        return mydict[myop]()
    

myclass = Aa()
myclass.getOperand('0')