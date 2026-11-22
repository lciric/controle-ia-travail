# Contre-lecture — préenregistrement de l'expérience 7 du billet « Sparks » sous paires nulles et aveuglement, v2, brouillon 1 — Opus, v1

- **Date** : 21 novembre 2026, de 19:48 à 19:58 UTC environ (`date -u` : 19:48:11 au début, 19:55:45 avant l'écriture).
- **Contre-lecteur** : Claude Opus 5.5, agent neuf. N'a écrit ni le brouillon, ni ses calculs, ni l'état des lieux, ni le texte v1, ni l'addendum n° 1, ni le code, ni leurs contre-lectures (R2 ; « Qui conçoit »).
- **Pièce relue** : `prereg/SPARKS-EXP7-NUL-preenregistrement-v2-brouillon1.md`, sha256 `ff6fac2bd7f54143d4b009d944c83aaca7c78ef9bda32282b181a5db6000b6ac` ; compagnon vérifié « OK » avant lecture.
- **Aucune dépense, aucun envoi, aucun commit.**

## 1. Verdict

**À corriger.** Le brouillon est fidèle au texte v1 et à l'addendum sur l'essentiel. Chaque chiffre que j'ai suivi retombe sur sa source. Les calculs se rejouent à l'octet. La prédiction et les seuils sont fixés d'avance. La liste d'arrêt ne lit le signe d'aucun résultat, et les douze nœuds sont, à deux options près, bien posés. Restent cinq corrections importantes avant le scellement :

1. le retrait de l'arrêt sur l'ampleur de l'écart dans la paire, sans que la marque ne passe dans le nom du verdict, avec une option du texte v1 perdue au nœud 5 ;
2. les conventions numériques de la distance au départ, perdues ;
3. le seuil de la base « normes sans départ », absent ;
4. la règle des conversations interrompues, incomplète : elle laisse une marge de choix ;
5. les taux d'erreur du contrôle causal à 24 unités, absents.

Il reste aussi treize points mineurs. Aucune lecture interdite, ni par le rédacteur ni par moi.

## 2. Ce que j'ai lu et vérifié

**Pièces données, empreintes vérifiées « OK »** :
- le brouillon ;
- les deux scripts de calcul et leurs sorties ;
- le relevé de rejeu ;
- l'état des lieux (`c384311c…`) ;
- le texte v1 (`4bacf20d…`) ;
- l'addendum n° 1 (`c0305919…`) ;
- le gabarit (`8cad4371…`).

**Lus en entier** :
- le brouillon ;
- l'état des lieux ;
- le texte v1, par l'outil de lecture sur le fichier du dépôt ;
- le gabarit ;
- les scripts et leurs sorties.

**Lu en partie** : l'addendum n° 1, lignes 1 à 30, 150 à 240 et 616 à 806 (sections réécrites, étape 0, table des changements A-1 à A-23, décisions D-1 à D-4). Sa table d'empreintes et ses tables de comptes ne sont pas lues.

**Vérifié en appui** :
- **la lecture factuelle du billet**, lignes 23, 26, 42, 56 à 108 (`fff05896…`) ;
- **le registre des accords** : ligne 678, GO-2026-11-21-79, registre `ac33f39b…`, identique à celui que cite le brouillon. Ligne 674 aussi (« Économie de Fable »).
- **`CLAUDE.md`** (`eb06c8fd…`), sections « Qui conçoit », « Économie de Fable » et « Appels aux modèles de Google ».
- **La décision N-062** (`63f42690…`).
- **Le validateur `prereg.py`** (`3b2e3ee5…`) : il refuse le brouillon pour les huit marqueurs et l'absence de contre-lecture inscrite, ce que le brouillon annonce.
- **Au commit `78671d93`, les empreintes des sept fichiers** :
  - consigne principale v2 ;
  - consigne de l'ancre ;
  - procédures des lecteurs v1 et v2 ;
  - `plan.py` ;
  - les seize textes ;
  - liste fermée v12.

  Toutes sont égales à celles du brouillon. Les clés de tâche de `plan.py` et les générateurs de l'incrément s'accordent avec le brouillon. Les « 92 Go pour 53 cas » viennent de la procédure v1, ligne 54.
- **Les dix PDF de la table des voisins** : empreintes égales. J'ai extrait les pages citées par `pdftotext` et relu chaque phrase de la table contre la page (section 4).
- **Le journal des dépôts de code** (`bbaca6eb…`) : lignes 52, 100, 248, 258, 259, 277, égales aux descriptions citées.

**Rejoué** :
- les deux scripts du rédacteur, sous le Python du système et sous `.venv` (Python 3.13.18 dans les deux cas) : sorties identiques à l'octet aux fichiers scellés ;
- les parties « puissance de la discrimination entre paires nulles » (`1ff1d809…`) et « incrément, alternatives » (`078e42af…`) du script de puissance de l'addendum : identiques à l'octet aux sorties scellées.

**Non ouvert** :
- aucun fichier « [chemin réservé] » ni « [chemin réservé] » ;
- rien sous `brouillons/ii-b-saboteur-budget-v1/`, sous `archives-reponses-modeles/` ni sous `[chemin réservé]` ;
- aucun résultat d'une autre course ;
- rien sous `/root/.claude/`. Le harnais y a rangé la sortie d'un affichage du texte v1 ; je ne l'ai pas ouverte et j'ai relu le fichier du dépôt.

Les copies des données des auteurs dans le code (`src/controle_ia/sparks_exp7_nul_v1/donnees_auteurs/`) n'ont pas été ouvertes. Leur nom seul est passé dans une liste de fichiers.

## 3. Corrections importantes, à faire avant le scellement

**I-1. Ampleur de l'écart dans la paire : la marque doit entrer dans le verdict, et le nœud 5 doit garder l'option du texte v1** (point soumis 1).

Retirer l'arrêt se défend. Sous des rangs échangeables, un arrêt sonne à tort dans 0,107 des cas (calc, F). La ligne « tient sous nul, au-delà » reste protégée par la discrimination entre paires nulles, par l'aire par modèle et par l'incrément sur les deux bases : l'ampleur seule ne la donne pas. Aucun verdict indu sur la première ligne, donc.

Mais le rédacteur juge lui-même probable (P13, 0,6) que les paires vraies soient plus écartées que les nulles. Le lecteur peut calculer cette ampleur sur ses deux dossiers. Dans ce monde, une scission minoritaire ne dit plus rien de la reconnaissance de l'absence du trait. Or les verdicts des deux premières lignes s'appellent toujours « sous nul ». La mise en garde est écrite dans « Ce que chaque issue ne montre pas », mais pas dans le nom du verdict ni dans la réponse à Q1.

Le texte v1 (l. 41) donnait aux graines différentes la raison même d'empêcher cette séparation. Il prévoyait d'avance une option de repli (l. 71) : paires nulles à données permutées, même graine et même ordre que la paire vraie. Le nœud 5 ne la propose plus.

Corrections :
- (a) quand la marque « types de paires séparables par l'ampleur » est posée, la phrase entre dans le nom du verdict des lignes 1 et 2, avec la mention « scission non probante », et dans la parenthèse de Q1 ;
- (b) ajouter au nœud 5 l'option (d) du texte v1, paires nulles à données permutées, avec son coût (des modèles de plus, une fabrication autre) ;
- (c) dire à qui va le résultat de l'étalonnage « rapporté avant tout lecteur » (au directeur, pour information, sans rien suspendre) ;
- (d) reprendre, à la section des bases, la réserve de calc, F : les 12 paires de l'étalonnage partagent leurs modèles, 4 par groupe. Elles ne sont pas indépendantes : le 0,107 est un ordre de grandeur, non un risque exact.

**I-2. Distance au départ : conventions numériques perdues** (fidélité). L'addendum (§ Bases et plafond, l. 650) fixe :
- les tenseurs servis en bf16, lus exactement en float32 ;
- sur l'étalonnage, les couches bf16 stockées par la recette ;
- θ_0 arrondi en bf16 de la même façon, à consigner.

Le brouillon ne garde que « calcul en double précision ». Ces conventions changent le score d'une base qui décide entre les lignes 1 et 2. Il faut les reprendre à la lettre.

**I-3. Base « normes sans départ » : seuil absent** (fidélité, complétude). L'addendum (l. 651) fixe le seuil : celui qui maximise l'exactitude équilibrée de o₄ · n sur l'étalonnage, calculé avec o₄. Il fait aussi rapporter l'orientation que donnerait l'étalonnage seul.

Le brouillon donne l'orientation, pas le seuil. Pourtant son plan d'analyse (étape 5) dit « sens et seuil … fixés d'abord », et la table de lecture appliquée à cette base seule en a besoin. Il faut reprendre les deux.

**I-4. Conversations coupées ou interrompues : règle incomplète, qui laisse une marge de choix** (point soumis 7). Il faut écrire :
- (i) la liste des signaux de transport qui classent une fin en « refus ou coupure du fournisseur » ou en « panne » (codes d'erreur, quota, réseau, redémarrage). Elle est figée à l'ordre de course, avant toute conversation, et appliquée par script ;
- (ii) seule la réponse de la conversation relancée compte. La trace interrompue est gardée, ne compte pour rien, et n'est pas lue avant l'ouverture du coffre ;
- (iii) une seconde interruption du même cas vaut « coupée », donc un échec ;
- (iv) si les conversations relancées comptent dans la ligne d'arrêt des 10 %, et quel est le dénominateur de cette ligne : 51 avec l'ancre, ou 48.

Sans (i) à (iii), le classement d'une fin ambiguë décide entre un échec et une seconde chance.

**I-5. Taux d'erreur du contrôle causal à 24 unités, absents** (point soumis 2 ; le gabarit demande les taux d'erreur visés). Calc, H donne les seuils, 6 et 2 sur 24, pas leur comportement. Je l'ai calculé par loi binomiale exacte (`python3 -I -c` dans mon bloc-notes, bibliothèque standard), en supposant les unités indépendantes :

| Part vraie d'unités porteuses | P(6 ou plus sur 24) | P(2 ou moins sur 24) |
|---|---|---|
| 0,05 | 0,001 | 0,884 |
| 0,10 | 0,028 | 0,564 |
| 0,25 | 0,578 | 0,040 |
| 0,35 | 0,896 | 0,003 |

Lecture : les deux seuils gardent un risque faible de mauvaise classe aux deux bouts. Mais avec une part vraie de 0,25, « porteurs » n'est déclaré qu'une fois sur deux environ. Avec 0,10, « non porteurs » ne l'est qu'un peu plus d'une fois sur deux.

Le rédacteur verse ces valeurs dans son propre script (bloc H) et à la section « Seuil ». Le sens des seuils à 24 unités tient. La table causale reste exhaustive et exclusive.

## 4. Points mineurs

- **m-1 (C-3 ; nœud 1, option d).** « Économie de Fable » réserve Fable 5.2 (`CLAUDE.md`, l. 72). Dire que Fable 5.1 « entame un quota rare » va au-delà de la lettre ; l'état des lieux (§ 4.1) laisse la question au directeur. Écrire : « quota de Fable 5.1 : à dire par le directeur ».
- **m-2 (nœud 1, option c).** Aucune pièce lue ne vérifie l'identifiant « Claude Sonnet 5.5 ». Écrire « un autre modèle Claude hors Fable, à nommer par le directeur, identifiant vérifié avant le devis ».
- **m-3 (nœud 7, option c).** « L'environnement à processeur est celui où les 361 essais passent » est inexact : ils passent dans la session, non sur une machine louée. Écrire « un environnement à processeur comme celui de la session ; suite à rejouer sur la machine ».
- **m-4 (C-4 ; Lecteurs).** « xhigh » est le nom d'un niveau du client des auteurs pour Astra (p3, l. 23). Le même nom chez Claude n'établit aucune équivalence. Écrire « même nom de niveau que le billet ; équivalence non établie ».
- **m-5 (voisins, Liu et Yang).** « Un réseau à la fois » n'est pas sur la page 1 lue. À retirer, ou à sourcer par une autre page lue.
- **m-6 (voisins, Balappanawar et al.).** La page 1 dit « We experiment using CNNs ». Ajouter « réseaux convolutifs » au régime, comme pour Liu et Yang.
- **m-7 (esquisse de devis, jetons de sortie).** p3, l. 108 donne un repère agrégé : environ 1,1 million de jetons de sortie pour les 15 conversations de l'expérience 7, dont 12 sans outil. Le citer comme repère au lieu de « non chiffrés dans les sources ».
- **m-8 (esquisse de devis, variante sans carte).** Les 75 h du texte v1 portent sur 2 016 mesures causales, dont 26 h de contrôle causal (v1, l. 190) ; le plan en a 1 632. Le dire, ou ramener le contrôle causal à environ 21 h par la même règle de trois.
- **m-9 (liste d'arrêt).** Ajouter « révision de Gemma plus servie », qui n'est que dans « Modèles », et « ampleur de l'écart incalculable sur un cas servi » : elle est calculée au service, mais la ligne ne nomme que la distance au départ et les normes.
- **m-10 (graines, R9).** L'ordre d'emploi des générateurs pour les secondaires de l'incrément, fixé par l'addendum (l. 712 : « repris après le calcul principal, dans cet ordre … »), n'est pas repris. Le générateur de l'intervalle de la marque n'est pas nommé (`dispersion-reechantillonnage` ?).
- **m-11 (gabarit).** Le gabarit attend les graines dans « Plan d'analyse ». Un renvoi d'une ligne à « Graines et manifeste » suffit.
- **m-12 (« Ce que ce texte change », en tête).** « Les quatre décisions prises sur l'addendum » sont celles de conv-audit (ad1, l. 17), non du directeur. Le dire.
- **m-13 (base d'attention scriptée).** Écrire, comme le texte v1 (l. 70), que les seize textes sont tirés de faits absents de tous les partages. C'est leur raison d'être ; « repris à l'octet » ne le dit pas.

## 5. Réponses aux dix points soumis

1. **Ampleur et scission.** La discrimination entre paires nulles garde son sens : elle demande une lecture absolue que l'ampleur ne donne pas. La scission perd le sien si la marque est posée. Pas de verdict indu sur la ligne 1, mais un nom de verdict trompeur sur les lignes 1 et 2 : I-1.
2. **Un lecteur au lieu de deux.** Les lignes de la table sont exclusives par leurs plages (exactitude d'ordre de 17 ou plus pour les trois premières ; scission de 7 ou moins contre 12 ou plus ; exactitude de 12 ou moins pour la quatrième). La table est exhaustive par « toute autre combinaison ». La règle de l'addendum « plusieurs lignes : non concluant » n'a plus d'objet. Contrôle causal : I-5.
3. **Provenance.** Je n'ai trouvé aucune valeur inventée. J'ai suivi jusqu'à sa source chaque valeur des sections « Seuil », « Ce que chaque issue ne montre pas », « Métrique », de l'esquisse de devis et de la table des voisins. Les « [P] » de la relance unique et du seuil strict à 0,5 sont des choix, non des valeurs de principe : écart de mot, sans effet.
4. **Voisins.** Les phrases de la table disent ce que disent les pages citées, sauf m-5 et l'omission m-6. J'ai relu les citations exactes, toutes conformes :
   - Goworek et al., p. 3 : « 12 of 12 over three runs each » ; p. 13 : « one of the networks was poisoned » et « how far each poisoned model is from the clean one » ; p. 14 et 15 : 23 et 14 sur 32, 13 et 17 sur 32 ;
   - Liu et Yang, p. 1 : « raised no false alarm in 21 runs on null networks » ;
   - Weight Oracles, p. 6 : « at the operating point yielding 94% TPR, 20% of clean models are incorrectly flagged » ; p. 1 : 0,93 et 0,81 ;
   - AuditBench, p. 1 ;
   - Abu Baker et al., p. 1 (76 organismes, fiable sans le point de départ) ;
   - Diff Mining, p. 1 ;
   - Minder et al., p. 1 (« might not be realistic ») ;
   - Ahmed, p. 1 (« local arithmetic plus dataset priors », « exploratory ») ;
   - IWIBench, p. 1.
5. **N-062.** La portée n'excède pas la lettre. Le brouillon dit que la lettre vise G1 et les sondes, et renvoie l'extension au nœud 8, sans défaut. C'est juste.
6. **Liste d'arrêt.** Aucune ligne ne lit le signe d'un résultat. Les déclencheurs de l'audit de symétrie sont des issues, mais dans les deux sens, et ils n'arrêtent que la lecture jusqu'à la fin de l'audit.
7. **Conversations coupées.** Oui, une marge reste : I-4.
8. **Prédictions.** Elles sont cohérentes :
   - la somme de P15 vaut 1 ;
   - P1 (0,65 pour 17 ou plus) donne 0,47 pour les trois lignes à exactitude d'ordre haute et 0,18 de « non concluant » à exactitude haute ;
   - 0,25 pour 13 à 16 et 0,10 pour 12 ou moins (« pas de détection ») ;
   - « non concluant » vaut donc 0,18 + 0,25 = 0,43, comme P15 ;
   - P2 (0,55) majore les 0,35 des deux premières lignes ;
   - P11 (0,95 « non tenu ») laisse 0,05 à l'incrément tenu, au-dessus des 0,04 de « tient, au-delà ».
9. **Modèles de secours retirés.** Aucun cas sans règle : accès en échec, nœud ; départ qui ne suit pas, arrêt ; révision retirée, arrêt et nœud (à porter à la liste d'arrêt, m-9).
10. **Clés de tâche et code.** Les clés, les noms de fichiers et les générateurs de l'incrément et des bases s'accordent avec `plan.py` et les modules au commit `78671d93`. Les clés neuves (`dispersion-…`, `contraste-…`, `pilotes`) n'existent pas encore dans le code, comme il est attendu ; la liste fermée du code les demande.

## 6. Ce qui est juste et doit rester

- Le passage de la table de calcul des bases avant l'empreinte du script d'analyse à l'ordre inverse (C-23). Il corrige un vrai défaut du texte v1 (l. 126-127).
- Le retrait de la phrase « apport propre », et la question posée avec les voisins lus sur PDF (C-9).
- Le lecteur unique : le texte v1 (l. 195) disait déjà que l'unité de l'exactitude d'ordre, de la scission et de la discrimination est le cas.
- La règle d'échec : jamais « 0,5 et 0,5 ».
- La conjonction de l'incrément et son nul, rejoués.
- Les règles d'appel à Google et à Carbon, sans objet ici, dites telles.

## 7. Nœuds pour le directeur, vus par cette contre-lecture

Aucun nœud neuf au-delà des douze. Deux nœuds sont à compléter par le rédacteur avant de te les soumettre :
- **nœud 5** : l'option du texte v1 (paires nulles à données permutées) ;
- **nœud 1, option d** : le quota de Fable 5.1, à ta main.

---
Contre-lecture v1, classe A (contre-lecture d'un préenregistrement), écrite par Claude Opus 5.5 avant toute donnée. La vérification des corrections revient au même contre-lecteur.
