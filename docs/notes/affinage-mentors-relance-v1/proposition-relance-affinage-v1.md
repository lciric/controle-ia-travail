# Proposition — relance du chantier d'affinage des idées des mentors par l'organisme d'idéation — v1

- **Nature** : pièce de travail (classe C) pour la mère ; aucune décision prise ici. Écrite le 2026-11-21T16:02:47Z (`date -u`) par un agent Opus 5.5 de la mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`), en lecture seule ; aucun appel payant, aucun commit.
- **Mandat** : GO-2026-11-21-62 (relance) et « affinage des hypothèses des mentors : go » dans GO-2026-11-21-63 ; erratum 1 du brief de la mère (`registres/passations/2026-11-21-1450-brief-lancement-mere-autre-compte-erratum-1.md`), point 3.
- **Lu** : N-072 (`docs/decisions/decision-matiere-premiere-mentors-v1.md`) et sa contre-lecture ; GO-2026-11-18-14, -15, -41, GO-2026-11-19-27, -28, GO-2026-11-21-19, -41, -47, -62, -63 ; registre des décisions R-3339 à R-4576 (lignes « affinage », plus R-3688, R-3701, R-3800 sur l'auto-conception v9) ; passation `registres/passations/2026-11-21-1535-compte-organisme.md` et état v3 pour la mère (`origin/lot/compte-organisme-v1`, 53c8e38b) ; en-tête de l'additif « matière première » v2 (664d6763a) ; devis v10 et commandes exactes v10 (`origin/prep/affinage-v10-compte-organisme-v1`, 6b704ede).
- **Non ouverts** (cloisonnement) : tout `archives-reponses-modeles/`, toute branche `quarantaine/…` ou `matiere-premiere/…`, l'annexe des objets de contrôle, le registre servi des visées, les pièces D2 et D3 de la mère sur la matière première (noms seulement), le relevé d'ensemble des mentors (au-delà de ce qu'en citent N-072 et sa contre-lecture).

## 1. Où en était la course d'affinage quand elle a été gelée

**Elle n'a jamais été jouée.** Aucune dépense de course sous GO-2026-11-18-14 (150 USD, échéance **2026-11-25**) ; la réservation de la clé Minuit a été levée pour l'auto-conception (R-3616).

| étape | état | où |
|---|---|---|
| v1 à v6 | écrites, essais à blanc (sans appel payant), contre-lues | `prep/affinage-v*-compte-organisme-v1` et `lot/compte-organisme-v1` |
| **v7** (commandes exactes `e508db13…`, lanceur `4439a614…`, préenregistrement `720cbe81…`, contre-lecture Fable 5.1 « Scellable. ») | remise à la mère le 18 vers 17:17Z (R-3339) ; préalables posés dans l'ancien conteneur de la mère (copie de l'orchestrateur à `a41b7b50`, `bwrap`, `socat`, R-3350) ; **non jouée** : échec certain, Carbon en mode lot ne tient pas la provision de pensée (diagnostic `510312b1…`, R-3446) | `prep/affinage-v7-compte-organisme-v1` (2c31fc6f) |
| v8 | abandonnée avant contre-lecture (troncature certaine, R-3479) | `prep/affinage-v8-…` (dd139d7e) |
| v9 | contre-lue « Scellable après corrections » | `prep/affinage-v9-…` (74676380) |
| **v10** (commandes `ecf3eb7d…`, lanceur `b0829025…`, préenregistrement `7fc71712…` scellé, contre-lecture `c4a809bc…` « Scellable. », devis `e007a137…` : 45,25 USD estimés, haut 141,59, plafond 150) | prête le 18 à 23:41Z (R-3533) ; **non jouée** : Carbon toujours appelé par lot, même défaut que l'auto-conception close sans mesure à 01:52Z (R-3584) ; « v11 suivra » (R-3610) | `prep/affinage-v10-…` (6b704ede), **hors** `lot/compte-organisme-v1` et `main` |
| v11 | **jamais écrite** ; gel le 19 vers 09:48Z (GO-2026-11-19-27) | — |

**Fait qui change la donne** : l'auto-conception v9, sur le même orchestrateur `a41b7b50`, avec **Carbon par la commande synchrone**, est close en code 0 (94 cartes, 72,50 USD, Carbon ≈ 2,25 USD par appel, 3 réponses 502 sur 22 sans arrêt ; R-3800). Le correctif existe ; il reste à le porter dans l'affinage.

**Ce que la v10 ne peut plus être jouée telle quelle** : (1) Carbon par lot ; (2) règle de GO-2026-11-21-47 (au moins 16 000 jetons de texte au-delà de la réflexion) : la v10 demande 32 768 jetons au plus, réflexion comprise, avec 28 672 de provision, soit au plus ≈ 4 096 de texte ; (3) plafond par appel des proposeurs 3,00 USD, sous le coût observé d'un appel synchrone de Carbon (2,25 en moyenne, 6 au plafond de l'auto-conception) ; (4) clé Minuit engagée depuis dans la course « nouvelles attaques » (§ 5) ; (5) contre-lecture par Fable 5.1, alors que la règle est aujourd'hui Fable 5.2 conçoit, Opus 5.5 contre-lit.

**Sorties gardées** : aucune sortie de course (rien n'a couru). Restent les pièces v1 à v10 sur leurs branches, leurs essais à blanc simulés, les contre-lectures, les devis v1 à v10, les lanceurs `scripts/lancer_course_affinage_mentors_v1.py` à `_v10.py`. La copie de l'orchestrateur de l'ancien conteneur de la mère est perdue (absente ici : `/home/user/ideation-organism` n'existe pas) ; sans dommage, le commit est public et épinglé. Préalable de N-072 § 2 sur les montants absents (≈ 41,82 USD) : inscrits (R-3201, `registres/depenses.md` l. 491-496).

## 2. Formes de relance

**(a) Session fille dédiée** (conception Fable 5.2, contre-lecture Opus 5.5, exécution dans son propre conteneur).
- Avantage : conteneur à elle (ports 8787 à 8793 libres, aucune collision avec « nouvelles attaques ») ; jamais exposée à l'additif « matière première », aux objets de contrôle, ni aux branches de quarantaine ; ne charge pas la session de l'organisme.
- Inconvénient : refaire les préalables (copie de l'orchestrateur, `bwrap`, `socat`) ; elle n'a pas l'histoire v1 à v10 (risque de refaire une erreur déjà corrigée : mandat avec chemins en entier) ; un chantier de plus au-delà de la règle des trois (GO-2026-11-19-27, déjà dépassée par la veille dégelée).

**(b) Rattachement à la session de l'organisme** (`session_01Qi7Gr4gcZHeTzfEWt2Es9T`).
- Avantage : lignée qui a écrit v1 à v10 et porté Carbon synchrone dans l'auto-conception v9 ; outillage, relais et gardes connus.
- Inconvénient : file déjà pleine (cinq points restants à la passation de 15:35Z, plus « nouvelles attaques » imminente) ; mêmes ports et mêmes clés que « nouvelles attaques », donc jamais en même temps ; session exposée à l'annexe des objets de contrôle et à la matière de « nouvelles attaques » ; machine redémarrée trois fois le 21, relais tués.

**(c) Hybride** : la session fille écrit la v11 et la fait contre-lire ; l'exécution est confiée à la session de l'organisme après la clôture de « nouvelles attaques ».
- Avantage : conception propre et exécution sur un outillage rodé.
- Inconvénient : double passation, et l'exposition de (b) au moment de l'exécution.

**Recommandation : (a)**, préparation tout de suite sans dépense, course après la clôture de « nouvelles attaques » ou sur une clé qu'elle n'emploie pas. **Confiance 0,6.** Défaut sous 48 heures : (a).

## 3. Devis (course v11, composition inchangée : deux Claude, Argon, Astra, Carbon ; 80 appels de proposeurs, 16 fils)

| poste | chiffre | chemin |
|---|---|---|
| préparation (v11, contre-lecture, essai à blanc) | 0 USD | travail de session, sans appel payant |
| proposeurs hors Carbon | 16,72 | devis v10 § 3 (24,70) moins Carbon 16 × 0,4985 (§ 2), `e007a137…` |
| Carbon synchrone | 36,00 = 16 × 2,25 | R-3800 (coût observé, auto-conception v9) |
| aiguilleur ; juges | 4,96 ; 11,47 | devis v10 § 3 |
| **borne basse (estimation)** | **76,07** = 69,15 × 1,10 | marge de 10 % du devis v10 |
| **estimation haute réaliste** | **93,43** = 76,07 × 72,50 / 59,03 | dépassement observé de l'auto-conception v9 : réel 72,50 (R-3800) contre estimation 59,03 (devis v2i, R-3688) |
| haut par formule | 201,93 = (35,21 + 16 × 6,00 + 21,12 + 31,24) × 1,10 | 35,21 = 59,21 − 16 × 1,50 (devis v10 § 3) ; 6,00 USD par appel de Carbon (R-3610, R-3641) ; **au-dessus du plafond : non atteignable** |
| **borne haute (pire cas)** | **150 USD** de course, plafond d'arrêt | GO-2026-11-18-14 ; mécanisme du plafond dur, devis v10 § 3 bis |
| sondes du jour | Carbon ≤ 6 (1,36 observé, R-3701) ; Astra ≤ 0,05 (R-3273) | hors plafond de la course |
| **total au pire** | **156,05 USD** | 150 + 6 + 0,05 |

Réserve : au haut par formule, la proposition dépasse 100 USD et les juges ne sont pas lancés (nœud « non mesuré (budget) », devis v10 § 3 bis) ; au coût observé (proposition ≈ 58 USD avec marge), rien n'est coupé. Prix Claude à relever le jour du départ.

**Dépense dans une ligne ouverte** : GO-2026-11-18-14 (150 USD) couvre la course si Lazar **prolonge son échéance** (2026-11-25) et **nomme la clé**. La sonde de Carbon n'a pas de ligne pour l'affinage : ligne neuve (≤ 6 USD) sur ce devis, au mot de Lazar.

## 4. Ce qu'il faut attacher

- **Rien par l'outil d'attache.** `lciric/ideation-organism` est public, lisible sans attache (fait relevé à R-3349) : copie en lecture seule dans le conteneur qui exécute, **commit `a41b7b50`** (celui de la v10 et de l'auto-conception v9 réussie). GO-2026-11-18-41 n'autorise que la session mère et finit le **2026-11-22** : un mot de Lazar l'étend à la session qui exécute.
- `bwrap` et `socat` à installer (sans dépense) ; clés présentes par leur nom dans l'environnement (jamais leur valeur).
- Pièces : `origin/prep/affinage-v10-compte-organisme-v1` (6b704ede) ; commande synchrone de Carbon et pièces de l'auto-conception v9 sur `origin/lot/compte-organisme-v1` (versées en 8029ae7f et ce80b32d, R-3800 ; les cartes de cette course ne sont pas à ouvrir).

## 5. Risques de cloisonnement

1. **Trois « matières premières » homonymes.** N-072 vise les 93 idées des mentors. L'additif « matière première » (664d6763a, vérification « À corriger » 51e02c764) vise une autre matière, sur une autre course : les visées mathématiques des consultations externes (registre servi `3bcb94e6…`, branche `matiere-premiere/visees-mathematiques-v1`, R-4419), et les modes concrets de la quarantaine y sont aussi versés (GO-2026-11-21-19). GO-2026-11-21-62 les cite ensemble ; **seules les idées des mentors entrent dans l'affinage**. Les décisions D1 et D4 de GO-2026-11-21-63 portent sur l'additif, pas sur l'affinage. L'additif, son annexe des objets de contrôle et les deux autres matières ne sont ni servis ni lus par la session d'affinage.
2. **Sens inverse.** Les cartes de l'affinage (certaines idées des mentors touchent attaques et moniteurs) ne doivent pas entrer dans « nouvelles attaques » (partie servie gelée à l'octet, additif v2 § 1) ni être lues par une session qui conçoit moniteurs, sondes ou le mode tenu à l'écart (N-054, GO-2026-11-20-59). Elles sont versées sur une branche de données à elles, hors de `main`, avec une liste des lecteurs.
3. **Clés partagées.** Chaque clé Claude est plafonnée à son solde pour « nouvelles attaques » (GO-2026-11-20-16 : juge sur Minuit, aiguilleur et espèce 4 sur Luc, espèce 3 sur Rigaud, GO-2026-11-20-22) ; Google (Argon et Carbon) et OpenAI (Astra) sont communes. Une dépense de l'affinage avant la clôture de « nouvelles attaques » (échéance 27 novembre, GO-2026-11-21-30) mange sa part et peut déclencher son arrêt nommé. **Nœud pour Lazar** : attendre la clôture, ou une clé neuve ou rechargée réservée à l'affinage.
4. **Ports** 8787 à 8793 : jamais deux courses dans le même conteneur (forme (b) ou (c)).
5. **Réserves du relevé** : 20 entrées retirées tant qu'aucune réserve n'est levée par écrit, CW15 servie (commandes v10 § 0, point 4) ; à reprendre dans la v11 sans changement, sauf décision écrite de la mère.

## 6. Première action concrète

Au mot de Lazar sur la forme (défaut (a)), la mère ouvre la session fille (Fable 5.2) sur un mandat qui donne chaque chemin en entier. Sa première tâche, sans appel payant : le différentiel v10 → v11 (Carbon par la commande synchrone de l'auto-conception v9 ; sortie de Carbon conforme à GO-2026-11-21-47 ; plafond par appel de Carbon à 6 USD ; clé, échéance et lieu des cartes laissés en valeurs ouvertes pour Lazar), puis le devis v11 et la contre-lecture par Opus 5.5. Les trois nœuds vont à Lazar en même temps : forme, clé et calendrier, prolongation de GO-2026-11-18-14 et de GO-2026-11-18-41 avec une ligne de sonde de Carbon.
