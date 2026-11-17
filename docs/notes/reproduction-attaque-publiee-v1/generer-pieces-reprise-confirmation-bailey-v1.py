"""Génère les pièces de la reprise (lecture 38) de la confirmation du témoin de Bailey (addendum 7) : poste de reprise
v4 et son constructeur v4, depuis le poste de reprise v3 et son constructeur (R12 ; v1 à v3 restent telles quelles).
Différences avec la v3 : sortie de la conduite v15, `lanceur_v21`, instance 61049303 (étiquette
temoin-bailey-c6-40eb0b51dade4963), GO-2026-11-17-07, manifeste v7, garde du commit du code a904aa39, noms neufs (v4),
garde « conduite v15 finie » (marque `poste-fini-v13.json` sur la branche), et, après la reprise et avant la marque de
fin, la liste des répertoires de chaque dossier de reprise écrit (addendum 7, § 3).
Usage : generer-pieces-reprise-confirmation-bailey-v1.py <dossier de sortie>"""
import re, sys
from pathlib import Path
out = Path(sys.argv[1])
base = Path("/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111")
p = (base / "poste-hetzner-reprise-v3.sh").read_text(encoding="utf-8")
h = "#!/bin/bash\n"
assert p.startswith(h)
p = (h + "# Poste Hetzner de REPRISE du témoin de Bailey, v4 — REPRISE DE LA CONFIRMATION (addendum 7 ; R12 : v1 à v3 restent telles\n"
     "# quelles). v4 = v3 avec : sortie `sortie-conduite-v15`, `lanceur_v21 reprendre`, instance 61049303 (étiquette\n"
     "# temoin-bailey-c6-40eb0b51dade4963, arrêtée par Vast faute de crédit le 17 novembre vers 17:12Z), GO-2026-11-17-07,\n"
     "# manifeste v7, garde du commit du code a904aa39, noms neufs, garde « conduite v15 finie », liste des répertoires de\n"
     "# chaque dossier de reprise écrite, scellée et poussée avant la marque de fin (addendum 7, § 3).\n" + p[len(h):])
corps = p.split("\nset -uo pipefail", 1)
c = corps[1]
def rep(a, b, n=None):
    global c
    k = c.count(a); assert k >= 1 and (n is None or k == n), (a, k); c = c.replace(a, b)
rep("sortie-conduite-v11", "sortie-conduite-v15")
rep("reprise-v3", "reprise-v4")            # journaux, PID, marque, état, script et son compagnon
rep("manifeste-local-v5.json.sha256", "manifeste-local-v7.json.sha256", 1)
rep("8d1c541ef7a3ac99f942e0b2f26567088f2cc503", "a904aa391cdcf2650b747fe64e48caa0ec8c5849", 2)
rep("commit du code 8d1c541e", "commit du code a904aa39", 1)
rep("du commit 8d1c541e", "du commit a904aa39", 1)
rep('str(t[0]["id"]) == "60417353" and t[0].get("label") == "temoin-bailey-c6-89bd4d5cb025406c"',
    'str(t[0]["id"]) == "61049303" and t[0].get("label") == "temoin-bailey-c6-40eb0b51dade4963"', 1)
rep("inventaire conforme : 60417353 seule instance du témoin", "inventaire conforme : 61049303 seule instance du témoin", 1)
rep("GO_ID=GO-2026-11-10-10", "GO_ID=GO-2026-11-17-07", 1)
rep("--go-id GO-2026-11-10-10", "--go-id GO-2026-11-17-07", 1)
rep("controle_ia.temoin_bailey.lanceur_v17 reprendre", "controle_ia.temoin_bailey.lanceur_v21 reprendre", 1)
rep("--etiquette temoin-bailey-c6-89bd4d5cb025406c", "--etiquette temoin-bailey-c6-40eb0b51dade4963", 1)
assert not re.search(r"8d1c541e|60417353|89bd4d5c|lanceur_v17|GO-2026-11-10-10|sortie-conduite-v11|reprise-v3", c), "reste ancien"
# poussées : listes des dossiers de reprise
rep('"$BASE"/poste-hetzner-reprise-v4-etat.txt; do', '"$BASE"/poste-hetzner-reprise-v4-etat.txt "$BASE"/repertoires-sortie-conduite-v15--reprise-v10*; do', 1)
# garde : conduite v15 finie (marque du poste v13 sur la branche)
a = "# inventaire R10 : l'instance à reprendre doit exister, arrêtée ; aucune autre instance du témoin\n"
rep(a, "# v4 : la conduite v15 doit être finie (marque du poste v13 sur la branche), sinon rien ne tourne\n"
       '[ -s "$BASE/poste-fini-v13.json" ] || { etat "conduite v15 non finie (poste-fini-v13.json absent) : rien ne tourne"; pousser "conduite non finie"; exit 3; }\n' + a, 1)
# liste des répertoires de chaque dossier de reprise, avant la marque de fin
a = 'etat "reprise terminée, code $C"\n'
rep(a, a + (
    "# v4 : liste des répertoires de chaque dossier de reprise (addendum 7, § 3), hors du dossier, avant la marque de fin\n"
    'for R in "$BASE"/sortie-conduite-v15/reprise-v10*; do\n'
    '  [ -d "$R" ] || continue\n'
    '  L="repertoires-sortie-conduite-v15--$(basename "$R")-v1.txt"\n'
    '  [ -e "$BASE/$L" ] && continue\n'
    '  (cd "$R" && find . -mindepth 1 -type d -printf \'%P\\n\' | LC_ALL=C sort > "$BASE/$L")\n'
    '  (cd "$BASE" && [ -f "$L" ] && LC_ALL=C sha256sum "$L" > "$L.sha256")\n'
    '  etat "liste des répertoires écrite : $L"\n'
    'done\n'
    'pousser "listes des répertoires de reprise"\n'), 1)
p = corps[0] + "\nset -uo pipefail" + c
(out / "poste-hetzner-reprise-v4.sh").write_text(p, encoding="utf-8")
k = (base / "construire-donnees-demarrage-reprise-v3.py").read_text(encoding="utf-8")
for a, b in (("de REPRISE, v3 (R12 ; v1 et v2 restent\ntelles quelles) = v2", "de REPRISE, v4 (R12 ; v1 à v3 restent\ntelles quelles) = v3"),
             ('"poste-hetzner-reprise-v3.sh"', '"poste-hetzner-reprise-v4.sh"'), ("(`poste-hetzner-reprise-v3.sh`)", "(`poste-hetzner-reprise-v4.sh`)"),
             ('"poste-temoin-bailey-reprise-v3"', '"poste-temoin-bailey-reprise-v4"'), ('"temoin-bailey-reprise-v3"}', '"temoin-bailey-reprise-v4"}')):
    assert k.count(a) == 1, a; k = k.replace(a, b)
(out / "construire-donnees-demarrage-reprise-v4.py").write_text(k, encoding="utf-8")
print("ok")
