"""Erreur type d'une exactitude (simple et équilibrée) et écart minimal détectable entre deux bras, sur les parts de la
banque `confrontation-v5` (effectifs lus dans `banque-confrontation-v5.json` : `manifeste.comptes_par_strate` et `n`,
jamais dans un fichier de clé). Formules fermées, loi binomiale, approximation normale :
- exactitude simple sur n tâches : ET = sqrt(p(1-p)/n) ;
- exactitude équilibrée d'une famille (n1, n0 par classe, exactitude p dans chaque classe) : ET = sqrt(p(1-p)(1/n1+1/n0))/2 ;
- score du programme (moyenne des deux familles) : ET = sqrt(ET_c^2 + ET_d^2)/2 ;
- écart minimal détectable (bilatéral 5 %, puissance 80 %) entre deux bras de k courses chacun, erreurs indépendantes :
  EMD = (1,96 + 0,8416) * sqrt(2/k) * ET  (borne optimiste : tout le bruit est « de course », il baisse en 1/sqrt(k)) ;
- plancher apparié sur les MÊMES tâches (le tirage des tâches ne baisse pas avec k) : si les deux bras diffèrent sur une
  part q des tâches, ET(Δ) >= sqrt(q/n) sur l'exactitude simple.
Écrit le 26 octobre 2026 (sous-agent conv-audit, étape 1 v10). Usage : python -I erreur_type_ecart_detectable_v1.py BANQUE_V5.json"""
import collections
import json
import math
import pathlib
import sys

Z = 1.959964 + 0.841621
p = pathlib.Path(sys.argv[1])
if p.name.endswith(("-cle.json", "-secret.json")):
    sys.exit("refusé")
m = json.loads(p.read_text(encoding="utf-8"))["manifeste"]
comptes = collections.defaultdict(lambda: collections.Counter())
for strate, parts in m["comptes_par_strate"].items():
    famille, classe = strate.split("|")[:2]
    for part, n in parts.items():
        comptes[(part, famille)][classe] += n
print("effectifs (part, famille) -> par classe :", {f"{k[0]}|{k[1]}": dict(v) for k, v in sorted(comptes.items())})
print("n par part :", m["n"])


def et_eq(n1, n0, q):
    return math.sqrt(q * (1 - q) * (1 / n1 + 1 / n0)) / 2


for part in ("test", "test_final"):
    c = list(comptes[(part, "conscience-evaluation")].values())
    d = list(comptes[(part, "controle-delegation")].values())
    n = m["n"][part]
    for q in (0.5, 0.75):
        etc, etd = et_eq(*c, q), et_eq(*d, q)
        etg = math.sqrt(etc ** 2 + etd ** 2) / 2
        ets = math.sqrt(q * (1 - q) / n)
        emd = {k: round(Z * math.sqrt(2 / k) * etg, 3) for k in (1, 2, 3, 4, 6, 10)}
        k_01 = math.ceil((Z * math.sqrt(2) * etg / 0.10) ** 2)
        print(f"{part} (n={n}, conscience {c}, délégation {d}), exactitude vraie {q} : ET simple {ets:.4f} ; "
              f"ET équilibrée conscience {etc:.4f}, délégation {etd:.4f}, score global {etg:.4f} ; "
              f"EMD du score global (k courses par bras) {emd} ; k pour EMD <= 0,10 : {k_01}")
    for qd in (0.1, 0.2, 0.3):
        print(f"  {part} : plancher apparié, désaccord q={qd} : ET(Δ) >= {math.sqrt(qd / n):.4f}, EMD >= {Z * math.sqrt(qd / n):.3f}")
print("une erreur en délégation (6 par classe) déplace l'exactitude équilibrée de la famille de", round(1 / 6 / 2, 4),
      "et le score global de", round(1 / 6 / 4, 4))
