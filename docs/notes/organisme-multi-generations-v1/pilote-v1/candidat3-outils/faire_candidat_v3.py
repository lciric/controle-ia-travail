"""Écrit le candidat 3 du préenregistrement du pilote MR-2 depuis le candidat 2 (R12 : fichier neuf ; le candidat 2 reste en place).

Remplacements comptés : chaque texte visé doit être présent exactement le nombre de fois dit, sinon refus et rien n'est écrit.
Entrées : candidat 2 (empreinte exigée), bloc gelé définitif rendu par `bloc --releve-sonde` du lanceur v74 (empreinte exigée),
les deux lignes de la sonde v74 inscrites sur `main` (`6db34425`, l. 329 et 330 ; empreinte exigée). Aucun réseau.

Usage : python3 -I faire_candidat_v3.py CANDIDAT2 BLOC LIGNES SORTIE DEBUT_UTC
"""
import hashlib
import os
import sys

C2_SHA = "640b2f556108647d4af362ac4d1aae652d0453b4c7fa7455987038cd2ed5c797"
BLOC_SHA = "8b5dcfe7a9f8e382469fc4638a2cbf18a99e1a9d8f449ffe5bf02e543f6618ec"
LIGNES_SHA = "30e500629b52002ffc230f72c0fa65f537871ebb5804c0fb271b3e78a3a640ee"
RELEVE = "f56d9c0e14ca1f36ac3d9d226c1e5f763731fcc697ad780ea35c483ccf85d529"


def lire(chemin, sha):
    with open(chemin, "rb") as f:
        b = f.read()
    if hashlib.sha256(b).hexdigest() != sha:
        sys.exit(f"REFUS : empreinte de {chemin} ≠ {sha}")
    return b.decode("utf-8")


def main():
    c2_chemin, bloc_chemin, lignes_chemin, sortie, debut = sys.argv[1:6]
    if os.path.exists(sortie):
        sys.exit("REFUS : sortie existante (R12)")
    t = lire(c2_chemin, C2_SHA)
    bloc = lire(bloc_chemin, BLOC_SHA).rstrip("\n")
    lignes = lire(lignes_chemin, LIGNES_SHA).rstrip("\n")
    compte = []

    def r(old, new, n=1):
        k = t.count(old)
        if k != n:
            sys.exit(f"REFUS : « {old[:90]} » présent {k} fois, {n} attendu(s)")
        compte.append((old[:60], n))
        return t.replace(old, new)

    # --- titre, statut, en-tête -------------------------------------------------------------------------------------------
    t = r("— v1, candidat 2 (compte organisme)", "— v1, candidat 3 (compte organisme)")
    t = r("""**Statut : candidat au scellement, « scellable après la sonde » (R1) ; jamais scellé par son auteur.** Nom neuf (R12) : le candidat 1
(`preenregistrement-pilote-conditionnelles-v1-candidat1-compte-organisme.md`, `48065053…`) reste versé, inchangé ; il porte les
corrections de sa contre-lecture (table « Changements depuis le candidat 1 »). Le""",
          """**Statut : candidat au scellement, « scellable après la phrase de Lazar sur les prix et la vérification courte » (R1) ; jamais
scellé par son auteur.** Nom neuf (R12) : le candidat 2 (`preenregistrement-pilote-conditionnelles-v1-candidat2-compte-organisme.md`,
`640b2f55…`) reste versé, inchangé ; ce candidat 3 y porte le code v74, la sonde v74 jouée, son bloc gelé définitif recopié et les
lignes de la sonde inscrites (table « Changements depuis le candidat 2 »). Le candidat 1
(`preenregistrement-pilote-conditionnelles-v1-candidat1-compte-organisme.md`, `48065053…`) reste versé, inchangé ; le candidat 2 a
porté les corrections de sa contre-lecture (table « Changements depuis le candidat 1 »). Le""")
    t = r("""cités) et les **v72 et v73** de ce compte (configuration v12 : consignes de la sonde écrites pour faire réfléchir ; conclusion
« réflexion observée » ; v73, décision de la mère R-2690 : bloc gelé qui nomme les proposeurs par leurs clés, sans identifiant de
modèle), parce que la sonde v71 (R-2621) a rendu Argon « indéterminé » et n'a pas confirmé la configuration v11. **Aucune
course, aucun appel, aucune dépense** avant la sonde v72 jouée sous ses lignes, le bloc gelé définitif recopié ici, la
contre-lecture de ce candidat, le scellement par `controle_ia.prereg.sceller_prereg` et les lignes de GO du pilote inscrites.""",
          """cités) et les **v72, v73 et v74** de ce compte (configuration v12 : consignes de la sonde écrites pour faire réfléchir ; conclusion
« réflexion observée » ; v73, décision de la mère R-2690 : bloc gelé qui nomme les proposeurs par leurs clés, sans identifiant de
modèle ; v74, option (a) de Lazar, R-2738 : pour `argon`, « aucune réflexion cachée » vaut règle sans effet sur le coût, et le
pilote s'arrête si un champ de réflexion lui apparaît), parce que la sonde v71 (R-2621) a rendu Argon « indéterminé » et n'a pas
confirmé la configuration v11, et que la sonde complète v73 l'a trouvé sans réflexion. **La sonde v74 est jouée** (une fois, sous
GO-2026-11-14-10 et -11 ; relevé `f56d9c0e…` ; toutes les conclusions exigées vraies) et son bloc gelé définitif est recopié ici.
**Aucune course, aucun appel du pilote, aucune dépense du pilote** avant la phrase de Lazar sur les prix lus à la console, la
vérification courte de ce candidat, le scellement par `controle_ia.prereg.sceller_prereg` et les lignes de GO du pilote inscrites.""")
    t = r("""- **Rédacteur** : modèle A (session du compte organisme). **Conflit dit** : je suis aussi le développeur des codes v72 et v73 que ce texte
  gèle.""", """- **Rédacteur** : modèle A (session du compte organisme). **Conflit dit** : je suis aussi le développeur des codes v72, v73 et v74 que ce
  texte gèle, et celui qui a joué les sondes.""")
    t = r("""est au bloc gelé. Le bloc gelé que rend le code v73 ne porte **aucun identifiant de modèle** (R-2690)""",
          """est au bloc gelé. Le bloc gelé que rend le code v74 (comme celui de la v73) ne porte **aucun identifiant de modèle** (R-2690)""")
    t = r("""- **Heures** : début et fin de la rédaction du candidat 2 : dernière ligne (`date -u`, relevés par la commande qui l'écrit).

## Changements depuis le candidat 1""",
          """- **Heures** : début et fin de la rédaction du candidat 3 : dernière ligne (`date -u`, relevés par la commande qui l'écrit).

## Changements depuis le candidat 2

| # | décision, fait ou mot | ce que fait le candidat 3 | où |
|---|---|---|---|
| R-2727 | candidat 2 reçu par la mère ; phrase de fin de liste d'arrêt gardée, option (a) | la mention « à confirmer par la mère » devient « gardée par la mère (R-2727, option (a)) » | Liste d'arrêt |
| R-2727, R-2728, R-2731 | sonde complète v73 jouée une fois (GO-2026-11-14-07 et -08 ; relevé `35afab77…`, 0,079262 USD) : `argon` sans réflexion aux deux appels (`thoughtsTokenCount` absent, total = entrée + sortie), règle non confirmable ; bloc refusé | relevé cité (documents ; dépenses déjà faites) ; ce relevé ne sert pas au mode réel | Documents ; Devis ; Préalables |
| mot de Lazar, R-2738 | option (a) : « code v74, réflexion absente sans effet » | **code v74** (module de la sonde v74, lanceur v74), paquet `1cda2feb…` ; **lanceur v74 gelé** ; règle de la sonde pour `argon` : règle confirmée **ou** « aucune réflexion cachée » ; garde du pilote pour un proposeur dit « sans réflexion » | Code ; Métrique ; Liste d'arrêt ; Préalables |
| GO-2026-11-14-10, -11 | lignes de la sonde v74 inscrites sur `main` (`6db34425`), mot pour mot | recopiées mot pour mot ; marqueurs GO-S1, GO-S2, DATE-GO, MOT-LAZAR-GO levés | Lignes de GO ; Marqueurs |
| sonde v74 | jouée une fois (13:38:30Z → 13:39:09Z) ; relevé `f56d9c0e…`, complet ; 0,099132 USD calculés ; toutes les conclusions exigées vraies ; `argon` a réfléchi à la borne gelée (786 jetons), règle « non comprise » confirmée ; aucun proposeur « sans réflexion » | **bloc gelé définitif recopié tel quel** ; marqueurs BLOC-GELE-V73 et RELEVE-SONDE-V72 levés ; chiffres mesurés au devis | Code ; Documents ; Devis ; Préalables |
| R-2731 | réponses brutes et relevé avec identifiants servis : restent sur la branche du compte, jamais recopiés tels quels dans `main` | le « point porté à la mère » devient la règle tranchée | Marqueurs |
| réserve (R4) | sous les mêmes consignes, `argon` n'a pas réfléchi à la sonde v73 et a réfléchi à la sonde v74 | dite au dessin et à la métrique : le choix de réfléchir varie d'un appel à l'autre ; sous la règle « ajoutée », une réflexion absente est sans effet sur le coût compté | Dessin ; Métrique |

## Changements depuis le candidat 1""")

    # --- documents --------------------------------------------------------------------------------------------------------
    t = r("""| relevé de la sonde v72 (à jouer) | dossier de la sonde, versé entier | [RELEVE-SONDE-V72] |""",
          """| **code du pilote v74 (ce compte)** : paquet de l'organisme contre `e7daf32`, tête `605e0f6` (ajouts seuls depuis la v73) | `pilote-v1/code-v74-compte-organisme/organisme-v74-pilote-mr2-compte-organisme-v1.bundle` (branche `prep/pilote-mr2-compte-organisme-v1`) | `1cda2feb88e297d758bed7d0bb30d93cbe9b196ac3ab789826d39cfa4506d48b` (les empreintes de ses fichiers sont au bloc gelé) |
| rapport du développeur v74 ; contre-lecture du code v74 ; relecture courte du jalon 3 | `pilote-v1/code-v74-compte-organisme/rapport-developpeur-code-pilote-v74-v1.md` ; `…/contre-lecture-code-pilote-v74-v1.md` ; `…/relecture-courte-jalon3-code-pilote-v74-v1.md` | `59d4db3dd38ee802548ed2d5f7261d1bd3993a6ee0ad637be8e6d6a22c7925ce` ; `d82de0532d78b83b6ca7a1097bc75a5d4734e51870f57e1e03a5c5f7c0a4e348` ; `895e776c5b67c989d3fbe341373aeb8202a4479f88a34ede8d30b9c27058dda4` |
| devis, commande et lignes de la sonde v74 | `pilote-v1/code-v74-compte-organisme/devis-et-lignes-sonde-complete-v74-v1.md` | `0426930a342d276cddcd501007667dbae9581109098c39d3c24bcb35ba29dac9` |
| relevé de la sonde complète v73 (jouée une fois, refusée au bloc : `argon` sans réflexion) | `pilote-v1/sonde-complete-v73-compte-organisme/sonde-complete-v73/releve-sonde-pilote-v72.json` (branche `lot/compte-organisme-v1`) | `35afab77d93b382f247ce3d854dab6caeefa601679373c766c86c632a8475962` |
| **relevé de la sonde v74** (jouée une fois, sous GO-2026-11-14-10 et -11 ; celui que le mode réel lit) | `pilote-v1/sonde-complete-v74-compte-organisme/sonde-complete-v74/releve-sonde-pilote-v74.json`, dossier de la sonde versé entier à côté (branche `lot/compte-organisme-v1`) | `f56d9c0e14ca1f36ac3d9d226c1e5f763731fcc697ad780ea35c483ccf85d529` |
| bloc gelé définitif rendu par `bloc --releve-sonde` du lanceur v74 | `pilote-v1/sonde-complete-v74-compte-organisme/bloc-releve-sonde-complete-v74.txt` | `8b5dcfe7a9f8e382469fc4638a2cbf18a99e1a9d8f449ffe5bf02e543f6618ec` (recopié tel quel à la section « Code ») |
| candidat 2 (gardé) | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat2-compte-organisme.md` | `640b2f556108647d4af362ac4d1aae652d0453b4c7fa7455987038cd2ed5c797` |""")

    # --- en dix lignes ----------------------------------------------------------------------------------------------------
    t = r("""   9,36, machine 3,00) ; **sonde v72 avant le scellement : 8,05 USD au pire** (s1 4,39 ; s2 3,68) ; ≈ 14,90 attendus pour le
   pilote, moins de 0,85 USD pour la sonde (estimés).""",
          """   9,36, machine 3,00) ; ≈ 14,90 attendus (estimés) ; **sonde v74 jouée avant le scellement** : 0,099132 USD calculés (pire
   8,05 ; s1 4,39 ; s2 3,68).""")
    t = r("""10. **Code** : C-1 à C-18 écrits (codes v68 à v71, v72 et v73 de ce compte), essayés, contre-lus ; **lanceur v73 gelé**, bloc gelé
    recopié après la sonde v72, qui doit confirmer la configuration v12 (règles de comptage de la réflexion comprises).""",
          """10. **Code** : C-1 à C-18 écrits (codes v68 à v71, v72 à v74 de ce compte), essayés, contre-lus ; **lanceur v74 gelé** ; la sonde v74
    a confirmé la configuration v12 (règles de comptage de la réflexion comprises) ; son bloc gelé définitif est recopié ici.""")

    # --- dessin -----------------------------------------------------------------------------------------------------------
    t = r("""  gelé ; le relevé de la sonde v72 confirme l'identifiant servi de chacun (règles M-1 et d-6 de la commande).""",
          """  gelé ; le relevé de la sonde v74 (`f56d9c0e…`) a confirmé l'identifiant servi de chacun (règles M-1 et d-6 de la commande).""")
    t = r("""par carte) ; la réflexion compte dans la sortie chez `fable52`, `opus55` et `astra`, elle s'y ajoute chez `argon` (règles gelées,
  à confirmer par la sonde, qui éprouve aussi que la borne est dure : sortie comptée au plus la borne courte) ;""",
          """par carte) ; la réflexion compte dans la sortie chez `fable52`, `opus55` et `astra`, elle s'y ajoute chez `argon` (règles gelées,
  confirmées par la sonde v74, qui a éprouvé aussi que la borne est dure : sortie comptée au plus la borne courte ; `argon` choisit
  de réfléchir ou non d'un appel à l'autre, sans réglage envoyé : sous sa règle « ajoutée », une réflexion absente est sans effet
  sur le coût compté) ;""")

    # --- ordre ------------------------------------------------------------------------------------------------------------
    t = r("""Sonde v72 jouée une fois sous ses deux lignes (registre des lancements), relevé et dossier versés, prix lus par Lazar →
bloc gelé définitif (`bloc --releve-sonde RELEVE`) recopié ici → contre-lecture → texte scellé → lignes π1 et π2 inscrites →""",
          """Sonde v74 jouée une fois sous ses deux lignes (GO-2026-11-14-10 et -11 ; registre des lancements), relevé et dossier versés
(fait) → bloc gelé définitif (`bloc --releve-sonde RELEVE`) recopié ici (fait) → prix lus par Lazar → vérification courte de ce
candidat → texte scellé → lignes π1 et π2 inscrites →""")
    t = r("""**`mesurer` du lanceur v73 (programme `mesure_pilote_v4.py`), une seule fois, sur les mondes du manifeste**""",
          """**`mesurer` du lanceur v74 (programme `mesure_pilote_v4.py`), une seule fois, sur les mondes du manifeste**""")

    # --- métrique ---------------------------------------------------------------------------------------------------------
    t = r("""- **Réflexion et coût** (secondaires, aucune issue ; D-2, A-1, v72) : la sortie comptée de chaque appel suit la règle gelée de son
  proposeur (`reflexion_comprise`), que la sonde v72 doit confirmer avant le scellement.""",
          """- **Réflexion et coût** (secondaires, aucune issue ; D-2, A-1, v72, v74) : la sortie comptée de chaque appel suit la règle gelée de
  son proposeur (`reflexion_comprise`), confirmée par la sonde v74 avant le scellement (relevé `f56d9c0e…`).""")
    t = r("""  mode réel refuse (« champ de réflexion absent »). Le coût de chaque appel est calculé aux prix de la configuration par la
  commande ; le rapprochement avec la console est fait par Lazar, hors du code.""",
          """  mode réel refuse (« champ de réflexion absent »). Pour `argon` seulement (v74, option (a) de Lazar), l'état « aucune réflexion
  cachée » (aucun champ de réflexion aux deux appels et total = entrée + sortie) vaut aussi : la règle est alors sans effet sur le
  coût, et le pilote s'arrête si un champ de réflexion lui apparaît. À la sonde v74 : `argon` a réfléchi à la borne gelée (786
  jetons, sortie visible 8, total 863 = 69 + 8 + 786 : deux votes « non comprise », égal à la règle) et non à la borne courte ;
  `astra` « comprise » (61 sur 72, puis 256 sur 256) ; `fable52`, `opus55` « sans champ » ; aucun proposeur n'est dit « sans
  réflexion ». Le coût de chaque appel est calculé aux prix de la configuration par la commande ; le rapprochement avec la console
  est fait par Lazar, hors du code.""")

    # --- plan d'analyse ---------------------------------------------------------------------------------------------------
    t = r("""2. Lancer **une seule fois** la sous-commande `mesurer --sortie DOSSIER --mondes MONDES.json --mondes-sha256 H` du lanceur v73""",
          """2. Lancer **une seule fois** la sous-commande `mesurer --sortie DOSSIER --mondes MONDES.json --mondes-sha256 H` du lanceur v74""")

    # --- liste d'arrêt ----------------------------------------------------------------------------------------------------
    t = r("""- Mode réel sans relevé de la sonde v72 valide (fait sous ce code et cette configuration, complet, conclusions toutes vraies,
  faits égaux à leurs pièces), ou dont l'empreinte n'est pas celle du bloc gelé de ce texte → refus avant tout dossier (D-4, a-2).""",
          """- Mode réel sans relevé de la sonde v74 valide (fait sous ce code et cette configuration, complet, conclusions toutes vraies,
  faits égaux à leurs pièces), ou dont l'empreinte n'est pas celle du bloc gelé de ce texte → refus avant tout dossier (D-4, a-2).
- Proposeur que le relevé dit « sans réflexion » (v74 ; aucun au relevé `f56d9c0e…`) : un champ de réflexion dans l'usage brut
  d'un de ses appels, une réflexion comptée non nulle, ou (pour `argon`) un total d'usage différent de entrée + sortie → **arrêt du
  pilote** (code 3), l'appel porté au relevé partiel, sa dépense comptée une fois.""")
    t = r("""  jamais réutilisés ; nœud de Lazar ; toute reprise demande un texte neuf, scellé, et des mondes neufs (ajout du candidat 2,
  à confirmer par la mère : il touche la lecture).""",
          """  jamais réutilisés ; nœud de Lazar ; toute reprise demande un texte neuf, scellé, et des mondes neufs (ajout du candidat 2,
  gardé par la mère, R-2727, option (a)).""")

    # --- code -------------------------------------------------------------------------------------------------------------
    t = r("## Code : écrit et gelé (v68 à v73)", "## Code : écrit et gelé (v68 à v74)")
    t = r("""que le développeur) et **codes v72 et v73** de ce compte (configuration v12, lecture v72, module de la sonde v72, lanceur v72 puis v73 ; rapport
du développeur ; contre-lectures par un autre modèle que le développeur). Le **lanceur gelé est `demonstrations/pilote_mr2_v73.py`** ;""",
          """que le développeur) et **codes v72 à v74** de ce compte (configuration v12, lecture v72, modules de la sonde v72 et v74, lanceurs v72,
v73 puis v74 ; rapports du développeur ; contre-lectures par un autre modèle que le développeur ; v74 : 147 essais passés, les 115 de
la v71 passent sur la même tête, banc de 54 mutations toutes tuées pour la raison attendue et G10 tuée). Le **lanceur gelé est
`demonstrations/pilote_mr2_v74.py`** ;""")
    t = r("""| C-11, C-13, C-14, C-18 | `demonstrations/pilote_mr2_v73.py` (sous-commandes `jouer`, `mesurer`, `lire`, `relire`, `rapatrier`, `bloc`, `sonde`), `pole/audit_pilote_v70.py` |
| sonde (D-4, A-1, A-2, a-1 à a-3, v72) | `pole/sonde_pilote_v71.py` et `pole/sonde_pilote_v72.py` |""",
          """| C-11, C-13, C-14, C-18 | `demonstrations/pilote_mr2_v74.py` (sous-commandes `jouer`, `mesurer`, `lire`, `relire`, `rapatrier`, `bloc`, `sonde`, `sonde-un`), `pole/audit_pilote_v70.py` |
| sonde (D-4, A-1, A-2, a-1 à a-3, v72, v74) | `pole/sonde_pilote_v71.py`, `pole/sonde_pilote_v72.py` et `pole/sonde_pilote_v74.py` |""")
    t = r("diffère de celui que rend le code présent avec ce relevé.\n\n[BLOC-GELE-V73]\n",
          "diffère de celui que rend le code présent avec ce relevé.\n\n" + bloc + "\n")

    # --- préalables -------------------------------------------------------------------------------------------------------
    old_pre = t[t.index("**Avant le scellement** : (1) code v73 écrit"):t.index("**Avant le premier appel du pilote**")]
    t = r(old_pre, """**Avant le scellement** : (1) **fait** : code v74 écrit, essayé (147 essais v74 passés ; les 115 de la v71 passent sur la même
tête), bancs de mutations (v72, 72 sur 73 tuées, N18 reciblée en N18b ; v73, 35 sur 35 après reciblage de B03 ; v74, 54 sur 54 et
G10), paquet scellé, contre-lu par un autre modèle que son développeur (« autorisable pour la sonde complète v74 ») ; (2) **fait** :
**sonde v74 jouée une seule fois** sous GO-2026-11-14-10 et -11 (section « Lignes de GO »), par la commande de la pièce de devis
(`0426930a…`, lanceur v74), depuis la session du compte organisme, clés passées par leur nom sous `env -i`, 2026-11-14 13:38:30Z →
13:39:09Z, code 0 ; registre des lancements consigné (une ligne neuve, module v74) ; **relevé et dossier entier de la sonde versés**
(relevé `f56d9c0e…`, pièces des huit appels, journaux des relais, ligne du registre des lancements) ; avant elle : sonde complète
v73 jouée une fois (GO-2026-11-14-07 et -08, relevé `35afab77…`, refusée au bloc : `argon` sans réflexion), et crédit du compte du
fournisseur d'Astra **vérifié par appel** (sonde du seul relais Astra, GO-2026-11-14-02, relevé
`40eb7b325da757c2ef7ec87afed0ce8ee6b89d8b973cf9201c63b406b7c6f599`, 0,0167 USD, R-2712 ; relevé versé :
`docs/notes/organisme-multi-generations-v1/pilote-v1/sonde-un-astra-v73-compte-organisme/sonde-un-astra-v73/releve-sonde-un-relais-v73.json`,
branche `lot/compte-organisme-v1`) ; ces deux relevés ne remplacent pas celui de la sonde v74 ; (3) **à faire** : prix lus par Lazar à
la console, rapprochés des coûts du relevé ; **si un prix réel d'entrée ou de sortie dépasse celui de la configuration v12 : nœud de
la mère, aucun scellement** (les pires cas et les parts ne seraient plus des bornes ; une configuration neuve demande un code qui la
nomme et une sonde neuve) ; (4) **fait** : le relevé confirme la configuration v12 (toutes les conclusions exigées vraies pour les
quatre relais, `reflexion_observee` comprise pour `argon` et `astra`, règle de comptage confirmée par les votes pour l'un et l'autre)
et `bloc --releve-sonde RELEVE` (code 0) a rendu le bloc gelé définitif, recopié tel quel à la section « Code » ; (5) contre-lecture
du candidat 1 faite ; **à faire** : vérification courte du différentiel candidat 2 → candidat 3 par un lecteur neuf d'un autre modèle
que le rédacteur ; (6) scellement par `controle_ia.prereg.sceller_prereg`.

""")

    # --- devis ------------------------------------------------------------------------------------------------------------
    t = r("""| poste (USD) | attendu | pire |
|---|---|---|
| **sonde v72, ligne s1** (crédits de Claude) : `fable52` (borne gelée 64 000 puis 256 jetons) | < 0,40 | 2,588224 (part 2,59) |
| sonde v72, s1 : `opus55` (89 000 puis 256) | < 0,20 | 1,794112 (part 1,80) |
| **sonde v72, ligne s2** (hors crédits) : `argon` (36 000 puis 256) | < 0,20 | 1,835280 (part 1,84) |
| sonde v72, s2 : `astra` (36 000 puis 256) | ≈ 0,02 (mesuré à la sonde d'un relais : 0,0167) | 1,835280 (part 1,84) |
| **sonde, total** (s1 4,39 ; s2 3,68) | < 0,85 | **8,052896** (lignes 8,07) |""",
          """| poste (USD) | attendu (sonde : calculé au relevé v74) | pire |
|---|---|---|
| **sonde v74, ligne s1** (GO-2026-11-14-10, crédits de Claude) : `fable52` (borne gelée 64 000 puis 256 jetons) | 0,018728 (calculé) | 2,588224 (part 2,59) |
| sonde v74, s1 : `opus55` (89 000 puis 256) | 0,009504 (calculé) | 1,794112 (part 1,80) |
| **sonde v74, ligne s2** (GO-2026-11-14-11, hors crédits) : `argon` (36 000 puis 256) | 0,0538 (calculé) | 1,835280 (part 1,84) |
| sonde v74, s2 : `astra` (36 000 puis 256) | 0,0171 (calculé) | 1,835280 (part 1,84) |
| **sonde v74, total** (s1 4,39 ; s2 3,68) | **0,099132** (calculé ; console à lire) | **8,052896** (lignes 8,07) |""")
    t = r("""| **sonde et pilote** | < 15,75 | **49,79** (lignes) |
| dépenses déjà faites (hors de ces lignes) : sonde v71 (R-2621, 1,865848 comptés, réelle attendue ≈ 0,03) ; sonde du seul relais Astra (R-2712, 0,0167 calculés) | — | — |""",
          """| **sonde v74 et pilote** | ≈ 15,00 | **49,79** (lignes) |
| dépenses déjà faites (hors des lignes du pilote et de la sonde v74) : sonde v71 (R-2621, 1,865848 comptés, réelle attendue ≈ 0,03) ; sonde du seul relais Astra (R-2712, 0,0167 calculés) ; sonde complète v73 (GO-2026-11-14-07 et -08, R-2731, 0,079262 calculés) | — | — |""")
    t = r("""il n'est pas borné par la borne gelée.""",
          """il n'est pas borné par la borne gelée. À la sonde v74, aucun coût au-dessus du pire cas (conclusion `au_dessus_du_pire_cas`
fausse pour les quatre relais).""")

    # --- lignes de GO -----------------------------------------------------------------------------------------------------
    old_go = t[t.index("Sonde v72 (avant le scellement ; les lignes GO-2026-11-13-04"):t.index("Pilote (après le scellement) :")]
    t = r(old_go, """Sonde v74 (avant le scellement), **inscrites** sur `main` (`6db34425`, `registres/go.md`, l. 329 et 330), recopiées mot pour
mot, **servies une fois** (relevé `f56d9c0e…`) et ne se reprennent pas. Lignes servies avant elles, sans reprise : GO-2026-11-13-04
et -05 (sonde v71), GO-2026-11-14-02 (sonde du seul relais Astra), GO-2026-11-14-07 et -08 (sonde complète v73) :

```
""" + lignes + """
```

""")
    t = r("""citant le relevé de la sonde complète (module v72, lanceur v73) ; code v73 du pilote contre-lu et gelé ;""",
          """citant le relevé de la sonde complète (module v74, lanceur v74) ; code v74 du pilote contre-lu et gelé ;""")
    t = r("## Lignes de GO proposées, mot pour mot, non inscrites", "## Lignes de GO : sonde inscrites et servies ; pilote proposées, non inscrites")

    # --- contre-lecture ---------------------------------------------------------------------------------------------------
    t = r("""- **Vérification courte du différentiel candidat 2 → texte à sceller** (corrections portées, bloc gelé recopié, marqueurs levés) :
  à faire après la sonde, par un lecteur neuf d'un autre modèle que le rédacteur ; texte relu, rapport et empreintes.""",
          """- **Vérification courte du différentiel candidat 2 → candidat 3** (code v74 porté, bloc gelé recopié, lignes de la sonde
  recopiées, marqueurs levés) : à faire sur ce texte, avant le scellement, par un lecteur neuf d'un autre modèle que le rédacteur
  (jamais sur le modèle Fable avant le 20 novembre 15:00 UTC) ; rapport `pilote-v1/verification-courte-candidat2-candidat3-preenregistrement-pilote-v1.md`,
  à côté de ce texte, avec le texte relu et son empreinte.""")

    # --- marqueurs --------------------------------------------------------------------------------------------------------
    old_m = t[t.index("Liste écrite, complète : tout autre marqueur entre crochets est un défaut."):t.index("Les deux lignes du pilote restent proposées")]
    t = r(old_m, """Liste écrite, complète : tout autre marqueur entre crochets est un défaut (hors de la table « Changements depuis le candidat 1 »,
qui en garde l'histoire). Le seul qui reste attend **la phrase de Lazar** :

| marqueur | attend | levé par |
|---|---|---|
| [PRIX-CONSOLE] | la lecture des prix à la console par Lazar | la phrase de Lazar sur les prix lus à la console, rapprochés des coûts du relevé `f56d9c0e…` |

Levés au candidat 3 : BLOC-GELE-V73 (bloc que rend `bloc --releve-sonde RELEVE` du lanceur v74, recopié tel quel), RELEVE-SONDE-V72
(empreinte du relevé v74, égale à celle du bloc gelé), GO-S1, GO-S2, DATE-GO, MOT-LAZAR-GO (lignes inscrites, recopiées mot pour
mot).

""")
    t = r("""**R-2598, tranché par la mère (R-2690, option b)** : le bloc gelé que rend le lanceur v73 nomme les proposeurs par leurs""",
          """**R-2598, tranché par la mère (R-2690, option b)** : le bloc gelé que rend le lanceur v74 (comme le v73) nomme les proposeurs par leurs""")
    old_pt = t[t.index("**Point porté à la mère** : le **relevé de la sonde**"):t.index("Rédaction du candidat 2 : début")]
    t = r(old_pt, """**Pièces brutes de la sonde, tranché par la mère (R-2731)** : le relevé de la sonde et les pièces de ses appels (réponses brutes,
corps des relais) portent par nature l'identifiant **servi** de chaque modèle ; ils restent sur la branche du compte organisme,
jamais recopiés tels quels dans `main` ; ce texte ne les recopie pas (il ne cite que l'empreinte du relevé).

""")
    old_h = t[t.index("Rédaction du candidat 2 : début"):]
    t = r(old_h, f"Rédaction du candidat 3 : début {debut} UTC ; fin @@FIN@@ UTC (`date -u`).\n")

    # --- contrôles --------------------------------------------------------------------------------------------------------
    import re
    a, b = t.index("## Changements depuis le candidat 1"), t.index("## Changements depuis le brouillon 4")
    restants = sorted(set(re.findall(r"\[[A-Z][A-Z0-9-]{3,}\]", t[:a] + t[b:])))
    if restants != ["[PRIX-CONSOLE]"]:
        sys.exit(f"REFUS : marqueurs restants {restants}")
    if t.count(RELEVE) != 2:
        sys.exit(f"REFUS : empreinte entière du relevé {t.count(RELEVE)} fois (attendue deux : documents et bloc gelé)")
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(t)
    print(f"{len(compte)} remplacements comptés ; marqueurs restants {restants}")


if __name__ == "__main__":
    main()
