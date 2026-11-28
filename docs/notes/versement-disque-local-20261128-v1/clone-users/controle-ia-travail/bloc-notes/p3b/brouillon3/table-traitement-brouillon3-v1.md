# Table « constat → endroit changé » du brouillon 3 de P3b — v1

Rédacteur neuf du brouillon 3 (Claude, sous-agent), session 16, 2026-10-21 vers 01:35 UTC (heure vraie, `date -u`). Une ligne
par constat des contre-lectures R2 du brouillon 2 : « méthode »
`…/p3b/contre-lectures-brouillon2/methode/contre-lecture-R2-P3b-brouillon2-methode-v1.md` (`9c312900…`, 12 constats) et
« texte et périmètre » `…/p3b/contre-lectures-brouillon2/texte/contre-lecture-R2-P3b-brouillon2-texte-v1.md` (`c2f68f5a…`,
15 constats), selon le traitement de la session `…/p3b/traitement-contre-lectures-brouillon2-P3b-v1.md` (`958b4601…`) :
tous acceptés. `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

Abréviations : T = `P3b-seconde-lecture-v1-brouillon3.md` ; D = `devis-P3b-v3.md` ; Pl = `plan-code-et-chaine-P3b-v3.md` ;
Q = `questions-ouvertes-P3b-v3.md` (même dossier). Base : `…/p3b/brouillon2/` (texte `64c5adad…`, devis `7dd3cfee…`, plan
`fd82f2f6…`, questions `417a111e…`). Méthode : script `travail/appliquer_brouillon3_v1.py`, 150 remplacements exacts, chacun
trouvé une seule fois dans la base (sinon arrêt) ; liste nommée dans `travail/journal-remplacements-v1.txt`. « Mots exacts » :
mots du rapport recopiés sans changement ; tout autre mot est écrit dans la dernière colonne avec son motif.

| constat | décision | passage | écart ou précision (motif) |
|---|---|---|---|
| CR2-P3b-methode-01 | accepté | T : Métrique, T4 résiduel (régression, recouvrement, seconde spécification) ; Pl : `residuel_p3b_v1.py` (rôle et tests) | corrections 1 à 4 en mots exacts. Conséquences au plan, mots de ce rédacteur : le test de courbure porte sur c_w − h_t et sur les déciles de c_w − h_t (l'ancien test visait des déciles de c_w, que la seconde spécification n'a plus) ; test du recouvrement « aire de m − h_t » |
| CR2-P3b-methode-02 | accepté | T : G6 (motif de T3 en deux branches ; branche « T4 résiduel non établi (spécification) ») ; O4 (ligne remplacée) ; O5 (branche « spécification ») ; Pl : `lecture_p3b_v1.py` (lignes atteintes) | (1) et (2) en mots exacts. (3) « ajouter à G6 et à O5 » : placé avant la branche générique « T4 résiduel non établi », pour que ce cas ne soit pas lu « à cette puissance » (motif du rapport) ; dans O5, en tête de la cellule, suivi de « sinon ». Fusion avec CR2-texte-05 (3) : le repli (B) de P-023 retire ces deux branches (T4 de P3 n'a pas de seconde spécification) |
| CR2-P3b-methode-03 | accepté | T : contrôle positif, (iii) et phrase « La bande de référence est rapportée » ; table D (D2b neuve, D3, D4, D4b) ; Seuil, double comptabilité (marge bilatérale) ; Pl : constantes (« marge 0,15 de D3, bilatérale »), `lecture_p3b_v1.py` (D2b, borne des deux côtés) ; Q : Q-17 | mots exacts. P3b-P8 non changé : D2b est un « non tranché », compris dans les ≈ 50 % écrits |
| CR2-P3b-methode-04 | accepté (traitement, décision 2) | T : contrôle positif, item (vi) ; D3 (lecture) ; Plan, point 6 (graine `cp-lentille/calcul`) ; P3b-P7 ; Plan, étape 2.3 et point 7 ; Chaîne, « Ce que la passe garde » ; D : § 3 (poste (vi), ≈ + 0,05 h), § 1, total, § 4 ; Pl : constantes ([1, 499]), `lentille_p3b_v1.py` (rôle et tests), sorties (`cp-lentille-p3b.npz`), `lecture_p3b_v1.py` ; Q : Q-12, Q-19 | corrections 1 à 3 en mots exacts. Conséquences, mots de ce rédacteur : « items (i) à (vi) » à l'étape 2.3, dans « Ce que la passe garde » et dans les sorties du plan ; P3b-P7, colonne du signe : « (v) et (vi) : aucun a priori écrit » ; Plan, point 7 : « copie, transformation et valeur calculée ». Totaux du devis fondus avec CR2-texte-12 (voir cette ligne) |
| CR2-P3b-methode-05 | accepté | T : T4 résiduel (h_t) ; double comptabilité (H_t) ; Pl : `residuel_p3b_v1.py` (rôle et test) ; Q : Q-28 | mots exacts aux deux endroits ; test « référence vide » ajouté au plan |
| CR2-P3b-methode-06 | accepté | T : Reconstitution (jeton de fin, contrôle négatif, lecture de M-P3b-2) ; Plan, point 6 (graine `reconstitution/controle-negatif`) ; D : § 6 ; Pl : `reconstitution_p3b_v1.py` (mode M-P3b-2, tests) | corrections 1 à 3 en mots exacts. Au devis, (3) fondu avec CR2-texte-07 (4) : « pour les tâches lues seulement » et « l'empreinte de trajectoire des fiches » (§ 6 et repli (A) de N-032). Tests du plan, mots de ce rédacteur : jeton de fin non déterminé, tirage par graine en proportion égale par condition, identifiant fixé égal à l'original (artefact) |
| CR2-P3b-methode-07 | accepté | T : Plan, point 4 (z, oracle, « non au-dessus » de l'oracle) ; Pl : `lecture_p3b_v1.py` | mots exacts |
| CR2-P3b-methode-08 | accepté | T : « Réserves de robustesse reprises de l'addendum 1 » (trois remplacements) ; Pl : `lecture_p3b_v1.py` | mots exacts. Fusion avec CR2-texte-05 (2) : dans le repli (B) de P-023, le passage remplacé par « pour T1 établi » est la phrase neuve de methode-08 (l'ancienne n'existe plus) |
| CR2-P3b-methode-09 | accepté | T : Oracle, puce « placebo de l'oracle » ((a), (b)) ; T4 résiduel ((c)) ; Pl : `oracle_p3b_v1.py`, `residuel_p3b_v1.py` | (a) et (b) en mots exacts, placés à la fin de la puce du placebo (le rapport ne nomme pas l'endroit) ; (c) après « appliqué au cinquième ; » |
| CR2-P3b-methode-10 | accepté | T : Bandes de couches ; lentille (ℓ = 0 à 31 ; garde d'identité) ; Pl : constantes, `lentille_p3b_v1.py` ; Q : Q-13, Q-14 (tranchée), Q-15 | mots exacts ; l'ajout « après « au même jeton » » précède la parenthèse existante : deux parenthèses se suivent, laissé tel quel |
| CR2-P3b-methode-11 | accepté (information ; mots du rapport appliqués) | T : Synthèse, troisième ligne (forme ; bases de lecture et leur repli (B) de P-016) ; repli (B) de P-023 (deux écarts déclarés ; tranches de T4 de P3) ; Q : Q-26, Q-28, Q-29 | « les deux sondes génériques en G2, G2a ou G2b » : mots exacts ; bases de lecture : mots de ce rédacteur, avec la version (B) de P-016. Des trois mots à ajouter au repli (B), les deux qui portent « (écart déclaré) » entrent dans la liste des écarts du repli ; le troisième, « T4 de P3 avec les tranches recalculées dans chaque tirage (A4 (a) de l'addendum 1) », sans cette mention, est lu comme un alignement sur la proposition : il remplace « `detection_stratifiee` » (quintiles fixes) dans la puce T4 de P3 du repli (fusion avec CR2-texte-05 (3)). Lecture à confirmer par la vérification courte |
| CR2-P3b-methode-12 | information | — | rien à changer |
| CR2-P3b-texte-01 | accepté | T : replis (C) et (B) de P-023, renvoi à la liste d'arrêt | mots exacts aux deux endroits |
| CR2-P3b-texte-02 | accepté | T : en-tête (GO de calcul, borne) ; Métrique (base de lecture ; leurre) ; Plan, point 1 | mots exacts ; dans la même phrase de l'en-tête, renvoi `devis-P3b-v3.md` |
| CR2-P3b-texte-03 | accepté (traitement, décision 3) | Pl : `sceller_p3b_v1.sh` ; T : renvois après la table O et dans la liste d'arrêt ; tableau hors périmètre (trois cellules) ; Q : Q-23 | mots exacts. Conséquence : la règle générale de CR2-texte-04 contient elle-même « en attente » et « de repli » (voir cette ligne) |
| CR2-P3b-texte-04 | accepté | T : en-tête, puce « Statut » ; Q : Q-23 | mots exacts, plus deux ajouts de ce rédacteur : « Version (A), recommandée : » dans la liste des étiquettes (étiquette de la puce « Partition », absente de la liste) ; une phrase qui retire au candidat la règle elle-même et la dernière phrase de la puce « Partition », qui contiennent « en attente » ou « de repli » et seraient refusées au scellement (fusion avec CR2-texte-03) |
| CR2-P3b-texte-05 | accepté | T : repli (B) de P-023 | (1) à (5) en mots exacts, avec ces changements déclarés : clauses de (3) réordonnées (retraits dans G6, O5 et H-P3b-1 avant le renommage « T4 résiduel » → « T4 de P3 », sinon les chaînes à retirer n'existent plus) ; retraits ajoutés : branches « non établi (spécification) » de G6 et O5 (CR2-methode-02) et parenthèse de H-P3b-1 (sinon « **T4 de P3** (T4 de P3 corrigé du coût…) ») ; puce T4 de P3 : « `detection_stratifiee` » remplacé par « tranches recalculées dans chaque tirage, forme A4 (a) de l'addendum 1 » (CR2-methode-11) ; la puce « choix » étant remplacée, « validation croisée interne en 5 plis de 4 tâches de découverte et critère inchangés » ajouté (sans quoi le repli perdait la règle de choix) ; (2) fondu avec CR2-methode-08 |
| CR2-P3b-texte-06 | accepté | T : « Ce que P3b ne revendique pas », après les replis (b) et (c) de N-031 ; Q : Q-01 | mots exacts |
| CR2-P3b-texte-07 | accepté | T : M-P3b-2 (texte principal, replis (A) et (B)) ; liste d'arrêt ; Chaîne, Ordre ; D : § 6 ; Pl : `controles_avant_depense_p3b_v1.sh`, § 4 ; Q : Q-03 | (1), (2), (4) en mots exacts. (3) fondu avec CR2-texte-11 : celui-ci insère « réponses de Lazar ou défauts échus … ; » entre « M-P3b-1 (puissance) ; » et « candidat », la chaîne « mesure de conception M-P3b-1 (puissance) ; candidat » n'existe plus ; les replis disent donc « mesure de conception M-P3b-1 (puissance) ; mesure M-P3b-2 avant le scellement (…) ; » à la place de « mesure de conception M-P3b-1 (puissance) ; ». Plan, `controles_avant_depense_p3b_v1.sh` : deux versions au singulier, tâches lues seulement |
| CR2-P3b-texte-08 | accepté | T : Plan, point 5 (crédit) ; repli (C) de P-024 ; Pl : `controle_fichiers_p3b_v1.py` ; Q : Q-21 | (1) mots exacts. (2) la règle (morceaux de 90 Mo, exclusions) est mise dans les guillemets du repli (C) ; l'instruction sur l'étape 2.6 suit, préfixée « En (C), » ; la borne de 100 Mo renvoie aussi à la puce d'arrêt neuve de CR2-texte-14 |
| CR2-P3b-texte-09 | accepté | T : G2a ; Plan, point 8 ; Q : Q-22, Q-23 | mots exacts |
| CR2-P3b-texte-10 | accepté | T : Périmètre, écarts (iv), (vi), (viii) | mots exacts |
| CR2-P3b-texte-11 | accepté | T : Chaîne, Ordre ; Pl : § 4 | mots exacts ; par la décision 6 du traitement, « brouillon 3 ; vérification courte des corrections par deux sous-agents neufs, une par lentille ; » ajouté après le second « traitement » |
| CR2-P3b-texte-12 | accepté | D : en-tête (renvoi « P3 l. … ») ; § 1 ; § 3 (l. 39, total, repli (B) de P-016) ; § 4 | fusion avec CR2-methode-04 (poste (vi), + 0,05 h, décision 2 du traitement) : sommes refaites sur les postes du § 3 : 1,25 à 1,95 h sans la lentille jacobienne, 1,35 à 2,25 avec ; 1,4 à 2,1 USD (1,5 à 2,5) à 1,09 USD de l'heure ; repli (B) de P-016 : 1,15 à 1,75 h (1,25 à 1,95). Borne inchangée : 7,5 USD |
| CR2-P3b-texte-13 | accepté | T : en-tête (historique) ; exposition (rédacteur du brouillon 2 ; puce de la session) | (1) l'en-tête devient celui du brouillon 3 ; l'heure corrigée du brouillon 2 (00:47 à 00:56) est écrite dans l'historique. (2), (3) mots exacts |
| CR2-P3b-texte-14 | accepté | T : liste d'arrêt (deux puces neuves) | mots exacts ; la puce « 100 Mo » suit la puce « axe de longueur 4 096 » (« même suite que la puce précédente ») ; la puce « 150 USD » suit celle des contrôles avant dépense |
| CR2-P3b-texte-15 | accepté | Q : Q-13 | mots exacts |

Constats non appliqués : aucun. Aucune décision de Lazar n'est tranchée : les marqueurs de N-031, N-032, P-016, P-017, P-023 et
P-024 restent, chaque version de repli reste complète à côté de la version recommandée.

## Changements qui ne viennent d'aucun constat

- En-têtes du texte, du devis, du plan et des questions : rédacteur du brouillon 3, heures (`date -u`), versions remplacées
  et leurs empreintes ; historique du texte (brouillon 2, traitement du brouillon 2).
- Exposition : déclaration du rédacteur du brouillon 2 gardée, étiquetée comme telle ; déclaration du rédacteur du brouillon 3.
- Attributions : les lectures du registre et des modules gelés (vers 00:45 UTC) sont rendues au rédacteur du brouillon 2 ;
  « ce rédacteur » devient « les rédacteurs des brouillons 2 et 3 » (Contre-lecture 1, Q-06, Q-27) ou « le rédacteur du
  brouillon 2 » (Q-26, Q-28).
- Renvois : `devis-P3b-v3.md`, `plan-code-et-chaine-P3b-v3.md` ; table du brouillon 2 citée par son chemin.
- Section « Contre-lecture » : entrées 3 et 4 (rapports du brouillon 2, traitement) ; entrée 5 à remplir (vérification courte).
- Questions : ajouts marqués « (brouillon 3) ».

## Points laissés à la vérification courte (lus par ce rédacteur, non changés)

- Les replis citent des chaînes du texte principal (Ordre, G6, O5, réserves) : au candidat, une chaîne citée apparaît plusieurs
  fois tant que les replis restent ; le remplacement se fait sur le texte principal, après le retrait des replis.
- Renvois « (Version de repli … de P-023 : section « Périmètre ».) » dans « Seuil », après la table O et dans la liste
  d'arrêt : retirés au candidat par la règle de la puce « Statut » ; écrits pour la version (A).
- Repli (B) de P-023 : P3b-P2 et P3b-P5 deviennent « T4 de P3 », mais leur a priori parle encore de « recouvrement faible ».
- P3b-P8 ne nomme pas D2b.
- Lignes de longueur inégale (remplacements sans remise en page).
