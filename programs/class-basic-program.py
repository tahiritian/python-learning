class Account():
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t
    def credit(self, amount):
        self.b += amount
    def debit(self, amount):
        self.b -= amount


ac1 = Account('tahiritian', 100, 'S')
print(ac1.n, ac1.b, ac1.t)
ac1.credit(100000)
print(ac1.n, ac1.b, ac1.t)
ac1.debit(100)
print(ac1.n, ac1.b, ac1.t)

#[ output

#$ python class-basic-program.py
#tahiritian 100 S
#tahiritian 100100 S
#tahiritian 100000 S

#]