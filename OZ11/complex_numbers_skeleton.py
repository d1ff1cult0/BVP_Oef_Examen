"""

    Definieer een ComplexNumber class die twee attributen heeft, een reëel deel en een imaginair deel. Implementeer hier
    4 methodes voor, plus, minus, multiply en conjugate.

"""


class ComplexNumber:
    # Overloaded operation
    """
        Dit laat toe om twee complexe getallen met elkaar te vergelijken via ==
    """

    def __eq__(self, other):
        re = other[0]
        im = other[1]
        other = ComplexNumber(re, im)
        return self.get_real() == other.get_real() and self.get_imaginary() == other.get_imaginary()

    def __init__(self, real, im):
        self.real = real
        self.im = im

    def get_real(self):
        return self.real

    def get_imaginary(self):
        return self.im

    def plus(self, other):
        return (self.real + other.real), (self.im + other.im)

    def minus(self, other):
        return self.real - other.real, self.im - other.im

    def multiply(self, other):
        return self.real * other.real - self.im * other.im, self.real * other.im + self.im * other.real

    def conjugate(self):
        return self.real, -self.im


c1 = ComplexNumber(1, 4)
c2 = ComplexNumber(2, 2)
c3 = ComplexNumber(1, -3)
assert c1.get_real() == 1
assert c2.get_imaginary() == 2
assert c1.plus(c2) == ComplexNumber(3, 6)
assert c1.minus(c3) == ComplexNumber(0, 7)
assert c1.multiply(ComplexNumber(0, 0)) == ComplexNumber(0, 0)
assert c2.multiply(c3) == ComplexNumber(8, -4)
assert c1.conjugate() == ComplexNumber(1, -4)
assert c3.conjugate() == ComplexNumber(1, 3)
