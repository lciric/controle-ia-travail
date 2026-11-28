"""Greffon pytest : lignes exécutées du module de l'addendum 2 (toute copie), par (fonction, décalage), sans dépendance."""
import json, os, sys

SORTIE = os.environ["TRACE_AV2_SORTIE"]
VUES = set()


def _local(frame, event, arg):
    if event == "line":
        c = frame.f_code
        VUES.add((c.co_qualname if hasattr(c, "co_qualname") else c.co_name, frame.f_lineno - c.co_firstlineno))
    return _local


def _global(frame, event, arg):
    if frame.f_code.co_filename.endswith("audit_verdict_p3_v1.py"):
        c = frame.f_code
        VUES.add((c.co_qualname if hasattr(c, "co_qualname") else c.co_name, 0))
        return _local
    return None


def pytest_sessionstart(session):
    sys.settrace(_global)


def pytest_sessionfinish(session, exitstatus):
    sys.settrace(None)
    with open(SORTIE, "w") as f:
        json.dump(sorted(VUES), f)
