"""Génère le poste de reprise v5 et son constructeur v5 (R12 ; v1 à v4 restent tels quels), pour retenter la reprise
(lecture 38) de la confirmation du témoin de Bailey après le refus de redémarrage de la v4 (18 novembre, 02:02Z :
`sortie-conduite-v15/reprise-v10/bilan-reprise-v10.json`, « redémarrage refusé (GardeArret) », carte de la machine 146915
louée ailleurs selon la recherche d'offres). v5 = v4 dont seuls changent les noms (journal, PID, sorties, marque de fin,
état, script et son compagnon, nom et étiquette du serveur) ; la reprise écrit dans un dossier neuf (`reprise-v10-2`),
la v4 ayant déjà écrit `reprise-v10` (dossier antérieur au poste : non listé, garde AVANT de la v4). Aucune autre
différence : mêmes gardes (conduite v15 finie, crédit, instance 61049303 seule et arrêtée, commit a904aa39).
Usage : generer-pieces-reprise-confirmation-bailey-v3.py <dossier de sortie>"""
import sys
from pathlib import Path
out = Path(sys.argv[1])
base = Path("/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111")
for n in ("poste-hetzner-reprise-v5.sh", "construire-donnees-demarrage-reprise-v5.py"):
    assert not (out / n).exists() and not (base / n).exists(), f"{n} déjà présent (R12)"
p = (base / "poste-hetzner-reprise-v4.sh").read_text(encoding="utf-8")
h = "#!/bin/bash\n"
assert p.startswith(h)
corps = p.split("\nset -uo pipefail", 1)
c = corps[1]
k = c.count("reprise-v4")
assert k >= 8, k
c = c.replace("reprise-v4", "reprise-v5")
assert "reprise-v4" not in c and c.count('[ -s "$BASE/poste-fini-v13.json" ]') == 1 and "AVANT=" in c
p = (h + "# Poste Hetzner de REPRISE du témoin de Bailey, v5 (R12 ; v1 à v4 restent tels quels). v5 = v4 dont seuls changent\n"
     "# les noms (journal, PID, sorties, marque de fin, état, script) : nouvel essai de la reprise après le refus de redémarrage\n"
     "# de la v4 (18 novembre, 02:02Z) ; `reprendre` écrira `sortie-conduite-v15/reprise-v10-2/`.\n" + corps[0][len(h):]
     + "\nset -uo pipefail" + c)
(out / "poste-hetzner-reprise-v5.sh").write_text(p, encoding="utf-8")
k5 = (base / "construire-donnees-demarrage-reprise-v4.py").read_text(encoding="utf-8")
for a, b in (("de REPRISE, v4 (R12 ; v1 à v3 restent\ntelles quelles) = v3", "de REPRISE, v5 (R12 ; v1 à v4 restent\ntelles quelles) = v4"),
             ('"poste-hetzner-reprise-v4.sh"', '"poste-hetzner-reprise-v5.sh"'), ("(`poste-hetzner-reprise-v4.sh`)", "(`poste-hetzner-reprise-v5.sh`)"),
             ('"poste-temoin-bailey-reprise-v4"', '"poste-temoin-bailey-reprise-v5"'), ('"temoin-bailey-reprise-v4"}', '"temoin-bailey-reprise-v5"}')):
    assert k5.count(a) == 1, a
    k5 = k5.replace(a, b)
(out / "construire-donnees-demarrage-reprise-v5.py").write_text(k5, encoding="utf-8")
print("ok")
