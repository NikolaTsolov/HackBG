class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        bigger = max(self.numerator, self.denominator)
        for number in range(2, bigger+1):
            if self.numerator % number == 0 and self.denominator % number == 0:
                self.numerator = self.numerator / number
                self.denominator = self.denominator / number


    def od(self):
        bigger = max(self.numerator, self.denominator)
        for number in range(2, bigger+1):
            if self.numerator % number == 0 and self.denominator % number == 0:
                self.numerator = self.numerator / number
                self.denominator = self.denominator / number


    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)


    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        a = Fraction(numerator, denominator)
        return a

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.numerator % other.numerator == 0 and self.denominator % other.denominator == 0


def main():
    a = Fraction(1, 2)
    b = Fraction(2, 4)

    print(a)
    print(b)
    print(a == b)
    print(a + b)
    print(a - b)
    print(a * b)

if __name__ == '__main__':
    main()
