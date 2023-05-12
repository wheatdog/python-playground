from numbers import Number, Complex, Real, Rational, Integral


# https://peps.python.org/pep-0484/#the-numeric-tower
# when an argument is annotated as having type float, an argument of type int is acceptable

# https://peps.python.org/pep-3141/
assert issubclass(Complex, Number) == True
assert issubclass(Real, Complex) == True
assert issubclass(Rational, Real) == True
assert issubclass(Integral, Rational) == True


assert issubclass(float, Real) == True
assert issubclass(int, Integral) == True

# https://peps.python.org/pep-0285/
assert issubclass(bool, int) == True


def test(value: float) -> None:
    pass

test(123)  # pass type checker
test(True)  # pass type checker