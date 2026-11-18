# Addendum — témoins du juge (v3) et budget de pensée de Carbon — organisme d'idéation sur les organismes discrets — v1

Écrit le 18 novembre 2026 par la session de relance (`session_01XJ6MgpChR1JWSMBxSQcf3c`, modèle Opus 5.5), sur l'ordre de la
session mère (07:04Z) et la condition de Lazar inscrite dans GO-2026-11-18-17, verbatim : « je recommande d'attendre que les
témoins du juge soient corrigés, sinon la course sera illisible. go ». Même condition pour la troisième course Carbon (R-3225).
**Aucune course ne part avant que cet addendum soit contre-lu par un agent neuf (Opus ou Sonnet, pas Fable), scellé, signalé à
la mère puis à Lazar.** C'est un écart au dispositif scellé des courses (devis v4 `005c02eb…`, lanceurs v8, v9 `63a54d04…`,
v10 `c3abd573…`, qui épinglent les témoins v1) ; il ne touche ni la question v3, ni les faits v3, ni le préenregistrement T0.7.

## 1. Pourquoi

Diagnostic : `diagnostic-temoins-v2.md` (`31d68ed2…`). Contre-lecture : `contre-lecture-diagnostic-temoins-v1.md`
(`830f71c7…`, agent neuf sur Opus 5.5) — « tient avec réserves ; la correction proposée ne tient pas en l'état ». Ce qui tient
après la contre-lecture :
- le juge Opus a porté (1, 1) en avantage et originalité le vrai témoin et son jumeau dans les deux courses, avec les mêmes
  raisons (copiable à bas coût ; technique courante) ; il a tenu les deux faux (0, 0) ; il porte éligibles 2 fiches de
  proposeurs sur 12 (Astra) et 5 sur 10 (Argon) ;
- la paire v1 se décrivait elle-même comme facile à construire et de niveau « transposition » ;
- la question v3 nomme son idée (« discordance locale texte/champ ») et des proposeurs l'ont écrite (doublons).

**Corrections du diagnostic** (constats de la contre-lecture, retenus) : (a) la grille ne définit que les notes 0 et 3, et la
porte à 2 n'est pas servie au juge ; « le juge applique la lettre » et « un juge qui le porterait éligible appliquerait la
grille moins bien » sont trop forts : le vrai témoin v1 tombait dans une zone non définie (1 ou 2 se défendent) ; (b) le
juge ne cite jamais la question dans ses raisons : le recouvrement avec la question explique les doublons, c'est une cause
aggravante ; (c) la fourchette de longueur des fiches est 3 353 à 4 808 caractères pour Astra, 2 677 à 5 404 pour Argon ;
(d) le jumeau a reçu 2 puis 3 en traitabilité (« mêmes notes » était inexact) ; (e) la preuve par le commit `9b5d3438` est
vide (commit racine d'un clone superficiel) ; meilleure preuve de version : le vrai témoin cite 128, 0,15 et la dose 3/4,
qui ne figurent que dans les pièces v3 ; (f) Argon T05 est le jumeau, pas une fiche de proposeur ; à Astra, le faux
d'antériorité est en doublon d'une fiche de proposeur (T12–T13).

## 2. Témoins v3

`temoins-organisme-discrets-v3.json` (`611c50a2…`, scellé). Écrits à la lettre de la grille, **sans être essayés devant le
juge**. Généré par `ecrire_temoins_v2.py` (scellé) puis assemblé ; la v2 (`5e8a276e…`) reste archivée.
- **Paire vrai et jumeau neuve** : « Restauration par dérangement inverse : certificat programme que la permutation est la
  seule différence avec le jumeau » et son jumeau « Défaire la permutation avec sa propre graine… ». Idée absente de la
  question v3 et des faits v3 (aucun de « restaur », « octet », « isolement », « certificat », « manipulation », « fuite »
  n'y figure ; « graine » et « dérangement » n'y paraissent que pour décrire le mécanisme). Elle répond aux sous-questions
  1 et 2. Avantage revendiqué : la graine scellée du dérangement, le jumeau apparié et la référence cachée, qu'aucun calcul
  ne remplace ; originalité déclarée « inédite », avec une recherche d'antériorité écrite (contrôles de manipulation, tests
  de permutation : ni l'un ni l'autre n'inverse une intervention scellée). Vise 2 au moins en originalité (contre-lecture,
  constat 12). Longueurs servies : 4 549 et 3 870 caractères, dans les deux fourchettes.
- **Faux** : ceux de la v1, **repris à l'identique** (contre-lecture, constat 8 : ils ont été tenus deux fois ; les réécrire
  rouvrirait un risque). Leur longueur reste hors fourchette (2 407 et 2 606) : rapportée par l'orchestrateur, sans effet sur
  la lisibilité ; dit ici comme défaut de validité connu.
- Validés hors ligne par les fonctions de l'orchestrateur épinglé (`valider_fiche_ideation`, garde du niveau méthode : rien).

Ce qui n'est pas retenu : changer la question (la question v3 est une pièce commune aux courses déjà jouées ; la changer
casserait la comparaison entre lignées et ne corrigerait pas l'avantage du vrai témoin v1) ; changer de juge (le défaut est
dans le témoin, sans preuve contraire) ; baisser la porte (code épinglé, hors de ce dépôt).

## 3. Épreuve des témoins seuls, puis règle d'arrêt écrite d'avance

**Forme retenue** (contre-lecture, constats 1, 4, 5 et 7 : le mode « juges seulement » ne peut pas servir) : option A, un
script de ce dépôt qui importe le code épinglé sans le modifier — `scripts/epreuve_temoins_seuls_v1.py` (`0b50b579…`,
scellé). Il bâtit la consigne du juge avec `anonymiser` et `consigne_juge` sur les quatre témoins v3, la question v3 et les
faits v3 comme pièce du juge, avec la graine des courses ; **gabarit vérifié identique à celui des deux courses** jusqu'au
titre « ## Les fiches » (égalité seulement, rien affiché) ; un seul appel `POST /v1/messages` au relais Claude (Opus 5.5,
clé `RR_ANTHROPIC_API_KEY_RIGAUD`), lecture par `valider_notes` et `lecture_temoins` (règle gelée de l'orchestrateur).
Éprouvé à sec et contre un faux relais : code 0 si les quatre témoins sont tenus, 4 sinon, refus si le dossier existe.
**Écart déclaré** : appel direct de l'interface de messages (pas une session de l'adaptateur de l'orchestrateur) ; quatre
fiches au lieu de 14 à 16 ; sans doublon possible avec un proposeur. L'épreuve est **nécessaire, pas suffisante**.

**Coût** : un appel du juge Opus sur une consigne de 24 561 caractères ; ≈ 0,1 à 0,2 USD (relevés : 0,474 USD pour 16 fiches,
0,417 pour 14) ; **plafond 0,5 USD**. **Un seul tirage**, joué une fois.

**Règle d'arrêt, écrite avant l'épreuve** :
1. Si l'épreuve rend 4 (un témoin v3 manqué), **aucune course** Kimi ni Carbon ; aucune retouche des témoins sans addendum
   neuf, contre-lu et scellé ; compte rendu à la mère puis à Lazar.
2. Si l'épreuve rend 3 (appel ou lecture en échec), elle n'est pas faite ; elle ne se rejoue que sur un mot de la mère.
3. Si elle rend 0, la course Kimi part (lanceur v11 ci-dessous, après sa contre-lecture), signalée avant départ ; **la
   course elle-même est l'épreuve suffisante** : si un témoin v3 y est manqué, la course est illisible, la lignée suivante
   ne part pas, et la règle 1 s'applique.
4. Les notes du juge sur les témoins ne sont lues qu'après l'épreuve ; aucune fiche de proposeur n'est ouverte.

## 4. Budget de pensée de Carbon

Épreuves du 18 novembre (journal de la relance, OD-020 ; `epreuve-lot-carbon-v1/`, scellé) :

| mode | budget de pensée | réponse | durée | coût |
|---|---|---|---|---|
| synchrone, sans flux | 8 192 | aucune ; coupure à 300 s (deux fois, course) | > 300 s | 1,53 USD comptés au pire cas |
| synchrone, en flux | 8 192 | aucun morceau en 240 s | > 240 s | 0,60 USD comptés au pire cas |
| synchrone, sans flux | 1 024 | juste | 4,5 s | 0,0016 USD |
| synchrone, en flux | 1 024 | juste | 46 s | 0,0016 USD |
| **par lot** | **8 192** | **juste**, 844 jetons de pensée, modèle servi `gemini-4-carbon` | **430 s** | ≈ 0,005 USD (moitié prix) |

Options pour la troisième course Carbon :
- **(A) mode par lot, budget 8 192** : courses jumelles d'Argon. Coût : une commande neuve (soumettre, relever l'état,
  lire), un relais Gemini neuf qui admette les chemins du lot, essais, contre-lecture ; délai d'un lot incertain pour une
  consigne de course (« cible 24 heures », 430 s ici pour une question triviale), à borner par le délai de la commande
  (3 300 s, comme Kimi), une course restant possible en échec par délai.
- **(B) synchrone, budget 2 048** : prête et scellée (enveloppe Carbon v2 `08531295…`, lanceur v10) ; écart déclaré : Argon a
  pensé avec 8 192.

**Recommandation** : (B) pour la course de cette ligne, (A) écrit ensuite si Lazar veut des courses jumelles ; confiance
moyenne. Défaut sous 48 heures : (B). Décision de Lazar par la mère.

## 5. Lanceurs à écrire après la contre-lecture de cet addendum

- **v11 (Kimi)** : le v9 (`63a54d04…`) avec les témoins v3 épinglés à la place des témoins v1 ; rien d'autre.
- **v12 (Carbon)** : le v10 (`c3abd573…`) avec les témoins v3 ; option (B), ou l'enveloppe du mode par lot si (A).
Chacun contre-lu par un agent neuf (Opus ou Sonnet), scellé, épreuve à sec réussie, avant sa ligne de GO (la mère inscrit
les lignes de forme avec l'empreinte de cet addendum).

## 6. Ordre

(1) contre-lecture de cet addendum ; (2) scellement ; (3) signal à la mère, puis à Lazar ; (4) épreuve des témoins seuls
(≤ 0,5 USD, signalée avant) ; (5) lanceurs v11 et v12, contre-lus, scellés ; (6) Kimi puis Carbon, une course à la fois,
chaque départ signalé.
