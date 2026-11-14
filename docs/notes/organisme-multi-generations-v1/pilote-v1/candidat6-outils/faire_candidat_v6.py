"""Écrit le candidat 6 du préenregistrement du pilote MR-2 depuis le candidat 5 (R12 : fichier neuf ; le candidat 5 reste en place).

Porte les décisions de la mère R-2803 (préalable 3 : lecture des prix publics déclarée comme telle ; la console fait foi pour les
montants facturés), R-2804 (vérification courte par un lecteur neuf, rapport écrit et versé) et R-2769 (dépense de la sonde v74
inscrite). Le candidat 5 portait déjà les trois mineurs du verdict rendu en réponse ; il reste versé, inchangé. La vérification
demandée est cumulée : différentiel candidat 3 → candidat 6 (le rapport de 3 → 4 n'a pas pu être versé). Remplacements comptés.

Usage : python3 -I faire_candidat_v6.py CANDIDAT5 SORTIE DEBUT_UTC
"""
import hashlib
import os
import re
import sys

C5_SHA = "c6c4eee8bb13b704c79e4937e20ac38476a65a322695cb277f6c7e31154e913d"
RAPPORT = "pilote-v1/verification-courte-candidat3-candidat6-preenregistrement-pilote-v1.md"


def main():
    c5, sortie, debut = sys.argv[1:4]
    if os.path.exists(sortie):
        sys.exit("REFUS : sortie existante (R12)")
    b = open(c5, "rb").read()
    if hashlib.sha256(b).hexdigest() != C5_SHA:
        sys.exit("REFUS : empreinte du candidat 5")
    t = b.decode("utf-8")
    n_r = [0]

    def r(old, new, n=1):
        k = t.count(old)
        if k != n:
            sys.exit(f"REFUS : « {old[:90]} » présent {k} fois, {n} attendu(s)")
        n_r[0] += 1
        return t.replace(old, new)

    t = r("— v1, candidat 5 (compte organisme)", "— v1, candidat 6 (compte organisme)")
    t = r("""**Statut : candidat au scellement, « scellable après une vérification courte versée du différentiel candidat 4 → candidat 5 et
l'inscription, par la mère, de la lecture des prix publics à la place de la console » (R1) ; jamais scellé par son auteur.** Nom neuf
(R12) : le candidat 4""",
          """**Statut : candidat au scellement, « scellable après une vérification courte versée du différentiel candidat 3 → candidat 6 »
(R1, R-2804) ; jamais scellé par son auteur.** Nom neuf (R12) : le candidat 5
(`preenregistrement-pilote-conditionnelles-v1-candidat5-compte-organisme.md`, `c6c4eee8…`) reste versé, inchangé ; ce candidat 6 y
porte les décisions de la mère R-2803 (préalable 3), R-2804 (vérification courte versée) et R-2769 (dépense de la sonde inscrite)
(table « Changements depuis le candidat 5 »). Le candidat 4""")
    t = r("""aucun appel du pilote, aucune dépense du pilote** avant la vérification courte versée de ce candidat, l'inscription de la lecture des prix
par la mère, le scellement par `controle_ia.prereg.sceller_prereg` et les lignes de GO du pilote inscrites.""",
          """aucun appel du pilote, aucune dépense du pilote** avant la vérification courte versée de ce candidat, le scellement par
`controle_ia.prereg.sceller_prereg` et les lignes de GO du pilote inscrites sur le mot de Lazar.""")
    t = r("""## Changements depuis le candidat 4
""", """## Changements depuis le candidat 5

| # | décision | ce que fait le candidat 6 | où |
|---|---|---|---|
| R-2803 | le préalable 3 devient la lecture des prix publics, déclarée comme telle ; la console fait foi pour les montants facturés | préalable 3 « fait, inscrit (R-2803) » ; phrase « la console fait foi pour les montants facturés » ajoutée ; plus aucun « à inscrire par la mère » hors des tables d'historique | Préalables ; Ordre ; Statut |
| R-2804 | vérification courte par un lecteur neuf, rapport écrit et versé ; si le même refus du classifieur revient, arrêt sans rejouer | vérification exigée **cumulée** : différentiel candidat 3 → candidat 6 (le rapport de 3 → 4 n'a pas pu être versé, celui de 4 → 5 n'a pas été fait) ; rapport `""" + RAPPORT + """` | Statut ; Ordre ; Préalables ; Contre-lecture |
| R-2769 | dépense de la sonde v74 inscrite (0,099132 USD) | dite au devis | Devis |

## Changements depuis le candidat 4
""")
    t = r("""| candidat 4 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat4-compte-organisme.md` | `576b070b83eabe2525cabb8225f68d75548c83bd64f49ae517e7b44d73c780a9` |""",
          """| candidat 4 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat4-compte-organisme.md` | `576b070b83eabe2525cabb8225f68d75548c83bd64f49ae517e7b44d73c780a9` |
| candidat 5 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat5-compte-organisme.md` | `""" + C5_SHA + """` |""")
    t = r("""prix publics lus et rapprochés (fait ; lecture
à inscrire par la mère) → vérifications courtes (candidat 2 → 3 : faite ; candidat 3 → 4 : rapport non versé, refus d'un classifieur ; candidat 4 → 5 :
à faire, rapport versé) → texte scellé""",
          """prix publics lus et rapprochés (fait ; préalable
inscrit, R-2803) → vérifications courtes (candidat 2 → 3 : faite ; candidat 3 → 4 : rapport non versé, refus d'un classifieur ;
candidat 3 → 6, cumulée : à faire, rapport versé) → texte scellé""")
    t = r("""(3) **fait, à inscrire par la mère** : prix de
l'offre standard""", """(3) **fait, inscrit par la mère (R-2803)** :
lecture des prix publics, déclarée comme telle ; prix de l'offre standard""")
    t = r("""aux prix publics, la sonde aurait coûté 0,056092 USD (0,099132 au relevé) ; le montant
réellement facturé n'est pas lu ;""",
          """aux prix publics, la sonde aurait coûté 0,056092 USD (0,099132 au relevé) ; le montant
réellement facturé n'est pas lu ici : **la console fait foi pour les montants facturés** (R-2803) ;""")
    t = r("""**à faire** :
vérification courte du différentiel candidat 4 → candidat 5 par un lecteur neuf d'un autre modèle que le rédacteur, **rapport versé** ;""",
          """**à faire** :
vérification courte du différentiel candidat 3 → candidat 6 (cumulée) par un lecteur neuf d'un autre modèle que le rédacteur,
**rapport écrit et versé** (R-2804) ;""")
    t = r("""| **0,099132** (calculé aux prix de la configuration ; 0,056092 aux prix publics) |""",
          """| **0,099132** (calculé aux prix de la configuration, inscrit, R-2769 ; 0,056092 aux prix publics) |""")
    t = r("""- **Vérification courte du différentiel candidat 4 → candidat 5** (note des prix v2, trois constats mineurs) : à faire sur ce texte,
  avant le scellement, par un lecteur neuf d'un autre modèle que le rédacteur (jamais sur la lignée du proposeur `fable52` avant le
  20 novembre 15:00 UTC) ; rapport `pilote-v1/verification-courte-candidat4-candidat5-preenregistrement-pilote-v1.md`, **versé** à
  côté de ce texte, avec le texte relu et son empreinte ; si son écriture est refusée à nouveau, nœud de la mère.""",
          """- **Vérification courte du différentiel candidat 3 → candidat 6** (cumulée : prix publics, note v2, constats mineurs, décisions
  R-2803, R-2804, R-2769) : à faire sur ce texte, avant le scellement, par un lecteur neuf d'un autre modèle que le rédacteur (jamais
  sur la lignée du proposeur `fable52` avant le 20 novembre 15:00 UTC) ; rapport `""" + RAPPORT + """`, **écrit et versé** à côté de ce
  texte, avec le texte relu et son empreinte ; si le même refus du classifieur revient, arrêt sans rejouer (R-2804).""")
    old_h = t[t.index("Rédaction du candidat 5 : début"):]
    t = r(old_h, f"Rédaction du candidat 6 : début {debut} UTC ; fin @@FIN@@ UTC (`date -u`).\n")

    hors_hist = t[:t.index("## Changements depuis le candidat 5")] + t[t.index("## En dix lignes"):]
    if "à inscrire par la mère" in hors_hist.replace("lecture à inscrire par la mère).", ""):
        i = hors_hist.find("à inscrire par la mère")
        sys.exit(f"REFUS : « à inscrire par la mère » restant : {hors_hist[max(0, i - 120):i + 30]}")
    restants = sorted(set(re.findall(r"\[[A-Z][A-Z0-9-]{3,}\]", t[:t.index("## Changements depuis le candidat 1")]
                                     + t[t.index("## Changements depuis le brouillon 4"):])))
    if restants:
        sys.exit(f"REFUS : marqueurs restants {restants}")
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(t)
    print(f"{n_r[0]} remplacements comptés ; aucun marqueur restant")


if __name__ == "__main__":
    main()
