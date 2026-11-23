import sys; sys.path.insert(0, sys.argv[1]); sys.path.insert(0, sys.argv[2])
import builtins
real = builtins.__import__
def imp(name, *a, **k):
    if name.split('.')[0] in ('numpy','scipy','pandas','torch'): raise ImportError('bloqué '+name)
    return real(name, *a, **k)
builtins.__import__ = imp
sys.path.insert(0, sys.argv[3]+'/tests')
from test_iib_scripts_v1 import SAIN
from controle_ia.iib import session_v5
sys.exit(session_v5.main(sys.argv[4:]))
