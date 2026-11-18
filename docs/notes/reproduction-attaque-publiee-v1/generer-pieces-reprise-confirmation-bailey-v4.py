"""Génère le poste de reprise v6 et son constructeur v6 (R12 ; v1 à v5 restent tels quels) : reprise (lecture 38) de la
RELANCE de la confirmation du témoin de Bailey (conduite v16, instance 61170458), pour l'option B du plan de sauvegarde
du 18 novembre (06:00Z) : plus aucune recharge du loueur (mot de Lazar, GO-2026-11-18-07, relayé par la session mère),
crédit épuisé avant la fin de la relance. Préparée d'avance, sans dépense ; rien n'est lancé sans le mot de Lazar.
v6 = v5 dont changent seulement : la sortie (`sortie-conduite-v16`), l'instance (61170458, étiquette
`temoin-bailey-c6-845f37c35eba4a3d`, relevée par `vastai show instances` le 18 novembre vers 04:55Z ; l'identifiant
est aussi celui de la ligne de création de `sortie-conduite-v16/conduite-v5.jsonl`, qui ne porte pas l'étiquette), la garde « conduite v16 finie » (marque du poste v14,
`poste-fini-v14.json`), les listes des répertoires (`repertoires-sortie-conduite-v16--…`) et les noms (v6). Mêmes
gardes sinon : crédit positif et recharge sans échec, instance seule et arrêtée, commit du code a904aa39, manifeste v7,
GO-2026-11-17-07. `reprendre` écrira `sortie-conduite-v16/reprise-v10/` (aucune reprise antérieure dans cette sortie).
Usage : generer-pieces-reprise-confirmation-bailey-v4.py <dossier de sortie>"""
import re
import sys
from pathlib import Path

out = Path(sys.argv[1])
base = Path("/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111")
for n in ("poste-hetzner-reprise-v6.sh", "construire-donnees-demarrage-reprise-v6.py"):
    assert not (out / n).exists() and not (base / n).exists(), f"{n} déjà présent (R12)"
p = (base / "poste-hetzner-reprise-v5.sh").read_text(encoding="utf-8")
h = "#!/bin/bash\n"
assert p.startswith(h)
corps = p.split("\nset -uo pipefail", 1)
assert len(corps) == 2
c = corps[1]


def rep(a, b, n=None):
    global c
    k = c.count(a)
    assert k >= 1 and (n is None or k == n), (a, k)
    c = c.replace(a, b)


rep("sortie-conduite-v15", "sortie-conduite-v16")
rep("reprise-v5", "reprise-v6")
rep("conduite v15", "conduite v16")
rep("poste-fini-v13.json", "poste-fini-v14.json")
rep("marque du poste v13", "marque du poste v14", 1)
rep("61049303", "61170458")
rep("temoin-bailey-c6-40eb0b51dade4963", "temoin-bailey-c6-845f37c35eba4a3d")
assert not re.search(r"sortie-conduite-v15|reprise-v5|61049303|40eb0b51|poste-fini-v13|conduite v15", c), "reste ancien"
assert c.count('[ -s "$BASE/poste-fini-v14.json" ]') == 1 and "AVANT=" in c and "lanceur_v21 reprendre" in c
assert c.count("a904aa391cdcf2650b747fe64e48caa0ec8c5849") == 2 and "GO_ID=GO-2026-11-17-07" in c
p = (h + "# Poste Hetzner de REPRISE du témoin de Bailey, v6 (R12 ; v1 à v5 restent tels quels) — reprise de la RELANCE de la\n"
     "# confirmation (conduite v16, instance 61170458, étiquette temoin-bailey-c6-845f37c35eba4a3d), option B du plan de\n"
     "# sauvegarde du 18 novembre (crédit épuisé, plus aucune recharge). v6 = v5 dont changent seulement la sortie\n"
     "# (`sortie-conduite-v16`), l'instance et son étiquette, la garde « conduite v16 finie » (`poste-fini-v14.json`), les\n"
     "# listes des répertoires et les noms ; `reprendre` écrira `sortie-conduite-v16/reprise-v10/`. Les lignes d'en-tête des\n"
     "# versions antérieures, ci-dessous, restent telles quelles (elles parlent de la conduite v15 et de 61049303).\n"
     + corps[0][len(h):] + "\nset -uo pipefail" + c)
(out / "poste-hetzner-reprise-v6.sh").write_text(p, encoding="utf-8")
k = (base / "construire-donnees-demarrage-reprise-v5.py").read_text(encoding="utf-8")
for a, b in (("de REPRISE, v5 (R12 ; v1 à v4 restent\ntelles quelles) = v4", "de REPRISE, v6 (R12 ; v1 à v5 restent\ntelles quelles) = v5"),
             ('"poste-hetzner-reprise-v5.sh"', '"poste-hetzner-reprise-v6.sh"'),
             ("(`poste-hetzner-reprise-v5.sh`)", "(`poste-hetzner-reprise-v6.sh`)"),
             ('"poste-temoin-bailey-reprise-v5"', '"poste-temoin-bailey-reprise-v6"'),
             ('"temoin-bailey-reprise-v5"}', '"temoin-bailey-reprise-v6"}')):
    assert k.count(a) == 1, a
    k = k.replace(a, b)
(out / "construire-donnees-demarrage-reprise-v6.py").write_text(k, encoding="utf-8")
print("ok")
