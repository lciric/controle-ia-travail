# Conception — l'atelier d'idées sur les bassins étroits et profonds, trois générations — v1

Écrite par un préparateur neuf (Claude Opus 5.5), sous-agent de la session mère, le 13 novembre 2026 (début 13:03 UTC,
heure relevée par `date -u`), sur la consigne `consigne-preparateur-organisme-bassins-etroits-v1.md` (`d404b6eb…`). Ligne de
dépense : **GO-2026-11-13-03** (60 USD, trois courses de 12 + 8 USD, échéance 2026-11-30). Rôle : **atelier d'idées**
(N-065, rôle 2) — les fiches sont du matériau, jamais une preuve ; tout usage décisif passe par un préenregistrement scellé
(R1). Citations obligatoires (N-064) pour tout texte qui présente l'organisme : POPPER (Huang et al., ICML 2025), Dwork et
al. (arXiv 1506.02629), Blum et Hardt « The Ladder » (arXiv 1502.04585), Co-Scientist (Nature 655, p. 487-496).

Pièces de ce dossier : question `question-organisme-bassins-etroits-v1.md` (`c188fa9a…`), témoins
`temoins-bassins-etroits-v1.json` (`748f391e…`), mesure sans appel `mesurer-consignes-g1-gabarit-40000-v1.json`
(`df384741…`), devis `devis-organisme-bassins-etroits-v1.md`, rapport `rapport-preparateur-v1.md` ; lanceur
`scripts/lancer_course_ideation_bassins_etroits_v1.py` (`a10420cc…`) et ses essais (`8fa7ae32…`).

## 1. Trois courses enchaînées, sans changer l'orchestrateur

- **Orchestrateur** : dépôt public `lciric/ideation-organism`, clone en lecture `/home/user/lciric/ideation-organism`
  (fait le 13 novembre, origine vérifiée), commit `be6b5af96c9e19812569d8dab55d6ce3978a3823`. Les neuf fichiers de la chaîne
  de lancement (`demonstrations/ideation_v8.py` → v7 → v6 → v5 → v4 → v2, `pole/ideation_v2.py`, `pole/adaptateurs.py`,
  `pole/relais.py`) ont **exactement** les empreintes épinglées par le lanceur v3 du 9 novembre (commit `f39a7f4a`) :
  la chaîne de la course à fiches n'a pas changé ; rien n'y est modifié, rien n'en est importé dans le lanceur.
- **Mode** : la course à fiches de l'atelier (sans `--course-2`, la main passe du v8 au v2), comme le 8 novembre. La course 2
  à monde planté (`--course-2`, juge statistique) n'est pas employée : elle demande une configuration et un monde, et ce
  n'est pas l'objet du GO.
- **Une génération = deux temps**, que le lanceur choisit sur l'état du disque (jamais par un argument) :
  1. **course** : proposeurs en deux passes, juge Opus, consigne du juge Argon mise en attente scellée ; aucun classement ;
  2. **lecture humaine** (la mère, ou Lazar) de toutes les fiches validées, relecture « aucune recette » (R-607), puis
     **attestation scellée** au chemin fixe `docs/notes/organisme-bassins-etroits-v1/attestations/attestation-lecture-
     humaine-g<g>-v1.json` (`{lecteur, lu_le, fiches_validees_sha256, consignes_en_attente_sha256}` ; le manifeste de fin
     du lanceur imprime les deux empreintes à recopier) ;
  3. **bras** (même commande, même argument) : le juge Argon note, l'orchestrateur écrit le classement agrégé.
- **Commande**, seule et exacte : `/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v1.py G`,
  G ∈ {1, 2, 3} ; tout autre argument est refusé. Une génération jouée (course et bras réussis) n'est jamais rejouée ; une
  génération tentée avec dépense n'est jamais relancée par ce lanceur (R3 : aucune course visant un « bon » résultat ; une
  relance demande un nœud et une version neuve, R12) ; seule une tentative refusée avant tout départ (rien dépensé) peut
  être refaite, trois au plus.

## 2. Ce que chaque génération reçoit

| | Proposeurs (`--piece`) | Juges (`--piece-juge`) |
|---|---|---|
| Toutes | la question (`--question`, la même aux trois générations) ; `faits-v1.md` du collisionneur (`d19b5400…`), auquel la question renvoie (« l'organisme décrit aux faits ») | `faits-v1.md` |
| Génération 1 | **le recoupement des méthodes** du tour du collisionneur, fourni par la mère | le même recoupement |
| Générations 2 et 3 | **les fiches reçues** de la génération précédente (§ 3), pièce écrite par le lanceur | la même pièce |

- **Recoupement (génération 1)** : chemin fixe `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md`,
  **scellé** (compagnon `.sha256`), UTF-8, non vide, **au plus 40 000 caractères** ; matériau de niveau méthode (aucune
  recette), sans secret ; le lanceur refuse sinon et porte son empreinte au manifeste. Le chemin ne contient aucun des
  fragments que l'orchestrateur refuse (`donnees`, `banque`, `prereg`, `test-final`…).
- **Pourquoi servir aux juges les mêmes pièces qu'aux proposeurs** : la grille note l'originalité « d'après les pièces
  d'antériorité servies » ; une fiche qui recopie le recoupement, ou une fiche reçue, est alors jugée occupée.
- **Pourquoi ces tailles** (mesure sans appel du 13 novembre, pièce au gabarit de 40 000 caractères, `df384741…`) :
  consigne de passe 1 = 56 691 caractères ; la consigne de contrôle d'Argon (la plus grosse : passe 1 + six fiches au
  maximum du gabarit) = 322 793 ; la garde de la course de l'orchestrateur vaut 400 000 (marge 77 207) ; la garde avant
  envoi de la commande d'Argon demande au contrôle un plafond de 1,21 USD à 4 caractères par jeton (1,45 à 3, lecture
  prudente), sous les 1,5 réglés. Avec 50 000 caractères de fiches reçues, la consigne de contrôle passe à ≈ 333 000 :
  tout tient encore ; le lanceur **remesure** à chaque génération (`--mesurer-consignes`, sans appel) et refuse si une
  garde ne tient pas.

## 3. Règle de passage, écrite d'avance

Appliquée par programme (`choisir_fiches_recues`), sur les fichiers scellés de la génération g − 1 :

1. **Source** : le classement agrégé écrit par le bras (`classement.json`, deux juges, agrégat « moyenne » de
   l'orchestrateur), seulement s'il est **lisible** (`lisible_L2_L4` vrai : les quatre témoins tenus chez chaque juge).
   Classement illisible, témoins échoués, bras sans juge externe : **aucune fiche transmise**, génération suivante refusée,
   nœud pour la mère (pas de relance, R3).
2. **Classement** : l'ordre du rang de l'orchestrateur — éligibles d'abord (max(avantage, originalité) ≥ 2 sur
   l'agrégat), puis total, puis max(avantage, originalité), puis robustesse, puis l'empreinte de la fiche (départage
   déterministe, indépendant des étiquettes des juges). Témoins exclus ; inéligibles exclus.
3. **Prise** : dans cet ordre, une fiche est **sautée** si (a) un juge (Opus ou Argon) l'a signalée en doublon d'une fiche
   déjà prise (doublons des juges remis en identifiants par les clés d'anonymisation de l'orchestrateur) ; (b) elle est
   l'autre passe d'une fiche déjà prise (appariement « même nom, sinon texte le plus proche » des mesures de convergence
   de l'orchestrateur — le 8 novembre, 4 retenues sur 5 étaient des paires passe 1 / passe 2, R-1865) ; (c) elle porterait
   la pièce au-delà de **50 000 caractères** (on passe à la suivante). Arrêt à **cinq** fiches, ou à l'épuisement.
4. **Service** : les fiches prises sont servies **dans l'ordre de leur empreinte** (sans rapport avec le rang), étiquetées
   `G<g>-R1` à `G<g>-R5`, **sans note, sans rang, sans auteur, sans passe** (vue servie de l'orchestrateur) ; le texte de
   tête dit qu'elles viennent d'un tournoi de juges à modèles, matériau et non preuve. La sélection (identifiants, rangs,
   fiches sautées et motifs) est au manifeste de départ du lanceur, jamais dans la pièce.
5. **Aucune fiche prise** : refus, nœud.

**Lecture d'N-053 à confirmer** (question ouverte) : le GO de Lazar transmet « les fiches retenues » ; la sélection se fait
donc sur le classement des juges de l'atelier (ses propres juges, non un moniteur du programme), et **aucun score n'est servi
à un agent**. Si la mère lit l'invariant d'N-053 comme couvrant aussi cette sélection, il faut une autre règle (par exemple
un tirage uniforme parmi les éligibles) : nœud.

## 4. Proposeurs et juges

| Rôle | Modèles | Plafond par session |
|---|---|---|
| Proposeurs (deux passes, six fiches au plus par passe) | Opus 5.5 (`claude-opus-5-5`), Fable 5.1 (`claude-fable-5-1`), Argon (`gemini-4-argon`, commande externe) | 2,0 ; 2,0 ; Argon passe 1 1,3, passe 2 1,9 |
| Juge de la course | Opus 5.5 | 1,5 |
| Juge différé (bras) | Argon | 2,5, contrôle court 0,6 |

Ce que le code permet, lu dans le commit épinglé :
- **Fable 5.2 : refusée.** `pole/adaptateurs.py` n'admet que les modèles qui commencent par `claude-opus-5-5` ou
  `claude-fable-5-1` (`MODELES_REELS_PERMIS`) ; `claude-fable-5-2` lève `ModeleNonPermis` avant tout appel. Fable 5.1 seule.
- **Un juge d'une autre lignée que tous les proposeurs : impossible avec ce code.** Une course réelle exige à la fois
  `--proposeur-externe` et `--juge-externe` (« décision de Lazar : poids égal, égalité », `demonstrations/ideation_v2.py`,
  refus avant tout appel sinon), et la commande externe ne joue qu'un modèle (`gemini-4-argon`). Chaque juge partage donc
  la lignée d'au moins un proposeur. Atténuations : juges aveugles aux auteurs (anonymisation par juge) ; l'orchestrateur
  rapporte, par juge, le total moyen donné aux fiches de son propre modèle et aux autres (lecture d'auto-préférence) ;
  deux lignées de juges (Claude, Gemini).
- **Pas de troisième juge** (Fable) : il ferait passer l'agrégat à la médiane et coûterait 1,5 de plus (somme Claude 11,4 ≤
  12, permis), mais chaque témoin devrait tenir chez trois juges pour que la chaîne passe ; laissé en option (§ 8).
- **Six fiches** par proposeur et par passe (huit le 8 novembre) : avec des pièces plus longues, huit fiches feraient
  passer la consigne de contrôle d'Argon au-delà de ce que ses plafonds paient (garde de la course et garde avant envoi de
  la commande) ; six est aussi le nombre de la conception à plusieurs générations ([C3] § 5.1, résumé dans les faits).
- **Graine** de la génération g : 2026111300 + g, passée à l'orchestrateur, qui en dérive les siennes par sa règle
  (SHA-256, écrite à ses manifestes ; écart à R9 dit : l'orchestrateur n'emploie pas `SeedSequence`).

## 5. Témoins plantés (`temoins-bassins-etroits-v1.json`)

Écrits par moi, tiers (ni proposeur ni juge), sans lecture d'aucune fiche ; validés par le chargeur réel de l'orchestrateur
(`charger_temoins`, quatre classes, aucun signal de la garde du niveau méthode) lors d'une passe simulée sans appel.

| Classe | Témoin | Attendu |
|---|---|---|
| vrai | « Courbe nulle exacte des tirages indépendants contre la largeur plantée d'un bassin » : toute méthode doit battre 1 − (1 − r)^n à coût égal, d'autant plus que r est petit ; avantage propre à l'organisme (l'oracle mesure la couverture d'un bassin de largeur connue) | éligible |
| jumeau | la même idée renommée et réécrite | éligible, signalé en doublon du vrai |
| faux falsifiabilité | « Indice d'élégance profonde noté par les proposeurs eux-mêmes » : prédiction vague, mesure par impression, auto-évaluation copiable et occupée | inéligible, falsifiabilité ≤ 1 |
| faux antériorité | « Montée de la température d'échantillonnage » présentée comme inédite | inéligible, originalité ≤ 1 |

Un témoin échoué chez un juge rend le classement illisible : la génération suivante est refusée (§ 3.1).

## 6. Ce qui est mesuré d'une génération à l'autre — sans juge de plus

Toutes ces mesures sont calculées **par programme, après la course**, sur les fichiers scellés ; aucune n'est servie à un
agent ni n'entre dans la sélection.

1. **Part déclarée** de fiches qui raffinent une fiche reçue : la question demande d'inscrire dans `questions_servies`
   l'élément `raffine G<g>-R<i>` (étiquette exacte) ou `nouvelle` ; on compte, par génération et par proposeur, les fiches
   validées qui portent au moins un `raffine …`, celles qui portent `nouvelle`, et celles qui ne portent ni l'un ni l'autre
   (consigne non suivie).
2. **Part lexicale** : pour chaque fiche validée de la génération g + 1, la plus petite distance d'édition (1 − rapport de
   `difflib.SequenceMatcher` sur les mots, la mesure même de l'orchestrateur) à chacune des fiches reçues ; distribution
   rapportée ; « proche » si ≤ 0,6 — **seuil exploratoire, non calibré**, écrit ici avant toute lecture.
3. **Concordance** entre 1 et 2 (une fiche déclarée `nouvelle` mais lexicalement proche, ou l'inverse), rapportée.
4. Rapportés aussi : nombre de groupes de doublons par juge ; part d'éligibles ; état des témoins ; couverture des questions
   Q1 à Q5 ; part des pièces citées (mesures de convergence de l'orchestrateur) ; coût par génération.
5. **Non mesuré** : qu'une fiche « ouvre une idée neuve » **au sens du fond**. La déclaration est un auto-rapport, la
   distance est lexicale ; sans juge de plus, la nouveauté de l'idée ne se mesure pas.

Le programme de ces mesures **n'est pas écrit dans ce lot** : à écrire (nom neuf), contre-lire et sceller **avant** la
lecture de la génération 2 ; ses seuils sont ceux ci-dessus.

## 7. Limites

- **Juges à modèles : matériau, pas preuve.** Des témoins tenus ne prouvent pas que les juges classent bien ; ils écartent
  seulement les erreurs grossières que les témoins visent.
- **La règle de passage elle-même pousse au raffinement** : transmettre les cinq premières fiches du tournoi invite la
  génération suivante à creuser les bassins déjà classés — exactement ce que la question veut éviter. Trois générations sans
  bras témoin ne disent rien de l'effet des générations ; les mesures du § 6 décrivent, elles ne prouvent pas.
- Même lignée entre juges et proposeurs (§ 4) ; auto-préférence possible, rapportée.
- La question parle de l'organisme à monde planté ; les proposeurs de l'atelier ne le voient qu'à travers les faits (aucune
  loi plantée, aucun chiffre) ; leurs fiches ne valent qu'à l'épreuve d'un préenregistrement sur ce monde.
- Aucun accès au Web (commande d'Argon sans `--recherche-web`, proposeurs Claude sans outil) : les antériorités sont
  RAPPORTE (lues dans une pièce) ou SUPPOSE (de mémoire), jamais vérifiées par l'atelier.
- L'attestation humaine entre la course et le bras est obligatoire dans le code : chaque génération attend un lecteur.

## 8. Options laissées à la mère ou à Lazar

(a) **Telle quelle** (recommandée, confiance 0,65) ; (b) troisième juge Fable 5.1 (médiane ; plus robuste, plus fragile aux
témoins, + 1,5 USD de plafond par génération, toujours ≤ 20) ; (c) règle de passage par tirage uniforme parmi les
éligibles si N-053 est lu comme couvrant la sélection (§ 3).
