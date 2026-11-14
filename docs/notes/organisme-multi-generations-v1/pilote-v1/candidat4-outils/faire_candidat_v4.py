"""Écrit le candidat 4 du préenregistrement du pilote MR-2 depuis le candidat 3 (R12 : fichier neuf ; le candidat 3 reste en place).

Remplacements comptés : chaque texte visé doit être présent exactement le nombre de fois dit, sinon refus et rien n'est écrit.
Porte : la lecture des prix publics (note `21bfbbd7…`, sur le message tapé dans le compte organisme), qui lève [PRIX-CONSOLE] ;
les quatre constats mineurs de la vérification courte du différentiel candidat 2 → candidat 3 (`f3dc757b…`). Aucun réseau.

Usage : python3 -I faire_candidat_v4.py CANDIDAT3 SORTIE DEBUT_UTC
"""
import os
import re
import sys
import hashlib

C3_SHA = "539cf171739ee9649719c7c851ebbf8e721e8f225b71ef5ec57ac44e0f8755a6"
NOTE = "pilote-v1/prix-publics-sonde-v74-compte-organisme/lecture-prix-publics-sonde-v74-v1.md"
NOTE_SHA = "21bfbbd76dcd4dd5c5219054aa13ec6a93149c51fd48fc046385ca5acf3b8f10"
VERIF = "pilote-v1/verification-courte-candidat2-candidat3-preenregistrement-pilote-v1.md"
VERIF_SHA = "f3dc757ba38ace8d9b87b5e30b995e593c5ea57728daf0625781cd075dabf016"
MESSAGE = "« écris le message pour la nouvelle mère ; va regarder les prix toi meme, ecris candidat 4 »"


def main():
    c3, sortie, debut = sys.argv[1:4]
    if os.path.exists(sortie):
        sys.exit("REFUS : sortie existante (R12)")
    b = open(c3, "rb").read()
    if hashlib.sha256(b).hexdigest() != C3_SHA:
        sys.exit("REFUS : empreinte du candidat 3")
    t = b.decode("utf-8")
    n_r = [0]

    def r(old, new, n=1):
        k = t.count(old)
        if k != n:
            sys.exit(f"REFUS : « {old[:90]} » présent {k} fois, {n} attendu(s)")
        n_r[0] += 1
        return t.replace(old, new)

    # --- titre, statut, en-tête --------------------------------------------------------------------------------------------
    t = r("— v1, candidat 3 (compte organisme)", "— v1, candidat 4 (compte organisme)")
    t = r("""**Statut : candidat au scellement, « scellable après la phrase de Lazar sur les prix et la vérification courte » (R1) ; jamais
scellé par son auteur.** Nom neuf (R12) : le candidat 2""",
          """**Statut : candidat au scellement, « scellable après la vérification courte du différentiel candidat 3 → candidat 4 et
l'inscription, par la mère, de la lecture des prix publics à la place de la console » (R1) ; jamais scellé par son auteur.** Nom neuf
(R12) : le candidat 3 (`preenregistrement-pilote-conditionnelles-v1-candidat3-compte-organisme.md`, `539cf171…`) reste versé,
inchangé ; ce candidat 4 y porte la lecture des prix publics des quatre relais et les quatre constats mineurs de la vérification
courte du candidat 3 (table « Changements depuis le candidat 3 »). Le candidat 2""")
    t = r("""**Aucune course, aucun appel du pilote, aucune dépense du pilote** avant la phrase de Lazar sur les prix lus à la console, la
vérification courte de ce candidat, le scellement par `controle_ia.prereg.sceller_prereg` et les lignes de GO du pilote inscrites.""",
          """Les prix publics des quatre relais sont lus et rapprochés du relevé (aucun au-dessus de la configuration). **Aucune course,
aucun appel du pilote, aucune dépense du pilote** avant la vérification courte de ce candidat, l'inscription de la lecture des prix
par la mère, le scellement par `controle_ia.prereg.sceller_prereg` et les lignes de GO du pilote inscrites.""")
    t = r("""- **Heures** : début et fin de la rédaction du candidat 3 : dernière ligne (`date -u`, relevés par la commande qui l'écrit).

## Changements depuis le candidat 2""",
          f"""- **Heures** : début et fin de la rédaction du candidat 4 : dernière ligne (`date -u`, relevés par la commande qui l'écrit).

## Changements depuis le candidat 3

| # | décision, fait, mot ou constat | ce que fait le candidat 4 | où |
|---|---|---|---|
| message tapé dans le compte organisme | {MESSAGE} | prix publics lus par le rédacteur sur les pages officielles des trois fournisseurs, rapprochés des coûts du relevé (note `{NOTE}`, `{NOTE_SHA[:8]}…`) ; **remplace la lecture de la console par Lazar** (préalable 3) : à inscrire par la mère ; marqueur PRIX-CONSOLE levé | Devis ; Préalables ; Ordre ; Métrique ; Marqueurs |
| vérification courte du candidat 3, constat 1 | en-tête de la table des proposeurs resté au mot d'avant la sonde | « confirmée par la sonde v74 » | Dessin |
| idem, constat 2 | nom de famille d'un modèle écrit | « jamais sur la lignée du proposeur `fable52` » | Contre-lecture |
| idem, constat 3 | causes d'arrêt de la garde v74 tirées du code | origine dite (code v74, rapport du développeur §2 ; R-2738 ne nomme que le champ) | Liste d'arrêt |
| idem, constat 4 | table « Changements depuis le candidat 2 » incomplète | ligne « autres mots » ajoutée à cette table | Changements depuis le candidat 2 |
| vérification courte du candidat 3 | « scellable après la phrase de Lazar sur les prix » ; 0 bloquant, 0 majeur, 4 mineurs | entrée écrite ; vérification courte du différentiel candidat 3 → candidat 4 à faire | Contre-lecture ; Documents |

## Changements depuis le candidat 2""")
    t = r("""| réserve (R4) | sous les mêmes consignes, `argon` n'a pas réfléchi à la sonde v73 et a réfléchi à la sonde v74 | dite au dessin et à la métrique : le choix de réfléchir varie d'un appel à l'autre ; sous la règle « ajoutée », une réflexion absente est sans effet sur le coût compté | Dessin ; Métrique |""",
          """| réserve (R4) | sous les mêmes consignes, `argon` n'a pas réfléchi à la sonde v73 et a réfléchi à la sonde v74 | dite au dessin et à la métrique : le choix de réfléchir varie d'un appel à l'autre ; sous la règle « ajoutée », une réflexion absente est sans effet sur le coût compté | Dessin ; Métrique |
| autres mots (ligne ajoutée au candidat 4, constat 4 de la vérification courte) | lanceur v74 nommé ; état « fait / à faire » des étapes ; heures de rédaction | « En dix lignes » 9 et 10 ; Ordre ; Plan d'analyse (lanceur v74) ; section Contre-lecture ; ligne des heures | En dix lignes ; Ordre ; Plan d'analyse ; Contre-lecture |""")

    # --- documents ---------------------------------------------------------------------------------------------------------
    t = r("""| candidat 2 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat2-compte-organisme.md` | `640b2f556108647d4af362ac4d1aae652d0453b4c7fa7455987038cd2ed5c797` |""",
          f"""| candidat 2 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat2-compte-organisme.md` | `640b2f556108647d4af362ac4d1aae652d0453b4c7fa7455987038cd2ed5c797` |
| candidat 3 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat3-compte-organisme.md` | `{C3_SHA}` |
| vérification courte du différentiel candidat 2 → candidat 3 | `{VERIF}` | `{VERIF_SHA}` |
| **lecture des prix publics** des quatre relais, rapprochés des coûts du relevé v74 (pages des fournisseurs versées ou extraites, programme et sortie à côté) | `{NOTE}` (branche `lot/compte-organisme-v1`) | `{NOTE_SHA}` |""")

    # --- dessin (constat 1) ------------------------------------------------------------------------------------------------
    t = r("réflexion comptée dans la sortie (règle gelée, à confirmer par la sonde) |",
          "réflexion comptée dans la sortie (règle gelée, confirmée par la sonde v74) |")

    # --- ordre -------------------------------------------------------------------------------------------------------------
    t = r("""(fait) → bloc gelé définitif (`bloc --releve-sonde RELEVE`) recopié ici (fait) → prix lus par Lazar → vérification courte de ce
candidat → texte scellé → lignes π1 et π2 inscrites →""",
          """(fait) → bloc gelé définitif (`bloc --releve-sonde RELEVE`) recopié ici (fait) → prix publics lus et rapprochés (fait ; lecture
à inscrire par la mère) → vérifications courtes (candidat 2 → 3 : faite ; candidat 3 → 4 : à faire) → texte scellé → lignes π1 et
π2 inscrites →""")

    # --- métrique ----------------------------------------------------------------------------------------------------------
    t = r("""  réflexion ». Le coût de chaque appel est calculé aux prix de la configuration par la commande ; le rapprochement avec la console
  est fait par Lazar, hors du code.""",
          """  réflexion ». Le coût de chaque appel est calculé aux prix de la configuration par la commande ; il est rapproché, hors du code,
  des prix publics des fournisseurs (lecture de la sonde v74 : note des prix) ; le montant réellement facturé n'est lu que sur les
  consoles des comptes.""")

    # --- liste d'arrêt (constat 3) -----------------------------------------------------------------------------------------
    t = r("""  pilote** (code 3), l'appel porté au relevé partiel, sa dépense comptée une fois.""",
          """  pilote** (code 3), l'appel porté au relevé partiel, sa dépense comptée une fois (R-2738 nomme le champ de réflexion ; les deux
  autres conditions sont celles du code v74, rapport du développeur, section 2).""")

    # --- préalables --------------------------------------------------------------------------------------------------------
    t = r("""(3) **à faire** : prix lus par Lazar à
la console, rapprochés des coûts du relevé ; **si un prix réel d'entrée ou de sortie dépasse celui de la configuration v12 : nœud de
la mère, aucun scellement** (les pires cas et les parts ne seraient plus des bornes ; une configuration neuve demande un code qui la
nomme et une sonde neuve) ;""",
          f"""(3) **fait, à inscrire par la mère** : prix lus,
non à la console mais sur les pages publiques des trois fournisseurs, par le rédacteur, sur le message tapé dans le compte organisme
{MESSAGE} (note `{NOTE_SHA[:8]}…`) : `fable52` 8 / 40, `opus55` 4 / 20, `astra` 10 / 50 (contexte court) USD par million, égaux à la
configuration ; `argon` 2 / 10 jusqu'au 30 novembre 2026, 4 / 20 à partir du 1er décembre, au-dessous de la configuration (10 / 50) ;
**aucun prix public d'entrée ou de sortie au-dessus de celui de la configuration v12** (règle gardée : sinon nœud de la mère, aucun
scellement, une configuration neuve demandant un code qui la nomme et une sonde neuve) ; coûts du relevé égaux aux prix de la
configuration recalculés pour les huit appels ; aux prix publics, la sonde aurait coûté 0,056092 USD (0,099132 au relevé) ; le montant
réellement facturé n'est pas lu ;""")
    t = r("""du candidat 1 faite ; **à faire** : vérification courte du différentiel candidat 2 → candidat 3 par un lecteur neuf d'un autre modèle
que le rédacteur ;""",
          """du candidat 1 faite ; vérification courte du différentiel candidat 2 → candidat 3 faite (« scellable après la phrase de Lazar sur
les prix », 0 bloquant, 0 majeur, 4 mineurs, portés ici) ; **à faire** : vérification courte du différentiel candidat 3 → candidat 4
par un lecteur neuf d'un autre modèle que le rédacteur ;""")

    # --- devis -------------------------------------------------------------------------------------------------------------
    t = r("""de jetons, ces deux derniers barème prudent **supposé** ; prix réels : console lue par Lazar).""",
          """de jetons, ces deux derniers barème prudent **supposé** ; prix publics lus le 14 novembre : égaux pour `fable52`, `opus55` et
`astra`, au-dessous pour `argon`, note des prix).""")
    t = r("""| **0,099132** (calculé ; console à lire) |""",
          """| **0,099132** (calculé aux prix de la configuration ; 0,056092 aux prix publics) |""")
    t = r("""Prix lus par Lazar à la console après la sonde : [PRIX-CONSOLE].""",
          f"""Prix après la sonde : lus sur les pages publiques des fournisseurs, non à la console (préalable 3 ; note `{NOTE_SHA[:8]}…`) ;
aucun au-dessus de la configuration.""")

    # --- contre-lecture (constat 2) ----------------------------------------------------------------------------------------
    t = r("""- **Vérification courte du différentiel candidat 2 → candidat 3** (code v74 porté, bloc gelé recopié, lignes de la sonde
  recopiées, marqueurs levés) : à faire sur ce texte, avant le scellement, par un lecteur neuf d'un autre modèle que le rédacteur
  (jamais sur le modèle Fable avant le 20 novembre 15:00 UTC) ; rapport `pilote-v1/verification-courte-candidat2-candidat3-preenregistrement-pilote-v1.md`,
  à côté de ce texte, avec le texte relu et son empreinte.""",
          f"""- **Vérification courte du différentiel candidat 2 → candidat 3** (code v74 porté, bloc gelé recopié, lignes de la sonde
  recopiées, marqueurs levés) : lecteur neuf, modèle E, autre modèle que le rédacteur (modèle A) ; texte relu `{C3_SHA}` ; rapport
  `{VERIF}` (`{VERIF_SHA}`) ; verdict « scellable après la phrase de Lazar sur les prix », 0 bloquant, 0 majeur, 4 mineurs, portés au
  candidat 4 (table « Changements depuis le candidat 3 »).
- **Vérification courte du différentiel candidat 3 → candidat 4** (prix publics, constats mineurs) : à faire sur ce texte, avant le
  scellement, par un lecteur neuf d'un autre modèle que le rédacteur (jamais sur la lignée du proposeur `fable52` avant le 20 novembre
  15:00 UTC) ; rapport `pilote-v1/verification-courte-candidat3-candidat4-preenregistrement-pilote-v1.md`, à côté de ce texte, avec le
  texte relu et son empreinte.""")

    # --- marqueurs ---------------------------------------------------------------------------------------------------------
    old_m = t[t.index("Liste écrite, complète : tout autre marqueur entre crochets est un défaut (hors de la table"):t.index("Levés au candidat 3 :")]
    t = r(old_m, """Liste écrite, complète : **aucun marqueur ne reste** ; tout marqueur entre crochets est un défaut (hors de la table
« Changements depuis le candidat 1 », qui en garde l'histoire).

""")
    t = r("""GO-S1, GO-S2, DATE-GO, MOT-LAZAR-GO (lignes inscrites, recopiées mot pour
mot).""", f"""GO-S1, GO-S2, DATE-GO, MOT-LAZAR-GO (lignes inscrites, recopiées mot pour
mot). Levé au candidat 4 : PRIX-CONSOLE (prix publics lus, note `{NOTE_SHA[:8]}…`, préalable 3 ; lecture à inscrire par la mère).""")

    # --- heures ------------------------------------------------------------------------------------------------------------
    old_h = t[t.index("Rédaction du candidat 3 : début"):]
    t = r(old_h, f"Rédaction du candidat 4 : début {debut} UTC ; fin @@FIN@@ UTC (`date -u`).\n")

    # --- contrôles ---------------------------------------------------------------------------------------------------------
    a, b = t.index("## Changements depuis le candidat 1"), t.index("## Changements depuis le brouillon 4")
    restants = sorted(set(re.findall(r"\[[A-Z][A-Z0-9-]{3,}\]", t[:a] + t[b:])))
    if restants:
        sys.exit(f"REFUS : marqueurs restants {restants}")
    if re.search(r"\bFable\b", t[:a] + t[b:]):
        sys.exit("REFUS : nom de famille de modèle restant")
    if "(règle gelée, à confirmer par la sonde)" in t:
        sys.exit("REFUS : « à confirmer par la sonde » restant")
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(t)
    print(f"{n_r[0]} remplacements comptés ; aucun marqueur restant")


if __name__ == "__main__":
    main()
