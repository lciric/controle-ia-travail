# cas sain du bras S : calcul symbolique et numérique avec les versions de l'environnement isolé
import mpmath
import numpy
import scipy
import sympy

x = sympy.symbols("x")
print("SAIN", sympy.simplify((x**2 - 1) / (x - 1)))
print("VERSIONS", sympy.__version__, mpmath.__version__, numpy.__version__, scipy.__version__)
