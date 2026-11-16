"""Version qui fera foi, v1, du préenregistrement du crible (iii), écrite sur le brouillon 8 par couples « ancien → nouveau ».

Seules changent les valeurs que les règles écrites du brouillon 8 refont d'après la section « Pour les cribles » du verdict du
pilote MR-2 v14 (devis, durées, bornes et garde de départ vérifiées, information sur le taux et le minimum, réserve de tronquage
annoncée, sonde obligatoire, lignes de GO, enveloppe, III-7 par sa règle), plus l'en-tête (titre, puce, documents, statut,
validateur) et la section « Contre-lecture » (entrée 8, « Tour suivant »). Les prédictions III-1 à III-6 (gelées, R-2993) ne
changent pas. Nombres neufs : `devis-crible-iii-version-foi-v1.py` et sa sortie (mêmes dossier, scellés).

Gardes (comme `appliquer-corrections-crible-iii-brouillon8.py`) : empreintes de la pièce de départ, du programme du devis et de
sa sortie ; nombre de couples ; chaque « ancien » figure exactement une fois ; aucun chevauchement ; chaque « nouveau » figure
dans la cible ; aucune ligne des prédictions III-1 à III-7 touchée ; cible jamais écrasée (mode « x ») ; validateur
`controle_ia.prereg.problemes` rejoué sur une copie temporaire, liste vide exigée ; aucun repli silencieux. Trois couples sont
donnés par leurs bornes (début et fin, chacune unique) : le statut, la table du devis et le « Tour suivant ».
Usage : python3 -I appliquer-version-foi-crible-iii-v1.py
"""
import hashlib
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-iii-brouillon8.md")
SOURCE_SHA = "d3406878de798040561e77289066c9c99bf2cee1c644f1f92a3510d52f6bcd1d"
PIECES = {
    os.path.join(ICI, "devis-crible-iii-version-foi-v1.py"): "0a0795d1a1f47bc042382d563631db2ebd27c05002bb56cf17fd5accfc4eadc3",
    os.path.join(ICI, "devis-crible-iii-version-foi-v1-sortie.txt"): "80fe88552b8e0ea3fc84d11d7364e6c96164b43d94929b5f2cc15fabae5332b0",
    os.path.join(ICI, "contre-lecture-crible-iii-b7-tour2-v1.md"): "87501081b3f7f5223f02c3f5f25063ec3a36dde91bf35afab0eead73449695c3",
}
CIBLE = os.path.join(ICI, "crible-iii-version-foi-v1.md")
HEURE = "23:20Z"


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


source = open(SOURCE, encoding="utf-8").read()


def borne(debut, fin):
    """« ancien » donné par ses bornes : de `debut` (unique) à la fin de `fin` (unique, après `debut`)."""
    if source.count(debut) != 1 or source.count(fin) != 1:
        arret(f"borne non unique : {debut[:40]!r} ou {fin[:40]!r}")
    i, j = source.index(debut), source.index(fin)
    if j < i:
        arret("bornes dans le désordre")
    return source[i:j + len(fin)]


STATUT = """**Statut.** **Version qui fera foi, v1**, écrite sur le brouillon 8 (jugé « scellable » au tour 2 de la lecture du
brouillon 7, `contre-lecture-crible-iii-b7-tour2-v1.md`, « Contre-lecture », entrée 8), variante « crédits de Claude au
maximum » (R-2992, point 1). **Prédictions III-1 à III-6 gelées** dans leur rédaction du brouillon 8 par R-2993
(2026-11-16T15:33:25Z, `date -u`, inscrit avant le lancement du lecteur neuf de l'issue du pilote ; gel de III-6 compris) :
**inchangées**, leurs « Raisons » aussi. **Seules changent** les valeurs que les règles écrites du brouillon refont sur les coûts
et durées mesurés du pilote MR-2 v14 (section « Pour les cribles » de son verdict, [VERDICT-PC], seule part lue ; R-3005) :
attendus par appel, devis (part sur crédits de Claude et part hors crédits séparées, attendu et pire), durées, information sur le
taux de réussite par appel et sur le minimum, réserve de tronquage annoncée et sonde des gabarits rendue **obligatoire** (la
règle est déclenchée par les deux appels tronqués de `fable52`), attendus des lignes de GO, enveloppe ; et III-7 par sa règle
(aucune sonde jouée : **III-7 inchangée**, 1,05 à 1,25). Les bornes de 3 000 s par appel et de 7 200 s par monde et la garde de
départ de 10 h **ne changent pas** (appel le plus long du pilote : 553,242 s, sous 1 500 s). **Étage 5** (comparaison des
écrivains, B contre D) **aux critères gelés** : choix de R-2977, confirmé par R-2993 (« c'est la question même du crible ; la
différence avec (v), où l'ablation est rapportée sans verdict, est voulue ») ; la question ouverte du tour 2 (point 2) est ainsi
close, déclaré. Chaque nombre neuf renvoie à `devis-crible-iii-version-foi-v1.py` et à sa sortie (section « Devis », « Mise à jour
d'après le pilote, appliquée », § de la sortie entre parenthèses).
**Restes avant la recopie sous `prereg/` par `sceller_prereg`** (aucun ne se fait ici ; aucun ne change un seuil ni une règle) :
(a) la **sonde des gabarits**, désormais obligatoire, sur sa ligne propre ; si elle est jouée avant la recopie, III-7 se refait par
sa règle dans une version 2, avec le dénominateur lu au pilote (2,504888 USD) ; ses règles d'avance s'appliquent (un appel sous G2
tronqué : gabarit réécrit, crible non lancé) ; (b) les **trois valeurs calculées sur processeur** (part de H après filtre pour
III-5 ; puissance de P1 et de P2 ; taux d'erreur de l'intervalle par percentile), non calculées par ce rédacteur ; (c) le
**versement** des deux programmes de l'annexe A et de leurs sorties, avec leurs compagnons (C4) ; (d) un **tour différentiel** par
un lecteur neuf (R2, R-2993). Ce texte est scellé comme pièce (empreinte compagnon, R6), non comme préenregistrement en vigueur.
Aucune dépense, aucun appel de modèle, aucun monde tiré. L'accord GO-2026-11-15-06 (enveloppe des cinq cribles, crédits de
Claude employés au maximum) **n'autorise encore aucun appel** : la ligne « calcul » propre à ce crible s'inscrit par la mère sur
ce devis refait et contre-lu (lecture de la mère, l. 339). **Les gabarits des deux passes sont neufs** : le pilote ne les éprouve
pas (section « Devis », sonde des gabarits).
Validateur `controle_ia.prereg.problemes` : aucun défaut sur cette version (vérifié par le programme d'application avant
l'écriture du fichier)."""

TABLE_DEVIS = """| ligne | appels | jetons d'entrée (brouillon : attendu ; compté au pire) | jetons de sortie (brouillon : attendu ; borne) | crédits | attendu (pilote, règle écrite) | attendu [NOTE] (brouillon) | pire (plafonds) |
|---|---|---|---|---|---|---|---|
| Pr-4, S standard | 20 | 0,30 à 0,36 M ; 1,06 M | 0,60 M ; 1,28 M | Claude | 50,10 | 32,00 | 60,00 |
| Pr-4, D passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,28 M | Claude | 50,10 | 32,00 | 60,00 |
| Pr-4, H passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,28 M | Claude | 50,10 | 32,00 | 60,00 |
| Pr-2, passe 1 (commune à D et B) | 20 | 0,30 à 0,36 M ; 1,06 M | 0,04 à 0,20 M ; 1,78 M | Claude | 5,29 | 16,00 | 40,00 |
| Pr-2, B passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,78 M | Claude | 5,29 | 16,00 | 40,00 |
| machine (≤ 0,15 USD/h ; 0,052222 relue au pilote) | — | — | — | hors | 0,07 (0,07 à 0,08) | 0,30 | 3,00 |
| **crédits de Claude** (Pr-4, Pr-2) | 100 | | | | **160,87** (160,866640) | 128,00 | **260,00** |
| **hors crédits** (machine) | 0 | | | | **0,07** (0,074520) | 0,30 | **3,00** |
| **total** | 100 | ≈ 1,5 à 1,85 M ; 5,36 M | ≈ 2,44 à 2,6 M ; 7,40 M | | **160,94** (160,941160) | 128,30 | **263,00** |
| sonde des gabarits neufs, **obligatoire** (G1 par Pr-2, G2 par Pr-4 et par Pr-2, un monde de développement) | 3 | — | — | Claude 3 | 3,03 (3,033556) | — | 7,00 (sur crédits) |
| partie A | 0 | — | — | — | 0 | 0 | 0 |

Attendus (version qui fera foi) : 20 × 2,504888 = 50,097760 par bras de Pr-4 ; 20 × 0,264334 = 5,286680 par ligne de Pr-2
(sortie, § 4) ; machine : file de quatre mondes attendue plus le temps de machine hors appels du pilote, au prix relu (§ 5) ; avec
la sonde : 163,90 sur crédits attendus et 267 au pire ; 163,97 et 270 en tout (§ 6). Pire : 60 × 3,00 + 40 × 2,00 = 260 sur
crédits, 3 hors crédits, inchangé (règle : « pire cas inchangé (plafonds) »). Parts : `fable52` 180 (attendu 150,29), `opus55` 80
(attendu 10,57), machine 3. Les colonnes de jetons sont celles du brouillon (non relues : absentes de la section lisible du
pilote) ; la fourchette du brouillon au prix public (94,90 à 121,04 ; sonde 2,08 à 2,73) est retirée : l'attendu mesuré la
dépasse (Pr-4 à 2,50 par appel contre 1,32 à 1,64 estimés)."""

ENTREE8_ET_TOUR = """- **Contre-lecture 8** (R2, tour 2 de la lecture du brouillon 7, huitième lecture du crible) — sous-agent neuf du modèle C, qui
  n'a écrit aucune des pièces du crible. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon8.md`,
  `d3406878de798040561e77289066c9c99bf2cee1c644f1f92a3510d52f6bcd1d` (égale à son compagnon) ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iii-b7-tour2-v1.md`,
  `87501081b3f7f5223f02c3f5f25063ec3a36dde91bf35afab0eead73449695c3` (égale à son compagnon `.sha256`, recalculée). Verdict :
  « **scellable** », aucune correction exigée ; les 11 couples du tour 1 sont appliqués fidèlement et rien d'autre ne change.
  **Traitement dans cette version qui fera foi** (écrite le 2026-11-16, de 23:09Z à HEURE, `date -u`, par un rédacteur neuf
  du modèle A, au moyen du programme `appliquer-version-foi-crible-iii-v1.py`, même dossier, scellé à côté ; chaque « ancien »
  figure une seule fois dans le brouillon 8, vérifié par le programme) :
  - remarque R-a (la règle de III-7 est écrite sous la table de mise à jour, non dans une de ses lignes) : **non appliquée** :
    la table reste celle du brouillon ; la règle de III-7 est appliquée telle qu'écrite (section « Devis », « Mise à jour
    d'après le pilote, appliquée ») ;
  - remarque R-b : libellé « sans perte notable » laissé tel quel (gelé) ; la fourchette de la machine est refaite sur les
    durées du pilote ;
  - remarque R-c (puissance de P1) : non calculée ici ; reste avant la recopie sous `prereg/` (statut, point (b)) ;
  - points pour la mère : (1) scellement : devis, durées, taux recopié et table de mise à jour appliqués ici ; restent la sonde
    (désormais obligatoire), les trois valeurs processeur, le versement de l'annexe A et un tour différentiel ; (2) étage 5 aux
    critères gelés : **tranché par R-2993** (choix de R-2977 gardé ; différence avec (v) voulue), déclaré au statut ; (3) gel de
    III-6 : inscrit par R-2993 ; versement de l'annexe A : non fait ici ; (4) enveloppe : vérifiée (« Lignes de GO »,
    enveloppe) ; (5) fragilité du minimum : au taux recopié du pilote, « non concluant » presque sûr (« Choix et doutes »,
    point 12) ; (6) code neuf et calendrier : hors de ce texte, inchangés.
  - **Mentions « rédacteur lettre C »** (R-2992, point 0) : recherche refaite sur tout le texte : aucune mention fausse (les
    seules occurrences disent qu'il n'y en a pas) ; rien à corriger ; entrées historiques inchangées.

**Tour suivant** (obligatoire avant la recopie sous `prereg/`, R2, R-2993) : un tour sur le différentiel
`diff-crible-iii-b-vers-foi-v1.txt` (brouillon 8 vers cette version) par un sous-agent neuf du modèle C qui n'a écrit ni ce
texte, ni les brouillons, ni aucun rapport de contre-lecture de ce crible ; une version 2 (sonde jouée, trois valeurs processeur)
appelle un tour de plus sur son propre différentiel.
**Fichiers à lui donner explicitement** : ce texte ; le brouillon 8 (`d3406878…`) ; le différentiel ; le programme
`appliquer-version-foi-crible-iii-v1.py` ; `devis-crible-iii-version-foi-v1.py` et sa sortie ; la section « Pour les cribles » du
verdict du pilote, recopiée telle quelle dans sa consigne (le verdict lui-même n'est pas à ouvrir) ; les rapports
`contre-lecture-crible-iii-b7-tour1-v1.md` (`4803c83b…`) et `contre-lecture-crible-iii-b7-tour2-v1.md` (`87501081…`) ; les
lignes R-2977, R-2992, R-2993 et R-3005 de `registres/decisions.md` ; les lignes GO-2026-11-15-06 et GO-2026-11-16-08 de
`registres/go.md` ; `registres/depenses.md` (enveloppe) ; [PILOTE] (`8aa33014…`), « Métrique » et bloc gelé ; [NOTE]
(`2f6a69dd…`), § 0 et § 4 ; le brouillon 9 du crible (v) (`c574e39d…`), section 0, point 8."""

MISE_A_JOUR = """
### Mise à jour d'après le pilote, appliquée (version qui fera foi)

Source : [VERDICT-PC] (seule part lue du verdict) ; calculs : `devis-crible-iii-version-foi-v1.py` et sa sortie
`devis-crible-iii-version-foi-v1-sortie.txt` (empreintes à l'en-tête ; paragraphes de la sortie entre parenthèses). Contrôles
de cohérence de la section (§ 0) : 14 + 2 + 0 = 16 appels ; somme des 16 durées 2 668,095 s pour 2 673 s entre `debut_utc` et
`fin_utc` du manifeste (les appels du pilote se sont suivis en série) ; machine du pilote 0,082018 / 0,052222 = 1,5706 h, dont
2 981 s hors appels ; écart de 0,075921 USD entre le total rapproché (15,378197) et la somme des postes détaillés (15,302276),
non détaillé dans la section, sans effet sur aucune règle (elles lisent les totaux par relais).

| ligne de la règle | lu dans [VERDICT-PC] | valeur appliquée |
|---|---|---|
| N (20) et minimum | répondus : `opus55` 4 sur 4, `fable52` 2 sur 4 (ses deux tronqués) ; 6 sur 8 = 0,75 (§ 3) | **inchangés** : N = 20, minimum 16 ; probabilité d'atteindre le minimum : 1,8 × 10⁻⁷ au taux commun (monde complet 0,75⁵ = 0,237), 1,0 × 10⁻¹¹ par relais (monde complet 1,00² × 0,50³ = 0,125) ; information (« Seuil ») |
| attendu par appel (0,80 ; 1,60) | `opus55` 1,057336 USD pour 4 appels ; `fable52` 10,019552 pour 4 (prix publics égaux à ceux de la configuration pour ces deux) | **Pr-2 0,264334 ; Pr-4 2,504888** (moyennes, § 1) ; **fourchette** (plus petit et plus grand appel) : dollars par appel **absents** de la section lisible ; seules bornes : `fable52` plus petit ≤ 2,216780 (moyenne des 2 complets), plus grand ≥ 2,792996 (moyenne des 2 tronqués), tout appel ≤ 3,00 ; `opus55` plus petit ≤ 0,264334 ≤ plus grand ≤ 1,057336 ; **pire cas inchangé** (plafonds) |
| sortie au-dessus de 80 % de la borne (71 200 ; 51 200) | `fable52` : 2 appels tronqués, raison d'arrêt = borne ([PILOTE], « Métrique ») : sortie 64 000 > 51 200 ; `opus55` : aucun tronqué ; sortie du plus grand appel ≤ 1,057336 USD / 20 USD par million = 52 867 jetons < 71 200 (§ 2) | **règle déclenchée pour Pr-4** : réserves « S tronqué », « D tronqué », « H tronqué » **annoncées à l'avance** (étage 2 ; au taux de tronquage du pilote, 0,50, trois tronqués ou plus sur les 20 appels d'un bras ont la probabilité 0,9998, § 3) ; **sonde des gabarits obligatoire** ; non déclenchée pour Pr-2 |
| machine (0,30 attendu) | prix horaire relu 0,052222 USD/h ; temps hors appels 2 981 s | **0,0745 attendu** (0,068 à 0,082) : file de quatre mondes attendue (2 156 s) plus le temps hors appels du pilote, lecture déclarée de « durée par monde × cinq files » (lecture littérale, cinq fois un monde : 0,0823) ; pire 3 inchangé ; au prix relu, dix heures coûteraient 0,52 (§ 5) |
| durée par monde (30 à 40 min) | `opus55` 36,425 à 109,396 s (moyenne 68,387) ; `fable52` 388,807 à 553,242 s (moyenne 470,650) ; mondes du pilote (quatre appels en série) 584,730 à 780,744 s (§ 5) | **≈ 539 s attendues** (425 à 663 s) : chemin passe 1 (Pr-2) puis D (Pr-4), S et H en même temps ; 1 549 s si les cinq appels se suivaient (information) ; file de quatre mondes ≈ 36 min (28 à 44) ; **bornes de 3 000 s et 7 200 s inchangées** (appel le plus long 553,242 s ≤ 1 500 s : aucun nœud) ; **garde de départ inchangée** : 4 × 7 200 s + 2 h = 10 h |
| lignes de GO (montants) | — | attendus refaits : κiii1 160,87 ; κiii2 0,07 ; κiii0 3,03 ; plafonds 260, 3 et 7 inchangés ; N = 20 ; enveloppe : « Lignes de GO proposées », enveloppe |
| mondes, appels, files | — | **inchangés** : 20 mondes, 100 appels (Pr-4 : 60 ; Pr-2 : 40), cinq files de quatre mondes |

**III-7** (règle écrite sous la table) : aucune sonde jouée à l'écriture de cette version : **III-7 reste 1,05 à 1,25** ;
dénominateur lu au pilote : 2,504888 USD ; une fois la sonde jouée, III-7 = 1 + c₁ / 2,504888, en fourchette de ± 0,05 (c₁ : coût
moyen d'un appel de passe 1 de Pr-2 lu à la sonde, au prix public), écrite dans une version 2 si la sonde précède la recopie sous
`prereg/`. Information (§ 7) : la fourchette 1,05 à 1,25 répond à c₁ entre 0,125 et 0,626 USD ; si c₁ valait le coût moyen d'un
appel standard de `opus55` au pilote (0,264334), 1,1055.
**Non relu, déclaré** : jetons d'entrée et de sortie par appel, réflexion, cartes admises, taille du texte servi (absents de
[VERDICT-PC]) ; pour Pr-4, les deux appels tronqués montrent une sortie arrêtée à la borne de 64 000 jetons, au-dessus des
30 000 attendus par ce texte (information). **Inchangés** : prédictions III-1 à III-6 (R-2993) et leurs « Raisons », écrites
avant le pilote ; tout seuil et toute règle.
"""

COUPLES = [
    ("T01", "— brouillon 8 (variante « crédits de Claude au maximum »)\n",
     "— version qui fera foi, v1 (variante « crédits de Claude au maximum »)\n"),
    ("T02", "- Commit du code d'analyse : **aucun à ce jour**.",
     "- **Version qui fera foi, v1** : écrite le 2026-11-16 de 23:09Z à HEURE (`date -u`) par un rédacteur neuf du modèle A\n"
     "  (identité dite en conversation seulement), qui n'a écrit ni les brouillons 1 à 8 ni aucun rapport de contre-lecture, sur\n"
     "  le brouillon 8 (`d3406878de798040561e77289066c9c99bf2cee1c644f1f92a3510d52f6bcd1d`), au moyen du programme\n"
     "  `appliquer-version-foi-crible-iii-v1.py` (même dossier, scellé) ; dépôt lu sur `main` (tête `07648857`) ; du pilote, seule\n"
     "  la section « Pour les cribles » de son verdict, recopiée dans la consigne du rédacteur, est lue (le verdict n'est pas\n"
     "  ouvert ; aucune branche du pilote n'est lue) ; aucun commit, aucune poussée, aucun appel, aucune dépense. Nombres neufs :\n"
     "  `devis-crible-iii-version-foi-v1.py` (`0a0795d1a1f47bc042382d563631db2ebd27c05002bb56cf17fd5accfc4eadc3` ; `python3 -I`,\n"
     "  Python 3.13.18, bibliothèque standard) et sa sortie `devis-crible-iii-version-foi-v1-sortie.txt`\n"
     "  (`80fe88552b8e0ea3fc84d11d7364e6c96164b43d94929b5f2cc15fabae5332b0`), scellés à côté ; différentiel contre le brouillon 8 :\n"
     "  `diff-crible-iii-b-vers-foi-v1.txt` (scellé). Rien d'autre que ce que dit le statut ne change. **Rédacteurs** : ceux des\n"
     "  brouillons 2 à 7 étaient du modèle A (R-2992, point 0), celui du brouillon 8 et celui de cette version aussi selon leurs\n"
     "  consignes (modèle servi à relever par la mère) ; les lecteurs, du modèle C ; aucune mention d'un rédacteur « lettre C »\n"
     "  n'est fausse dans ce texte (recherche refaite).\n"
     "- Commit du code d'analyse : **aucun à ce jour**."),
    ("T03", "    R-2883, R-2968 à R-2970, R-2977, R-2992 (registre vivant) ;",
     "    R-2883, R-2968 à R-2970, R-2977, R-2992, R-2993 (gel des prédictions), R-3005 (devis à refaire sur le pilote) (registre\n"
     "    vivant) ; GO-2026-11-15-06 (l. 339, inchangée) et GO-2026-11-16-08 (l. 349, verdict P-2 accepté), relues dans\n"
     "    `registres/go.md` du fichier de travail (`0a9f171027594f83d6d61174f4390ff5e2b12268e4b7e96e188a8ff700b3caf0`) ;\n"
     "  - section « Pour les cribles » du verdict du pilote MR-2 v14 (`verdict-issue-pilote-mr2-v14-v2.md`,\n"
     "    `e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d` selon GO-2026-11-16-08, branche\n"
     "    `verdict/pilote-mr2-v74-v14-v1`) : **seule part lue**, recopiée dans la consigne du rédacteur, non vérifiée sur le\n"
     "    fichier (non ouvert) — **[VERDICT-PC]** ;"),
    ("T04", borne("**Statut.** Brouillon 8 (corrections",
                  "aucun défaut sur ce brouillon 8 (vérifié avant son scellement comme pièce de\ntravail)."), STATUT),
    ("T05", "8. **Devis (brouillon, estimé ; variante « crédits de Claude au maximum », R-2992)** : 128,30 USD attendus aux prix de [NOTE]\n"
            "   (128 sur crédits de Claude, 0,30 hors crédits : la machine ; fourchettes de ce texte au prix public : 94,90 à 121,04) ;",
     "8. **Devis (version qui fera foi ; coûts mesurés du pilote, règles écrites ; variante « crédits de Claude au maximum »,\n"
     "   R-2992)** : **160,94 USD attendus** (160,87 sur crédits de Claude : 60 appels de Pr-4 à 2,504888 et 40 de Pr-2 à 0,264334,\n"
     "   moyennes du pilote ; 0,07 hors crédits : la machine ; brouillon : 128,30 aux prix de [NOTE]) ; avec la sonde des gabarits,\n"
     "   désormais obligatoire : 163,97 attendus, 270 au pire ;"),
    ("T06", "9. **Durée** : 20 mondes l'un après l'autre = ≈ 12 à 15 h attendues, 60 h au pire",
     "9. **Durée** : 20 mondes l'un après l'autre = ≈ 3 h attendues d'après les durées mesurées du pilote (20 × 539 s, chemin\n"
     "   passe 1 puis D ; 8,6 h si les cinq appels d'un monde se suivaient ; brouillon : 12 à 15 h), 60 h au pire"),
    ("T07", "calculées pour quatre mondes en série de 10 800 s. Le code du pilote",
     "calculées pour quatre mondes en série de 10 800 s. **Bornes et garde inchangées** par la règle de mise à jour (appel le plus long du pilote : 553,242 s, sous 1 500 s) ; durée attendue d'une file : ≈ 36 min (28 à 44 min), plus mesure et barrières. Le code du pilote"),
    ("T08", "10. **Préalable conseillé** : une sonde des deux gabarits neufs (trois appels sur un monde de développement, ≈ 2,08 à 2,73 USD\n"
            "    au prix public, 7,00 au pire, sur crédits de Claude), avant les 100 appels.",
     "10. **Préalable obligatoire** (règle de la table de mise à jour : deux appels de `fable52` tronqués au pilote, sortie à la\n"
     "    borne de 64 000 jetons, au-dessus de 51 200) : une sonde des deux gabarits neufs (trois appels sur un monde de\n"
     "    développement, ≈ 3,03 USD attendus aux coûts moyens du pilote, 7,00 au pire, sur crédits de Claude ; brouillon : 2,08 à\n"
     "    2,73, conseillée), avant les 100 appels."),
    ("T09", "  échec » : remarque R-5, sans objet désormais).",
     "  échec » : remarque R-5, sans objet désormais). **Recopié** (version qui fera foi ; comptes `corps.appels` du verdict\n"
     "  prononcé par un lecteur neuf, R-3001, lus dans [VERDICT-PC], non recalculés ici) : `opus55` 4 répondus sur 4, `fable52` 2 sur 4\n"
     "  (ses deux appels tronqués), soit **6 sur 8 = 0,75** pour les deux relais (sortie du programme de cette version, § 3)."),
    ("T10", "recalculée au taux\n  recopié du pilote (information) ;",
     "recalculée au taux\n  recopié du pilote (information) : 1,8 × 10⁻⁷ à p = 0,75 ; 1,0 × 10⁻¹¹ par relais (Pr-2 1,00, Pr-4 0,50 : monde\n"
     "  complet 0,125 ; sortie, § 3) ;"),
    ("T11", "| poste | clé de configuration | crédits | rôle ici | attendu par appel ([NOTE] § 1) |",
     "| poste | clé de configuration | crédits | rôle ici | attendu par appel (moyenne du pilote, version qui fera foi ; [NOTE] § 1 entre parenthèses) |"),
    ("T12", "| passe 1 (D, B) ; écrivain de B | 0,80 |", "| passe 1 (D, B) ; écrivain de B | 0,264334 (0,80) |"),
    ("T13", "| S ; écrivain de D et H | 1,60 |", "| S ; écrivain de D et H | 2,504888 (1,60) |"),
    ("T14", "## Devis (brouillon ; tout est estimé sauf les plafonds ; à refaire sur le coût mesuré du pilote)",
     "## Devis (version qui fera foi : attendus refaits sur le coût mesuré du pilote par la règle écrite ; plafonds inchangés)"),
    ("T15", "**Hypothèses de coût** (ce texte ;",
     "**Hypothèses de coût du brouillon** (gardées pour les colonnes de jetons, que [VERDICT-PC] ne permet pas de relire, et pour\n"
     "l'attendu de [NOTE] ; ce texte ;"),
    ("T16", borne("| ligne | appels | jetons d'entrée (attendu ; compté au pire)", "| partie A | 0 | — | — | — | 0 | 0 | 0 |"),
     TABLE_DEVIS),
    ("T17", "128,30 attendus au lieu de 63,30, 263,00 au pire au lieu de 243,00.",
     "160,94 attendus d'après le pilote (128,30 au brouillon) au lieu de 63,30, 263,00 au pire au lieu de 243,00."),
    ("T18", "- **Durée** (estimée) : mondes ≈ 1 h ;",
     "- **Durée mesurée au pilote** (version qui fera foi ; sortie, § 5) : appels de `opus55` 36,425 à 109,396 s (moyenne 68,387),\n"
     "  de `fable52` 388,807 à 553,242 s (moyenne 470,650), joués en série au pilote ; monde du crible, chemin passe 1 puis D (S et H\n"
     "  en même temps) : ≈ 539 s attendues (425 à 663 s ; 1 549 s si les cinq appels se suivaient) ; file de quatre mondes : ≈ 36 min\n"
     "  (28 à 44 min ; 103 min en série), plus mesure et barrières (temps de machine hors appels du pilote : 2 981 s) ; pire\n"
     "  inchangé (8 h par file, garde de 10 h) ; la latence sous vingt sessions à la fois n'est pas mesurée par le pilote, dont les\n"
     "  appels se sont suivis.\n"
     "- **Durée** (estimation du brouillon ; valeurs remplacées par la puce précédente, règles et risques inchangés) : mondes ≈ 1 h ;"),
    ("T19", "longueur et forme des cartes\nsous G2.\n", "longueur et forme des cartes\nsous G2.\n" + MISE_A_JOUR),
    ("T20", "| GO-AAAA-MM-JJ-NN (κiii0, conditionnelle) |", "| GO-AAAA-MM-JJ-NN (κiii0, obligatoire par la règle de mise à jour) |"),
    ("T21", "Mots exigés par le lecteur gelé des lignes : à fixer avec le code ; montants à refaire sur le devis mesuré.",
     "Mots exigés par le lecteur gelé des lignes : à fixer avec le code ; montants (plafonds) inchangés par la règle ; attendus\n"
     "refaits d'après le pilote : κiii1 160,87 USD, κiii2 0,07, κiii0 3,03 (section « Devis »)."),
    ("T22", "brouillon 4 : 123 + 483 + 243 + 196,60 + 263 ; avec les 7 USD de la sonde des gabarits, 1 315,60).",
     "brouillon 4 : 123 + 483 + 243 + 196,60 + 263 ; avec les 7 USD de la sonde des gabarits, 1 315,60). **Vérifié pour la\n"
     "version qui fera foi** (sortie, § 8) : aucune ligne « calcul » de `registres/go.md` ni aucune ligne de `registres/depenses.md`\n"
     "ne cite GO-2026-11-15-06 : **rien n'est engagé** sous l'enveloppe ; ce crible, sonde comprise, 270 USD au pire (267 sur crédits,\n"
     "3 hors crédits), **y tient** (reste 1 005) ; aux textes actuels des quatre autres ((i) 123, (ii) 483 et (iv) 243 de [NOTE] ;\n"
     "(v) 204,67 avec sa sonde neuve, brouillon 9), le cumul des cinq fait 1 323,67 USD (1 308,60 sans les deux sondes), au-dessus\n"
     "de 1 275 : le dernier crible inscrit n'y tiendra pas, nœud de Lazar à ce moment (R-2992, point 3). Attendus : 163,97 pour ce\n"
     "crible avec la sonde, contre 63,30 à [NOTE] et 247,20 pour les cinq à GO-2026-11-15-06."),
    ("T23", "8. **Sonde des gabarits neufs** avant le crible (≈ 2,08 à 2,73 USD au prix public, 7,00 au pire, sur crédits) : recommandation : oui ;\n"
            "   confiance 0,7.",
     "8. **Sonde des gabarits neufs** avant le crible : **obligatoire** dans cette version (règle de la table de mise à jour :\n"
     "   `fable52` tronqué au pilote) ; ≈ 3,03 USD attendus aux coûts moyens du pilote, 7,00 au pire, sur crédits (brouillon : 2,08\n"
     "   à 2,73 au prix public, conseillée, confiance 0,7)."),
    ("T24", "à N = 20, un « non concluant » est donc probable si le taux réel par appel est de 0,95 ou moins (0,49 à\n    p = 0,95).",
     "à N = 20, un « non concluant » est donc probable si le taux réel par appel est de 0,95 ou moins (0,49 à\n    p = 0,95). "
     "**Au taux recopié du pilote** (version qui fera foi) : 6 sur 8 (`fable52` 2 sur 4, ses deux appels tronqués) :\n"
     "    probabilité d'atteindre le minimum ≈ 1,8 × 10⁻⁷ (taux commun) à 1,0 × 10⁻¹¹ (par relais) ; la ligne d'arrêt du minimum\n"
     "    se déclencherait alors presque sûrement, après ≈ 10 mondes commencés, pour ≈ 78 USD dépensés (approximation : chaque\n"
     "    monde indépendant, les quatre autres files menant leur monde en cours à son terme ; sortie, § 3) ; information, rien ne\n"
     "    change (R-2992) ; point pour la mère."),
    ("T25", "crédits de Claude** à couvrir : 260 USD au pire pour ce crible, plus 7 pour la sonde des gabarits,",
     "crédits de Claude** à couvrir : 260 USD au pire pour ce crible (160,87 attendus d'après le pilote), plus 7 pour la sonde\n"
     "    des gabarits (3,03 attendus),"),
    ("T26", borne("**Tour suivant** (obligatoire avant le scellement, R-2992, point 1", "l'annexe A et ses deux programmes."),
     ENTREE8_ET_TOUR),
]
NOMBRE_ATTENDU = 26

if HEURE.startswith("@@"):
    arret("heure de fin non inscrite")
COUPLES = [(i, a, n.replace("HEURE", HEURE)) for i, a, n in COUPLES]
if not os.path.isfile(os.path.join(DEPOT, "src", "controle_ia", "prereg.py")):
    arret(f"racine du dépôt introuvable : {DEPOT}")
if sha(SOURCE) != SOURCE_SHA:
    arret(f"empreinte différente : {SOURCE}")
for chemin, attendu in PIECES.items():
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")
if len(COUPLES) != NOMBRE_ATTENDU or len({c[0] for c in COUPLES}) != NOMBRE_ATTENDU:
    arret("nombre de couples ou identifiants inattendus")

# Les lignes des prédictions (table « Prédiction chiffrée et signe attendu ») ne sont touchées par aucun couple.
debut_pred = source.index("| III-1 |")
fin_pred = source.index("| III-7 |")
fin_pred = source.index("\n", fin_pred)
places = []
for ident, ancien, nouveau in COUPLES:
    n = source.count(ancien)
    if n != 1:
        arret(f"{ident} : « ancien » trouvé {n} fois dans la pièce de départ (une seule exigée)")
    debut = source.index(ancien)
    if debut < fin_pred and debut + len(ancien) > debut_pred:
        arret(f"{ident} touche la table des prédictions gelées")
    places.append((debut, debut + len(ancien), ident, ancien, nouveau))
places.sort()
for p, q in zip(places, places[1:]):
    if q[0] < p[1]:
        arret(f"chevauchement entre {p[2]} et {q[2]}")
morceaux, curseur = [], 0
for debut, fin, ident, ancien, nouveau in places:
    morceaux.append(source[curseur:debut])
    morceaux.append(nouveau)
    curseur = fin
morceaux.append(source[curseur:])
texte = "".join(morceaux)
for ident, ancien, nouveau in COUPLES:
    if nouveau not in texte:
        arret(f"{ident} : « nouveau » absent de la cible")
if source[debut_pred:fin_pred] not in texte:
    arret("table des prédictions changée")

with tempfile.TemporaryDirectory() as dossier:
    essai = os.path.join(dossier, "crible-iii-version-foi-v1.md")
    with open(essai, "w", encoding="utf-8") as f:
        f.write(texte)
    py = os.path.join(DEPOT, ".venv", "bin", "python")
    r = subprocess.run([py, "-c", "import sys; from controle_ia.prereg import problemes; p = problemes(sys.argv[1]); "
                        "print(p); sys.exit(1 if p else 0)", essai],
                       cwd=DEPOT, env={"PYTHONPATH": os.path.join(DEPOT, "src"), "PATH": "/usr/bin:/bin"},
                       capture_output=True, text=True)
    if r.returncode != 0:
        arret("validateur : " + (r.stdout + r.stderr).strip())

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(texte)
print(f"{len(COUPLES)} couples appliqués ; cible écrite : {CIBLE}")
print("empreinte de la cible :", sha(CIBLE))
