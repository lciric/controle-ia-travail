# Table « constat → endroit changé » du brouillon 4 de P3b — v1

Rédacteur neuf du brouillon 4 (Claude, sous-agent), session 16, 2026-10-21 vers 02:32 UTC (heure vraie, `date -u`). Il
remplace un rédacteur du brouillon 4 coupé par une limite d'usage avant d'écrire, sans contact avec lui ; aucun dossier
`brouillon4/` n'existait (rien à mettre de côté sous `brouillon4-partiel-coupe-1/`). Consigne
`…/p3b/consigne-redacteur-P3b-brouillon4-v1.md` (`1d4819921d764877ceedbc1b935933e5f777be61038f6ba0b5095098e2648ff3`, égale à
son compagnon). Une ligne par constat des deux vérifications courtes du brouillon 3, toutes acceptées par la session :
« méthode » `…/p3b/verification-courte-brouillon3/methode/verification-courte-P3b-brouillon3-methode-v1.md` (`66165ba5…`,
8 constats) et « texte » `…/p3b/verification-courte-brouillon3/texte/verification-courte-P3b-brouillon3-texte-v1.md`
(`2c77870f…`, 9 constats). `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

Abréviations : T = `P3b-seconde-lecture-v1-brouillon4.md` ; D = `devis-P3b-v4.md` ; Pl = `plan-code-et-chaine-P3b-v4.md` ;
Q = `questions-ouvertes-P3b-v4.md` (même dossier). Base : `…/p3b/brouillon3/` (texte `9430e359…`, devis `3dc920f8…`, plan
`d950e428…`, questions `aff0a7ed…`, table `89e67f7f…` ; empreintes égales aux compagnons). Méthode : script
`travail/appliquer_brouillon4_v1.py`, 63 remplacements exacts, chacun trouvé une seule fois dans la base (sinon arrêt) ;
liste nommée dans `travail/journal-remplacements-v1.txt`. Les chaînes de la base coupées par un retour à la ligne sont
cherchées avec leur retour à la ligne et leur retrait, mot pour mot. « Mots exacts » : mots du rapport recopiés sans
changement (retours à la ligne mis pour la longueur des lignes seulement) ; tout autre mot est écrit dans la dernière
colonne avec son motif. VCm-NN = VCP3b-methode-NN ; VCt-NN = VCP3b-texte-NN.

| constat | décision | passage | écart ou précision (motif) |
|---|---|---|---|
| VCm-01 (majeur, bloquant) | appliqué | T : repli (B) de P-023, inséré après « déclarés, R-295) » est retirée ; » (H-P3b-2, G5, O7), avant le renommage | mots exacts. **Fusion avec VCt-04 (3)**, qui vise les mêmes trois passages par des remplacements « partout » (« ni au nombre écrit », « du nombre écrit », « ni au nombre écrit ») placés après le renommage : les mots de VCm-01 sont gardés pour H-P3b-2, G5 et O7, car ils écrivent ce que T4 de P3 ne contrôle pas (R4, R8) ; les trois remplacements de VCt-04 pour ces passages sont omis (leurs chaînes n'existent plus après VCm-01 : règles mortes). Contrôle en mémoire (`travail/controle_repli_B_P023_v1.py`) : chaque chaîne citée trouvée une fois dans le texte principal. Effet de forme accepté : G5 lit « … du texte trompeur du contexte, et du nombre écrit (…) » (mots exacts du rapport) |
| VCm-02 (bloquant) | appliqué | T : G6 (branche « recouvrement » avant la branche générique) ; repli (B) de P-023, clause de G6 ; Pl : `lecture_p3b_v1.py` (lignes atteintes) | G6 : mots exacts de VCm-02 (« ; sinon T4 résiduel non calculable (recouvrement) → … ; sinon T4 résiduel non établi ou non calculable → … »). **Fusion avec VCt-09** : colonne d'issue de G6 selon VCt-09 (« non établi ou non calculable ») ; motifs selon VCm-02 (la branche générique couvre aussi « non calculable » faute d'effectifs, que VCt-09 laissait sans motif). Clause du repli (B) : **forme de VCt-09** (« sinon … (recouvrement insuffisant) » ; » est retiré ») au lieu de celle de VCm-02 : avec les mots de VCm-02, le retrait laisse une double espace et le second retrait (« sinon … (spécification) … ; ») ne se trouve plus mot pour mot (premier essai, mis de côté sous `travail/essai-1-v1/`) ; avec la forme de VCt-09, G6 garde « … à cette puissance » ; sinon T4 de P3 non établi ou non calculable → … », le résultat que VCm-02 écrit. Plan, mots de ce rédacteur : test « G6 avec T4 résiduel non calculable (recouvrement) → motif « recouvrement insuffisant », et non calculable faute d'effectifs → motif « à cette puissance » » |
| VCm-03 (bloquant) | appliqué | T : contrôle positif, (iv) ; Pl : `lentille_p3b_v1.py` (test de l'artefact) ; Q : Q-19 | mots exacts aux deux endroits |
| VCm-04 | appliqué | T : T4 résiduel (h_t) ; double comptabilité (H_t) ; Pl : `residuel_p3b_v1.py` (rôle, « covariables manquantes », test), `lentille_p3b_v1.py` (exclusions) ; Q : Q-28 | mots exacts aux deux endroits du texte. Conséquences au plan, mots de ce rédacteur : la règle du rôle reprend les mots du texte ; « covariables manquantes (hors « référence vide ») » ; test neuf « action du saboteur d'une tâche sans action lisible de l'honnête → exclue, motif « référence vide », le reste du bras lu (jamais « non calculable » pour tout le bras) » ; exclusions de la lentille : « « référence vide » selon la règle du texte » |
| VCm-05 | appliqué | T : seconde spécification ; Pl : `residuel_p3b_v1.py` (rôle et test) | mots exacts au texte. Conséquences au plan, mots de ce rédacteur : « premier décile omis (référence) » dans le rôle ; test « seconde spécification de plein rang, premier décile omis (artefact : dix indicatrices plus la constante → colinéarité détectée, arrêt) » |
| VCm-06 | appliqué | T : item (vi) ; Pl : `lentille_p3b_v1.py` (test) ; Q : Q-19 | mots exacts au texte. Plan, mots de ce rédacteur : test des leurres des items (vi) (artefact : leurre de premier identifiant τ(A) → candidat écarté) |
| VCm-07 (forme) | appliqué | T : P3b-P8 ; plancher par rotation | mots exacts aux deux endroits. P3b-P8 : seule la liste des issues change, aucune probabilité |
| VCm-08 (information) | appliqué pour ce qui en demande | T : en-tête (empreinte actuelle de `registres/decisions.md`) ; Q : Q-23, Q-26 | (1) réserve 1 du brouillon 3, mots proposés : **fondus avec VCt-02 (1)**, dont les mots exacts sont appliqués (même règle, plus complète : marqueurs retirés d'abord, puis la version écrite comme des remplacements est appliquée et retirée). (2) renvois « (Version de repli … de P-023 …) » : retirés au candidat par la règle de VCt-02 (1). (3) a priori de P3b-P2 et P3b-P5 en (B) : non bloquants, non changés (Q-26). (4) = VCm-07. (5) longueur des lignes : sans effet, non changée. D4b : « sans correction exigée », non changé. Hors lentille : titres = VCt-08 ; empreinte du registre : ajoutée à l'en-tête, mots de ce rédacteur (« empreinte relevée … `6005137f…` (registre vivant : lignes à relire au candidat) »), le registre n'étant pas relu par ce rédacteur |
| VCt-01 (bloquant) | appliqué | Pl : `sceller_p3b_v1.sh` ; T : puce « Statut » ; Q : Q-23 | mots exacts aux deux endroits. Dans le texte, la chaîne citée (« le scellement refuse « en attente » et « de repli », sans égard à la casse. ») est coupée par un retour à la ligne : cherchée avec lui |
| VCt-02 (bloquant) | appliqué | T : puce « Statut » ((1) deux remplacements, (3) liste des phrases retirées) ; replis de N-031 (phrase de suite) ; repli (C) de P-024 (phrase de suite) ; Q : Q-01, Q-21, Q-23 | (1), (2) et (3) en mots exacts. Fusion avec VCm-08 (1) (voir cette ligne) |
| VCt-03 (bloquant) | appliqué | T : T4 résiduel (plis des sondes génériques) ; Plan d'analyse, point 1 ; Pl : `partition_p3b_v1.py`, `residuel_p3b_v1.py` ; Q : Q-02 | (1) et (2) en mots exacts. Conséquences au plan, mots de ce rédacteur : confirmation « 5 × 8 ; en (B) 5 × 4 » ; plis du résidu « Version de repli (B) de P-016 : `plis/lecture-40` » |
| VCt-04 (bloquant) | appliqué, fondu | T : repli (B) de P-023 (renommage étendu au point 3 du plan d'analyse et à la phrase de l'audit R4 ; prédiction de P3b-P5 ; motifs de G6, O5, P3b-P5) ; Q : Q-26 | mots exacts, sauf les trois remplacements « partout » qui visent H-P3b-2, G5 et O7, omis par la fusion avec VCm-01 (voir cette ligne) ; les trois autres (« historique des coûts », « historique », motif de P3b-P5) sont gardés dans l'ordre du rapport. A priori de P3b-P2 et P3b-P5 laissés (VCm-08 (3)) |
| VCt-05 | appliqué | T : repli (C′) de P-017 ; Q : Q-25 | mots exacts |
| VCt-06 | appliqué | T : replis (b) et (c) de N-031, écart (iv) ; Q : Q-01 | mots exacts ; chaîne de la base coupée par un retour à la ligne (« pour G0 / (l. 157) ») : cherchée avec lui |
| VCt-07 | appliqué | T : Chaîne de lancement, Ordre, repli (A) de N-032 ; Pl : § 4 ; Q : Q-03 | mots exacts aux deux endroits ; le repli (B) (« de même, avec … ») suit la forme de (A) sans autre changement |
| VCt-08 | appliqué, titres v4 | D, Pl, Q : titres et en-têtes | le rapport demande « — v3 » et « brouillon 3 » pour les pièces v3 ; la consigne fait écrire des pièces v4 : titres « — v4 » et « brouillon 4 — v4 » (R12, même intention). Les en-têtes disent que les pièces v3 portaient « — v2 » par erreur ; les pièces v3 restent telles quelles |
| VCt-09 | appliqué, fondu | T : G6 (colonne d'issue ; motifs) ; repli (B) de P-023, clause de G6 | colonne d'issue : mots exacts. Motifs : fondus avec VCm-02 (bloquant, même passage), dont les mots sont pris (voir cette ligne). Clause du repli (B) : mots exacts de VCt-09 |

Constats non appliqués : aucun. Parties non appliquées, par fusion déclarée : les trois remplacements « partout » de VCt-04
pour H-P3b-2, G5 et O7 (remplacés par ceux de VCm-01) ; les motifs de G6 dans la forme de VCt-09 (remplacés par ceux de
VCm-02) ; la clause du repli (B) dans la forme de VCm-02 (remplacée par celle de VCt-09). Aucune décision de Lazar n'est
tranchée : les marqueurs de N-031, N-032, P-016, P-017, P-023 (cinq) et P-024 restent (10 marqueurs, comme au brouillon 3),
chaque version de repli reste complète et remplaçable en mots exacts.

## Changements qui ne viennent d'aucun constat

- En-têtes du texte, du devis, du plan et des questions : rédacteur du brouillon 4 (remplaçant d'un rédacteur coupé), heures
  (`date -u`), consigne et empreinte, versions remplacées et leurs empreintes ; historique du texte (brouillon 3, vérifications
  courtes, table du brouillon 4).
- Exposition : déclaration du rédacteur du brouillon 3 gardée, étiquetée comme telle ; déclaration du rédacteur du brouillon 4.
- Renvois : `devis-P3b-v4.md`, `plan-code-et-chaine-P3b-v4.md` ; table du brouillon 3 citée par son chemin ; « rédacteurs des
  brouillons 2 à 4 » (Contre-lecture 1).
- Section « Contre-lecture » : entrées 5 et 6 (vérifications courtes du brouillon 3, traitement par la consigne du brouillon 4) ;
  entrée 7 à remplir (brouillon 4, puis candidat). Le validateur la lit toujours « à remplir » : sortie de `problemes`
  identique à celle du brouillon 3 (`problemes-brouillon4-v1.txt`).
- Questions : ajouts marqués « (brouillon 4) » (Q-01, Q-02, Q-03, Q-19, Q-21, Q-23, Q-25, Q-26, Q-28).

## Points laissés à la session (lus par ce rédacteur, non changés)

- « Chaîne de lancement », Ordre (et plan § 4) : il nomme encore « brouillon 3 ; vérification courte des corrections … ; code
  et tests » sans le brouillon 4 ; ce rédacteur n'y ajoute rien, l'étape qui suit le brouillon 4 (nouvelle vérification ou
  non) étant à la session.
- Au candidat, une version retenue écrite comme des remplacements cite des chaînes que le texte coupe parfois par un retour à
  la ligne (repli (B) de P-023 notamment) : la recherche se fait aux blancs près, comme la garde du scellement (VCt-01).
- G5 en (B) : « … du contexte, et du nombre écrit (…) » (mots exacts de VCm-01), virgule suivie de « et » : forme seulement.
- P3b-P2, colonne du signe, en (B) : « une sonde au champ ne serait pas séparée du nombre, de la tâche ou de l'historique » n'est
  visé par aucun remplacement (VCt-04 vise la colonne de réfutation de P3b-P5 seulement) ; a priori non bloquant (VCm-08 (3)).
- Synthèse, ligne « oracle en O4, O5 ou O6 » : « au-delà de la consigne, du nombre et de la tâche : non établi » ; aucun
  constat ne la vise ; elle dit « non établi », sans revendiquer la tâche.
- Lignes de longueur inégale (remplacements sans remise en page complète).
