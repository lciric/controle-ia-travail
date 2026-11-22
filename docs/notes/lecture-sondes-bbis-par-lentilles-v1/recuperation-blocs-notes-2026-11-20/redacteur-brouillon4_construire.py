# Bâtisseur (bloc-notes du rédacteur du brouillon 4) : écrit le script des couples, autonome, à partir du brouillon 3.
# Usage : python -I construire.py <brouillon3> <critere_v8> <script_de_sortie> <heure_de_fin> <egales> <reecrites>
import hashlib, re, sys

B3, CI, SORTIE, FIN, EGALES, REECRITES = sys.argv[1:7]
texte = open(B3, encoding="utf-8").read()
assert hashlib.sha256(texte.encode("utf-8")).hexdigest() == "1bfac4672e27e07ff8680e7be70c28f79dd921d0eccdc00ce873b8af467c47c7"
lignes = texte.split("\n")


def L(a, b):
    """Texte des lignes a à b du brouillon 3 (numéros depuis 1, bornes comprises), saut de ligne final compris."""
    return "\n".join(lignes[a - 1:b]) + "\n"


C = []  # (identifiant, tâche, lieu, avant, après)


def couple(ident, tache, lieu, avant, apres):
    C.append((ident, tache, lieu, avant, apres))


# ------------------------------------------------------------------ phrases de CI, vérifiées contre le fichier scellé
ci = re.sub(r"\s+", " ", open(CI, encoding="utf-8").read())
P1_DEUX = ("« Les fichiers d'ajustement réajustés sont identiques à l'octet à ceux du 18 novembre (empreintes …) ; les mesures du "
           "18 novembre décrivent ces lentilles. »")
P1_UNE = ("« Le fichier d'ajustement réajusté de la lentille [R | S] est identique à l'octet à celui du 18 novembre (empreinte …) ; "
          "les mesures du 18 novembre faites sur cette lentille la décrivent. »")
P2_DEUX = ("« Les deux lentilles mesurées le 18 novembre ont été détruites avec la machine louée. Nous les avons réajustées avec le "
           "même code d'ajustement, le même corpus et les mêmes graines sur une autre machine. Les fichiers obtenus ne sont pas "
           "identiques à l'octet. Deux comparaisons restent possibles. La différence entre les deux moitiés du corpus, couche par "
           "couche, s'écarte d'au plus [écart mesuré] de celle du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³) ; "
           "cette grandeur ne voit pas un déplacement commun aux deux moitiés. Pour la lentille R seulement, l'écart maximal de "
           "chaque matrice à la lentille publique et à l'identité change d'au plus [valeur] et [valeur] d'une course à l'autre, "
           "pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était fixé d'avance pour ces deux "
           "séries, et ces changements sont un plancher, non un plafond, de l'écart maximal, entrée par entrée, entre les matrices "
           "des deux courses. Pour la lentille S, aucune comparaison de ce genre n'existe. Nous ne savons pas si les lentilles "
           "réajustées lisent comme celles du 18 novembre. Les mesures du 18 novembre [n'ont pas été refaites sur elles | ont été "
           "refaites sur elles et sont rapportées à côté]. »")
P2_R_DEBUT = ("« La lentille R mesurée le 18 novembre a été détruite avec la machine louée. Nous l'avons réajustée avec le même code "
              "d'ajustement, le même corpus et les mêmes graines sur une autre machine. Le fichier obtenu n'est pas identique à "
              "l'octet. La différence entre les deux moitiés du corpus, couche par couche, s'écarte d'au plus [écart mesuré] de "
              "celle du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un déplacement "
              "commun aux deux moitiés. ")
P2_R_SERIES = ("L'écart maximal de chaque matrice à la lentille publique et à l'identité change d'au plus [valeur] et [valeur] d'une "
               "course à l'autre, pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était fixé "
               "d'avance pour ces deux séries, et ces changements sont un plancher, non un plafond, de l'écart maximal, entrée par "
               "entrée, entre les matrices des deux courses. ")
P2_R_FIN = ("Nous ne savons pas si la lentille réajustée lit comme celle du 18 novembre. Les mesures du 18 novembre [n'ont pas été "
            "refaites sur elle | ont été refaites sur elle et sont rapportées à côté]. »")
P2_R = P2_R_DEBUT + P2_R_SERIES + P2_R_FIN
P2_S_REMPLACE = "Aucune autre comparaison n'existe pour cette lentille."
P2_S = P2_R_DEBUT.replace("« La lentille R mesurée", "« La lentille S mesurée") + P2_S_REMPLACE + " " + P2_R_FIN
P_AUTRE = "« Lentille [R | S] : verdict d'identité « [libellé exact] » ; elle n'est pas lue ici. »"
for nom, p in (("P1_DEUX", P1_DEUX), ("P1_UNE", P1_UNE), ("P2_DEUX", P2_DEUX), ("P2_R", P2_R), ("P_AUTRE", P_AUTRE),
               ("P2_S_REMPLACE", "« " + P2_S_REMPLACE + " »")):
    assert p in ci, nom          # chaque phrase recopiée est, à l'espacement près, dans le critère scellé
assert "Pour S seule : la même phrase, « La lentille S… », où la phrase des deux séries" in ci

H_ADD = "7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970"
H_ADD_B2 = "924d02989412700d6241d0e3663fd4914e462bc68560df345b8cdc1889f2813c"
H_CI = "541bb86b15088c5cea5a291a294cccdd1067fe39be995b7f9014661f96cb3940"
H_CI4 = "60df6c539f8aa0a04d5eec0c5b47a421bb780dc5ab8d0251c80ebfb06c67ccfa"
H_D9 = "064e735a8b98cb1bd76916d2514d98f6e5cf7d57e367b5b2dcfc6f0222b6bb41"
H_PROG = "4a0f3b2c8c73c282de3fbf7f18314e8085c7bbd03e4bb009c21775db78b09b01"
H_VERIF_ADD = "867983f3026af6d55dfdeb746f7431e2417aec4db00b5a4914adcd3cc430e88b"
H_VERIF_DIFF = "0113727274b047d58745969081289b7c230db45448080553cf0a4ee83e2cc146"
H_VERIF_CI8 = "caa7753edbab84f5e297268960c9cdfab4440048d764fc7dc23e5cf792d809bc"
H_BLOC = "4e1fe2d7aa76f4cefe717298f98c5368e33a1a5992743d48232c96b6785f5358"
H_MOT_GARDE = "dbd1e5140b987ed2067df7b0912c45f0d8606f424018bb3d669d3dfbb3f52fff"
H_MOT_GO = "9ac9ed2bf65596198f0c51a4a06564919dd58b89517262feae03599c18749f67"
H_MANDAT = "845eab686252a3a47f01eac645d39149a7f4b4377f1860ca6a18ebb0838a7f6d"
H_FREQ = "b1d0d47439be89d7380aa81c08f08ae83b0f92053b3dbefda27810e6be97d5b2"
H_FREQ_S = "26f4abba8e5816165b5cb01bdba969ff90af570791578967ac6c7d666cc02e74"
MAIN = "3a58d00832bdd211df976486ed26d02b57be9e55"
V_MOTS = "« la lecture prédit mal l'effet d'une activation en contexte jusqu'à la couche 14, la couche 15 est intermédiaire, bien tard »"

# ================================================================== K01 — bloc de tête du brouillon 4
BLOC = f"""## Brouillon 4 — différences avec le brouillon 3

- **Ce qu'est ce fichier** : le brouillon 3 (`prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon3.md`,
  `1bfac4672e27e07ff8680e7be70c28f79dd921d0eccdc00ce873b8af467c47c7`, archivé sans changement, R12) avec les changements des douze
  tâches du mandat de son rédacteur, et ce bloc. Fabriqué par programme : des couples (texte avant, texte après), chaque « avant »
  trouvé une fois et une seule dans le brouillon 3 ; contrôle par `diff` contre le brouillon 3. Pièces de fabrication, scellées, dans
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/` : `couples-brouillon3-vers-brouillon4-v1.py` (le script, qui porte chaque
  couple, sa tâche et son lieu), `sortie-couples-brouillon3-vers-brouillon4-v1.txt` (sa sortie) et
  `diff-brouillon3-vers-brouillon4-v1.txt` (le `diff`) ; leurs empreintes sont dans leurs compagnons (ce fichier ne peut pas porter
  l'empreinte d'une pièce qui le fabrique). **Tout le reste — en-têtes, déclarations d'auteur, dates et pieds des brouillons 1 à 3 —
  est inchangé et décrit le brouillon qu'il nomme.**
- **Auteur du brouillon 4** : rédacteur neuf, sous-agent de la session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`), modèle
  **Claude Fable 5.2** (`claude-fable-5-2`), sur le mandat
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-redacteur-texte-lecture-v2-brouillon4-v1.md`
  (`{H_MANDAT}`, section « Texte du mandat », seule lue), parti sur le mot de Lazar
  « go pour le brouillon 4, option 3 » (note `docs/notes/neuron-lens-v1/mot-lazar-go-redacteur-brouillon4-2026-11-19-v1.md`,
  `{H_MOT_GO}`). Il n'a écrit ni la v1, ni les brouillons 1 à 3 de la v2, ni le
  critère d'identité, ni le devis, ni l'addendum de concentration, ni aucune contre-lecture ou vérification ; il ne sera ni
  développeur, ni opérateur, ni lecteur de ce texte. Aucun commit, aucun push, aucune machine, aucune dépense, aucun modèle chargé ;
  aucun fichier existant modifié.
- **Heures (UTC, `date -u`)** : 2026-11-19 ; lecture des pièces à partir de 22:01:52 ; écriture à partir de 22:14:09 ; fin relevée au
  pied. Branche des lentilles `claude/brave-galileo-jhp684` à `8e28e20e3606ad80f6730ae545c9c7a9a182600d` ; branche principale
  récupérée à `{MAIN}` (daté 2026-11-19T22:03:05Z).
- **Pièces lues** : la section « Texte du mandat » du mandat ; `CLAUDE.md` ; le brouillon 3 en entier ; le critère d'identité
  version 8 en entier (`{H_CI}`) et, de sa version 4 (`60df6c53…`), les § 4 à § 8, pour comparer ; du devis version 9 (`064e735a…`),
  l'en-tête, les titres, le § 2, le point 3 du § 5 et les lignes des chiffres que ce texte cite ; du programme de comparaison
  version 4 (`4a0f3b2c…`), les lignes rendues par une recherche des noms de champs de sa sortie et de ses libellés ; de la
  contre-lecture 3 (`42024aa9…`), la correction B1 entière (douze lieux) et l'annexe B ; l'addendum de concentration, version finale
  (`7c738708…`) : en-tête, § 3 (EC-1 à EC-6), § 4, § 9, § 12 et § 12 bis ; sa vérification (`867983f3…`) : en-tête, conclusion, § 3
  et § 4 ; la vérification de son différentiel (`01137272…`), entière ; le rapport du lecteur désigné sur le bloc séparable
  (`4e1fe2d7…`), entier ; de la vérification du critère version 8 (`caa7753e…`), l'en-tête et la conclusion ; les deux notes des
  mots de Lazar (`9ac9ed2b…`, `dbd1e514…`) ; la sortie de la pièce d'appui sur la fréquence des égalités (`26f4abba…`) ; le
  validateur `src/controle_ia/prereg.py` (l. 1-75) et le début de `src/controle_ia/scellement.py` ; la v1 scellée (`ca5066d7…`)
  par le seul programme de contrôle de l'annexe B, sans lecture.
- **Expositions, déclarées** (R4) :
  - *V, le verdict scellé de la tranche de l'ajustement de nos lentilles* (`3a9b947e…`, lecture permise par le mandat) : ouvert par
    une recherche des mots « intermédiaire », « prédit mal » et « B-7 » ; lignes rendues, coupées à 900 caractères : 29, 30, 72,
    101, 131, 172, 173, 189 et 190 (lignes des mesures B-6 et B-7 : libellés, valeurs par couche de la lecture contre ablation,
    marges). Le reste de V n'a pas été ouvert. S'y ajoutent les valeurs de V que cite le rapport du lecteur désigné (toutes celles du
    bloc séparable). Toutes portent sur nos lentilles, aucune sur les sondes.
  - *Registres de la branche principale, par recherche de clés nommées* : du registre propre de la v1, les clés et les heures de ses
    trois lignes (`ABSENCE-VERDICT-LENTILLES-BBIS`, `SCELLEMENT-LENTILLES-BBIS`, `ADDENDUM-CONCENTRATION-LENTILLES-BBIS`) et la ligne
    entière de la troisième ; de `registres/scellements-v1.md`, les deux lignes `CRITERE-IDENTITE-REAJUSTEMENT-LENTILLES` et
    `DEVIS-REAJUSTEMENT-LENTILLES` ; de `registres/go.md`, les lignes GO-2026-11-19-47, -78, -40 et -42 ; de
    `registres/decisions.md`, les lignes que rendent les recherches de « GO-2026-11-19-47 », de « R-3929 », de « R-3819 » à
    « R-3821 » et de quelques mots (« option 2 », « texte v2 », « brouillon 3 ») : R-3368, R-3771, R-3786, R-3796, R-3819 à R-3821,
    R-3853, R-3860, R-3865, R-3878, R-3929, R-3930. Plusieurs de ces lignes parlent aussi d'autres chaînes (devis et modules du
    « bras A » de la relance des organismes discrets, organisme d'idéation) : noms, états et montants de devis seulement ; aucune
    aire, aucun score, aucune issue, aucun verdict d'une chaîne interdite n'y paraît.
  - *Chiffres vus sur données synthétiques* : ceux de l'addendum de concentration et de ses vérifications (fréquence des égalités,
    bancs sur matrices aléatoires).
- **Jamais ouverts** : aucun fichier de la liste « Jamais ouverts » de la v1 ; aucune sortie, aucun score, aucune table, aucune
  lecture, aucun verdict de l'apprentissage des sondes sur la tâche ; aucune table ni sortie de la lecture par la lentille publique ;
  aucune branche `donnees/*` ou `calcul/*` ; aucun fichier sous `diag/` ou `runs/` ; aucune sortie de P3, P3-bis, T0.6, T0.7, de
  l'étape B, du bras d'attaque ni du saboteur à budget ; ni le texte gelé de la tranche, ni le code voisin, ni la note de place.
  **Aucun choix de ce brouillon n'a pu être fait d'après une sortie de la chaîne des sondes.**
- **Refus d'outil** : état au pied du texte.

**Traitement des douze tâches du mandat**

| tâche | traitement | où |
|---|---|---|
| 1. alignement sur le critère d'identité version 8 | **faite.** « CI » désigne la version 8 scellée (chemin, empreinte, ligne du registre des scellements) ; « D » le devis version 9 scellé ; le programme de comparaison version 4 est cité par chemin et empreinte. Les douze lieux de B1 repris un à un contre la version 8 : (a) Documents : changé ; (b) vocabulaire : changé (procédure en points 0 à 6 ; libellé du premier palier avec reprise notée ; seconde course incomplète) ; (c) portée du verdict de la tranche : changé (premier palier en cas mixte) ; (d) fiche de rangement : changé (champs du programme version 4 ; déclencheurs ; achèvement de la seconde course ; la liste H1 à H7 n'existe plus) ; (e) condition de lecture : changé (audit ; reprise ; seconde course incomplète ; phrase par cas) ; (f) phrase de tête de la seconde passe : changé (six formes de phrases permises, mots de la version 8 ; verdict d'ensemble en cas mixte) ; (g) règles de la seconde passe : relu, **inchangé** (la version 8 n'y touche pas) ; (h) liste d'arrêt : changé ; (i) frontière : point 6 changé (cas mixte), points 13 et 14 relus, inchangés ; (j) nœud N12 : changé (version nommée ; seconde course incomplète) ; (k) lieux d'accord : table des changements, essais, lignes de registre, plan, point 1 : changés ; (l) « par gabarit » : relu, **inchangé** (CI, § 5, « Dans tous les cas », mêmes mots). **Renvois de paragraphes** : les § 1 à § 10 n'ont pas bougé de la version 4 à la version 8 ; seuls changent « procédure, points 1 à 5 » (désormais 0 à 6) et les deux renvois à la liste H (H5, H7), qui n'existe plus. **Écarts qui changent une règle** : ci-dessous. | Documents ; Vocabulaire ; Hypothèse ; Entrées ; Plan (1) ; Critères ; Liste d'arrêt ; Frontière (6) ; Lignes de registre ; Code neuf ; N12 |
| 2. écart sur la couche 15 | **faite**, aux deux endroits que nomme le rapport du lecteur désigné : la réserve (R-c) et la colonne « ce qui en suit » de la ligne « lecture contre ablation par fenêtre » du bloc séparable reprennent les mots de V, cités ; « intermédiaire » y est dit « au sens de V pour cette mesure », sans rapport avec le libellé de concentration. **Aucune valeur chiffrée ne bouge.** Couples exacts : pièces de fabrication, couples K14 et K16 | Hypothèse |
| 3. marqueur de la vérification du bloc séparable | **faite** : le marqueur est remplacé par sa déclaration datée (chemin, empreinte, conclusion « conforme », un écart en mots, renvoi à la tâche 2) ; porté par le rédacteur du brouillon 4, sur ordre de la session des lentilles, **à confirmer par la session principale** | Hypothèse, bloc séparable ; table des marqueurs |
| 4. les autres marqueurs | **faite** : table des marqueurs mise à jour (un porté, onze restants, dont deux ajoutés par ce brouillon) ; le marqueur du critère reste, à la session principale ; texte de déclaration proposé remis à la session des lentilles, hors de ce fichier ; bornes du bloc séparable intactes, une occurrence chacune (contrôle du script) | en-tête ; Documents |
| 5. la phrase « elle ne penche vers aucun libellé » | **faite** : remplacée par ce qui est vrai (validité des valeurs p gardée ; règle non neutre envers les familles ; effet de l'ordre de 10⁻⁵ par liste) | Métrique (6) |
| 6. règle de départage étendue aux listes de dix | **faite** : pôles par cosinus (indice de neurone croissant, puis signe + avant signe −) ; dix premiers jetons de chaque pôle, par toute lentille (même règle que pour les vingt) ; garde de la fonction de lecture : sa tolérance couvre déjà les égalités, raison écrite | Métrique (6, 7) ; Plan (5) |
| 7. option « permutation fixe des identifiants, tirée par graine » | **faite** : nœud N18, au format de décision, trois options, recommandation (a), identifiant croissant, confiance 0,65, sans défaut ; le texte porte la règle recommandée et dit le nœud ouvert ; un marqueur empêche le scellement avant le mot de Lazar | Nœuds (N18) ; Métrique (6) ; table des marqueurs |
| 8. essais de « Code neuf » | **faite** : statistique corrigée (concentration et part), ses deux arrêts (essais de l'addendum de concentration, EC-5, repris), règle de départage aux vingt et aux dix, pôles à cosinus égal, compte des égalités ; cas sain et artefact pour chacun | Code neuf |
| 9. table « Changements de la v1 à la v2 » | **faite** : lignes 20 à 24 ; le compte des lignes de la v1 touchées est rejoué et mis à jour (la statistique corrigée réécrit des lignes de la v1) | Changements |
| 10. citation de l'addendum de concentration | **faite** : version finale `7c738708…` et ses deux vérifications ; l'addendum est scellé et inscrit : ligne du registre propre citée, vérifiée par le rédacteur sur la branche principale ; **aucun marqueur** ; ordre écrit : la ligne de l'addendum précède toute ligne de la v2 (aucun autre ordre proposé) | bloc du brouillon 3, (a) ; Documents ; Plan (1) ; Liste d'arrêt ; Lignes de registre |
| 11. le mot de Lazar GO-2026-11-19-47 vaut-il pour la v2 | **cherché, non trouvé** : aucune ligne de `registres/go.md` ni de `registres/decisions.md` (branche principale, `3a58d008…`) ne dit que cette décision vaut pour la version 2 ; la ligne GO-2026-11-19-47 nomme le seul texte scellé de la v1 (R-3771). **Marqueur `MOT_DE_LAZAR_GO_47_POUR_LA_V2`** (nom sans chevrons), porté par la session principale | Nœuds (N19) ; table des marqueurs |
| 12. garde d'égalité au vingtième rang de la v1 | **faite**, le mot de Lazar étant donné au départ : option 3, la garde à trois étages écrite en EC-6 (GO-2026-11-19-78, R-3929) ; paragraphe « Lien avec la v1 » réécrit sous cette option, **sans marqueur** ; la ligne H2 de l'addendum (compte des paires de jetons de même ligne de sortie) suit le même mot : dite, non tranchée ici | bloc du brouillon 3, (b) ; Métrique (6) ; Plan (11) |

**Écarts de la version 8 du critère qui changent une règle que ce texte suit** (et pas seulement un numéro), avec leur raison et
leurs lieux. Le texte ne recopie du critère que ses libellés et ses phrases permises ; le reste est cité.

| écart | raison | lieux |
|---|---|---|
| E1. **Une phrase permise par cas.** La version 8 écrit la phrase du premier palier pour deux lentilles et pour une seule, celle du deuxième palier pour deux lentilles, pour R seule et pour S seule, et une phrase pour tout autre verdict. Le préfixe « Pour notre lentille [R / S] : » du brouillon 2, écrit faute de mieux pour le cas mixte, n'a plus d'emploi | CI, § 5 (pour le premier palier d'une seule lentille et pour les autres verdicts : couples 3 et 4 de la vérification de sa version 5, d'après son § 0.1) | Critères (phrase de tête) ; Entrées (condition de lecture) ; Code neuf (essais « phrases ») |
| E2. **Premier palier en cas mixte.** Si une seule lentille est au premier palier, seules les mesures faites sur elle la décrivent ; le verdict d'ensemble et les conditions communes aux deux lentilles ne se transportent pas tels quels | CI, § 5, tableau et premier alinéa | Hypothèse (portée du verdict) ; Critères (verdict d'ensemble, réserves) ; Frontière (6) |
| E3. **Seconde course incomplète.** En course rejouée, si la seconde course s'arrête avant la fin de ses mesures, une lentille au deuxième palier est traitée comme en ajustement seul : aucune lecture sans nœud de Lazar | CI, § 5 ; D, § 2 | Vocabulaire ; Entrées (condition, fiche) ; Plan (1) ; Critères ; Liste d'arrêt ; Code neuf ; N12 |
| E4. **Libellé du premier palier avec reprise.** Le programme ajoute « ; reprise sur sauvegarde notée » au libellé du premier palier ; le code de la seconde passe, qui arrête sur un libellé inconnu, doit le reconnaître | CI, § 4, mention 1 ; programme version 4 | Vocabulaire ; Entrées ; Liste d'arrêt ; Code neuf |
| E5. **Mots de la phrase du deuxième palier.** « le même code d'ajustement » (au lieu de « le même code ») ; « de l'écart maximal, entrée par entrée, entre les matrices des deux courses » (au lieu de « de l'écart entre les matrices des deux courses ») | CI, § 5 | Critères |
| E6. **Audit.** Il est dû dès que le programme rend un déclencheur, donc aussi au deuxième palier quand un déclencheur y est rendu ; le brouillon 2 ne l'exigeait qu'au premier palier (la version 4 portait déjà ces déclencheurs : c'est une lacune du brouillon 2 autant qu'un écart de version). La liste des contrôles H1 à H7 est remplacée par des préalables du programme et par les contrôles K1 à K5 : les deux champs de la fiche qui la citaient sont repris | CI, § 4, § 6 et § 7 | Entrées (condition, fiche) ; Liste d'arrêt ; Code neuf |

Sans effet sur une règle de ce texte : la procédure du critère en points 0 à 6 ; le second cas de la mention suspendue (octets
différents, écart sur `diffs` au-delà de 10⁻³) ; les préalables neufs et l'arrêt du programme sur une erreur (ils rendent des
libellés que ce texte traite déjà : lentille non lue).

**Occurrences de la version 4 du critère vues et laissées, avec leur raison** (numéros de ligne du brouillon 3) : lignes 174 à 182
et 208 à 211 (« Traitement de la contre-lecture 3 » : histoire du brouillon 2 ; une note de tête le dit) ; ligne 467 (demandes
faites au rédacteur du brouillon 2 : histoire) ; ligne 1974 (points signalés par le rédacteur du brouillon 2 : histoire) ; ligne
423 (ce que le rédacteur du brouillon 2 a lu). Le bloc du brouillon 3 est gardé, hors trois endroits : la citation de l'addendum
(tâche 10), le mot de Lazar (tâche 11, un renvoi) et « Lien avec la v1 » (tâche 12).

**Nœuds pour Lazar ouverts ou signalés par ce brouillon** : **N18**, règle de départage à score égal (ouvert, sans défaut ;
recommandation : identifiant croissant, confiance 0,65) ; **N19**, portée de la décision GO-2026-11-19-47 pour la seconde passe
(un marqueur, non un choix ouvert). Restent ouverts du brouillon 2 : N12 pour l'ajustement seul (étendu à la seconde course
incomplète), N17.

**Reste à faire après ce brouillon** : sa contre-lecture par un autre modèle (R2, R-3735), puis la vérification des corrections ;
les onze marqueurs ; le mot de Lazar sur N18 ; la confirmation, par la session principale, du marqueur porté à la tâche 3.

## Brouillon 3 — différences avec le brouillon 2
"""
couple("K01", "forme", "tête : bloc « Brouillon 4 », avant le bloc du brouillon 3",
       "## Brouillon 3 — différences avec le brouillon 2\n", BLOC)

# ================================================================== K02 — tâche 11, bloc du brouillon 3
couple("K02", "11", "bloc du brouillon 3, (a) : mot de Lazar",
       "donné pour le texte v1 ; **la session principale dit si ce mot couvre la version 2**). Le brouillon 2 gardait la statistique",
       "donné pour le texte v1 ; **la session principale dit si ce mot couvre la version 2** ; brouillon 4 : aucune ligne de registre\n"
       "  trouvée, marqueur porté au nœud N19). Le brouillon 2 gardait la statistique")

# ================================================================== K03 — tâche 10, bloc du brouillon 3
couple("K03", "10", "bloc du brouillon 3, (a) : citation de l'addendum de concentration",
       "concentration de la v1, version corrigée après sa contre-lecture :\n"
       "  `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,\n"
       f"  `{H_ADD_B2}` (**non encore scellée** : à vérifier par son contre-lecteur ;\n"
       "  l'empreinte de la version scellée est à reprendre ici avant le scellement de ce texte), noté « l'addendum de concentration ».",
       "concentration de la v1, **version finale, scellée** (citation reprise au brouillon 4) :\n"
       "  `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,\n"
       f"  `{H_ADD}`, noté « l'addendum de concentration » (clé\n"
       "  `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` du registre propre, 2026-11-19T16:35:35Z ; ses deux vérifications et sa ligne de\n"
       "  registre : « Documents »). Le brouillon 3 citait ici `924d0298…`, alors « non encore scellée », devenue depuis le brouillon 2\n"
       "  de l'addendum ; les passages repris (EC-1 à EC-3) sont identiques, à l'octet, dans les deux.")

# ================================================================== K04 — tâche 12, bloc du brouillon 3
couple("K04", "12", "bloc du brouillon 3, (b) : « Lien avec la v1 »",
       "**Lien avec la v1** : sous le texte scellé de la v1, l'addendum de concentration propose une\n"
       "  garde et non une règle (son EC-6, soumis à Lazar) ; si elle est retenue, une première passe menée à son terme n'a aucune égalité\n"
       "  au vingtième rang sur une direction lue, et aucun de ses libellés ne dépend du départage des directions nulles : la règle écrite\n"
       "  ici ne peut donc changer ni une liste de direction lue ni un libellé de la première passe.",
       "**Lien avec la v1** (réécrit au brouillon 4, le mot de Lazar étant donné) : sous le texte scellé de la v1, l'addendum de\n"
       "  concentration pose une garde et non une règle (son EC-6) ; **Lazar a retenu l'option 3, la garde à trois étages écrite en\n"
       "  EC-6** (GO-2026-11-19-78, R-3929). Une première passe menée à son terme n'a donc aucune égalité au vingtième rang sur une\n"
       "  direction lue, et aucun de ses libellés ne dépend du départage des directions nulles : la règle écrite ici ne peut changer ni\n"
       "  une liste de direction lue ni un libellé de la première passe. Paragraphe complet : « Métrique », point 6, « Lien avec la\n"
       "  première passe ».")

# ================================================================== K05 à K08 — tâche 1 (a), Documents
couple("K05", "1 (a), 4", "Documents : critère d'identité", L(97, 103),
       f"""  - **critère d'identité du réajustement, version 8, scellé** (« **CI** » ; brouillon 4),
    `docs/notes/neuron-lens-v1/devis-reajustement/critere-identite-reajustement-lentilles-v8.md`,
    `{H_CI}` ; ligne `CRITERE-IDENTITE-REAJUSTEMENT-LENTILLES` de
    `registres/scellements-v1.md` (branche principale, 2026-11-19T13:03:14Z ; R-3819) : **il prime sur le devis et sur ce texte pour
    tout ce qui touche l'identité** ; ses libellés et ses phrases permises sont recopiés ici mot pour mot, le reste est cité. **Ce
    texte n'est scellé que si l'empreinte du critère scellé est celle citée ici.** Sa version 4
    (`…/devis-reajustement/critere-identite-reajustement-lentilles-v4.md`,
    `{H_CI4}`), contre laquelle le brouillon 2 était écrit, reste archivée ; les
    numéros de ses paragraphes sont ceux de la version 8. Ses contre-lectures, ses vérifications et son scellement :
    <<CONTRE_LECTURE_ET_SCELLEMENT_DU_CRITERE>> ;
""")
couple("K06", "1 (a)", "Documents : devis", L(104, 109),
       f"""  - devis du réajustement, **version 9, scellé** (« **D** » ; brouillon 4),
    `…/devis-reajustement/devis-reajustement-lentilles-b-beta-v9.md`,
    `{H_D9}` ; ligne `DEVIS-REAJUSTEMENT-LENTILLES` du même registre, même
    heure (§ 1, § 2 les deux variantes, § 3 durées et coût, § 4 statut de la seconde mesure, § 5 préalables, § 6 lieu L2, § 7
    décisions ; mêmes numéros et mêmes chiffres de durée, de prix et de plafond que la version 4 que citait le brouillon 2, relus
    dans la version 9 par le rédacteur du brouillon 4) ; ses versions 1 à 8 et l'erratum de la version 2 restent archivés ;
    vérification de la différence entre ses versions 1 et 2,
    `…/devis-reajustement/verification-difference-devis-reajustement-v1-v2.md`,
    `3cc64c86e3bec7a7ee8d9e9ca8b70725093aa0e3740d263d836cf802d6855073` (« VD » ; lue par le rédacteur du brouillon 1) ;
""")
couple("K07", "1 (a)", "Documents : programme de comparaison", L(110, 113),
       f"""  - **programme de comparaison du réajustement, version 4**, celui que cite CI, § 7, et lui seul, scellé avec le critère
    (R-3819) : `src/controle_ia/neuron_lens/comparer_reajustement_v4.py`,
    `{H_PROG}` ; ses essais,
    `tests/test_neuron_lens_comparer_reajustement_v4.py`, `e1708b3932601b4bf4d8e5c1c55703879c2d186333ea83828311a748cf1192ee`
    (empreintes recalculées sur la branche principale par le rédacteur du brouillon 4). Il rend, par lentille, la mention du
    programme, ses déclencheurs et les chiffres que la fiche de rangement recopie (« Entrées », nos lentilles) ;
""")
couple("K08", "10, 3, 12", "Documents : pièces ajoutées par le brouillon 4",
       "`42024aa938d00df2a728dd7bd709df7fef4a4af3ad450329a434e08a2a98cb6c`.\n- **Décisions de Lazar reçues pendant l'écriture**",
       f"""`42024aa938d00df2a728dd7bd709df7fef4a4af3ad450329a434e08a2a98cb6c` ;
  - **addendum de concentration de la v1, version finale, scellée** (ajout du brouillon 4) :
    `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
    `{H_ADD}`. **Ligne du registre propre**
    (`registres/lecture-sondes-bbis-par-lentilles-v1.md`, branche principale ; relevée par le rédacteur du brouillon 4 au commit
    `{MAIN}`, portée par le commit `bc4bdbbc7a272e8df7917d8cc95834f5f1ba8285`) :
    `| ADDENDUM-CONCENTRATION-LENTILLES-BBIS | 2026-11-19T16:35:35Z | prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md | {H_ADD} |` ;
    scellé par la session principale après le mot de Lazar sur la garde d'égalité (R-3929). **Ses deux vérifications**, du même
    contre-lecteur (Opus 5.5), sur la branche principale : celle de la version corrigée, qui est aussi la contre-lecture entière
    de la garde d'égalité, `docs/notes/lecture-sondes-bbis-par-lentilles-v1/verification-addendum-concentration-v1.md`,
    `{H_VERIF_ADD}` (« Scellable après ces couples exacts » ; son § 3 porte six
    points sur le brouillon 3 de ce texte, traités au brouillon 4) ; celle du différentiel de la version finale,
    `docs/notes/lecture-sondes-bbis-par-lentilles-v1/verification-differentiel-addendum-concentration-v1.md`,
    `{H_VERIF_DIFF}` (« Scellable tel quel »). L'empreinte `924d0298…` que citait le
    brouillon 3 est désormais celle du **brouillon 2 de l'addendum**
    (`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1-brouillon2.md`, inchangé d'un octet) ; les écarts EC-1
    à EC-5 et le § 7 de l'addendum, d'où viennent les mots repris ici, sont identiques à l'octet dans les deux (comparés par le
    rédacteur du brouillon 4) ;
  - **décision de Lazar sur la garde d'égalité au vingtième rang de la v1** : option 3, la garde à trois étages écrite en EC-6 de
    l'addendum ; mot « option 3 pour la garde, relance les tests sans limite », note
    `docs/notes/neuron-lens-v1/mot-lazar-garde-egalite-vingtieme-rang-2026-11-19-v1.md`,
    `{H_MOT_GARDE}` ; ligne GO-2026-11-19-78 de `registres/go.md` et R-3929 de
    `registres/decisions.md` (branche principale, lues par le rédacteur du brouillon 4) ;
  - pièce d'appui de la fréquence des égalités (données synthétiques) :
    `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/frequence_egalite_vingtieme_rang_v1.py`,
    `{H_FREQ}`, et sa sortie
    `sortie-frequence-egalite-vingtieme-rang-v1.txt`, `{H_FREQ_S}` ;
  - **rapport du lecteur désigné par Lazar sur le bloc séparable** (Opus 4.6 ; GO-2026-11-19-39 et -42) :
    `docs/notes/lecture-sondes-bbis-par-lentilles-v1/verification-bloc-v/rapport-verification-bloc-v-v1.md`,
    `{H_BLOC}` (« BLOC-V conforme », un écart en mots : « Hypothèse ») ;
  - vérification du critère d'identité version 8 et du devis version 8 (branche principale) :
    `docs/notes/neuron-lens-v1/verification-critere-v8-devis-v8-v1.md`,
    `{H_VERIF_CI8}` (« Critère d'identité v8 : scellable »).
- **Décisions de Lazar reçues pendant l'écriture**""")

# ================================================================== K09 — tâches 3, 4, 7, 11 : table des marqueurs
couple("K09a", "4", "en-tête, table des marqueurs : ligne du critère", L(166, 166),
       "  | CONTRE_LECTURE_ET_SCELLEMENT_DU_CRITERE | Documents | la session principale (**reste à porter** ; un texte de déclaration, "
       "avec chemins et empreintes relevés sur la branche principale, est proposé par le rédacteur du brouillon 4 et remis à la session "
       "des lentilles, hors de ce fichier) | chemins et empreintes des contre-lectures, des vérifications et du compagnon de scellement "
       "de CI version 8 ; sa ligne au registre des scellements ; empreinte de CI scellé égale à celle citée |\n")
couple("K09b", "3", "en-tête, table des marqueurs : ligne du bloc séparable", L(167, 167),
       "  | VERIFICATION_DU_BLOC_V — **porté au brouillon 4** | Hypothèse, bloc séparable | porté par le rédacteur du brouillon 4, sur "
       "ordre de la session des lentilles ; **à confirmer par la session principale** (décision de Lazar GO-2026-11-19-39, option (a) ; "
       "lecteur désigné : GO-2026-11-19-42) | chemin et empreinte du rapport scellé du lecteur désigné par Lazar (Opus 4.6), qui "
       "compare les valeurs du bloc et les réserves en mots au verdict de la tranche ; sa conclusion : conforme, un écart en mots, "
       "corrigé au brouillon 4 |\n")
couple("K09c", "4, 7, 11", "en-tête, table des marqueurs : lignes ajoutées et état",
       "chemin et empreinte de la pièce qui liste chaque changement du brouillon 2 à la version |\n",
       "chemin et empreinte de la pièce qui liste chaque changement du brouillon 2 à la version |\n"
       "  | MOT_DE_LAZAR_GO_47_POUR_LA_V2 (ajouté au brouillon 4) | Nœuds, N19 | la session principale | la ligne de registre, ou le mot "
       "de Lazar, qui dit que la décision GO-2026-11-19-47 (chaque direction nulle jugée sans elle-même), donnée pour le texte scellé "
       "de la v1, vaut pour la version 2 |\n"
       "  | MOT_DE_LAZAR_SUR_LA_REGLE_DE_DEPARTAGE (ajouté au brouillon 4) | Nœuds, N18 | la session principale, d'après le mot de Lazar "
       "| l'option que Lazar retient pour l'égalité de score (nœud sans défaut), avec sa ligne de registre ; si ce n'est pas l'option "
       "(a), le texte est repris avant le scellement |\n"
       "\n"
       "  **État des marqueurs au brouillon 4** : **un porté** (VERIFICATION_DU_BLOC_V, par le rédacteur du brouillon 4, à confirmer par\n"
       "  la session principale) ; **onze restent** : les neuf autres de la table du brouillon 2, portés par qui la table le dit\n"
       "  (la session principale pour sept, la session des lentilles pour un, qui écrit la version pour un), et les deux ajoutés par ce\n"
       "  brouillon, portés par la session principale. La pièce des différences du brouillon 2 à la version aura à lister aussi les\n"
       "  changements des brouillons 3 et 4, dont les pièces de fabrication existent.\n")

# ================================================================== K10 — tâche 1 : note de tête de l'histoire du brouillon 2
couple("K10", "1", "« Traitement de la contre-lecture 3 » : note de tête",
       "## Traitement de la contre-lecture 3 (du brouillon 1 au brouillon 2)\n\n",
       "## Traitement de la contre-lecture 3 (du brouillon 1 au brouillon 2)\n\n"
       "*Note du brouillon 4 : cette section est l'histoire du brouillon 2, écrit contre la version 4 du critère d'identité ; elle est\n"
       "gardée telle quelle. Partout ailleurs, « CI » désigne désormais la version 8, scellée ; les douze lieux de B1 sont repris\n"
       "contre elle (bloc « Brouillon 4 », tâche 1). Les numéros de paragraphe cités ici valent aussi pour la version 8. Le point (1)\n"
       "signalé en fin de section (cas mixte et phrase permise au pluriel) est réglé par la version 8, qui écrit une phrase par cas.*\n\n")

# ================================================================== K11, K34 — tâche 9 : table des changements
couple("K34", "9", "« Changements de la v1 à la v2 » : compte des lignes de la v1, rejoué",
       "d'écart** (« Plan d'analyse », point 1).\n",
       "d'écart** (« Plan d'analyse », point 1).\n"
       "\n"
       "**Mise à jour du brouillon 4** (contrôle rejoué par son rédacteur, avec le même programme, sur la v1 `ca5066d7…` et sur ce\n"
       f"brouillon). Depuis le brouillon 3, la correction de la statistique réécrit des lignes de la v1 : sur ses 814 lignes, {EGALES} sont\n"
       f"égales, aucune n'est supprimée, **10 sont prolongées** (les mêmes) et **{REECRITES} sont réécrites** : les cinq ci-dessus, et les lignes\n"
       "335 à 337 et 339 (« Métrique », point 6 : fin de la puce des vingt premiers jetons, concentration, part au-dessus du nul), 461\n"
       "et 465 à 467 (« Plan d'analyse », point 6 : calibration) — changements 20 et 21 de la table. Les mots « sans changement de sens\n"
       "pour la première passe » ne valent que pour les cinq premières ; **pour la première passe, le changement de statistique est\n"
       "porté par l'addendum de concentration de la v1, scellé, non par ce texte**, qui ne régit que la seconde passe.\n")
couple("K11", "9", "« Changements de la v1 à la v2 » : lignes 20 à 24 de la table",
       "| 19 | entrées 3 et 4 de contre-lecture | Contre-lecture | R2 |\n",
       "| 19 | entrées 3 et 4 de contre-lecture | Contre-lecture | R2 |\n"
       "| 20 | **statistique de la valeur p corrigée** (brouillon 3) : chaque direction nulle est jugée sans elle-même, pour la "
       "concentration et pour la part au-dessus du nul ; calibration : témoins jugés comme la direction lue, loi de référence dite "
       "approchée ; **lignes de la v1 réécrites** ; essais (brouillon 4) | Métrique (6) ; Plan (6) ; Code neuf | biais anti-conservateur "
       "de la statistique d'origine ; l'addendum de concentration de la v1, scellé, porte la même correction pour la première passe, "
       "que la seconde refait (décision de Lazar GO-2026-11-19-47, donnée pour la v1 ; sa portée pour la v2 : N19) |\n"
       "| 21 | **règle de départage à score égal** (brouillon 3 : listes de vingt, identifiant de jeton croissant), **étendue aux listes "
       "de dix** (brouillon 4 : jetons d'un pôle ; pôles par indice de neurone croissant, puis signe + avant signe −) ; ce qu'elle "
       "garde (validité des valeurs p) et ne garde pas (neutralité envers les familles) ; compte des égalités écrit ; lien avec la "
       "garde d'égalité de la première passe ; essais | Métrique (6, 7) ; Plan (5, 11) ; Code neuf ; N18 | la v1 ne disait rien de ce "
       "cas et le code laissait la fonction de tri décider ; vérification de l'addendum de concentration, § 3 ; le choix de la règle "
       "est un nœud ouvert (N18) |\n"
       "| 22 | **alignement sur le critère d'identité version 8, scellé**, et sur le devis version 9 (brouillon 4) : une phrase permise "
       "par cas ; premier palier en cas mixte ; seconde course incomplète traitée comme l'ajustement seul ; libellé du premier palier "
       "avec reprise notée ; audit dû dès qu'un déclencheur est rendu ; programme de comparaison version 4 cité | Documents ; "
       "Vocabulaire ; Hypothèse ; Entrées ; Plan (1) ; Critères ; Liste d'arrêt ; Frontière (6) ; Code neuf ; N12 | CI prime ; le "
       "brouillon 2 était écrit contre sa version 4 |\n"
       "| 23 | **couche 15** (brouillon 4) : la réserve (R-c) et la ligne « lecture contre ablation par fenêtre » du bloc séparable "
       "reprennent les mots de V (« intermédiaire » à la couche 15, au sens de V pour cette mesure) ; aucune valeur chiffrée changée ; "
       "le bloc séparable est déclaré vérifié | Hypothèse | rapport du lecteur désigné par Lazar (`4e1fe2d7…`) ; interdit du chiffre "
       "non vérifié |\n"
       "| 24 | **ordre des lignes de registre** (brouillon 4) : la ligne de l'addendum de concentration précède toute ligne de la v2 ; "
       "nœuds N18 (ouvert, sans défaut) et N19 (marqueur) | Plan (1) ; Liste d'arrêt ; Lignes de registre ; Nœuds | vérification de "
       "l'addendum de concentration, § 3, points 1 et 5 |\n")

# ================================================================== K12 — tâche 1 (b) : vocabulaire
couple("K12", "1 (b)", "Vocabulaire : verdict d'identité, variante de la course", L(527, 536),
       """- **Verdict d'identité** d'une de nos lentilles (ce texte dit aussi « mention d'identité ») : le verdict que prononce la session
  principale en appliquant CI à cette lentille (CI, § 4, procédure, points 0 à 6 ; § 8), écrit sur le fichier **rangé**. Ses
  libellés, recopiés de CI et jamais reformulés : « palier 1 — même lentille, octets identiques », que le programme de
  comparaison fait suivre de « ; reprise sur sauvegarde notée » quand une reprise lui est indiquée (CI, § 4, mention 1) — **seul
  ce palier établit l'identité** (CI, § 5) ; « palier 2 — différences entre moitiés concordantes à 10⁻³ près ; octets différents ;
  matrices non comparables » — l'identité n'est pas établie et le verdict du 18 novembre ne se transporte pas ; « différente » ;
  « non comparable (traitée comme différente) » ; « mention suspendue : anomalie (nœud de Lazar) » ; « R non réajustée », « S non
  réajustée ». La mention ne dit jamais « équivalente », « proche » ni, au deuxième palier, « même lentille » (CI, § 4).
- **Variante de la course** du réajustement (D, § 2) : **ajustement seul** (variante A : aucune mesure de la tranche n'est refaite)
  ou **course rejouée** (variante B : les mesures de la tranche sont refaites sur la machine neuve ; c'est la **seconde course**,
  lue par un lecteur neuf sur un plan scellé). La seconde course ne décide rien de l'identité. **Seconde course incomplète**
  (brouillon 4 ; CI, § 5 ; D, § 2) : arrêtée après des ajustements copiés, avant la fin de ses mesures ; une lentille au deuxième
  palier reste alors sans mesure propre et est traitée comme en ajustement seul.
""")

# ================================================================== K13 — tâche 1 (c) : portée du verdict de la tranche
couple("K13", "1 (c)", "Hypothèse : portée du verdict de la tranche", L(617, 619),
       """Verdict d'ensemble de la tranche : **« partiel »** (V, « Verdict, en mots simples »), accepté par Lazar. Il porte sur les lentilles
du 18 novembre, détruites. Il décrit une lentille réajustée **au premier palier seulement** ; au deuxième palier, il ne se
transporte pas, et ce qui suit est alors un rappel de contexte qui ne décrit pas la lentille lue (CI, § 5). **Si une seule de nos
deux lentilles est au premier palier** (brouillon 4 ; CI, § 5), seules les mesures faites sur elle la décrivent : le verdict
d'ensemble et les conditions qui portent sur les deux lentilles ensemble ne se transportent pas tels quels (« Critères », phrase
de tête de la seconde passe).
""")
couple("K13b", "3", "Hypothèse : réserves en mots, vérification par le lecteur désigné",
       "il recopie les mots de V et écrit l'écart en tête de sa description (« Plan d'analyse », point 8).\n",
       "il recopie les mots de V et écrit l'écart en tête de sa description (« Plan d'analyse », point 8).\n"
       "**Brouillon 4** : le lecteur désigné par Lazar a depuis comparé ces réserves à V (rapport `4e1fe2d7…`, « Documents ») : (R-a),\n"
       "(R-b), (R-d) et (R-e) sont conformes ; (R-c) disait « prédit mal » pour la couche 15, que V dit « intermédiaire » : elle est\n"
       "reprise ci-dessous dans les mots de V. La vérification par le lecteur de la seconde passe reste due.\n")

# ================================================================== K14, K16 — tâche 2 : couche 15
couple("K14", "2", "Hypothèse : réserve (R-c)",
       "- (R-c) aux couches 7 et 15, la lecture par R prédit mal l'effet en contexte ;\n",
       "- (R-c) lecture contre ablation par fenêtre, dans les mots de V (§ 2, ligne B-7) : " + V_MOTS + " ;\n"
       "  pour les couches de ce texte : à la couche 7, la lecture par R prédit mal l'effet en contexte ; **à la couche 15, V la dit\n"
       "  « intermédiaire »** — « intermédiaire » au sens de V pour cette seule mesure, sans rapport avec le libellé « intermédiaire »\n"
       "  de la lecture par concentration de ce texte (« Seuil ») ;\n")
couple("K16", "2", "Hypothèse, bloc séparable : ligne « lecture contre ablation par fenêtre », colonne « ce qui en suit »",
       "| aux couches 7 et 15, la lecture prédit mal ce qu'une activation fait en contexte (G, B-7) |",
       "| à la couche 7, la lecture prédit mal ce qu'une activation fait en contexte ; à la couche 15, V la dit « intermédiaire » "
       "(V, § 2, ligne B-7 : " + V_MOTS + " ; « intermédiaire » au sens de V pour cette mesure, la mesure B-7 de G, sans rapport avec "
       "le libellé « intermédiaire » de la lecture par concentration de ce texte) |")

# ================================================================== K15 — tâche 3 : état du bloc séparable
couple("K15", "3", "Hypothèse, bloc séparable : état et déclaration à la place du marqueur", L(641, 649),
       f"""> **État : vérifié par le lecteur désigné ; un écart en mots, corrigé au brouillon 4.** Ces valeurs ont été relevées dans V par le
> rédacteur du brouillon 1. La contre-lecture 3 n'a pas pu les comparer à V (B6 de son rapport) ; le rédacteur du brouillon 2 les
> a recopiées du brouillon 1 sans les vérifier ni les changer. Le dépôt interdit un chiffre non vérifié dans un préenregistrement.
> **Décision de Lazar** (GO-2026-11-19-39, option (a) ; mot « 1a, go recos », vers 10:57Z, R-3743, relayé par la session des
> lentilles ; nœud N16) : avant le scellement, un lecteur neuf, qui n'a écrit ni ce texte ni le critère d'identité, d'un autre
> modèle que le rédacteur du brouillon 2 (désigné par Lazar sur Opus 4.6, mot de 11:01Z ; GO-2026-11-19-42), compare chaque valeur
> de ce bloc, et chaque réserve en mots ci-dessus, à V (`3a9b947e…`).
> **Déclaration du 2026-11-19 (brouillon 4), écrite à la place du marqueur de la vérification du bloc.** Son rapport existe et est
> scellé : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/verification-bloc-v/rapport-verification-bloc-v-v1.md`,
> `{H_BLOC}` (lecteur sur Opus 4.6 ; rapport daté du 2026-11-19, 11:16 UTC ;
> il a lu le bloc dans le brouillon 2, `ff121bdd…`, lignes 587 à 623, bloc resté le même, à l'octet, dans le brouillon 3).
> Conclusion du rapport : **« BLOC-V conforme », avec un seul écart, non chiffré.** Toutes les valeurs chiffrées du bloc sont
> conformes à V ; les réserves (R-a), (R-b), (R-d) et (R-e) sont conformes ; la réserve (R-c) et la colonne « ce qui en suit » de
> la ligne « lecture contre ablation par fenêtre » disaient « prédit mal » pour la couche 15, que V dit « intermédiaire ». **Cet
> écart est corrigé au brouillon 4, aux deux endroits, dans les mots de V ; aucune valeur chiffrée ne bouge** (couples K14 et K16
> des pièces de fabrication du brouillon 4). Aucune valeur n'a été trouvée fausse. Déclaration portée par le rédacteur du
> brouillon 4, sur ordre de la session des lentilles ; **à confirmer par la session principale**, qui dit aussi si le lecteur
> désigné vérifie ce seul changement de mots. Le bloc reste séparable : il se supprime de sa ligne de début à sa ligne de fin,
> sans toucher au reste.
""")

# ================================================================== K18 à K20 — tâche 1 (d), (e) : condition de lecture, fiche
couple("K18", "1 (e)", "Entrées : condition de lecture", L(845, 877),
       """**Condition de lecture** (chaque lentille jugée séparément, CI, § 4 ; cas mixte permis, chaque lentille recevant la phrase de son
propre verdict, CI, § 5). Le verdict d'identité, les chiffres de la sortie du programme de comparaison, la liste de ses
déclencheurs et la variante de la course sont pris dans la **fiche de rangement** (ci-dessous), jamais recalculés ni reformulés
ici. **Seul le premier palier établit l'identité** (CI, § 5). **Audit** (brouillon 4 ; CI, § 6) : il est dû dès que la sortie du
programme rend au moins un déclencheur — toujours au premier palier (déclencheur (i)), et au deuxième quand un déclencheur y est
rendu ((ii) ou (vi)) ; une lentille dont l'audit est dû n'est lue que si la fiche le cite, versé scellé, sans contrôle manqué.
- **« palier 1 — même lentille, octets identiques »**, suivi ou non de « ; reprise sur sauvegarde notée » (CI, § 4, mention 1 :
  la reprise est notée dans le libellé, le palier reste le premier ; tout autre ajout au libellé : arrêt, forme mal comprise) :
  **lue**, si la fiche cite l'audit, toujours dû à ce palier, versé scellé, sans contrôle manqué ; sans cet audit : non lue
  (« Non lue : notre lentille [R / S] au premier palier sans audit versé »). Phrase de tête : la phrase permise du premier palier
  de CI, mot pour mot, dans la forme de son cas (« Critères »).
- **« palier 2 — différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables »**, variante
  **course rejouée, seconde course menée en entier** : **lue** (nœud N12 tranché, option (b), GO-2026-11-19-40) **seulement si**,
  avant le montage de la seconde passe, (1) CI est scellé à l'empreinte citée ; (2) la ligne
  `AVERTISSEMENT-PALIER-2-LENTILLES-BBIS` est inscrite (Lazar averti dans les termes de CI, § 5, chiffres de la sortie compris) ;
  (3) la ligne `LECTURE-SECONDE-COURSE-NOS-LENTILLES-BBIS` est inscrite (lecture de la seconde course par un lecteur neuf,
  scellée) ; (4) la fiche dit la seconde course **menée en entier** (CI, § 5 : « course rejouée en entier ») ; (5) si l'audit est
  dû, la fiche le cite. La lecture se fait **dans les limites de cette lecture** : la fiche recopie, mot pour mot, par lentille
  et par couche (7, 15, 23), la limite que la lecture de la seconde course écrit, ou « aucune limite écrite » ; une couche que cette
  lecture écarte n'est pas lue (« Non lue à la couche [ℓ] : [mots de la lecture de la seconde course] »). Phrase de tête : la phrase
  permise du deuxième palier de CI, mot pour mot, dans la forme de son cas, crochets remplis d'après la fiche, dernier crochet
  « ont été refaites sur [elle | elles] et sont rapportées à côté ».
- **Même mention, variante ajustement seul, ou course rejouée dont la seconde course est incomplète** (brouillon 4 : CI, § 5,
  traite la seconde course incomplète comme l'ajustement seul ; une fiche qui ne dit pas si la seconde course a été menée en
  entier est lue comme « incomplète ») : **non lue** (« Non lue : notre lentille [R / S] au deuxième palier, sans mesure
  propre ; aucune lecture sans nœud de Lazar »). **Ni ce texte ni la décision GO-2026-11-19-40 ne sont tenus ici pour ce
  nœud** : cette décision a été prise avant tout verdict d'identité, sur une recommandation écrite contre la version 2 du critère,
  alors que CI (§ 5) veut que Lazar soit averti de l'écart mesuré avant tout usage et qu'en ajustement seul rien ne se
  lise sans son nœud (lecture du rédacteur, portée à Lazar : nœud N12, reste à trancher). Une seule voie : après l'avertissement
  (ligne `AVERTISSEMENT-PALIER-2-LENTILLES-BBIS`), un mot de Lazar **postérieur à cet avertissement**, qui nomme la lentille,
  inscrit par la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` avant le montage de la seconde passe ; la lentille est
  alors lue sous la phrase permise du deuxième palier, dernier crochet « n'ont pas été
  refaites sur [elle | elles] », suivie de la phrase gelée « Cette lentille n'a pour mesure à elle que la différence entre moitiés de son
  ajustement (et, pour notre R, les deux séries d'écart) ; aucune des mesures de la tranche du 18 novembre n'a été refaite sur
  elle. » Sans cette ligne : non lue.
- **« différente », « non comparable (traitée comme différente) », « mention suspendue : anomalie (nœud de Lazar) »** ; CI non
  scellé, ou scellé d'une autre empreinte que celle citée ici ; verdict d'identité non scellé ; audit dû et non versé, ou non
  scellé ; verdict absent de la fiche pour cette lentille ; deuxième palier sans la ligne d'avertissement : **non lue**
  (« Non lue : notre lentille [R / S] [motif] ») ; tout usage passe par un nœud de Lazar et une version neuve (CI, § 5). Phrase
  de tête, ici et à la ligne suivante : la phrase que CI, § 5, donne au verdict de la lentille, quand elle en a un
  (« Critères »), suivie de la ligne « Non lue […] ».
- **« R non réajustée », « S non réajustée », ou lentille absente** (réajustement non fait, abandonné, perdu, non rangé, fichier
  introuvable à la révision nommée) : **non lue** (« Non lue : notre lentille [R / S] absente »).
""")
couple("K19", "1 (d)", "Entrées : fiche de rangement", L(902, 912),
       f"""- le **verdict d'identité, mot pour mot** (au premier palier, avec ou sans « ; reprise sur sauvegarde notée ») ; la **variante de
  la course** et, en course rejouée, si la seconde course a été **menée en entier** ou est **incomplète** (CI, § 5) ;
  l'indication d'une reprise ;
- les **chiffres de la sortie du programme de comparaison**, tels qu'il les rend (noms de champs relevés par le rédacteur du
  brouillon 4 dans le programme version 4, celui que cite CI, § 7, `{H_PROG[:8]}…`, « Documents ») : l'écart absolu maximal des
  différences entre moitiés en double précision (`ecart_max_abs_diffs_float64`, « l'écart mesuré ») ; l'écart maximal sur `diffs`
  (`ecart_max_abs_diffs` ; CI, § 4, mentions 2 et 4, et § 6, déclencheur (vii)) ; pour R, pour chacune des deux séries d'écart à
  la lentille publique et à l'identité (`series_export_R_sans_critere`), le plus grand changement d'une course à l'autre et la
  plus petite et la plus grande valeur du 18 novembre (`ecart_max_abs`, `ref_min`, `ref_max`), et le compte des matrices des
  moitiés égales (`matrices_moities_egales`) ; **la liste des déclencheurs** (`declencheurs`) et `audit_requis` (CI, § 6).
  Brouillon 4 : la fiche ne dit plus « si le contrôle « même code » est tenu » — la liste H1 à H7 de la version 4 du critère
  n'existe plus ; les mots « même code d'ajustement » de la phrase permise du deuxième palier sont couverts par les préalables
  « même code » et « K2 : … » du programme et par la part du contrôle K2 tenue à la main, sans lesquels le verdict ne serait pas
  au deuxième palier (CI, § 4, § 5 et § 7) ;
- les différences entre moitiés (`diffs`, cible `out`) **des deux ajustements** aux couches 7, 15 et 23 ;
- chemin et empreinte du verdict d'identité scellé, de son audit quand il est dû (CI, § 6), de la sortie du programme de
  comparaison et de CI scellé ; au deuxième palier, chemin et empreinte de l'avertissement à Lazar ; en variante course rejouée,
  chemin et empreinte de la lecture scellée de la seconde course, sa ligne d'ensemble, et sa limite par couche, mot pour mot.
""")
couple("K20", "1 (e)", "Entrées : code de la seconde passe, point 1 (libellé avec reprise)",
       "« palier 1 — même lentille, octets identiques », que ce SHA-256 égale",
       "« palier 1 — même lentille, octets identiques » (suivie ou non de « ; reprise sur sauvegarde notée »), que ce SHA-256 égale")

# ================================================================== K21 — tâches 5, 6, 7, 12 : « Métrique », point 6
couple("K21a", "6", "Métrique (6) : portée de la règle de départage",
       "**Portée** : toute liste de vingt premiers jetons de ce texte, pour toute lentille : direction lue (chaque vecteur,",
       "**Portée** : toute liste de vingt premiers jetons de ce texte, pour toute lentille et pour la référence « plongements seuls »\n"
       "     (point 4), listes du témoin de couche comprises : direction lue (chaque vecteur,")
couple("K21b", "5", "Métrique (6) : ce que la règle garde et ne garde pas",
       "La\n     règle ne dépend ni de la direction, ni de son signe, ni du nul ; appliquée de même à v, aux u_j et aux témoins, elle ne penche\n"
       "     vers aucun libellé.",
       "La\n     règle ne dépend ni de la direction, ni de son signe, ni du nul ; appliquée de même à v, aux u_j et aux témoins, **elle ne\n"
       "     change pas la validité des valeurs p** (c'est une fonction fixe des scores : l'échangeabilité sous le nul est gardée).\n"
       "     **Elle n'est pas neutre envers les familles** (brouillon 4 ; vérification de l'addendum de concentration, `867983f3…`,\n"
       "     § 3) : à score égal, elle garde toujours le plus petit identifiant ; si les plus petits identifiants comptent des jetons\n"
       "     de famille (chiffres seuls, « $ » : probable pour le vocabulaire de Llama, non vérifié sur le tokeniseur), une égalité\n"
       "     tranchée ainsi pousse, pour la direction en cause, vers « sur-représentée » ; le taux de « sur-représentée » à tort sous\n"
       "     le nul n'en change pas. L'effet est minime : de l'ordre de 10⁻⁵ par liste, fréquence d'une égalité au vingtième rang dans\n"
       "     le modèle simple de l'addendum de concentration (EC-6 : données synthétiques ; non mesurée sur la lentille réelle).")
couple("K21c", "6, 7, 12", "Métrique (6) : signe −, listes de dix, nœud ouvert, lien avec la première passe",
       "par (couche, lentille, nul) et par sorte de direction (lue, nulle, témoin) ;\n",
       f"""par (couche, lentille, nul) et par sorte de direction (lue, nulle, témoin).
     **Signe − (brouillon 4)** : la liste de −v est classée par score opposé décroissant, puis identifiant croissant ; à score
     égal, ce n'est donc pas la liste de v lue à l'envers, et le code ne la tire pas d'un classement de v retourné.
     **Listes de dix (brouillon 4)** : les dix premiers jetons de chaque pôle, par toute lentille qui les lit (lentille publique,
     notre R : point 7), suivent la même règle, l'égalité se lisant entre la dixième et la onzième valeur ; les dix pôles par
     cosinus ont leur règle au point 7 ; pour la garde de la fonction de lecture, voir le plan, point 5. Le nombre de listes de
     dix dont la dixième et la onzième valeur sont égales est écrit dans les tables (point 7).
     **Nœud ouvert (brouillon 4)** : le choix entre cette règle et une permutation fixe des identifiants, tirée par graine, est
     porté à Lazar (nœud N18, sans défaut) ; ce texte porte la règle recommandée, l'identifiant croissant ; si Lazar en retient
     une autre, ce point, le point 7 et les essais sont repris avant le scellement.
     **Lien avec la première passe (brouillon 4 ; mot de Lazar reçu).** La première passe est régie par la v1 scellée et par son
     addendum de concentration, qui ne départage pas : il pose une garde. Lazar a retenu **l'option 3, la garde à trois étages
     écrite en EC-6** (mot « option 3 pour la garde, relance les tests sans limite », note `dbd1e514…`, « Documents » ;
     GO-2026-11-19-78, R-3929) : direction lue à égalité (listes de vingt, et les deux listes de dix des pôles) : arrêt nommé ;
     direction nulle à égalité : marquée, valeur p encadrée par p_bas et p_haut, p_haut écrite, arrêt nommé seulement si le
     libellé en dépend ; témoin : compté et écrit. Donc, **pour une première passe menée à son terme**, aucune liste d'une
     direction lue n'a d'égalité à sa limite, et aucun libellé ne dépend du départage d'une direction nulle : la règle de la
     seconde passe ne peut changer, par rapport à la première, **ni une liste de direction lue, ni un libellé**. Elle peut
     changer une **valeur p écrite** (la première passe écrit p_haut quand une direction nulle est marquée ; la seconde écrit la
     valeur que donne le départage, comprise entre p_bas et p_haut ; écart d'au plus 1/(M + 1) par direction marquée) et
     l'**attendu d'une famille sous le nul** (calculé sans les directions marquées dans la première passe, sur toutes dans la
     seconde) : la reproduction (plan, point 11) compare les libellés et les vingt premiers jetons, que ces deux écarts ne
     touchent pas. La ligne de l'addendum qui fait compter, au montage, les paires de jetons gardés de même ligne de
     `lm_head.weight` (son couple H2, sans arrêt) suit le même mot de Lazar ; le montage de la seconde passe, qui refait celui de
     la première, écrit le même compte. **Si la première passe s'arrête** sur l'une de ses deux gardes d'égalité, c'est un nœud
     de la v1, que ce texte ne tranche pas ; la seconde passe n'a pas cette garde : elle départage et écrit ses comptes ;
""")

# ================================================================== K22 — tâche 6 : pôles
couple("K22", "6", "Métrique (7) : pôles à cosinus égal, dix premiers jetons d'un pôle",
       "notre S ne lit pas les pôles (directions d'écriture, non des covecteurs de lecture).\n",
       """notre S ne lit pas les pôles (directions d'écriture, non des covecteurs de lecture).
   **Égalités (brouillon 4)** : les dix pôles sont les dix premiers de l'ordre total « cosinus décroissant, puis **indice de neurone
   croissant**, puis **signe + avant signe −** » (égalités exactes, en simple précision ; classement fait pour v au signe + ; pour
   le signe −, les pôles sont ceux du signe +, de signe opposé, par définition, sans nouveau classement). Les dix premiers jetons
   de chaque pôle, par la lentille publique comme par notre R, suivent la règle du point 6 (score décroissant, puis identifiant
   de jeton croissant). Le nombre de listes de dix dont la dixième et la onzième valeur sont égales est écrit dans les tables :
   pour les pôles par cosinus, par couche et par sorte de direction ; pour les jetons d'un pôle, par couche et par lentille. La
   concentration des pôles (cosinus maximal) et son rang parmi les maxima nuls n'emploient aucune liste : inchangés.
""")

# ================================================================== K23 — tâche 6 : garde de la fonction de lecture
couple("K23", "6", "Plan (5) : garde de la fonction de lecture et égalités",
       "partage avec le code l'hypothèse d'orientation de K (« Frontière », point 18).\n",
       """partage avec le code l'hypothèse d'orientation de K (« Frontière », point 18).
   **Égalités (brouillon 4)** : de notre côté, les dix premiers jetons suivent la règle de « Métrique », point 6 ; `read` du voisin
   départage à sa façon (la fonction de tri de sa bibliothèque), et ce texte ne lui impose rien. **La tolérance du cas sain couvre
   déjà les égalités** : si des jetons ont le même score à cheval sur le dixième rang, les deux listes ne peuvent différer que par
   des jetons de ce score, dont les scores diffèrent de zéro, sous le seuil de 10⁻⁴ en valeur relative ; l'écart est compté et
   rapporté, sans arrêt (deux scores égaux, nuls compris, comptent pour une différence relative nulle). Sur les artefacts, le
   compte des colonnes porte sur des listes qui diffèrent par des jetons de scores distincts : une égalité n'y change rien. Il en
   va de même pour le chemin indépendant de notre S. Aucune règle de plus n'est donc écrite pour cette garde.
""")

# ================================================================== K24, K25 — tâches 10, 1 (k), 12 : plan
couple("K24a", "10", "Plan (1) : place de la ligne de l'addendum de concentration",
       "lève la retenue). Seconde passe, dans cet ordre : (h)",
       f"""lève la retenue). **Addendum de concentration (brouillon 4)** : la ligne
   `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` du registre propre (2026-11-19T16:35:35Z ; addendum scellé, `7c738708…`, « Documents »)
   **précède toute ligne des clés ajoutées par la v2** : la statistique que la seconde passe reprend est ainsi scellée et inscrite
   avant `SCELLEMENT-LENTILLES-BBIS-V2`. C'est le cas à l'écriture : au commit `{MAIN[:8]}…` de la branche principale, le registre
   propre ne porte que trois lignes (`ABSENCE-VERDICT-LENTILLES-BBIS`, `SCELLEMENT-LENTILLES-BBIS`, et celle de l'addendum), relevées
   par leurs clés et leurs heures. Le code de la seconde passe le vérifie (une seule ligne de cette clé, antérieure à toute ligne
   d'une clé de la v2 ; sinon rien de la seconde passe ne part : « Liste d'arrêt »). Sa place dans la première passe est fixée
   par l'addendum lui-même (avant `CODE-LENTILLES-BBIS` et `ENTREES-LENTILLES-BBIS` : son EC-4). Seconde passe, dans cet ordre : (h)""")
couple("K24b", "1 (k)", "Plan (1), (k bis) : seconde course incomplète",
       "ajustement seul, `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` (mot de Lazar postérieur à l'avertissement) ; sans les lignes",
       "ajustement seul, ou en course rejouée dont la seconde course est incomplète (CI, § 5),\n"
       "   `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` (mot de Lazar postérieur à l'avertissement) ; sans les lignes")
couple("K25", "12, 6", "Plan (11) : reproduction et régime des égalités",
       "de la lentille publique n'a alors eu lieu avant).\n",
       """de la lentille publique n'a alors eu lieu avant).
    **Égalités (brouillon 4)** : la première passe est calculée sous la garde d'égalité de l'addendum de concentration (EC-6,
    option 3), la seconde sous la règle de départage de « Métrique », points 6 et 7. Le module des statistiques n'est donc pas le
    même d'une passe à l'autre, et la reproduction porte la phrase « code de lecture différent de celui de la première passe :
    [modules] ». Ce que la comparaison peut alors trouver, et ne peut pas trouver : « Métrique », point 6, « Lien avec la première
    passe ».
""")

# ================================================================== K26 — tâche 1 (f) : phrase de tête de la seconde passe
couple("K26", "1 (f)", "Critères : phrase de tête de la seconde passe, verdict d'identité et phrases permises", L(1363, 1384),
       f"""- « Verdict d'identité : notre R : [verdict recopié de la fiche de rangement, mot pour mot, ou « non lue : [motif] »] ; notre S :
  [idem]. Course du réajustement : [ajustement seul | course rejouée | course rejouée, seconde course incomplète]. »
- Pour chacune de nos deux lentilles, **la phrase que CI, § 5, donne à son verdict, recopiée mot pour mot, dans la forme que CI
  donne à son cas** (brouillon 4 : la version 8 de CI écrit une phrase par cas ; le préfixe « Pour notre lentille [R / S] : » du
  brouillon 2 n'a plus d'emploi). Seuls se remplissent, d'après la fiche, les crochets « [R | S] », « (empreinte …) » ou
  « (empreintes …) », les crochets de chiffres et le dernier crochet ; aucun autre mot ne change. Une lentille non lue reçoit
  quand même la phrase de son verdict, suivie de sa ligne « Non lue […] ».
  - **Nos deux lentilles au premier palier** : {P1_DEUX}
  - **Une seule de nos lentilles au premier palier** : {P1_UNE}
  - **Nos deux lentilles au deuxième palier** (crochets remplis par les chiffres de la fiche, **obligatoires quel que soit leur
    sens, sans aucun qualificatif**) : {P2_DEUX}
  - **Notre R seule au deuxième palier** (mêmes crochets, mêmes obligations) : {P2_R}
  - **Notre S seule au deuxième palier** : CI dit « la même phrase, « La lentille S… », où la phrase des deux séries […] est
    remplacée par « Aucune autre comparaison n'existe pour cette lentille. » » ; écrite en entier selon cette règle (si la session
    principale la construit autrement, ce sont les mots de CI qui valent) : {P2_S}
  - **Tout autre verdict** (« différente », « non comparable (traitée comme différente) », « mention suspendue : anomalie (nœud
    de Lazar) », « R non réajustée », « S non réajustée ») : {P_AUTRE}
  - **Dernier crochet du deuxième palier** : « ont été refaites sur [elle | elles] et sont rapportées à côté » seulement en course
    rejouée menée en entier et lue (« Entrées », condition de lecture) ; « n'ont pas été refaites sur [elle | elles] » en
    ajustement seul et en course rejouée dont la seconde course est incomplète ; dans ces deux derniers cas, la phrase est suivie
    de la phrase gelée de « Entrées » (« Cette lentille n'a pour mesure à elle que […] »).
  - Ces phrases sont celles de CI version 8, scellé, § 5 (comparées par programme, à l'espacement près, au fichier `541bb86b…`,
    hors celle de notre S seule, construite) ; un écart d'un caractère avec CI est une faute de ce texte : les mots de CI valent,
    et ce texte est repris avant son scellement.
  - **Aucune phrase interdite de CI, § 5, ni paraphrase** : ni « équivalente », ni « proche », ni « la même à la précision
    près », ni « couverte par concordance », ni « rattachée », ni « réajustée à l'identique », ni aucune phrase qui tire des deux
    séries de R un appui à la proximité, ni aucune phrase qui prête à la lentille lue une mesure faite sur celle du 18 novembre.
""")
couple("K26b", "1 (f)", "Critères : verdict d'ensemble de la tranche, nos deux lentilles au premier palier",
       "- Premier palier : « Verdict d'ensemble",
       "- Premier palier, **nos deux lentilles** : « Verdict d'ensemble")
couple("K26c", "1 (f)", "Critères : verdict d'ensemble de la tranche, une seule lentille au premier palier",
       "  par le lecteur, plan, point 8]. »\n",
       """  par le lecteur, plan, point 8]. »
- Premier palier, **une seule de nos lentilles** (brouillon 4 ; CI, § 5 : l'autre a un autre verdict) : « Verdict d'ensemble de la
  tranche sur les deux lentilles du 18 novembre : [ligne recopiée de V, comme ci-dessus]. Ce verdict d'ensemble et les conditions
  communes aux deux lentilles ne se transportent pas tels quels : seules les mesures faites sur notre lentille [R | S] la
  décrivent. » Puis : « Réserves qui portent sur notre lentille [R | S] à ces couches : [pour notre R : (R-a) pour la lecture
  contre pilotage, (R-b), (R-c) et (R-e) ; pour notre S : (R-d) et (R-e) ; vérifiées contre V par le lecteur, plan, point 8]. »
  La condition de stabilité de la tranche est exigée des deux lentilles ensemble (CI, § 5) : elle n'est écrite ni tenue ni
  manquée pour une lentille seule ; vaut pour la lentille lue la stabilité par couche que le code contrôle (« Entrées »).
""")

# ================================================================== K27 — tâches 1 (h), 10 : liste d'arrêt
couple("K27a", "10", "Liste d'arrêt (v2) : ligne de l'addendum de concentration",
       "| la v2 n'est pas scellée ; reprise du texte sur CI scellé |\n",
       "| la v2 n'est pas scellée ; reprise du texte sur CI scellé |\n"
       "| `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` absente du registre propre, en plusieurs lignes, d'une autre empreinte que celle "
       "citée en « Documents », ou postérieure à une ligne d'une clé ajoutée par la v2 (brouillon 4) | la v2 n'est pas scellée ; "
       "rien de la seconde passe ne part ; nœud |\n")
couple("K27b", "1 (h)", "Liste d'arrêt (v2) : lentille non lue", L(1496, 1496),
       "| pour **une** lentille : verdict d'identité absent de la fiche ; « différente », « non comparable (traitée comme différente) » "
       "ou « mention suspendue : anomalie (nœud de Lazar) » ; « non réajustée » ; verdict d'identité non scellé ; **audit dû (au moins "
       "un déclencheur rendu par le programme ; toujours au premier palier) non versé ou non scellé** ; deuxième palier sans la ligne "
       "`AVERTISSEMENT-PALIER-2-LENTILLES-BBIS` ; deuxième palier en course rejouée **menée en entier** sans la ligne "
       "`LECTURE-SECONDE-COURSE-NOS-LENTILLES-BBIS` ; deuxième palier en ajustement seul, **ou en course rejouée dont la seconde course "
       "est incomplète ou dont la fiche ne dit pas l'achèvement**, sans la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` | "
       "cette lentille **non lue** (motif écrit en tête des tables et de la description) ; l'autre lentille et la lentille publique "
       "restent lues ; rien n'est remplacé ; si aucune de nos lentilles n'est lue : `NON-LUES-NOS-LENTILLES-BBIS` |\n")
couple("K27c", "1 (h)", "Liste d'arrêt (v2) : libellé du premier palier avec reprise",
       "pour la mention « palier 1 — même lentille, octets identiques », différents de l'empreinte",
       "pour la mention « palier 1 — même lentille, octets identiques » (suivie ou non de « ; reprise sur sauvegarde notée »), "
       "différents de l'empreinte")

# ================================================================== K28 — tâche 1 (i) : frontière
couple("K28", "1 (i)", "Frontière (6) : premier palier en cas mixte",
       "au premier palier, le verdict de notre R est celui de V ;",
       "au premier palier, le verdict de notre R est celui de V (si notre S n'est pas elle aussi au premier palier : seulement les "
       "mesures de V faites sur notre R, CI, § 5) ;")

# ================================================================== K29 — tâche 10 : lignes de registre
couple("K29", "10, 1 (k)", "Lignes de registre : clé de l'addendum de concentration",
       "n'en lit que ce que la fiche de rangement recopie.\n",
       "n'en lit que ce que la fiche de rangement recopie. **Brouillon 4** : la clé `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` (addendum\n"
       "de concentration de la v1, son EC-4) est une clé du même registre propre, inscrite par la session principale le\n"
       "2026-11-19T16:35:35Z ; la seconde passe la lit (clé, heure, chemin, empreinte) et exige qu'elle précède toute ligne d'une clé\n"
       "ajoutée par la v2 (plan, point 1). La ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` vaut aussi pour une course rejouée\n"
       "dont la seconde course est incomplète (CI, § 5).\n")

# ================================================================== K30 — tâches 8, 1 (k) : code neuf
couple("K30a", "8, 12", "Code neuf : module des statistiques de la seconde passe",
       "- un lanceur de la seconde passe, sous une horloge de 10 h.\n",
       """- un lanceur de la seconde passe, sous une horloge de 10 h ;
- **brouillon 4** : le code de la première passe applique l'addendum de concentration (statistique corrigée et garde d'égalité) ;
  celui de la seconde applique la statistique corrigée et la **règle de départage** (« Métrique », points 6 et 7). Le module des
  statistiques de la seconde passe est donc une version neuve, sous un nom neuf (R12), déclarée à `CODE-LENTILLES-BBIS-V2` ; il
  écrit dans les tables les comptes d'égalités, et la reproduction porte la phrase « code de lecture différent […] » (plan,
  point 11) ; `nos_lentilles_v1` vérifie en plus la place de la ligne de l'addendum au registre propre (plan, point 1).
""")
couple("K30b", "1 (k)", "Code neuf : essais de la condition de lecture",
       "couche écartée par la lecture de la seconde course (non lue à cette couche) ;\n",
       """couche écartée par la lecture de la seconde course (non lue à cette couche) ; **brouillon 4** : libellé du premier palier suivi de
  « ; reprise sur sauvegarde notée » (lu comme le premier palier ; un autre ajout : arrêt, forme mal comprise) ; deuxième palier,
  course rejouée, seconde course incomplète, sans la ligne du mot de Lazar (non lue) et avec elle (lue, phrase « n'ont pas été
  refaites ») ; fiche qui ne dit pas l'achèvement de la seconde course (lue comme incomplète) ; deuxième palier avec un déclencheur
  rendu et sans audit (non lue), avec audit (lue), sans déclencheur ni audit (lue) ;
""")
couple("K30c", "1 (k)", "Code neuf : essais des phrases permises",
       "- **phrases** : les deux phrases permises égales, octet pour octet, à celles de ce texte ;",
       "- **phrases** : les phrases permises de CI, § 5, dans chacune des six formes de « Critères » (deux lentilles ou une seule au\n"
       "  premier palier ; deux lentilles, R seule ou S seule au deuxième ; tout autre verdict), égales, octet pour octet, à celles de\n"
       "  ce texte ; la forme choisie d'après le couple des deux verdicts, un cas par couple (artefact : la forme au pluriel écrite\n"
       "  alors qu'une seule lentille est à ce palier : refus) ; en cas mixte au premier palier, la ligne du verdict d'ensemble dans sa\n"
       "  forme « ne se transportent pas tels quels » et les seules réserves de la lentille ;")
couple("K30d", "8", "Code neuf : essais ajoutés par le brouillon 4",
       "neuf ; bout en bout sur un Llama miniature avec de faux fichiers d'ajustement R et S, une fois par palier.\n",
       """neuf ; bout en bout sur un Llama miniature avec de faux fichiers d'ajustement R et S, une fois par palier.
**Essais ajoutés par le brouillon 4** (R5 : cas sain et artefact pour chacun ; graines `lentilles-bbis-v2/essai/<garde>` ; les
essais de la statistique corrigée et de ses deux arrêts sont ceux de l'addendum de concentration, EC-5, repris parce qu'ils
conviennent tels quels ; les autres sont écrits pour la règle de départage, que l'addendum n'a pas) :
- **statistique corrigée, concentration et part** (chaque direction nulle jugée sans elle-même) : cas sain : C(u_j) et P(u_j) de
  chaque direction nulle égales à un calcul direct, direction par direction, sur les M − 1 autres (moyenne, écart type de
  population, quantile par interpolation linéaire sur M − 1 valeurs), et formules exactes de « Métrique », point 6, égales à ce
  calcul direct ; C(v), P(v) et ceux des témoins égaux à un calcul direct sur les M directions ; artefact : la statistique
  d'origine de la v1 (la direction nulle comprise dans sa propre référence) rend une concentration strictement plus petite pour
  toute direction nulle dont le plus grand z est positif (réserve de l'addendum, § 12 : jouet où chaque direction nulle a un z
  positif) : l'essai le voit ; artefact de taux, à petite taille : scores gaussiens indépendants, M = 19 directions nulles,
  128 jetons, 2 000 répliques, chaque réplique tirant ses propres 19 directions nulles et sa direction témoin : la part des
  témoins à p ≤ 0,05 est exigée entre 0,03 et 0,065 ; la statistique d'origine en sort (≈ 0,47 dans la simulation de l'addendum,
  partie A, contre ≈ 0,045) ; comparaison C(u_j) ≥ C(v) en simple précision : deux valeurs égales après arrondi comptent contre v
  (cas sain : valeurs distinctes) ; mêmes valeurs par notre R et par notre S que par la lentille publique quand on leur donne les
  mêmes scores (le point 6 vaut pour toute lentille), et même règle pour le nul refait par direction ;
- **ses deux arrêts** : variance des M − 1 autres nulle pour un jeton (jeton constant sur les autres directions), ou au plus
  10⁻¹⁰ fois la variance des M : arrêt ; nul de deux directions : arrêt ; cas sain : trois directions de scores distincts, pas
  d'arrêt ;
- **règle de départage, listes de vingt** : cas sain : scores tous distincts : la liste est celle d'un tri simple et les comptes
  d'égalités sont nuls ; égalités placées ailleurs qu'à la limite (rangs 5 et 6 ; rangs 21 et 22) : mêmes vingt identifiants,
  compte nul ; artefact : lentille jouet dont deux jetons ont la même ligne de sortie, direction choisie pour qu'ils tiennent les
  rangs 20 et 21 : le plus petit identifiant est gardé, pour la direction lue, pour une direction nulle et pour un témoin, par
  chaque lentille ; trois jetons de même score à cheval sur le vingtième rang : les plus petits identifiants gardés ; la liste
  ne dépend pas de l'ordre dans lequel les jetons sont donnés au code (jetons permutés à l'entrée : même liste) ; un tri qui
  garde le plus grand identifiant, ou l'ordre d'arrivée, est vu par l'essai ; **signe −** : sur le même jouet, la liste de −v
  n'est pas celle de v lue à l'envers (un classement de v retourné, qui garderait le plus grand identifiant, est vu) ; liste
  par z : le même essai sur une égalité de z ; part au-dessus du nul, comptes de familles et recouvrement égaux à un calcul
  direct sur les listes départagées ; référence « plongements seuls » et listes du témoin de couche : même règle ;
- **règle de départage, listes de dix** : dix premiers jetons d'un pôle, par la lentille publique et par notre R : les mêmes
  essais, l'égalité placée aux rangs 10 et 11 ; jetons communs par pôle calculés sur les listes départagées ; **garde de la
  fonction de lecture** : cas sain : deux jetons de même score aux rangs 10 et 11, notre code et `read` du voisin gardant chacun
  l'un des deux : écart compté et rapporté, sans arrêt (scores nuls compris) ; artefact : un écart qui porte sur deux jetons
  dont les scores diffèrent de plus de 10⁻⁴ en valeur relative : arrêt ;
- **pôles à cosinus égal** : cas sain : colonnes de `W_down` toutes distinctes : les dix pôles sont ceux d'un tri simple ;
  artefact : deux colonnes égales d'une matrice `W_down` jouet, aux dixième et onzième cosinus : le neurone de plus petit indice
  est gardé ; une colonne égale à l'opposée d'une autre (même cosinus, signes opposés) : le plus petit indice est gardé ; un
  neurone de colonne orthogonale à v, sur un jouet de moins de dix cosinus positifs (cosinus nul aux deux signes) : le signe +
  avant le signe − ; pour −v, les pôles sont ceux de v, de signe opposé, sans nouveau classement ;
- **compte des égalités écrit dans les tables** : cas sain : aucune égalité : tous les comptes à zéro, écrits, par (couche,
  lentille, nul) et par sorte de direction, et pour les listes de dix ; artefact : une égalité à la limite placée dans une
  direction lue, une dans une direction nulle, une dans un témoin, une au dixième rang d'un pôle : chaque compte vaut un à sa
  place et zéro ailleurs ; une égalité ailleurs dans le classement ne compte pas ; liste de moins de vingt-et-un éléments (ou de
  onze), jouets seulement : compte « sans objet », écrit ;
- **ligne de l'addendum de concentration** (registre jouet) : présente, d'une seule ligne, de l'empreinte citée, antérieure à
  toute ligne d'une clé de la v2 : accepté ; absente, en deux lignes, d'une autre empreinte, ou postérieure à
  `SCELLEMENT-LENTILLES-BBIS-V2` : refus.
Si Lazar retient au nœud N18 une autre règle que l'identifiant croissant, les essais de la règle de départage sont repris avec elle.
""")

# ================================================================== K31 — tâches 1 (j), 7, 11 : nœuds
couple("K31a", "1 (j)", "Nœuds, N12 tranché : version du critère, seconde course incomplète",
       "**Ce texte l'applique dans ce que CI version 4 autorise** (CI prime, et la\n"
       "  recommandation tranchée avait été écrite contre sa version 2) : en **course rejouée**, la lentille est lue après l'avertissement\n"
       "  et après la lecture scellée de la seconde course, dans ses limites ; en **ajustement seul**, voir le point ouvert ci-dessous.",
       "**Ce texte l'applique dans ce que CI autorise** (CI prime, dans sa version 8 scellée ; la\n"
       "  recommandation tranchée avait été écrite contre sa version 2) : en **course rejouée menée en entier**, la lentille est lue\n"
       "  après l'avertissement et après la lecture scellée de la seconde course, dans ses limites ; en **ajustement seul**, ou si la\n"
       "  **seconde course est incomplète** (CI, § 5, la traite de même), voir le point ouvert ci-dessous.")
couple("K31b", "1 (j)", "Nœuds, N12 ouvert : renvoi au critère",
       "Enjeu : CI (version 4, § 5) dit qu'une telle lentille",
       "Enjeu : CI (§ 5) dit qu'une telle lentille")
couple("K31c", "1 (j)", "Nœuds, N12 ouvert : seconde course incomplète",
       "en dépend : en course rejouée la question ne se pose pas.",
       "en dépend : en course rejouée menée en entier la question ne se pose pas ; elle se pose de même si la seconde course\n"
       "  s'arrête avant la fin de ses mesures (CI, § 5 ; brouillon 4).")
couple("K31d", "7, 11", "Nœuds : N18 (règle de départage, ouvert) et N19 (portée de la décision sur la statistique)",
       "Défaut sous 48 heures : (b) pour une lentille au deuxième palier, (a) au premier.\n",
       """Défaut sous 48 heures : (b) pour une lentille au deuxième palier, (a) au premier.
- **N18 — égalité de score : quelle règle de départage** (ouvert au brouillon 4 ; **sans défaut** : c'est le contenu d'une pièce
  décisive, rien n'est scellé avant le mot de Lazar : <<MOT_DE_LAZAR_SUR_LA_REGLE_DE_DEPARTAGE>>).
  Décision : quand deux jetons ont le même score à la limite d'une liste (vingtième et vingt-et-unième rangs ; dixième et onzième
  pour les listes de dix), dire lequel la seconde passe garde.
  Enjeu : la part au-dessus du nul, les comptes de familles, le recouvrement et les listes montrées en dépendent. Toute règle
  fixe, appliquée de même à la direction lue, aux directions nulles et aux témoins, garde des valeurs p valides ; les règles
  diffèrent par leur neutralité envers les familles et par ce qu'elles coûtent. Dans tous les cas l'effet est minime : une
  égalité à la limite d'une liste a une fréquence de l'ordre de 10⁻⁵ par liste dans le modèle simple de l'addendum de
  concentration (données synthétiques ; non mesurée sur la lentille).
  Options :
  (a) **identifiant de jeton croissant** (la règle du brouillon 3, que ce texte porte). Avantage : aucune pièce de plus ; le même
  résultat sur toute machine et toute version des bibliothèques ; vérifiable à l'œil ; c'est la variante (a) déjà montrée à Lazar
  dans l'addendum de concentration (§ 9, point 7). Inconvénient : à score égal elle garde toujours le plus petit identifiant ;
  si les plus petits identifiants comptent des chiffres seuls et « $ », une égalité tranchée pousse, pour la direction en cause,
  vers « sur-représentée », le seul libellé qui porte une phrase de « soupçon ».
  (b) **permutation fixe des identifiants, tirée par graine** : à score égal, rang croissant dans une permutation π des 89 498
  jetons gardés. Graine dérivée de l'entropie E par `numpy.random.SeedSequence` (R9 ; forme du plan, point 3), clé nommée
  `lentilles-bbis-v2/departage/permutation-jetons` ; π tirée une fois, au montage de la seconde passe, par
  `numpy.random.Generator.permutation` sur les jetons gardés rangés par identifiant croissant ; **consignée par son empreinte**
  (SHA-256 des 89 498 identifiants dans l'ordre de π, entiers de 64 bits petit-boutistes), écrite au montage, au manifeste et en
  tête des tables ; **la même permutation** pour la direction lue, les directions nulles des deux nuls, les témoins, toutes les
  lentilles et toutes les listes de jetons, de vingt comme de dix ; empreinte différente entre le montage et le calcul : arrêt.
  Avantage : aucune préférence fixe pour une famille (π est tirée avant toute lecture et ne connaît pas les familles).
  Inconvénient : une pièce de plus à tirer, consigner, vérifier et essayer ; la suite que rend `Generator.permutation` n'est
  garantie que pour une version de numpy, si bien qu'un changement de version change π et ajoute un arrêt possible ; la règle ne
  se vérifie plus à l'œil.
  (c) **aucune règle : la garde à trois étages de la première passe**, reprise pour la seconde (addendum de concentration, EC-6,
  retenue par Lazar pour la v1, GO-2026-11-19-78). Avantage : le même régime dans les deux passes ; aucun libellé ne dépend d'un
  départage. Inconvénient : la seconde passe peut s'arrêter sur une égalité d'une direction lue, et elle a plus de listes de
  directions lues que la première (quatre lentilles et deux moitiés au lieu de deux lentilles) ; les bornes p_bas et p_haut
  restent à définir pour le recouvrement, qui dépend de deux listes ; un arrêt renvoie à un nœud, tard dans le calendrier.
  **Recommandation : (a), confiance 0,65.** Les trois gardent des valeurs p valides. Le penchant de (a) ne joue que si une
  égalité tombe à la limite d'une liste et y oppose un jeton de famille à un autre jeton ; le compte des égalités, écrit dans les
  tables par sorte de direction, montre si cela a pu arriver. L'option (b) retire ce penchant au prix d'une pièce et d'un arrêt
  de plus. L'incertitude tient à la fréquence réelle des égalités, non mesurée sur la lentille. Si Lazar retient (b) : dans
  « Métrique », point 6, « identifiant de jeton croissant » devient « rang croissant dans π », avec le tirage et l'empreinte de
  π au plan, points 3 et 4 ; les pôles gardent l'indice de neurone croissant ; les essais sont repris. Si Lazar retient (c) :
  « Métrique », points 6 et 7, le plan, point 5, la « Liste d'arrêt » et les essais sont repris, et les bornes du recouvrement
  sont à écrire. Dans les deux cas, avant le scellement.
- **N19 — la statistique corrigée vaut-elle pour la seconde passe** (signalé au brouillon 4 ; ce n'est pas un choix ouvert de ce
  texte, c'est une ligne de registre à citer). Le mot de Lazar GO-2026-11-19-47 (« go », R-3771 : option 2, chaque direction
  nulle jugée sans elle-même) est donné pour l'addendum au texte scellé de la v1. La passation de la session des lentilles dit,
  d'après la session principale, qu'il vaut pour la v2. Le rédacteur du brouillon 4 a cherché la ligne qui le consigne dans
  `registres/go.md` et `registres/decisions.md` (branche principale, commit `3a58d008…`) et ne l'a pas trouvée :
  <<MOT_DE_LAZAR_GO_47_POUR_LA_V2>> (à porter par la session principale : la ligne de registre, ou le mot de Lazar). Ce que le
  texte en dit sans attendre : la seconde passe refait la première, que régit l'addendum ; une autre statistique dans la seconde
  passe romprait la reproduction (plan, point 11).
""")

# ================================================================== K32 — R2 : fichiers à donner au contre-lecteur
couple("K32", "forme (R2)", "Contre-lecture : fichiers à donner à qui contre-lit le brouillon 4",
       "le rapport du lecteur des valeurs du BLOC-V.\n",
       """le rapport du lecteur des valeurs du BLOC-V.
  **Brouillon 4** : à qui contre-lit ce brouillon, donner en plus, explicitement : le brouillon 3 ; les trois pièces de
  fabrication du brouillon 4 (script des couples, sa sortie, le `diff`) ; CI dans sa version 8 et D dans sa version 9, scellés ;
  le programme de comparaison version 4 ; l'addendum de concentration, version finale, et ses deux vérifications ; les deux notes
  des mots de Lazar du 19 novembre (garde d'égalité ; départ du rédacteur du brouillon 4) ; le mandat du rédacteur du brouillon 4.
  Chemins et empreintes : « Documents » et bloc « Brouillon 4 » (aucune empreinte entière n'est répétée ici, pour que le
  validateur continue de signaler cette entrée tant qu'elle n'a pas eu lieu).
""")

# ================================================================== K33 — pied
couple("K33", "forme", "pied du brouillon 4",
       "Ce brouillon n'est donc pas scellable comme préenregistrement en l'état, et ne doit pas l'être.\n",
       "Ce brouillon n'est donc pas scellable comme préenregistrement en l'état, et ne doit pas l'être.\n"
       "\n"
       f"Pied (v2, brouillon 4) : écriture achevée le 2026-11-19 à {FIN} UTC (`date -u`), juste avant le dernier passage du validateur. "
       "Aucun refus d'outil, de permission ni de classifieur pendant la lecture des pièces ni pendant l'écriture. Contrôle de la v1 dans "
       f"ce brouillon (programme de la contre-lecture 3, annexe B) : {EGALES} lignes égales, aucune supprimée, 10 prolongées (182, 320, "
       f"351, 356, 358, 385, 476, 478, 480, 600), {REECRITES} réécrites (1, 147, 263, 321, 322, 335, 336, 337, 339, 461, 465, 466, 467), "
       "comme au brouillon 3, que ce brouillon ne change pas sur ce point. Bornes du bloc séparable : une occurrence de la ligne de "
       "début, une de la ligne de fin (contrôle du script des couples). `controle_ia.prereg.problemes` sur ce brouillon rend deux "
       "manques, **attendus et voulus** : « contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport) » et « marqueurs de "
       "gabarit restants » (onze marqueurs : les neuf de la table du brouillon 2 qui restent, et les deux ajoutés par ce brouillon) ; "
       "il ne rend aucune section absente ou vide. Ce brouillon n'est donc pas scellable comme préenregistrement en l'état, et ne doit "
       "pas l'être.\n")

# ------------------------------------------------------------------ contrôles du bâtisseur, puis écriture du script
for ident, tache, lieu, avant, apres in C:
    n = texte.count(avant)
    assert n == 1, (ident, n)
    for t in (avant, apres):
        assert "'''" not in t and "\\" not in t and not t.endswith("'") and not t.startswith("'"), ident
# les « avant » ne se chevauchent pas
pos = sorted((texte.index(a), texte.index(a) + len(a), i) for i, _, _, a, _ in C)
for (d1, f1, i1), (d2, f2, i2) in zip(pos, pos[1:]):
    assert f1 <= d2, (i1, i2)

ENTETE = '''# Script des couples du brouillon 3 au brouillon 4 du préenregistrement
# « lecture des sondes de l'étape B bis par lentilles, v2 » — v1
#
# Auteur : rédacteur du brouillon 4 (sous-agent de la session des lentilles, Claude Fable 5.2), 2026-11-19.
# Ce que fait ce script : il lit le brouillon 3, vérifie son empreinte, applique chaque couple (texte avant, texte après) après
# avoir vérifié que le texte « avant » paraît une fois et une seule dans le brouillon 3, que les textes « avant » ne se chevauchent
# pas, puis écrit le brouillon 4 et imprime, pour chaque couple, son identifiant, la tâche du mandat, son lieu, la ligne du
# brouillon 3 où commence le texte « avant » et les deux textes. Il vérifie enfin que les deux bornes du bloc séparable paraissent
# une fois chacune et liste les marqueurs entre doubles chevrons du brouillon 4.
# Il ne lit aucune donnée, aucune sonde, aucun score. Bibliothèque standard seulement.
#
# Usage : python -I couples-brouillon3-vers-brouillon4-v1.py BROUILLON3 BROUILLON4
#   (refuse d'écraser un BROUILLON4 qui existe et diffère, R12 ; « - » comme BROUILLON4 : contrôle seul, rien n'est écrit)
import hashlib
import re
import sys

EMPREINTE_BROUILLON_3 = "1bfac4672e27e07ff8680e7be70c28f79dd921d0eccdc00ce873b8af467c47c7"

# (identifiant, tâche du mandat, lieu, texte avant, texte après)
COUPLES = [
'''
PIED = '''

def main(argv):
    source, cible = argv[1], argv[2]
    octets = open(source, "rb").read()
    assert hashlib.sha256(octets).hexdigest() == EMPREINTE_BROUILLON_3, "le fichier donné n'est pas le brouillon 3"
    texte = octets.decode("utf-8")
    # 1. chaque « avant » une fois et une seule dans le brouillon 3 ; aucun chevauchement
    places = []
    for ident, tache, lieu, avant, apres in COUPLES:
        n = texte.count(avant)
        if n != 1:
            raise SystemExit(f"couple {ident} : texte avant trouvé {n} fois dans le brouillon 3 (attendu : 1)")
        d = texte.index(avant)
        places.append((d, d + len(avant), ident))
    places.sort()
    for (d1, f1, i1), (d2, f2, i2) in zip(places, places[1:]):
        if f1 > d2:
            raise SystemExit(f"couples {i1} et {i2} : textes avant qui se chevauchent")
    # 2. application, de la fin vers le début (les positions relevées restent justes)
    neuf = texte
    par_ident = {c[0]: c for c in COUPLES}
    for d, f, ident in sorted(places, reverse=True):
        neuf = neuf[:d] + par_ident[ident][4] + neuf[f:]
    # 3. sortie lisible
    print(f"brouillon 3 : {source} ; sha256 {EMPREINTE_BROUILLON_3}")
    print(f"couples : {len(COUPLES)} ; chaque texte avant trouvé une fois et une seule ; aucun chevauchement")
    for d, f, ident in places:
        _, tache, lieu, avant, apres = par_ident[ident]
        ligne = texte.count("\\n", 0, d) + 1
        print("=" * 100)
        print(f"couple {ident} | tâche : {tache} | lieu : {lieu} | brouillon 3, ligne {ligne} | "
              f"avant : {len(avant)} caractères ; après : {len(apres)} caractères")
        print("--- avant")
        print(avant)
        print("--- après")
        print(apres)
    print("=" * 100)
    # 4. contrôles sur le brouillon 4
    debut = neuf.count("> **[DÉBUT DU BLOC-V")
    fin = neuf.count("> **[FIN DU BLOC-V]**")
    print(f"bornes du bloc séparable dans le brouillon 4 : début {debut} fois, fin {fin} fois (attendu : 1 et 1)")
    assert debut == 1 and fin == 1
    assert neuf.index("> **[DÉBUT DU BLOC-V") < neuf.index("> **[FIN DU BLOC-V]**")
    avant_m = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
    apres_m = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", neuf)))
    print("marqueurs du brouillon 3 :", len(avant_m))
    print("marqueurs du brouillon 4 :", len(apres_m))
    for m in apres_m:
        print("   ", m.strip("<>"), "| occurrences :", neuf.count(m), "|", "gardé du brouillon 3" if m in avant_m else "ajouté")
    for m in avant_m:
        if m not in apres_m:
            print("   ", m.strip("<>"), "| porté (absent du brouillon 4)")
    empreinte = hashlib.sha256(neuf.encode("utf-8")).hexdigest()
    print(f"brouillon 4 : {len(neuf.encode('utf-8'))} octets ; {neuf.count(chr(10))} lignes ; sha256 {empreinte}")
    if cible == "-":
        print("contrôle seul : rien n'est écrit")
        return
    try:
        existant = open(cible, "rb").read()
    except FileNotFoundError:
        existant = None
    if existant is not None and existant != neuf.encode("utf-8"):
        raise SystemExit(f"{cible} existe et diffère : on n'écrase jamais (R12)")
    if existant is None:
        with open(cible, "xb") as f:
            f.write(neuf.encode("utf-8"))
    print(f"écrit : {cible}")


if __name__ == "__main__":
    main(sys.argv)
'''
with open(SORTIE, "w", encoding="utf-8") as f:
    f.write(ENTETE)
    for ident, tache, lieu, avant, apres in C:
        f.write(f"    # {'-' * 96}\n    ({ident!r}, {tache!r}, {lieu!r},\nr'''{avant}''',\nr'''{apres}'''),\n")
    f.write("]\n")
    f.write(PIED)
print(len(C), "couples écrits dans", SORTIE)
