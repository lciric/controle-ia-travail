# Vérification courte (CM4, R2) — préenregistrement « arène : mélange d'équilibre » v1, brouillon 4, et code v4

**Vérificateur** : sous-agent neuf Sonnet 5.5 (modèle autre que l'auteur, un Opus ; n'a écrit aucun brouillon, aucun code, aucune contre-lecture de ce pilote).
**Date (UTC)** : 2026-11-01, relevé `date -u` à 08:29:06 juste avant l'écriture de ce fichier. Branche `canal/conv-audit-n04`.
**Contraintes tenues** : aucun commit, aucun `.sha256` écrit, aucun fichier existant modifié, rien lu sous `donnees/`, rien lu ni écrit dans `arene-extension-familles-v1/`, aucun `git fetch`, aucun réseau, aucun modèle. Aucune racine neuve employée : seulement des rejeux (le code des essais et du calcul de puissance emploie ses racines gelées 20264301–303 et 20264401, comme à l'écriture) ; mes deux rééchantillonnages personnels ont une graine hors de toute racine du dépôt. Sorties temporaires dans le dossier de travail de la session, pas dans le dossier du pilote (vérifié : aucun fichier nouveau ni `__pycache__` dans le dossier).

## 0. Verdict

**Gelable après corrections.** 0 bloquant, 1 majeur, 2 moyens, 6 mineurs. Le travail est honnête et solide : les 16 constats de la contre-lecture 3 sont traités dans le texte et dans le code, les 97 essais passent, la sortie de puissance se rejoue à l'identique, le calibrage et les chiffres du pilote se retrouvent depuis les JSON, la garde de racines refuse tout ce qu'elle doit. Ce qui doit changer est **uniquement du texte** (pas de nouveau code, pas de nouveau pilote, aucune racine) : la section « temps » (majeur : les deux options offertes à Lazar ne sont pas chiffrées contre l'efficacité réellement mesurée, et l'une d'elles ne règle rien), la ligne de recommandation de S10 (k = 3 écrit, k = 4 en vigueur), et six précisions.

## 1. Empreintes vérifiées

`sha256sum -c` sur tous les compagnons v4 du dossier (code, essais depuis `essais/`, puissance et sa sortie, gel, calibrage, pilote et ses deux parties, audit, assemblage, journaux, PID, LISEZMOI) et sur la contre-lecture 3 : **tous conformes**. Fichiers cités sans compagnon, calculés : brouillon 4 `305911b7ab1945d7…` (conforme au texte demandé ; **pas de compagnon `.sha256`**, voir CM4-07).

| Fichier | Empreinte (début) | Compagnon |
|---|---|---|
| `preenregistrement-…-brouillon4.md` | `305911b7ab19` | absent (CM4-07) |
| `LISEZMOI-arene-melange-v4.md` | `6805d846e5bb` | OK |
| `arene_melange_v4.py` | `70c77fd5c0ec` | OK |
| `essais/test_arene_melange_v4.py` | `2adcf876a09a` | OK (depuis `essais/`) |
| `calcul-puissance-arene-melange-v4.py` | `cf5543a76842` | OK |
| sortie (M4) `calcul-puissance-…-sortie.txt` | `45a7fe3b56d8` | OK |
| `gel-conception-arene-melange-v4.md` | `9e1f25aeaf1c` | OK |
| `calibrage-deltas-arene-melange-v4.json` | `622c3bb44865` | OK |
| `essai-pilote-…-detection.json` (et ses deux parties, `963441f8…`, `11b31596…`) | `4d1fb23f0c72` | OK |
| `audit-essai-arene-melange-v4.json` | `528b5cd4f68b` | OK |
| `assembler-pilote-arene-melange-v4.py` | `406db1c3de37` | OK |
| journaux v4 (`a69e4cef…`) et v4b (`e92f0690…`) | | OK |
| contre-lecture 3 | `7ccc1460d692` | OK |

Les 29 empreintes de 64 caractères citées dans le brouillon 4 ont été recoupées une à une avec les fichiers du dépôt (dossier, `src/controle_ia/{gardes,prereg,scellement,manifeste}.py`, gabarit, brainstorm et réponse « pont » du dossier P-041) : **toutes conformes** sauf la configuration, qui n'est pas un fichier : l'empreinte `3fbb27fc…` est retrouvée en recalculant la forme canonique du bloc JSON du brouillon. La commande `arene_melange_v4.py identite` rend un bloc d'identité identique à celui du texte (code, configuration, quatre bibliothèques, versions).

## 2. Constats

### Majeur

**CM4-01 — Temps : les options offertes à Lazar ne sont pas chiffrées contre l'efficacité mesurée, et N = 80 ne règle rien** (majeur)
- Où : résumé 9, S8, S4, § Plan 5.
- Constat. Le texte est honnête sur le fond : il écrit que 9 000 s exigent une efficacité ≥ 0,67, que 0,51–0,52 a été mesuré, que le run serait « perdu entier », et il déclare la divergence avec R-739 (S8, « Réserve (divergence non résolue avec R-739) »). Mais :
  1. **N = 80** est présenté comme une issue (« fait tenir 9 000 s jusqu'à une efficacité de 0,54 »). L'efficacité mesurée est 0,51–0,52, **sous** 0,54 : à N = 80 le run durerait **9 518 s** (0,51) ou **9 335 s** (0,52), soit 104 à 106 % du délai : il serait coupé aussi. Je recalcule : processeur N = 80 = 0,8 × 12 136 s = 9 709 s ; mur = 9 709 / (2 × e). Le texte donne le seuil (0,54) mais pas la comparaison avec la mesure, ce qui laisse croire que N = 80 résout le problème.
  2. **`timeout 12600`** n'est pas chiffré du tout : seuil d'efficacité **0,48**, mur à 0,51 = **11 898 s** (94 % du délai, marge de 6 %). Pour mémoire, 14 400 s (4 h) exigerait 0,42.
  3. La **durée totale décision + audit** n'est écrite qu'à pleine efficacité (2 h 20) ; à l'efficacité mesurée elle vaut ≈ **16 600 s = 4 h 37** (11 898 + 4 741 s). Le texte écrit 3 h 15 pour la décision seule et 79 min pour l'audit, mais ne les additionne pas.
  4. L'efficacité **0,52 est attribuée à « [M4 § 5, § 8] »** ; (M4) § 8 donne bien 0,51 (audit), mais § 5 ne donne que 0,16 et 0,41 **par lancement** (avec des projections trompeuses « 621 min », « marge −76 % » à 0,16). Le 0,52 est une dérivation du journal v4b (R5) : 2 912,4 / (2 812,4 × 2) = 0,518, que j'ai recalculée. À renvoyer au journal v4b, pas à (M4).
- Correction (texte) : une petite table dans S8 : N (100 ; 80), délai (9 000 ; 12 600 ; 14 400), efficacité minimale (0,67 ; 0,54 ; 0,48 ; 0,42), mur à 0,52 et 0,51 ; dire que N = 80 à 9 000 s échoue à l'efficacité mesurée ; écrire la durée totale décision + audit à l'efficacité mesurée ; corriger le renvoi du 0,52. Lazar tranche en connaissance de cause. Aucun changement de code (le délai est une commande ; N est un champ de configuration : si Lazar choisit N = 80, l'identité est à régénérer, déclaré).

### Moyens

**CM4-02 — La condition de lancement (charge < 0,5 « juste avant le lancement ») ne protège pas** (moyen)
- Où : § Plan 5, S8, résumé 9.
- Constat : la condition est une mesure à l'instant du lancement. Le journal v4b (R2) montre que l'audit d'essai a **démarré à charge 0,3 sur 2 cœurs (machine « calme ») et fini à l'efficacité 0,51** (charge 3 à 6 ensuite, autres sessions). Rien dans le texte ni dans le code ne surveille la charge pendant le run ; un dépassement perd tout (aucun point de reprise partiel, une seule reprise complète). Le texte présente la condition comme suffisante (« Condition de lancement écrite »).
- Correction : écrire que la condition réduit le risque sans l'éliminer (preuve : l'audit d'essai) ; indiquer la conséquence (verdict « non concluant », une seule reprise) ; en faire un argument pour le délai plus long ou N plus petit **avec** délai plus long (CM4-01).

**CM4-03 — S10 : la ligne « Recommandation » dit k = 3, la valeur en vigueur est k = 4** (moyen)
- Où : S10 ; résumé 8 ; résumé 10 (« recommandations inchangées sauf S10, S11, S17 »).
- Constat : la recommandation écrit « k = 3 … règle et repli k = 4 », et les bandes données sont à k = 4 ; que k = 4 soit la valeur à geler ne se lit que dans « Raison » et dans l'intitulé des bandes. Lazar écrit une ligne de gel d'après la ligne « Recommandation » ; S10 est appliqué par le lecteur R13 (seuil de lecture, non épinglé par le code) : un k = 3 gelé avec des bandes à k = 4 (ou l'inverse) serait un écart de scellement.
- Correction : « Recommandation : **k = 4** (k = 3 écrit d'avance ; repli appliqué : taux simulé 0,095 > 0,05) ; bandes ci-dessous ».
- Rejeu : v3 0,323 ; k = 3 **0,095** ; k = 4 **0,025** retrouvés à l'identique (voir § 4). Ma simulation indépendante (autre graine, pilote pris pour population) : 0,309 ; 0,097 ; 0,032.

### Mineurs

**CM4-04 — La liste de ce que Lazar gèle omet le délai de l'audit** (mineur) : S8 contient « Audit … `timeout` à geler par Lazar — À REMPLIR » (recommandation 5 400 s ; je recalcule : 4 830 s de processeur, tient jusqu'à l'efficacité 0,45), mais l'en-tête de « Seuil » et « Rôles » listent « S1 à S3, S5 à S7, S9 à S17 » sans S8 ; le résumé 10 écrit « S1–S17 à geler » puis « S4, S8, S18 décidés » (contradiction de forme). Le validateur arrêterait le scellement (marqueur restant), donc sans danger, mais Lazar peut oublier la ligne. Ajouter « S8 (délai de l'audit) » aux listes.

**CM4-05 — Preuve de l'ordre gel → code → calcul : écrite plus fort que les pièces ne la montrent** (mineur)
- Vérifié par `git show` (sans réseau) : le gel (`9e1f25ae…`) est **identique** aux commits `f65feb1a` (12:51:10 UTC), `c34a06d7` (12:57:30) et `fd37ceb3` ; le code au calibrage (`dcc3e0b9…`) est au commit `c34a06d7` ; le code du pilote (`70c77fd5…`) est au commit `fd37ceb3` ; la seule différence `c34a06d7` → fichier actuel est la ligne 137 (`DELTAS_V4 = None` → `(1.4, 1.6)`), lue par `diff` ; le manifeste du calibrage porte `code_sha256 = dcc3e0b9…` et `gel_v4_sha256 = 9e1f25ae…`. Donc **gel avant calibrage : établi**.
- Mais `f65feb1a` contient **aussi** le premier état du code v4 (`7e65185a…`, 2 176 lignes), les essais et le script de puissance : ce commit ne prouve pas que le gel précède « toute ligne de code » ; cela repose sur le journal (gel 12:43–12:44, code 12:46–13:04), déclaration de l'auteur, plausible et non contredite. Le journal v4b (R1) écrit « attesté par des commits externes » ; le brouillon (§ Plan 6) écrit « avant toute ligne de code v4 (journal v4) et présent au commit `f65feb1a` » : exact, mais la table « Ce qui change » ne dit pas que ce commit contient le code. À préciser en une phrase.
- Texte périmé : la table CM3-08 écrit « Consignation dans `registres/decisions.md` : à faire par conv-audit » ; R-1031 l'a faite (empreinte du gel, racines, règle ; **sans** l'heure de naissance ni les commits). Idem LISEZMOI réserve 8. À mettre à jour.

**CM4-06 — P10 « 0,990 avec son incertitude » suppose les deux δ indépendants** (mineur) : le code (`calcul-puissance…v4.py`, section 4b) tire deux lois bêta indépendantes (δ 1,4 : 0,961 ; δ 1,6 : 0,748) et combine : 1 − 0,039 × 0,252 = 0,990. Les deux δ partagent les mêmes lois cibles par instance, donc la pureté est vraisemblablement positivement corrélée entre δ : la probabilité d'« au moins un δ » est entre 0,961 et 0,990. Ne change pas la confiance 0,95 de P10 ; à écrire (« au plus 0,990 ; au moins 0,961 »).

**CM4-07 — Brouillon 4 sans empreinte compagnon (R6)** (mineur) : `preenregistrement-…-brouillon4.md` n'a pas de `.sha256`, contrairement aux brouillons 1 à 3 ; son empreinte n'est que dans le LISEZMOI v4 et R-1031. Le texte étant non scellé par construction, c'est de forme ; à créer par conv-audit (je n'écris aucun compagnon).

**CM4-08 — Essais des gardes : quelques cas sains hors de l'essai nommé** (mineur) : `test_chaque_garde_a_son_essai` (78 sites, 33 essais nommés) ne prouve que l'existence d'un essai nommé (le brouillon le dit). Trois essais nommés n'ont pas leur cas sain dans la même fonction : `test_jeu_artefact` (le sain est dans `test_jeu_sain`), `test_racines_essai_artefact` (le sain dans `test_racines_essai_sain`, qui vérifie en plus que chaque racine gelée figure dans le texte du gel), `test_cli_calibrage_refuse_autres_instances` (le cas sain 0:48 n'est pas essayé : trop long ; le calibrage réel l'a exercé). Aucun repli silencieux trouvé dans les parties relues. Rien à corriger sauf, si l'on veut, une phrase.

**CM4-09 — « Arbre git propre » avec d'autres sessions dans le dépôt** (mineur) : `creer_manifeste` arrête sur un arbre non propre (`src/controle_ia/manifeste.py` l. 81–84) ; `git status` montre en ce moment des fichiers non suivis d'autres sessions (`pre-pilote-course-2-v1/…`, `prereg/brouillons/…`). Le lancement de la décision exigera de committer ou d'isoler ces fichiers ; à noter au Plan 5 (le champ `commit` des manifestes de pilote désigne déjà un arbre sans le code exécuté, déclaré).

## 3. Les neuf points demandés

| # | Point | Résultat |
|---|---|---|
| 1 | CM3-01 à CM3-16 traités dans le texte **et** le code | Oui, tous (table § 5) ; réserves : CM3-08 (CM4-05), CM3-10 (CM4-01, CM4-02) |
| 2 | R-739 : Q2 gardée et relue (CM3-02) ; S18 = 0,10, N = 100, 9 000 s avec leur raison, postérieurs au pilote v3 | **Oui.** Q2 gardée, lue comme plafond de classe (résumé 5, § n'autorise pas, § Portée, Table 7 ligne 1 « lecture obligée ») ; S4, S8, S18 « DÉCIDÉ (R-739) », avec raison et mention « après lecture du pilote v3 » ; `taux_nonconv_max = 0.1` et `n_instances = 100` dans la configuration dès le premier calcul v4 (pas de rupture d'empreinte). Divergence sur le temps : voir point 8 |
| 3 | Gel : racines 20264001–20264999 écrites avant emploi ; garde | **Oui.** 10 racines gelées (20264101/102, 201/202, 211/212, 301/302/303, 401), toutes dans la plage, bornes exclues, toutes citées dans le gel (vérifié par `test_racines_essai_sain` et par grep) ; gel `9e1f25ae…` identique aux commits `f65feb1a` (12:51 UTC), `c34a06d7`, `fd37ceb3`. **Garde essayée** (module chargé depuis son fichier, `python3 -I -B`, aucun tirage) : refus de 20261311 (pilote v3), 20261296 (calibrage v2), 20261291 (v1), 20261101, 20269741 (contre-lecture 3) avec « déjà employée » ; refus de 20265001, 20265500, 20265999 avec « plage d'une autre session » ; refus de 20264555 (dans la plage v4 mais non gelée), 20264001, 20266000 ; refus de 20261201 et 20261202 sans autorisation ; `gen(20261311)` et `gen(20265500)` refusent avant tout tirage ; `exiger_racines_essai` refuse (20261311, 20261312), (20265001, 20265002) et deux racines égales ; les racines gelées 20264101, 20264401, 20264211 passent. Toutes les racines trouvées dans les anciens brouillons, codes, essais, journaux, JSON v1–v3 et contre-lectures sont dans la liste refusée (recoupement fait). Réserve de précision : CM4-05 |
| 4 | Calibrage : 48 × grille, règle à la lettre, δ = (1,4 ; 1,6), instabilité dite | **Oui.** JSON : 432 tâches = 48 instances (0 à 47) × 9 δ, sans doublon, bras A seul (clés `('A',)`), racine 20264101/102, gel et code `dcc3e0b9…` au manifeste. Moyennes et erreurs-types recalculées : identiques au texte. Règle (`choisir_deltas`, relue) : δ_haut = 1,6 (0,0563 ≥ 0,03 ; 1,8 : 0,0256 < 0,03) ; δ_bas = 1,4 (0,1019 ≥ 0,10) → (1,4 ; 1,6). **L'instabilité est dite** : résumé 3 et S11 (33 % pour le couple retenu, 43 % pour (1,2 ; 1,6), 23 % pour (1,4 ; 1,8) ; 1,4 à 0,15 erreur-type de 10α ; 1,8 à 0,7 erreur-type de 3α). Mon rééchantillonnage (2 000 tirages, ma graine) : 0,446 ; 0,323 ; 0,225. Le texte dit aussi que V(A) au pilote est 0,082 au δ bas (sous 10α) : prédiction réfutée, déclarée |
| 5 | Taux de fausse alerte retrouvés | **Oui, à l'identique** : 0,002 (écarts centrés ; 0,011 à bruit doublé), S10 v3 0,323 / k = 3 **0,095** / k = 4 **0,025** (§ 4) |
| 6 | Essais | **97 réussis, 0 échoué, 0 ignoré** (159,7 s) ; R5 : § 2 CM4-08 |
| 7 | Chiffres du texte = JSON du pilote et sortie de puissance | **Oui** : plus de 40 chiffres recoupés (§ 4) ; aucun écart |
| 8 | Divergence sur le temps | Honnêtement **écrite** (S8 : « divergence non résolue avec R-739 » ; résumé 9 : délai « serait dépassé » ; R-1031 idem). **Chiffrage incomplet** et condition de lancement insuffisante : CM4-01, CM4-02 |
| 9 | S1–S18 | Tous « À REMPLIR par Lazar » avec recommandation, **sauf** S4 (N = 100), S8 (9 000 s, décision) et S18 (0,10), décidés avec raison. Omission de forme : CM4-04 ; ligne S10 : CM4-03. **Validateur** (`controle_ia.prereg.problemes`, brouillon 4) : 2 problèmes, « section vide ou à remplir : Seuil » et « section vide ou à remplir : Contre-lecture » (attendus ; identiques sur le brouillon 3) ; 18 marqueurs « À REMPLIR » dans le texte |

## 4. Rejeux et recalculs

**Rejoué** :
- `essais/test_arene_melange_v4.py` : `PYTHONPATH=src python3 -I -B -m pytest -q -p no:cacheprovider` depuis un dossier temporaire vide, chemin absolu : **97 passed in 159,69 s**. Le décompte « 97 essais » et « 78 gardes » du texte est exact (78 sites `raise GardeArret`, 78 motifs, 33 essais nommés).
- `calcul-puissance-arene-melange-v4.py` sur les deux parties du pilote et l'audit d'essai (`python3 -I -B`, dossier vide, chemins absolus) : sortie de **292 lignes identique ligne à ligne** à (M4) (`diff` vide, empreinte `45a7fe3b56d8…`). Retrouvés : fausse alerte du critère d'audit 0,002 / 0,011 ; S10 0,323 / 0,095 / 0,025 ; P10 0,961 / 0,748 / 0,990 ; valeur nulle de I3 0,7329 (0,0012) contre 0,7345.
- `arene_melange_v4.py identite` : bloc identique à celui du brouillon.
- Validateur et garde de racines (§ 3).

**Recalculé depuis les JSON** (sonde, plus de 40 chiffres) : calibrage (9 moyennes, 9 erreurs-types, règle, stabilité) ; pilote (48 tâches, racine 20264201/202, code, configuration `3fbb27fc`) : V moyens des 8 bras aux deux δ (A 0,0816 / 0,0359 ; B 0,2099 / 0,1746 ; D 0,4440 / 0,3541 ; B′ 0,4464 / 0,3582 ; C3′ 0,4392 / 0,3469 ; C3 0,4034 / 0,3189), B − A +0,1283 / +0,1387, B − C1 +0,0202 / +0,0205, B − C2 +0,0402 / +0,0356, B − C3 −0,1935 / −0,1443, B − D −0,2341 / −0,1795, B′ − D +0,0024 / +0,0042, B′ − C3′ +0,0072 / +0,0114, part pure de B′ 17/24 (0,708) et 14/24 (0,583) avec pureté forcée 17/17 et 14/14, poids de B jamais purs, I3 de A 0,9028 / 0,9444 contre la valeur nulle 0,7345 (formule vérifiée à la main : moyenne de (t − 2)/(t − 1) sur t = 3 … 8), I3 − nul +0,1683 / +0,2099, I1 +0,0020 / −0,0005, temps 60,68 s de processeur par tâche (médiane 59,55 ; maximum 87,26 ; somme 2 912,4 s), non-convergences 3 sur 1 632 (34 par tâche) dont 2 dans la tâche (δ 1,4, instance 13), efficacité de l'union 0,518. Audit d'essai : |c̄| ≤ 0,0011, écart maximal par tâche 0,0097, aucun drapeau (i) ni (ii). Chiffres de tailles de S2 (Q1 0,001–0,005 / 0,002–0,006 / 0,004–0,015 ; Q2 0,005–0,014 / 0,004–0,015 / 0,006–0,024), de S1, S3, S5, S15, bandes S10, rubriques de la Table « Sort » des prédictions du gel (31 branches : 29 tenues, 2 réfutées, comptées une à une) : conformes à (M4) et au gel. Table 5 du texte = `ligne_table5` du code ; Table 1 = `classe_table1` ; classes de `lire_tables` conformes aux Tables 2, 4, 5, 7.
- Moniteur dominant de B′ sur les tâches pures (14/17 aux tours 2 à 4 et 2 au dernier à δ 1,4 ; 12/14 et 1 à δ 1,6) : conforme.

**Simulation indépendante** (graine personnelle, pilote pris pour population, 3 000 tirages) de la fausse alerte de S10 : v3 0,309 ; k = 3 0,097 ; k = 4 0,032 : même ordre que (M4) (0,323 ; 0,095 ; 0,025), même conclusion (repli k = 4, taux sous 0,05).

**Non rejoué** (durées prohibitives ou hors consigne) : le pilote v4 (48 tâches, ≈ 49 min de processeur), l'audit d'essai (≈ 40 min), le calibrage (432 tâches, ≈ 13 min de processeur, 36 min de mur) ; les essais v1 à v3 ; le mode `decision` ; la relecture ligne à ligne des 2 176 lignes du code (lues : configuration, racines et gardes, `valeur_nulle_I3`, `taux_retours`, garde relative de `MoniteurOu`, `choisir_deltas`, `ligne_table5`, `classe_table1`, `lire_tables`, `auditer_tache`, `juger_audit`, `classes_sous_audit`, indicateurs de pureté) ; l'égalité au bit de V(A) en mode léger et complet (affirmée par le gel, non essayée) ; les antériorités (toutes SUPPOSÉ, hors périmètre) ; les chiffres de la contre-lecture 3 (décompte 26/8 de CM3-12 b recopié, non recompté).

## 5. CM3-01 à CM3-17 → traité ?

| Id | Traité (texte et code) ? | Où vérifié | Réserve |
|---|---|---|---|
| CM3-01 | **Oui** | S17 et § Métrique ; `auditer_tache` (choix source et audit réévalués sur un même échantillon, graine commune), `juger_audit` (drapeau (i) \|c̄\| > 0,01), `classes_sous_audit` (drapeau (ii) : classe recalculée et t × erreur-type), `audit_critere = 0.01`, K = 10 ; aucun changement de signe seul ; fausse alerte simulée 0,002 rejouée, repli fixé d'avance non déclenché | bruit estimé sur 5 tâches par δ, puissance 0,76 à 0,010 : déclarés |
| CM3-02 | **Oui** (Q2 gardée, R-739 (1)) | résumé 5, § n'autorise pas, § Portée, Table 7 ; explication « le dernier domine » retirée et contredite par l'indice du moniteur dominant (recompté) ; B′ − D et B′ − C3′ selon la pureté, pureté forcée (`poids_max_min_equilibres`, 17/17 et 14/14) ; « B′ − D ne mesure pas le tirage seul » écrit | témoin « mode », « ou » sur le support de B′, maxout de 73 unités : options laissées à Lazar, non codées, déclarées |
| CM3-03 | **Oui** | valeur nulle 0,7345 (formule recalculée), I3 − nul lu avec son intervalle, Table 5 réécrite = `ligne_table5`, I2 renommé et recopié sans verdict, H et I2 de B et B′ « par moniteur », A bas au δ haut écrit | — |
| CM3-04 | **Oui** | `BRAS_AUDIT` contient A, `PAIRES_AUDIT` contient B − A, `auditer_tours_A` ; déclencheur 9 étendu à P1, P10, P11 ; contrôle de non-unicité pour P10 | I3 de A jamais changé par l'audit (contrôle faible de la forme du cycle) : déclaré dans S17 |
| CM3-05 | **Oui** | S10 : k × é.-t. × √(1/24 + 1/N) ; règle et repli écrits au gel ; rejeu 0,323 / 0,095 / 0,025 | ligne de recommandation : CM4-03 |
| CM3-06 | **Oui** | P10 conditionnelle (1,000) et avec incertitude (0,990 ; 0,961 ; 0,748) | indépendance des δ : CM4-06 |
| CM3-07 | **Oui** | titre « à classe égale contre D, à moniteurs égaux contre C3′ » ; résumé 1 ; § n'autorise pas (511 paramètres par requête, dilution) ; « ou » sur le support de B′ : option Lazar | — |
| CM3-08 | **En partie** | gel committé (`f65feb1a`) ; empreinte épinglée dans le code et exigée par `exiger_gel_v4` (essai `test_gel_v4_sain_et_artefacts` passé) ; R-1031 consigne l'empreinte | CM4-05 (texte périmé, commit qui contient aussi du code, heure non consignée) |
| CM3-09 | **Oui** | S18 = 0,10 décidé, dans la configuration dès le premier calcul v4 (aucune rupture d'empreinte : pilote, essais, puissance sur `70c77fd5…`) ; à 0,05 le pilote v4 se serait arrêté (2/34) — recalculé | — |
| CM3-10 | **En partie** | délai 9 000 s décidé, projection refaite (12 136 s de processeur, 101 min), durée totale écrite à pleine efficacité | CM4-01, CM4-02 |
| CM3-11 | **Oui** | audit d'essai sur 5 tâches par δ, présenté comme essai de fonctionnement et base du bruit simulé | — |
| CM3-12 | **Oui** | (a) chiffres de S2 recopiés de (M4) et recoupés ; (b) décompte v3 corrigé (26 tenues, 8 réfutées, 34) ; (c) `SEUIL_PURETE = 1 − 1e-9`, test `>=` ; (d) sans objet au pilote v4 | décompte (b) non recompté par moi |
| CM3-13 | **Oui** | note au LISEZMOI ; compagnon des essais vérifié depuis `essais/` | — |
| CM3-14 | Sans objet | `resource_tracker` déclaré | — |
| CM3-15 | **Oui** | garde relative écart-type > 10⁻⁶ × max(1, \|moyenne\|) (code l. 569, texte, essai `test_ou_composite_sain_et_artefacts`) | — |
| CM3-16 | **Oui** | recalibrage → (1,4 ; 1,6) ; A bas au δ haut (3,6 α au pilote) écrit | V(A) au pilote au δ bas 8,2 α, sous 10α : déclaré |
| CM3-17 | Positif | reconduit (essais, puissance rejouée, graines, gardes) | — |

## 6. Résumé des comptes

- Bloquants : **0**. Majeurs : **1** (CM4-01). Moyens : **2** (CM4-02, CM4-03). Mineurs : **6** (CM4-04 à CM4-09). Total : 9.
- Essais : **97 réussis, 0 échoué**. Rejeux identiques : sortie de puissance (292 lignes), bloc d'identité, validateur (2 problèmes attendus), garde de racines (13 refus attendus, 3 passages sains).
- CM3-01 à CM3-16 : 13 traités, 2 en partie (CM3-08, CM3-10), 1 sans objet (CM3-14) ; aucun non traité.
- Corrections demandées avant gel (toutes de texte) : CM4-01 (table de temps et durée totale), CM4-03 (S10 = k 4), puis CM4-02, CM4-04 à CM4-07 en une passe ; CM4-08 et CM4-09 à la discrétion de Lazar.
- Ce que le gel ne règle pas : le choix entre garder 9 000 s sous condition, N plus petit avec délai plus long, ou 12 600 s reste à Lazar ; à l'efficacité mesurée, seul un délai d'au moins 12 000 s (N = 100) fait tenir la décision seule.
