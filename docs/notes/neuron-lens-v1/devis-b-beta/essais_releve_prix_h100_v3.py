"""Essais de l'épreuve des offres du relevé v3 (`releve_prix_h100_v3.py`) : un cas sain, des artefacts, des bornes (R5).

Lancement : `python3 -I docs/notes/neuron-lens-v1/devis-b-beta/essais_releve_prix_h100_v3.py` ; aucun appel au loueur, aucun réseau.
Prix avec stockage de la base = dph + 0,5 × 200 / 720 = dph + 0,1389.
"""
import importlib.util
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("releve_v3", ICI / "releve_prix_h100_v3.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

BASE = {"id": 1, "dph_total": 2.50, "storage_cost": 0.5, "inet_up": 500, "inet_up_cost": 0.01, "inet_down_cost": 0.01,
        "verification": "verified"}


def cas(**k):
    return dict(BASE, **k)


ESSAIS = [
    ("cas sain, L2 3,00 / 88, refus", m.passe(BASE, 3.00, 88.0, 3.40, "refus"), True),
    ("cas sain, L2 3,00 / 88, borne", m.passe(BASE, 3.00, 88.0, 3.40, "borne"), True),
    ("machine non vérifiée", m.passe(cas(verification="unverified"), 3.00, 88.0, 3.40, "borne"), False),
    ("prix au-dessus du prix exigé (3,039)", m.passe(cas(dph_total=2.90), 3.00, 88.0, 3.40, "borne"), False),
    ("sous le prix minimal 2,11, règle refus (2,039)", m.passe(cas(dph_total=1.90), 3.00, 88.0, 3.40, "refus"), False),
    ("sous le prix minimal 2,11, règle borne (2,039)", m.passe(cas(dph_total=1.90), 3.00, 88.0, 3.40, "borne"), True),
    ("débit montant 150", m.passe(cas(inet_up=150), 3.00, 88.0, 3.40, "borne"), False),
    ("trafic entrant 0,05", m.passe(cas(inet_down_cost=0.05), 3.00, 88.0, 3.40, "borne"), False),
    ("trafic sortant 0,05", m.passe(cas(inet_up_cost=0.05), 3.00, 88.0, 3.40, "borne"), False),
    ("prix minimal L2 88 = 2,1056", abs(m.prix_minimal(88.0, 3.40) - 2.1056) < 1e-3, True),
    ("prix minimal L1 82 = 2,0222", abs(m.prix_minimal(82.0, 1.00) - 2.0222) < 1e-3, True),
    ("prix minimal L1 115 = 2,8472", abs(m.prix_minimal(115.0, 1.00) - 2.8472) < 1e-3, True),
    ("L1 4,25 / 115, 2,939 au-dessus du prix minimal 2,85 : passe en refus", m.passe(cas(dph_total=2.80), 4.25, 115.0, 1.00, "refus"), True),
    ("L1 4,25 / 115, 2,739 sous le prix minimal 2,85 : écartée en refus", m.passe(cas(dph_total=2.60), 4.25, 115.0, 1.00, "refus"), False),
    ("ligne témoin non évaluée", m.ligne(m.TEMOIN, cas(machine_id=1, host_id=1, reliability=0.9, gpu_ram=81559,
                                                        geolocation="x"))[-1], "-"),
]
try:
    m.passe(BASE, 3.00, 88.0, 3.40, "autre")
    ESSAIS.append(("règle inconnue refusée", False, True))
except ValueError:
    ESSAIS.append(("règle inconnue refusée", True, True))

echecs = [(nom, obtenu, attendu) for nom, obtenu, attendu in ESSAIS if obtenu != attendu]
for nom, obtenu, attendu in ESSAIS:
    print(("ok    " if obtenu == attendu else "ÉCHEC ") + nom)
print(f"{len(ESSAIS) - len(echecs)} essai(s) passé(s) sur {len(ESSAIS)}")
sys.exit(1 if echecs else 0)
