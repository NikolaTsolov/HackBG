class Fraction:

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    def numerator(self):
        return self.__numerator

    def denominator(self):
        return self.__denominator

    def simplify(self):
        for num in range(1, min(abs(self.__numerator), abs(self.__denominator)) + 1):
            if self.__denominator % num == 0 and self.__numerator % num == 0:
                self.__denominator //= num
                self.__numerator //= num



    def __str__(self):
        self.simplify()
        if self.__denominator == 1:
            return "{}".format(self.__numerator)
        else:
            return "{} / {}".format(self.__numerator, self.__denominator)



    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        num = Fraction(numerator, denominator)
        num.simplify()
        return num

    def __sub__(self, other):
        numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        num = Fraction(numerator, denominator)
        num.simplify()
        return num

    def __mul__(self, other):
        numerator = self.__numerator * other.__numerator
        denominator = self.__denominator * other.__denominator
        num = Fraction(numerator, denominator)
        num.simplify()
        return num

    def __eq__(self, other):
        self.simplify()
        other.simplify()
        if self.__numerator != 0:
            return self.__str__() == other.__str__()
        elif self.__numerator == other.__numerator:
            return True
        else:
            return False


