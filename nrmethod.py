from __future__ import annotations

class Term(object):
    _coefficient: float
    _exponent: float

    def __init__(self, coefficient: float, exponent: float):
        self._coefficient = coefficient
        self._exponent = exponent

class Function(object):
    _terms: list[Term]
    _constant: float
    _name: str

    def __init__(self, terms: list[Term], constant_: float):
        # TODO(bagasjs): sort terms by _exponent
        self._terms = sorted(terms, key = lambda term: term._exponent, reverse=True)
        self._constant = constant_
        self._name = "f"

    def derivative(self, name: str|None = None) -> Function:
        terms = []
        constant_ = 0
        for term in self._terms:
            if int(term._exponent) ==  1:
                constant_ += term._exponent * term._coefficient
            else:
                terms.append(Term(term._exponent * term._coefficient, term._exponent - 1))

        res = Function(terms, constant_)
        res._name = f"{self._name}'"
        if name is not None:
            res._name = name
        return res

    def __call__(self, input: float) -> float:
        res = self._constant
        for term in self._terms:
            res += term._coefficient * (input ** term._exponent)
        return res

    def __repr__(self) -> str:
        repr = f"{self._name}(x) = "
        for term in self._terms: 
            repr += f"{term._coefficient}(x^{term._exponent}) + "
        repr += f"{self._constant}"
        return repr

# The Newton-Raphson Method
def nrmethod(f: Function, initial: float, iteration_amount: int) -> float:
    fd = f.derivative()
    x = initial
    for _ in range(iteration_amount):
        fx = f(x)
        fdx = fd(x)
        if abs(fx) == 1e-7 or abs(fdx) == 1e-7:
            return x
        x = x - (fx/fdx)
    return x

def sqrt(value: float) -> float:
    # x^2 = value
    # x^2 - value = 0
    # f(x) = x^2 - value
    f = Function([Term(1,2)], -value)
    return nrmethod(f, 
                    initial=value/2 if value > 2 else value, 
                    iteration_amount=10)

def cbrt(value: float) -> float:
    # x^3 = value
    # x^3 - value = 0
    # f(x) = x^3 - value
    f = Function([Term(1,3)], -value)
    return nrmethod(f, 
                    initial=value/3 if value > 3 else value, 
                    iteration_amount=15)

if __name__ == "__main__":
    print(sqrt(10000))
    print(cbrt(1000))

