# Complément au rejeu à graine de R1 — validation complète des 147 épisodes résolus — v1

- Auteur : sous-agent de rédaction (Opus 5.5), pour Lazar ; **brouillon 2, non scellé** (le brouillon 1, même dossier,
  reste intact). Nom à sceller : `prereg/R1-addendum-relance-v2-complement-validation-v1.md` (nom nouveau, R12).
- Date (UTC) : 2026-11-02 19:11 (`date -u`).
- **Changements depuis le brouillon 1** (décisions transmises par la session, sur les mots de Lazar) : repli porté à sa
  frontière écrite (`combinaisons_max` 272) ; gardes de durée relevées (épisode 4 h, étape 72 h) ; GO `GO-2026-11-02-30`,
  40 USD ; prédictions et devis refaits ; configuration `R1-graine-config-complement-v2.json`.
- **Texte parent (scellé, non modifié)** : `prereg/R1-addendum-relance-v2.md`
  (`9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059`, « v2 » ci-dessous). Tout ce que ce texte ne change
  pas reste celui de la v2 : méthode, faits établis sur le harnais de P3, mesures, règle gelée de la validation, filtres
  de location, essais.
- **Demande de Lazar** (session conv-audit, 2 novembre 2026) : 18:26 UTC « go finir, arrête de mettre des budgets temps
  et de les couper » et « je ne veux pas de blocage, de résultats non concluants par défaut de conception, de plafond ou
  que sais-je » ; 18:27 UTC « prends des budgets et plafonds très larges » ; 18:53 UTC « Session-depot la relance sans
  budget de temps, sous un texte court. : prepare les ».
- **GO** : `GO-2026-11-02-30` (`registres/go.md`, ligne 76), calcul, **plafond exactement 40 USD**, échéance 2026-11-16 ;
  la ligne annonce « attendu ≈ 6 à 20 USD ».
- **Portée** : la seule **étape 0 (validation à l'aveugle des 147 épisodes résolus)**, refaite entière, sans budget de
  temps qui coupe et sans borne de travail qui fasse perdre un épisode avant d'avoir épuisé la frontière écrite du repli.
  Le script d'instance, inchangé, rejoue ensuite la résolution des 7 et une table : **lues comme épreuves de répétabilité
  seulement**. La table v3 de référence reste `prereg/R1-table-tokenisation-v3.json`
  (`ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423`).
- Commit du code d'analyse : `c2a8b6e1297a3134b49ec5b2aeb1849eddc4b98d`
  (commit du passage du 2 novembre ; arbre gelé identique à celui de `0e2a8871…`, cité par la v2 : `git diff --quiet`
  sur les chemins gelés rend 0 ; **aucun fichier de code, d'essai ni de script n'est changé**)
- Empreintes du code au commit cité : `resolution_graine_v1.py` `cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663` ;
  `resolution_graine_lot_v1.py` `5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156` ;
  `scripts/r1_resolution_graine_instance_v1.sh` `da07025f5cae92cc0041a234a1a3951f33cd42e86da808befbaaedd7d5351cc8` ;
  amorce `scripts/amorce_instance_r1_resolution_graine_v1.sh` : celle de la v2 (`dc8164e2…`), à revérifier au lancement.
- Chemin de la configuration de la résolution à graine : `prereg/R1-graine-config-complement-v2.json`
  (42 clés : la configuration de la v2, sept valeurs changées, liste à « Seuil » ; scellée avec ce texte)
- Configuration de la résolution à graine (empreinte canonique) : `70b0b77135594b8566833c57535086e26379787b2735b8a3372ece2a3922ff5e`
- Configuration de la résolution à graine, lot fidèle (empreinte canonique) : `70b0b77135594b8566833c57535086e26379787b2735b8a3372ece2a3922ff5e`
  (sha256 du JSON canonique, clés triées, comme `empreinte_config` ; un seul fichier pour le cœur et le lot ; celle de la
  configuration de la v2 était `f91716bf…`)
- Entropie : `36410133060804533274328900142752730279`
  (celle du parent ; ce passage ne tire rien ; manifeste `aucun-tirage-propre`)
- Tests attendus : `71`
  (liste `CIBLES` du script, au commit cité ; 71 passés le 2 novembre, journal de l'instance, 17:15:51 UTC)
- Documents qui font foi : la v2 ; sa configuration `prereg/R1-graine-config-v1.json`
  (`0f300925546d886b8408d137903e711af579abb0d5947b1b88a27da894c4070f`) ; table v2
  (`5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`) ; verdict scellé du passage du 2 novembre
  `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md`
  (`64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68`) ; sorties du 2 novembre (branche
  `calcul/r1-resolution-graine-v1`) : validation `diag/20261102-171752-r1-graine-validation/resolution-graine-validation.json`
  (`8e6a49126f37af6020b8bf056e6d35c6d53c7391f6d5d311fa0e6caa1298f773`), son tableau des pas
  (`fe2ef360a2444dc518c4e67b1a4623dce091abce636de0a572cacdd26d1142f6`) et ses épisodes `episodes-validation/000.json` à
  `146.json` ; résolution `diag/20261102-175806-r1-graine-resolution/resolution-graine-resolution.json`
  (`674825453a8ce34c8bb6f8cb59a054b37af76d24f5e8b44b06f2c5e59d396079`) ; table v3 (`ead8a668…`).

**Statut.** Le 2 novembre, la résolution a retrouvé les 7 épisodes (table v3 complète), mais la validation n'a tenté que
57 des 147 épisodes résolus : le budget d'étape de 2 400 s (horloge partie avant le chargement du modèle) l'a coupée.
Comptes du verdict scellé, qui fait foi : **54 retrouvés, 3 coupés pendant leur repli, 90 non tentés** (93 manqués, tous
par une durée ; tout autre compte, « 87 non tentés » compris, est faux). Classe « méthode non transposée », réserve sur
HG-2, mesure déclarée incomplète. Ce texte refait la validation entière, même code, même type de carte, mêmes graines. Il
ne lit aucun score et ne touche à aucune entrée de la table v3. Ses prédictions partent des résultats du 2 novembre
(déclaré) ; le passage qu'il préenregistre n'est lu qu'après son scellement.

## Choix de conception

**Les 147, code inchangé.** Le code exige que la validation porte sur exactement `seuil_validation` = 147 épisodes
(`exiger_compte_validation`, `resolution_graine_v1.py` l. 1156-1160, appelée l. 1531-1532 sur la liste
d'`episodes_de_l_etape`, l. 1396-1401). Ne rejouer que les 93 manqués demanderait du code neuf, des essais et une
relecture. Les 54 déjà retrouvés, rejoués d'abord (même liste, même ordre : rangs 0 à 56), sont l'**épreuve de
répétabilité** qui manquait : le verdict a montré que le « contrôle croisé » n'en éprouvait aucune (réserve 3). Leur coût :
798 s de carte mesurées le 2 novembre (≈ 0,3 USD).

**Repli porté à sa frontière écrite.** Le repli bascule au plus `quasi_egalites_max` = 16 quasi-égalités de l'essai
direct (l. 730), puis, pour chaque rejeu basculé, au plus 16 des siennes après sa bascule (l. 767-770), sur
`bascules_max` = 2 niveaux : sa frontière compte au plus **16 + 16 × 16 = 272** combinaisons. Avec `combinaisons_max` =
272, la borne `essayees >= cmax` (l. 739, 771) ne peut plus arrêter le repli avant qu'il ait essayé toute sa frontière :
**aucun épisode n'est perdu par une borne de travail**. Une manquée signifie alors que la frontière écrite (deux bascules
au plus, vers le second candidat, parmi les 16 quasi-égalités les plus fragiles de chaque niveau, écart sous 1 nat) ne
contient pas le chemin de P3 : une **limite de la méthode**, mesurée, non un plafond.

**Durées : gardes contre une boucle folle seulement, jamais un couperet.** Au taux observé le 2 novembre (8,3 à 33 s par
combinaison), un épisode qui épuise ses 272 combinaisons coûte au plus ≈ 8 976 s ; la garde d'épisode (14 400 s) est à
1,6 fois ce pire, la garde d'étape (259 200 s, 72 h) au-delà de tout devis. Elles ne sont pas des budgets de mesure : une
garde atteinte serait une anomalie auditée (« Critères »), non une issue prévue. La seule borne qui peut couper est celle
de la dépense (plafond du GO, « Coût et GO »).

**Script complet.** Le script d'instance n'a pas de mode « validation seule » (l. 457-499) ; l'étape validation du module
n'écrit aucune table (seule `--etape table` en écrit, l. 1812-1822). Code inchangé, la chaîne entière tourne : résolution
des 7 (≈ 13 min), cibles du lot, table écrite sous `TABLE_V3=prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json`
(le nom par défaut, s'il est au commit, arrête le script avant l'installation, l. 150-151, R12). Ces étapes sont lues comme
répétabilité ; la table produite est un sous-produit, jamais une référence.

## Écarts à la v2

| n° | v2 | Ce texte | Raison |
|---|---|---|---|
| C1 | `combinaisons_max` = `combinaisons_max_validation` = `combinaisons_max_lot` = 136 | **272** (frontière écrite entière) | Aucun épisode perdu par une borne de travail (mot de Lazar, 18:26 UTC) |
| C2 | Durées 600 / 2 400 s (cœur), 900 / 3 600 s (lot) | **14 400 / 259 200 s** (cœur et lot) : gardes contre une boucle folle | « arrête de mettre des budgets temps et de les couper » |
| C3 | Plafond de l'amorce 235 min | **13 055 min**, somme exigée par le script (« Seuil ») ; la dépense est bornée par sa garde (« Coût et GO ») | Le script refuse de partir sous cette somme (l. 178-187) |
| C4 | R3 : une exécution par étape sous la v2 | Ce texte est le texte neuf que la v2 exige pour tout essai de plus | v2, « Seuil » |
| C5 | Résolution et table lues pour la table v3 | Rejouées par le script inchangé, lues comme répétabilité seulement | Pas de mode « validation seule » |
| C6 | Libellés : contrôle croisé, comptes par épisode, cause de durée, horloge | Lus comme à « Corrections de libellé » | Verdict, réserves 3 et 6, § 6 |
| C7 | `PREREG`, `TABLE_V3`, `PLAFOND_MIN` décrits par l'amorce « pour l'essai local » | Passés à la création de l'instance, code inchangé | Seul moyen, code inchangé, de lancer ce texte |

## Hypothèse

- **HC-1 (transposition à frontière entière)** : sous HG-1 à HG-3 de la v2, la passe forcée et son repli, essayé sur
  toute sa frontière écrite, retrouvent l'empreinte de P3 des 147 épisodes résolus.
- **HC-2 (répétabilité)** : même code, même type de carte (A100-SXM4-80GB), mêmes réglages déterministes, mêmes graines :
  les 54 épisodes retrouvés le 2 novembre le sont de nouveau, par la même voie, avec les mêmes bascules, et le journal de
  leurs pas est identique au bit.

## Prédiction chiffrée et signe attendu

Base (verdict § 2 et § 6) : sur 57 tentés, voie directe réussie 40 fois ; 17 échecs de la voie directe, dont 11 sauvés
par une bascule, 3 par deux (au plus 18 combinaisons), et 3 (rangs 0, 20 et 56) qui avaient épuisé leurs bascules simples
et essayé 8, 3 et 31 paires quand le temps les a coupés. Six épisodes sur 57 ont donc demandé au moins deux bascules ; les
quatre retrouvés à deux bascules (dont `honnete/2512.05150v2/e0`, à la résolution) l'ont été en 6 à 23 combinaisons.
J'estime à ≈ 0,6 la chance qu'un épisode du type des trois coupés soit retrouvé dans la frontière entière (échecs possibles :
trois erreurs ou plus, ou une erreur hors de la frontière). Des 90 non tentés, les 3 de C-6 sont déjà retrouvés (à la
résolution) ; sur les 90 − 3 autres, ≈ 9 épisodes à deux bascules ou plus sont attendus, dont ≈ 4,6 du type « coupé ».
Manquées attendues : ≈ 1,2 parmi les 3 coupés et ≈ 1,8 parmi ces 90 − 3, soit **≈ 3** (entre 0 et 8).
- **P-C1 (empreintes retrouvées ; signe : R > 54, au plus 6 manquées)** : R ≥ 141, confiance ≈ 0,9 ; R ≥ 144, confiance
  ≈ 0,6 ; **R = 147, confiance ≈ 0,1**. Toute manquée a pour cause la frontière épuisée (ou une contradiction terminale),
  non une durée, confiance ≈ 0,95.
- **P-C2 (classe de la règle gelée)** : **« graines validées », confiance ≈ 0,1** (sous R = 147, les quatre conditions
  d'accord tiennent avec une confiance ≈ 0,95 : sur les 54 retrouvés, accord moyen 0,99222, minimum 0,98608, 28 253 pas
  informatifs, accord informatif 0,97961) ; **« méthode non transposée », confiance ≈ 0,9** ; « méthode transposée,
  graines non validées », ≈ 0,01. Le relèvement à 272 ôte la cause « durée », non la limite de la frontière : une seule
  manquée suffit à la classe « méthode non transposée ».
- **P-C3 (répétabilité des 54)** : 54 retrouvés sur 54, confiance ≈ 0,97 ; même voie, mêmes bascules, même nombre de
  combinaisons, confiance ≈ 0,8 ; journal des pas identique au bit, confiance ≈ 0,7 (autre carte physique, même modèle).
- **P-C4 (voie directe)** : réussie pour ≈ 70 % des 147 (90 à 115 épisodes), confiance ≈ 0,7 ; premier écart de la voie
  directe identique pour les 17 épisodes qui en avaient un, confiance ≈ 0,8.
- **P-C5 (les 3 coupés)** : au moins un retrouvé, confiance ≈ 0,9 ; les trois, confiance ≈ 0,2.
- **P-C6 (étapes rejouées)** : résolution 7 sur 7 par les mêmes voies, identifiants égaux au 2 novembre, contrôle croisé
  « conforme », confiance ≈ 0,9 ; table du sous-produit égale à `ead8a668…` sur les 4 entrées « identifiants »,
  confiance ≈ 0,9 ; les 3 de C-6 retrouvés aussi à l'étape 0, confiance ≈ 0,9 ; lot « sans objet », confiance ≈ 0,9.
- **P-C7 (durée, descriptif)** : étape 0 entre ≈ 2 h et ≈ 24 h, point central ≈ 9 h (« Coût et GO »).
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

**Ce que le code exige pour un passage de plus (vérifié au commit cité)** : la garde d'exécution unique du cœur
(`executions_anterieures`, l. 1192-1211) ne retient un run antérieur que de même commande, **même empreinte canonique de
configuration** et même arbre gelé ; celle du lot (l. 968-978), de même commande et même configuration. Une autre empreinte
canonique (`70b0b771…` au lieu de `f91716bf…`) suffit : code inchangé. Le texte neuf entre dans les gardes de citation
(configuration sous chacun de ses deux libellés, l. 1163-1166 et lot l. 1193 ; entropie, l. 1723-1726 ; commit cité,
`exiger_code_cite`). Le script exige en outre, avant l'installation : « Tests attendus » et « Chemin de la configuration …
» cités une fois chacun (l. 114-124) ; empreinte canonique une fois sous chacun de ses deux libellés (l. 145-149) ; table
`TABLE_V3` absente (l. 150-151) ; `40 + 2 × (259 200/60 + 10) + 5 + (259 200/60 + 10) + 15 + 5 = 13 055` minutes ≤ plafond
de l'amorce (l. 172, 178-187).

**Bornes qui restent, déclarées** : celles de la frontière (deux bascules, vers le second candidat, 16 quasi-égalités par
niveau, écart sous 1 nat) et `balayages_max` = 16 par U+FFFD (aucun U+FFFD dans les 147) ; ce sont des bornes de la
méthode, gelées par la v2, que ce texte ne change pas. Valeurs des gardes de durée : au choix de la session, sur le taux
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

**Commande exacte (script d'instance existant, inchangé).** Avant la création, par la session, au commit de scellement
de ce texte sur `main` (`COMMIT_COMPLEMENT`, 40 caractères) :

```
git diff --quiet c2a8b6e1297a3134b49ec5b2aeb1849eddc4b98d "$COMMIT_COMPLEMENT" -- . ':(exclude)prereg' \
    ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' \
    ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md'   # code 0 exigé
git ls-tree "$COMMIT_COMPLEMENT" prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json \
    prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json.sha256                                          # sortie vide exigée
git ls-remote --exit-code origin refs/heads/calcul/r1-graine-complement-validation-v1                         # code 2 exigé
```

Création : la **commande de création du 2 novembre, reprise mot pour mot** (offre sous les filtres de la v2, image,
disque, amorce `scripts/amorce_instance_r1_resolution_graine_v1.sh` en mode « args »), seules ces valeurs changées ou
ajoutées dans l'environnement de l'instance :

```
GO_ID=GO-2026-11-02-30 vastai create instance <offre conforme> … --env "\
 -e COMMIT=$COMMIT_COMPLEMENT \
 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git \
 -e BRANCHE=calcul/r1-graine-complement-validation-v1 \
 -e PREREG=prereg/R1-addendum-relance-v2-complement-validation-v1.md \
 -e TABLE_V3=prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json \
 -e PLAFOND_MIN=13055 \
 -e GH_TOKEN=… -e HF_TOKEN=…" …
```

L'amorce appelle alors, sans autre changement :
`timeout --signal=TERM --kill-after=3m 13055m env COMMIT=$COMMIT_COMPLEMENT TRAVAIL=/root/r1graine PLAFOND_AMORCE_MIN=13055 bash amorce-depot/scripts/r1_resolution_graine_instance_v1.sh`,
qui hérite de `BRANCHE`, `PREREG`, `TABLE_V3` et `DEPOT_URL`. Jetons jamais écrits ni affichés. Un essai local des gardes
(`ARRET_AVANT_CALCUL=1`) pousse la branche avant l'installation (l. 190) : seulement contre un dépôt local nu ou sous un
autre nom de branche.

## Corrections de libellé exigées par le verdict (sans toucher au code)

1. **Contrôle croisé** (réserve 3) : `lecture_controle_croise` (l. 1254-1264) compare les épisodes de C-6 résolus aux
   identifiants de la table v2 ; « conforme » dit que deux voies prouvées par l'empreinte s'accordent (garanti hors
   collision) ; **il n'éprouve aucune répétabilité**. Ici, la répétabilité n'est éprouvée que par un même épisode rejoué
   deux fois : les 54, les 7, et les 3 de C-6 (étape 0 contre résolution de ce passage).
2. **Comptes par épisode** (réserve 6 a) : `balayages`, `balayages_complets` et `passes` écrits par épisode sont ceux de
   l'**essai direct seul** (l. 716-717, 726-727 ; non mis à jour par les rejeux basculés, l. 761-765, 774-781 ; chaque rejeu
   a son compteur, l. 750, sur lequel le plafond de balayages s'applique). Passes de l'étape : `passes` du résultat
   (l. 1666) et lignes de progression ; balayages du chemin retenu : colonne `balayage` du tableau des pas.
3. **Cause de durée** (réserve 6 b) : l'échéance d'un épisode est la plus proche de celle de l'étape et de la sienne
   (`echeance_episode`, l. 662-667) ; « durée : … à l'essai direct » (l. 720) et « budget de l'épisode épuisé pendant le
   repli » (l. 777) se lisent « **échéance de l'épisode ou de l'étape, la plus proche** » (au rang 56 du 2 novembre :
   coupé par l'échéance de l'étape).
4. **Horloge de l'étape** (verdict § 6, point 2) : partie l. 1734, avant le chargement du modèle (l. 1523) ; échéance
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
| « méthode non transposée », toutes les manquées de cause « méthode » (frontière épuisée, contradiction terminale, empreinte différente) | **Mesure complète** (réserve B levée) ; **réserve sur HG-2 maintenue, chiffrée** : la passe forcée, à frontière entière, retrouve R épisodes sur 147 ; pour chaque manquée : premier écart de la voie directe, quasi-égalités, combinaisons par niveau et leurs issues, accords. La table v3 reste valide (entrées prouvées par l'empreinte) ; l'addendum v3 avance avec la réserve. Aucun passage de plus sous ce texte (R3) ; une frontière plus profonde (trois bascules) ou une validation par le lot fidèle relèveraient d'un texte neuf, proposé à Lazar |
| « méthode non transposée », une manquée au moins de cause « durée » | Mesure déclarée incomplète ; **anomalie auditée (R4)** : une garde contre une boucle folle n'aurait pas dû être atteinte ; l'audit lit passes, combinaisons et durée de l'épisode |
| Répétabilité des 54 : 54 retrouvés | **Répétabilité de l'empreinte tenue** (HC-2) |
| Répétabilité des 54 : un au moins non retrouvé (empreinte calculée ≠ empreinte de P3, ou non résolu pour toute cause) | **Audit (R4), réserve sur la reproductibilité**, portée dans l'addendum v3 ; l'audit cherche d'abord une différence d'environnement (carte, pilote, CUDA, cuDNN, `pip-freeze.txt` des deux passages) ; la table v3 reste prouvée |
| 54 retrouvés, mais voie, bascules, combinaisons ou journal des pas différents pour un au moins | Descriptif : « empreinte répétée, chemin numérique non répété » ; comptes rapportés avec l'environnement des deux passages ; limite chiffrée de HG-2, non réserve sur les résultats |
| Résolution rejouée 7 sur 7, identifiants égaux, contrôle croisé « conforme », table du sous-produit égale sur les 4 entrées | Répétabilité de la résolution tenue |
| Résolution rejouée : un épisode non retrouvé, contrôle croisé autre que « conforme », lot exécuté, table du sous-produit absente ou différente | **Audit (R4)**, réserve sur la reproductibilité ; la table `ead8a668…` reste valide ; la classe de la validation de ce passage reste lue telle quelle |
| 3 épisodes de C-6 retrouvés à l'étape 0 et à la résolution | La répétabilité que la v2 prêtait au contrôle croisé est éprouvée, sur ces 3 |
| Audit de symétrie (R4) | Déclencheurs de la v2, inchangés (accord égal à 1 sur tous les pas des 147 ; aucune quasi-égalité sous 1 ; étapes 0 et 1 sous 5 min ; `accord_sur_les_pas` ≤ attendu + 0,02 ; sous les deux autres classes, `accord_informatif` ≤ attendu + 0,10). La répétabilité au bit des 54 est la **prédiction** (P-C3), non un signal de propreté |
| Validation arrêtée (`arret.json` : erreur de chaîne, signal, arrêt de dépense) | Aucune classe pour ce passage ; la classe du 2 novembre reste ; épisodes consignés comptés et lus pour la répétabilité, rien d'autre ; mesure déclarée incomplète |

Aucune issue ne crée de nœud qui bloque l'addendum v3 (table v3 complète et prouvée) ; les audits (R4) se font avant lui.

## Liste d'arrêt

Celle de la v2 : **erreurs de chaîne seulement** (pièces, sceaux, graines, bibliothèque, carte indisponible, tests autres
que « 71 passed », commits, poussées) ; aucune mesure n'arrête rien, sauf le contrôle croisé du cœur, qui, autre que
« conforme », arrête l'étape table (sans effet sur la validation). Changements :
- **aucun budget de temps qui coupe une mesure** : gardes de durée et délais externes du script (4 330 min par étape)
  contre une boucle folle seulement ; plafond de l'amorce fixé par la somme qu'exige le script (13 055 min) ;
- **avant l'installation** (code 2), en plus de la v2 : table du sous-produit (ou son sceau) au commit ; branche
  `calcul/r1-graine-complement-validation-v1` présente ou non vérifiable ;
- **avant la création** (session) : arbre gelé du commit lancé différent de celui de `c2a8b6e1` ; texte, configuration ou
  sceaux absents ; `GO_ID=GO-2026-11-02-30` refusé par la garde de calcul ; aucune offre sous les filtres de la v2 (rien
  n'est loué : nœud porté à Lazar) ;
- **garde de dépense** (plafond du GO, non une borne de mesure) : à **30 USD** engagés, la session écrit à Lazar
  (épisodes faits, dépense, durée restante estimée ; demande d'extension du GO si la fin n'est pas en vue) ; à **40 USD**
  sans GO étendu (procédure lancée à 39,5 USD engagés, pour que la poussée et l'arrêt, ≈ 10 min, tiennent sous le
  plafond), la session envoie TERM au processus Python de l'étape en cours **par son PID** (R10) ; le module écrit
  `arret.json` avec les épisodes consignés, le script les committe et les pousse (l. 379-386) ; puis l'instance est
  arrêtée **par son identifiant** (R10), consigné dans `registres/arrets.md`. Jamais par motif de ligne de commande.
**Ce qui n'est pas un arrêt** : toute classe ; moins de 147 retrouvées ; un épisode « durée » ; un lot « sans objet » ;
une carte, un CUDA ou un cuDNN autres que ceux de P3 (réserves écrites) ; une répétabilité en défaut (lue, auditée).
**Lancement** : texte et configuration scellés ; contre-lecture neuve (R2) traitée ; concordance de conv-audit ; GO valide
le jour même. Dans tous les cas : sorties poussées sur `calcul/r1-graine-complement-validation-v1` ; arrêt de l'instance
par son identifiant (R10), consigné.

## Coût et GO

A100-SXM4-80GB au **prix plafond de 1,40 USD de l'heure** (filtre de la v2), plus le disque. Composantes : mise en place
**33 min mesurées** le 2 novembre (16:44:49 → 17:17:52 UTC, dont 25 min 47 s d'essais) ; les 54 ≈ 13 min (798 s
mesurées) ; les 3 coupés : au moins les 1 564 s déjà dépensées (mêmes combinaisons, rejouées à l'identique), au plus
≈ 4,7 h à frontière épuisée (≈ 272 × 25 s, 255 × 33 s et 221 × 8,3 s), point central ≈ 3,4 h ; les 90 autres ≈ 22 min
au taux des 54 (14,8 s par épisode), plus les épisodes difficiles parmi eux (≈ 4,6 attendus, de 1 à ≈ 11 ; de ≈ 0,5 à
≈ 2,5 h chacun) ; résolution rejouée ≈ 13 min (13 min 24 s mesurées) ; cibles et table ≈ 1 min.

| Cas | Durée de carte | Dépense au prix plafond |
|---|---|---|
| Bas (3 coupés retrouvés tôt, un difficile neuf) | ≈ 3 h | ≈ 4 USD |
| **Central** (≈ 4,6 difficiles neufs, ≈ 1,1 h chacun ; 3 coupés ≈ 3,4 h) | **≈ 10 h** | **≈ 14 USD** |
| Haut (≈ 9 difficiles neufs menés au bout de leur frontière ; 3 coupés aussi) | ≈ 24 h | ≈ 34 USD |
| Pire | non borné par les gardes de durée (72 h par étape) | **borné par la garde de dépense : arrêt à 40 USD** (≈ 28 h) |

Estimation de l'auteur, sur les 57 épisodes tentés le 2 novembre, non mesurée au-delà ; un prix réel sous le plafond
allonge d'autant la durée couverte. Alerte à 30 USD et arrêt à 40 USD : « Liste d'arrêt ». La garde de dépense est tenue
par la session ; si la session s'interrompt, seule une vérification planifiée des dépenses la remplace (à poser à la
création). Dépenses déjà imputées à `GO-2026-11-02-30` : à relever dans `registres/depenses.md` avant la création.
Lancement : `GO_ID=GO-2026-11-02-30` devant la commande ; échéance 2026-11-16 ; après, GO nouveau.

## Ce qui suit

- « graines validées » : réserve sur HG-2 levée ; l'addendum v3 cite la table v3 (`ead8a668…`), le résultat de la
  résolution du 2 novembre (`674825453a…`) et le résultat scellé de la validation de ce complément, avec sa classe.
- toute autre issue : lecture telle qu'écrite aux « Critères » ; l'addendum v3 porte la réserve correspondante ; audit
  (R4) avant lui quand les critères l'exigent.
- dans tous les cas : verdict d'un lecteur neuf (R13), scellé, soumis à Lazar ; aucune étape refaite sous ce texte.

## Contre-lecture

R2 : sous-agent neuf, auteur d'aucune pièce, avant le scellement : ce texte, la configuration
`R1-graine-config-complement-v2.json` et sa différence avec la v2, le code au commit cité (lignes citées), le script
d'instance et l'amorce, le verdict du 2 novembre. Puis concordance de conv-audit sur la version scellée, avant le
lancement.
