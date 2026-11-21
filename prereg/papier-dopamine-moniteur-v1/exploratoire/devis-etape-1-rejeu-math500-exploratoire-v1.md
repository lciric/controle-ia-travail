# Papier « dopamine » — devis de l'étape 1 en mode exploratoire : rejeu du chiffre publié sur MATH500 (v1)

**EXPLORATOIRE. Ce devis ne dépense rien : il demande une ligne d'accord à Lazar.** Non contre-lu (mode ouvert par GO-2026-11-21-44). Les sorties de la course seront marquées « exploratoire », sans verdict ni porte.

- Auteur : Claude Fable 5.2, concepteur. Date : 21 novembre 2026, 11:40 UTC.
- Pièces (chemin, empreinte) :
  - le plan, `prereg/papier-dopamine-moniteur-v1/exploratoire/plan-etapes-0-et-1-exploratoire-v1.md` (`60f4d959825a1e13cc19ae173b1290bec3c4015f89df22a38b8cb037ad79ea3c`), cité « plan, § » ;
  - le relevé d'offres du loueur de cartes (Vast.ai), `prereg/papier-dopamine-moniteur-v1/releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json` (`bc54f8bd468eb65e051234b31b77373aad1c52100b6e2b2a377532336f6a5196`), 30 offres dont 13 cartes A100 SXM4 de 80 Go ;
  - le programme de calcul, `prereg/papier-dopamine-moniteur-v1/exploratoire/calculs-devis-etape-1-rejeu-math500-exploratoire-v1.py` (`43c1a8942cf92fa202c2a52c075c8a5f7148292007246ac6806694f5f78be916`), et sa sortie, `…-v1.txt` (`ec8bcd8825193f243d21120456580af756edf9ec503f5f1be66f29971c643e69`), citée « calcul, bloc » ; rejeu : `python calculs-devis-etape-1-rejeu-math500-exploratoire-v1.py ../releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json`, sortie identique à l'octet ;
  - le devis voisin du même bras, `prereg/papier-dopamine-moniteur-v1/devis-lot-l-1-v2.md` (`a31d53e0a68e76a182f9305fedcadb2d6714249111ff330273526d1b7cc9766e`), l. 51, 54 et 109 seulement : bornes de l'offre, débit de seconde main, et le constat que l'étape 1 n'avait pas de devis faute de deux mesures.

## 1. Ce qui est acheté

Une instance, une carte A100 SXM4 de 80 Go, pour : générer une réponse de Llama-3.1-8B-Instruct à chacune des 500 questions publiques de MATH500 ; en extraire les états internes ; entraîner les sondes de réussite attendue et leurs contrôles ; rapatrier. Les mesures (aires, intervalles) se font ensuite sur processeur, sans dépense (plan, § B.3 à B.5).

| | Sondes | Ce que ça donne |
|---|---|---|
| **Noyau** | 25 | le chiffre sur 500 questions (couches 2 à 4, cinq plis, une graine), et les deux contrôles : étiquettes permutées, vérité plantée |
| Deux graines de plus | 30 | la variabilité due au découpage et à l'initialisation |
| Taux d'élagage par validation emboîtée | 15 | un chiffre sans le biais du « meilleur de quinze » |
| Couches 7, 15, 23 | 15 | le lien avec les couches du programme |
| Cible gelée dans l'objectif | 15 | l'effet du silence du papier sur le gradient |
| Couches 1 et 5 | 10 | l'effet du silence du papier sur l'indice de couche |
| **Complet** | **110** | |

Le noyau est le plus petit calcul qui donne le chiffre avec ses contrôles. Les blocs suivants partent dans cet ordre, chacun seulement si l'horloge le permet (calcul, bloc 3).

## 2. Machine et prix

- Bornes de l'offre, reprises du devis voisin (l. 51) : carte au plus 1,30 USD de l'heure ; stockage au plus 0,08 USD de l'heure ; soit **1,38 USD de l'heure tout compris, prix haut**. Offre vérifiée. Disque de 90 Go. Allégé ici, parce que rien n'en a besoin : 12 cœurs et 64 Go de mémoire vive suffisent.
- Au relevé de 10:55 UTC, deux offres tiennent ces bornes avec 90 Go de disque : 1,135 et 1,190 USD de l'heure tout compris (Autriche, Tchéquie). **Prix du cas attendu : 1,163 USD de l'heure** (leur médiane). Avec 60 Go de disque, trois offres, dès 0,977 (calcul, bloc 1).
- Réseau : 21 Go descendus (poids du modèle, paquets), 3 Go remontés ; de 0,04 à 0,68 USD selon l'offre (calcul, bloc 1).
- Les offres bougent d'heure en heure : un relevé neuf est pris à la création ; hors bornes, on ne crée pas.
- Disque (calcul, bloc 2) : 3,1 Go par couche au cas attendu, 8,2 au cas pessimiste. À 90 Go, les trois couches du noyau tiennent toujours ; si les réponses sont longues, les couches 7, 15, 23, puis 1 et 5, ne sont gardées que tant que la place le permet.

## 3. Débit supposé, et sa source

**Aucune pièce que j'ai le droit de lire ne donne un débit en jetons par seconde.** Le devis voisin donne 40,2 secondes par épisode en lots de 8, de seconde main, pour des épisodes d'agent (l. 54) : sans la longueur de ces épisodes, ce n'est pas convertible. Il disait lui-même que l'étape 1 manquait de deux mesures, la longueur des réponses et le débit en lots (l. 109).

Je pose donc, **supposé**, de mon seul ordre de grandeur (30 à 40 jetons par seconde et par séquence pour un modèle de cette taille en demi-précision sur cette carte, lots d'environ 24, pertes de remplissage comptées) :

| | Cas attendu | Cas pessimiste |
|---|---|---|
| Débit de génération, toutes séquences confondues | 400 jetons par seconde | 150 jetons par seconde |
| Longueur moyenne d'une réponse | 750 jetons | 2 000 jetons |
| Temps d'une sonde (100 époques) | 80 secondes | 270 secondes (hôte une fois et demie plus lent) |

**La course mesure ces trois grandeurs avant de s'engager** : les 32 premières questions sont une tranche de mesure, avec règle d'arrêt (§ 5). Le temps de la première sonde est chronométré de même. La dépense ne dépend donc pas de la justesse de ces suppositions : la coupure la borne.

## 4. Durée, cas attendu, pire cas

Calcul, bloc 4.

| | Durée | Coût |
|---|---|---|
| **Cas attendu, complet (110 sondes)** | **3,4 heures** | **4,03 USD** |
| Cas attendu, noyau seul | 1,6 heure | 1,83 USD |
| Cas pessimiste, noyau seul | 5,4 heures | 8,10 USD |
| Cas pessimiste, complet — **empêché par la coupure** | 11,8 heures | 16,90 USD |
| **Pire cas payable** : la minuterie, au prix haut, réseau haut | 6,5 heures | **9,65 USD** |

Détail du cas attendu : mise en place 0,35 h ; génération 0,26 h (375 000 jetons) ; confiance demandée 0,03 h ; extraction 0,10 h ; sondes 2,44 h ; inventaire et rapatriement 0,25 h.
Si toutes les réponses atteignaient le plafond de 16 000 jetons, la génération seule prendrait 14,8 heures (20,44 USD) : la tranche de mesure et la minuterie l'empêchent (calcul, bloc 5).
Au cas pessimiste, la course rend le noyau et aucun bloc en plus : fin à 5,38 heures (calcul, bloc 5).

## 5. Coupure et minuterie de destruction

- **Plafond : 10 USD.** Cumul relevé chez le loueur, de la création à la destruction : heures de carte, stockage, descente, remontée.
- **Tranche de mesure (32 questions).** Arrêt et destruction si : 4 réponses ou plus au plafond de jetons ; longueur moyenne au-dessus de 2 400 jetons ; taux de réussite sous 10 % ou au-dessus de 90 % ; fin du noyau projetée au-delà de 5 h 30. Un arrêt à ce stade coûte environ 0,5 USD au cas attendu, 3 USD au pire (calcul à la main : 0,75 h de mise en place plus 32 réponses au plafond à 150 jetons par seconde, 0,95 h ; 1,70 h × 1,38 + 0,68 = 3,03). Il rend les deux mesures qui manquaient.
- **Arrêt des lancements : 5 h 30 après la création.** Plus aucun bloc ne part ; inventaire, rapatriement.
- **Minuterie de destruction : 6 h 30 après la création**, par l'identifiant de l'instance (R10), armée à la création, indépendante de la session, quel que soit l'état de la course. 6,5 × 1,38 + 0,68 = 9,65 USD, sous le plafond.
- Rien n'est perdu à la destruction : après chaque bloc, inventaire (noms, tailles, empreintes) et rapatriement des scores, des poids des sondes, des textes générés et des états de la position de lecture. **Exception à trancher par la mère** : les états de toutes les positions des réponses (9 à 25 Go pour les couches 2 à 4) ne sont pas rapatriés par défaut ; ils se recalculent des textes, qui, eux, sont rapatriés. Les rapatrier ajoute au plus 1 USD et un quart d'heure, et ne se fait que si le cumul reste sous le plafond.
- L'horloge et la minuterie sont des gardes : essayées sur un cas sain et sur un artefact avant la création (R5 ; plan, § B.3, point 10).

## 6. Ce qu'on sacrifie si on réduit

- **Noyau seul, même plafond** (1,83 USD attendus au lieu de 4,03). Perdus : la variabilité entre graines (l'intervalle ne porte alors que le tirage des questions) ; le chiffre sans biais de sélection (il reste l'excès sur les étiquettes permutées) ; le lien avec les couches 7, 15 et 23 du programme ; les deux réponses aux silences du papier (cible gelée, indice de couche). Relancer plus tard pour les avoir recoûte la mise en place et l'extraction.
- **Un seul découpage, à la lettre du papier** (5 sondes ; calcul à la main : 0,99 h + 5 × 80 s = 1,10 h ; 1,32 USD attendus). Perdu : 100 questions notées au lieu de 500, donc une demi-largeur d'environ 0,10 au lieu de 0,05 (calcul, bloc 8). Le chiffre ne dirait presque rien. Déconseillé : on y gagne un demi-dollar.
- **Carte de 40 Go** (15 offres vérifiées de 0,40 à 0,87 USD de l'heure au relevé ; calcul, bloc 1). Divise le prix par deux environ. Risque : une réponse au plafond occupe 2,1 Go de mémoire pendant la génération (calcul, bloc 2), donc des lots plus petits si les réponses s'allongent. Hors des bornes héritées : sur un mot de Lazar seulement.

**Recommandation** : la ligne entière, noyau puis blocs sous l'horloge, plafond de 10 USD. Confiance moyenne sur les durées (trois grandeurs supposées), forte sur la borne (la minuterie ne dépend d'aucune).

## 7. Conditions avant la création de l'instance

1. Le code est écrit, son commit est consigné, et chaque garde a passé son cas sain et son artefact sur processeur (plan, § B.3).
2. Le manifeste est écrit : racine des graines, force plantée (4), ordre des blocs, seuils des gardes, empreinte du jeu, révision des poids, empreinte du relevé neuf, identifiant de l'accord.
3. Le libellé de l'invite et les champs du jeu, écrits de mémoire dans le plan, sont relevés sur leur source.
4. L'accès aux poids du modèle est acquis (jeton lu par son nom, jamais écrit).
5. Le crédit du loueur couvre le plafond ; aucune recharge n'est supposée.
6. Une ligne d'engagement est écrite au registre des dépenses avant la première minute : ligne d'accord, plafond, devis et empreinte, commit, offre retenue, attendu et pire cas.

## 8. Ligne d'accord proposée

`| GO-2026-11-21-NN | 2026-11-21 | calcul | Papier « dopamine », étape 1 en mode exploratoire : rejeu du chiffre publié sur MATH500 (Llama-3.1-8B-Instruct, 500 questions publiques : génération, extraction des états internes, sondes de réussite attendue, contrôles), noyau puis blocs dans l'ordre du devis prereg/papier-dopamine-moniteur-v1/exploratoire/devis-etape-1-rejeu-math500-exploratoire-v1.md (empreinte de son compagnon). Une instance, carte A100 SXM4 de 80 Go, au plus 1,30 USD de l'heure et 0,08 USD de l'heure de stockage ; tranche de mesure de 32 questions avec règle d'arrêt ; plus aucun lancement après 5 h 30 ; destruction par minuterie 6 h 30 après la création. Sorties marquées « exploratoire », sans verdict ni porte. | 10 USD | 2026-11-24 | Lazar | mot de Lazar à porter par la mère |`

Le numéro est attribué par la mère.

---

## Relevé de méthode

**Chaîne de raisonnement.**
1. Treize offres de carte A100 de 80 Go au relevé ; deux tiennent les bornes avec 90 Go de disque, à 1,135 et 1,190 USD de l'heure. — calcul, bloc 1 ; relevé (`bc54f8bd…`).
2. Les bornes de l'offre sont celles du devis voisin. — `devis-lot-l-1-v2.md`, l. 51 ; de seconde main pour moi. Cœurs et mémoire allégés : supposé suffisant.
3. Débit, longueur des réponses, temps d'une sonde. — **supposé**, § 3 ; mesurés par la tranche et par la première sonde.
4. Volumes de disque et de mémoire. — calcul, bloc 2 ; pas 3.
5. 25 sondes au noyau, 110 au complet. — calcul, bloc 3 ; plan, § B.5.
6. Durées et coûts. — calcul, bloc 4 ; pas 1, 3, 5.
7. Le pire cas payable est 9,65 USD, sous un plafond de 10. — calcul, bloc 5 ; pas 1.
8. Au cas pessimiste, le noyau finit avant l'arrêt des lancements. — calcul, bloc 5.

**Objets de contrôle.** Pour l'énoncé « la dépense tient sous le plafond » (calcul, bloc 6). Objets où il est faux : le complet au cas pessimiste (16,90 USD) ; la génération tout au plafond de jetons (20,44 USD). Prévu : au-dessus. Rendu : au-dessus. Objets où il est vrai : le pire cas payable (9,65) ; le noyau pessimiste (8,10) ; le complet attendu (4,03). Prévu : sous. Rendu : sous.

**Premier pas non justifié.** Le pas 3 : aucune mesure ne porte le débit, la longueur des réponses ni le temps d'une sonde. Les justifieraient la tranche de mesure et le chronométrage de la première sonde, qui sont dans la course.

**Mode d'échec affecté.** Sans objet : cette pièce n'est pas une relecture.

**Dérivation de l'énoncé seul.** Sans objet : cette pièce n'est pas une re-dérivation.

**Trouvaille de côté.** Deux offres seulement tiennent les bornes héritées avec 90 Go de disque, dont une au disque de 91 Go : la borne de stockage de 0,08 USD de l'heure écarte quatre offres dont le prix tout compris, de 1,17 à 1,31 USD de l'heure, tient pourtant sous 1,38 (calcul, bloc 1). Question pour la mère, non poursuivie.

**Évaluateur et conseil.**
- Ce qui juge ce devis : Lazar, sur la ligne proposée ; puis le cumul relevé chez le loueur. Aucun contre-lecteur (mode exploratoire). Ce juge n'a été admis sur aucun témoin.
- Par où ce devis paraîtrait bon sans l'être : les trois grandeurs supposées peuvent être fausses d'un facteur trois sans que le calcul le montre ; le « cas attendu » peut être lu comme une promesse. Seule la minuterie est sûre, et elle protège la dépense, pas le résultat : une course coupée rend moins de blocs, ou seulement les deux mesures.
- Conseil au lanceur : armer et essayer la minuterie avant de créer l'instance ; rapatrier après chaque bloc, pas à la fin.
