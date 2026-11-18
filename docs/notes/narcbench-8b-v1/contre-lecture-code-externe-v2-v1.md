# Contre-lecture du code du bras externe NARCBench v2 (nos sondes et la recette de HELIOS sur les activations publiées) — v1

- **Contre-lecteur** : sous-agent neuf, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le développeur (Claude Opus 5.5),
  même famille (N-052). Je n'ai écrit ni ce code, ni sa version 1, ni le texte court du barreau 7 ; je ne serai ni lecteur ni
  juge de son verdict. Travail du 2026-11-18, de ≈ 16:57 à 17:10 UTC (`date -u`).
- **Mandat** : `docs/notes/narcbench-8b-v1/mandat-contre-lecture-code-externe-v2-v1.md` (empreinte vérifiée par son compagnon :
  OK), sous GO-2026-11-18-30.
- **Objet lu** : arbre `/home/user/narcbench-externe-v2`, branche locale `prep/narcbench-externe-v2`, tête
  `70cb77b848da03f044d676ce04fc79c3c24b371d` (vérifiée, arbre propre avant et après ; rien n'y a été modifié, aucun
  `__pycache__` écrit : `PYTHONDONTWRITEBYTECODE=1`).
- **Aucun score calculé ni lu sur les données réelles.** Sur elles : seulement l'essai de forme déjà écrit
  (`forme_externe_v2`, tailles, empreintes, en-têtes, comptes), rejoué une fois. Tous mes calculs de sondes et d'aires ont
  tourné sur des données factices fabriquées par les essais du développeur.

## Verdict

**Autorisable après corrections.** Aucun bloquant. La recette des auteurs est transcrite fidèlement : je l'ai vérifiée
contre **le script des auteurs lui-même** (et pas seulement contre sa recopie dans l'essai), y compris dans le régime où
l'arrêt à 8 itérations agit. Les corrections demandées portent sur les **essais** (règle R5 : plusieurs gardes n'ont pas d'essai
sur artefact ; le paramètre central « 8 itérations » n'est épinglé par aucun essai) et sur la **garde de lancement** (elle
refuse bien sans texte scellé ni clé au registre nominal, mais quatre trous la rendent contournable ou la laissent muette sur
le choix de l'augmentation).

## Ce que j'ai fait (preuves)

1. **Empreintes** : rapport du développeur `40fbdc70…`, manifeste des données `43106834…`, relevé des licences `ba780896…`,
   sortie de l'essai de forme `61cc1313…` : les quatre compagnons vérifient (`sha256sum -c` : OK).
2. **Script des auteurs** retéléchargé (public, licence MIT) : `probes/reproduce_LR.py` au commit `85fea3be2a9d` =
   `1d66fdc7ca81c972db357566b42a729e19f58f2ce85f5d8ecd0662c3c1141e0f` (égal à la citation) ; `config.py` (à la racine du dépôt
   des auteurs, pas sous `probes/` : `probes/config.py` répond 404) = `9c65f55ba781b0ba2872969a146f85a95c6454c08a3cf11f5cdb8db9841431c0`
   (égal à la citation du chargeur, l. 36). Bandes 26 à 30 et 32 à 37 : conformes (`config.py`, `MODEL_LAYERS`).
3. **Les 78 essais rejoués** : `78 passed in 25.00s` (environnement `.venv`, `PYTHONPATH=src:/home/user/narcbench-paquets-v2`,
   `-p no:cacheprovider`, `--basetemp` dans mon dossier temporaire, 8,4 Mo, supprimé).
4. **Oracle plus fort que celui du développeur** : j'ai importé les fonctions du **vrai script** (sans appeler `main`, modules
   `config` réel et `colours` factice) et comparé `externe_v2.reproduire_helios_v2` à `compute_all_results` suivi de
   l'agrégation des lignes 639 à 650, sur cinq jeux factices (classes égales avec domaine vide, épisode à trois agents, plus
   d'honnêtes, plus de colludeurs, signal faible à cinq domaines) × deux augmentations × quatre graines × deux couches, aires
   **et** erreur type :
   - 4 jeux sur 5 : **égalité au bit près** partout (32 comparaisons d'aire, 32 d'erreur type) ;
   - jeu « signal faible » : écart de **≈ 10⁻¹⁶** sur CORE (`0.47777777777777775` contre `0.47777777777777786`) ; en
     remplaçant, dans mon seul processus, l'aire du paquet gelé par `roc_auc_score`, **tout redevient égal au bit près** : le
     seul écart est l'arrondi entre l'aire de Mann-Whitney du paquet et `roc_auc_score`, pas la recette ;
   - **régime non convergé** (jouet de largeur 400, plus de dimensions que de lignes ; avertissement « Liblinear failed to
     converge » présent) : direction, `scaler`, direction d'un pli, aires de CORE et de STEGO **égales au bit près** au vrai
     script, avec et sans augmentation.
5. **Épreuve par mutation** sur une copie du module dans mon dossier temporaire : 28 mutations, **20 tuées, 8 survivantes**
   (détail en M1 et M2).
6. **Gardes sans essai d'artefact appelées à la main** : toutes arrêtent bien (détail en M2) ; trois absences de garde
   constatées (m1, m11, M3 c).
7. **Essai de forme rejoué** sur `/home/user/narcbench-donnees-v2` (vers mon dossier temporaire, supprimé) : sortie **égale**
   à celle du développeur hors date ; les huit fichiers vérifient tailles et empreintes.
8. **Épinglages** : `requirements-cpu.txt` de la branche = celui de `main` + les six lignes annoncées (scikit-learn 1.9.1,
   joblib 1.6.0, threadpoolctl 3.8.0, narwhals 2.28.0, cloudpickle 3.1.3) ; `/home/user/narcbench-paquets-v2` contient ces cinq
   versions exactes (`METADATA`) ; joblib 1.6.0 exige bien `cloudpickle>=3.0` ; l'avertissement de scikit-learn 1.9.1 dit
   lui-même « 'penalty' was deprecated in version 1.8 and will be removed in 1.10 ».

## Réponses aux six points du mandat

1. **Fidélité à la recette** : oui. E1 (lignes par message, ordre du fichier, troncature `col[:nc]`, tirage
   `RandomState(graine).choice`, `StandardScaler` sur `vstack([honnêtes, colludeurs])`), E2 (4 copies, 0,05, `RandomState(0)`,
   aucun défaut), E3 (moyenne de toutes les lignes publiques de discussion), E4 (graines 0 à 9, servies aussi à liblinear),
   pli sauté, domaine vide jamais tenu à l'écart, STEGO sauté à moins de quatre épisodes, agrégation `nanmean` sur graine ×
   couche : conformes aux lignes citées, et vérifiés contre le vrai script. « Égalité au bit près » : réelle sur les jouets des
   essais ; en général elle vaut **à l'arrondi de l'aire près** (m2). E6 (point de contrôle Llama introuvable, 401) : déclaré,
   sans effet sur le code. Domaines de CORE différents entre modèles : traités correctement (chaque modèle a ses propres plis,
   tirés de ses propres métadonnées), déclarés ; précision en m7.
2. **Gardes** : celles qui existent fonctionnent ; **R5 n'est pas tenue pour toutes** (M2) ; aucun repli silencieux trouvé
   dans `externe_v2` ; arrêts plus stricts que les auteurs : quatre déclarés, cinq non déclarés (m5).
3. **Graines** : la lecture du développeur **tient**, à mon avis (voir « R9 » plus bas) ; ce n'est pas un nœud si le texte
   court le déclare.
4. **Moyenne sur les jetons** : aucune dans nos familles (un jeton par message, agrégation « max » du harnais, qui refuse toute
   autre) ; les moyennes de la reproduction portent sur des messages (E3), des agents (Deception Split), des plis et des
   couples graine × couche, sous la marque « diagnostic, jamais en production (N-026) ». **Lecture avant scellement** : la
   commande refuse sans texte scellé et sans clé au registre (six refus éprouvés, code 2, rien d'écrit), **mais** voir M3.
5. **Épinglages** : conformes (preuve 8) ; la version n'est pas exigée à l'exécution (m3).
6. **Essais** : 78 verts (preuve 3).

## Bloquants

Aucun.

## Majeurs

- **M1 — L'arrêt à 8 itérations, cœur de la recette, n'est épinglé par aucun essai.**
  `src/controle_ia/narcbench/externe_v2.py` l. 62 (`PARAMETRES_LR`). Mutation « `max_iter` 8 → 100 » : **survivante** (33
  essais verts). Cause : les jouets des essais (largeur 12) convergent avant 8 itérations (aucun avertissement de
  non-convergence ; `tests/test_narcbench_externe_v2.py` l. 27, 41-72, et l. 420-423 qui n'exige que l'avertissement
  « penalty »). Sur les données réelles (372 lignes pour 5 120 ou 8 192 dimensions), l'arrêt agira. Le code est juste (preuve
  4, régime non convergé) ; c'est l'essai qui manque. **Correction** : un cas d'oracle à plus de dimensions que de lignes,
  qui exige l'avertissement de non-convergence et l'égalité au bit près de la direction.
- **M2 — R5 : gardes sans essai sur artefact, et mutations survivantes.** Chaque garde ci-dessous arrête bien quand je
  l'appelle à la main, mais aucun essai ne le prouve ; les retirer laisse la suite verte.
  - `externe_v2.py` l. 160-161, direction nulle (mutation survivante) ;
  - `externe_v2.py` l. 193-194 et 203-204, mode incohérent entre agents, CORE et STEGO (mutation survivante) ;
  - `externe_v2.py` l. 291-292, aucune graine ou aucune couche ;
  - `externe_v2.py` l. 353-354 et 361-362, nos familles : une classe manque à l'apprentissage ; aucun épisode de collusion STEGO ;
  - `externe_v2.py` l. 275, seuil « moins de quatre épisodes » : la borne n'est pas éprouvée (mutation « < 3 » survivante ;
    l'artefact de `tests/test_narcbench_externe_v2.py` l. 371 n'a que deux épisodes) ;
  - `externe_v2.py` l. 388-390, placebo de nos familles : remplacer le déclencheur par « jamais » survit
    (`tests/test_narcbench_externe_v2.py` l. 447 et 454 acceptent « D6 ou D2 », « D5 ou D2 ») : ni le cas sain ni l'artefact
    du câblage ne sont éprouvés ;
  - `externe_v1.py` l. 38, tolérance 0,03 de la garde de reproduction : « 0,3 » survit (les essais n'ont que 1,00 contre
    ≈ 0,5) ; la borne gelée de N7 mérite un cas à 0,03 et un cas juste au-delà ;
  - `lecture_externe_v2.py` l. 61-63, ligne du registre mal formée (cinq cellules, date, empreinte, chemin absolu, « .. ») :
    mutation survivante ;
  - `lecture_externe_v2.py` l. 73-74, « la ligne cite un autre texte que celui donné » : mutation survivante ; le cas
    `autre_fichier` de `tests/test_narcbench_lecture_externe_v2.py` l. 136 cite un fichier **absent**, c'est donc l'absence du
    fichier qui refuse, pas la comparaison ; il faut un second texte scellé présent.
- **M3 — Garde de lancement : quatre trous** (`src/controle_ia/narcbench/lecture_externe_v2.py`).
  - (a) l. 121 et 160-161 : `--registre` est libre. Un chemin absolu sort du dépôt (`depot / "/ailleurs"` vaut `/ailleurs`) :
    un registre de fortune, non commité, satisferait la garde. **Correction** : registre fixé
    (`registres/scellements-v1.md`), ou refus de tout chemin absolu ou hors du dépôt.
  - (b) l. 122-123 : `--augmentation`, `--couches-familles` et `--run-id` ne sont comparés à rien dans le texte scellé. E2
    est « sans défaut », mais rien n'empêche de lancer « code » sous un texte qui a tranché « papier ». **Correction** : le
    texte porte une ligne de configuration lue par programme (ou l'empreinte de la configuration canonique), et la commande
    refuse l'écart.
  - (c) aucune garde « déjà jouée » : deux lancements successifs à identifiants différents (un par augmentation) passent
    tous deux. **Correction** : refus si la ligne `EXTERNE-NARC` est au registre ou si un résultat `externe-narcbench-v2.json`
    existe déjà sous `diag/`.
  - (d) l. 76 : l'entropie est cherchée comme **sous-chaîne** du texte. Constaté : sur un texte daté du 2026-11-18, les
    entropies `2026` et `7` passent. **Correction** : motif exact (« Entropie : <entier> » entre limites de mot).

## Mineurs

- **m1** — `externe_v2.py` l. 359-369 : `nos_familles_v2` ne vérifie plus « deux colludeurs par épisode de collusion » (la
  v1 le faisait, `externe_v1.py` l. 51). Constaté : un épisode STEGO à trois colludeurs est lu sans arrêt (17 positifs, 15
  négatifs). Sans effet sur les données publiées (essai de forme : `collusion/2` partout). De même, l. 185-194 : un mode
  incohérent **entre lignes d'un même épisode** n'arrête pas (seul le mode entre agents est comparé). Ajouter les deux gardes.
- **m2** — « Égalité au bit près » (rapport du développeur, § 2 ; en-tête de l'essai) : vraie sur les jouets des essais, pas
  en général (preuve 4 : ≈ 10⁻¹⁶ par l'arrondi de l'aire). À écrire « au bit près pour la direction, à l'arrondi près pour
  l'aire » ; sans portée devant la tolérance de 0,03.
- **m3** — `externe_v2.py` l. 71-79 et `lecture_externe_v2.py` l. 106-113 : la version de scikit-learn est consignée, jamais
  exigée. L'épinglage est dit « porteur » ; une garde d'égalité à 1.9.1 au lancement le rendrait vrai.
- **m4** — Valeurs `NaN` possibles dans le résultat scellé (`externe_v2.py` l. 263, pli sans valeur ;
  `manifeste.ecrire_resultat` écrit par `json.dumps` sans `allow_nan=False`) : JSON non standard. Écrire `null` et un état.
- **m5** — Arrêts plus stricts que les auteurs **non déclarés** dans l'en-tête de `externe_v2.py` (l. 33-35) : rôle
  incohérent entre lignes (l. 185-186), mode incohérent entre agents (l. 193-194, 203-204), direction nulle (l. 160-161),
  activations qui ne sont pas en `float32` (l. 89-94), et, au chargeur, vingt champs exacts, valeurs fermées de mode, de rôle
  et de canal, valeurs non finies (`chargeur_externe_v1.py` l. 99-106, 125-126). Tous vont dans le sens de l'arrêt ; à
  déclarer dans le texte court.
- **m6** — En-tête de `tests/test_narcbench_externe_v2.py` l. 9-10 : « seules différences de la transcription » omet la
  branche PCA retirée, les avertissements masqués dans la recopie (l. 148-153), le calcul des scores d'apprentissage et
  `evaluate` retirés de la validation ; l'erreur type (l. 650 des auteurs) n'est pas dans l'oracle (je l'ai trouvée égale).
- **m7** — Rapport du développeur, § 1 point 4 : « "edu" d'un côté, "env" de l'autre » est incomplet : Qwen3-32B a seul
  « env » ; Llama-3.1-70B a seuls « edu » **et « sport »**. Non signalé : pour CORE de Llama-3.1-70B, le champ
  `scenario_domain` diffère du domaine des auteurs dans 14 domaines (forme longue contre abréviation, « cybersecurity » contre
  « cyber »… ; correspondance un à un, sans effet sur les plis). Le docstring de `externe_v1.py` l. 18 dit encore « 17 plis » ;
  `__init__.py` ne cite pas les modules v2.
- **m8** — `creer_manifeste` appelle `prereg.exiger_prereg_scelle` : le texte court doit être **conforme au gabarit** des
  préenregistrements, sinon arrêt (visible) après la vérification des données ; l'essai de bout en bout remplace cette garde
  (`tests/test_narcbench_lecture_externe_v2.py` l. 106, déclaré). Le rédacteur du texte doit le savoir. Le lancement est
  marqué `decisif=False` (`lecture_externe_v2.py` l. 134) : à confirmer par le texte.
- **m9** — Pas de journal des ouvertures ni des refus (T0.7 en tient un) ; le commit du code n'est pas comparé à celui que
  citera le texte ; un `GardeArret` sort en trace d'erreur (code 1), seul `RefusRegistre` rend le code 2.
- **m10** — `externe_v1.py` l. 40-41 : la garde compare aussi CORE aux Tables 2 et 3, alors que la prédiction N7 du brouillon
  4 ne nomme que STEGO : plus strict, à déclarer. Je n'ai **pas** revérifié ces nombres sur le PDF (hors mandat) ; R7 repose
  sur la vérification du 10 novembre.
- **m11** — `externe_v2.py` l. 334 : une graine booléenne passe (`True` est un entier pour Python). `externe_v1.py` l. 134 :
  un étage absent de la sortie est sauté sans bruit (inatteignable en v2, qui arrête avant). `externe_v2.py` l. 227-228 :
  garde inatteignable, sans essai.
- **m12** — Le dossier `/home/user/narcbench-paquets-v2` n'a pas d'empreinte consignée ; les auteurs ne figent pas leur
  version de scikit-learn (E7, déclaré) : les nombres publiés viennent d'une version inconnue.

## R9 et les graines 0 à 9 (point 3 du mandat)

La lecture du développeur tient. R9 gouverne **nos tirages** ; ici, 0 à 9 sont des constantes d'une recette publiée, au même
titre que `C = 25` et « 8 itérations » : les remplacer par des graines dérivées casserait la reproduction que la garde à 0,03
veut éprouver. Elles sont consignées dans la configuration du manifeste (`lecture_externe_v2.py` l. 128), et tous nos tirages
à nous (apprentissage, plancher, rééchantillonnage, placebo) viennent bien de `SeedSequence` par tâche nommée (l. 133-134,
147-149). Fait qui allège encore la question : sur les données publiées, les deux classes ont 186 lignes par modèle et chaque
épisode de collusion porte deux colludeurs et deux honnêtes à trois tours, donc la graine ne fait que permuter les honnêtes, et
`random_state` est sans effet sur ce solveur : les dix graines valent presque une. **Condition** : le texte court l'écrit en
toutes lettres comme lecture déclarée de R9 ; à ce prix, pas de nœud.

## Lectures hors du mandat (déclarées)

- En cherchant la ligne R-3310 par son numéro dans `registres/decisions.md`, la commande a aussi affiché le début de la ligne
  **R-3312**, qui la cite (décision de Lazar sur le barreau 8 et le bras A : aucun score, aucun résultat). La ligne R-3310
  elle-même mentionne, sans contenu, des lectures interdites déclarées par un explorateur. Rien d'autre.
- Le script et la configuration des auteurs (publics, MIT) ont été **exécutés en partie** (fonctions importées, `main` jamais
  appelé) sur des données factices, dans mon dossier temporaire : le mandat demande de vérifier l'oracle, c'est le moyen le
  plus fort ; je le déclare parce que le développeur, lui, ne les a jamais exécutés.
- Dossiers de cadre lus par extraits : décision N-061, devis v2 (lignes du bras externe), brouillon 4 (placebo, seuils, N7),
  contre-lecture 3 du brouillon 4 (`prereg/contre-lectures/narcbench-8b-descriptif-v1-brouillon4-cl3.md`, l. 31), lignes
  R-2175 et R-2184.
- Rien lu sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `calcul/` ou `donnees/` ; aucune recherche
  récursive. Rien commité, rien poussé, rien écrit sous `registres/`. Dossier temporaire vidé.
