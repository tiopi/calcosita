
# a, b, n, m is an element of z (integers), x and y are function variables
# code currently only works for functions such that f(x) = ax^n + by^m or f(x) = ax^n
# LIMITED TO 2 VARIABLES/2D --> XY

import re

class Derive(object):


    #  regex constants - i.p
    COS = re.compile("cos([xy])")
    SIN = re.compile("sin([xy])")
    TAN = re.compile("tan([xy])")
    SEC = re.compile("sec([xy])")
    CSC = re.compile("csc([xy])")
    COT = re.compile("cot([xy])")
    ARCCOS = re.compile("arccos([xy])")
    ARCSIN = re.compile("arcsin([xy])")
    ARCTAN = re.compile("arctan([xy])")
    LN = re.compile("ln([xy])")

    def __init__(self, f):
        self.f = f

    def d1(self, var):  # power rule
        pow = int(self.f[self.f.index("^")+1])  # new power
        coeff = 1
        if "" not in self.f[:self.f.index(var)]:
            coeff = int(self.f[:self.f.index(var)])  # multiply coeff w/ new power
        self.f = str(pow*coeff) + var + "^" + str(pow-1)  # modify new string
        return self.f

    def d2(self):  # product rule
        X = Derive(self.f[:self.f.index("y")])
        Y = Derive(self.f[self.f.index("y"):])
        xstr = X.getstr()
        ystr = "(" + Y.getstr() + ")"
        return Derive.cleanup(self, X.d1("x")) + ystr + " + " + xstr + "(" + Derive.cleanup(self, Y.d1("y")) + ")"

    # methods or constants or regex ?? i.p
    def dsin(self):
        return "cos(x)"

    def dcos(self):
        return "-sin(x)"

    def dtan(self):
        return "sec^2(x)"

    def cleanup(self, s):
        if "^1" in s:  # clean up function format
            s = s[:s.index("^")]
        elif "^0" in s:
            s = s[:s.index("x")]
        if s == "1":
            s = ""
        return s

    def getstr(self):
        return self.f


x = Derive("x^2y^2")
print(Derive.d2(x))

