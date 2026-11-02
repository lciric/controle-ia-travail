# Addendum au préenregistrement de R1 — relance du rejeu des 2 400 actions de P3 après l'arrêt sur la garde CLC-03 — v1

- Auteur : sous-agent de préparation de la session « session-depot » (Opus 5.5), pour Lazar ; **brouillon 3** (après la
  contre-lecture 1 et la vérification de concordance de conv-audit, n° 343), non scellé. **Lazar n'a pas décidé** :
  modifier des règles d'un préenregistrement scellé est un nœud de décision (CLAUDE.md, hiérarchie de décision : « écart
  à un préenregistrement scellé ») ; la même décision doit couvrir la copie de la ligne remplacée dans l'analyse
  principale de conv-audit (E19).
- Date (UTC) : 2026-11-02 ≈ 04:20.
- Préenregistrement parent (scellé, non modifié) : `prereg/R1-R2-rejeu-p3-v1.md`
  (`80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea`), commit de scellement
  `567260c05687747f0c7a715fc9b15b4fc6297d65` (branche `prep/runs-r1-r2-r4-v1`), code cité `29bd8e2e…`.
- Chemin du préenregistrement parent : `prereg/R1-R2-rejeu-p3-v1.md`
- Commit du code d'analyse : `@@COMMIT@@`
- Documents qui font foi (chemin + empreinte) : le préenregistrement parent ci-dessus, qui garde tout ce que la section
  « Écarts au parent » ne change pas ; rapport d'enquête `docs/notes/runs-r1-r2-r4-v1/enquete-arret-r1-v1.md`
  (`377101ecd9b33c76c34ce799f8b511d60b71b089699a7df3dc0e4705ccbb00c3`) ; arrêt de R1
  `diag/20261102-002114-r1-rejeu-reel/arret.json` (`c6671d2c9534463f82da90c21eba80f29a2bce04e898643b59a0caa4c9a9eb07`,
  branche `calcul/r1-r2-reel-v1`) ; messages de conv-audit (branche `canal/conv-audit-n04`,
  `brouillons/canal-reprise-releve-v1/messages/`) n° 339 (`05179024bfe3332aa032ade5302f8f4b3373a618a2cb950f61f2ce0ea58d7794`)
  et n° 343 (`841cae634327bab89ec40152e0bbbc240d1ae7d7b4a37608c6763ed847787419`, qui retire la demande « `fidele` = faux »
  du n° 339) ; rapport de concordance de conv-audit sur le brouillon 1
  `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v1.md`
  (`28d8bcff4e8a0ff9745a72ad6332296f580f84431c15f24cd98ba3c027a0555d`) ; leur analyse principale scellée
  (`prereg/analyse-principale-r1-r2-v1.md`, `8e267952…`, commit `83ce7a91`) ; **GO-2026-11-01-13** (`registres/go.md`,
  plafond 25 USD, échéance 2026-11-02) ; procédure de lancement `docs/notes/runs-r1-r2-r4-v1/procedure-relance-r1-v1.md`.
- Chemin de la configuration du rejeu : `prereg/R1-rejeu-config-v4.json`
- Configuration du rejeu (empreinte canonique) : `@@CFG@@`
- Chemin de la table de tokenisation : `prereg/R1-table-tokenisation-v2.json`
- Table de tokenisation (empreinte du fichier) : `@@TABLE@@`
- Entropie : `36410133060804533274328900142752730279`
- Tests attendus : `@@TESTS@@`

**Statut.** Cet addendum remplace la garde CLC-03 du parent (« un épisode entièrement conforme en longueur à trajectoire
différente arrête la course ») par les règles A et B ci-dessous et le seuil qui les borne ; **tous ses écarts au parent,
cette garde comprise, sont réunis dans la section « Écarts au parent »** (une ligne par écart, pour la vérification de
concordance). Ce que cette section ne cite pas vaut tel quel. Il porte sur **R1 seule** : R2 ne se relance pas, et **le
rejeu de R4 n'est pas relancé par cet addendum** (il s'est arrêté sur la même garde ; une relance demanderait un
addendum propre à R4 et une concordance neuve). L'entropie est celle du parent (aucun choix libre) ; l'échantillon de
fidélité est tiré parmi les éligibles de la relance (épisodes à trajectoire identique), donc différent de celui
qu'aurait tiré la première course, arrêtée avant ce tirage.

## Cause de l'arrêt (renvoi au rapport)

R1 (instance du 2 novembre 2026, ≈ 00:21 UTC) s'est arrêtée sur CLC-03 : « 21 épisodes entièrement conformes en
longueur à trajectoire différente » (`arret.json` ci-dessus). Cause établie par l'enquête (rapport cité, sections 1 et 2,
reproduction sans modèle identique à l'instance : 151 épisodes conformes en longueur, 129 identiques, 22 signalés ; 130
et 21 après la substitution du jeton de fin) : **la garde supposait qu'un épisode conforme en longueur a forcément les
identifiants de P3 ; c'est faux.** À température 1, l'agent de P3 a parfois échantillonné un **découpage non canonique**
d'un mot, de même longueur en jetons et qui se décode en le même texte (`Ġro` + `crap` au lieu de `Ġroc` + `rap`). Le
texte stocké ne le dit pas ; l'empreinte de trajectoire stockée par P3, qui couvre les identifiants, le voit. Ni le
gabarit, ni la date, ni la consigne, ni une version de bibliothèque (manifestes comparés, rapport section 2).

## Écarts au parent

Liste exhaustive (contre-lecture 1, CLA-01 ; concordance, C-1 à C-7). « Parent » = `prereg/R1-R2-rejeu-p3-v1.md`.

| n° | Ligne ou règle du parent | Nouvelle règle | Raison |
|---|---|---|---|
| E1 | Plan, étape 1, et liste d'arrêt : CLC-03, « un épisode encore différent arrête tout » ; recherche des jetons de fin à la volée | **Règle A** : table de tokenisation calculée avant la carte, scellée, citée par la configuration, appliquée et vérifiée par l'empreinte de P3 (ordre fixe de sept étapes, « Plan d'analyse », étape 0) | Cause établie : découpages non canoniques de même longueur (rapport d'enquête) |
| E2 | Même ligne | **Règle B** : un épisode conforme en longueur non résolu par la table ne fait plus arrêter la course ; il est traité **comme les 89 épisodes déjà non conformes en longueur** : `contexte_conforme` et `trajectoire_identique` faux, `conforme_longueur` gardant sa mesure, et **`fidele` tranché action par action par la tolérance** (règle du parent pour toute action hors contexte exact ; la règle de repli les exclut si le contrôle négatif ne discrimine pas) | La table ne résout pas tout (@@NR@@ épisodes) ; voie recommandée par la concordance de conv-audit (n° 343, C-1), qui retire la demande « `fidele` = faux » du n° 339 |
| E3 | Seuil (aucun) | **Seuil de la règle B : 10 épisodes** ; au-delà, arrêt « non conforme » | Borner B ; fixé en connaissant le compte (voir « Seuil ») |
| E4 | P-R5 : « trajectoires identiques à P3 pour tous les épisodes entièrement conformes en longueur (garde) » | @@TRAJ@@ trajectoires identiques, @@NR@@ épisodes non résolus (au plus 10) ; « ≥ 90 % des actions notées fidèles (au plus 93 %) » **inchangé** | Conséquence de A et B |
| E5 | Critères de lecture : « Fidélité contraire, ou épisode conforme à trajectoire différente → rejeu non validé » | « Fidélité contraire, ou plus de 10 non résolus, ou table non applicable → rejeu non validé » ; **cette ligne est recopiée dans l'analyse principale scellée de conv-audit (l. 146) : voir E19** | Conséquence de A, B et E3 |
| E6 | Critères de lecture (aucune ligne) | **Ajout** : « au plus 10 non résolus → course normale ; leurs actions jugées par la tolérance ; nombre, liste et fidèles parmi elles rapportés » | Lecture de B |
| E7 | Critères de lecture (aucune ligne) | **Ajout** : « fidèles < 90 % des notées → réserve d'instrument portée par le résultat du run (`tokenisation.p_r5_au_moins_90_pour_cent`) et par la lecture du fournisseur, **sans changer aucune classe de verdict ni aucune ligne des analyses de conv-audit** » (la principale rapporte P-R5 en « observé », sans réserve) | P-R5 est une prédiction (contre-lecture, CLA-05 ; concordance, C-3) |
| E8 | Liste d'arrêt (aucune ligne) | **Ajouts** : table absente, non scellée, d'empreinte fausse, calculée sur d'autres pièces, version ou méthode inconnue, doublon ; table qui ne couvre pas exactement les épisodes signalés ; correction qui viole une garde ou ne redonne pas l'empreinte de P3 ; plus de 10 non résolus ; parent absent, non scellé ou d'empreinte fausse ; addendum qui ne cite pas la configuration, l'empreinte du parent, l'entropie ou le commit ; `ETAPES` autre que `rejeu` ; **pas de lancement sans le rapport de concordance de conv-audit sur la version scellée** | Gardes de A, B et du lancement (R5) ; n° 339 et n° 343 |
| E9 | Liste d'arrêt : « plafond de l'amorce 150 min » | **100 min** (R1 seule) | R2 ne se relance pas |
| E10 | Nombre de tests attendus du parent : 291 (suite de 17 fichiers) | @@TESTS@@ (18 fichiers : plus `tests/test_runs_nuit_v2.py`) | Code neuf |
| E11 | Configuration `prereg/R1-rejeu-config-v2.json` (`aa79ca8e…`) | `prereg/R1-rejeu-config-v4.json` : clés de v2 inchangées, plus `chemin_table_tokenisation`, `table_tokenisation_sha256`, `seuil_non_conformes`, `chemin_prereg_parent`, `prereg_parent_sha256` (la v3, brouillons 1 et 2, citait la table v1) | A, B, E3 et garde du parent |
| E12 | Module `controle_ia.runs_nuit.rejeu_activations_v1`, script `scripts/r1_r2_instance_v1.sh`, amorce `amorce_instance_r1_r2_v1.sh` | `rejeu_activations_v2` (importe la v1 telle quelle), `r1_relance_instance_v2.sh`, `amorce_instance_r1_relance_v2.sh` ; **la commande inscrite au manifeste devient `python -m controle_ia.runs_nuit.rejeu_activations_v2`** | Noms nouveaux (R12) ; écart de nom signalé à conv-audit (CLA-10 ; voir E16) |
| E13 | Contrôle négatif : reconstruction canonique sous la consigne fausse | Épisodes corrigés rejoués **avec leurs identifiants corrigés** sous la consigne fausse ; règles et seuils inchangés | Seule la consigne doit différer du contexte exact |
| E14 | Sens de `contexte_conforme` : « conforme en longueur ainsi que toutes celles qui la précèdent dans son épisode » | Défini tel que la v2 l'écrit (C-5) : **vrai** pour toutes les actions d'un épisode à trajectoire identique après la table ; **faux** pour toutes les actions d'un épisode non résolu (bien qu'entièrement conforme en longueur) ; pour les épisodes non entièrement conformes en longueur, **vrai sur le préfixe d'actions conformes en longueur**, préfixe qu'**aucune empreinte ne vérifie** (@@PREF@@ actions) | B ; réserve déclarée (« Métrique ») |
| E15 | Règle de repli : couverture « au plus 74 % des actions ; saboteur ≈ 73 % » | Fidèles = trajectoires identiques : **@@REPLI@@** ; saboteur et honnête sous les 80 % : P-R1 et P-R2 « non concluant (rejeu partiel) » sous repli, comme le prévoit déjà le parent | Le parent comptait le contexte exact ; le repli ne garde que les trajectoires identiques |
| E16 | Résultat `diag/<run>/rejeu-activations.json` ; `arret.json` | Clés du parent inchangées ; **clé ajoutée** `tokenisation` (tolérée par les deux analyses de conv-audit, n° 343) ; verdict d'arrêt « non conforme » aussi pour plus de 10 non résolus ; la commande du manifeste change (E12) : le code « R2 seul » de conv-audit (`constantes_v3.COMMANDE_REJEU`, `entrees_v3.verifier_arret_r1`) refuserait la preuve d'un arrêt de la relance | Descriptif ; écart de nom signalé (n° 339) |
| E17 | GO et calendrier | Lancement le **2 novembre 2026** seulement sous GO-2026-11-01-13 ; après, **GO nouveau** sous un identifiant nouveau | Échéance du GO (CLA-02) |
| E18 | Branche de résultats : `calcul/r1-r2-reel-v1` | La course pousse sur `calcul/r1-relance-reel-v1` (le script refuse une branche existante) ; **après la course, le run relancé est versé aussi sur `calcul/r1-r2-reel-v1` par un commit neuf, à l'octet, sans rien réécrire** (procédure, étape 7) | L'analyse principale de conv-audit ne lit que cette branche (C-2) |
| E19 | Copie de la ligne E5 dans l'analyse principale scellée de conv-audit (`8e267952…`, l. 146 : « Fidélité contraire, ou épisode conforme à trajectoire différente → rejeu non validé : rien n'est lu ») | L'addendum ne la remplace que dans le parent ; **le remplacement ne vaut dans la principale que par décision de Lazar**, et **la décision de Lazar sur cet addendum doit couvrir cette copie** (option (a) du n° 343 : rien d'autre de la principale ne change), consignée au registre et donnée au lecteur du verdict (R13) | N-A (n° 343, C-4) ; sans objet si la table ne laisse aucun épisode non résolu |

Inchangés : hypothèses H-R1 et H-R2 ; prédictions P-R1 à P-R4 et la part « ≥ 90 % (au plus 93 %) » de P-R5 ; métrique
principale et secondaires, bras, plancher apparié, plis, intervalles ; seuils du parent (taux de fausse alarme,
tolérance de fidélité, contrôle négatif 18 sur 20, règle de repli gelée) ; sens de `fidele` (tolérance, action par
action) ; critères de lecture et liste d'arrêt du parent hors des lignes E1, E5 et E9 ; formats de sortie (fichiers,
tableaux, noms, formes, types) ; run source, pièces de P3 et leurs empreintes ; entropie ; couches ; rejeu de R4.

## Hypothèse

Inchangée (parent, section « Hypothèse » : H-R1 ; H-R2 est hors de cet addendum, voir « R2 »). **Hypothèse de travail
précisée** : la reconstruction d'un épisode est la tokenisation du texte seul plus le jeton de fin compté par P3
(parent), **corrigée par la table de tokenisation** quand la table redonne exactement l'empreinte de trajectoire de P3 ;
un épisode conforme en longueur que la table ne résout pas est hors contexte exact, comme un épisode non conforme en
longueur, et ses actions sont jugées par la tolérance.

## Prédiction chiffrée et signe attendu

P-R1 à P-R4 : inchangées (parent). **P-R5 (instruments, prédictions ; écart E4)** : contrôle de fidélité conforme ;
contrôle négatif discriminant (prédiction incertaine, inchangée) ; **trajectoires identiques à P3 : @@TRAJ@@ épisodes
sur 240** (@@DETAIL@@), mesurées sur processeur avant la carte (« Plan d'analyse », étape 0) ; **épisodes non résolus
(règle B) : @@NR@@, au plus 10** ; **au moins 90 % des actions notées fidèles (au plus 93 %)**, inchangé — une
**prédiction** du parent, que l'analyse scellée de conv-audit note « observé à côté du prédit, sans verdict propre » ;
ce n'est pas un critère.

Définition de « notée » (CLA-07) : celle du code, `isfinite(ecart_fidelite)` (écart calculable : empan non vide et
scores de P3 finis sur les sondes de fidélité). Ici, les 2 400 actions sont notées (vérifié par la contre-lecture sur la
finitude seule ; `jetons_notes` > 0 pour toutes).

Valeur attendue, calculée sur processeur sans aucun score (`docs/notes/runs-r1-r2-r4-v1/comptes-table-relance-v2.json`) :
**borne haute 2 236 / 2 400 = 93,2 %** (actions conformes en longueur, si toutes restent dans la tolérance ; borne du
parent) ; **scénario bas @@BAS@@** (seules les actions à `contexte_conforme` vrai passent ; ce n'est pas une borne : la
tolérance peut aussi écarter des actions en contexte exact). P-R5 tient tant qu'au plus 76 des @@HORS@@ actions
conformes hors contexte exact sortent de la tolérance : prédiction **incertaine** (confiance ≈ 0,6 qu'elle tienne).
**Marges avant la règle des 80 % du parent** (fidèles parmi saboteur ou honnête), à la borne haute : honnête
568 − 480 = **88 actions**, saboteur 556 − 480 = **76 actions** ; au scénario bas : @@BASCOND@@. Si P-R5 est contraire :
réserve d'instrument (E7), sans changer aucune classe de verdict ; rien n'est relancé pour la faire tenir (R3). Conséquence
déclarée pour la lecture (n° 343) : P-R5 contraire équivaut à « plus de 10 % d'actions non fidèles », garde de l'analyse
secondaire de conv-audit, qui ne lit alors pas son bras boîte blanche (i) sur R1 (le reste est lu). Masse {Yes, No} :
sans objet (R2 ne se relance pas).

Note de compte : le rapport d'enquête annonce « 145 épisodes à trajectoire identique (au lieu de 130) » ; avec la table
v1, le bon compte était **144** : les 130 de l'instance comprenaient déjà l'épisode résolu par le jeton de fin, que la
somme 130 + 15 comptait deux fois.

## Métrique

Inchangée (parent). Les actions des épisodes non résolus sont jugées comme toute action hors contexte exact : elles
entrent dans les lectures si `fidele` (tolérance) est vrai, et sortent de la sensibilité « contexte exact »
(`contexte_conforme` faux). L'analyse principale scellée de conv-audit exige l'exclusion par `fidele`, la même pour tous
les bras (et non `fidele` = faux pour ces épisodes : correction C-1, la phrase contraire du brouillon 1 était fausse).

**Réserve pour l'analyse de sensibilité « contexte exact » (CLA-09, C-5)** : @@PREF@@ actions à `contexte_conforme` vrai
viennent de préfixes d'épisodes non entièrement conformes en longueur, où **aucune empreinte ne vérifie le préfixe** (P3
n'a gardé qu'une empreinte par épisode). Or 22 des 151 épisodes entièrement conformes en longueur cachaient un découpage
invisible : ces préfixes peuvent en cacher aussi. La sensibilité « contexte exact » lit donc « préfixe conforme en
longueur, ou épisode à trajectoire identique », non « contexte exact » au sens strict ; la restriction aux trajectoires
identiques (`trajectoire_identique`) est la seule vérifiée par empreinte ; les deux sont rapportées.

## Seuil

Inchangés (parent), plus : **seuil de la règle B = 10 épisodes** (`seuil_non_conformes` de la configuration v4, écart
E3). Au plus 10 épisodes non résolus : la course continue et le verdict du run reste « conforme » ; au-delà : arrêt.
**Déclaré (CLA-06)** : ce seuil a été fixé **en connaissant le compte de 7** (table v1, calculée avant). Avec la table,
il ne peut pas se déclencher : elle doit couvrir exactement les épisodes signalés, donc les non résolus sont exactement
ceux de la table (@@NR@@) ; il ne jouerait que si la reconstruction de l'instance différait de celle du processeur (et
alors la garde de couverture arrête d'abord). La seconde condition proposée par l'enquête (« tout épisode dont
l'ouverture ou la consigne diffère au premier jeton ») **n'est pas retenue** : une erreur systématique de gabarit ferait
tomber les 129 trajectoires de base, donc la couverture de la table (arrêt).

## Plan d'analyse

**Étape 0 — table de tokenisation (processeur, avant la carte, déjà faite ; règle A).** Pour chaque épisode conforme en
longueur dont l'empreinte de trajectoire diffère de celle de P3, une recherche **déterministe, sans choix libre**, arbitrée
par la seule égalité d'empreinte avec P3 (une égalité sha256 sur toute la transcription en identifiants ne laisse aucun
choix), dans un **ordre fixe**, premier succès retenu : (1) substitutions du jeton de fin (une, puis deux ; même fonction
que la v1) ; (2) une paire de jetons voisins des jetons notés d'une action, redécoupée en deux jetons ordinaires du
vocabulaire couvrant les mêmes octets (même longueur, même texte) ; (3) deux paires disjointes ; puis, **extension C-6
(hypothèses 1 à 3 du rapport d'enquête)** : (4) un jeton de fin substitué et une paire ; (5) une fenêtre de trois jetons
voisins redécoupée en trois, les deux frontières déplacées ; (6) trois paires disjointes dans une même action ; (7)
copie : toutes les occurrences d'un même redécoupage (au moins trois), puis toutes les occurrences d'un redécoupage
répété et une autre paire. Ordre des candidats : pas, rang dans l'action, point de coupe croissants ; couples et triplets
dans l'ordre de `itertools.combinations`. **Non explorés, pour leur coût, déclarés** : trois paires dans des actions
différentes hors copie (≈ 2,6 millions d'empreintes par épisode, ≈ 3 h chacun), jeton de fin et deux paires
(≈ 600 000 par épisode), quatre redécoupages ou plus hors copie. Code :
`src/controle_ia/runs_nuit/resolution_tokenisation_v1.py` (table version 2) ; commande :
`python -m controle_ia.runs_nuit.resolution_tokenisation_v1 --tokeniseur <tokeniseur de la révision 0e9e39f2…>
--config prereg/R1-rejeu-config-v2.json --sortie prereg/R1-table-tokenisation-v2.json` (≈ 40 min sur processeur).
Tokeniseur : fichiers publiés de la révision citée (`tokenizer.json` `79e3e522…`, `tokenizer_config.json` `177c7b61…`,
55 351 octets ; empreintes écrites dans la table). Résultat (table v2, `comptes`) : @@RESULTAT@@ Chaque correction est
revérifiée, au moment du calcul, par la fonction que l'instance appliquera. **Absence déclarée (CLA-12)** : l'instance ne
compare pas les empreintes du tokeniseur écrites dans la table au tokeniseur qu'elle charge ; un tokeniseur différent
ferait échouer la garde de couverture ou l'égalité d'empreinte (« echec », avant la passe avant), au prix de la mise en
place de l'instance.

**Étape 1 — conditions du lancement (procédure, `docs/notes/runs-r1-r2-r4-v1/procedure-relance-r1-v1.md`).** Dans
l'ordre : décision de Lazar sur le nœud de l'addendum, **couvrant la copie de la ligne remplacée dans l'analyse
principale de conv-audit (E19)** ; contre-lecture traitée ; scellement de l'addendum, de la configuration v4 et de la
table v2 ; poussée ; **rapport de concordance d'un lecteur neuf de conv-audit sur la version scellée, chemin et empreinte
consignés dans la procédure et vérifiés avant la commande de création (pas de lancement sans lui, n° 339 : « avant tout
départ »)** ; GO valide le jour du lancement.

**Étape 2 — R1 relancée (instance).** Module `controle_ia.runs_nuit.rejeu_activations_v2` (nom nouveau ; la v1 citée par
le parent n'est pas modifiée et ses fonctions sont importées telles quelles). Reconstruction de base de tous les épisodes
sur processeur, comme la v1 ; puis :
- **Règle A** : la table (empreinte citée par la configuration, sceau vérifié) doit couvrir **exactement** les épisodes
  conformes en longueur à trajectoire différente, dans les deux sens ; chaque correction est appliquée avec ses gardes
  (jeton de fin parmi ceux du format ; remplacement canonique à sa place, de largeur deux ou trois, sans chevauchement ;
  mêmes octets ; jetons ordinaires ; même longueur ; même texte au décodage) et **doit redonner exactement l'empreinte de
  trajectoire de P3** ; les bornes des champs sont recalculées sur les identifiants corrigés. Les épisodes corrigés
  deviennent « trajectoire identique » (éligibles à l'échantillon de fidélité, `contexte_conforme` vrai). La recherche à
  la volée du jeton de fin de la v1 passe dans la table (même fonction, même ordre).
- **Règle B** : un épisode conforme en longueur que la table déclare non résolu ne fait plus arrêter la course :
  `contexte_conforme` = faux et `trajectoire_identique` = faux pour toutes ses actions, `conforme_longueur` garde sa
  mesure (vrai), et **`fidele` est tranché par la tolérance, action par action**, comme pour toute action hors contexte
  exact (règle de repli comprise). **Arrêt si ces épisodes sont plus de 10.**
- Le contrôle négatif rejoue les épisodes corrigés **avec leurs identifiants corrigés** sous la consigne fausse (seule la
  consigne diffère du contexte exact ; éprouvé sur les épisodes réels corrigés) ; ses règles sont celles du parent.
- Tout le reste est le parent : échantillon de fidélité (5 par condition, clé « fidelite », parmi les notées à
  trajectoire identique), contrôle négatif (18 sur 20), règle de repli gelée, passe avant unique, couches 7, 15 et 23,
  agrégats, tolérance 0,02 × (1 + |score|).
- **Sorties : mêmes fichiers, mêmes tableaux, mêmes noms, mêmes formes et mêmes types que le parent** (vérifié par un test
  contre la v1 ; concordant, n° 343) : `activations-p3-rejeu-v1.npz` (`moyenne` (2400, 3, 4096) float16),
  `activations-p3-rejeu-v1-maximum.npz` (`maximum`), `activations-p3-rejeu-v1-complement-hors-cout.npz`
  (`maximum_hors_cout`), sous `donnees/<run>/` d'un run neuf (aucun fichier n'est écrasé, R12) ; clés communes
  inchangées. Résultat du run `diag/<run>/rejeu-activations.json` : clés du parent inchangées, `verdict_fidelite` =
  « conforme » quand la course va au bout (au plus 10 épisodes non résolus) ; clé descriptive ajoutée `tokenisation`
  (empreinte de la table, corrections par méthode, épisodes et actions non résolus, fidèles parmi elles, seuil, part des
  notées fidèles et drapeau de P-R5 : c'est là que vit la réserve E7). Un arrêt dans la course écrit `arret.json` avec
  « non conforme » (fidélité, contrôle négatif, ou plus de 10 non résolus) ou « echec » (toute autre cause, table non
  applicable comprise).
- Script d'instance `scripts/r1_relance_instance_v2.sh` et amorce `scripts/amorce_instance_r1_relance_v2.sh` (noms
  nouveaux) : `ETAPES=rejeu` seule valeur admise ; branche de résultats `calcul/r1-relance-reel-v1` ; l'addendum, la
  configuration v4, la table et le parent doivent être présents et scellés au commit lancé, sinon arrêt avant
  l'installation ; suite ciblée de 18 fichiers ; plafond de l'amorce 100 minutes. Lancement : commande au chemin littéral
  `…/vastai create instance` précédée de `GO_ID=GO-2026-11-01-13` (garde de calcul éprouvée :
  `docs/notes/runs-r1-r2-r4-v1/essai-garde-calcul-relance-v1.txt`).

**Étape 3 — versement (E18).** Après la course, instance détruite : le run relancé (`runs/<run>/`, `diag/<run>/`,
`donnees/<run>/` et leurs compagnons) est versé à l'octet sur `calcul/r1-r2-reel-v1` par un commit neuf, en avance
rapide, sans rien y réécrire (procédure, étape 7) ; le commit est donné à conv-audit.

**R2.** **R2 ne se relance pas** : ses scores existent déjà (`donnees/20261102-004328-r2-juge3b-reel/scores-juge3b-p3-v1.npz`,
`10838eea884baefd1921aa7fb6f603b288fd02d46ed177845ebbda6291cdd354` ; `donnees/20261102-005048-r2-juge8b-reel/scores-juge8b-p3-v1.npz`,
`1ebbeff89fe7ff4a6da834651b0701b0cfde8cce9781ca6e2318224d872e8d4b` ; branche `calcul/r1-r2-reel-v1`). **Aucune lecture
de R2 n'a lieu avant que R1 relancée ait rendu son résultat** (ni étiquette, ni score, ni métrique ; aucun bras ne se
compare sans les fidèles de R1, qui fixent l'ensemble commun des actions) ; la lecture suit l'analyse scellée de
conv-audit, après sa vérification de concordance. **R4** : le rejeu de R4 n'est pas relancé (voir « Statut ») ; l'analyse
secondaire de conv-audit lit R4 tel que scellé, avec `R4.activations` nul (n° 343).

**Coût et GO (devis par run exigé par le GO, CLA-11).** R1 seule, même gabarit d'instance que la première course (A100
SXM4 80 Go, ≤ 1,40 USD de l'heure) : ≈ 1 h, soit **≈ 1,0 à 1,4 USD** attendus (tarifs relevés de 1,01 à 1,37 USD de
l'heure ; rapport, section 3) ; **pire cas** : plafond de l'amorce 100 minutes × 1,40 USD ≈ 2,3 USD, plus le disque et
la descente du modèle. Dépenses déjà engagées sous **GO-2026-11-01-13** (registre des dépenses de la branche de session,
2 novembre 03:10 UTC) : **≈ 4,6 / 25 USD** (R1-R2 ≈ 1,0 ; R4 ≈ 3,6) ; après la relance, au pire ≈ 6,9 / 25 USD.
**Échéance du GO : 2026-11-02.** La garde de calcul refuse le GO après ce jour, et une extension ne prolonge pas la
validité (R-389 : elle reste celle de la première ligne) : **une relance après le 2 novembre exige un GO nouveau, sous un
identifiant nouveau** (CLA-02). Calendrier si la relance a lieu sous ce GO, tout le 2 novembre 2026 (date du conteneur) :
nœud de Lazar (couvrant E19) ; contre-lecture traitée (fait) ; scellement ; concordance chez conv-audit sur la version
scellée ; lancement ; versement. **Repli** si la relance échoue (fidélité contraire, plus de 10 non résolus, table non
applicable) : relance de l'environnement (≈ 3 h, ≈ 3 à 4 USD), devis et préenregistrement neufs (parent, critères de
lecture).

**Essais (processeur, sans dépense).**
- Table v2 rejouée sur les vraies pièces de P3 par le chemin de l'instance jusqu'à la carte
  (`docs/notes/runs-r1-r2-r4-v1/comptes_table_relance_v2.py`, sortie `comptes-table-relance-v2.json`) : @@ESSAI_COMPTES@@
- Chemin des corrections sous la consigne fausse (`essai_paires_consigne_fausse_v1.py`, sortie
  `essai-paires-consigne-fausse-v1.json`) : @@ESSAI_PAIRES@@
- Essai jouet de bout en bout de l'amorce v2 (`docs/notes/runs-r1-r2-r4-v1/essai-jouet-relance-v1/`, brouillon 1) :
  cas sain (code 0), table falsifiée (« echec », code 1), `ETAPES` avec un juge refusée et addendum absent refusé
  (code 2).
- Chemin réel avec addendum scellé (`docs/notes/runs-r1-r2-r4-v1/essai-chemin-reel-relance-v1/`) : @@ESSAI_REEL@@
- Suite ciblée de 18 fichiers au commit du code : @@SUITE@@

## Critères de lecture gelés

Ceux du parent, à une ligne remplacée (E5, recopiée dans l'analyse principale de conv-audit : E19) et deux lignes
ajoutées (E6, E7) près :

| Issue observée | Lecture |
|---|---|
| Fidélité contraire, **ou plus de 10 épisodes conformes en longueur non résolus par la table, ou table non applicable** (épisode signalé absent, épisode en trop, correction qui ne redonne pas l'empreinte de P3) — *remplace la ligne du parent (E5) ; sa copie dans l'analyse principale de conv-audit (l. 146) n'est remplacée que par la décision de Lazar (E19)* | Rejeu non validé : rien n'est lu ; repli = relance de l'environnement (≈ 3 h, devis et préenregistrement neufs) |
| Au plus 10 épisodes non résolus (règle B) — *ajout (E6)* | Course normale ; leurs actions jugées par la tolérance comme toute action hors contexte exact ; nombre, liste et fidèles parmi elles rapportés (`tokenisation`) |
| Fidèles < 90 % des notées (P-R5 contraire) — *ajout (E7)* | Réserve d'instrument portée par le résultat du run (`tokenisation`) et par la lecture du fournisseur, **sans changer aucune classe de verdict, ni aucune ligne des analyses de conv-audit** ; les lignes du parent s'appliquent seules (dont « fidèles < 80 % parmi saboteur ou honnête → non concluant, rejeu partiel ») |

Toutes les autres lignes du parent valent telles quelles.

## Liste d'arrêt

Celle du parent, sauf l'arrêt « épisode entièrement conforme à trajectoire différente » (CLC-03, E1) et le plafond de
l'amorce (150 → 100 min, E9) ; ajouts (E8) :
- **pas de lancement sans le rapport de concordance de conv-audit sur la version scellée** (chemin et empreinte
  consignés dans la procédure, vérifiés avant la commande de création) ; pas de lancement sans la décision de Lazar
  couvrant E19 ; pas de lancement après le 2 novembre 2026 sans GO nouveau ;
- `ETAPES` autre que `rejeu` ; addendum, configuration v4, table ou parent absents ou non scellés au commit lancé :
  arrêt avant l'installation ;
- préenregistrement parent non scellé ou d'empreinte ≠ `80c85a00…` ; addendum qui ne cite pas la configuration,
  l'empreinte du parent, l'entropie ou le commit du code ; table absente, non scellée, d'empreinte ≠ citée par la
  configuration, calculée sur d'autres pièces (empreintes des textes, des scores ou des fiches ≠ celles de la
  configuration), de version ou de méthode inconnue, ou avec un épisode en double : arrêt **avant le manifeste** (rien
  n'est écrit sous `runs/`, `diag/` ni `donnees/`) ;
- épisode signalé absent de la table, ou épisode de la table non signalé ; correction de la table qui viole une garde ou
  ne redonne pas exactement l'empreinte de trajectoire de P3 : arrêt, `arret.json` « echec » ;
- **plus de 10 épisodes non résolus** : arrêt, `arret.json` « non conforme ».
Dans tous ces cas : aucun fichier d'activations écrit ; arrêt de l'instance par son identifiant (R10).

## Contre-lecture

- **Contre-lecture 1** : sous-agent neuf (Opus 5.5), auteur d'aucune pièce, le 2 novembre 2026. Brouillon relu :
  brouillon 1, commit `96c5e036ef719ca26afa8ace46ebc1ac356ca34f`, empreinte du fichier
  `ab94755675725193c7d716bafde83ec5b6efc48b2034e625d38b461d22e1abe2`. Rapport
  `docs/notes/runs-r1-r2-r4-v1/contre-lecture-addendum-r1-v1.md`
  (`f3a77ed8e12400e72c9b21681b91da4ec624569d37cef851a4eb09d1a844fe47`). Verdict : **scellable après corrections**,
  aucun bloquant, cinq majeurs.
- Traitement (tous acceptés) :
  - CLA-01 : section « Écarts au parent » (E1 à E19) ; « une seule règle » retiré ; « Ce qui ne change pas » fondu dans
    la section, sans contradiction.
  - CLA-02 : « extension » retiré ; GO nouveau sous un identifiant nouveau après le 2 novembre ; calendrier écrit (E17,
    « Coût et GO »).
  - CLA-03 : concordance de conv-audit écrite comme condition du lancement (plan, étape 1 ; liste d'arrêt ; étape 3,
    vérifiée, de `procedure-relance-r1-v1.md`).
  - CLA-04 : test des gardes du parent et de l'addendum (sain ; empreinte du parent fausse ; parent sans sceau ;
    addendum sans l'empreinte du parent ; addendum présent non scellé), `tests/test_runs_nuit_v2.py` ; essai du chemin
    réel avec addendum scellé, puis addendum présent non scellé ; essai des corrections réelles sous la consigne fausse.
  - CLA-05 : P-R5 dite prédiction ; réserve d'instrument déclarée comme ajout (E7), sans changer de classe de verdict ;
    marges avant les 80 % ; couverture par condition sous repli (E15).
  - CLA-06 : seuil fixé en connaissant le compte de 7, et condition « premier jeton » de l'enquête non retenue,
    déclarés (« Seuil »).
  - CLA-07 : définition de « notée » du code citée.
  - CLA-08 : « scénario bas » au lieu de « borne basse ».
  - CLA-09 : réserve sur la sensibilité « contexte exact » (« Métrique »).
  - CLA-10 : changement de commande du manifeste déclaré (E12, E16), signalé à conv-audit.
  - CLA-11 : dépenses citées (≈ 4,6 / 25 USD) ; section « Coût » déclarée devis par run.
  - CLA-12 : absence de garde sur le tokeniseur déclarée (étape 0).
- **Vérification de concordance de conv-audit** (lecteur neuf de conv-audit, sur le même brouillon 1
  `ab94755675725193c7d716bafde83ec5b6efc48b2034e625d38b461d22e1abe2`) : rapport
  `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v1.md` (branche
  `canal/conv-audit-n04`, `28d8bcff4e8a0ff9745a72ad6332296f580f84431c15f24cd98ba3c027a0555d`) ; message n° 343
  (`841cae63…`). Verdict : formats concordants ; un nœud de Lazar (N-A) ; concordant pour le reste si l'addendum change.
  Traitement (tous acceptés) :
  - C-1 : voie alternative retenue (E2 ; code v2 et tests alignés : `fidele` par la tolérance pour les épisodes non
    résolus) ; phrase fausse du brouillon 1 sur l'exigence de la principale corrigée (« Métrique ») ; P-R5 rendue au
    parent (≥ 90 %, au plus 93 %).
  - C-2 : versement du run relancé sur `calcul/r1-r2-reel-v1` par un commit neuf (E18 ; plan, étape 3 ; procédure,
    étape 7).
  - C-3 : réserve P-R5 portée par `tokenisation` et la lecture du fournisseur, sans changer aucune classe des analyses de
    conv-audit (E7).
  - C-4 : copie de la ligne remplacée dans la principale (l. 146) déclarée ; la décision de Lazar doit la couvrir (E19 ;
    procédure, étape 1).
  - C-5 : `contexte_conforme` défini tel que le code l'écrit ; préfixes non vérifiés déclarés (E14, « Métrique »).
  - C-6 : règle A étendue (étapes 4 à 7 ; table v2) ; résultat : @@C6@@
  - C-7 : le rejeu de R4 n'est pas relancé par cet addendum (« Statut », « R2 »).
- La concordance qui autorise le lancement porte sur la version scellée (plan, étape 1).
