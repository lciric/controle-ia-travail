# Complément au rejeu à graine de R1 — validation complète des 147 épisodes résolus — v1

- Auteur : sous-agent de rédaction (Opus 5.5), pour Lazar, à la demande de la session qui pilote le rejeu ; **brouillon 1,
  non scellé**. Nom à sceller : `prereg/R1-addendum-relance-v2-complement-validation-v1.md` (nom nouveau, R12 ; l'addendum
  v2 n'est pas modifié).
- Date (UTC) : 2026-11-02 19:02 (heure relevée par `date -u`).
- **Texte parent (scellé, non modifié)** : `prereg/R1-addendum-relance-v2.md`
  (`9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059`), lui-même complément de
  `prereg/R1-R2-rejeu-p3-v1.md` (`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`). Tout ce que ce
  texte ne change pas reste celui de l'addendum v2 (« v2 » ci-dessous) : méthode, faits établis sur le harnais de P3,
  mesures, règle gelée de la validation, filtres de location, essais.
- **Demande de Lazar** (session conv-audit, 2 novembre 2026, 18:26 UTC) : « go finir, arrête de mettre des budgets temps
  et de les couper » ; 18:27 UTC : « prends des budgets et plafonds très larges ».
- **GO** : `GO-2026-11-02-26` (`registres/go.md`, ligne 72), calcul, plafond **exactement 15 USD**, échéance 2026-11-16 ;
  la ligne annonce « attendu ≈ 4 USD » (ce texte : voir « Coût et GO »).
- **Portée** : la seule **étape 0 (validation à l'aveugle sur les 147 épisodes résolus)**, refaite **sans budget de temps
  qui coupe**, sous le même code et la même configuration, durées exceptées. Le script d'instance, inchangé, enchaîne
  ensuite la résolution des 7, les cibles du lot et une table : ces étapes tournent, mais **ne sont lues que comme
  épreuves de répétabilité** ; elles ne remplacent rien (la table v3 de référence reste
  `prereg/R1-table-tokenisation-v3.json`, `ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423`).
- Commit du code d'analyse : `c2a8b6e1297a3134b49ec5b2aeb1849eddc4b98d`
  (commit de lancement du passage du 2 novembre ; arbre gelé identique à celui du commit `0e2a8871…` que cite la v2 :
  `git diff --quiet 0e2a8871 c2a8b6e1 -- <chemins gelés>` rend 0 ; **aucun fichier de code, d'essai ni de script n'est
  changé par ce texte**)
- Empreintes des fichiers de code (inchangées depuis la v2, recalculées sur la copie du commit cité) :
  `resolution_graine_v1.py` `cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663` ;
  `resolution_graine_lot_v1.py` `5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156` ;
  `scripts/r1_resolution_graine_instance_v1.sh` `da07025f5cae92cc0041a234a1a3951f33cd42e86da808befbaaedd7d5351cc8` ;
  `scripts/amorce_instance_r1_resolution_graine_v1.sh` : celle que cite la v2 (`dc8164e2…`), à revérifier au lancement.
- Chemin de la configuration de la résolution à graine : `prereg/R1-graine-config-complement-v1.json`
  (42 clés ; celle de la v2, `prereg/R1-graine-config-v1.json`, dont seules les quatre durées changent : liste à
  « Seuil » ; scellée avec ce texte)
- Configuration de la résolution à graine (empreinte canonique) : `8d18c7ee9ce7bc6f2b176d2e5c67422708c8fc6c99f5b09e40b25d1e166663e8`
- Configuration de la résolution à graine, lot fidèle (empreinte canonique) : `8d18c7ee9ce7bc6f2b176d2e5c67422708c8fc6c99f5b09e40b25d1e166663e8`
  (sha256 du JSON canonique, clés triées, comme `resolution_graine_v1.empreinte_config` ; un seul fichier pour le cœur et
  le lot, comme la v2 ; l'empreinte canonique de la configuration v2 était `f91716bf…` : elle diffère, ce qui suffit à la
  garde d'exécution unique, voir « Seuil »)
- Entropie : `36410133060804533274328900142752730279`
  (celle du parent ; ce passage ne tire rien : son manifeste porte `aucun-tirage-propre`)
- Tests attendus : `71`
  (les sept fichiers de la liste `CIBLES` du script d'instance, au commit cité ; 71 passés le 2 novembre, journal de
  l'instance, 17:15:51 UTC)
- Documents qui font foi (chemin + empreinte) : la v2 et le parent ci-dessus ; configuration de la v2
  `prereg/R1-graine-config-v1.json` (fichier `0f300925546d886b8408d137903e711af579abb0d5947b1b88a27da894c4070f`) ; table
  v2 `prereg/R1-table-tokenisation-v2.json` (`5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`) ;
  verdict scellé du passage du 2 novembre
  `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md`
  (`64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68`) ; sorties du passage du 2 novembre, branche
  `calcul/r1-resolution-graine-v1` : résultat de la validation
  `diag/20261102-171752-r1-graine-validation/resolution-graine-validation.json`
  (`8e6a49126f37af6020b8bf056e6d35c6d53c7391f6d5d311fa0e6caa1298f773`) et son tableau des pas
  `pas-resolution-graine-validation.npz` (`fe2ef360a2444dc518c4e67b1a4623dce091abce636de0a572cacdd26d1142f6`), épisodes
  consignés `episodes-validation/000.json` à `146.json` ; résultat de la résolution
  `diag/20261102-175806-r1-graine-resolution/resolution-graine-resolution.json`
  (`674825453a8ce34c8bb6f8cb59a054b37af76d24f5e8b44b06f2c5e59d396079`) ; table v3 (`ead8a668…`, ci-dessus).

**Statut.** Le passage du 2 novembre a résolu les 7 épisodes (table v3 complète), mais sa validation n'a tenté que 57
des 147 épisodes résolus : le budget de l'étape (2 400 s, horloge partie avant le chargement du modèle) l'a coupée ;
54 empreintes retrouvées, 3 épisodes coupés pendant leur repli, 90 non tentés ; classe « méthode non transposée »,
réserve sur HG-2 et mesure déclarée incomplète (verdict, § 0 et § 8). Ce texte refait la validation **entière**, sous
le même code, la même carte et les mêmes graines, avec des bornes de durée qui ne servent qu'à arrêter une boucle folle.
Il ne relit aucun score et ne touche à aucune entrée de la table v3. Il n'est pas aveugle aux résultats du 2 novembre :
ses prédictions en partent (déclaré) ; le passage qu'il préenregistre, lui, n'est lu qu'après son scellement.

## Choix de conception : rejouer les 147, code inchangé

Le code exige que la validation porte sur **exactement** `seuil_validation` = 147 épisodes : `exiger_compte_validation`
(`resolution_graine_v1.py`, l. 1156-1160), appelée avant la boucle (l. 1531-1532) sur la liste rendue par
`episodes_de_l_etape` (l. 1396-1401 : tous les épisodes à identifiants connus, dans l'ordre du run). Ne rejouer que les
93 manqués exigerait du code neuf (une liste d'épisodes de validation, un compte attendu de 93), ses essais et une
relecture. On rejoue donc **les 147, code inchangé**. Les 54 déjà retrouvés, rejoués, ne sont pas une dépense perdue :
ils sont l'**épreuve de répétabilité** qui manquait (même code, même type de carte, mêmes graines, réglages
déterministes : empreinte identique attendue, et même chemin). Le verdict a montré que le « contrôle croisé » du
2 novembre n'en éprouvait aucune (réserve 3). Coût en plus des 54 : 798 s de calcul mesurées le 2 novembre (209,8 s pour
les 40 directs, 588,1 s pour les 14 par repli ; verdict § 6), soit ≈ 13 min de carte (≈ 0,3 USD au prix plafond).

Même ordre : la liste des 147 est construite comme le 2 novembre (`classer`, puis `episodes_de_l_etape`, sur les mêmes
pièces scellées) ; les rangs 0 à 56 sont donc les mêmes épisodes, et les 54 sont rejoués d'abord.

## Écarts à l'addendum v2

| n° | Ligne ou règle de la v2 | Règle de ce texte | Raison |
|---|---|---|---|
| C1 | Budgets de durée : `duree_max_episode_s` = 600, `duree_max_s` = 2 400, `duree_max_episode_lot_s` = 900, `duree_max_lot_s` = 3 600 | 7 200, 86 400, 7 200, 86 400 : **gardes contre une boucle folle seulement**, non des budgets de mesure | Mot de Lazar (18:26 UTC) ; la coupure du 2 novembre a laissé la validation incomplète |
| C2 | Plafond de l'amorce 235 min ; délais externes = budget + 10 min | Plafond de l'amorce **4 415 min**, exactement la somme exigée par le script (voir « Seuil ») ; la seule borne de dépense est la garde de dépense du GO, tenue par la session (« Coût et GO ») | Le script refuse de partir si la somme des délais dépasse le plafond (l. 179-187) |
| C3 | R3 : une exécution par étape sous la v2 | Ce texte est le « texte neuf » que la v2 exige pour tout essai de plus ; une exécution par étape sous ce texte | v2, « Seuil », R3 |
| C4 | Étape 1 (résolution) et étape table lues pour la table v3 | Rejouées par le script inchangé, **lues seulement comme répétabilité** ; la table produite (sous-produit) est écrite sous un autre nom et n'est jamais une table de référence | Le script n'a pas de mode « validation seule » (voir « Plan d'analyse ») |
| C5 | Libellés : contrôle croisé « répétabilité » ; comptes `balayages` et `passes` par épisode ; cause « budget de l'épisode épuisé pendant le repli » ; horloge de l'étape | Lus comme écrit à la section « Corrections de libellé » | Verdict, réserves 3 et 6, § 6 point 2 |
| C6 | Variables `PREREG`, `TABLE_V3`, `PLAFOND_MIN`, `BRANCHE` de l'amorce : décrites « pour l'essai local » (sauf `BRANCHE`) | Passées à la création de l'instance, sans changer le code de l'amorce ni du script | Seul moyen, code inchangé, de lancer ce texte (déclaré) |

## Hypothèse

Hypothèses de travail de l'instrument (aucune hypothèse du programme n'est en jeu) :
- **HC-1 (transposition, sans coupure de temps)** : sous HG-1 à HG-3 de la v2, la passe forcée et son repli écrit
  (bornes de travail inchangées : `seuil_ecart` 1,0, `quasi_egalites_max` 16, `bascules_max` 2, `combinaisons_max` 136)
  retrouvent l'empreinte de P3 des 147 épisodes résolus quand aucun budget de temps ne les coupe.
- **HC-2 (répétabilité)** : même code, même type de carte (A100-SXM4-80GB), mêmes réglages déterministes, mêmes graines :
  les 54 épisodes retrouvés le 2 novembre sont retrouvés de nouveau, par la même voie, avec les mêmes bascules, et le
  journal de leurs pas est identique au bit près.

## Prédiction chiffrée et signe attendu

Fondées sur les taux observés à l'étape 0 du 2 novembre (verdict § 2 et § 6) : 54 retrouvés sur 57 tentés (0,947) ; voie
directe en échec dans 17 cas sur 57 (0,30), dont 14 sauvés par repli (au plus 18 combinaisons) et 3 qui avaient épuisé
leurs bascules simples sans succès quand le temps les a coupés (rangs 0, 20 et 56 ; 24, 18 et 44 combinaisons).
Extrapolé aux 147, environ 8 épisodes du type « difficile » (3 connus et ≈ 5 parmi les 90 non tentés), dont une partie
peut résister aux 136 combinaisons.
- **P-C1 (empreintes retrouvées, signe : R > 54, et au plus 6 manquées)** : R ≥ 141 sur 147, confiance ≈ 0,75 ;
  **R = 147, confiance ≈ 0,3**. Toute manquée a pour cause la méthode (repli épuisé, contradiction, empreinte différente),
  non une durée, confiance ≈ 0,9.
- **P-C2 (classe de la règle gelée)** : « graines validées », confiance ≈ 0,3 (sous R = 147, les quatre conditions
  d'accord tiennent avec une confiance ≈ 0,95 : sur les 54 retrouvés du 2 novembre, accord moyen 0,99222, minimum
  0,98608, 28 253 pas informatifs, accord informatif 0,97961) ; « méthode non transposée », confiance ≈ 0,7 (une seule
  manquée suffit) ; « méthode transposée, graines non validées », confiance ≈ 0,02.
- **P-C3 (répétabilité des 54, HC-2)** : 54 retrouvés sur 54, confiance ≈ 0,97 ; même voie, mêmes bascules (`forcages`)
  et même nombre de combinaisons pour chacun, confiance ≈ 0,8 ; journal des pas identique au bit (colonnes du tableau
  des pas, voir « Métrique »), confiance ≈ 0,7 (carte physique autre, même modèle de carte).
- **P-C4 (voie directe)** : réussie dans ≈ 70 % des 147 (entre 90 et 115 épisodes), confiance ≈ 0,7 ; premier écart de
  la voie directe identique au 2 novembre pour les 17 épisodes qui en avaient un, confiance ≈ 0,8.
- **P-C5 (les 3 coupés)** : au moins un des rangs 0, 20 et 56 retrouvé (par paires), confiance ≈ 0,6 ; les trois,
  confiance ≈ 0,3.
- **P-C6 (étapes rejouées par le script, répétabilité)** : résolution 7 sur 7, contrôle croisé « conforme », identifiants
  retrouvés égaux à ceux du 2 novembre (donc aux entrées de la table v3 de référence), confiance ≈ 0,9 ; les 3 épisodes
  de C-6 retrouvés aussi à l'étape 0 de ce passage, confiance ≈ 0,85 ; lot « sans objet », confiance ≈ 0,9.
- **P-C7 (durée, descriptif)** : étape 0 entre 1 h et 9 h, point central ≈ 4 h (voir « Coût et GO »).
Ces valeurs sont des prédictions, non des seuils (R3 : rien n'est relancé pour les atteindre).

## Métrique

Celle de la v2 (« Métrique »), inchangée : empreintes retrouvées (seule métrique d'un « résolu »), voies, causes,
accords, écarts contraints, repli, classe écrite par `lire_validation` au résultat de la validation. En plus, calculées
**après** l'étape par le lecteur, sans module du dépôt, à partir des sorties scellées des deux passages (2 novembre et
celui-ci), épisode par épisode et par nom d'épisode :
- **répétabilité de l'empreinte (54)** : pour chacun des 54 épisodes retrouvés le 2 novembre, empreinte retrouvée de
  nouveau (champ `empreinte` égal à `empreinte_cible`, statut recalculé, jamais le drapeau seul) ;
- **répétabilité du chemin (54)** : égalité de `voie`, `forcages` et `combinaisons_essayees` entre les deux passages ;
- **répétabilité au bit (54)** : égalité, ligne à ligne, des colonnes `pas`, `rang`, `choix`, `non_contraint`,
  `candidats`, `ecart`, `second`, `marge`, `balayage`, `p_k`, `argmax_p` du tableau des pas (`fe2ef360…` contre le
  nouveau), sur les lignes de l'épisode ;
- **premier écart de la voie directe** (`erreurs_directes`) : égalité de (pas, rang, trouvé, vrai, écart, marge) pour
  les 17 épisodes qui en avaient un le 2 novembre ;
- **résolution rejouée** : empreintes, identifiants (`ids`) égaux à ceux du résultat `674825453a…`, contrôle croisé ;
  table du sous-produit : pour chacune des 4 entrées « identifiants », `actions` et `trajectoire_p3` égales à celles de
  la table `ead8a668…` ;
- **C-6 dans les deux étapes de ce passage** : statut des 3 épisodes de C-6 à l'étape 0 et à la résolution.
Aucune moyenne sur les jetons n'entre dans une sonde ; aucun score, aucune activation, aucune étiquette n'est lu.

## Seuil

**Règle de lecture de la validation : la règle gelée de la v2, inchangée**, fonction `lire_validation`
(`resolution_graine_v1.py`, l. 854-886), seuils de `regle_validation` inchangés. Soit R le nombre d'empreintes de P3
retrouvées et E = 147 :
1. « méthode non transposée » si E = 0 ou R < E (cause quelconque, « non tenté » ou « durée » compris) ;
2. sinon « graines validées » si accord moyen par épisode ≥ 0,95, accord minimum par épisode ≥ 0,90, pas informatifs
   réunis ≥ 1 000, accord sur eux ≥ 0,90 (une mesure absente compte comme manquée) ;
3. sinon « méthode transposée, graines non validées ».
Aucun seuil d'arrêt sur une mesure. La répétabilité n'a pas de seuil : sa lecture est à « Critères ».

**Configuration** `prereg/R1-graine-config-complement-v1.json` : la configuration de la v2, **42 clés, mêmes valeurs**,
sauf ces quatre (différences clé par clé avec la configuration v2) :

| Clé | v2 | Ce texte | Exigé par le code ? |
|---|---|---|---|
| `duree_max_s` | 2 400 | **86 400** | La garde d'exécution unique exige seulement une empreinte canonique différente (voir ci-dessous) : changer **une** clé suffit ; celle-ci est changée pour la demande de Lazar |
| `duree_max_episode_s` | 600 | **7 200** | Non (doit rester > 0 et ≤ `duree_max_s` : `exiger_reglages_execution`, l. 1103-1105 ; et contrôle du script, l. 165-167) |
| `duree_max_lot_s` | 3 600 | **86 400** | Non ; changé par cohérence (aucun budget de temps qui coupe, même dans une étape qui ne devrait pas tourner) |
| `duree_max_episode_lot_s` | 900 | **7 200** | Non (doit rester > 0 et ≤ `duree_max_lot_s` : module du lot, l. 845-846 ; script, l. 168-171) |

Toutes les autres clés sont identiques, dont `seuil_validation` = 147, `combinaisons_max` = `combinaisons_max_validation`
= `combinaisons_max_lot` = 136, `episodes_resolution` (mêmes 7, même ordre), pièces et empreintes, `mode` « reel ».

**Ce que le code exige pour accepter un passage de plus, vérifié dans le code au commit cité** :
- **garde d'exécution unique du cœur (R3)** : `executions_anterieures` (l. 1192-1211) ne retient un run antérieur que si
  sa commande, **son empreinte canonique de configuration** et son arbre gelé sont les mêmes ; la nouvelle configuration
  a une autre empreinte canonique (`8d18c7ee…` au lieu de `f91716bf…`) : la garde passe, **code inchangé**. Le texte
  neuf n'y entre pas ; il entre dans les gardes de citation : `exiger_config_citee` (l. 1163-1166, libellé du cœur),
  l'entropie (l. 1723-1726), `exiger_code_cite` (arbre gelé au lancement égal à celui du commit cité) ; la garde lit tous
  les manifestes de `runs/` et s'arrête sur un manifeste illisible (l. 1199-1203) ;
- **garde d'exécution unique du lot** (module du lot, l. 968-978) : même commande et même empreinte de configuration ;
  passe pour la même raison ; libellé du lot cité (l. 1193) ;
- **script, avant l'installation** : texte et sceau présents ; « Tests attendus » et « Chemin de la configuration … »
  cités une fois chacun (l. 114-124) ; configuration et sceau présents (l. 125) ; empreinte canonique citée une fois sous
  chacun de ses deux libellés (l. 145-149) ; **table à écrire absente** (l. 150-151) ; budgets cohérents (l. 165-171) ;
  `40 + 2 × (86 400/60 + 10) + 5 + (86 400/60 + 10) + 15 + 5 = 4 415` minutes ≤ plafond de l'amorce (l. 178-187).

**Bornes qui restent, déclarées** : `combinaisons_max` = 136 par épisode (borne de travail du repli, non de temps ; la
frontière écrite en permet au plus 16 + 16 × 16 = 272 : un épisode peut donc finir « non résolu » avant d'avoir épuisé
sa frontière, comme sous la v2) ; `balayages_max` = 16 par U+FFFD (aucun U+FFFD dans les 147) ; gardes de durée de
7 200 s par épisode et 86 400 s par étape (au taux observé, 136 combinaisons coûtent de ≈ 19 à ≈ 75 min : 8,3 à 33 s par
combinaison aux rangs 56, 0 et 20 ; la garde d'épisode laisse donc une marge d'au moins 1,6 fois au pire taux observé) ;
délais externes du script, 1 450 min par étape ; plafond de l'amorce, 4 415 min. **Déclaré** : ces valeurs sont au choix
de l'auteur, non mesurées au-delà des 57 épisodes du 2 novembre.

**R3** : chaque étape sur carte n'est exécutée qu'une fois sous ce texte ; tout essai de plus relève d'un texte neuf.

## Plan d'analyse

**Données et graines** : celles de la v2, inchangées (pièces de P3 vérifiées par empreinte au chargement ; seuls les
tableaux d'identité, `jetons` et `jetons_notes` des scores ; aucune note, étiquette ni activation). Graines (R9) :
celles de P3, dérivées comme `jouer_p3` (clé `tache/<identifiant>` du manifeste de P3) ; ce passage ne tire rien et n'a
aucune graine propre ; manifeste `aucun-tirage-propre`.

**Étape 0 — validation à l'aveugle des 147 (carte ; la seule lue pour la mesure).** Méthode, repli, aveugle et mesures :
ceux de la v2 (« Plan d'analyse », étape 0), au code cité. Les gardes de durée ne sont plus atteintes que par une boucle
folle : un épisode qui les atteindrait finit « non résolu », cause « durée : … », et la règle gelée le lit comme toute
autre manquée (classe « méthode non transposée ») ; un tel épisode est une **anomalie** auditée (« Critères »).

**Étapes rejouées par le script, lues comme répétabilité seulement.** Le script d'instance n'a pas de mode « validation
seule » : il enchaîne validation, résolution (l. 467-473), cibles du lot (l. 476), lot s'il reste une cible (l. 478-489)
et table (l. 490-494). L'étape validation du module, elle, **n'écrit aucune table** (elle n'écrit que
`diag/<run>/…` et `runs/<run>/…` : l. 1544-1545, 1628-1640, 1699 ; la table n'est écrite que par l'étape `table`,
l. 1812-1822). Code inchangé, la chaîne entière tourne donc :
- **résolution des 7** (≈ 13 min le 2 novembre) sous la configuration de ce texte, après la validation de ce passage
  (`exiger_validation`, l. 1419-1438 : même configuration, même code) ; lue comme répétabilité (P-C6) ; elle porte aussi
  le contrôle croisé, cette fois après une étape 0 qui a tenté les 3 épisodes de C-6 ;
- **cibles du lot** : attendu « sans objet » ; si une cible reste (répétabilité en défaut), le lot tourne sous les
  gardes de durée de ce texte, et son résultat n'est lu que pour l'audit ;
- **table** : écrite sous le nom **`prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json`** (variable `TABLE_V3`),
  sous-produit jamais cité comme table de référence ; comparée à `ead8a668…` (« Métrique »). Le nom par défaut du script
  (`prereg/R1-table-tokenisation-v3.json`) ne peut pas servir : s'il est présent au commit lancé, le script s'arrête avant
  l'installation (l. 150-151, R12) ; le dossier `prereg/` existe, donc l'écriture (l. 1785-1795) ne manque pas de
  dossier parent.
Un arrêt de la résolution, des cibles ou de la table **n'enlève rien** à la validation, déjà committée et poussée par le
script avant la résolution (l. 388-395, 458-465) ; il est lu à « Critères ».

**Lecture** (R13) : par un lecteur neuf, auteur ni de ce texte ni d'un code, sur les sorties scellées, après leur
réception : classe recalculée par la règle gelée ; métriques de répétabilité recalculées sur les deux passages ;
critères appliqués ligne à ligne ; verdict scellé, puis soumis à Lazar.

**Commande exacte (à partir du script d'instance existant, inchangé).** Avant la création, par la session qui lance, au
commit de scellement de ce texte sur `main` (noté `COMMIT_COMPLEMENT`, 40 caractères) :

```
git diff --quiet c2a8b6e1297a3134b49ec5b2aeb1849eddc4b98d "$COMMIT_COMPLEMENT" -- . ':(exclude)prereg' \
    ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' \
    ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md'   # code 0 exigé
git ls-tree "$COMMIT_COMPLEMENT" prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json \
    prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json.sha256                                          # sortie vide exigée
git ls-remote --exit-code origin refs/heads/calcul/r1-graine-complement-validation-v1                         # code 2 exigé
```

Création de l'instance : la **commande de création du 2 novembre, reprise mot pour mot** (offre, image, disque, amorce
`scripts/amorce_instance_r1_resolution_graine_v1.sh` en mode « args »), sous les filtres d'offre de la v2
(« Location »), avec seulement ces valeurs changées ou ajoutées dans l'environnement de l'instance (`--env`) :

```
GO_ID=GO-2026-11-02-26 vastai create instance <offre conforme> … --env "\
 -e COMMIT=$COMMIT_COMPLEMENT \
 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git \
 -e BRANCHE=calcul/r1-graine-complement-validation-v1 \
 -e PREREG=prereg/R1-addendum-relance-v2-complement-validation-v1.md \
 -e TABLE_V3=prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json \
 -e PLAFOND_MIN=4415 \
 -e GH_TOKEN=… -e HF_TOKEN=…" …
```

L'amorce appelle alors, sans autre changement :
`timeout --signal=TERM --kill-after=3m 4415m env COMMIT=$COMMIT_COMPLEMENT TRAVAIL=/root/r1graine PLAFOND_AMORCE_MIN=4415 bash amorce-depot/scripts/r1_resolution_graine_instance_v1.sh`,
qui hérite de `BRANCHE`, `PREREG`, `TABLE_V3` et `DEPOT_URL` par l'environnement. Les jetons ne sont jamais écrits ni
affichés. Un essai local des gardes (`ARRET_AVANT_CALCUL=1`) **pousse la branche** avant l'installation (l. 190) : s'il
est fait, c'est contre un dépôt local nu (`DEPOT_URL`) ou sous un autre nom de branche, jamais contre le dépôt distant
avec `BRANCHE=calcul/r1-graine-complement-validation-v1` (sinon le lancement réel s'arrêterait, branche présente).

## Corrections de libellé exigées par le verdict (sans toucher au code)

1. **Contrôle croisé** (verdict, réserve 3). `lecture_controle_croise` (l. 1254-1264) compare les épisodes de C-6
   résolus à la résolution aux identifiants de la table v2 : « conforme » dit que deux voies, chacune prouvée par
   l'empreinte de P3, s'accordent, ce qui est garanti hors collision de sha256. **Il n'éprouve aucune répétabilité.** La
   répétabilité, dans ce texte, n'est éprouvée que par la comparaison d'un même épisode rejoué deux fois : les 54 (entre
   les deux passages), les 7 (résolution du 2 novembre contre résolution rejouée) et les 3 de C-6 (étape 0 contre
   résolution de ce passage, s'ils sont retrouvés aux deux). La phrase de la v2 (« ils ont été retrouvés à l'aveugle
   parmi les 18 de l'étape 0 ») était fausse le 2 novembre (rangs 119, 126 et 137, non tentés).
2. **Comptes par épisode après repli** (verdict, réserve 6 a). Pour tout épisode, `balayages`, `balayages_complets` et
   `passes` écrits par épisode sont **ceux de l'essai direct seul** : posés l. 726-727 (ou l. 716-717 si l'essai direct
   finit par le budget de balayages), jamais mis à jour par le retour d'un rejeu basculé (l. 761-765) ni par la fin du
   repli (l. 774-781) ; chaque rejeu basculé a son propre compteur (l. 750), sur lequel le plafond de balayages est
   appliqué. Ils se lisent « compte de l'essai direct ». Les passes de l'étape entière sont `passes` du résultat
   (`moteur.passes`, l. 1666) et les lignes de progression du journal. Le compte de balayages du chemin retenu se lit
   sur la colonne `balayage` du tableau des pas.
3. **Cause « budget de l'épisode épuisé pendant le repli »** (verdict, réserve 6 b). L'échéance d'un épisode est la plus
   proche de l'échéance de l'étape et de son propre budget (`echeance_episode`, l. 662-667) ; les libellés « durée : … à
   l'essai direct » (l. 720) et « durée : budget de l'épisode épuisé pendant le repli » (l. 777) se lisent donc
   « **échéance de l'épisode ou de l'étape, la plus proche** ». Au rang 56 du 2 novembre, c'était l'échéance de l'étape
   (« coupé par l'échéance de l'étape »). Sous ce texte, l'échéance d'étape (86 400 s) ne devrait jamais être la plus
   proche ; si elle l'est, le lecteur le dit, d'après `duree_s` de l'épisode.
4. **Horloge de l'étape** (verdict § 6, point 2). Elle part juste après la création du manifeste (l. 1734), donc avant
   le chargement du modèle (l. 1523) et le classement (l. 1528) ; l'échéance de l'étape est posée l. 1519. Le budget
   d'étape couvre donc le chargement ; sans effet à 86 400 s, déclaré.
5. **Réserves de la concordance reconduites telles quelles** (verdict, réserves 1 et 2) : la lecture par cible du lot
   (VI-09) reste sans objet si le lot ne tourne pas ; le compte qui justifie le plafond de 16 balayages est de 2 pas
   comptés sur le chemin de `mention/2605.17899v2/e0` (`comptes_reels-sortie.txt`, `a2bd318f…`), et de 2 sur le chemin
   retenu au 2 novembre ; aucun U+FFFD dans les 147.

## Critères de lecture gelés

Règle unique, celle de la v2 : un épisode est résolu si et seulement si son empreinte de trajectoire égale celle de P3.
La classe est celle de `lire_validation`. Les lignes de la v2 pour la validation valent, reprises ici, et complétées de
celles de la répétabilité.

| Issue observée | Lecture |
|---|---|
| Classe « graines validées » (R = 147, quatre conditions tenues) | **Réserve sur HG-2 levée** et mesure de validation complète (réserves A et B du verdict levées). La table v3 de référence (`ead8a668…`) n'est pas réécrite (R12) : sa `lecture_validation` garde la classe du 2 novembre, comme trace ; l'addendum v3 cite le résultat scellé de ce complément et sa classe, qui fait foi pour HG-1 et HG-2. Rien d'autre ne change (aucun non résolu dans la table) |
| Classe « méthode transposée, graines non validées » (R = 147, une condition d'accord manquée) | Réserve sur HG-2 levée ; **réserve « graines »** (v2) ; audit (R4) avant l'addendum v3 ; les entrées de la table v3 restent des preuves |
| Classe « méthode non transposée », toutes les manquées de cause « méthode » (repli épuisé à 136 combinaisons, contradiction, empreinte différente) | **Réserve sur HG-2 maintenue**, avec un constat chiffré : la méthode, à ses bornes gelées, manque k épisodes sur 147. Pour chacun : premier écart de la voie directe, quasi-égalités, combinaisons essayées et leurs issues, accords. La table v3 reste valide (chaque entrée est prouvée par l'empreinte) ; l'addendum v3 avance avec la réserve. Aucun passage de plus sous ce texte (R3) ; une borne de travail plus large (`combinaisons_max` ≥ 272, exhaustif dans la frontière écrite) relèverait d'un texte neuf, proposé à Lazar, non d'une décision de ce texte |
| Classe « méthode non transposée », une manquée au moins de cause « durée » (garde de 7 200 s ou de 86 400 s atteinte) | Réserve sur HG-2 maintenue ; mesure déclarée incomplète ; **anomalie auditée (R4)** : une garde contre une boucle folle n'aurait pas dû être atteinte (taux observé ≤ 75 min pour 136 combinaisons) ; l'audit lit les passes, les combinaisons et la durée de l'épisode |
| Répétabilité des 54 : 54 retrouvés de nouveau | **Répétabilité de l'empreinte tenue** (HC-2), première épreuve de répétabilité du rejeu à graine |
| Répétabilité des 54 : un au moins non retrouvé (empreinte calculée différente de celle de P3, ou non résolu pour toute cause) | **Audit (R4), réserve sur la reproductibilité** du rejeu à graine, écrite au verdict et portée dans l'addendum v3 ; l'audit cherche d'abord une différence d'environnement (carte, pilote, CUDA, cuDNN, bibliothèques : `pip-freeze.txt` des deux passages) ; les entrées de la table v3 restent des preuves |
| Répétabilité des 54 : tous retrouvés, mais voie, bascules ou nombre de combinaisons différents pour un au moins, ou journal des pas différent au bit | Descriptif : « empreinte répétée, chemin numérique non répété » ; nombre d'épisodes et de lignes différents rapportés, avec l'environnement des deux passages. Ce n'est pas une réserve sur les résultats (l'empreinte reste juge), c'est une limite chiffrée de HG-2 |
| Résolution rejouée : 7 sur 7, contrôle croisé « conforme », identifiants égaux au 2 novembre ; table du sous-produit égale à `ead8a668…` sur les 4 entrées « identifiants » (`actions`, `trajectoire_p3`) | Répétabilité de la résolution tenue ; la table de référence reste `ead8a668…` |
| Résolution rejouée : un épisode non retrouvé, contrôle croisé autre que « conforme », lot exécuté, table du sous-produit non construite ou différente | **Audit (R4)**, réserve sur la reproductibilité ; la table de référence `ead8a668…` reste valide (ses 22 corrections sont prouvées par l'empreinte) ; la classe de la validation de ce passage reste lue telle quelle |
| Épisodes de C-6 retrouvés à l'étape 0 et à la résolution de ce passage | La répétabilité que la v2 prêtait au contrôle croisé est éprouvée, sur ces 3 épisodes |
| Audit de symétrie (R4), déclencheurs de la v2 | Inchangés : accord non contraint égal à 1 sur tous les pas des 147 ; aucune quasi-égalité sous 1 ; durée cumulée des étapes 0 et 1 sous 5 min ; à l'étape 0, `accord_sur_les_pas` ≤ `attendu_graine_independante_sur_les_pas` + 0,02 ; sous les deux autres classes, `accord_informatif` ≤ `attendu_informatif` + 0,10. Une répétabilité au bit parfaite des 54 est la **prédiction** (P-C3), non un signal de propreté |
| Validation arrêtée (`arret.json` : erreur de chaîne, signal, arrêt de dépense) | Aucune classe pour ce passage ; la classe du 2 novembre reste celle de la table ; les épisodes consignés et scellés sont comptés et lus pour la répétabilité (ceux des rangs 0 à 56 qui le sont), rien d'autre ; mesure déclarée incomplète |

Aucune issue de ce passage ne crée de nœud qui bloque l'addendum v3 : la table v3 est complète et prouvée. Les audits
(R4) se font avant l'addendum v3.

## Liste d'arrêt

Celle de la v2 (« Liste d'arrêt »), inchangée : **erreurs de chaîne seulement** (pièces, sceaux, graines, bibliothèque,
carte indisponible, tests autres que « 71 passed », commits, poussées). Aucune mesure n'arrête quoi que ce soit, sauf le
contrôle croisé du cœur, qui, autre que « conforme », arrête l'étape table (ici sans effet sur la validation). Changements :
- **aucun budget de temps qui coupe une mesure** : les quatre durées de la configuration et les délais externes du
  script (1 450 min par étape) sont des gardes contre une boucle folle ; le plafond de l'amorce (4 415 min) est fixé par
  la somme qu'exige le script ;
- **avant l'installation** (code 2), en plus de la v2 : table du sous-produit (ou son sceau) présente au commit ; branche
  `calcul/r1-graine-complement-validation-v1` présente ou non vérifiable ;
- **avant la création** (session) : arbre gelé du commit lancé différent de celui de `c2a8b6e1` ; ce texte, sa
  configuration ou leurs sceaux absents du commit lancé ; `GO_ID=GO-2026-11-02-26` non accepté par la garde de calcul ;
  aucune offre sous les filtres de la v2 (rien n'est loué : nœud porté à Lazar) ;
- **garde de dépense** (non une lecture, non un budget de mesure) : à **10 USD** engagés sur cette ligne sans fin en vue,
  la session écrit à Lazar (demande d'extension du GO, avec le nombre d'épisodes faits) ; à **14 USD** engagés sans GO
  étendu, la session envoie TERM au processus Python de l'étape en cours, **par son PID** (R10), sur l'instance ;
  le module écrit `arret.json` avec les épisodes consignés, le script les committe et les pousse (l. 379-386) ; puis
  l'instance est arrêtée par son identifiant (R10) et l'arrêt consigné dans `registres/arrets.md`. Ce n'est jamais fait
  par motif de ligne de commande.
**Ce qui n'est pas un arrêt** : toute classe ; moins de 147 retrouvées ; un épisode « durée » ; un lot « sans objet » ;
une carte, un CUDA ou un cuDNN autres que ceux de P3 (réserves écrites) ; une répétabilité en défaut (lue, auditée).
**Lancement** : pas de lancement sans ce texte et sa configuration scellés, la contre-lecture neuve (R2) traitée, la
concordance de conv-audit (annoncée par la ligne du GO) et le GO valide le jour même.
Dans tous les cas : sorties committées et poussées sur `calcul/r1-graine-complement-validation-v1` ; arrêt de l'instance
par son identifiant (R10), consigné.

## Coût et GO

A100-SXM4-80GB au **prix plafond de 1,40 USD de l'heure** (filtre de la v2). Durées : mise en place **33 min mesurées le
2 novembre** (16:44:49 → 17:17:52 UTC, dont 25 min 47 s d'essais) ; étape 0 : les 54 ≈ 13 min (798 s mesurées) ; les 3
coupés, de quelques minutes (retrouvés tôt) à ≈ 2,5 h (136 combinaisons chacun au taux observé : ≈ 57, 75 et 19 min) ;
les 90 autres ≈ 22 min au taux des 54 (14,8 s par épisode), plus les épisodes difficiles parmi eux (≈ 5 attendus, de 10
à 75 min chacun : de 0 à ≈ 6 h) ; résolution rejouée ≈ 13 min (13 min 24 s mesurées) ; cibles et table ≈ 1 min.
**Attendu ≈ 2 à 10 h, point central ≈ 4 h, soit ≈ 3 à 14 USD, point central ≈ 6 USD** (estimation de l'auteur, non
mesurée au-delà des 57 épisodes tentés). **Écart déclaré** : la ligne du GO annonce ≈ 4 USD et la demande de rédaction
≈ 3 USD ; ces valeurs sont dans la fourchette, en bas. Le plafond de 15 USD tient tant que la garde de dépense
(« Liste d'arrêt ») est tenue ; le haut de la fourchette s'en approche. Dépenses déjà imputées à `GO-2026-11-02-26` : à
relever dans `registres/depenses.md` avant la création. Lancement : `GO_ID=GO-2026-11-02-26` devant la commande de
création ; échéance du GO : 2026-11-16 ; après, GO nouveau.

## Ce qui suit selon chaque issue

- « graines validées » : réserve sur HG-2 levée ; l'addendum v3 cite la table v3 (`ead8a668…`), le résultat de la
  résolution du 2 novembre (`674825453a…`) et le résultat scellé de la validation de ce complément, avec sa classe.
- toute autre classe, ou une répétabilité en défaut : lecture telle qu'écrite aux « Critères » ; l'addendum v3 porte la
  réserve correspondante ; audit (R4) avant lui quand les critères l'exigent.
- dans tous les cas : verdict d'un lecteur neuf (R13), scellé, soumis à Lazar ; aucune étape refaite sous ce texte.

## Contre-lecture

R2 : contre-lecture par un sous-agent neuf, auteur d'aucune pièce, avant le scellement : ce texte entier, la
configuration `R1-graine-config-complement-v1.json` (et sa différence avec la v2), le code au commit cité (lignes
citées), le script d'instance et l'amorce (appel décrit à « Plan d'analyse »), le verdict du 2 novembre. Puis
concordance de conv-audit sur la version scellée, avant le lancement.
