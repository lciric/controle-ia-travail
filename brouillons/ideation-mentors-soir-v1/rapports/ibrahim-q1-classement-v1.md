# Classement D — question 1 de Lujain Ibrahim — v1

Classeur neuf de l'étape D, 3 novembre 2026, de 14:42 à 14:57 (temps universel, `date -u`). Je n'ai écrit aucune idée et je ne sais pas d'où elles viennent. Je n'ai fait aucune recherche et appelé aucun modèle.

**Réserve de tête : aucun témoin déguisé pour ce mentor. L'originalité n'est donc pas contrôlée** (protocole des mentors du soir, section 2).

## Verdict

Ordre final des huit : **IB-03, IB-01, IB-04, IB-10, IB-14, IB-09, IB-07, IB-08**.
Cohérence : 28 paires sur 28, soit 1,0. Ce chiffre trop parfait vient d'un juge unique qui se souvient de ses jugements : réserve (voir plus bas).
Drapeaux de risque devant la mentor : oui pour IB-03, IB-01, IB-09 et IB-08 ; non pour IB-04, IB-10, IB-14 et IB-07, avec une précaution de formulation pour chacun.

## Entrées (empreintes vérifiées avant lecture)

| Fichier | sha256 |
|---|---|
| consigne `…/prompts-sous-agents/soir-classeur-D-ibrahim-q1-v1.md` | `659d69bdbe9847cbccfa283991c018d3da7b5df60f28c39fc72bdd699034d374` (conforme) |
| fiches `…/ibrahim-q1/prep-v1/fiches-servies-v1.json` | `46efe88c21e33f6f99461f1c2d9343d4fcc3b635b938e668a317edd715f3f462` (conforme) |
| moisson `…/ibrahim-q1/moisson-C/moisson-fusionnee-v1.json` | `b58a10590a1cdf8a2a469bc265284603f64eb0d1ef2ab928680c3f709820525d` (conforme) |
| protocole des mentors du soir, étape D | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` (conforme) |
| protocole Heimersheim v1, ancres (section 5) | `942b93241b6e033e34cc7cb035fe1d70f6e944a8a98bc4c556b83b0d7fdbad18` (relevée ; aucune empreinte attendue) |
| pièce Ibrahim v1, section 1 | `4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149` (relevée ; aucune empreinte attendue) |

## 1. Porte

Est dans le sujet une fiche qui décrit ou conditionne la première expérience du projet visé par la pièce : la persistance, après un apprentissage par renforcement, d'une persona installée par entraînement de caractère, et son effet sur la sycophancie. La pièce ne décrit pas le second projet de la mentor. J'ai donc jugé la porte sur cette seule direction.

- **Dans le sujet (10)** : IB-01, IB-02, IB-03, IB-04, IB-06, IB-07, IB-08, IB-09, IB-10, IB-14.
- **Hors sujet (4), en annexe et non classées** : IB-05, IB-11, IB-12 et IB-13. Ce sont des ré-analyses des campagnes de Lazar sur le modèle de base : pas de persona, pas de renforcement, pas d'instrument du projet. Ces quatre fiches viennent de la moisson du matin. Raisons détaillées dans `notes-v1.json`.
- **La porte pèse lourd.** Recalcul du script : si ces quatre fiches entraient, IB-05, IB-11 et IB-13 prendraient trois des huit places. IB-07, IB-09 et IB-14 en sortiraient. Quatre ex aequo (IB-04, IB-08, IB-10, IB-12) se disputeraient les trois dernières places.
- **Erratum à `notes-v1.json`** (fichier non réécrit, règle R12) : sa phrase de sensibilité dit « égalité résiduelle à quatre […] pour deux places ». La bonne valeur est **trois places**. Le recalcul de `bradley_terry_ibrahim_q1_v1-sortie.json` fait foi.

## 2. Notes (raisons en une ligne : `notes-v1.json`)

Ancres de Heimersheim, section 5. Pour « testable en jours », je prends le coût déclaré par la fiche. Quand une fiche renvoie à « l'entraînement commun », je compte 15 à 30 jours, la durée déclarée par IB-02 et IB-14.

| Fiche | Originalité vérifiée | Testable en jours | Prolonge un outil de la mentor | Somme |
|---|---|---|---|---|
| IB-03 | 2 (voisin lointain) | 2 | 3 (taxonomie : factuel contre social) | **7** |
| IB-01 | 2 (voisin lointain) | 1 (environ un mois) | 3 (distinction d'ELEPHANT, plusieurs tours) | **6** |
| IB-04 | 1 | 2 (paires post-renforcement : une course d'abord) | 3 (validation des juges, validité de construit) | **6** |
| IB-08 | 1 | 3 | 2 | **6** |
| IB-10 | 1 | 3 | 2 (son erreur sous fausse croyance) | **6** |
| IB-07 | 1 | 1 (reportée par sa source) | 3 | **5** |
| IB-09 | 1 | 2 | 2 | **5** |
| IB-14 | 1 | 1 (environ un mois) | 3 | **5** |
| IB-02 | 1 | 2 | 1 | 4 |
| IB-06 | 1 | 2 | 1 | 4 |

**Les huit premières.** On classe par somme ; à somme égale, par originalité. La coupure tombe entre la somme 5 et la somme 4, donc les égalités qui restent ne changent pas qui entre dans les huit. Pour construire le tirage, j'ai départagé ces égalités par l'ordre des identifiants ; l'ordre final ne dépend que des paires. **IB-02 et IB-06 sont écartées** avec une somme de 4. IB-02 est la fiche la plus élaborée de la série, mais sa moisson la classe en voisin proche (PerMix-RLVR) et elle n'utilise aucun instrument de la mentor.

## 3. Comparaisons par paires

On compare 28 paires, chacune dans les deux ordres, soit 56 jugements. Graine : e = `int("46efe88c21e33f6f", 16)` = 5111559790650408815. Ordre de présentation : `numpy.random.default_rng(numpy.random.SeedSequence(e)).permutation(56)`, avec numpy 2.5.3. La construction canonique est décrite dans `notes-v1.json`, champ `tirage`. Question gelée : « laquelle ferait une réponse à cette question plus juste, plus originale et plus mémorable pour ce mentor, sur ces trois critères ? ». Les jugements ont été écrits par lots de 20, 20 et 16, entre 14:50 et 14:52.

**Forces de Bradley-Terry** (`bradley_terry_ibrahim_q1_v1.py`, numpy seul) :

| Rang | Fiche | Victoires sur 14 | Log-force centrée (λ = 1) |
|---|---|---|---|
| 1 | IB-03 | 14 | +1,93 |
| 2 | IB-01 | 12 | +1,32 |
| 3 | IB-04 | 10 | +0,77 |
| 4 | IB-10 | 8 | +0,25 |
| 5 | IB-14 | 6 | −0,25 |
| 6 | IB-09 | 4 | −0,77 |
| 7 | IB-07 | 2 | −1,32 |
| 8 | IB-08 | 0 | −1,93 |

- **Le maximum de vraisemblance n'existe pas ici.** IB-03 gagne tous ses duels et IB-08 les perd tous : c'est une séparation parfaite. Les forces viennent donc d'une estimation pénalisée, déclarée dans le script : loi a priori normale de précision λ = 1 sur les log-forces. L'ordre est le même pour λ = 0,1, 1 et 10, et il coïncide avec le décompte des victoires. Seul l'ordre est à lire ; l'échelle dépend de λ.
- **Cohérence** : 28 paires concordantes sur 28, soit 1,0. Le seuil de 0,8 est franchi, mais je garde une **réserve : le résultat est presque parfait pour un juge unique qui se souvient**. Ce chiffre mesure ma constance, pas la robustesse de l'ordre. La première présentée gagne une fois sur deux (0,5), donc pas de biais de position visible. Aucune triade intransitive : l'ordre est linéaire parfait, trop propre pour valoir mesure (R4). Je ne donne aucun intervalle, car mes jugements ne sont pas indépendants.
- **Les paires ont renversé la somme trois fois, toujours contre IB-08** : IB-07, IB-09 et IB-14 la battent 2 à 0. Raison : IB-08 se passe de renforcement et repose sur la loi de Lazar, et un voisin publié (2608.29198) montre déjà la même dissociation avec des personas données par l'invite. Le tau de Kendall entre l'ordre final et l'ordre par somme vaut 0,5. Quatre des sept discordances tombent entre ex aequo, que l'ordre canonique avait rangés par identifiant.
- **Paires serrées**, marquées « Serré » dans `paires-v1.jsonl` ; l'ordre y est fragile :
  - IB-04 contre IB-14 (présentations 3 et 25) ;
  - IB-09 contre IB-14 (12 et 17) ;
  - IB-01 contre IB-04 (18 et 48) ;
  - IB-07 contre IB-08 (32 et 41) ;
  - IB-10 contre IB-14 (51 et 56).

  Rangs 3 à 5 : l'enjeu est de choisir entre une porte rapide (IB-04, IB-10) et l'expérience de fond dans la mesure de la mentor (IB-14).

**Gardes éprouvées avant le calcul réel : 18 sur 18 réussies.** Le détail est dans la sortie, champ `gardes_eprouvees`.

- Cas sain : 56 jugements conformes au tirage, et des forces connues retrouvées avec un écart maximal de 0,045.
- Artefacts refusés :
  - ligne manquante, ligne en double ;
  - identifiant inconnu, gagnant hors de la paire ;
  - ordre A/B inversé, indice canonique faux, clé absente ;
  - empreinte des fiches fausse ;
  - maximum de vraisemblance demandé sous séparation, non-convergence, valeur non finie, λ nul ;
  - paire jugée une seule fois.
- Contrôle de la cohérence : 1 sur un ensemble concordant, 27/28 après un retournement.

En cas d'échec, le script n'écrit rien. Il refuse aussi d'écraser un fichier existant.

## 4. Drapeaux de risque devant la mentor

Question posée pour chaque fiche : contient-elle une affirmation que la mentor pourrait contredire par ses propres travaux (pièce, section 1) ?

- **IB-03 — oui.** La fiche attend une sélectivité nulle (0 point). Or, d'après son papier sur les hypothèses verbalisées (pièce 1.4), le pilotage agit finement sur la sycophancie sociale, plus faiblement et de façon plus bruitée sur la factuelle : chez elle, les deux formes répondent déjà différemment à une intervention. Il faut présenter un duel sans attendre la nullité, ou attendre la sélectivité.
- **IB-01 — oui.** ELEPHANT, son papier (5e autrice), mesure déjà séparément l'approbation d'une conduite et la validation émotionnelle (moisson : « they affirm behavior deemed inappropriate… »). Présenter cette distinction comme neuve serait corrigé sur-le-champ : il faut la lui attribuer et revendiquer seulement l'avant/après renforcement sur une persona.
- **IB-04 — non.** La fiche vise le classifieur d'Open Character Training, dont les auteurs déclarent eux-mêmes les biais, et les sorties post-renforcement. Précaution : ne pas laisser entendre que son juge GPT-4o n'était pas validé ; il l'a été sur des annotations humaines (pièce 1.1). Ce qui manque, c'est la validation à style constant.
- **IB-10 — non.** La fiche est cohérente avec sa mesure d'erreur sous fausse croyance. Précaution : la rivale « pas de capitulation factuelle à cette taille » est affaiblie par ses propres chiffres sur Llama-3.1-8B (prépublication, tableau E5 : −15,06 points avec tristesse et fausse croyance, pièce 1.1). Elle ne doit pas être présentée comme probable.
- **IB-14 — non.** Précaution : garder le « coût initial positif » comme prérequis mesuré. Elle déclare en effet ne pas prétendre que toutes les méthodes pour induire la chaleur produisent les mêmes effets (*Nature* p. 1165, pièce 1.1). Citer aussi le titre publié (« can reduce accuracy ») plutôt que celui de la prépublication.
- **IB-09 — oui.** Selon la fiche, l'issue H_B « réfuterait » la cause désignée par les experts. C'est trop dire : un modèle, une récompense et une seule grandeur (le gain g de Lazar) ne suffisent pas. Sa thèse de la fragmentation (pièce 1.2) dit justement qu'un résultat nul sur une forme ne vaut pas pour les autres.
- **IB-07 — non.** La fiche va dans le sens de ce que son papier suppose et de ce que croient ses experts. Précaution : la fiche est reportée par sa propre source faute de puissance.
- **IB-08 — oui.** La fiche lit une dissociation de comportement à l'intérieur d'un modèle comme une « fragmentation du construit ». Or sa taxonomie définit la fragmentation comme des études qui donnent le même nom à des comportements de forme différente (pièce 1.2). Elle peut corriger ce sens à partir de son propre papier.
- Hors des huit : IB-02 et IB-06 — non.

## 5. Limites

- Un seul juge, auteur des notes et des paires. Les notes reflètent ma lecture des ancres, qu'il a fallu adapter : coût déclaré, entraînement commun de 15 à 30 jours.
- L'originalité repose sur la seule moisson, sans témoin.
- La porte repose sur la direction décrite par la pièce ; le second projet m'est inconnu.

## Fichiers produits (dans `/home/claude/scratch/soir-rapport/ibrahim-q1/classement-D/`)

| Fichier | sha256 |
|---|---|
| `notes-v1.json` | `4d28ea8ce1578954b721f2a3256489df1d53636a7989050066e1467a7db2c78e` |
| `paires-v1.jsonl` | `05f43ca50729f2508622c40842f0a00c79cddd9a34ab4e31cca9a6e24c68c6f0` |
| `bradley_terry_ibrahim_q1_v1.py` | `03eaa54df3325204ee5ea8cdb8f9de08c8bbce60a77caaa781ca1288cbf1505c` |
| `bradley_terry_ibrahim_q1_v1-sortie.json` | `2780ac7eb62aaff8f7ffe1820debefcf7fb701ca3dd4737a7380490547dc1557` |
| `classement-v1.md` (ce fichier) | empreinte donnée dans le rapport final (un fichier ne peut pas porter la sienne) |
