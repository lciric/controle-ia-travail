# Préenregistrement — pilote d'une génération : les vrais proposeurs trouvent-ils une composante conditionnelle avant sa condition ? — v1, brouillon 1

**Statut : brouillon 1 (R1), non contre-lu, non scellé comme texte décisif.** Il est scellé comme pièce de travail (compagnon
`.sha256`) ; il devient candidat au scellement après les décisions Q-P1 à Q-P4 (section 15), le code de la section 11 et la
contre-lecture R2 (section 17). **Aucune course, aucun appel de modèle, aucune dépense** avant : le texte scellé, la ligne de
GO inscrite par Lazar (section 14), les préalables de la section 12.

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. **Je
  suis aussi l'auteur de la conception v4** (famille MR-2, règle de garde, modèle de proposeurs synthétiques dont la valeur 0,02)
  que ce pilote met à l'épreuve : conflit dit ; la contre-lecture doit venir d'un lecteur neuf d'une autre lignée (Fable 5.2).
- **Commande** : mots de Lazar **R-2501**, transmis par la mère : « Q-14 (b) — pilote d'abord ; Q-15 (b) — 24 mondes de
  calibration au banc », et la consigne de la mère (une génération ; vrais proposeurs Fable 5.2, Opus 5.5, Argon, Astra, isolés,
  réponses brutes et témoins d'isolement versés ; 2 mondes de calibration MR-2 tirés par programme avec un secret engagé avant,
  forme de Q-3, jamais publiés ; mesure principale définie et calculée par un programme, avec intervalle ; règle écrite d'avance ;
  mesures secondaires sur la chaîne réelle ; aucun résultat de progrès ; R3).
- **Heures** (`date -u`) : début 2026-11-13 09:26:33 ; fin de la rédaction : voir la dernière ligne.
- **Interpréteur des calculs de ce brouillon** : Python 3.13.18, numpy 2.5.3 (système) ; un processus à la fois, `ulimit -v
  6000000`, `OMP_NUM_THREADS=2` ; calculs légers seulement (moins d'une minute chacun).

## Documents qui font foi (chemin, empreinte sha256)

Chemins relatifs à `docs/notes/organisme-multi-generations-v1/`.

| pièce | chemin | empreinte |
|---|---|---|
| conception v4 (famille MR-2, règle de garde, simulations) | `conception-monde-riche-doublons-v4.md` | `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc` |
| générateur et vérificateur MR-2, course simulée | `outils-v4/monde_riche_v4.py` | `4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8` |
| sorties v4 (résumé ; table par monde) | `sorties-v4/resume-v4.json` ; `sorties-v4/table-v4.json` | `c4c55f010bed7e28d0e87c72a8702cabd4f0807a7023309f4c62c238829dfbd5` ; `145c0dbcaeff5c5657ce7680a8375f1413686e382b8f754603fb66e5bcfb0604` |
| note de décision de la course (Q-1 à Q-13) | `preenregistrement-v1/note-decisions-lazar-v1.md` | `d2bcf5810be0ac7cec214eb908a873a2a98cb6500ce74478868cc3eb68f2b2ee` |
| préenregistrement de la course, brouillon 3 (modèle de forme) | `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon3.md` | `2dda3b74ff5e13d56a8f0818623b0b64730a3b3da5f86a136df321343f653a39` |
| texte v2 de la v67 (modèle de forme ; chaîne réelle) | `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md` | `80fe4f03b4905b2376b8cd16873c9ab93da3b97e4e01a9a2932be329bab0954d` (égale à son compagnon et au verdict v67) |
| code v67 (différentiel lu, non exécuté) | `docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/code-v67/organisme-v67-contre-7e415cb.patch` | compagnon |
| **seuils de la règle** (script ; sortie) | `pilote-v1/outils/seuil_pilote_v1.py` ; `pilote-v1/sorties/seuil-pilote-v1.json` | `14eecfccdd83274d32388fcf2771bc608f0ad83bd8a3e5ac1161322d775e46ab` ; `16cd10047d2b353e05e02c711dbaa8943e5845ad6e60732dfad7dbb6a03590c5` |
| **programme de la mesure** (mesure, règle, puissance, essai) | `pilote-v1/outils/mesure_pilote_v1.py` | `0d806aca4b8f21c777c836fe39286326aa6753b060782123f9c117f32cf491a4` |
| puissance de la règle ; essai du programme (cas sain et artefacts) | `pilote-v1/sorties/puissance-pilote-v1.json` ; `pilote-v1/sorties/essai-mesure-pilote-v1.json` | `84b214f7b17b0c6f92e50504a068ec0ac33bd3cc41656103ab86058143535064` ; `9ba9522374e06092caaba8515119dd2d27b68f2e9df74a1f7050eb320998de9f` |
| devis (script ; sortie) | `pilote-v1/outils/devis_pilote_v1.py` ; `pilote-v1/sorties/devis-pilote-v1.json` | `99d5d677efb8745d90db8e6bb1ba8e94dffd1f0a8e81066dd59ff76eded1687b` ; `dcae0286ba5d5fb46c85c407eb9ad2f59ab5ac2305022187ad805ed9671a9763` |

## 0. En dix lignes

1. **Question** : quand une composante de la famille MR-2 n'est visible qu'en conditionnant sur le signe d'un autre trait, un
   vrai proposeur la propose-t-il **avant** que sa condition soit dans l'archive ? La conception v4 l'a **supposé rare** (0,02 par
   carte, sans pièce) ; sa règle de garde ne tient que sous cette hypothèse (8 mondes sur 12 ; 0 sur 12 si 0,25).
2. **Dessin** : une génération, 4 vrais proposeurs (Fable 5.2, Opus 5.5, Argon, Astra), un appel chacun, au plus 6 cartes, sur
   **2 mondes MR-2** tirés par programme d'un secret engagé avant (forme Q-3 (c)), **jamais publiés**, jamais réutilisés.
3. **Bras A** (archive {K1}) : mesure principale. **Bras B** (archive {K1 ; « K1 + condition »}), si Lazar le retient (Q-P1) :
   la même probabilité quand la condition est connue.
4. **Mesure** (programme `mesure_pilote_v1.py`) : un appel « trouve » une conditionnelle si une de ses cartes la porte (attribution
   de l'oracle ≥ 0,75 · I_i) ; p_c = 1 − (1 − q̂)^(1/6), q̂ = part des appels qui trouvent ; intervalle de Clopper-Pearson à 95 %.
5. **Règle** : borne basse de p_c > **0,051** (au-delà, la règle de garde d'un banc de 24 mondes tient avec probabilité ≤ 0,05)
   → **P-1** : MR-2 ne sert pas telle quelle, nœud de Lazar ; aucun appel répondu en bras A → **P-0**, nœud ; sinon **P-2** :
   banc de 24 mondes avec p_c ponctuel à la place de 0,02 (et p_v à la place de 0,25 si le bras B est joué).
6. **Puissance, dite d'avance** : à 8 appels, P-1 sort avec probabilité 0,04 si p vaut 0,075, 0,36 si 0,15, 0,84 si 0,25 ; le
   pilote **ne réfute** qu'une hypothèse franchement fausse ; le reste se décide au banc, avec la valeur mesurée.
7. **Secondaires** : probabilités par classe (forte, moyenne, faible, latente) contre le modèle synthétique ; chaîne réelle
   éprouvée : coûts par fournisseur, troncatures, refus au gardien, cartes non évaluables, sessions en échec.
8. **Aucun progrès revendiqué** (une génération) ; aucun signe visé (R3) : les trois issues mènent chacune à une action écrite.
9. **Devis** (bras A et B, recommandé) : crédits de Claude **20 USD au pire**, ≈ 9,60 attendus ; hors crédits **19 USD au pire**
   (Argon 8, Astra 8, machine 3), ≈ 5,30 attendus. Bras A seul : 10 et 11.
10. **Code** : la chaîne v67 ne sait ni charger un monde privé à 8 traits, ni appeler Claude ou Astra, ni jouer une seule
    génération sans étage ; section 11, sans l'écrire.

## 1. Question, motivation, ce qui existe

La conception v4 (`47e38ec0…`, §3.3, §4.2) a rendu la question du progrès répondable **sous une hypothèse** : un proposeur
propose rarement une composante conditionnelle tant que sa condition n'est pas connue. La part marginale mesure la structure
(une correction sans condition ne rend que 2 % en médiane de l'information d'une conditionnelle, 14 composantes) ; elle ne dit
rien de ce que font les proposeurs, qui reçoivent 400 épisodes de développement et peuvent essayer des conditions au hasard ou
par méthode. Lazar a retenu le pilote (Q-14 (b), R-2501) : mesurer cette probabilité avec les vrais proposeurs avant de
dépenser la course, et **remplacer la valeur 0,02** du modèle du banc par la valeur mesurée.

Ce qui existe : la course réelle v67 (verdict `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` :
issue C1, chaîne garde ; deux proposeurs Kimi et Argon ; monde jouet S-V1 à 2 traits) ; la conception v4 et ses simulations ;
aucune mesure du comportement des proposeurs sur un monde à composantes conditionnelles.

## 2. Hypothèse

H-P : la probabilité par carte qu'un vrai proposeur, sans la condition dans l'archive, propose une composante conditionnelle
MR-2 est assez basse pour que la règle de garde d'un banc de 24 mondes puisse tenir (p_c ≤ 0,051). Le pilote **ne vise aucun
signe** : il donne une valeur au paramètre du banc, et ne réfute H-P que si elle est franchement fausse (section 4.2).

## 3. Dessin

### 3.1 Mondes

- **Famille MR-2** (conception v4, §2 ; générateur et vérificateur `outils-v4/monde_riche_v4.py`, `4b165847…`, portés dans
  l'arbre de l'organisme sous un nom neuf, section 11) ; vérification C0 à C8 v4 (toute conditionnelle certifiée, C8 à m = 48),
  au plus 8 tirages par monde, refus rapportés.
- **Deux mondes du pilote**, d'un **secret du pilote** distinct des secrets de calibration et de test, par la forme de Q-3 (c) :
  (1) ce texte scellé, sans secret ; (2) pièces servies gelées et scellées ; (3) secret machine de 32 octets tiré sur la machine
  privée, **empreinte inscrite et poussée** ; (4) puis la phrase de Lazar, empreinte inscrite ; (5) graine du monde r ∈ {1, 2},
  tirage t ∈ {0, …, 7} : sha256(secret ∥ phrase ∥ empreinte du texte scellé ∥ « pilote » ∥ r ∥ t), entier ≥ 2⁶⁴ ; (6) génération
  et vérification dans un processus qui n'imprime que des empreintes et des contrôles ; fichiers des mondes dans un dossier privé
  de la liste blanche (`ecrire_prive`), **hors de tout dépôt** ; seules leurs empreintes vont au registre.
- **Jamais publiés**, ni le secret ni la phrase ni les devis des mondes, même après le pilote (plus strict que Q-10 (a)) ; **jamais
  réutilisés** : ni au banc de calibration (24 mondes, Q-15 (b)), ni en test.
- Qui lit les mondes : des programmes seulement (générateur, vérificateur, lanceur, `mesure_pilote_v1.py`) ; le lecteur du
  verdict lit la sortie de la mesure, jamais un devis.

### 3.2 Archive servie et bras

- **K1** de chaque monde (`k1_du_monde` : softmax du seul trait de la forte principale, ajustée sous le monde), arrondie à six
  décimales, servie comme héritage de génération 0 (comme la v67 et la course).
- **Bras A** : archive {K1}. Toutes les conditionnelles ont leur condition hors de l'archive (la condition est une moyenne ou la
  conditionnelle précédente, jamais l'effet de K1 ; le programme refuse le monde sinon).
- **Bras B** (Q-P1) : archive {K1 ; V-K1+B}, V-K1+B la loi plantée « K1 + un effet » de la condition B de la première
  conditionnelle (`jeu_plante_mr1`, tempérée et inclinée), servie **comme une loi retenue d'une génération 0**, sans mention de
  ce qu'elle contient. Sessions neuves, distinctes de celles du bras A.

### 3.3 Proposeurs (composition de la course, Q-7 (a))

| proposeur | modèle | crédits | plafond de session |
|---|---|---|---|
| Fable 5.2 | `claude-fable-5-2` | Claude | 3 USD |
| Opus 5.5 | `claude-opus-5-5` | Claude | 2 USD |
| Argon | `gemini-4-argon` | hors crédits | 2 USD |
| Astra | `gpt-6-astra` (identifiant « rapporté, à confirmer » ; prix supposé 10 / 50 USD par million de jetons) | hors crédits | 2 USD |

- **Un appel** par proposeur, par monde et par bras ; **au plus 6 cartes** ; une carte au-delà de la sixième est refusée au
  gardien et comptée ; **aucune reprise** d'un appel en échec (il est compté « échec », ses 6 emplacements sortent du dénominateur
  et sont rapportés).
- **Gabarit** : celui de la course (dimension 8, 3 sous-populations, grammaire servie avec `par_sous_population` et `si_sinon`
  sur un trait ou une sous-population), **aucune description des sortes d'effets** ni de la famille ; aucune consigne
  diversifiante ; la tranche de 400 épisodes de développement du monde, comme dans la course.
- **Isolement** : relais par fournisseur ; une session neuve sans historique par appel ; **réponse brute** de chaque appel (corps
  entier, raison d'arrêt, en-tête du modèle servi, usage) écrite et scellée **avant** l'extraction des cartes (garde 26 de la
  course) ; **témoin d'isolement** de chaque session (identité du relais, absence d'historique, empreinte du texte servi égale à
  celle reçue) versé ; absence = arrêt.
- **Gardien** mécanique (grammaire, bornes ±4, évaluation sur un jeu factice à la dimension du monde). **Aucun juge, aucun test
  de mort, aucun expérimentateur, aucun vérificateur** dans le dessin recommandé (Q-P2 (a)).

### 3.4 Ordre

Texte scellé → GO inscrit → secret du pilote engagé et poussé → phrase de Lazar → mondes générés et vérifiés, empreintes au
registre → essai à blanc de la chaîne (proposeurs factices) avec les mêmes pièces servies → appels réels, bras A puis bras B,
monde 1 puis monde 2 → réponses brutes et témoins scellés → extraction des cartes → gardien → fichier des cartes scellé →
**mesure** par `mesure_pilote_v1.py` (une seule fois) → rapatriement des pièces (réponses brutes, témoins, cartes, sortie de la
mesure ; jamais les mondes) → destruction de la machine (R10).

## 4. Prédictions chiffrées et puissance

### 4.1 Valeurs de comparaison (aucune n'est un signe visé)

| quantité | hypothèse de la conception v4 | autre repère |
|---|---|---|
| p_c (bras A, par carte, équivalent appel) | 0,02 (« masquage ») | 0,25 (« sans masquage ») |
| p_v (bras B) | 0,25 | — |
| forte / moyenne / faible / latente (bras A) | 0,5 / 0,25 / 0,1 / 0,25 | — |

### 4.2 Puissance de la règle (`puissance-pilote-v1.json`, `84b214f7…`)

Probabilité que la règle rende P-1, selon la vraie probabilité par carte p (appels indépendants ; 8 appels = bras A, 2 mondes,
une conditionnelle par monde ; 10 à 16 avec les chaînes) :

| appels | p = 0,02 | 0,051 | 0,075 | 0,10 | 0,15 | 0,25 | appels qui trouvent, au moins, pour P-1 |
|---|---|---|---|---|---|---|---|
| 8 | 0,0001 | 0,0064 | 0,0353 | 0,1071 | 0,3649 | 0,8432 | 6 |
| 12 | 0,0001 | 0,0217 | 0,1157 | 0,3053 | 0,7238 | 0,9890 | 7 |
| 16 | 0,0000 | 0,0126 | 0,0979 | 0,3070 | 0,7775 | 0,9967 | 9 |

Lecture dite d'avance : **le pilote ne réfute H-P que si les proposeurs trouvent souvent** (p ≳ 0,15) ; entre 0,05 et 0,15, il
rend presque toujours P-2 et c'est le **banc**, nourri de p_c mesuré, qui dira que la règle de garde ne tient pas. Avec 8 à 16
appels, p_c ponctuel est grossier (pas de 1/8 sur q) : le banc l'emploie tel quel, et rapporte la règle aussi aux deux bornes de
l'intervalle (mesure, ne décide pas).

## 5. Métriques (programme `mesure_pilote_v1.py`, `0d806aca…`)

- **Porte** : carte admise au gardien, évaluable par l'oracle, attribution Δ_i = gain(carte | W) − gain(carte | W₋ᵢ) ≥ τ_i =
  max(0,005 ; 0,75 · I_i) (oracle de 12 000 instances, graine dérivée du monde). Carte absente, refusée au gardien ou non
  évaluable (loi à mémoire, type inconnu) : ne porte pas, comptée à part.
- **Principale** : p_c = 1 − (1 − q̂)^(1/6), q̂ = (appels du bras A qui trouvent une conditionnelle donnée) / (appels répondus ×
  conditionnelles du monde), mise en commun sur les deux mondes ; intervalle à 95 % : Clopper-Pearson sur q, transformé.
- **Bras B** : p_v, même forme, sur les conditionnelles de condition B ; la seconde d'une chaîne rapportée à part.
- **Sensibilités** (rapportées, ne décident pas) : unité carte (p̂ = cartes qui portent / emplacements, Clopper-Pearson) ;
  τ'_i = max(0,005 ; 0,25 · I_i).
- **Secondaires** : même forme par classe (forte hors K1, moyenne, faible, latente), bras A ; par proposeur (appels qui trouvent,
  jamais un classement, N-058) ; chaîne réelle : coût par fournisseur et par appel (relevé des relais, rapproché), jetons d'entrée
  et de sortie, **troncatures** (raison d'arrêt de la réponse brute = borne), sessions en échec, cartes rendues, refusées au
  gardien, non évaluables, durée de chaque appel.

## 6. Seuils

- **p_max = 0,051** (`seuil-pilote-v1.json`, `16cd1004…`) : plus petit p (pas 0,0005) où la règle de garde d'un banc de 24
  mondes tient avec probabilité ≤ 0,05, sous l'approximation écrite dans `seuil_pilote_v1.py` (survie (1 − p)^24, toute carte qui
  porte est captante ; 2 mondes sur 12 à chaîne ; moyennes restées par hasard ignorées). Contrôle : π(0,02) = 0,655 contre 8 sur
  12 observés en v4. Le programme de la mesure recalcule p_max et refuse s'il diffère.
- Niveau des intervalles : 95 % bilatéral. Aucun autre seuil.

## 7. Plan d'analyse

1. Vérifier les empreintes : texte scellé, mondes (registre), réponses brutes, témoins, fichier des cartes, programme de la mesure.
2. `python3 -I -B mesure_pilote_v1.py mesurer MONDES.json CARTES.json SORTIE.json`, une seule fois, sur la machine privée ;
   sortie scellée ; elle ne contient aucun coefficient des mondes.
3. Issue lue au champ `regle` de la sortie (section 8) ; sensibilités et secondaires recopiés sans lecture d'issue.
4. Rapprochement des coûts : relevés des relais contre réponses brutes ; écart rapporté.
5. Aucune exclusion autre que celles de la section 5 ; aucune analyse en sous-groupe ne décide.

## 8. Critères de lecture gelés (la première ligne qui s'applique donne l'issue)

| issue | condition | ce qui suit |
|---|---|---|
| **P-0** non concluant | aucun appel répondu en bras A | nœud de Lazar ; aucun banc sur cette mesure ; cause rapportée |
| **P-1** « MR-2 ne sert pas telle quelle » | borne basse de l'intervalle de p_c > 0,051 | nœud de Lazar : la famille MR-2 ne laisse rien après une génération 1 réelle ; options écrites alors (garder MR-1 et la réponse « garde et boucle », Q-13 (a) ; famille neuve sur texte neuf) ; **aucun banc MR-2 avec masquage** |
| **P-2** banc | sinon | banc de 24 mondes de calibration (code v68 gelé), modèle de proposeurs avec **P_CACHÉE := p_c ponctuel** et **P_VUE := p_v ponctuel** si le bras B est joué (0,25 sinon, dit) ; la règle de garde de la conception v4 y décide de la course ; autres probabilités du modèle : Q-P3 |

Une issue P-2 **ne dit pas** que les proposeurs « ne voient pas » les conditionnelles : elle dit que le pilote ne l'a pas réfuté
et donne le paramètre du banc.

## 9. Audit de symétrie (R4), écrit d'avance

- **p_c = 0 sur tous les appels** (trop propre pour l'hypothèse) : relire à la main 3 cartes par appel tirées au hasard (graine
  de la tâche) ; vérifier que l'attribution porte bien la condition quand une carte la contient (essai du programme) ; vérifier
  que les épisodes servis contiennent les traits ; rapporter.
- **p_c élevé** (trop propre contre l'hypothèse) : relire les cartes qui portent ; vérifier qu'aucune pièce servie ne décrit la
  famille ou une condition (fuite C7, gabarit) ; vérifier l'isolement (témoins) ; rapporter.
- Même audit pour p_v.

## 10. Liste d'arrêt

- Empreinte d'un monde, du texte, d'une pièce servie ou du programme de la mesure différente → arrêt avant tout appel.
- Réponse brute ou témoin d'isolement absent pour un appel → arrêt (code 3), pièces versées.
- Panne d'un relais → l'appel est « échec », aucune reprise, aucune bascule vers un autre fournisseur ; deux échecs du même
  fournisseur → arrêt du pilote, issue lue sur ce qui est répondu (P-0 si rien en bras A).
- Dépense d'un fournisseur atteignant sa part → arrêt ; aucune ligne d'extension.
- Un monde sans tirage conforme en 8 → arrêt avant tout appel, cause écrite ; nouvelle graine seulement sur texte neuf et mot de
  Lazar.
- Toute garde essayée sur un cas sain et un artefact avant le pilote (R5) ; l'essai du programme de la mesure est fait
  (`essai-mesure-pilote-v1.json`, `9ba95223…` : cas sain conforme ; quatre entrées malformées refusées ; carte à mémoire comptée
  non évaluable ; une pente sans condition sur le trait de la conditionnelle ne la porte pas, Δ/I = −0,696).

## 11. Code : ce qui manque pour faire tourner un monde MR-2 dans la chaîne réelle (dit, non écrit)

Lu dans le différentiel du code v67 (`organisme-v67-contre-7e415cb.patch`) et la configuration v8 ; l'arbre de l'organisme
(`lciric/ideation-organism`, commit `ab53b7f4`) **n'est pas dans cette session** : noms de fonctions à vérifier sur l'arbre.
Noms neufs (R12) ; v68 ou une branche « pilote » de la v68 ; rien d'antérieur modifié.

| # | où (v67) | ce qui manque | pourquoi |
|---|---|---|---|
| C-1 | `A.charger_monde(RACINE)` puis `L64.verifier_monde(monde, MONDE_SHA256)` : monde lu dans l'arbre, empreinte constante | `charger_monde_prive_v68(chemin, sha256_attendu)` : monde lu **hors de l'arbre**, chemin donné au lancement, empreinte comparée à celle du registre | les mondes du pilote sont privés et jamais publiés |
| C-2 | manifeste : `monde={source, sha256, loi_vraie}` | manifeste et relevé n'écrivent **que l'empreinte** du monde, jamais `loi_vraie` | la loi vraie au manifeste publierait le monde |
| C-3 | `B65.DIM` (2), instances à 2 traits et 2 sous-populations ; `episodes_de_developpement` | dimension 8 et 3 sous-populations lues dans le monde ; tranche de 400 épisodes tirée du monde MR-2 (K-1, K-3 de la conception v3) | monde MR-2 |
| C-4 | compilation du monde | porter `compiler_v4` (sorte `interaction_xor` développée en une principale et une interaction de seuil) et `verifier_v4` dans l'arbre ; vérifier que la loi compilée passe `selection_pari.valider_loi` et donne les mêmes probabilités que `proba` (écart ≤ 10⁻⁹ sur un jeu fixe) | le monde doit être évalué par la loi de la chaîne |
| C-5 | gardien (jeu factice fixe, D = 2) | jeu factice à la dimension du monde ; refus de la septième carte, compté (S-6) | lois à 8 traits |
| C-6 | gabarit du proposeur (bornes ±4, D = 2) | D = 8, 3 sous-populations, `si_sinon` et `par_sous_population` décrits ; **rien** sur les sortes d'effets (K-5) | ne pas souffler la structure |
| C-7 | `proposeurs` de la configuration v8 : Kimi et Argon seuls ; `commandes-v6` ; `plafonds_session.proposeur` unique (1,5 USD) | **commandes et relais pour Claude (Fable 5.2, Opus 5.5) et pour Astra** ; plafond de session **par modèle** (3, 2, 2, 2) ; délais par fournisseur (garde 24 de la v67) ; configuration v9 ; **voie d'accès aux crédits de Claude à confirmer** (relais local à clé tenue hors de l'orchestrateur, comme Kimi et Argon) | quatre proposeurs du pilote |
| C-8 | `ReleveDeJetons.instrumenter` (champs de Kimi et d'Argon) | champs d'usage de Claude (`input_tokens`, `output_tokens`) et d'Astra (à fixer, [CHAMPS-ASTRA]) ; raison d'arrêt de chaque réponse lue (troncature) | coûts et troncatures, mesures secondaires |
| C-9 | `plan["parts"] = {"kimi", "argon"}`, options `--plafond-kimi-usd`, `--plafond-argon-usd` ; `R.verifier_go_v66(…, part=PART_DU_GO)` | parts par fournisseur pour `claude`, `argon`, `astra` (et machine) ; lecteur du GO qui lit **deux** lignes (crédits, hors crédits) | lignes de GO du pilote |
| C-10 | réponses des proposeurs (réserve R-2 de la v67) | réponse brute et témoin d'isolement de chaque appel écrits et scellés avant l'extraction ; garde 26 ; absence = arrêt (K-10) | isolement versé |
| C-11 | `B.GENERATIONS` = 2 imposé (« le code v67 en joue 2 (D2) ») ; `jouer_boucle` enchaîne gardien, juge, étage des tests de mort | **lanceur du pilote** : une génération, proposeurs puis gardien, **sans juge ni étage** (Q-P2 (a)) ; deux bras et deux mondes, sessions séparées, aucune information d'un monde ou d'un bras servie à l'autre (K-11) ; aucun bac `bwrap` exigé | dessin du pilote |
| C-12 | héritage de départ (`B65.ecrire_heritage_depart`, une loi K1 tirée du jeu) | héritage de départ par monde et par bras : {K1} ; {K1 ; V-K1+B} (bras B), écrit par programme depuis le monde privé, empreinte au registre (garde 17) | bras B |
| C-13 | — | export des cartes au format de `mesure_pilote_v1.py` (`{"cartes": [...], "appels": [...]}` : monde, bras, proposeur, emplacement 1 à 6, état admise ou refusée, loi) et fichier `MONDES.json` privé (monde, devis, empreinte) | entrée du programme de la mesure |
| C-14 | lecture gelée v66 | lecture du pilote = sortie de `mesure_pilote_v1.py` (champ `regle`) plus le rapprochement des coûts ; heure et chemin hors du corps empreinté (R-7) | issue lue par programme |
| C-15 | — | générateur MR-2 dans l'arbre avec le compteur de tirage et la graine de la section 3.1 ; écriture des mondes par `ecrire_prive` dans un dossier de la liste blanche | secret du pilote |

Chaque garde neuve essayée sur un cas sain et un artefact (R5) ; essai à blanc avec proposeurs factices et les vraies pièces
servies ; contre-lecture du code par un autre modèle que son développeur (N-052). C-1 à C-6, C-8 à C-10 et C-15 servent aussi
la course (préalable 16.1 point 2 du brouillon 3) : le pilote les éprouve avant elle.

## 12. Préalables

**Avant le scellement** : décisions Q-P1 à Q-P4 ; code de la section 11 écrit, essayé, contre-lu, gelé, empreintes en bloc
gelé de ce texte ; identifiant et prix d'Astra confirmés ; contre-lecture R2 (section 17) ; marqueurs levés (section 18).
**Avant le premier appel** : ligne de GO inscrite ; secret du pilote engagé et poussé, puis phrase de Lazar ; mondes vérifiés,
empreintes au registre ; essai à blanc réussi ; relais lancés avec leur part comme plafond ; dossier des sessions prêt ;
rapatriement essayé sur l'essai à blanc.

## 13. Devis (`devis_pilote_v1.py`, `99d5d677…` ; sortie `dcae0286…` ; tout **estimé** sauf les plafonds)

Pire = plafonds de session ; attendu = coûts centraux d'un appel du devis v2 (Fable 1,60 ; Opus 0,80 ; Argon 0,25 ; Astra 1,00 USD).
Aucun expérimentateur, aucun vérificateur, aucun test de mort.

| poste (USD) | bras A seul : attendu / pire | **bras A et B** (recommandé) : attendu / pire |
|---|---|---|
| **crédits de Claude** : Fable 5.2 et Opus 5.5 | 4,80 / 10,00 (4 appels) | **9,60 / 20,00** (8 appels) |
| Argon | 0,50 / 4,00 (2 appels) | 1,00 / 8,00 (4 appels) |
| Astra | 2,00 / 4,00 (2 appels) | 4,00 / 8,00 (4 appels) |
| machine (petite machine ou poste local ; plafond) | 0,30 / 3,00 | 0,30 / 3,00 |
| **hors crédits** (Argon, Astra, machine) | 2,80 / 11,00 | **5,30 / 19,00** |
| **total** | 7,60 / 21,00 | 14,90 / 39,00 |

Sous Q-P2 (c) (tests de mort des cartes promues), ajouter au pire 1,60 USD par test (Opus 1,50 sur crédits, Argon 0,10), jusqu'à
24 tests par monde et par bras : non retenu.

## 14. Lignes de GO proposées, mot pour mot, **non inscrites** (bras A et B ; numéro donné à l'inscription)

```
| GO-AAAA-MM-JJ-NN (π1) | AAAA-MM-JJ | calcul | **Pilote d'une génération de l'organisme sur la famille MR-2, part sur crédits de Claude** : proposeurs Fable 5.2 (plafond de session 3 USD) et Opus 5.5 (2 USD), un appel par proposeur, par monde et par bras, au plus 6 cartes, aucune reprise ; 2 mondes du secret du pilote (engagé et poussé avant la phrase de Lazar), jamais publiés ni réutilisés ; bras A (archive {K1}) et bras B (archive {K1 ; K1 + condition}) ; gardien mécanique seul, aucun juge, aucun test de mort ; conditions toutes exigées : préenregistrement du pilote contre-lu par un lecteur neuf et scellé ; code du pilote (section 11) contre-lu et gelé ; essai à blanc réussi avec les vraies pièces servies ; mondes vérifiés et leurs empreintes inscrites ; réponses brutes et témoins d'isolement versés pour chaque appel ; mesure par `mesure_pilote_v1.py` (`0d806aca…`) une seule fois ; jamais de ligne d'extension ; arrêt par identifiant (R10), dépenses et arrêts consignés | 20 USD (sur crédits) | 2026-11-30 | Lazar | R-2501 ; mot de Lazar à recopier |
| GO-AAAA-MM-JJ-NN (π2) | AAAA-MM-JJ | calcul | **Même pilote, part hors crédits** : Argon proposeur (2 USD par session) 8 USD, Astra proposeur (2 USD par session) 8 USD (identifiant et prix confirmés avant l'appel), machine 3 USD ; plafond de chaque relais égal à sa part ; mêmes conditions que la ligne π1 ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 19 USD | 2026-11-30 | Lazar | R-2501 ; mot de Lazar à recopier |
```

Sous Q-P1 (a) (bras A seul) : mêmes textes sans « et bras B (archive {K1 ; K1 + condition}) », **π1 10 USD**, **π2 11 USD**
(Argon 4, Astra 4, machine 3).

## 15. Décisions de Lazar à trancher avant le scellement

**Q-P1 — Jouer le bras B (condition connue).** Enjeu : sans lui, le banc garde 0,25 pour une conditionnelle dont la condition est
connue, valeur aussi arbitraire que 0,02. (a) Bras A seul : 10 + 11 USD au pire ; P_VUE reste 0,25. (b) **Bras A et B** : 20 + 19
USD au pire ; p_v mesuré remplace 0,25 ; à 8 appels, il ne pourra pas établir qu'une conditionnelle est introuvable (borne haute
pour 0 appel sur 8 ≈ 0,074 par carte) mais donne la valeur du banc. Recommandation : **(b)**, confiance 0,55. Défaut sous 48 heures : (b).

**Q-P2 — Périmètre de la chaîne réelle.** (a) **Proposeurs et gardien seuls** : la mesure n'a besoin que des cartes ; code plus
court (C-11) ; l'étage reste éprouvé par l'essai à blanc de la course. (b) Plus le juge mécanique (processeur seul) : promotions
rapportées, aucune revendication ; demande le juge v68 (K-1, K-2, K-8) avant le pilote. (c) Plus les tests de mort des cartes
promues : chaîne entière éprouvée ; jusqu'à 1,60 USD par test, expérimentateur Opus. Recommandation : **(a)**, confiance 0,6.

**Q-P3 — Ce que le banc reprend du pilote.** (a) **p_c et p_v seuls** (lettre de R-2501) ; les probabilités par classe sont
rapportées. (b) Toutes les probabilités du modèle remplacées par les mesures du pilote (forte, moyenne, faible, latente) :
modèle du banc entièrement mesuré, mais sur 8 appels, et sur les seules composantes de deux mondes. Recommandation : **(a)**,
confiance 0,5 ; (b) rapportée comme variante du banc, sans décider.

**Q-P4 — Où tourne le pilote.** (a) **La machine jetable de la course** (prix horaire consigné, détruite après) : le pilote y
éprouve la chaîne de la course. (b) Le poste local de Lazar (comme la v67) : pas de machine à payer ; mondes privés sur son poste.
Recommandation : **(a)**, confiance 0,5.

**Échéance.** Pilote (code, texte, contre-lecture, appels), puis banc de 24 mondes, puis course avant le 30 novembre : serré ;
le pilote et le banc ne demandent que le sous-ensemble C-1 à C-15 du code v68, que la course exige aussi.

## 16. Portée

Une génération, deux mondes, quatre proposeurs, un appel chacun par bras : une **mesure** du comportement de ces proposeurs
sur cette famille, avec ces pièces servies. Rien sur le progrès, rien sur la qualité des idées, rien sur d'autres familles ;
aucune décision de composition (N-058).

## 17. Contre-lecture (R2)

À faire par un sous-agent neuf d'une autre lignée (Claude Fable 5.2 recommandé), qui n'a écrit ni ce texte ni la conception v4 ;
fichiers à lui donner : ce brouillon ; `conception-monde-riche-doublons-v4.md` ; `outils-v4/monde_riche_v4.py` ;
`pilote-v1/outils/seuil_pilote_v1.py`, `mesure_pilote_v1.py`, `devis_pilote_v1.py` et leurs sorties ; la note de décision ;
le différentiel du code v67. Points à éprouver en priorité : définition de « porte » (τ = 0,75 · I) pour des cartes réelles ;
unité appel et transformation en p par carte ; approximation de `seuil_pilote_v1.py` ; fuite par le bras B (la loi V-K1+B
désigne-t-elle trop la condition ?).

## 18. Marqueurs restants (aucun ne doit rester au scellement)

[CHAMPS-ASTRA] (C-8) ; identifiant et prix d'Astra ; voie d'accès aux crédits de Claude pour les proposeurs (C-7) ; empreintes
du code du pilote (bloc gelé, à créer) ; décisions Q-P1 à Q-P4.

Fin de la rédaction : 2026-11-13 09:36:22 UTC (`date -u`).
