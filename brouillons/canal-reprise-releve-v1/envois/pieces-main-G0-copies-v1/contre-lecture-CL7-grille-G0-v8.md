# Contre-lecture R2 n° 7 — `prereg/brouillon-G0-grille-lecture-v8.md` — v1

- Contre-lecteur : contre-lecteur neuf ; je n'ai écrit ni la grille (v1 à v8), ni CL1 à CL6, ni la table de dépendance de G0, ni le mémo, ni la synthèse de repli, ni l'un des avis, ni aucune des preuves que la grille lit. Modèle : Opus 5.5 (`claude-opus-5-5`), **le même modèle que l'auteur de la v8** ; lancé par la lignée conv-audit, autre lignée que session-depot.
- Réserves de neutralité : (i) la préférence « d'un autre modèle que l'auteur de la v8 » (v8 l. 1300-1301) n'est pas remplie, seule l'exigence « autre lignée » l'est ; (ii) ma lignée a écrit la table de dépendance (v4 à v7), le mémo et CL6 : mes avis sur le traitement de CL6, sur DIV-1 à DIV-5 et sur D-G0-15 (ii) (options reprises de la table v7) sont à lire avec cette réserve.
- Début non horodaté (première commande vers 13:00 UTC) ; fin : voir la dernière ligne (`date -u`). Commandes sous `LC_ALL=C.UTF-8` (`locale -a` contient `C.utf8`), GNU grep 3.11, Python 3.13.18. Lecture et calcul seulement : aucun fichier existant modifié, aucun commit, aucun `.sha256` écrit, aucun `git fetch`, aucun appel de modèle ni de réseau. `src/controle_ia` extrait d'`origin/main` par `git archive` sous `/tmp/cl7w` ; essais et scripts sous `/tmp/cl7w/` (hors dépôt, non scellés), lancés depuis des dossiers vides, Python en `-I`.
- Jamais ouverts : `donnees/`, `prereg/P3-consignes-v1.md`, `diag/*/traces`, le contenu des `diag/*/arret.json` (noms seulement), les conclusions des verdicts de `docs/verdicts/` (aucun motif appliqué à leurs lignes : aucune lecture de G0 avant scellement). Lu sur la branche `canal/conv-audit-n04` (permis au contre-lecteur, interdit au lecteur de la porte) : la table v7 au commit `4da9ee45`, pour vérifier les passages recopiés.

**Scellable après corrections.**

Une v9 est nécessaire, et les mots de Lazar sur D-G0-1, D-G0-14 (f), D-G0-15 et D-G0-16 devraient porter sur son texte : les corrections changent du texte gelé et les options qu'il tranche. Aucun bloquant ; cinq majeurs ; six moyens ; neuf mineurs. Les dix-sept constats de CL6 sont portés au texte aux endroits que la table « Ce que la v8 corrige » annonce, sans contresens ; trois ne le sont qu'en partie (CL6-02, CL6-06, CL6-07) et le traitement de CL6-09 laisse une fenêtre nouvelle (CL7-07). Aucun des huit critères n'est changé. La v8 ouvre deux voies de sortie du gel de R-765 (CL7-02, CL7-03) et en laisse une troisième (CL7-04). La borne du 31 janvier 2027, étiquetée [EXISTANT], contredit les documents de pilotage, qui disent encore « G0 au plus tard fin novembre 2026 » : nœud pour Lazar (N-1), décrit sans être tranché.

## Empreintes et contrôles

| pièce | empreinte (12 premiers caractères) | contrôle |
|---|---|---|
| v8, copie du dossier des pièces et `origin/main:prereg/brouillon-G0-grille-lecture-v8.md` | `0c2ea83c7dc1` | égales entre elles, à l'attendu et au compagnon `.sha256` d'`origin/main` |
| v7 (`git show origin/main:…`) | `911d79e6d209` | égale au compagnon |
| CL6 (dossier des pièces) | `7092fe4ef735` | égale au compagnon |
| table de dépendance v7 (commit `4da9ee45`) | `2e17b8a538bf` | égale à celle que cite la v8 ; passages recopiés en annexe B : D:1 (l. 13-17), D:4 (l. 31-36), D:5 (l. 37-41) identiques ligne à ligne ; l. 97, 125, 346 présentes telles quelles (script de comparaison) |
| `registres/decisions.md` d'`origin/main` (vivant) | `d85a0e243edf` | N-027 l. 462, R-749 l. 977, R-750 l. 978, R-761 l. 989, R-765 l. 993, R-795 l. 1023, R-796 l. 1024, R-908 l. 1137 lues ; lignes citées par la v8 inchangées |
| brief v2 | `9261932a11f2` | égale à `docs/sha256sums-lancement-v2.txt` ; l. 190-201 = v8 l. 289-300 (`diff` vide) |
| synthèse de repli (dossier des pièces et `origin/main`) | `527f5853ac41` | égales ; l. 13, 36-38, 118-131 lues |
| CL4 (`origin/main`) | `01718af16285` | Q4 (l. 76-90) lue, pour les cinq cas exigés en dossiers synthétiques |
| script M-8.3 extrait de la v8 (l. 1029-1095) | `6007c9483300` | égale à l'annexe G |

`controle_ia.prereg.problemes` (extrait d'`origin/main`, `python3 -I`) sur la v8 : deux messages, « contre-lecture 6 sans ses deux empreintes » et « contre-lecture 7 sans ses deux empreintes » ; le second est la protection voulue, le premier non (CL7-12). Tables Markdown hors blocs de code : 203 lignes, aucune au mauvais nombre de cellules.

## Réponses aux sept questions

**1. CL6-01 à CL6-17, traités à l'endroit nommé ?** Oui pour tous, sans contresens ; partiels marqués.

| constat | endroit vérifié dans la v8 | jugement |
|---|---|---|
| CL6-01 | l. 445-467, 1164-1183, 1372, 1386 | traité : verdict borné, [EXISTANT] retiré de l'ouverture, lecture tardive réservée à la première lecture, ambiguïté de N-027 portée en D-G0-1 (ii) ; reste : l'heure d'ouverture que CL6-01 (i) demandait n'est fixée par aucune option (CL7-08) ; D-G0-1 (ii) hors format (CL7-09) ; fond : N-1 |
| CL6-02 | l. 339-349, 424-428, 606, 1385, 1503-1507 | traité dans la forme ; **partiel** : le recoupement repose sur une prémisse inexacte et ne joue que dans le sens qui retire le gel (CL7-02) ; (f) ouvre une sortie par (ε) « non » (CL7-03) |
| CL6-03 | l. 606, 1834 | traité ; essai reproduit (question 6) |
| CL6-04 | l. 1168-1183, 1386, 1401 | traité (défaut retiré, options bornées, trois causes sans ouverture à part) ; restes en CL7-08 |
| CL6-05 | l. 9-10, 472-481, 1364-1368, 1389-1432 | traité ; passages fidèles ; restes en CL7-09 (DIV-5) et CL7-10 (section 0) |
| CL6-06 | l. 323, 393, 432-435, 656-660 | **partiel** : la correction proposée par CL6-06 est appliquée, mais « sans effet sur le gel » garde la sortie de R-765 que CL6-06 décrivait (CL7-04) |
| CL6-07 | l. 592-593, 1122-1133 | traité pour les verdicts scellés après la grille ; **partiel** pour les antérieurs, où le motif faux est gardé (écart dit par l'auteur ; CL7-05) |
| CL6-08 | l. 351-352, 556-562 | traité |
| CL6-09 | l. 533-535, 540-542, 552-555 | traité dans le corps ; annexe B D-G0-13 (a) non mise à jour (CL7-06) ; la commande manque les branches fusionnées (CL7-07) |
| CL6-10 | l. 1378, 1384 (b), 1399 | traité |
| CL6-11 | l. 367-370, 1467-1469, 1529-1530 | ordre écrit ; dossiers exigés, non exécutés (question 6) |
| CL6-12 | l. 12-13, 1463-1464, 1470-1472 | traité ; « Grille avant lecture » ne nomme pas les onze choix (CL7-18) |
| CL6-13 | l. 361-365, 1843-1848 | traité ; même défaut réintroduit l. 1129 (CL7-13) |
| CL6-14 | l. 528-531, 542-544 | traité |
| CL6-15 | l. 277-281, 1022-1024, 1035-1080 | traité pour trois motifs et le script ; NFKC change le sens des exposants (CL7-17) ; les autres motifs des verdicts restent hors de la forme normalisée (CL7-14) |
| CL6-16 | l. 723-724, 750-755, 960, 1387 | traité ; limite inexacte et angle mort (CL7-15, CL7-16) |
| CL6-17 | l. 574-578, 1512-1518 | traité ; la forme fermée n'est pas contrôlée par commande (CL7-20) |

**2. CL6-01 et N-027.** La v8 écrit « verdict scellé au plus tard le 2027-01-31 à 23:59 UTC » [EXISTANT, R-750 et R-765] (l. 452-458). `CLAUDE.md` l. 20 et `registres/etat.md` l. 120 d'`origin/main` disent « porte de sortie G0, au plus tard fin novembre 2026, critères inchangés (N-027) » ; `docs/decisions/` ne contient ni N-027, ni N-027 bis, ni aucune mention du 31 janvier 2027 (`git grep` : 0). La borne n'existe qu'au registre (R-749, R-750, R-765), et R-765 renvoie son inscription à « N-027 bis quand tout sera fixé ». Contradiction entre pièces : constat CL7-01 et nœud N-1, non tranché.

**3. Aucun critère changé ?** Vrai. Bloc « Hypothèse » l. 289-300 = brief l. 190-201 = v7 (`diff` vides) ; huit titres de fiches identiques ; `diff` des fiches v7 → v8 : seuls changent F-2.2 et F-2.3 (marqués D-G0-16 (d)), D-G0-2 (e) (D-G0-16 (b)), F-7.1 (D-G0-16 (c)) et le script M-8.3 ; les fiches des critères 1, 3, 4, 5 et 6 sont inchangées. Les lectures qui durcissent (D-G0-16) ou assouplissent (D-G0-14 (f), transition de D-G0-16 (a)) sont marquées [À DÉCIDER] et portées à Lazar.

**4. Erreurs nouvelles de la v8.** CL7-02, CL7-03, CL7-07, CL7-08 (i), CL7-10 (convention non mise à jour), CL7-12, CL7-13, CL7-14 (c), CL7-17, CL7-19 ; CL7-06 est une mise à jour oubliée.

**5. Format des nœuds nouveaux.**

| nœud | une phrase | enjeu | options (avantage, inconvénient) | recommandation et confiance | défaut |
|---|---|---|---|---|---|
| D-G0-1 (ii) | oui (question) | non écrit | « ouverture » ou « verdict » nommées, sans avantage ni inconvénient | non (recommandation de fait « ouverture », l. 447-448, sans confiance) | aucun, juste |
| D-G0-1 (iv) | oui | renvoi à R-796 (3) seulement | aucune | non | aucun, juste |
| D-G0-14 (f) | oui | commun à D-G0-14 | une autre option avec avantage et inconvénient ; celle recommandée sans les siens | oui, 0,6 | « défaut » applicable seulement par D-G0-1 (iv) ; prémisse inexacte (CL7-02) |
| D-G0-15 | deux décisions dans une ligne | oui | oui pour les options rejetées ; non pour (i) et (ii) (a) recommandées (seulement dans le passage recopié de la table) | oui, 0,5 et 0,55 | aucun, juste |
| D-G0-16 | quatre sous-points | oui | oui pour les autres options ; l'inconvénient de (a) recommandé n'est pas dit (CL7-05) | oui, 0,5 à 0,6 | « défaut » applicable seulement par D-G0-1 (iv) |
| DIV-5 | oui | seulement dans le passage recopié | position de la grille sans inconvénient ; « V et C » non défini ; « droit de devis » de la table sans correspondant | oui, 0,6 | aucun, juste |

D-G0-1, D-G0-15 et DIV-5 sont sans défaut, comme R-796 (3) le veut. D-G0-14 (f) et D-G0-16 gardent une colonne « défaut » qui ne joue que si le mot de Lazar sur D-G0-1 (iv) l'accepte : conforme à la lettre de R-796 (3) si (iv) est bien un mot explicite, mais le vocabulaire et la convention de la section 0 le contredisent (CL7-10).

**6. CL6-11 et M-0.7.**

Reste à exécuter avant le scellement (rien ne l'est ; la v8 le dit, l. 1529-1530) :
1. écrire, sceller et garder un script d'énumération de la règle telle qu'écrite (négatif gelant, ordre des sortes, (f), précédence) : l'énumération de CL6 (1 536 combinaisons) n'a pas été conservée et la v8 ne l'a pas refaite ; avec (ε) (sans objet, oui, non, absent) et le recoupement, l'espace grandit ; les « 16 cas oui + prononcé positif » que l'annexe C exige doivent d'abord être retrouvés par ce script ;
2. construire des dossiers synthétiques (dépôt git jetable : pièces fictives et `.sha256` committés, manifestes, `diag/<run>/arret.json`, fichiers d'ouverture), exécutés avec les commandes de la grille par une main qui ne sera pas le lecteur de la porte (section 1, « choix 10 ») : (a) les cinq cas de CL4 Q4 : liste d'arrêt et R4 sans audit ; famille (i) négative par liste d'arrêt, famille (ii) sans verdict ; pièces concurrentes dont une négative ; négatif lu contre un niveau non fixé d'avance (F-3.1) ; défaut de forme « invalide » qui masquerait un négatif ; (b) les 16 cas « oui + prononcé positif » de CL6-02 (attendu sous (f) : non concluant, non gelant) ; (c) les deux recouvrements de CL6-11 ((β) « absent » et ligne de table négative à seuil fixé : attendu « indéterminée ») ;
3. ajouter les cas que la v8 crée et que l'annexe C ne nomme pas : (ε) oui, non, absent × recoupement (aucun `arret.json`, `arret.json` sur le run décisif, sur un run antérieur avorté) × prononcé (négatif, positif, de forme imprévue) ; (β) « oui », (ε) « non » et table négative (CL7-03) ; pièce négative écartée sous (m3) (CL7-04) ; pièce venue d'une branche fusionnée après `C_lecture` (CL7-07) ; règles de transition avant et après la grille (D-G0-14 (e), D-G0-16 (a)) ;
4. sceller les sorties et les citer dans la version suivante (R5 : chaque garde essayée sur un cas sain et sur un artefact). D-G0-15 est une procédure : aucun dossier ne l'éprouve.

M-0.7 corrigée : la grille fournit l'essai (annexe G, l. 1834-1835). Reproduit à l'identique (motifs recopiés des l. 584 et 589 ; « Liste d'arrêt déclenchée : non » en ligne 12 d'un verdict synthétique) :

```
== essai annexe G, cas sain (sans -n, v8) :
non
code=0
== essai annexe G, artefact (avec -n, v7) :
code=1
== recopie avec numéros (v8) :
12:Liste d'arrêt déclenchée : non
== NFD : grep direct (sans NFC_LIT) :
0
== NFD : avec NFC_LIT :
famille=aucune valeur=non
```

Cas hostiles ajoutés (même chaîne) : « Liste d'arrêt déclenchée (i) : oui » → (i), oui ; « … (ii) : non » → (ii), non ; « Arrêt sur résultat (i) : non déterminé » → non ; « Arrêt sur résultat (ii) : non applicable » → non (CL7-11) ; « Liste d'arrêt déclenchée (cf. condition 3 : dose) : oui » → ligne prise, valeur vide ; octet invalide dans le verdict → sortie vide, `PIPESTATUS` = 1 1, lu « absent » (CL7-14). Les essais de `ARRET_CAUSE`, `AUDIT_R4`, `IMPREVU_CL`, doses distinctes, `SIGNE` et du script M-8.3 annoncés à l'annexe G (l. 1836-1841) sont aussi reproduits à l'identique.

**7. Verdict** : en tête.

## Constats

### CL7-01 — majeur — la borne du 31 janvier 2027 est étiquetée [EXISTANT] sans dire qu'elle contredit les documents de pilotage

Lignes v8 : 452-458, 302-304, 1189-1194, 1457-1458.
Défaut : la v8 fait de la borne un « verdict scellé au plus tard le 2027-01-31 à 23:59 UTC » [EXISTANT, R-750 et R-765]. Or `CLAUDE.md` l. 20 et `registres/etat.md` l. 120 disent « porte de sortie G0, au plus tard fin novembre 2026, critères inchangés (N-027) » ; `docs/decisions/` ne porte ni N-027 ni N-027 bis ni le 31 janvier ; au registre, R-749 (l. 977) consigne le mot relayé (« la forme de la clause reste à fixer »), R-750 (l. 978) la confirmation « 31 janvier : go » dans une entrée consacrée aux refus de modèles, R-765 (l. 993) le mot de Lazar sur le gel (verbatim : « … jusqu'au second verdict … : go ») suivi du résumé « Un seul verdict final au 31 janvier 2027 au plus tard … (commun aux trois modèles) » et de « la clause sera inscrite en décision N-027 bis quand tout sera fixé ». La table v7 écrit elle-même que la forme de la clause « reste « à confirmer par Lazar » » (l. 4) et que N-027 bis « n'existe pas encore » (l. 5). La grille ne cite ni `CLAUDE.md` ni `etat.md` et ne dit pas l'écart.
Correction : écrire l'écart dans « Seuil » (seconde lecture) et le porter en D-G0-1, point (v) nouveau, sans défaut ; la seconde lecture ne s'applique qu'après le mot de Lazar qui confirme la borne et son inscription (N-027 bis ; choix 11 « R-750 dans `docs/decisions/` ») ; annexe C point 4 : mise à jour de `CLAUDE.md` l. 20 et d'`etat.md` l. 120, sur ce mot. Le fond est le nœud N-1.

### CL7-02 — majeur — recoupement par `arret.json` : prémisse inexacte, portée trop large ; toute contradiction retire le gel

Lignes v8 : 339-345, 424-428, 606 (M-0.7), 1385 (D-G0-14 (f)), 1531-1535 (annexe D), 1304 ; table « Ce que la v8 corrige », CL6-02.
Défauts : (a) « fichier qu'écrit une garde d'arrêt d'instrument » et « `src/controle_ia/gardes.py` l. 50 » : `gardes.py` l. 49-52 ne fait que composer le motif (`motif_d_arret`) ; le fichier est écrit par les lanceurs pour **toute** exception après le manifeste, « garde, panne (mémoire…), signal TERM » (`environnements/lancer_pilote_a.py` l. 305-306 ; de même `noter_pilote_a.py` l. 220-221, `noter_rejeu_juges_v1.py` l. 649-650, `noter_rejeu_juges_v2.py` l. 650-651, `revalider_pilote_a.py` l. 417-419, `harnais/validation_reelle.py` l. 768-770, `premier_test_ia/run.py` l. 376-377) ; un arrêt sur résultat programmé dans le run par une garde l'écrit aussi. (b) Le recoupement porte sur « chaque run de P (M-0.8 (b)) », soit tout run dont le manifeste cite le préenregistrement : un seul run antérieur avorté (panne, délai TERM ; T0.5 fige un TERM à 270 minutes ; deux runs du 5 octobre de T0.4 ont un `arret.json`) suffit à faire une « contradiction ». (c) Il ne joue que dans un sens : (ε) « non » sans aucun `arret.json` n'est pas une contradiction. (d) Toute contradiction rend « pas de négatif gelant ».
Effet : sous la recommandation de D-G0-14 (f), une réfutation par liste d'arrêt cesse d'être gelante dès qu'un run quelconque de la preuve a planté ; « jamais retenté » (R-765) ne tient plus qu'en l'absence d'incident. Le point est présenté à Lazar sur la prémisse fausse.
Correction : (i) corriger l'attribution ; (ii) restreindre le recoupement au run ou aux runs que le verdict lit (manifestes cités, M-0.4) ; (iii) contradiction dans un sens ou dans l'autre ((ε) « oui » avec `arret.json` sur ce run ; (ε) « non » sans `arret.json` sur ce run) → sorte indéterminée (gelante après la grille, D-G0-14 (e)), non « pas de négatif gelant » ; (iv) annexe C point 6 : les lanceurs de T0.6 à T0.8 consignent un arrêt sur résultat sous un motif distinct, ou l'évaluent hors du run ; (v) offrir cette variante comme option de D-G0-14 (f).

### CL7-03 — majeur — D-G0-14 (f) « d'aucune sorte » : une déclaration non recoupée efface aussi la sorte « table »

Lignes v8 : 342-345, 355-357, 367-370, 1385.
Défaut : (β) « oui », (ε) « non », ligne de table négative à seuil fixé : (f) puis « une preuve sans négatif gelant au sens de D-G0-14 (f) n'est d'aucune sorte » (l. 370) : ni liste d'arrêt ni table, aucun gel, même pendant le report. Le même verdict serait « par table » avec (β) « non » (gelé pendant le report, D-G0-13 (a)) et « indéterminé » avec (β) « absent » (gelé dès la première lecture, D-G0-13 (b)) : la déclaration la moins contrôlée (CL7-02 (c)) est la plus protectrice. De même, (β) « oui », (ε) « oui » et un prononcé négatif de forme imprévue (F-1.1 : `PRONONCE_1` = 0, `LARGE_1` ≥ 1, par exemple une espace insécable) relèvent de (f), sans gel, alors qu'un (β) mal formé rend « indéterminé », gelant. La définition de la sorte indéterminée (l. 355-357, « le verdict prononce un négatif et (β) est « absent » …, ou (β) est « oui » et (ε) « absent » ») ne dit pas si le second membre exige un prononcé négatif (l'annexe C l. 1506 et D-G0-14 (e) le supposent). Une ligne « Arrêt sur résultat » dans un verdict à (β) « non » est ignorée (« sans objet »), sans « forme imprévue ».
Correction : (f) ne retire que la sorte « liste d'arrêt » ; la preuve passe ensuite à « indéterminée » ((ε) « non » non recoupé ; prononcé de forme imprévue pris par `LARGE_1` sur un mot négatif), puis à « table » ; écrire « (β) « oui », (ε) « absent » et un prononcé négatif » ; (ε) présent avec (β) « non » → non concluant (forme imprévue).

### CL7-04 — majeur — l'écart (m3) laisse encore une réfutation par liste d'arrêt sortir de R-765

Lignes v8 : 323, 393, 432-435 ((δ), « sans effet sur le gel »), 656-660.
Défaut : la v8 applique la correction de CL6-06 (non concluant, nom en (δ)) mais écrit que la pièce (m3) est « sans effet sur le gel », et M-0.7 n'est pas appliquée aux pièces écartées. Le défaut que CL6-06 décrivait (« ni geler, … ni déclencher R-765 ») reste : une preuve à négatif gelant écartée sous (m3) ne gèle rien, et une version suivante autorisée avec cause nommée redevient recevable (D-G0-7). Le motif négatif est étroit ; essayé, compte 0 (pièce « libre », ni non concluant ni nom en (δ)) sur « Liste d'arrêt déclenchée : oui », « Critère 2 de G0, famille (i) : non tenu », « Sabotage non mesurable à la dose 0,1 », « Dose-réponse absente pour (ii) », « À corriger avant scellement. » : le critère peut alors rester « tenu ».
Correction : M-0.7 sur tout verdict inventorié par M-0.8, remis ou écarté ; le négatif gelant (liste d'arrêt, indéterminé gelant) d'une pièce écartée gèle comme si elle était remise (même raison que CL5-11 pour une pièce concurrente) ; élargir le motif (au moins `non tenu|liste d['’]arr(ê|e)t d(é|e)clench(é|e)e?s?[^[:alnum:]]{0,4}:[^[:alnum:]]{0,4}oui|à corriger avant`), ou renverser la règle : (m3) libre seulement si la ligne de conclusion porte une forme positive reconnue.

### CL7-05 — majeur — D-G0-16 (a) : pour tous les verdicts existants, un motif R4 connu pour être faux, avec une simple réserve

Lignes v8 : 1122-1133, 1387, 1538-1539.
Défaut : pour tout verdict scellé avant la grille, c'est-à-dire tous ceux d'aujourd'hui, dont ceux des critères 1 et 5, le lecteur applique le motif de la v7 (l. 1131), que CL6-07 a montré faux dans les deux sens. Essayé (1 = « non déclenché ») : « Aucune anomalie de run ; audit R4 déclenché (résultat trop propre) » → 1 ; « Résultat non suspect en soi, mais audit R4 déclenché » → 1 ; « audit R4 non déclenché pour (i), déclenché pour (ii) » → 1 ; « Aucun écart de propreté ; audit de symétrie déclenché à titre de précaution » → 1 ; « Le déclencheur n'est pas atteint » → 0. Un audit déclenché lu « non déclenché » n'exige plus de rapport scellé : le critère peut être « tenu » avec la seule réserve générique « R4 lu par motif non ancré », qui ne change aucun état. À la question de la v8 (l. 1306-1307) : oui, la règle peut masquer un R4. La ligne D-G0-16 de l'annexe B ne dit cet inconvénient que de l'option rejetée, pas de celle qu'elle recommande. Non appliqué aux verdicts réels (aucune lecture avant scellement).
Correction : offrir une option de plus : pour un verdict antérieur à la grille, « non déclenché » seulement sur une forme stricte (une seule occurrence de `d(é|e)clench`, précédée d'une négation, sans `mais`, `;` ni seconde famille) ou avec un rapport d'audit R4 scellé avant `C_lecture` ; sinon « non concluant » ; écrire l'inconvénient de chaque option, dont le coût (rapports d'audit pour des verdicts déjà scellés).

### CL7-06 — moyen — annexe B : D-G0-13 (a) n'est pas mise à jour

Lignes v8 : 1384 contre 540-542 ; 1213-1216.
Défaut : la ligne que Lazar tranche, et que la grille scellée recopie, dit encore « dont le verdict est scellé après le verdict de la première lecture » (la fenêtre que CL6-09 a fermée dans le corps) et « négatif issu de sa liste d'arrêt déclenchée ((β) = « oui ») ou d'une ligne de sa table », sans (ε) ni sorte indéterminée gelante ; la même ligne finit par « « pendant le report » = après `C_lecture` de la première lecture ». Le « Repli », garantie 5 (l. 1214-1216), écrit aussi « c'est-à-dire un négatif … issu de sa liste d'arrêt ou d'une ligne de sa table gelée ».
Correction : recopier en annexe B le (a) du corps (l. 540-542) ; corriger la garantie 5.

### CL7-07 — moyen — la commande « pendant le report » (CL6-09) manque une pièce venue d'une branche fusionnée

Lignes v8 : 533-535, 552-555, 652-654.
Défaut : « pendant le report » = `git merge-base --is-ancestor <C_lecture(1)> <commit du .sha256>`, code 0, et commit différent. Une pièce committée sur une branche partie avant `C_lecture(1)` et fusionnée après n'en descend pas. Essayé sur un dépôt jetable : `is-ancestor C1 X` → code 1 ; `is-ancestor X C1` → 1 (non comptée par la première lecture) ; `is-ancestor X C2` → 0 (comptée par la seconde). La pièce n'est ni gelante au sens de D-G0-13 (a) ni écartable sous (m4). Le dépôt fusionne parfois (R-113 : « fusion de la demande n° 1 dans `main` »).
Correction : « pendant le report » = `! git merge-base --is-ancestor X <C_lecture(1)>` **et** `git merge-base --is-ancestor X <C_lecture(2)>`, pour D-G0-13 (a), (γ) et (m4).

### CL7-08 — moyen — D-G0-15 : raccord à D-G0-1 (ii), heure d'ouverture, état de porte sans verdict R13

Lignes v8 : 455-456, 459-462, 1172-1183, 1386.
Défauts : (i) la recommandation de D-G0-15 (i) laisse reprendre la première lecture « au plus tard avant l'ouverture de la seconde » : si Lazar retient en D-G0-1 (ii) la borne « verdict », un premier verdict en décembre ou en janvier la contredit ; « Lecture tardive » (l. 465-466) prévoit ce cas, D-G0-15 (i) non. (ii) Le « Seuil » renvoie « l'heure limite d'ouverture » de la seconde lecture à D-G0-15 ; aucune option ne la fixe. (iii) Les options (a) et (b) donnent un état de porte « non franchie » sans verdict R13 (R13 : verdict de porte prononcé par un sous-agent neuf) : qui le constate, sous quelle forme scellée, n'est ni dit ni compté comme inconvénient. (iv) « `C_lecture` est le parent » du commit d'ouverture (l. 461) n'est pas conditionné à la coupure du 24 janvier de l'option (a). (v) Avantages et inconvénients des options recommandées absents de la ligne.
Correction : conditionner (i) à D-G0-1 (ii) ; fixer l'heure d'ouverture dans chaque option, ou retirer la phrase du « Seuil » ; écrire la forme du constat « non franchie » sans verdict ; renvoyer la l. 461 à D-G0-15 ; compléter la ligne.

### CL7-09 — moyen — D-G0-1 (ii) et (iv), DIV-5 : hors du format de décision ; une divergence manque

Lignes v8 : 445-448, 474-479, 1372, 1403.
Défauts : voir la table de la question 5. De plus, D-G0-1 (ii) omet que la clause recommandée par la synthèse (l. 123 : « Si le verdict scellé de G0 (R13), rendu au plus tard le 30 novembre 2026 à 23:59 UTC, n'est pas « franchie » … ») et la table v7 (l. 4 : « le verdict de G0 du 30 novembre 2026 (V1) ») lisent déjà « verdict » : divergence non portée parmi les DIV, que Lazar trancherait deux fois ; sous « verdict », l'heure d'ouverture doit être avancée, et rien n'est proposé.
Correction : écrire ces points au format (décision en une phrase, enjeu, options avec avantage et inconvénient, recommandation et confiance, sans défaut) ; ajouter DIV-6 (« ouverture » ou « verdict » au 30 novembre : grille contre synthèse et table) ; définir ou retirer « V et C » ; dire la correspondance de DIV-5 avec les options (a) et (b) de la table.

### CL7-10 — moyen — régime des défauts : la section 0 contredit D-G0-1 (iv)

Lignes v8 : 250-252 ; 1385 (« Délai : défaut au 2026-11-15 ») ; 1387 (« Recommandation : défaut »).
Défaut : la convention, inchangée depuis la v7, dit « Chaque point porte sa recommandation **et un défaut** (annexe B) ; le défaut ne prend effet que si D-G0-1 a reçu un mot explicite de Lazar ». Lue seule, tout mot sur D-G0-1 ferait jouer les défauts, ce que R-796 (3) exclut et ce que « Grille avant lecture » (iv) et l'annexe B (l. 1364-1368) refusent ; elle dit aussi que chaque point a un défaut, alors que D-G0-1, D-G0-15 et DIV-1 à DIV-5 n'en ont pas.
Correction : réécrire la convention selon (iv) ; nommer la colonne « recommandation (applicable en bloc seulement si D-G0-1 (iv)) » ; retirer « Délai : défaut ».

### CL7-11 — moyen — « non » suivi d'un mot est lu « non » (`ARRET_CAUSE`, `ARRET_BETA`, `AUDIT_R4`)

Lignes v8 : 584, 589, 592, 606, 1127.
Essais : « Arrêt sur résultat : non établi », « … : non déterminé », « … : non applicable », « … : non connu à la date du verdict » → non, c'est-à-dire arrêt d'instrument déclaré, donc (f) et aucun gel ; « Audit de symétrie déclenché : non applicable », « … : non vérifié » → non, c'est-à-dire « non déclenché », faux négatif de la garde R4. `ARRET_BETA` se comporte de même.
Correction : après la valeur, n'admettre que ponctuation, parenthèse, tiret ou fin de ligne (`(oui|non)[[:space:]]*([.,;(—–-]|$)`) ; un mot après « non » → valeur absente (indéterminée pour (ε), non concluant pour R4) ; essais à l'annexe G.

### CL7-12 — mineur — l'entrée « Contre-lecture 6 » porte des empreintes tronquées

Lignes v8 : 1287-1291. `problemes` rend « contre-lecture 6 sans ses deux empreintes (brouillon relu et rapport) », en plus de la protection voulue pour CL7 : `sceller_prereg` refuserait de sceller le texte tel quel, et M-0.2 sur la grille (`exiger_prereg_scelle`, l. 482-483) échouerait (`prereg.py` l. 63-76). Correction : écrire `911d79e6d2095aba8582253dbbfb984193c5f5cdac28047d3021025240f3e2cd` et `7092fe4ef735aa0bad0258a0c31ea39c909a583bbce95cd6bca74b7202962ae5`, avec le chemin définitif après versement de CL6 sur `main`.

### CL7-13 — mineur — constat d'état réintroduit dans la partie gelée

Ligne v8 : 1129, « (aucun ne porte cette ligne, annexe G) » : même défaut que CL6-13, avec renvoi à une annexe retirée de la version scellée. Correction : supprimer la parenthèse ; la règle « verdict dont le `.sha256` n'est pas postérieur à celui de la grille » suffit.

### CL7-14 — mineur — robustesse de la lecture normalisée

Lignes v8 : 277-281, 606 ; table « Ce que la v8 corrige », CL6-15.
Essais : (a) un octet invalide dans un verdict fait échouer `NFC_LIT` ; le tube rend le code de `grep` (`PIPESTATUS` = 1 1) et la ligne se lit « absent », sans « erreur d'exécution (code 3) » (R5 : aucun repli silencieux) ; (b) « Liste d'arrêt déclenchée (cf. condition 3 : dose) : oui » est prise par `ARRET_BETA` mais la valeur extraite est vide (le `sed` coupe au premier deux-points) : état non prévu ; (c) seuls `ARRET_BETA`, `ARRET_CAUSE` et `AUDIT_R4` passent par `NFC_LIT`, alors que la table de la v8 écrit « les motifs des verdicts sont lus sur la forme NFC » : un verdict en NFD rend `PRONONCE_1` = 0 et `LARGE_1` = 0, donc le critère 1 « non tenu — absent » (F-1.1).
Correction : `set -o pipefail`, ou `NFC_LIT` dans un fichier et code ≠ 0 → code 3 ; « ligne prise, valeur vide » → absent, écrit ; `NFC_LIT` pour tout fichier lu par un motif.

### CL7-15 — mineur — doses distinctes : la limite dite est inexacte

Lignes v8 : 750-753. Tout nombre de la ligne après les deux-points compte, même dans un segment, et pas seulement « après un « ; » » : « Doses non nulles : 0,2 ; 0,2 (palier 2) » → (c) = 1, (e) = 2 ; « … : 0,1 ; 0,1 (proportion 2 × intensité 3) » → (e) = 3 : deux doses identiques passent. Cas de l'annexe G reproduits (2, 2, 2, 3, 2 ; 1, 1). Correction : ne prendre que le premier nombre de chaque segment (`sed -E 's/^[^0-9]*//' | grep -o -E "^DOSE"`), ou écrire la limite exacte.

### CL7-16 — mineur — `SIGNE` ne prend pas le trait d'union

Lignes v8 : 595, 960. « HC1 : écart attendu -0,05 » (trait d'union ordinaire) → 0, non concluant ; « HC2 : signe non prédit (exploratoire), ni au-dessus ni en dessous du témoin » → 1. Cas de l'annexe G reproduits. Correction : admettre `(^|[^[:alnum:]])-[0-9]`, ou exiger un mot de signe à l'annexe C point 6 ; dire le faux positif.

### CL7-17 — mineur — script M-8.3 : la forme NFKC change le sens des exposants

Lignes v8 : 1022-1024, 1036, 1068-1080.
Essais (arbres synthétiques, scripts de la v7 et de la v8 extraits ; les six cas de l'annexe G reproduits à l'identique) : table « facteur 102 », document « facteur 10² » → v7 « absent » (code 1), v8 « doute typographique » (code 2) ; chiffre introuvable « 12 », ligne de sa source « arXiv:9 : coût 1² unités » → v8 « F-8.2 negatif » (v7 : rien) ; le doute typographique est compté dans « F-8.2 doutes ». Correction : forme NFC et repli explicite des espaces (U+00A0, U+202F, U+2009) au lieu de NFKC ; compteur « M-8.3 doutes » distinct.

### CL7-18 — mineur — conditions du scellement

Lignes v8 : 470-471, 1372 (iii) contre 1463-1464. L'annexe C dit que les onze choix du repli « conditionnent le scellement au même titre » ; « Grille avant lecture » et D-G0-1 (iii) ne les nomment pas. Correction : les y ajouter, ou retirer la phrase de l'annexe C.

### CL7-19 — mineur — horodatage et compte des tables

Lignes v8 : 20, 1827, 1850-1851, 1857. Essais « exécutés … entre 12:20 et 12:40 UTC », fin de rédaction 12:23:44 UTC, commit `e6aa6248` à 12:24:33 UTC ; « Tables : voir la ligne de fin », qui ne porte aucun compte (le mien : 203 lignes, aucune au mauvais nombre de cellules). Correction : heures exactes ; compte écrit.

### CL7-20 — mineur — la forme fermée des verdicts de contre-lecture n'est pas contrôlée par commande

Lignes v8 : 602 (M-0.3 (5)), 1512-1518. « Scellable après corrections ; Lazar doit d'abord trancher D-G0-1. » → conforme (aucun mot d'`IMPREVU_CL`) ; le sens reste « scellable après corrections », sans effet sur l'état, mais la forme exigée n'est pas vérifiée. Correction : pour un rapport scellé après la grille, `<L> | grep -c -i -E "^[*#> -]*(VERDICT_CL)[*]*\."` = 1.

## Nœuds pour Lazar

**N-1 — Date de sortie de G0 : fin novembre 2026 ou verdict final au 31 janvier 2027 ?** (décrit, non tranché ; consigne de cette contre-lecture)
- Ce que disent les pièces : N-027 (registre l. 462, ton mot du 20 octobre) : « la porte G0 se prononce au plus tard fin novembre 2026, sur les critères inchangés » ; `CLAUDE.md` l. 20 et `registres/etat.md` l. 120 le reprennent comme date de sortie de la phase 0 ; `docs/decisions/` ne porte ni N-027 ni N-027 bis. Tes mots du 29 octobre : « 31 janvier : go » (R-750, après le mot relayé de R-749 : « la forme de la clause reste à fixer ») et « go » sur le gel jusqu'au second verdict (R-765), consigné avec « un seul verdict final au 31 janvier 2027 au plus tard » et « la clause sera inscrite en décision N-027 bis quand tout sera fixé ». La grille v8 en fait une seconde lecture finale, verdict scellé au plus tard le 2027-01-31 à 23:59 UTC, étiquetée [EXISTANT].
- Lectures possibles, sans recommandation : (a) N-027 fixe le premier verdict ; R-750 et R-765 ajoutent un report unique dont le verdict final peut tomber jusqu'au 31 janvier 2027 : la sortie de la phase 0 peut alors glisser en 2027, et `CLAUDE.md`, `etat.md` et `docs/decisions/` (N-027 bis) sont à mettre à jour ; (b) N-027 reste la date de sortie et le 31 janvier ne borne qu'une phase de repli sans nouvelle chance de « franchie » : la seconde lecture de la grille perd son objet, et l'on s'écarte du point commun de la synthèse consigné en R-761 (« au second verdict, tout sauf « franchie » … est définitif ») ; (c) une autre forme, fixée avec les onze choix restants.
- Enjeu : existence et mécanique de la seconde lecture (D-G0-13, D-G0-15, champs (γ), motif (m4)) ; date d'ouverture de la phase 1 ; plan financé, qui commence en décembre 2026 avec G0 comme « porte interne avant la période financée » (N-017, R-113) ; scellement de la grille au 15 novembre.

**N-2 — D-G0-14 (f) : à ne pas trancher sur le texte de la v8.** Sa recommandation repose sur une prémisse inexacte (`arret.json` n'est pas propre aux gardes d'instrument) et ouvre deux sorties du gel (CL7-02, CL7-03). Recommandation : attendre la v9, qui devrait offrir une troisième option (contradiction ou déclaration non recoupée → sorte indéterminée, gelante après la grille) ; confiance 0,7.

**N-3 — D-G0-16 (a) : choisir en connaissant le coût caché de la recommandation.** Elle garde, pour tous les verdicts existants (critères 1 et 5 compris), un motif R4 qui lit « non déclenché » des lignes qui disent « déclenché » (CL7-05). Option à ajouter : forme stricte ou rapport d'audit R4 scellé avant la lecture, sinon « non concluant » ; inconvénient : des rapports d'audit à produire pour des verdicts déjà scellés. Recommandation : demander cette option en v9 ; confiance 0,6.

**N-4 — D-G0-1 (ii) : un seul mot pour trois pièces.** La synthèse de repli (l. 123) et la table v7 (l. 4) lisent déjà « verdict au plus tard le 30 novembre 2026 à 23:59 UTC » ; la grille propose « ouverture ». Ton mot sur D-G0-1 (ii) devrait valoir pour les trois (CL7-09) ; s'il retient « verdict », l'heure d'ouverture de la première lecture est à avancer, et D-G0-15 (i) à borner de même (CL7-08).

Pour tous ces points : aucun défaut (R-796 (3)) ; les mots sur D-G0-1 à D-G0-16 et DIV-1 à DIV-5 sont à demander sur le texte de la v9 ; échéance de scellement de la grille inchangée (2026-11-15, D-G0-1).

## Ce que je n'ai pas vérifié

Les contenus des verdicts scellés (règle d'aucune lecture avant scellement) : en particulier, je n'ai pas appliqué le motif de transition R4 aux verdicts réels (CL7-05) ni ouvert les trois `arret.json` (noms seulement, CL7-02) ; la table de dépendance au-delà des l. 1-45, 97, 125 et 346, et son script ; la synthèse au-delà des l. 13, 21-38, 118-131 ; CL1 à CL5 sauf CL4 Q4 ; les motifs que la v8 ne modifie pas (`CRIT_2`, `FAM_I`, `FAM_II`, `BRAS_P`, `AGREG`, `NETTOIE`, `NEG_DEBUT`, `NEUTRE`) ; l'inventaire M-0.8 sur l'état actuel d'`origin/main` ; le rendu des tables ; l'énumération des 1 536 combinaisons, que je n'ai pas refaite.

Fin de rédaction : 2026-10-31 13:17 UTC (`date -u`).
