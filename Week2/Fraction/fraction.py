class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        for num in range(1, min(abs(self.numerator), abs(self.denominator)) + 1):
            if self.denominator % num == 0 and self.numerator % num == 0:
                self.denominator //= num
                self.numerator //= num



    def __str__(self):
        self.simplify()
        if self.denominator == 1:
            return "{}".format(self.numerator)
        else:
            return "{} / {}".format(self.numerator, self.denominator)



    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        num = Fraction(numerator, denominator)
        num.simplify()
        return num

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        num = Fraction(numerator, denominator)
        num.simplify()
        return num

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        num = Fraction(numerator, denominator)
        num.simplify()
        return num

    def __eq__(self, other):
        self.simplify()
        other.simplify()
        if self.numerator != 0:
            return self.__str__() == other.__str__()
        elif self.numerator == other.numerator:
            return True
        else:
            return False


