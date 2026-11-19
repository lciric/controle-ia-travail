# Brouillon de devis — relecture des quatre cases par un même chemin de calcul, pour la seconde lecture du texte neuf « validité de l'adaptateur pour les sondes apprises sur la tâche » — v1 — brouillon 1

- **Auteur** : rédacteur neuf, sous-agent de la session mère, Claude Fable 5.2 ; le même que celui du brouillon 1 du texte neuf. **Date (UTC)** : 2026-11-19, vers 14:10 (`date -u`).
- **Statut** : brouillon de devis, scellé comme brouillon, non contre-lu. **Aucune dépense engagée, aucune machine louée.** La dépense attend ce devis scellé après contre-lecture et une ligne neuve du registre des accords : Lazar a donné un accord de principe (ligne `GO-2026-11-19-62`, décision 3, option a : « de l'ordre de 2,5 à 4,6 USD, coupure 8,5 »), pas une ligne de calcul.
- **Texte servi** : `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md` (plan d'analyse, « relecture sur carte » ; empreinte dans son compagnon). Ce devis ne change aucune règle de ce texte.
- **Arithmétique** : `devis-relecture-meme-chemin-v1.py` (`c73b01a7f39f568392dd2d9b942cf1b51cd5c1c108b30f49e165b3534d3a2e9e`) et sa sortie `sortie-devis-relecture-meme-chemin-v1.json` (`d158afae7b48e4acf89505eab351a8fb09f4639e629a95f289d2e01ac5016fa4`), au bloc-notes du rédacteur, `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/barreau5-premiere-lecture/`, à verser par la session mère à côté de ce devis. Aucune donnée du programme n'y est ouverte.

## En une ligne

Une carte A100 de 80 Go, une marche de 2,1 à 3,4 heures. Attendu : **≈ 2,9 à 4,9 USD** sans le dépôt des activations par jeton, **≈ 3,2 à 7,0 USD** avec. Pire cas (hôte deux fois plus lent, tout gardé) : **≈ 12,4 USD**, au-dessus de la coupure. **Coupure : 8,5 USD**, celle du mot de Lazar. Au pire cas, l'ordre de sacrifice ci-dessous garde les quatre cases du saboteur aux quatre doses et leurs scores (≈ 8,0 USD) ; il perd d'abord le dépôt des activations par jeton, puis les séries descriptives.

## Ce qui change par rapport au chiffre de la note de résolution (2,5 à 4,6 USD)

Ce chiffre était celui du devis scellé de la relecture à texte constant du texte de validité (`prereg/validite-adaptateur-v1.md`, « Calcul et dépense », lignes « R : … » : 1,90 à 2,80 heures, pire cas ≈ 8,85 USD, coupure 8,5). La note le disait à refaire. Trois choses s'ajoutent :
- vingt et une séries au lieu de onze : vingt sont dans la liste de la note, dont trois hors de son compte de volume, et une est ajoutée (voir « Séries ») ;
- la mesure d'intensité des deux adaptateurs, de deux façons ;
- les activations gardées, que les deux courses scellées ne gardaient pas : c'est le poste le plus incertain (débit d'envoi de l'hôte, prix du réseau).

Une chose s'enlève : aucune sonde de la famille de Mahalanobis, aucun témoin distillé, aucune recherche de facteur d'échelle.

## Sources des nombres (aucun chiffre de résultat, aucun chiffre de l'état de l'art)

- **Débit** : 0,45 seconde par passe d'épisode ; **prix** d'une A100 SXM4 de 80 Go : 1,0889 à 1,30 USD de l'heure attendus, 1,40 au pire (hôte deux fois plus lent) ; stockage au plus 0,08 USD de l'heure ; réseau au plus 0,05 USD par Go. Source : `prereg/validite-adaptateur-v1.md` (`7e78909d…`), « Calcul et dépense » ; `brouillons/T0.7-etape-B-bis-v1/devis-etape-b-bis-v3.md`, « Sources des nombres ».
- **Dépenses réelles voisines** (`registres/depenses.md`) : course de l'apprentissage des sondes sur la tâche, relecture, apprentissage et notation compris, 3,9633 heures à 1,1833 USD de l'heure, 4,690 USD (ligne du 18 novembre, instance 61276240) ; relance de la notation des sondes génériques, 2,170 heures, ≈ 2,36 USD.
- **Volume des activations** : le sous-ensemble poussé par la course de confirmation pèse 1 058 424 128 octets pour 576 actions, à la couche 15, par jeton, en demi-précision (note 04 du socle, § 3), soit ≈ 1,18 Go pour les 640 actions d'une série.
- **Hôte** : la roue de torch employée demande un hôte à CUDA 13.0 au moins (répétition de l'étape B bis, `registres/depenses.md`, 15 novembre, instance 60756203).

## Séries, dans l'ordre de jeu

Une série = les 64 épisodes d'une condition, relus en forçage des identifiants générés, sous un état d'adaptateur imposé, par la fonction d'état imposé existante (`src/controle_ia/t07bbis/etat_impose_v1.py`, `39e8e1a9…`, qui accepte toute dose de 0 à 1 pour tout adaptateur chargé). L'ordre de jeu est l'inverse de l'ordre de sacrifice.

| bloc | séries | nombre | sert à |
|---|---|---|---|
| **A** | textes honnêtes sous le modèle nu ; puis, pour chaque dose dans l'ordre 1 ; 0,5 ; 0,25 ; 0,75 : textes du saboteur sous son adaptateur, textes honnêtes sous l'adaptateur saboteur, textes du saboteur sous le modèle nu | 13 | les quatre cases aux quatre doses : interaction, contraste à adaptateur constant, tendance, sans réserve de chemin de calcul |
| **B** | textes honnêtes sous l'adaptateur témoin à la dose 1 ; textes du témoin sous son adaptateur ; textes du témoin sous le modèle nu | 3 | les quatre cases du témoin à la dose 1 : triple différence, qui ôte la part de l'effet « texte propre » commune à tout adaptateur |
| **C** | textes honnêtes sous l'adaptateur témoin aux doses 0,5 ; 0,25 ; 0,75 | 3 | saboteur contre témoin à intensité mesurée voisine, sur les mêmes textes |
| **D** | épisodes du témoin instruit, puis du saboteur instruit, dans leur état d'origine (modèle nu, leur consigne) | 2 | la rivale « présence d'une consigne » sous les sondes de dose |

- L'ordre des doses (1 ; 0,5 ; 0,25 ; 0,75) est celui du texte scellé de validité pour son témoin (`prereg/validite-adaptateur-v1.md`, plan, point 2, « Ordre de jeu ») : il a été écrit avant tout résultat ; il n'est pas choisi ici.
- **Écart de compte avec la note de résolution.** Elle écrit « dix-sept séries, ≈ 20 Go » (décision 5), alors que sa propre liste de l'étape 4 en compte vingt : treize pour les quatre cases, quatre pour le témoin sur les textes honnêtes, deux pour les textes du témoin (sous son adaptateur et sous le modèle nu), une pour le témoin instruit. Vingt séries font ≈ 23,5 Go.
- **Série ajoutée par le rédacteur, déclarée** : le saboteur instruit relu par le même chemin (bloc D, dernière jouée, première sacrifiée). Sans elle, la ligne « présence d'une consigne » compare une série du chemin neuf à une série de l'ancien chemin, et n'existe que pour la sonde de la dose 1. Avec elle : vingt et une séries, ≈ 24,7 Go. Coût marginal : 64 passes et leur notation.
- **Mesure d'intensité** : pour chaque épisode honnête, la loi du jeton suivant sous le modèle nu et sous les huit états (saboteur et témoin, quatre doses) ; 576 passes comptées à part, comme majorant (elles peuvent se confondre avec les séries « textes honnêtes sous adaptateur »).

Total : 1 344 passes de séries et 576 de mesure d'intensité, 1 920 passes, soit 0,24 heure de passe pure.

## Entrées descendues sur l'instance, et seulement elles

- De la course de confirmation de l'organisme à adaptateur : les textes des actions avec leurs identifiants générés, les mesures, les deux adaptateurs, le sous-ensemble d'activations (pour la garde d'équivalence), le manifeste, la fiche de distillation (empreintes des adaptateurs).
- De la course de l'apprentissage des sondes sur la tâche : les poids des sondes (`sondes-bbis.npz`), les 800 directions de chaque sonde (`planchers-bbis-000.npz` à `-002.npz`), les réglages retenus (`sondes-bbis.json`, qui ne porte aucune aire).
- Un fichier neuf des **poids des sondes jumelles** : ils ne sont pas dans le fichier des sondes, mais dans les fichiers fermés de scores (tableaux `o2__w`, `o2__b`, `o2__q`). Ils en sont extraits au processeur, par nom de tableau, sans lire aucun score, après le scellement du texte neuf ; le fichier extrait est scellé.
- **Jamais** les fichiers de scores eux-mêmes, ni aucun fichier de lecture ou de verdict.

## Postes (heures de carte ; attendu bas et haut)

| poste | heures |
|---|---|
| mise en place (image, modèle, dépôt, données de la course de confirmation, poids des sondes, des jumelles et des directions) | 1,0 |
| essais ciblés sur l'instance (jouet, identité, chemin, refus de la moyenne) | 0,3 |
| contrôles d'identité des deux adaptateurs (dose 0 égale à la base au bit près, dose 1 différente) | 0,05 |
| relectures et mesure d'intensité (1 920 passes), écriture locale des activations de la couche 15 | 0,45 à 0,80 |
| garde d'équivalence des séries à l'état d'origine contre le sous-ensemble poussé par la course de confirmation | 0,05 |
| notation fermée : sondes, jumelles, 800 directions par sonde sur le bloc A, avec et sans les jetons du champ du coût | 0,15 à 0,50 |
| écriture des scores fermés, sceaux, poussée des scores | 0,10 |
| **total sans le dépôt des activations par jeton** | **2,10 à 2,80** |
| dépôt des activations par jeton (≈ 25 Go) | 0,15 à 0,60 |
| **total avec ce dépôt** | **2,25 à 3,40** |

Les postes de mise en place, d'essais, de garde et de poussée sont ceux du devis scellé de la relecture à texte constant. Le poste des relectures est mis à l'échelle de celui de la course de l'étape B bis (1 216 passes et trois couches écrites : 0,35 à 0,55 heure). Le poste de notation part de celui du devis scellé (0,1 à 0,5 heure pour 3 200 directions) ; sa borne basse est relevée à 0,15 pour 6 400 directions.

## Montants (USD)

- **Attendu, sans le dépôt des activations par jeton** : 2,10 h × 1,0889 à 2,80 h × 1,30, stockage, descente du modèle et des données (0,4 à 1,0) : **≈ 2,9 à 4,9**.
- **Attendu, avec ce dépôt** : 2,25 h à 3,40 h, plus l'envoi de ≈ 25 Go (de 0,1 à 1,2 selon le prix du réseau de l'hôte) : **≈ 3,2 à 7,0**.
- **Pire cas** (hôte deux fois plus lent, 1,40 USD de l'heure, réseau au plus cher) : 6,8 heures, **≈ 12,4** si tout est gardé ; **≈ 9,4** sans le dépôt des activations par jeton ; **≈ 8,0** pour le bloc A seul, scores poussés (4,66 heures).
- **Lecture au processeur** (première et seconde) : 0 USD.

## Coupure, garde de projection, ordre de sacrifice

- **Coupure : 8,5 USD.** Arrêt et destruction par identifiant (R10) dès que le cumul relevé plus un quart d'heure de carte (≤ 0,37 USD au prix pire) atteint la coupure. Au pire cas, le bloc A seul laisse 0,15 USD de marge sous cette règle : c'est juste, et c'est dit.
- **Garde de projection**, pour que la coupure ne détruise pas une marche sans scores : après chaque bloc, le lanceur calcule le cumul, plus le coût projeté du bloc suivant au débit observé, plus le coût de la poussée des scores. Si la somme dépasse 8,5 USD moins un quart d'heure, le bloc suivant n'est pas joué, les scores des blocs faits sont scellés et poussés, l'instance est détruite. La règle est mécanique ; elle ne lit aucun score.
- **Ordre de sacrifice** (du premier sacrifié au dernier) :
  1. le dépôt des activations par jeton des blocs D, C puis B ; puis celui du bloc A. Les vecteurs moyens par action et le sous-ensemble apparié du repli restent dus ;
  2. le bloc D (consigne) ;
  3. le bloc C (témoin aux doses intermédiaires) et la mesure d'intensité du témoin ;
  4. le bloc B (quatre cases du témoin) ;
  5. dans le bloc A, les doses dans l'ordre inverse du jeu : 0,75, puis 0,25, puis 0,5. La dose 1 et les textes honnêtes sous le modèle nu ne se sacrifient pas : sans eux la marche est « partielle sans seconde lecture », scellée comme telle.
- Chaque série est notée et ses scores écrits avant la suivante : une coupure laisse des séries entières. Une ligne dont une série manque est « non calculable (coupure) » à la seconde lecture.
- **Aucune relance** n'entre sous la coupure : toute relance est un retour à Lazar.
- **Avant toute destruction** (règle « récupérer ce qui est récupérable ») : inventaire des sorties (noms, tailles, empreintes), versement scellé des scores, des journaux et de ce que le lieu de dépôt accepte des activations.

## Lieu de dépôt des activations gardées, et repli

Ce qui est gardé (décision 5 de la note, adoptée avec la décision 1) :
- les activations **par jeton, à la couche 15**, en demi-précision, pour les jetons notés de chaque action : ≈ 1,18 Go par série ; 15,3 Go pour le bloc A, 18,8 Go avec B, 22,3 Go avec C, **24,7 Go** pour tout ;
- le **vecteur moyen par action** aux trois couches lues (7, 15, 23), pour toutes les séries : ≈ 330 Mo. Bras de diagnostic au sens de la décision N-026, jamais pour apprendre une sonde de production ; aucune ligne du texte neuf ne le lit.

Vingt-cinq gigaoctets ne tiennent pas commodément sur une branche du dépôt : sa pratique est le morceau de moins de 95 Mo (le sous-ensemble de 1,06 Go y est en treize morceaux) ; 24,7 Go feraient de 260 à 300 morceaux, jamais essayé. La limite du dépôt distant n'a pas été vérifiée par moi.

| lieu | ce qu'il prend | coût | ce qu'il demande |
|---|---|---|---|
| **1 (recommandé)** : pièces jointes d'une version du dépôt privé de travail | tout : treize fichiers de moins de 2 Go | aucun, si la documentation de l'hébergeur dit vrai (fichiers de moins de 2 Go, pas de plafond de volume annoncé : **à vérifier**, non relu ici) | un usage neuf du dépôt distant : **mot de Lazar** ; un essai à blanc d'un fichier de 1,9 Go depuis la session, avant la course, sans dépense |
| **2** : volume loué chez l'hébergeur du projet | tout | ordre de grandeur 1,2 EUR par mois pour 25 Go (non vérifié), récurrent | **mot de Lazar** (dépense récurrente) ; une clé d'envoi sur l'instance |
| **3 (repli, sans mot neuf)** : branche du dépôt, morceaux de moins de 95 Mo | un **sous-ensemble apparié** : une action sur dix, tirée par graine (par tâche, un rang de pas, le même pour toutes les séries de la tâche), ≈ 2,5 Go, de 26 à 30 morceaux ; plus les vecteurs moyens | aucun | rien de neuf ; la sonde ne pourra pas être réapprise sur ce sous-ensemble, la localisation jeton par jeton reste possible sur un dixième des actions |

- **Règle de repli, écrite d'avance.** Si le lieu 1 n'a pas le mot de Lazar ou si son essai à blanc échoue, et que le lieu 2 n'est pas accordé, le lieu 3 s'applique sans autre décision. Si le lieu retenu n'accepte qu'une partie, l'ordre est : les jetons des quatre cases du saboteur d'abord (bloc A), puis le témoin (B, C), puis la consigne (D).
- Le sous-ensemble apparié du lieu 3 et les vecteurs moyens sont versés **dans tous les cas** : ils servent de filet si le dépôt complet échoue en route.
- Ce qui est gardé n'est réemployé dans une mesure que par un texte contre-lu et le mot de Lazar. Noter les sondes génériques sur ces activations, ou y apprendre une sonde, est hors du texte neuf.

## Offre et étiquette

A100 SXM4 de 80 Go chez le loueur habituel (Vast.ai), au plus 1,30 USD de l'heure, au moins 16 cœurs effectifs, au moins 128 000 Mo de mémoire vive, disque d'au moins 150 Go, stockage au plus 0,08 USD de l'heure (bornes du devis de l'étape B bis, reprises sans choix neuf) ; hôte à CUDA 13.0 au moins ; étiquette `vsat-relecture-v1`, qui ne commence par l'étiquette d'aucune autre chaîne ; une seule instance, détruite par son identifiant après la poussée vérifiée (R10) ; H200 seulement sur un mot de Lazar.

## Ligne d'accord proposée (à inscrire par la session mère sur le mot de Lazar)

« calcul | Barreau 5, relecture des quatre cases par un même chemin de calcul, pour les sondes apprises sur la tâche : une carte A100 de 80 Go ; vingt et une séries relues en forçage sous état d'adaptateur imposé (quatre cases du saboteur aux quatre doses, quatre cases du témoin à la dose 1, témoin aux doses intermédiaires, témoin instruit et saboteur instruit) ; notation fermée, mesure d'intensité, activations gardées selon le lieu retenu ; seulement après le scellement du texte neuf, la fiche de code de la relecture contre-lue et le feu écrit de la mère ; aucune relance ; sortie scellée avant lecture ; arrêt et destruction par identifiant | **8,5 USD** | échéance à fixer avec la décision 2 | Lazar | GO-2026-11-19-62 (3) ; ce devis ».

Ligne d'engagement au registre des dépenses avant la première minute : attendu, pire cas, coupure, dépense antérieure sous la ligne.

## Ce que ce devis ne couvre pas

- Les heures de rédaction, de code et de contre-lecture (sessions).
- La relecture des adaptateurs de la course exploratoire (décision 7 de la note, non tranchée) et tout adaptateur neuf (plan à plusieurs adaptateurs, autre texte, autre devis).
- Le coût récurrent d'un volume loué, si le lieu 2 est retenu.

## Nœuds de ce devis (sans défaut)

1. **Ligne d'accord** : neuve, ou report de l'accord de 30 USD `GO-2026-11-10-07` (décision 2 de la note, non tranchée). Demandée **avant** l'ouverture de la première lecture, pour que la relecture ne soit pas décidée au vu d'un résultat.
2. **Coupure** : 8,5 USD, comme le mot de Lazar. Couvrir le pire cas avec tout gardé demanderait ≈ 12,5 USD : non demandé ; au pire cas, l'ordre de sacrifice s'applique.
3. **Lieu de dépôt** : lieu 1 ou 2 sur ton mot ; sinon lieu 3.
4. **Série ajoutée** (saboteur instruit) : comprise dans la ligne proposée ; à retirer d'un mot si tu ne la veux pas.
