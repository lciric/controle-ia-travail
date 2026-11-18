"""Arithmétique du rédacteur de l'option « plan séquentiel » (lois normales supposées ; aucune donnée lue ;
aucune simulation jouée). Une affirmation, une dose : puissance de la borne basse > 0 pour un écart vrai donné.

    PYTHONPATH=src python3 -B calculs-option-sequentiel-v1.py > sortie-calculs-option-sequentiel-v1.txt
"""
import math

from scipy.stats import multivariate_normal, norm

from controle_ia.sequentiel_cycle2 import niveaux_v1 as niveaux

Q = niveaux.Q_DECISIF
ERREURS_TYPES_64 = (0.034, 0.038, 0.045)     # hypothèses de planification du brouillon 3, « Puissance »


def puissance_unique(effet, et64, n):
    return float(norm.sf(niveaux.z_de(Q) - effet / (et64 * math.sqrt(64 / n))))


def puissance_deux_lectures(effet, et64, n1, n, z1, z2):
    """(à l'intermédiaire ; à l'une des deux lectures) — accroissements normaux indépendants."""
    d1, d2 = effet / (et64 * math.sqrt(64 / n1)), effet / (et64 * math.sqrt(64 / n))
    r = math.sqrt(n1 / n)
    loi = multivariate_normal(mean=[0.0, 0.0], cov=[[1.0, r], [r, 1.0]])
    return float(norm.sf(z1 - d1)), 1.0 - float(loi.cdf([z1 - d1, z2 - d2]))


print("§ 1. Niveaux par lecture (percentile décisif du brouillon 3 : %.6f)" % Q)
for part in (0.1, 0.2, 0.3, 0.5):
    qi, qf = niveaux.repartir(Q, part)
    print("  part %.1f : intermédiaire %.7f (z %.3f ; tirages pour 25 en queue : %d) ; finale %.7f (z %.3f ; %d)"
          % (part, qi, niveaux.z_de(qi), niveaux.tirages_minimaux(qi), qf, niveaux.z_de(qf), niveaux.tirages_minimaux(qf)))
for t in (1 / 3, 0.5):
    z1, z2 = niveaux.bornes_depense(Q, t)
    print("  dépense de type O'Brien-Fleming, fraction %.2f : z %.3f (niveau nominal %.2e) puis z %.3f"
          % (t, z1, norm.sf(z1), z2))
print("  lecture unique : z %.3f" % niveaux.z_de(Q))

print("\n§ 2. Puissance d'une affirmation à une dose : unique | répartie (dès l'intermédiaire ; au total), par part")
for n1, n in ((200, 400), (200, 500), (200, 600), (300, 600)):
    for et in ERREURS_TYPES_64:
        for effet in (0.05, 0.075, 0.10):
            ligne = "  n1=%d N=%d et64=%.3f effet=%.3f : unique %.2f" % (n1, n, et, effet, puissance_unique(effet, et, n))
            for part in (0.2, 0.5):
                z1, z2 = (niveaux.z_de(x) for x in niveaux.repartir(Q, part))
                p1, p = puissance_deux_lectures(effet, et, n1, n, z1, z2)
                ligne += " | part %.1f : %.2f ; %.2f" % (part, p1, p)
            print(ligne)

print("\n§ 3. Risque réel du plan réparti sous accroissements normaux (borne d'union : au plus %.6f)" % Q)
for part in (0.2, 0.5):
    for t in (1 / 3, 0.5, 0.75):
        z1, z2 = (niveaux.z_de(x) for x in niveaux.repartir(Q, part))
        print("  part %.1f, fraction %.2f : %.6f ; sans correction (deux lectures au niveau plein) : %.6f"
              % (part, t, niveaux.risque_deux_lectures(z1, z2, t),
                 niveaux.risque_deux_lectures(niveaux.z_de(Q), niveaux.z_de(Q), t)))

print("\n§ 4. Effectif supplémentaire pour garder une puissance de 0,80 à la finale seule (rapport des effectifs)")
for part in (0.1, 0.2, 0.3, 0.5):
    zf = niveaux.z_de(niveaux.repartir(Q, part)[1])
    print("  part %.1f : %.3f" % (part, ((zf + norm.isf(0.2)) / (niveaux.z_de(Q) + norm.isf(0.2))) ** 2))

print("\n§ 5. Frontière du processus e à mélange normal (réglé sur un écart de 0,05, et64 = 0,038), en écarts types")
rho = (0.05 / (0.038 * 8)) ** 2
for n in (200, 400, 600):
    print("  après %d tâches : %.3f (lecture unique : %.3f)" % (n, niveaux.frontiere_melange(n, Q, rho), niveaux.z_de(Q)))
