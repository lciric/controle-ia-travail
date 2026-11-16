"""Part de la moitié chère dans l'attendu des proposeurs, d'après les moyennes du pilote MR-2 v14 (information).

Complément de `devis-crible-v-foi-v1.py` (mêmes entrées, recopiées à la main de la section « Pour les cribles »
du verdict et du registre des dépenses, l. 479-480) : f = ($ de Pr-3 + $ de Pr-4) / ($ des quatre), aux prix publics
puis au compte de la configuration ; épargne S(k) = f (N - k) / N à N = 20 quand la règle appelle les chers dans k
mondes (approximation de la section « Seuil » du brouillon 9, dollars égaux d'un monde à l'autre) ; plus grand k
avec S(k) >= 0,25. Information seulement : le seuil 0,25 et les étages ne changent pas. Bibliothèque standard,
fractions exactes ; aucune donnée lue, aucun tirage, aucun appel.
"""

from fractions import Fraction as F

moy_pub = {"Pr-1": F("0.494324") / 4, "Pr-2": F("1.057336") / 4, "Pr-3": F("1.671750") / 4, "Pr-4": F("10.019552") / 4}
moy_cfg = dict(moy_pub, **{"Pr-1": F("2.471620") / 4})
N = 20
for nom, m in (("prix public", moy_pub), ("compte de la configuration", moy_cfg)):
    f = (m["Pr-3"] + m["Pr-4"]) / sum(m.values())
    kmax = max(k for k in range(N + 1) if f * (N - k) / N >= F(1, 4))
    print(f"{nom} : part de la moitié chère f = {float(f):.4f} ; S >= 0,25 ssi k <= {kmax} "
          f"(S({kmax}) = {float(f * (N - kmax) / N):.4f} ; S({kmax + 1}) = {float(f * (N - kmax - 1) / N):.4f}) ; "
          f"S(0) = {float(f):.4f} ; S(3) = {float(f * (N - 3) / N):.4f}")
