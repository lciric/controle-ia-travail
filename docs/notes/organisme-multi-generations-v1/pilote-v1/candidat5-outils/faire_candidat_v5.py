"""Écrit le candidat 5 du préenregistrement du pilote MR-2 depuis le candidat 4 (R12 : fichier neuf ; le candidat 4 reste en place).

Remplacements comptés : chaque texte visé doit être présent exactement le nombre de fois dit, sinon refus et rien n'est écrit.
Porte : la note des prix v2 (erreur PO-040 corrigée, « offre standard ») ; les trois constats mineurs rendus en réponse par le
lecteur de la vérification courte du candidat 4, dont le rapport n'a pas pu être écrit (refus d'un classifieur, PO-039, non
contourné) ; l'état de cette vérification. Aucun réseau.

Usage : python3 -I faire_candidat_v5.py CANDIDAT4 SORTIE DEBUT_UTC
"""
import hashlib
import os
import re
import sys

C4_SHA = "576b070b83eabe2525cabb8225f68d75548c83bd64f49ae517e7b44d73c780a9"
NOTE2 = "pilote-v1/prix-publics-sonde-v74-compte-organisme/lecture-prix-publics-sonde-v74-v2.md"
NOTE2_SHA = "b88253b841d5f41ec83d7be86c9f62402b429a13b6ed2a63a6984641f735643d"
CLAUDE = "crédits des proposeurs `fable52` et `opus55`"


def main():
    c4, sortie, debut = sys.argv[1:4]
    if os.path.exists(sortie):
        sys.exit("REFUS : sortie existante (R12)")
    b = open(c4, "rb").read()
    if hashlib.sha256(b).hexdigest() != C4_SHA:
        sys.exit("REFUS : empreinte du candidat 4")
    t = b.decode("utf-8")
    n_r = [0]

    def r(old, new, n=1):
        k = t.count(old)
        if k != n:
            sys.exit(f"REFUS : « {old[:90]} » présent {k} fois, {n} attendu(s)")
        n_r[0] += 1
        return t.replace(old, new)

    # --- titre, statut ------------------------------------------------------------------------------------------------------
    t = r("— v1, candidat 4 (compte organisme)", "— v1, candidat 5 (compte organisme)")
    t = r("""**Statut : candidat au scellement, « scellable après la vérification courte du différentiel candidat 3 → candidat 4 et
l'inscription, par la mère, de la lecture des prix publics à la place de la console » (R1) ; jamais scellé par son auteur.** Nom neuf
(R12) : le candidat 3""",
          """**Statut : candidat au scellement, « scellable après une vérification courte versée du différentiel candidat 4 → candidat 5 et
l'inscription, par la mère, de la lecture des prix publics à la place de la console » (R1) ; jamais scellé par son auteur.** Nom neuf
(R12) : le candidat 4 (`preenregistrement-pilote-conditionnelles-v1-candidat4-compte-organisme.md`, `576b070b…`) reste versé,
inchangé ; ce candidat 5 y porte la note des prix v2 et les trois constats mineurs rendus par le lecteur de la vérification courte
du candidat 4, dont le rapport n'a pas pu être versé (table « Changements depuis le candidat 4 »). Le candidat 3""")
    t = r("""**R-2542** (code v69 : parts π1 = 20,00 et π2 = 21,72 USD ; loi hors bornes récrite en `transformee` ; effort « high » envoyé aux
deux proposeurs de Claude, rien à Argon ni à Astra ; voie de Claude branchée)""",
          """**R-2542** (code v69 : parts π1 = 20,00 et π2 = 21,72 USD ; loi hors bornes récrite en `transformee` ; effort « high » envoyé aux
deux proposeurs `fable52` et `opus55`, rien à `argon` ni à `astra` ; voie de leur fournisseur branchée)""")
    t = r("""aucun appel du pilote, aucune dépense du pilote** avant la vérification courte de ce candidat, l'inscription de la lecture des prix""",
          """aucun appel du pilote, aucune dépense du pilote** avant la vérification courte versée de ce candidat, l'inscription de la lecture des prix""")
    t = r("""## Changements depuis le candidat 3
""", """## Changements depuis le candidat 4

| # | fait, erreur ou constat | ce que fait le candidat 5 | où |
|---|---|---|---|
| journal PO-039 | vérification courte du différentiel candidat 3 → candidat 4 par un lecteur neuf (modèle F) : l'écriture de son rapport a été refusée par un classifieur ; refus non contourné, rapport non écrit par le rédacteur ; constats rendus en réponse seulement | état dit (rapport non versé) ; vérification courte du différentiel candidat 4 → candidat 5 à faire, rapport versé exigé | Statut ; Ordre ; Préalables ; Contre-lecture |
| journal PO-040 | erreur de la note des prix v1 : un prix de l'offre longue d'`astra` qui n'est pas dans la page versée | **note des prix v2** citée (`""" + NOTE2_SHA[:8] + """…`) ; la v1 reste au registre des documents | Documents ; Préalables ; Devis |
| constat 1 (rendu en réponse) | « prix publics » sans l'offre | « offre standard » dite (seule offre des relais) | Préalables ; Devis |
| constat 2 (rendu en réponse) | `astra` : offre courte seulement | « offre courte, au plus 272 000 jetons d'entrée ; texte servi au plus 52 000 octets » | Préalables |
| constat 3 (rendu en réponse) | nom de famille du fournisseur hors des tables d'historique | « """ + CLAUDE + """ » ou « sur crédits » ; inchangés : lignes de GO inscrites et proposées, mots exigés par le lecteur gelé | En-tête ; En dix lignes ; Dessin ; Devis |

## Changements depuis le candidat 3
""")

    # --- documents ----------------------------------------------------------------------------------------------------------
    t = r("""| `pilote-v1/prix-publics-sonde-v74-compte-organisme/lecture-prix-publics-sonde-v74-v1.md` (branche `lot/compte-organisme-v1`) | `21bfbbd76dcd4dd5c5219054aa13ec6a93149c51fd48fc046385ca5acf3b8f10` |""",
          """| `pilote-v1/prix-publics-sonde-v74-compte-organisme/lecture-prix-publics-sonde-v74-v1.md` (branche `lot/compte-organisme-v1`) | `21bfbbd76dcd4dd5c5219054aa13ec6a93149c51fd48fc046385ca5acf3b8f10` (remplacée par la v2) |
| **lecture des prix publics, v2** (offre standard ; erreur de la v1 corrigée, journal PO-040) | `""" + NOTE2 + """` (branche `lot/compte-organisme-v1`) | `""" + NOTE2_SHA + """` |
| candidat 4 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat4-compte-organisme.md` | `""" + C4_SHA + """` |""")

    # --- constat 3 : nom du fournisseur ---------------------------------------------------------------------------------------
    t = r("(π1 20,00 sur crédits de Claude ;", f"(π1 20,00 sur {CLAUDE} ;")
    t = r("| `fable52` | Claude | 3 USD |", "| `fable52` | sur crédits | 3 USD |")
    t = r("| `opus55` | Claude | 2 USD |", "| `opus55` | sur crédits | 2 USD |")
    t = r("| **sonde v74, ligne s1** (GO-2026-11-14-10, crédits de Claude) :", f"| **sonde v74, ligne s1** (GO-2026-11-14-10, {CLAUDE}) :")
    t = r("| **pilote, π1** (crédits de Claude) :", f"| **pilote, π1** ({CLAUDE}) :")

    # --- ordre --------------------------------------------------------------------------------------------------------------
    t = r("""vérifications courtes (candidat 2 → 3 : faite ; candidat 3 → 4 : à faire)""",
          """vérifications courtes (candidat 2 → 3 : faite ; candidat 3 → 4 : rapport non versé, refus d'un classifieur ; candidat 4 → 5 :
à faire, rapport versé)""")

    # --- préalables (constats 1 et 2, note v2, vérifications) -----------------------------------------------------------------
    t = r("""(3) **fait, à inscrire par la mère** : prix lus,
non à la console mais sur les pages publiques des trois fournisseurs,""",
          """(3) **fait, à inscrire par la mère** : prix de
l'offre standard (seule offre des relais : ni mode rapide ni lot) lus, non à la console mais sur les pages publiques des trois
fournisseurs,""")
    t = r("""(note `21bfbbd7…`) : `fable52` 8 / 40, `opus55` 4 / 20, `astra` 10 / 50 (contexte court) USD par million, égaux à la
configuration ;""",
          f"""(note v2 `{NOTE2_SHA[:8]}…`) : `fable52` 8 / 40, `opus55` 4 / 20, `astra` 10 / 50 (offre courte, au plus 272 000 jetons
d'entrée ; texte servi au plus 52 000 octets) USD par million, égaux à la configuration ;""")
    t = r("""**aucun prix public d'entrée ou de sortie au-dessus de celui de la configuration v12**""",
          """**aucun prix public de l'offre standard (entrée ou sortie) au-dessus de celui de la configuration v12**""")
    t = r("""les prix », 0 bloquant, 0 majeur, 4 mineurs, portés ici) ; **à faire** : vérification courte du différentiel candidat 3 → candidat 4
par un lecteur neuf d'un autre modèle que le rédacteur ;""",
          """les prix », 0 bloquant, 0 majeur, 4 mineurs, portés ici) ; vérification courte du différentiel candidat 3 → candidat 4 : rapport
non versé (refus d'un classifieur à son écriture, non contourné ; ses constats, rendus en réponse, sont portés ici) ; **à faire** :
vérification courte du différentiel candidat 4 → candidat 5 par un lecteur neuf d'un autre modèle que le rédacteur, **rapport versé** ;""")

    # --- devis --------------------------------------------------------------------------------------------------------------
    t = r("""prix publics lus le 14 novembre : égaux pour `fable52`, `opus55` et
`astra`, au-dessous pour `argon`, note des prix).""",
          """prix publics de l'offre standard lus le 14 novembre : égaux pour
`fable52`, `opus55` et `astra`, au-dessous pour `argon`, note des prix v2).""")
    t = r("""Prix après la sonde : lus sur les pages publiques des fournisseurs, non à la console (préalable 3 ; note `21bfbbd7…`) ;
aucun au-dessus de la configuration.""",
          f"""Prix après la sonde : ceux de l'offre standard, lus sur les pages publiques des fournisseurs, non à la console (préalable 3 ;
note v2 `{NOTE2_SHA[:8]}…`) ; aucun au-dessus de la configuration.""")

    # --- contre-lecture -----------------------------------------------------------------------------------------------------
    t = r("""- **Vérification courte du différentiel candidat 3 → candidat 4** (prix publics, constats mineurs) : à faire sur ce texte, avant le
  scellement, par un lecteur neuf d'un autre modèle que le rédacteur (jamais sur la lignée du proposeur `fable52` avant le 20 novembre
  15:00 UTC) ; rapport `pilote-v1/verification-courte-candidat3-candidat4-preenregistrement-pilote-v1.md`, à côté de ce texte, avec le
  texte relu et son empreinte.""",
          """- **Vérification courte du différentiel candidat 3 → candidat 4** (prix publics, constats mineurs) : lecteur neuf, modèle F, autre
  modèle que le rédacteur ; texte relu `576b070b83eabe2525cabb8225f68d75548c83bd64f49ae517e7b44d73c780a9` ; **rapport non versé** :
  son écriture a été refusée par un classifieur, refus non contourné, et le rédacteur ne l'écrit pas à sa place (journal du compte
  organisme, PO-039) ; ses trois constats mineurs, rendus en réponse, sont portés au candidat 5.
- **Vérification courte du différentiel candidat 4 → candidat 5** (note des prix v2, trois constats mineurs) : à faire sur ce texte,
  avant le scellement, par un lecteur neuf d'un autre modèle que le rédacteur (jamais sur la lignée du proposeur `fable52` avant le
  20 novembre 15:00 UTC) ; rapport `pilote-v1/verification-courte-candidat4-candidat5-preenregistrement-pilote-v1.md`, **versé** à
  côté de ce texte, avec le texte relu et son empreinte ; si son écriture est refusée à nouveau, nœud de la mère.""")

    # --- heures -------------------------------------------------------------------------------------------------------------
    old_h = t[t.index("Rédaction du candidat 4 : début"):]
    t = r(old_h, f"Rédaction du candidat 5 : début {debut} UTC ; fin @@FIN@@ UTC (`date -u`).\n")

    # --- contrôles ----------------------------------------------------------------------------------------------------------
    a, b2 = t.index("## Changements depuis le candidat 3"), t.index("## Documents") if "## Documents" in t else None
    restants = sorted(set(re.findall(r"\[[A-Z][A-Z0-9-]{3,}\]", t[:t.index("## Changements depuis le candidat 1")]
                                     + t[t.index("## Changements depuis le brouillon 4"):])))
    if restants:
        sys.exit(f"REFUS : marqueurs restants {restants}")
    hors_go = "\n".join(l for l in t.split("\n") if not l.startswith("| GO-") and "« crédits de Claude »" not in l)
    tete = hors_go[:hors_go.index("## Changements depuis le candidat 4")]
    corps = hors_go[hors_go.index("## En dix lignes"):]
    for nom in ("Claude", "Fable"):
        for zone, z in (("en-tête", tete), ("corps", corps)):
            for m in re.finditer(nom, z):
                ligne = z[z.rfind("\n", 0, m.start()) + 1:z.find("\n", m.start())]
                if "R-2690" in ligne or "identifiant de modèle Claude" in ligne or "voie de Claude, bornes" in ligne:
                    continue
                sys.exit(f"REFUS : « {nom} » restant ({zone}) : {ligne[:120]}")
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(t)
    print(f"{n_r[0]} remplacements comptés ; aucun marqueur restant")


if __name__ == "__main__":
    main()
