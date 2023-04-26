# calculate √2 with 100 decimals
from sympy import sqrt, N
N(sqrt(2), 100)


# calculate 1/2 + 1/3 in rational arithmetic
from sympy import Rational
a = Rational(1, 2)
b = Rational(1, 3)
a + b


# calculate the expanded form of (x + y)^6
from sympy import symbols, expand, Eq
x, y = symbols('x y')
expand((x + y) ** 6)


# symplify the trigonometric expression sin (x) / cos (x)
from sympy import Symbol, sin, cos, simplify, Eq
x = Symbol('x')
simplify(sin(x) / cos(x))


# calculate lim x -> 0: sin(x) - x / x^3
from sympy import Symbol, sin, limit
x = Symbol('x')
expr = (sin(x) - x) / x ** 3
limit(expr, x, 0)


# calculate the derivative of log(x), 1/x, sin(x) and cos(x) for x
from sympy import Symbol, diff, log, sin, cos
x = Symbol('x')
diff(log(x), x)
diff(1 / x, x)
diff(sin(x), x)
diff(cos(x), x)


# solve the system of equations x + y = 2, 2x + y = 0
from sympy import symbols, linsolve
x, y = symbols('x y')
system = [x + y - 2, 2 * x + y]
linsolve(system, x, y)


# integrate x^2, sin(x), cos(x) interms of x and y
from sympy import symbols, integrate, sin, cos
x, y = symbols('x y')
integrate(x ** 2, x)
integrate(x ** 2, y)
integrate(sin(x), x)
integrate(sin(x), y)
integrate(sin(x), y)
integrate(cos(x), x)
integrate(cos(x), y)


# solve f''(x) + 9 f(x) = 1
from sympy import Function, Symbol, diff, Eq, dsolve
x = Symbol('x')
f = Function('f')
eq = Eq(diff(diff(f(x))) + 9 * diff(f(x)), 1)
dsolve(eq)


# using matrices solve the linear equations: 3x + 7y = 12z, 4x - 2y = 5z
from sympy import Matrix, linsolve, symbols
x, y, z = symbols('x y z')
M = Matrix(((3, 7, -12), (4, -2, -5)))
linsolve(M, x, y, z)