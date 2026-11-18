"""Génère le poste de reprise v7 (dit « v6 bis ») et son constructeur v7 (R12 ; v1 à v6 restent tels quels) : variante B′
du repli de la relance de la confirmation du témoin de Bailey (18 novembre ; GO-2026-11-18-09 ; B′ soumise à Lazar par la
session mère, sans son mot c'est B, tel que le GO l'écrit). B′ : pas de redémarrage. La session détruit le serveur Hetzner
du poste v14 (176575468) par son identifiant, ce qui arrête la conduite v16, puis pousse la marque
`arret-conduite-v16-poste-v14.json` ; ce poste lance ensuite `lanceur_v21 reprendre --arreter-en-cours` sur l'instance
61170458 encore en marche (branche « running » de `Reprise`, `src/` figé au commit a904aa39) : arrêt de la commande en
cours par son PID, état reconstitué (« arrêt par la conduite »), transfert, destruction.
v7 = v6 dont changent seulement : la garde « conduite v16 finie » remplacée par la marque d'arrêt de la conduite (le
poste v14 détruit n'écrit pas `poste-fini-v14.json`) ; l'inventaire, qui exige l'instance en marche (états réel et
voulu « running ») ; la garde de crédit, au moins 1,0 USD (transfert en marche d'environ 20 min à 1,2194 USD/h, environ
0,4 USD, sans redémarrage ni attente de carte) ; l'option `--arreter-en-cours` ; les noms (v7).
Usage : generer-pieces-reprise-confirmation-bailey-v6.py <dossier de sortie>"""
import re
import sys
from pathlib import Path

out = Path(sys.argv[1])
base = Path("/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111")
for n in ("poste-hetzner-reprise-v7.sh", "construire-donnees-demarrage-reprise-v7.py"):
    assert not (out / n).exists() and not (base / n).exists(), f"{n} déjà présent (R12)"
p = (base / "poste-hetzner-reprise-v6.sh").read_text(encoding="utf-8")
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


rep("reprise-v6", "reprise-v7")
rep("# v4 : la conduite v16 doit être finie (marque du poste v14 sur la branche), sinon rien ne tourne\n"
    '[ -s "$BASE/poste-fini-v14.json" ] || { etat "conduite v16 non finie (poste-fini-v14.json absent) : rien ne tourne"; pousser "conduite non finie"; exit 3; }\n',
    "# v7 (B′) : la conduite v16 doit être arrêtée (serveur du poste v14 détruit par la session, marque poussée), sinon rien ne tourne\n"
    '[ -s "$BASE/arret-conduite-v16-poste-v14.json" ] || { etat "conduite v16 non arrêtée (arret-conduite-v16-poste-v14.json absent) : rien ne tourne"; pousser "conduite non arrêtée"; exit 3; }\n', 1)
rep("# v6 : crédit Vast au moins 2,0 USD (pire cas du redémarrage 1,87 USD, plus le stockage), sinon rien ne tourne ;\n",
    "# v7 : crédit Vast au moins 1,0 USD (transfert en marche, sans redémarrage : environ 0,4 USD), sinon rien ne tourne ;\n", 1)
rep('etat "crédit Vast sous 2,0 USD : rien ne tourne"', 'etat "crédit Vast sous 1,0 USD : rien ne tourne"', 1)
rep("sys.exit(0 if float(u.get('credit') or 0) >= 2.0 else 1)", "sys.exit(0 if float(u.get('credit') or 0) >= 1.0 else 1)", 1)
rep("# inventaire R10 : l'instance à reprendre doit exister, arrêtée ; aucune autre instance du témoin\n",
    "# inventaire R10 (v7) : l'instance à reprendre doit exister, en marche ; aucune autre instance du témoin\n", 1)
rep('and t[0].get("actual_status") in ("exited", "stopped") and t[0].get("intended_status") in (None, "", "exited", "stopped")',
    'and t[0].get("actual_status") == "running" and t[0].get("intended_status") == "running"', 1)
rep('etat "inventaire conforme : 61170458 seule instance du témoin, arrêtée"',
    'etat "inventaire conforme : 61170458 seule instance du témoin, en marche"', 1)
rep("  --go-id GO-2026-11-17-07 --depot \"$DEPOT\" \\\n", "  --go-id GO-2026-11-17-07 --depot \"$DEPOT\" --arreter-en-cours \\\n", 1)
assert not re.search(r"reprise-v6|poste-fini-v14|>= 2\.0", c), "reste ancien"
assert c.count("--arreter-en-cours") == 1 and c.count("arret-conduite-v16-poste-v14.json") == 2
p = (h + "# Poste Hetzner de REPRISE du témoin de Bailey, v7 dit « v6 bis » (R12 ; v1 à v6 restent tels quels) — variante B′ du\n"
     "# repli de la relance (conduite v16, instance 61170458 EN MARCHE) : `reprendre --arreter-en-cours`, sans redémarrage,\n"
     "# après destruction du serveur du poste v14 (176575468) par la session et poussée de `arret-conduite-v16-poste-v14.json`.\n"
     "# v7 = v6 dont changent seulement cette garde, l'inventaire (instance en marche), la garde de crédit (au moins 1,0 USD),\n"
     "# l'option et les noms. Les lignes d'en-tête des versions antérieures, ci-dessous, restent telles quelles.\n"
     + corps[0][len(h):] + "\nset -uo pipefail" + c)
(out / "poste-hetzner-reprise-v7.sh").write_text(p, encoding="utf-8")
k = (base / "construire-donnees-demarrage-reprise-v6.py").read_text(encoding="utf-8")
for a, b in (("de REPRISE, v6 (R12 ; v1 à v5 restent\ntelles quelles) = v5", "de REPRISE, v7 (R12 ; v1 à v6 restent\ntelles quelles) = v6"),
             ('"poste-hetzner-reprise-v6.sh"', '"poste-hetzner-reprise-v7.sh"'),
             ("(`poste-hetzner-reprise-v6.sh`)", "(`poste-hetzner-reprise-v7.sh`)"),
             ('"poste-temoin-bailey-reprise-v6"', '"poste-temoin-bailey-reprise-v7"'),
             ('"temoin-bailey-reprise-v6"}', '"temoin-bailey-reprise-v7"}'),
             ("Lit `poste-hetzner-reprise-v6.sh`", "Lit `poste-hetzner-reprise-v7.sh`")):
    assert k.count(a) == 1, a
    k = k.replace(a, b)
(out / "construire-donnees-demarrage-reprise-v7.py").write_text(k, encoding="utf-8")
print("ok")
