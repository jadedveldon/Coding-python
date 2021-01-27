import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.imaginary = imaginary
        self.real = real

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = (self.real * no.real) - (self.imaginary * no.imaginary)
        imaginary = (no.real * self.imaginary) + (self.real * no.imaginary)
        return Complex(real, imaginary)

    def __truediv__(self, no):
        den = no.real ** 2 + no.imaginary ** 2
        num_real = self.real * no.real + self.imaginary * no.imaginary
        num_imaginary = - self.real * no.imaginary + self.imaginary * no.real
        return Complex(num_real / den, num_imaginary / den)

    def mod(self):
        real = math.sqrt((self.real ** 2) + (self.imaginary ** 2))
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')


#https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen