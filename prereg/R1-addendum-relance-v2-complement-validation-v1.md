# Complément au rejeu à graine de R1 — validation complète des 147 épisodes résolus — v1

- Auteurs : **fusion des brouillons de session-depot et de conv-audit** (sous-agents de rédaction, Opus 5.5), pour
  Lazar ; **version à contre-lire, non scellée**. Base : le brouillon 2 de conv-audit
  (`brouillons/preuves-mentors-v1/complement-validation-rejeu-v1/R1-addendum-relance-v2-complement-validation-v1-brouillon2.md`,
  branche `canal/conv-audit-n04`, `41d5350ea60f6a989d0354d2ae46fb27676795dad9fc320446ff1889218d5888` ; notes
  `notes-redaction-v2.md`, `429d0e97fd55f347e45255ece17e7079ced5cd51b78845f91ca5f6a0f66af87e`), complété et corrigé par
  l'analyse et le pré-vol de session-depot ; ce que la fusion change est listé à « Fusion ». Nom nouveau (R12).
- Date (UTC) : 2026-11-02 23:20 (`date -u` ; version corrigée après la contre-lecture, « Contre-lecture » ; la version relue,
  `3b7955f1…`, datait du 2 novembre 2026, 19:44 UTC).
- **Texte parent (scellé, non modifié)** : `prereg/R1-addendum-relance-v2.md`
  (`9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059`, « v2 » ci-dessous). Tout ce que ce texte ne change
  pas reste celui de la v2 : méthode, faits établis sur le harnais de P3, mesures, règle gelée de la validation, filtres
  de location, essais.
- **Demande de Lazar** (session conv-audit, 2 novembre 2026) : 18:26 UTC « go finir, arrête de mettre des budgets temps
  et de les couper » et « je ne veux pas de blocage, de résultats non concluants par défaut de conception, de plafond ou
  que sais-je » ; 18:27 UTC « prends des budgets et plafonds très larges » ; 18:53 UTC « Session-depot la relance sans
  budget de temps, sous un texte court. : prepare les ».
- **GO** : `GO-2026-11-02-30` (`registres/go.md` de `main`, ligne 218 au commit `b1d911b5`), calcul, **plafond exactement
  40 USD**, échéance 2026-11-16 ; la ligne annonce « attendu ≈ 6 à 20 USD » et décrit ce passage (même code, résolution
  et table rejouées comme épreuves, table de référence `ead8a668…`). `GO-2026-11-02-26` (15 USD) reste valide mais n'est
  pas utilisé.
- **Portée** : la seule **étape 0 (validation à l'aveugle des 147 épisodes résolus)**, refaite entière, sans budget de
  temps qui coupe et sans borne de travail qui fasse perdre un épisode avant d'avoir épuisé la frontière écrite du repli.
  Le script d'instance, inchangé, rejoue ensuite la résolution des 7 et une table sous un nom neuf : **lues comme épreuves
  de répétabilité seulement**. La table v3 de référence reste `prereg/R1-table-tokenisation-v3.json`
  (`ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423`).
- Commit du code d'analyse : `c2a8b6e1297a3134b49ec5b2aeb1849eddc4b98d`
  (commit du passage du 2 novembre ; **aucun fichier de code, d'essai ni de script n'est changé**). **Commit lancé** : le
  commit de scellement de ce texte, sur la branche `prep/r1-complement-v1`, qui descend de
  `ab8088424c1c50ea6cebba9cdc318498adf07a3e` (tête de `calcul/r1-resolution-graine-v1` : sorties du 2 novembre et table de
  référence), elle-même descendante de `c2a8b6e1` ; arbre gelé identique (`git diff --quiet` sur les chemins gelés rend 0).
  **Pas sur `main`** : au commit `b1d911b5`, `main` n'a ni le module, ni ses essais, ni le script (35 fichiers de l'arbre
  gelé de `c2a8b6e1` y manquent) ; `exiger_code_cite` y arrêterait l'étape.
- Empreintes du code au commit cité (inchangées depuis la v2) : `src/controle_ia/runs_nuit/resolution_graine_v1.py`
  `cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663` ; `src/controle_ia/runs_nuit/resolution_graine_lot_v1.py`
  `5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156` ; `scripts/r1_resolution_graine_instance_v1.sh`
  `da07025f5cae92cc0041a234a1a3951f33cd42e86da808befbaaedd7d5351cc8` ; `scripts/amorce_instance_r1_resolution_graine_v1.sh`
  `dc8164e2cc44b9d05925dfb4a880f898b3f5dc0466ed1acec52e0291cd516478`.
- Chemin de la configuration de la résolution à graine : `prereg/R1-graine-config-complement-v2.json`
  (fichier `1b6f943c7fcd84f4486ab1961efbf4496392a27d61304a36e1ce50e590d545dd`, celui du brouillon 2 de conv-audit, repris à
  l'octet ; 42 clés : la configuration de la v2, sept valeurs changées, liste à « Seuil » ; scellée avec ce texte)
- Configuration de la résolution à graine (empreinte canonique) : `70b0b77135594b8566833c57535086e26379787b2735b8a3372ece2a3922ff5e`
- Configuration de la résolution à graine, lot fidèle (empreinte canonique) : `70b0b77135594b8566833c57535086e26379787b2735b8a3372ece2a3922ff5e`
  (sha256 du JSON canonique, clés triées, comme `empreinte_config` ; un seul fichier pour le cœur et le lot, cité sous les
  deux libellés qu'exige le script ; celle de la configuration de la v2 était `f91716bf…`)
- Entropie : `36410133060804533274328900142752730279`
  (celle du parent ; ce passage ne tire rien ; manifeste `aucun-tirage-propre`)
- Tests attendus : `71`
  (liste `CIBLES` du script, au code cité ; 71 passés le 2 novembre sur l'instance, journal, 17:15:51 UTC ; 71 à l'essai
  local de ce texte, « Pré-vol »). Les 71 sont ceux des sept fichiers de la liste `CIBLES` (script, l. 314-315),
  tokeniseur présent ; le script exige « 71 passed » sans test sauté (l. 323). Le seul fichier du cœur, lancé sans
  tokeniseur, en saute 10 (**12 passés, 10 sautés**, constaté à la contre-lecture, point 6.10 ;
  `contre-lecture-complement-pytest-graine-sortie.txt`, `65e2068b8c6da1a6ee24a0672fe0506c6dfb22242d6cdd3eee58920849fb67ab`) :
  un tel essai partiel n'est pas un écart.
- **Documents qui font foi** : la v2 ; sa configuration `prereg/R1-graine-config-v1.json`
  (`0f300925546d886b8408d137903e711af579abb0d5947b1b88a27da894c4070f`) ; table v2
  (`5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`) ; verdict scellé du passage du 2 novembre
  `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md` (branche `canal/conv-audit-n04`,
  `64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68`) ; sorties du 2 novembre, présentes au commit lancé
  (compagnons `.sha256` relus) : validation `diag/20261102-171752-r1-graine-validation/resolution-graine-validation.json`
  (`8e6a49126f37af6020b8bf056e6d35c6d53c7391f6d5d311fa0e6caa1298f773`), son tableau des pas
  `pas-resolution-graine-validation.npz` (`fe2ef360a2444dc518c4e67b1a4623dce091abce636de0a572cacdd26d1142f6`), ses épisodes
  `episodes-validation/000.json` à `146.json`, son manifeste
  (`86e90b3693550e4626b47a9b6adf577b63dcec800e82539dd76a10f0728ee2c9`) ; résolution
  `diag/20261102-175806-r1-graine-resolution/resolution-graine-resolution.json`
  (`674825453a8ce34c8bb6f8cb59a054b37af76d24f5e8b44b06f2c5e59d396079`), son manifeste
  (`0aeb5b58755753a0fce902de0ad9cf97ff4fdaa717d0bbf461dda83f8c200e31`) ; table v3 (`ead8a668…`) ; journal de l'instance
  `traces/r1-graine-20261102-181212-iXsM/journal.txt` (`2e0a0948352731318bec2453429e664184109abc67fe5d9f6fe057fdc745f7f3`) ;
  `registres/depenses.md` et `registres/arrets.md` de `main` au commit `b1d911b5` (instance 58851293 : 1,187 USD de
  l'heure ; après la fin de l'amorce, deux relances refusées par sa garde R12 avant la destruction).

**Statut.** Le 2 novembre, la résolution a retrouvé les 7 épisodes (table v3 complète), mais la validation n'a tenté que
57 des 147 épisodes résolus : le budget d'étape de 2 400 s, dont l'horloge part avant le chargement du modèle, l'a coupée
vers 17:57:53 UTC. Comptes du verdict scellé, qui font foi : **54 retrouvés (40 par la voie directe, 14 par le repli),
3 coupés pendant leur repli (rangs 0 et 20 à leur budget d'épisode de 600 s, rang 56 à l'échéance de l'étape), 90 non
tentés (rangs 57 à 146)** : 93 manqués, tous par une durée. Tout autre compte est faux (« 87 non tentés », écrit dans la
ligne de `GO-2026-11-02-26`, compris). Classe « méthode non transposée », réserve sur HG-2, mesure déclarée incomplète.
Ce texte refait la validation entière : même code, même type de carte, mêmes graines. Il ne lit aucun score et ne touche
à aucune entrée de la table v3. Ses prédictions partent des résultats du 2 novembre (déclaré) ; le passage qu'il
préenregistre n'est lu qu'après son scellement.

## Choix de conception

**Les 147, code inchangé.** Le code exige que la validation porte sur exactement `seuil_validation` = 147 épisodes
(`exiger_compte_validation`, `resolution_graine_v1.py` l. 1156-1160, appelée l. 1531-1532 sur la liste
d'`episodes_de_l_etape`, l. 1396-1405). Ne rejouer que les 93 manqués demanderait du code neuf, des essais et une
relecture. Les 57 tentés le 2 novembre passent d'abord (même liste, même ordre : rangs 0 à 56) ; leurs 54 retrouvés sont
l'**épreuve de répétabilité** qui manquait (le contrôle croisé n'en éprouvait aucune : réserve 3 du verdict). Coût des 54 :
798 s de carte mesurées le 2 novembre (≈ 0,3 USD).

**Repli porté à sa frontière écrite.** Le repli bascule au plus `quasi_egalites_max` = 16 quasi-égalités de l'essai
direct (l. 730), puis, pour chaque rejeu basculé, au plus 16 des siennes après sa bascule (l. 767-770), sur
`bascules_max` = 2 niveaux (l. 736) : sa frontière compte au plus **16 + 16 × 16 = 272** combinaisons, toutes distinctes
(la première bascule fixe la combinaison du premier niveau ; les secondes sont des positions distinctes). Avec
`combinaisons_max` = 272, la borne `essayees >= cmax` (l. 739, 771) ne peut plus arrêter le repli avant qu'il ait essayé
toute sa frontière : **aucun épisode n'est perdu par une borne de travail**. Éprouvé sans modèle (« Pré-vol », point 1) :
avec un rejeu factice qui rend toujours 16 quasi-égalités et jamais l'empreinte de P3, le repli essaie 136 combinaisons
sous la borne de 136 (16 simples, 120 paires sur 256), 272 sous 272 comme sous 10 000. Une manquée signifie alors que la
frontière écrite (deux bascules au plus, vers le second candidat, parmi les 16 quasi-égalités les plus fragiles de chaque
niveau, écart sous 1 nat) ne contient pas le chemin de P3 : une **limite de la méthode**, mesurée, non un plafond.

**Durées : gardes contre une boucle folle seulement, jamais un couperet.** Au taux observé le 2 novembre (8,3 à 33 s par
combinaison), un épisode qui épuise ses 272 combinaisons coûte au plus ≈ 8 976 s ; la garde d'épisode (14 400 s) est à
1,6 fois ce pire, la garde d'étape (259 200 s, 72 h) au-delà de tout devis. Elles ne sont pas des budgets de mesure : une
garde atteinte serait une anomalie auditée (« Critères »), non une issue prévue. La seule borne qui peut arrêter le
passage est celle de la dépense : les deux tâches planifiées de la session (« Liste d'arrêt »), dont la destruction à
l'heure du plafond du GO, qui est ce plafond exprimé en heures, non un budget de mesure.

**Script : le script complet existant, inchangé, plutôt qu'un script neuf « validation seule ».** Le script d'instance
n'a pas de mode « validation seule » (l. 457-499) ; deux voies étaient ouvertes : ce script entier, ou un script neuf qui
ne lancerait que l'étape validation. Retenu : **le script existant**, le plus sûr et le plus simple :
1. **aucun code neuf** : ce script a tourné sur la carte le 2 novembre, de bout en bout (journal cité) ; un script neuf,
   même tiré de lui, n'aurait été éprouvé que par une répétition jouet et demanderait une contre-lecture de plus ;
2. **un script neuf ne bornerait pas mieux la dépense** : son seul gain aurait été un plafond d'amorce court ; or
   l'instance ne s'arrête que par sa destruction : après la fin de l'amorce, le conteneur redémarre en boucle et reste
   facturé (le 2 novembre, deux relances de l'amorce refusées par sa garde R12 avant la destruction, `registres/arrets.md`) ;
   dans les deux voies, la garde de dépense est celle de la session : deux tâches planifiées (« Liste d'arrêt ») ;
3. la ligne de `GO-2026-11-02-30` décrit ce passage (même code, résolution et table rejouées comme épreuves) ;
4. la résolution rejouée éprouve la répétabilité des 7, que le contrôle croisé n'éprouve pas.

Ce que la voie retenue coûte, déclaré : ≈ 15 min de carte de plus (résolution : 13 min 24 s le 2 novembre ; cibles du lot
et table ≈ 1 min ; ≈ 0,3 USD) ; une table écrite sous un nom neuf,
`TABLE_V3=prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json`, **sous-produit, jamais une référence** (l'étape
validation n'écrit aucune table ; seule l'étape `table` en écrit, l. 1812-1822) ; et un arrêt de dépense pendant une
étape est une destruction, qui perd ce que le script n'a pas encore poussé (il pousse à la fin de chaque étape,
l. 388-395 : pendant l'étape validation, **toute la validation**), là où un plafond d'amorce court aurait poussé les
épisodes consignés, ou qu'un signal `TERM` au processus Python les aurait fait consigner, committer et pousser
(`sur_term`, l. 234-240) : cette dernière voie exige un accès au conteneur, ni posé ni éprouvé (« Liste d'arrêt ») ;
l'alerte à 30 USD sert à obtenir une extension du GO à temps (« Liste d'arrêt »).

**Gardes du commit lancé contre un oubli à la création.** Le commit lancé porte les sorties du 2 novembre et la table de
référence (il descend de `ab808842…`). Le code inchangé arrête donc, sans dépense ou presque (éprouvé au pré-vol) :
- `TABLE_V3` oublié : le nom par défaut, `prereg/R1-table-tokenisation-v3.json`, est au commit : arrêt avant
  l'installation (script, l. 150-151, R12) ;
- `PREREG` oublié (texte v2, configuration v2) : la garde R3 du cœur retient la validation du 2 novembre (même commande,
  même empreinte `f91716bf…`, même arbre gelé, sortie présente) et refuse l'étape (l. 1192-1225), après l'installation
  (≈ 35 min de carte, poids en cache ; davantage sinon : le téléchargement des poids, ≈ 16 Go, précède l'étape
  validation, script l. 332-348 ; rien de calculé) ;
- `BRANCHE` oublié : la branche par défaut existe : arrêt avant l'installation (l. 104-107) ; `PLAFOND_MIN` oublié
  (235 min) : somme des délais non tenue, arrêt avant l'installation (l. 184-187).
Sur `c2a8b6e1` seul, la table de référence et les manifestes du 2 novembre seraient absents : ces deux premières gardes ne
joueraient pas.

## Écarts à la v2

| n° | v2 | Ce texte | Raison |
|---|---|---|---|
| C1 | `combinaisons_max` = `combinaisons_max_validation` = `combinaisons_max_lot` = 136 | **272** (frontière écrite entière) | Aucun épisode perdu par une borne de travail (mot de Lazar, 18:26 UTC) |
| C2 | Durées 600 / 2 400 s (cœur), 900 / 3 600 s (lot) | **14 400 / 259 200 s** (cœur et lot) : gardes contre une boucle folle | « arrête de mettre des budgets temps et de les couper » |
| C3 | Plafond de l'amorce 235 min | **13 055 min**, somme exigée par le script (« Seuil ») ; la dépense est bornée par les deux tâches planifiées de la session (« Liste d'arrêt ») | Le script refuse de partir sous cette somme (l. 178-187) |
| C4 | R3 : une exécution par étape sous la v2 | Ce texte est le texte neuf que la v2 exige pour tout essai de plus | v2, « Seuil » |
| C5 | Résolution et table lues pour la table v3 | Rejouées par le script inchangé, lues comme répétabilité seulement | Pas de mode « validation seule » ; choix argumenté (« Choix de conception ») |
| C6 | Libellés : contrôle croisé, comptes par épisode, cause de durée, horloge | Lus comme à « Corrections de libellé », texte seulement | Verdict, réserves 3 et 6, § 6 |
| C7 | `PREREG`, `TABLE_V3`, `PLAFOND_MIN` décrits par l'amorce « pour l'essai local » | Passés à la création de l'instance, code inchangé | Seul moyen, code inchangé, de lancer ce texte |
| C8 | Commit lancé : `c2a8b6e1` | Commit de scellement descendant de `ab808842…` (sorties du 2 novembre, table de référence), jamais `main` | `main` n'a pas le code ; gardes contre un oubli à la création |

## Hypothèse

- **HC-1 (transposition à frontière entière)** : sous HG-1 à HG-3 de la v2, la passe forcée et son repli, essayé sur
  toute sa frontière écrite, retrouvent l'empreinte de P3 des 147 épisodes résolus.
- **HC-2 (répétabilité)** : même code, même type de carte (A100-SXM4-80GB), mêmes réglages déterministes, mêmes graines :
  les 54 épisodes retrouvés le 2 novembre le sont de nouveau, par la même voie, avec les mêmes bascules, et le journal de
  leurs pas est identique au bit ; de même les 7 de la résolution rejouée.

## Prédiction chiffrée et signe attendu

Base (verdict, § 2 et § 6) : sur 57 tentés, voie directe réussie 40 fois ; 17 échecs de la voie directe, dont 11 sauvés
par une bascule, 3 par deux (au plus 18 combinaisons), et 3 (rangs 0, 20 et 56) qui avaient épuisé leurs bascules simples
et essayé 8, 3 et 31 paires quand le temps les a coupés. Six épisodes sur 57 ont donc demandé au moins deux bascules ; les
quatre retrouvés à deux bascules (dont `honnete/2512.05150v2/e0`, à la résolution) l'ont été en 6 à 23 combinaisons.
Estimation de l'auteur : ≈ 0,6 de chance qu'un épisode du type des trois coupés soit retrouvé dans la frontière entière
(échecs possibles : trois erreurs ou plus, ou une erreur hors de la frontière). Des 90 non tentés, les 3 de C-6 sont déjà
retrouvés (à la résolution) ; sur les 87 autres, ≈ 9 épisodes à deux bascules ou plus sont attendus, dont ≈ 4,6 du type
« coupé ». Manquées attendues : ≈ 1,2 parmi les 3 coupés et ≈ 1,8 parmi ces 87, soit **≈ 3** (entre 0 et 8), **par la
frontière gelée elle-même**, non par une borne de travail.
- **P-C1 (empreintes retrouvées ; signe : R > 54, au plus 6 manquées)** : R ≥ 141, confiance ≈ 0,9 ; R ≥ 144, confiance
  ≈ 0,6 ; **R = 147, confiance ≈ 0,1**. Toute manquée a pour cause la frontière épuisée (ou une contradiction terminale),
  non une durée, confiance ≈ 0,95.
- **P-C2 (classe de la règle gelée)** : **« graines validées », confiance ≈ 0,1** (sous R = 147, les quatre conditions
  d'accord tiennent avec une confiance ≈ 0,95 : sur les 54 retrouvés, accord moyen 0,99222, minimum 0,98608, 28 253 pas
  informatifs, accord informatif 0,97961) ; **« méthode non transposée », confiance ≈ 0,9** ; « méthode transposée,
  graines non validées », ≈ 0,01. Le relèvement à 272 ôte la cause « durée », non la limite de la frontière : une seule
  manquée suffit à la classe « méthode non transposée », **lue sans nœud** (« Critères »).
- **P-C3 (répétabilité des 54)** : 54 retrouvés sur 54, confiance ≈ 0,97 ; même voie, mêmes bascules, même nombre de
  combinaisons, confiance ≈ 0,8 ; journal des pas identique au bit, confiance ≈ 0,7 (autre carte physique, même modèle).
- **P-C4 (voie directe)** : réussie pour ≈ 70 % des 147 (90 à 115 épisodes), confiance ≈ 0,7 ; premier écart de la voie
  directe identique pour les 17 épisodes qui en avaient un, confiance ≈ 0,8.
- **P-C5 (les 3 coupés)** : au moins un retrouvé, confiance ≈ 0,9 ; les trois, confiance ≈ 0,2.
- **P-C6 (étapes rejouées)** : résolution 7 sur 7 par les mêmes voies, identifiants égaux au 2 novembre, contrôle croisé
  « conforme », confiance ≈ 0,9 ; table du sous-produit égale à `ead8a668…` sur les 4 entrées « identifiants »,
  confiance ≈ 0,9 ; les 3 de C-6 retrouvés aussi à l'étape 0, confiance ≈ 0,9 ; lot « sans objet », confiance ≈ 0,9.
- **P-C7 (durée, descriptif)** : étape 0 entre ≈ 2 h et ≈ 28 h (cas « Haut » à la borne haute, hors vie de l'instance), point central ≈ 9 h (« Coût et GO »).
Prédictions, non seuils (R3 : rien n'est relancé pour les atteindre).

## Métrique

Celle de la v2, inchangée (empreintes retrouvées, seule métrique d'un « résolu » ; voies ; causes ; accords ; écarts
contraints ; repli ; classe écrite par `lire_validation` au résultat). En plus, calculées après réception par le lecteur,
sans module du dépôt, sur les sorties scellées des deux passages, par nom d'épisode :
- **répétabilité de l'empreinte (54)** : chacun des 54 retrouvés le 2 novembre l'est de nouveau (champ `empreinte` égal
  à `empreinte_cible`, recalculé, jamais le drapeau seul) ;
- **répétabilité du chemin (54)** : égalité de `voie`, `forcages`, `combinaisons_essayees` ;
- **répétabilité au bit (54)** : égalité ligne à ligne des colonnes `pas`, `rang`, `choix`, `non_contraint`, `candidats`,
  `ecart`, `second`, `marge`, `balayage`, `p_k`, `argmax_p` du tableau des pas (`fe2ef360…` contre le nouveau) ;
- **premier écart de la voie directe** (`erreurs_directes`) : égalité de (pas, rang, trouvé, vrai, écart, marge) pour les
  17 épisodes qui en avaient un ;
- **résolution rejouée** : empreintes, `ids` égaux à ceux de `674825453a…`, contrôle croisé ; table du sous-produit :
  `actions` et `trajectoire_p3` des 4 entrées « identifiants » égales à celles de `ead8a668…` ;
- **C-6** : statut des 3 épisodes de C-6 à l'étape 0 et à la résolution de ce passage ;
- **taux de transposition à frontière entière** (descriptif) : R / 147, et pour chaque manquée le nombre de combinaisons
  essayées par niveau et leurs issues.
Aucune moyenne sur les jetons dans une sonde ; aucun score, aucune activation, aucune étiquette lus.

## Seuil

**Règle de lecture de la validation : la règle gelée de la v2, inchangée** (`lire_validation`, l. 854-886 ; seuils de
`regle_validation` inchangés). R empreintes retrouvées, E = 147 : « méthode non transposée » si E = 0 ou R < E ; sinon
« graines validées » si accord moyen par épisode ≥ 0,95, minimum par épisode ≥ 0,90, pas informatifs ≥ 1 000 et accord
sur eux ≥ 0,90 (mesure absente = condition manquée) ; sinon « méthode transposée, graines non validées ». Aucun seuil
d'arrêt sur une mesure ; la répétabilité se lit à « Critères ».

**Configuration** `prereg/R1-graine-config-complement-v2.json` : la configuration de la v2, 42 clés ; **35 identiques**,
**7 changées** (différences clé par clé avec `R1-graine-config-v1.json`) :

| Clé | v2 | Ce texte | Exigé par le code ? |
|---|---|---|---|
| `combinaisons_max` | 136 | **272** | Choix (frontière entière) ; doit égaler `combinaisons_max_validation` (`exiger_reglages_execution`, l. 1108-1110) |
| `combinaisons_max_validation` | 136 | **272** | Oui, égal à `combinaisons_max` (même garde) |
| `combinaisons_max_lot` | 136 | **272** | Non : le lot n'exige qu'un entier ≥ 0 (module du lot, l. 839-841) ; même frontière que le cœur (l. 708, 714, 749), 272 l'épuise aussi |
| `duree_max_episode_s` | 600 | **14 400** | Non ; doit rester > 0 et ≤ `duree_max_s` (l. 1103-1105 ; script, l. 165-167) |
| `duree_max_s` | 2 400 | **259 200** | Non ; > 0 (l. 1084-1085) |
| `duree_max_episode_lot_s` | 900 | **14 400** | Non ; > 0 et ≤ `duree_max_lot_s` (module du lot, l. 845-846 ; script, l. 168-171) |
| `duree_max_lot_s` | 3 600 | **259 200** | Non ; cohérence avec le cœur |

Inchangées notamment : `seuil_validation` 147, `regle_validation`, `seuil_ecart` 1,0, `quasi_egalites_max` 16,
`bascules_max` 2, `balayages_max` 16, `episodes_resolution` (mêmes 7, même ordre), pièces et empreintes, `mode` « reel ».
272 est accepté par les gardes de configuration du cœur (`exiger_config`, `exiger_reglages_execution`) et du lot
(`exiger_config` du lot), vérifié au pré-vol ; les artefacts `combinaisons_max_validation` ≠ `combinaisons_max` et
`duree_max_episode_s` > `duree_max_s` y arrêtent.

**Ce que le code exige pour un passage de plus (vérifié au code cité et au pré-vol)** : la garde d'exécution unique du
cœur (`exiger_execution_unique`, `executions_anterieures`, l. 1192-1225) ne retient un run antérieur que de même
commande, **même empreinte canonique de configuration**, même arbre gelé et sortie laissée ; celle du lot (module du lot,
l. 968-978), de même commande et même configuration. Une autre empreinte canonique (`70b0b771…` au lieu de `f91716bf…`)
suffit donc : code inchangé. Au pré-vol, sur le commit de ce texte (qui porte les manifestes du 2 novembre), la garde ne
retient aucun run pour la configuration de ce texte (validation, résolution) et arrête pour celle de la v2. Le texte neuf
entre dans les gardes de citation (configuration sous ses deux libellés : cœur, l. 1163-1166, lot, l. 1193 ; entropie,
l. 1723-1726 ; commit cité, `exiger_code_cite`). Le script exige en outre, avant l'installation : « Tests attendus » et
le chemin de la configuration cités une fois chacun (l. 114-124) ; empreinte canonique une fois sous chacun de ses deux
libellés (l. 145-149) ; table `TABLE_V3` absente (l. 150-151) ;
`40 + 2 × (259 200/60 + 10) + 5 + (259 200/60 + 10) + 15 + 5 = 13 055` minutes ≤ plafond de l'amorce (l. 172, 178-187).

**Bornes qui restent, déclarées** : celles de la frontière (deux bascules, vers le second candidat, 16 quasi-égalités par
niveau, écart sous 1 nat) et `balayages_max` = 16 par U+FFFD (aucun U+FFFD dans les 147) ; ce sont des bornes de la
méthode, gelées par la v2, que ce texte ne change pas. Valeurs des gardes de durée : au choix des sessions, sur le taux
observé des 57 épisodes du 2 novembre, non mesurées au-delà.

**R3** : chaque étape sur carte n'est exécutée qu'une fois sous ce texte ; tout essai de plus relève d'un texte neuf.

## Plan d'analyse

**Données et graines** : celles de la v2 (pièces de P3 vérifiées par empreinte ; des scores, seuls les tableaux
d'identité, `jetons` et `jetons_notes`). Graines (R9) : celles de P3, dérivées comme `jouer_p3` (clé
`tache/<identifiant>` du manifeste de P3) ; ce passage n'a aucune graine propre.

**Étape 0** : méthode, repli, aveugle et mesures de la v2, au code cité, avec la configuration de ce texte. **Étapes
rejouées par le script** : résolution des 7 (après la validation de ce passage : `exiger_validation`, l. 1419-1438),
cibles du lot (attendu « sans objet » ; si une cible reste, le lot tourne et n'est lu que pour l'audit), table sous le
nom du sous-produit. Un arrêt de ces étapes n'enlève rien à la validation, committée et poussée par le script avant la
résolution (l. 388-395, 458-465).

**Lecture** (R13) : lecteur neuf, auteur ni de ce texte ni d'un code, sur les sorties scellées : classe recalculée par
la règle gelée ; métriques de répétabilité ; critères ligne à ligne ; verdict scellé, soumis à Lazar.

**Commandes avant la création** (session ; `C` = commit de scellement de ce texte, 40 caractères, poussé) :

```
git merge-base --is-ancestor ab8088424c1c50ea6cebba9cdc318498adf07a3e "$C"            # code 0 exigé
git diff --quiet c2a8b6e1297a3134b49ec5b2aeb1849eddc4b98d "$C" -- . ':(exclude)prereg' \
    ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' \
    ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md'   # code 0 exigé
git ls-tree "$C" prereg/R1-table-tokenisation-v3.json                                    # sortie non vide exigée
git ls-tree "$C" prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json \
    prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json.sha256                       # sortie vide exigée
git ls-remote --exit-code origin refs/heads/calcul/r1-graine-complement-validation-v1    # code 2 exigé
```

**Tâches planifiées avant la création** (session) : les deux tâches de « Liste d'arrêt » créées, listées, consignées
avec leurs identifiants dans `registres/decisions.md` ; `H` calculé et écrit, avec le prix horaire et le prix du disque
de l'offre, dans `registres/depenses.md`.

**Création** : la commande de création du 2 novembre, reprise mot pour mot (offre sous les filtres de la v2, image,
disque, amorce `scripts/amorce_instance_r1_resolution_graine_v1.sh` lue au commit `C` et passée en mode « args »), seules
ces valeurs changées ou ajoutées dans l'environnement de l'instance :

```
GO_ID=GO-2026-11-02-30 vastai create instance <offre conforme> … --env "\
 -e COMMIT=$C \
 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git \
 -e BRANCHE=calcul/r1-graine-complement-validation-v1 \
 -e PREREG=prereg/R1-addendum-relance-v2-complement-validation-v1.md \
 -e TABLE_V3=prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json \
 -e PLAFOND_MIN=13055 \
 -e GH_TOKEN=… -e HF_TOKEN=…" …
```

L'amorce appelle alors, sans autre changement :
`timeout --signal=TERM --kill-after=3m 13055m env COMMIT=$C TRAVAIL=/root/r1graine PLAFOND_AMORCE_MIN=13055 bash amorce-depot/scripts/r1_resolution_graine_instance_v1.sh`,
qui hérite de `BRANCHE`, `PREREG`, `TABLE_V3` et `DEPOT_URL` (éprouvé à l'essai local, « Pré-vol »). Jetons jamais écrits
ni affichés. Un essai local des gardes (`ARRET_AVANT_CALCUL=1`) pousse la branche avant l'installation (l. 190) :
seulement contre un dépôt local nu ou sous un autre nom de branche.

## Corrections de libellé exigées par le verdict (texte seulement, code inchangé)

1. **Contrôle croisé** (réserve 3) : `lecture_controle_croise` (l. 1254-1264) compare, pour les épisodes de la résolution
   à identifiants connus (les 3 de C-6), le statut et l'égalité des identifiants retrouvés à ceux de la table v2 ;
   « conforme » dit que deux voies, chacune prouvée par l'empreinte de P3, donnent les mêmes identifiants (garanti hors
   collision de sha256) ; **il n'éprouve aucune répétabilité**, qui exige le même épisode rejoué deux fois. Ici, elle est
   éprouvée par les 57 tentés le 2 novembre (dont les 54 retrouvés), les 7 de la résolution rejouée, et les 3 de C-6
   (étape 0 et résolution de ce passage contre la résolution du 2 novembre).
2. **Comptes par épisode** (réserve 6 a) : `passes`, `balayages` et `balayages_complets` écrits pour chaque épisode sont
   ceux de l'**essai direct seul** : posés par `sortie.update(…)` l. 726-727 (et l. 716-717 quand l'essai direct finit
   « non résolu »), ils ne sont mis à jour ni par le retour « résolu » du repli (l. 761-765), ni par les retours qui
   suivent le repli (l. 774-781) ; chaque rejeu basculé a son propre compteur (l. 750), sur lequel le plafond de balayages
   s'applique. Passes de toute l'étape : `passes` du résultat (`moteur.passes`, l. 1666) et lignes de progression ; pas
   comptés du chemin retenu : colonne `balayage` du tableau des pas.
3. **Cause de durée** (réserve 6 b) : l'échéance d'un épisode est la plus proche de la sienne et de celle de l'étape
   (`echeance_episode`, l. 662-667) ; « durée : … à l'essai direct » (l. 720) et « durée : budget de l'épisode épuisé
   pendant le repli » (l. 777) se lisent « **échéance de l'épisode ou de l'étape, la plus proche, atteinte** » ; au rang 56
   du 2 novembre (363,86 s sur 600) : **coupé par l'échéance de l'étape**.
4. **Horloge de l'étape** (verdict, § 6, point 2) : partie l. 1734, avant le chargement du modèle (l. 1523) ; échéance
   posée l. 1519 ; sans effet à 72 h, déclaré.
5. **Réserves de la concordance** (réserves 1 et 2), reconduites : lecture par cible du lot (VI-09) sans objet si le lot
   ne tourne pas ; le plafond de 16 balayages repose sur 2 pas comptés sur le chemin de `mention/2605.17899v2/e0`
   (`comptes_reels-sortie.txt`, `a2bd318f…`), 2 aussi sur le chemin retenu au 2 novembre.

## Critères de lecture gelés

Règle unique de la v2 : résolu si et seulement si l'empreinte de trajectoire égale celle de P3. Classe : `lire_validation`.

| Issue observée | Lecture |
|---|---|
| « graines validées » (R = 147, quatre conditions tenues) | **Réserve sur HG-2 levée**, mesure complète (réserves A et B du verdict levées). La table v3 de référence n'est pas réécrite (R12) : sa `lecture_validation` garde la classe du 2 novembre, comme trace ; l'addendum v3 cite le résultat scellé de ce complément et sa classe, qui fait foi pour HG-1 et HG-2 |
| « méthode transposée, graines non validées » | Réserve sur HG-2 levée ; **réserve « graines »** (v2) ; audit (R4) avant l'addendum v3 ; les entrées de la table v3 restent des preuves |
| « méthode non transposée », toutes les manquées de cause « méthode » (frontière épuisée, contradiction terminale, empreinte différente) | **Mesure complète** (réserve B levée) ; **réserve sur HG-2 maintenue, chiffrée** : la passe forcée, à frontière entière, retrouve R épisodes sur 147 ; pour chaque manquée : premier écart de la voie directe, quasi-égalités, combinaisons par niveau et leurs issues, accords. La table v3 reste valide (entrées prouvées par l'empreinte) ; l'addendum v3 avance avec la réserve. **Aucun nœud.** Aucun passage de plus sous ce texte (R3) ; une frontière plus profonde (trois bascules) ou une validation par le lot fidèle relèveraient d'un texte neuf, proposé à Lazar |
| « méthode non transposée », une manquée au moins de cause « durée » | Mesure déclarée incomplète ; **anomalie auditée (R4)** : une garde contre une boucle folle n'aurait pas dû être atteinte ; l'audit lit passes, combinaisons et durée de l'épisode |
| Répétabilité des 54 : 54 retrouvés | **Répétabilité de l'empreinte tenue** (HC-2) |
| Répétabilité des 54 : un au moins non retrouvé (empreinte calculée ≠ empreinte de P3, ou non résolu pour toute cause) | **Audit (R4), réserve sur la reproductibilité**, portée dans l'addendum v3 ; l'audit cherche d'abord une différence d'environnement (carte, pilote, CUDA, cuDNN, `pip-freeze.txt` des deux passages) ; la table v3 reste prouvée |
| 54 retrouvés, mais voie, bascules, combinaisons ou journal des pas différents pour un au moins | Descriptif : « empreinte répétée, chemin numérique non répété » ; comptes rapportés avec l'environnement des deux passages ; limite chiffrée de HG-2, non réserve sur les résultats |
| Résolution rejouée 7 sur 7, identifiants égaux, contrôle croisé « conforme », table du sous-produit égale sur les 4 entrées | Répétabilité de la résolution tenue |
| Résolution rejouée : un épisode non retrouvé, contrôle croisé autre que « conforme », lot exécuté, table du sous-produit absente ou différente | **Audit (R4)**, réserve sur la reproductibilité ; la table `ead8a668…` reste valide ; la classe de la validation de ce passage reste lue telle quelle |
| 3 épisodes de C-6 retrouvés à l'étape 0 et à la résolution | La répétabilité que la v2 prêtait au contrôle croisé est éprouvée, sur ces 3 |
| Audit de symétrie (R4) | Déclencheurs de la v2, inchangés (accord égal à 1 sur tous les pas des 147 ; aucune quasi-égalité sous 1 ; étapes 0 et 1 sous 5 min ; `accord_sur_les_pas` ≤ attendu + 0,02 ; sous les deux autres classes, `accord_informatif` ≤ attendu + 0,10). La répétabilité au bit des 54 est la **prédiction** (P-C3), non un signal de propreté |
| Validation arrêtée (`arret.json` : erreur de chaîne, signal) ou instance détruite par la garde de dépense pendant l'étape | Aucune classe pour ce passage ; la classe du 2 novembre reste ; épisodes consignés et poussés, s'il y en a, comptés et lus pour la répétabilité, rien d'autre (une destruction pendant l'étape validation ne laisse **aucun** épisode poussé : toute la validation est perdue, un texte neuf serait nécessaire pour la refaire) ; mesure déclarée incomplète ; dépense et cause rapportées à Lazar |

Aucune issue ne crée de nœud qui bloque l'addendum v3 (table v3 complète et prouvée) ; les audits (R4) se font avant lui.

## Liste d'arrêt

Celle de la v2 : **erreurs de chaîne seulement** (pièces, sceaux, graines, bibliothèque, carte indisponible, tests autres
que « 71 passed », commits, poussées) ; aucune mesure n'arrête rien, sauf le contrôle croisé du cœur, qui, autre que
« conforme », arrête l'étape table (sans effet sur la validation). Changements :
- **aucun budget de temps qui coupe une mesure** : gardes de durée et délais externes du script (4 330 min par étape)
  contre une boucle folle seulement ; plafond de l'amorce fixé par la somme qu'exige le script (13 055 min) ;
- **avant l'installation** (code 2), en plus de la v2 : table du sous-produit (ou son sceau) au commit ; branche
  `calcul/r1-graine-complement-validation-v1` présente ou non vérifiable ; et les gardes contre un oubli à la création
  (« Choix de conception ») ;
- **avant la création** (session) : une des commandes de « Plan d'analyse » qui ne rend pas l'attendu ; texte,
  configuration ou sceaux absents au commit `C` ; `GO_ID=GO-2026-11-02-30` refusé par la garde de calcul ; une des deux
  tâches planifiées de la garde de dépense absente du listing ; nœud de « Coût et GO » sans décision de Lazar ; aucune
  offre sous les filtres de la v2 (rien n'est loué : nœud porté à Lazar) ;
- **garde de dépense : deux tâches planifiées indépendantes de la session de pilotage** (hors du code ; plafond du GO,
  non une borne de mesure), **créées et constatées (listées) avant la création de l'instance**, consignées avec leurs
  identifiants dans `registres/decisions.md` :
  - (i) **vérification planifiée de la dépense de l'instance**, au plus toutes les heures et à chaque reprise de la
    session ; dépense engagée = durée de vie de l'instance × prix horaire de l'offre (relevé à la création), plus le
    disque (prix relevé à la création, écrit avec le prix horaire dans la ligne de `registres/depenses.md`) ; (a) dès que
    la dépense atteint **30 USD**, ou l'atteindra avant la vérification suivante, message à Lazar (épisodes faits, d'après
    les lignes de progression du journal de l'instance ; dépense ; durée restante estimée ; **demande d'extension du GO
    dès que la durée de vie projetée dépasse l'heure de destruction de (ii)**, « Coût et GO » ; de l'alerte à la
    destruction : ≈ 6,8 h au prix plafond, ≈ 8 h à 1,187 USD/h) ; (b) sans GO étendu, dès que la dépense atteindrait
    **39,5 USD** avant la vérification suivante (dépense engagée + prix horaire × (intervalle + 10 min)) : **destruction
    de l'instance par son identifiant** (R10), consignée dans `registres/arrets.md` ; (c) à la fin de l'amorce (ligne
    « AMORCE … fin » au journal de l'instance), destruction par identifiant au plus tard à la vérification suivante (le
    conteneur redémarre en boucle après la fin et reste facturé) ;
  - (ii) **tâche planifiée unique de destruction par identifiant**, à l'heure `T0 + H`, `T0` = heure de création de
    l'instance, `H = (39,5 USD − dépenses déjà imputées au GO − disque estimé) / prix horaire de l'offre − 15 min`
    (sans dépense imputée ni disque : ≈ 28,2 h au prix plafond, ≈ 33,3 h à 1,187 USD/h, avant la marge ; contre-lecture,
    B1), calculée et écrite dans `registres/depenses.md` à la création ; elle **ouvre une session neuve, indépendante de la
    session de pilotage** (elle n'a besoin que de l'outil Vast et de la clé par nom), détruit l'instance par son
    identifiant et le consigne dans `registres/arrets.md` ; **annulée ou reportée seulement sur GO étendu consigné dans
    `registres/go.md`**. Elle est **le plafond du GO exprimé en heures, non un budget de mesure** : la ligne du GO
    interdit un budget de mesure qui coupe (étape, épisode), pas le plafond de dépense ; elle arrête exactement ce que
    (i) (b) arrêterait, rien de plus.
  - **Constat avant la création** : la session liste les deux tâches, les consigne (identifiants, heures), puis constate
    le premier départ de (i) à la première heure et le consigne.
  - **Conséquence d'une destruction pendant l'étape validation, par (i) ou (ii)** : le script ne pousse qu'à la fin
    d'une étape (l. 388-395 ; aucun épisode n'est poussé avant) : **toute la validation est perdue** ; aucun manifeste
    poussé, R3 ne bloque rien, mais un **texte neuf** serait nécessaire pour la refaire.
  - **Aucun signal par numéro de processus dans ce texte, fait constaté** : les sessions n'ont posé aucune clé d'accès
    au conteneur à la création (amorce en mode « args », point d'entrée `bash`, comme le 2 novembre) et aucun accès à
    l'instance n'a été éprouvé. La voie du brouillon 2 de conv-audit, « `TERM` au processus Python, lu par lignée depuis
    l'amorce (`ps --ppid`, jamais par motif, R10), puis destruction par identifiant » (le script relaie `TERM` au module,
    consigne l'arrêt, committe et pousse les épisodes consignés : `sur_term`, l. 234-240), n'est possible qu'après un
    accès établi et éprouvé une fois sur le cas sain (R5), hors de ce texte. La destruction par identifiant reste donc la
    voie première, avec sa conséquence : perte de ce qui n'est pas poussé (« Choix de conception »).
- **exposition résiduelle, déclarée et portée comme nœud** (« Coût et GO ») : si les deux tâches planifiées échouent et
  que la session est interrompue, rien ne borne la dépense avant le plafond de l'amorce (13 055 min ≈ 217,6 h : ≈ 258 USD
  à 1,187 USD/h, ≈ 305 USD au prix plafond), puis la boucle de redémarrage jusqu'à la destruction. Aucune garde interne
  à l'instance ne peut l'abaisser avec le code gelé : le script refuse un plafond d'amorce sous 13 055 min (l. 178-187,
  pré-vol) ; un `timeout` extérieur posé autour de l'amorce dans la commande de création ne signalerait que le `bash` de
  l'amorce (le `timeout` intérieur, amorce l. 44, place le script et le processus Python dans un groupe de processus
  neuf) et ses orphelins continueraient (contre-lecture, B1). Une borne de compte la réduirait au crédit disponible.
**Ce qui n'est pas un arrêt** : toute classe ; moins de 147 retrouvées ; un épisode « durée » ; un lot « sans objet » ;
une carte, un CUDA ou un cuDNN autres que ceux de P3 (réserves écrites) ; une répétabilité en défaut (lue, auditée).
**Lancement** : texte et configuration scellés ; contre-lecture neuve (R2) traitée ; concordance de conv-audit ; GO valide
le jour même. Dans tous les cas : sorties poussées sur `calcul/r1-graine-complement-validation-v1` ; arrêt de l'instance
par son identifiant (R10), consigné.

## Coût et GO

A100-SXM4-80GB au **prix plafond de 1,40 USD de l'heure** (filtre de la v2 ; le 2 novembre, 1,187 USD/h), plus le disque.
Composantes : mise en place **33 min mesurées** le 2 novembre (16:44:49 → 17:17:52 UTC, dont 25 min 47 s d'essais) ; les
54 ≈ 13 min (798 s mesurées) ; les 3 coupés : au moins les 1 564 s déjà dépensées (mêmes combinaisons, rejouées à
l'identique), au plus ≈ 4,7 h à frontière épuisée (≈ 272 × 25 s, 255 × 33 s et 221 × 8,3 s), point central ≈ 3,4 h ; les
90 autres ≈ 22 min au taux des 54 (14,8 s par épisode), plus les épisodes difficiles parmi eux (≈ 4,6 attendus, de 1 à
≈ 11 ; de ≈ 0,5 à ≈ 2,5 h chacun) ; résolution rejouée ≈ 13 min (13 min 24 s mesurées) ; cibles et table ≈ 1 min ; vie
de l'instance hors amorce : ≈ 2 min avant (2 novembre), au plus une heure après la fin (vérification horaire).

| Cas | Durée de carte | Dépense au prix plafond (à 1,187 USD/h) |
|---|---|---|
| Bas (3 coupés retrouvés tôt, un difficile neuf) | ≈ 3 h | ≈ 4 USD (≈ 3,6) |
| **Central** (≈ 4,6 difficiles neufs, ≈ 1,1 h chacun : ≈ 5,1 h ; 3 coupés ≈ 3,4 h ; mise en place, 54, 90, résolution et table ≈ 1,4 h ; vie hors amorce ≈ 1 h : somme ≈ 10,8 h, arrondie) | **≈ 10 h** | **≈ 14 USD** (≈ 12) |
| Haut, **à la borne haute de ses propres hypothèses** (≈ 9 difficiles neufs menés au bout de leur frontière à ≈ 2,5 h chacun, 272 × 33 s : 22,5 h ; 3 coupés à frontière épuisée : 4,7 h ; mise en place, 54, 90, résolution et table ≈ 1,4 h ; vie hors amorce ≈ 1 h) | ≈ 30 h (29,6 h) | **≈ 42 USD** (≈ 35) : **au prix plafond, au-delà du plafond du GO** (destruction à 39,5 USD ≈ 28,2 h) ; à 1,187 USD/h, sous le point de destruction (≈ 33,3 h) |
| Pire | non borné par les gardes de durée (72 h par étape) | **borné par la tâche planifiée de destruction à l'heure du plafond du GO** (39,5 USD : ≈ 28,2 h au prix plafond, ≈ 33,3 h à 1,187 USD/h, moins les dépenses déjà imputées, le disque et 15 min), sauf GO étendu ; exposition résiduelle à « Liste d'arrêt » et nœud ci-dessous |

Estimation des sessions, sur les 57 épisodes tentés le 2 novembre, non mesurée au-delà ; un prix réel sous le plafond
allonge d'autant la durée couverte. **Conséquence du cas haut** : au prix plafond, un passage à taux lent est détruit
pendant l'étape validation et perd toute la validation (« Liste d'arrêt ») ; l'alerte à 30 USD (≈ 21,4 h au prix
plafond) part donc **avec une demande d'extension du GO** dès que la durée de vie projetée, d'après les lignes de
progression, dépasse l'heure de destruction ; et la session **préfère, à la création, une offre nettement sous le
plafond quand il y en a une** (le 2 novembre : 1,187 USD/h). Dépenses déjà imputées à `GO-2026-11-02-30` : à relever dans
`registres/depenses.md` avant la création ; s'il y en a, les seuils de 30 et 39,5 USD s'appliquent à la somme et `H`
en est réduit. Lancement : `GO_ID=GO-2026-11-02-30` devant la commande ; échéance 2026-11-16 ; après, GO nouveau.

**Nœud pour Lazar, avant le lancement** (dépense de calcul : nœud, aucun défaut après 48 heures). **Décision** : borner
le compte Vast pendant la course, ou accepter l'exposition résiduelle avec les deux tâches planifiées seules. **Enjeu** :
exposition résiduelle si les deux tâches planifiées échouent et que la session est interrompue : **≈ 258 à 305 USD**
(plafond de l'amorce, 13 055 min, au prix réel du 2 novembre et au prix plafond ; contre-lecture, B1), sept fois le
plafond du GO ; une borne de compte (recharge automatique du crédit Vast suspendue pendant la course, crédit laissé
≈ au plafond du GO) la réduirait au crédit disponible. **Options** : (a) suspendre la recharge automatique pendant la
course, crédit laissé ≈ 40 USD (avantage : exposition bornée par le compte, indépendante de toute session et de toute
tâche planifiée ; inconvénient : si le crédit s'épuisait avant la fin, l'instance serait arrêtée par le fournisseur,
comportement non éprouvé par les sessions, et la validation en cours perdue, comme à la destruction) ; (b) accepter
l'exposition avec les deux tâches planifiées seules (avantage : rien à régler sur le compte ; inconvénient : ≈ 258 à
305 USD si les deux échouent). **Recommandation** : (a), confiance ≈ 0,8 (les deux tâches restent en place dans les deux
options). **Décision de Lazar avant le lancement** ; le lancement sans cette décision est un arrêt (« Liste d'arrêt »).

## Pré-vol

Session-depot, 2 novembre 2026, ≈ 19:45 à 20:11 UTC ; processeur, sans réseau ni carte ; comptes seulement (aucun texte,
score, étiquette ni activation de P3). Pièces versées sous `docs/notes/runs-r1-r2-r4-v1/graine-complement-v1/` (sha256
du fichier ; compagnons `.sha256` posés au scellement) :
1. **Frontière du repli** : `frontiere_272.py` (`0372ffed464c7c65a3e8526d5ed0f8b9ada636f60665f622fbeb30a43f119169`), sortie `frontiere_272-sortie.txt`
   (`550f128eaa8b359269f6bc5ad005a479735c701db6b27e49ddded71276fa22aa`) : `resoudre_avec_repli` du code cité, rejeu factice (16 quasi-égalités après chaque bascule,
   jamais l'empreinte de P3) : 136 combinaisons essayées sous la borne de 136 (16 + 120), 271 sous 271, **272 sous 272
   (16 + 256) comme sous 10 000**.
2. **Gardes du code sur l'arbre lancé** : `prevol_complement.py` (`c7f1ffda0372184cb8f925ac8082222b01e7b65c980ace287aa1c902cb472b89`), sortie `prevol-complement-sortie.txt`
   (`31c0520c155196a0bb01b5a33d5857a7eff4ba166c98a82c420b72d5b257dbf2`) ; arbre de travail à `ab808842…`, texte et configuration de cette version ajoutés ; vraies pièces
   de P3 par liens symboliques dans un dossier temporaire, effacé ensuite. Configuration : 42 clés, 7 changées, canonique
   `70b0b771…`, acceptée par les gardes du cœur et du lot ; artefacts arrêtés (`combinaisons_max_validation` 271,
   `duree_max_episode_s` > `duree_max_s`, clé de répétition en mode réel). **R3** : 47 manifestes sous `runs/`, dont les
   deux du 2 novembre ; configuration de ce texte : aucune exécution antérieure retenue (validation, résolution, lot) ;
   configuration de la v2 : arrêt (validation `20261102-171752-…` et résolution `20261102-175806-…` retenues).
   **Citations** : six libellés, une ligne chacun ; `exiger_config_citee` passe (et arrête pour la configuration de la
   v2) ; entropie et commit lus ; `exiger_code_cite` passe ; `problemes()` ne signale que « Contre-lecture ». **Pièces** :
   empreintes vérifiées, agent égal à celui du manifeste de P3 (artefact : révision changée, arrêt) ; ouverture conforme ;
   classement en 56 s : 129 identiques de base, 18 corrigés par la table v2, **147 en validation**
   (`exiger_compte_validation` passe ; artefact 146 : arrêt), 7 en résolution ; les 3 de C-6 aux rangs 119, 126 et 137.
3. **Essai local du script existant** : `essai_local_complement.sh` (`0da65f6a08d8142319bc9f637e8cbfd47dd22a186424f2771b0384606fff6df9`) ; dépôt local nu tenant lieu du dépôt
   distant ; son commit porte l'arbre de `ab808842…` (hors dossiers lourds) plus ce texte et sa configuration, scellés
   dans ce dépôt jetable seulement ; amorce lue au commit ; environnement de l'instance de « Plan d'analyse ». Cas sain,
   `ARRET_AVANT_CALCUL=1` (journal `essai-cas-sain-journal.txt`, `2f71495804ba7f0438dca0ba715f4fc4dc9c4a7c8b148d313126ee8b71a28512` ; sortie de l'amorce
   `essai-cas-sain-amorce.txt`, `20473ba1aacbf3ecccca57e230732a4928eba04cefe1d0a9475e59d763a07ad2`) : variables héritées par le script ; texte lu (71 tests attendus ;
   configuration de canonique `70b0b7713559` citée sous ses deux libellés ; 7 pièces présentes et scellées ; table du
   sous-produit absente ; somme 13 055 min ≤ plafond 13 055 min) ; branche poussée ; **« 71 passed » (972 s sur processeur)** ; arrêt propre
   avant le calcul. Artefacts (`essai-artefacts-sortie.txt`, `4c78a0ce50981cf041410e845fc3f535b2af39cdeacc53d7bf502cb1b3b5aede`) : plafond de 13 054 min et plafond oublié
   (235) : arrêt avant l'installation (code 2) ; `TABLE_V3` oublié : arrêt avant l'installation (table de référence au
   commit, R12) ; `BRANCHE` oubliée : arrêt (branche présente) ; `PREREG` oublié : **le script ne l'arrête pas** (le texte
   v2 passe ses contrôles ; ici arrêt sur l'absence de carte, code 1) : c'est la garde R3 du module qui l'arrête
   (point 2). Deux premières séries d'artefacts, mal montées (sans `ARRET_AVANT_CALCUL` ni `HF_TOKEN` ; puis sous la branche
   déjà prise par le cas sain), rapportées dans le même fichier.

## Ce qui suit

- « graines validées » : réserve sur HG-2 levée ; l'addendum v3 cite la table v3 (`ead8a668…`), le résultat de la
  résolution du 2 novembre (`674825453a…`) et le résultat scellé de la validation de ce complément, avec sa classe.
- toute autre issue : lecture telle qu'écrite aux « Critères » ; l'addendum v3 porte la réserve correspondante ; audit
  (R4) avant lui quand les critères l'exigent.
- dans tous les cas : verdict d'un lecteur neuf (R13), scellé, soumis à Lazar ; aucune étape refaite sous ce texte.
- **La relance de R1 (addendum v3, écrit en parallèle) ne dépend pas de ce complément** : elle part de la table v3
  complète et prouvée ; elle cite la classe de ce complément si son verdict est rendu avant elle, sinon la classe du
  2 novembre avec ses réserves.

## Fusion

Fusion des brouillons de session-depot et de conv-audit. Repris du brouillon 2 de conv-audit : toutes les sections, la
configuration (à l'octet), les prédictions, les critères, le devis. Changé ou ajouté par session-depot :
1. **commit lancé** : descendant de `ab808842…`, sur `prep/r1-complement-v1`, et non « sur `main` » (le brouillon 2) :
   `main` n'a pas le code ; gardes contre un oubli à la création ajoutées (« Choix de conception ») ; commandes avant la
   création complétées (ascendance, table de référence présente) ;
2. **choix du script argumenté** (script existant, contre un script neuf « validation seule », voie que la consigne de
   session-depot ouvrait d'abord ; aucun script neuf n'est versé) : boucle de redémarrage du conteneur constatée le
   2 novembre ; aucun accès au conteneur posé ni éprouvé par les sessions (fait constaté) ; ce que la voie retenue coûte ;
3. **garde de dépense** : décrite comme deux tâches planifiées de la session (vérification planifiée, alerte à 30 USD,
   destruction par identifiant à 39,5 USD avec règle d'anticipation, destruction après la fin ; et, depuis la
   contre-lecture, destruction planifiée à l'heure du plafond du GO) ; le « TERM par PID » du brouillon 2 est retiré
   comme voie de ce texte (aucun accès au conteneur posé ni éprouvé : fait constaté, « Liste d'arrêt » ; voie possible
   après un accès éprouvé, hors de ce texte) ; exposition résiduelle chiffrée et portée comme nœud ;
4. **pré-vol** de session-depot (« Pré-vol ») : frontière de 272 éprouvée sans modèle, gardes R3 et de citation, pièces
   et classement, essai local du script sur ce texte, oublis à la création ;
5. **libellés** : la correction 1 dit ce que le contrôle croisé éprouve ; la 2 cite aussi l. 716-717 et 774-781 ;
6. ligne de `GO-2026-11-02-30` citée au commit `b1d911b5` (ligne 218), et non « ligne 76 » ; prix réel du 2 novembre
   ajouté au devis ; « Ce qui suit » : indépendance de l'addendum v3 ;
7. **HC-2** étendue aux 7 de la résolution rejouée (le brouillon 2 : les 54 seulement) ;
8. **critères** : ligne « Validation arrêtée » étendue à l'instance détruite par la garde de dépense, « épisodes
   consignés et poussés, s'il y en a », « dépense et cause rapportées à Lazar » (et, depuis la contre-lecture, la perte
   de toute la validation) ; « **Aucun nœud.** » ajouté à la ligne « méthode non transposée, cause méthode » et « lue
   sans nœud » à P-C2 ;
9. **devis** : ligne « Pire » passée de « arrêt à 40 USD » à la destruction à l'heure du plafond du GO (39,5 USD), sauf
   GO étendu ; seuils de 30 et 39,5 USD appliqués à la somme avec les dépenses déjà imputées ; colonne au prix réel ;
   vie de l'instance hors amorce ajoutée ; depuis la contre-lecture : cas haut à la borne haute, nœud de l'exposition
   résiduelle ;
10. **statut** : comptes détaillés du verdict (40 directs, 14 par le repli ; rangs 0 et 20 au budget d'épisode, 56 à
    l'échéance de l'étape ; rangs 57 à 146 ; 17:57:53 UTC) ; « 87 non tentés » attribué à la ligne de `GO-2026-11-02-26` ;
11. **documents qui font foi** enrichis : manifestes des deux runs, tableau des pas nommé, journal de l'instance,
    `registres/depenses.md` et `registres/arrets.md` à `b1d911b5` (instance 58851293, 1,187 USD/h, deux relances
    refusées), `GO-2026-11-02-26` (15 USD) non utilisé ;
12. **seuil** : garde R3 « et sortie laissée » (cœur, l. 1208-1209) ; paragraphe « 272 accepté par les gardes, vérifié au
    pré-vol » ; résultats du pré-vol sur la garde R3 ;
13. **prédictions** : « sur les 87 autres » au lieu de « sur les 90 − 3 autres » ; « ≈ 3 (entre 0 et 8), par la
    frontière gelée elle-même, non par une borne de travail » ;
14. **amorce** : empreinte `dc8164e2…` citée comme vérifiée, au lieu de « à revérifier au lancement » ;
15. **écart C3** : dépense bornée par les tâches planifiées de la session (« Liste d'arrêt »), au lieu de « par sa
    garde (« Coût et GO ») » ;
16. **après la contre-lecture** (`2ef1f192…`) : corrections B1, I1, I2, I3 et m1 à m6, listées à « Contre-lecture » ;
    elles s'ajoutent aux différences avec le brouillon 2 (garde de dépense à deux tâches, nœud de l'exposition, cas haut
    à la borne haute, accès au conteneur comme fait constaté, lignes du lot remises).

**Avec ces ajouts, la liste est complète** : elle couvre les dix-sept différences de fond relevées à la section 5 de
la contre-lecture (points 1 à 3, 9, 12 à 15 déjà listés aux points 1 à 6 ; points 4 à 8, 10, 11, 16 et 17 ajoutés aux
points 7 à 15) ; la configuration est identique à l'octet au brouillon 2 (`1b6f943c…`) ; rien du fond du brouillon 2
n'est perdu ni contredit. **La concordance de conv-audit se fait sur cette liste.**

## Contre-lecture

- **Version relue** : `3b7955f14d1ace8759c91d387372381eaa38ae6f288664afecdf0acd1d4aeed9` (`3b7955f1…`, commit `2764e6cc` de
  `prep/r1-complement-v1`, 2 novembre 2026, 20:11:18 UTC ; cette version corrigée a une empreinte autre, la version relue
  reste dans l'histoire git) ; **contre-lecture** (R2 ; sous-agent neuf, Fable 5.1, auteur d'aucune pièce ; 2 novembre
  2026, 23:00 à 23:08 UTC) : `docs/notes/runs-r1-r2-r4-v1/graine-complement-v1/contre-lecture-complement-validation-v1.md`
  (`2ef1f19249bd86afbcd2a10b33a6bb7ca5d77940d84f23efdd3ecd465e7f543d`, `2ef1f192…`) ; verdict « scellable après
  corrections précises » : un bloquant, trois importants, six mineurs, tous acceptés ; **corrections apportées** par un
  sous-agent de rédaction (Fable 5.1), détail point par point et différence ligne à ligne dans
  `docs/notes/runs-r1-r2-r4-v1/graine-complement-v1/corrections-apres-contre-lecture-v1.md` et `….patch` :
  - B1 : garde de dépense réécrite en deux tâches planifiées indépendantes, listées avant la création (vérification
    horaire ; destruction unique à `T0 + H`, session neuve, annulée seulement sur GO étendu) ; plafond du GO en heures,
    non budget de mesure ; constat des deux tâches avant la création ; perte de toute la validation dite ; nœud pour
    Lazar sur l'exposition résiduelle (≈ 258 à 305 USD) à « Coût et GO » ;
  - I1 : « Fusion » complétée (points 7 à 16), liste déclarée complète ;
  - I2 : cas « Haut » à la borne haute (≈ 30 h, ≈ 42 USD au prix plafond, ≈ 35 à 1,187 USD/h, composantes détaillées),
    au-delà du plafond du GO au prix plafond ; alerte à 30 USD avec demande d'extension ; « Central » ≈ 10,8 h arrondi ;
    offre sous le plafond préférée ;
  - I3 : « aucun accès aux processus » remplacé par le fait constaté (aucune clé d'accès posée, aucun accès éprouvé) ;
    voie `TERM` par lignée possible seulement après un accès éprouvé (R5), hors de ce texte ; destruction par identifiant
    voie première, conséquence dite ;
  - m1 : date du texte = date de cette version ;
  - m2 : 71 tests de la liste `CIBLES`, tokeniseur présent ; cœur seul sans tokeniseur : 12 passés, 10 sautés ;
  - m3 : lignes du lot (l. 839-841, 845-846 ; 708, 714, 749) remises, vérifiées au code cité ;
  - m4 : « ≈ 35 min, poids en cache ; davantage sinon » ;
  - m5 : prix du disque relevé à la création, écrit dans la ligne de `registres/depenses.md` ;
  - m6 : cette sous-liste (empreinte de la version relue, rapport, corrections).

À REMPLIR. R2 : sous-agent neuf, auteur d'aucune pièce, avant le scellement : ce texte, la configuration
`prereg/R1-graine-config-complement-v2.json` et sa différence avec celle de la v2, le code au commit cité (lignes citées),
le script d'instance et l'amorce, le verdict du 2 novembre, les sorties du pré-vol. Puis concordance de conv-audit sur la
version scellée, avant le lancement.
