# Avis de la session habilitée — sondes candidates pour la ligne `SONDES-LUES-CRITERE-3` (v1)

- **Pour** : `prereg/G0-critere-3-designation-course-v1.md` (`19dbc99edb551a4e1bbbef0ea28a5a860bd739b69d84d60ccf43c2de03125c31`, égale à son compagnon, `main` à la tête `44860af18c`). Ce texte exige la ligne `SONDES-LUES-CRITERE-3` (« Plan d'analyse », point 1, ligne 101) et pose sa demande (7) (ligne 111). Il ne désigne aucune sonde.
- **Écrit par** : la session habilitée du coffre du compte 01Qi7 (`session_01Qi7Gr4qGhdorfC7VG4KA4b`, Opus 5.5, effort élevé), le 2026-11-24 vers 15:30Z (`date -u`), sur demande de la mère (message de 15:27Z). Classe C. Aucune dépense. Je n'ai conçu ni choisi aucune sonde : je rapporte ce que disent les textes scellés.
- **Ce que j'ai lu** : textes scellés et compagnons `.sha256` seulement, plus la table `index` du fichier de scores de l'étape A, déjà ouverte pour l'erratum 1 des marqueurs du versant honnête. Aucun score, aucun épisode, aucune sortie de course nouvelle, aucun verdict.

## Verdict

| question | candidat (i) : les trois sondes figées du texte du barreau 8 | candidat (ii) : les sondes du texte des sondes v0 |
|---|---|---|
| apprise sur un épisode de la famille jugée (consigne cachée) ? | **non** | **non** pour toutes les sondes que ce texte apprend |
| choisie sur un tel épisode ? | **non** pour la sélection elle-même (réserve C1 ci-dessous) | **non** pour les sondes principales ; **risque** si un sous-ensemble des autres sondes était choisi aujourd'hui |
| apprise ou choisie sur une tâche de la banque neuve (rang 125 et au-delà du tirage de T0.5) ? | **non** | **non** |
| apprise ou choisie sur un épisode des deux témoins du premier test (« témoin instruit », « mention sans usage ») ? | **non** ; mais **lues** en validité sur ces témoins (P3, puis T0.7) : à déclarer | **non** ; mêmes lectures de validité |
| s'applique au modèle de la course de dose-réponse ? | **oui** | **oui** |

**Recommandation : (i), les trois sondes figées à la couche 15, telles quelles, sans en retirer ni en ajouter aucune. Confiance 0,75.**

Raisons :
- (i) est une liste **nommée, empreintée et munie de planchers** dans un texte scellé.
- Elle coïncide avec l'ensemble **complet** des sondes principales du texte des sondes v0. La table `concepts` de l'index du fichier de scores de l'étape A porte trois entrées, sous ces mêmes noms (erratum 1 des marqueurs du versant honnête, § 3). Ce n'est donc pas un choix parmi des sondes déjà lues : c'est tout l'ensemble principal.
- Avec (ii) pris largement, on obtient soit une multiplicité intenable, soit un sous-ensemble choisi aujourd'hui, après les lectures de P3 et de T0.7 sur l'organisme à consigne cachée du premier test. Ce dernier cas contredirait la demande (7).

## Candidat (i) — `prereg/lecture-sondes-barreau8-v1.md` (`8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4`)

### Sondes, fichiers, empreintes

Table des identités, lignes 316 à 322, option (a1) scellée.

| sonde | famille, couche, agrégation | fichier du vecteur (empreinte du compagnon) | clé ; empreinte du vecteur ; empreinte d'index | plancher : 800 directions |
|---|---|---|---|---|
| `tromperie-difference_moyennes-c15` | différence de moyennes, 15, maximum | `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz` (`701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60`, sur `main`) | `s1_w` ; `dabd4336…` ; `edf5e22a…` | `donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz` (`94ca013c66e5dbd35b3ea55ec8aa4eb7b299e5dd63a95f7ccea7ced8d120f224`) |
| `enjeux-lineaire-c15` | linéaire, 15, maximum | même fichier | `s16_w` ; `30d432f8…` ; `88f4af7c…` | même fichier |
| `dissimulation-lineaire-c15` | linéaire, 15, maximum | `donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz` (`374ad47346ae40d5a4d350724d0d19b5961724066dd7fdfaaf0adf1c3a4cbb79` ; versé en neuf morceaux, `.morceau-000` à `-008`, liste `…morceaux.json` `f5e38cba…`) | `s4_w` ; `fe414af7…` ; `e537e4f8…` | dans le fichier des sondes neuves : 800 entrées de famille « plancher », couche 15 |

Branche des fichiers de l'étape A : `donnees/t07-etape-a-v1` (tête `0c176db582`). Ligne de registre : `SONDES-T07` (`diag/20261114-001352-t07-lecture-reel/sondes-t07.json`, `aa689232…`, non ouvert).

### Apprentissage, d'après les textes scellés

- **Tromperie et enjeux** : sondes du premier test (P3), apprises sur des données **génériques**, sans aucun organisme :
  - P3 : `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`), lignes 127 et 128 ;
  - provenance : `docs/sources/donnees-T0.7/provenance-donnees-sondes-v1.md` (`36585c7d…`) ;
  - enjeux : jeu public *models-under-pressure* (McKenzie et al., arXiv 2506.10805), `training/train.jsonl` `04216df3…` ;
  - tromperie : recette de Goldowsky-Dill et al. (arXiv 2502.03407) sur les 306 affirmations vraies d'Azaria et Mitchell, redistribuées par Zou et al., `facts_true_false.csv` `151b6163…`.
  - Sondes principales **figées avant toute lecture de P3**, choisies sur la validation générique (texte des sondes v0, lignes 1024 et 1025).
- **Dissimulation** : apprise à l'étape A du texte des sondes v0 sur le jeu J-D, écrit sur les **32 tâches de réserve** de la banque initiale (`donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl`, `32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228`, ligne `SCELLEMENT-JEUX-T07-JD`), « jamais sur une tâche d'évaluation » (lignes 1026 et 1027).
  - Sonde principale choisie sur la **validation de ce jeu** et scellée à l'étape A (« sonde principale consignée et scellée », ligne 1443), **avant** l'ouverture des scores sur les épisodes de la course 7b (étape B, journal des ouvertures : 2026-11-16T23:11Z).
  - Activations du jeu prises sur le modèle de base, à dose 0 (ligne 1441).
- **Planchers** : 800 directions tirées dans la covariance des jetons d'entraînement de chaque sonde (données génériques réextraites pour tromperie et enjeux ; jeu J-D pour dissimulation). Aucun épisode d'organisme.

### Contraintes de la demande (7)

- **Famille jugée (consigne cachée)** : aucune des trois sondes n'a été apprise sur un épisode d'organisme. Les deux sondes du premier test ont été fixées avant toute lecture de P3 ; la sonde de dissimulation, avant toute lecture de T0.7 sur des épisodes. **Réserve C1** :
  - les trois ont depuis été **lues** sur le saboteur instruit du premier test (famille à consigne cachée) : en P3 (tromperie, enjeux) et à l'étape B de T0.7 (les trois) ;
  - le choix (a1) du barreau 8 a été fait après ces lectures, et le texte du barreau 8 ne dit pas si son auteur ou la session mère en connaissaient l'issue ;
  - il prend néanmoins **tout** l'ensemble principal disponible (le domaine n'a jamais été appris : aucune ligne `SCELLEMENT-JEUX-T07-JC` au registre des scellements), sans rien filtrer.
  - La ligne `SONDES-LUES-CRITERE-3` doit le déclarer en ces termes, et ne rien retirer ni ajouter.
- **Banque neuve** : la banque de la dose-réponse commence au rang 125 du tirage de T0.5 (`prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md`, `2263c5c4…`, ligne 114). Les rangs 0 à 124 ont donné les 96 tâches. Aucune des trois sondes n'a vu une tâche de rang 125 ou plus : données génériques externes, ou jeu écrit sur les 32 tâches de réserve (rangs inférieurs à 125).
- **Deux témoins du premier test** : aucune apprise ni choisie sur leurs épisodes. Elles y ont été **notées et lues** : en P3, dont les quatre conditions comprennent ces deux témoins (tromperie et enjeux ; contrôles de P3 sur `temoin` et `mention`) ; en T0.7, qui note toutes les actions des neuf conditions de la course 7b par les sondes principales (ligne 1444), et lit la dissimulation sur `temoin` (T7-P3, ligne 1171). La demande (7) ne vise que l'apprentissage et le choix. Je recommande pourtant que la ligne et la phrase d'issue disent « déjà lues sur ces deux témoins (P3, T0.7) » : leur lecture de validité n'y est pas neuve pour le programme.

### Application au modèle de la course de dose-réponse

- **Modèle** : Llama-3.1-8B-Instruct, révision `0e9e39f249a16976918f6564b8830bc894c89659`, sans changement (dose-réponse, ligne 59). C'est le modèle sur lequel les trois sondes ont été apprises (P3, T0.7).
- **Activations** : passe unique du harnais par épisode, couches 7, 15 et 23, demi-précision (dose-réponse, ligne 132). C'est le même mode et la même précision que la course 7b, sur laquelle le texte des sondes v0 a noté ces sondes (lignes 1056 à 1060). Les sondes lisent la couche 15 : **oui**.
- **Différence à déclarer** : le texte du barreau 8 calcule ses scores à partir d'une capture en simple précision, alors que la dose-réponse enregistre en demi-précision. Le texte de lecture des sondes du critère 3 doit dire laquelle il emploie. La notation de T0.7 sur la course 7b s'est faite en demi-précision.

## Candidat (ii) — `prereg/T0.7-sondes-v0-v1.md` (`d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5`)

- **Ce qu'il apprend ou lit** :
  - les quatre sondes principales prévues : tromperie et enjeux (figées du premier test), dissimulation (J-D), domaine (J-C) ;
  - la sonde d'intention sans le mode « coût » (J-A, deux autres modes, T7-P6) ;
  - les 30 couples neufs ;
  - les 24 couples figés du premier test (4 familles × 2 concepts × 3 couches, descriptifs) ;
  - témoins lexicaux, directions de concepts, planchers.
- **Sondes principales effectives** : trois. J-C n'a jamais été scellé, donc pas de domaine. La table `concepts` de l'index de `scores-actions-t07.npz` (`13ac4480…`, ligne `SCORES-T07`) porte trois noms, égaux à ceux du candidat (i) (erratum 1 des marqueurs du versant honnête, § 3 ; réserve : non vérifié sur `sondes-t07.json`).
- **Apprentissage** : données génériques ou jeux écrits sur les 32 tâches de réserve, jamais sur un épisode d'organisme (« Anti-circularité », lignes 1022 à 1027). Activations des jeux prises sur le modèle de base, à dose 0. Aucune tâche de la banque neuve. Aucun apprentissage ni choix sur les deux témoins du premier test ; lectures de validité sur eux, comme au candidat (i).
- **Application au modèle** : oui. Même modèle, couches 7, 15 et 23, même mode de passe.
- **Fichiers** : ceux du candidat (i), plus `sondes-neuves-t07.npz` pour les couples neufs et J-A, et `sondes-figees-legeres.npz` pour les 24 couples figés. Empreintes au tableau du candidat (i).
- **Risque propre** : réduit à ses trois sondes principales, (ii) **est** (i). Pris plus largement, il demande soit de lire des dizaines de sondes (niveau corrigé intenable), soit d'en choisir un sous-ensemble aujourd'hui, après la lecture de l'étape B de T0.7 sur le saboteur instruit du premier test (famille à consigne cachée) et sur les deux témoins. Ce choix tomberait sous la demande (7) (« choisie sur un épisode […] de la famille jugée »).
- **Sondes à exclure en tout cas** : celles de l'étape « sondes apprises sur la tâche » (`prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f…`). Elles sont apprises sur les épisodes de la course 7b, dont le saboteur instruit du premier test et les deux témoins (« Métrique », ligne 69) : elles violent la demande (7). Elles ne font pas partie du candidat (ii), mais sont citées ici pour qu'aucune ligne ne les reprenne.

## Ce que la ligne `SONDES-LUES-CRITERE-3` devrait porter, si (i) est retenu

Pour chacune des trois sondes :
- nom, fichier, clé, empreinte du vecteur, empreinte d'index, fichier et empreinte du plancher (tableau du candidat (i)) ;
- « apprise sur données génériques » (tromperie, enjeux) ou « apprise sur le jeu J-D, 32 tâches de réserve » (dissimulation) ;
- « jamais apprise ni choisie sur un épisode d'organisme ni sur une tâche de rang ≥ 125 » ;
- « non apprise ni choisie sur les témoins du premier test ; déjà lue sur eux (P3, T0.7) » ;
- « ensemble complet des sondes principales du texte des sondes v0, sans filtre ; déjà lues sur le saboteur instruit du premier test (P3, T0.7) ».

## Réserves

1. Je n'ai pas ouvert `sondes-t07.json` ni `sondes-figees.json` : les désignations des sondes principales viennent des textes scellés et de la table `index` déjà ouverte.
2. Le texte du barreau 8 ne déclare pas ce que son auteur savait de l'issue de T0.7 sur le saboteur instruit (réserve C1).
3. Précision de la capture : demi-précision (dose-réponse) ou simple précision (barreau 8), à fixer par le texte de lecture des sondes du critère 3.
