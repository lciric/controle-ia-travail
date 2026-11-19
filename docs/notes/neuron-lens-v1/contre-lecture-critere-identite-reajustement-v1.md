# Contre-lecture du critère d'identité du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v1

- Heure (`date -u`) : 2026-11-19T10:16:58Z.
- Contre-lecteur : sous-agent neuf (règle de la contre-lecture par un agent qui n'a pas écrit la pièce, R2), modèle Fable 5.2
  (`claude-fable-5-2`). Il n'a écrit ni le critère, ni le devis, ni leurs lectures précédentes. Modèle de l'auteur : Claude Opus 5.5
  selon le mandat de la mère ; la pièce ne le dit pas (mineure 6).
- Pièce relue, classe A : `docs/notes/neuron-lens-v1/devis-reajustement/critere-identite-reajustement-lentilles-v1.md`, branche
  `claude/brave-galileo-jhp684`, commit `ca7956952c60f2bab394883ad6504e0b1ea8a9d6`, empreinte recalculée
  `1a5da7f2e5995377287cc54f0a6765953152072ed3dc9e09ae6424df0725c8dc` — égale à l'attendue et au compagnon. Les numéros de ligne
  ci-dessous sont ceux de ce fichier (47 lignes).
- Empreintes recalculées des pièces de contexte, toutes égales à leur compagnon : devis v2 `49dcbc93…` ; vérification de la différence
  entre la v1 et la v2 du devis `3cc64c86…` (c'est elle, et non la contre-lecture de la v1 `e58dc66c…`, qui pose la réserve sur la tolérance du deuxième palier, dite N-1) ;
  décision d'entrée des lentilles `6aaf54e7…` ; place des lentilles dans le billet `a6e91e25…` ; essai de `torch.save`
  `4fdec19d…`, sortie `3a18c2c2…` ; pièces du 18 novembre, `diag/20261118-164930-neuron-lens-b-beta/` (sur la branche des
  lentilles, absentes de la branche principale) : `b-beta-ajustement-R.json`
  `129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab`, `b-beta-ajustement-S.json`
  `2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297`, `b-beta-export.json`
  `17304c936792e4b79e9a47d78abf5bb6966310c36b92f387b3303b23891eedf1`.
- Lu en plus : les trois champs `diffs`, `diffs_float64`, `diffs_recopie` et les noms de clés des deux fichiers d'ajustement ; les
  **noms de clés seulement** du champ `valeurs` de l'export (aucune valeur) ; la définition des grandeurs dans notre lanceur
  (`src/controle_ia/neuron_lens/b_beta_lancer_v3.py`, l. 484-512, 895-908, 950-969) et dans les contrôles
  (`controles_b_beta_v2.py`, l. 146-162, 196-232, 407-410) ; par recherche, les lignes 97, 131, 174 et 519 du texte gelé de la tranche (seuil de
  stabilité, audit du résultat trop beau) ; au registre des accords, les lignes GO-2026-11-19-16, -27, -28 et -33.
- Non lu, selon le mandat : `docs/verdicts/`, `donnees/`, tout verdict ou résultat de l'apprentissage des sondes sur la tâche
  (étape B bis), tout fichier « consigne-privee » ou « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/`. Aucune machine, aucun
  modèle chargé, aucune dépense, aucun réseau hors `git fetch`, aucun commit, aucun fichier existant modifié. Aucun refus d'outil.

## Conclusion

**Pas avant : six corrections** (C1 à C6, texte avant et après ci-dessous). Le critère est bien écrit avant toute lentille réajustée,
ses chiffres sont justes, et il lève l'essentiel de la réserve sur la tolérance (N-1). Mais la grandeur du deuxième palier ne voit pas un déplacement
commun aux deux moitiés d'une lentille, la mention garde pourtant le mot « proche » pour la lentille, rien ne dit ce que cette mention
autorise, et aucun audit n'est écrit pour un résultat trop propre ni pour un résultat différent. Une version 2 courte suffit.

## Ce qui a été recalculé et tient

| chiffre de la pièce | recalcul du contre-lecteur | état |
|---|---|---|
| R : `31061d6c…`, 8 455 720 309 octets ; S : `aac70eef…`, 8 589 938 049 octets (l. 12, 15) | identiques dans les deux pièces | juste |
| 63 valeurs pour R, 64 pour S (l. 12, 15, 30) | R : 32 (`mid`) + 31 (`out`) ; S : 32 + 32 | juste |
| R, `diffs` contre `diffs_float64` 3,48 × 10⁻⁵ ; `diffs_recopie` contre `diffs_float64` 1,52 × 10⁻⁶ (l. 19-20) | 3,482 × 10⁻⁵ et 1,520 × 10⁻⁶ (cible `mid`, troisième couche) | juste |
| S : 5,86 × 10⁻⁵ et 3,12 × 10⁻⁶ (l. 20) | 5,856 × 10⁻⁵ (cible `out`, rang 26) et 3,118 × 10⁻⁶ | juste |
| plus petite valeur 3,53 × 10⁻³ (R), 4,11 × 10⁻³ (S) (l. 20-21) | 0,003530 et 0,004114 | juste |
| « ≈ 17 fois le plancher », « un centième du seuil de stabilité (0,10) » (l. 31-32) | 10⁻³ / 5,856 × 10⁻⁵ = 17,1 ; seuil de 0,10 au texte gelé, l. 174 | juste |
| sommes accumulées en simple précision (l. 21) | porté par la vérification du devis (`3cc64c86…`, l. 59-62) ; code voisin non relu ici | porté |
| aucune ligne de calcul à ce jour (l. 9) | aucune ligne de type « calcul » pour le réajustement au registre des accords (469 lignes lues par recherche) | juste |

Relevés du contre-lecteur, absents de la pièce : la plus grande valeur vaut 0,1114 (R) et 0,1046 (S) ; la tolérance de 10⁻³ vaut donc
0,9 % de la plus grande valeur et 28 % (R) ou 24 % (S) de la plus petite ; en valeur relative, l'écart entre chemins de calcul va
jusqu'à 2,0 × 10⁻³ (R) et 1,4 × 10⁻³ (S) ; la valeur de R la plus proche du seuil de stabilité est 0,100444 (cible `mid`, troisième
couche), à **4,4 × 10⁻⁴** de 0,10.

## Verdict par point

### 1. Fixé avant de voir, sans marge après coup ? — **Avant : oui. Sans marge : non.**
La lentille réajustée n'existe pas (aucune machine, aucune ligne de calcul) : la règle du préenregistrement avant toute lecture (R1)
est tenue pour le moment de l'écriture. Les deux seuils (égalité d'empreinte ; écart absolu maximal « au plus 10⁻³ ») et le
jugement lentille par lentille sont sans ambiguïté. Restent cinq choix ouverts après coup :
1. **Ce que le deuxième palier autorise** n'est écrit nulle part. Le troisième cas (« différente ») exige un nœud de Lazar ; le
   deuxième palier, par silence, laisse lire la lentille. La ligne 39 renvoie à un « texte de lecture v2 » qui n'existe pas dans le
   dépôt (seuls existent des brouillons de la v1 et le mandat de son rédacteur).
2. **Quelle liste de couches stables** sert ensuite. La place des lentilles dans le billet limite toute lecture par nos lentilles
   « aux couches où la stabilité tient ». Une valeur de R est à 4,4 × 10⁻⁴ du seuil : une lentille « à 10⁻³ près » peut être stable là
   où celle du 18 ne l'était pas. Prendre la liste du 18 ou la nouvelle est un choix laissé à l'auteur.
3. **Valeur non finie, manquante, ou compte différent** : rien n'est dit. Un maximum calculé naïvement ignore une valeur `nan`
   et conclurait « proche ».
4. **Le programme qui compare** n'est ni nommé ni essayé (l. 45-46 : « par programme », sans nom) ; la fonction qui donne les
   nouvelles valeurs (`_split_half_64` du lanceur) n'est pas citée.
5. **Empreinte de fichier égale mais empreinte de matrice différente** (pour R) : la ligne 27 l'exclut par raisonnement ; aucune
   règle si cela arrive.

### 2. Le plancher et la tolérance — **plancher juste et reproductible, mal rattaché ; tolérance conventionnelle, honnêtement déclarée, mais elle laisse passer une lentille déplacée.**
- **Origine.** Le plancher est l'écart, sur les **mêmes sommes**, entre la différence entre moitiés calculée en simple précision
  (`Accumulator.split_half` du code voisin, champ `diffs`) et en double précision (`_split_half_64` de notre lanceur, champ
  `diffs_float64`). Je le retrouve au chiffre près.
- **Rattachement (règle « tout chiffre renvoie à un chemin et une empreinte », R6) : non tenu.** La section dit « calcul de la session
  […] sur ces seules pièces » : ni programme, ni sortie, ni empreinte des deux pièces lues (C5).
- **Ce que ce plancher borne : rien, dans la comparaison du critère.** Le critère compare deux valeurs calculées toutes deux en
  double précision ; l'écart entre simple et double précision n'y entre pas. Le plancher donne un ordre de grandeur de la sensibilité
  de la grandeur à l'arithmétique en simple précision, pas l'écart d'un réajustement, que la pièce dit elle-même non mesuré. « ≈ 17
  fois le plancher » se lit comme un étalonnage et n'en est pas un. Les deux autres repères (un centième du seuil, « sous la plus
  petite valeur ») ne justifient pas davantage : le second dit en réalité qu'aux couches les plus stables une valeur peut bouger d'un
  quart sans sortir du palier.
- **Ce que la tolérance laisse passer.** La grandeur vaut ‖moyenne paire − moyenne impaire‖ / ‖moyenne‖. Tout déplacement Δ ajouté aux
  deux moitiés s'annule au numérateur ; seul le dénominateur bouge. Elle mesure donc si le **bruit entre moitiés** est retrouvé, pas
  si la lentille est **au même endroit**. Bornes (d la différence entre moitiés, ε = ‖Δ‖ / ‖moyenne‖) : déplacement orthogonal à la
  moyenne, écart d · (1 − 1/√(1 + ε²)) ; déplacement colinéaire, écart d · ε / (1 + ε). Essai du contre-lecteur (numpy, matrices
  simulées, hors dépôt, script en annexe) :

  | différence d'origine | déplacement commun | nouvelle valeur | écart | rangement par le critère |
  |---|---|---|---|---|
  | 0,11100 | 13 % de la norme, orthogonal | 0,11007 | 9,3 × 10⁻⁴ | « proche » |
  | 0,11100 | 25 %, orthogonal | 0,10769 | 3,3 × 10⁻³ | « différente » |
  | 0,11100 | 0,9 %, colinéaire | 0,11001 | 9,9 × 10⁻⁴ | « proche » |
  | 0,03000 | 25 %, orthogonal | 0,02910 | 9,0 × 10⁻⁴ | « proche » |
  | 0,00353 | 25 %, orthogonal | 0,00342 | 1,1 × 10⁻⁴ | « proche » |
  | 0,00353 | 5 %, colinéaire | 0,00336 | 1,7 × 10⁻⁴ | « proche » |

  **Oui : une lentille peut être « proche » selon ce critère et lire autre chose.** Une lentille déplacée à chaque couche de 13 % de
  sa norme, dans une direction commune à ses deux moitiés, passe, alors que les deux moitiés de la lentille du 18 ne diffèrent
  elles-mêmes que de 0,35 % à 11 % de cette norme. Or un effet de machine, de pilote ou de version de bibliothèque est justement un
  effet commun aux deux moitiés. La raison donnée à la ligne 34 (« 63 ou 64 nombres résument des matrices ») est vraie et trop
  faible : ce n'est pas seulement un résumé court, c'est un résumé aveugle par construction à ce qu'on cherche.
- **Ce que les pièces du 18 portent en plus, et que le critère laisse de côté.** Pour R, l'export du 18 a versé deux séries sensibles
  à la position de la lentille : l'écart maximal de chaque matrice à la lentille R publique (`valeurs.npR_notre_R`, 28 couches) et à
  l'identité (`valeurs.identite_notre_R`, 28 couches). L'export est dans les deux variantes du devis. Ces séries restent des
  conditions nécessaires, mais sur un autre axe (une ancre fixe, qui existe toujours). Pour S, rien de tel n'existe : à dire.

### 3. « Proche sur les différences entre moitiés » : ce que la mention autorise — **non écrit.**
La pièce dit ce que la mention ne dit pas (« équivalente ») ; elle ne dit pas ce qu'un texte sortant peut écrire. Phrases proposées,
à porter dans le critère (C3) ; le billet étant en anglais, la traduction suit.

**Phrase permise au deuxième palier** : « Les deux lentilles mesurées le 18 novembre ont été détruites avec la machine louée. Nous les
avons réajustées avec le même code, le même corpus et les mêmes graines sur une autre machine. Les fichiers obtenus ne sont pas
identiques à l'octet. La seule comparaison possible porte sur la différence entre les deux moitiés du corpus, couche par couche :
elle s'écarte d'au plus [écart mesuré] de celle du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³). Cette grandeur
ne voit pas un déplacement commun aux deux moitiés : nous ne savons pas si la lentille réajustée lit comme celle du 18 novembre.
Les mesures du 18 novembre [n'ont pas été refaites sur elle | ont été refaites sur elle et sont rapportées à côté]. »
(*The two lenses measured on 18 November were destroyed with the rented machine. We refitted them with the same code, corpus and
seeds on another machine. The files are not byte-identical. The only comparison left is the per-layer split-half difference, which
deviates by at most [x] from the 18 November values (tolerance fixed in advance, by convention, at 10⁻³). This quantity is blind to
any shift common to both halves, so we cannot establish that the refitted lens reads like the one measured on 18 November. The
18 November measurements [were not repeated on it | were repeated on it and are reported alongside].*)

**Phrases interdites au deuxième palier** : « Nous avons réajusté à l'identique les lentilles jugées le 18 novembre » ; « la lentille
réajustée est proche de l'originale », « équivalente », « la même à la précision numérique près » ; « le verdict “partiel” du
18 novembre vaut pour la lentille employée ici » ; toute phrase qui prête à la lentille réajustée une mesure faite sur celle du 18.
(*“We refitted the same lenses” ; “the refitted lens is close/equivalent to the original” ; “the 18 November verdict applies to the
lens used here”.*)

**Phrase permise au premier palier** : « Les fichiers d'ajustement réajustés sont identiques à l'octet à ceux du 18 novembre
(empreintes …) ; les mesures du 18 novembre décrivent ces lentilles. »

### 4. Symétrie et repli — **non tenues en l'état.**
- **Résultat trop propre (règle de symétrie, R4)** : rien. Des octets identiques après dix heures de sommes en simple précision sur
  une autre machine, ou un écart exactement nul avec des octets différents, sont des résultats trop beaux ; le texte gelé de la
  tranche avait un audit de ce genre pour la stabilité (audit A2, l. 519), le critère n'en a pas. Une empreinte de 8 Go ne s'égale
  pas par hasard, mais un programme peut comparer la référence à elle-même.
- **Résultat « différent »** : la lentille est rangée et marquée, et aucune lecture ne la lit sans nœud de Lazar (l. 38-39) : c'est
  le sens sévère, et conforme à la règle de récupération. Mais aucun audit non plus : ni table des écarts par couche, ni comparaison
  des métadonnées, des versions et du matériel. Les deux sens sont donc traités pareil seulement en ce qu'aucun n'est audité.
- **Replis (règle des gardes essayées et d'aucun repli silencieux, R5)** : le passage du premier au deuxième palier est nommé et
  porte sa mention : pas silencieux. Trois replis silencieux restent possibles : (a) une valeur non finie ou manquante avalée par le
  maximum ; (b) une lentille « différente » qui disparaît du billet sans un mot (la pièce 3 retirée en silence) ; (c) « marquée
  telle » sans dire où : la mention doit voyager avec les fichiers au lieu de rangement. Le programme de comparaison n'est essayé ni
  sur un cas sain ni sur un artefact.

### 5. La réserve N-1 est-elle levée ? — **en grande partie ; pas entièrement.**
| demande de la réserve (`3cc64c86…`, l. 74-78) | état |
|---|---|
| dire la précision réelle | fait (l. 21) |
| tolérance au-dessus du plancher que les pièces mesurent | fait (10⁻³ contre 5,86 × 10⁻⁵) |
| la déclarer conventionnelle | fait (l. 31) |
| « de préférence relative à la valeur » | non fait, sans un mot de raison |
| mention « différences entre moitiés concordantes à tant près, contenu non comparable matrice par matrice » plutôt que « lentille équivalente » | à moitié : « équivalente » a disparu, mais le sujet de la mention reste la lentille (« lentille proche ») et « non comparable matrice par matrice » n'y est pas |
| dire à Lazar que, si les octets diffèrent, l'identité ne sera pas établie | absent ; le devis v2 dit toujours « identité par les paliers 1 et 2 » (décision 1, l. 151) et le critère ne dit pas qu'il prime sur cette phrase |
La réserve disait aussi que le deuxième palier était vide à 10⁻⁶. Il ne l'est plus ; il est devenu facile (point 2).

### 6. Un choix qui arrange l'auteur ? — **trois choix penchent du même côté, aucun n'est caché.**
- La tolérance passe de 10⁻⁶ à 10⁻³ : la réserve demandait de monter au-dessus du plancher, pas de combien ; 17 fois, arrondi à une
  puissance de dix, en valeur absolue alors que la réserve préférait une valeur relative.
- La mention garde « lentille proche », le mot le plus favorable que la réserve n'interdisait pas à la lettre.
- La grandeur retenue est la seule disponible pour S, mais pour R deux séries plus exigeantes sont dans les pièces et ne sont pas
  prises (point 2).
- Enjeu : le deuxième palier laisse la lentille entrer dans la pièce 3 du billet (la lecture des sondes avec nos lentilles) sans
  nœud propre à l'identité ; le troisième cas l'arrête. La largeur du palier pèse donc sur la suite du chantier de l'auteur. Enfin, les écarts sont calculés « dans la session » de l'auteur (l. 45-46).
Rien de cela n'est une faute : chaque choix est déclaré conventionnel. Les corrections C1 à C4 retirent l'enjeu (la mention dit
moins, elle autorise moins, le calcul est refait hors de la session de l'auteur) ; la tolérance de 10⁻³ peut alors rester.

## Corrections (texte avant et après)

**C1 — Mention et définition du deuxième palier (l. 29-30).**
- Avant : « 2. **Palier 2 — « lentille proche à 10⁻³ près sur les différences entre moitiés »** (sinon) : écart absolu maximal entre
  les nouvelles `diffs_float64` et celles du 18, sur toutes les couches et cibles (63 valeurs pour R, 64 pour S), **au plus 10⁻³**. »
- Après : « 2. **Palier 2 — « différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables »**
  (sinon) : écart absolu maximal, en double précision et sans arrondi, entre les nouvelles `diffs_float64` (fonction
  `_split_half_64` de notre lanceur, inchangée, calculée sur la machine à la fin de l'ajustement) et celles du 18
  (`b-beta-ajustement-R.json`, `129c43b0…` ; `b-beta-ajustement-S.json`, `2dce646e…`), sur toutes les couches et cibles (R : 32
  `mid` et 31 `out` ; S : 32 et 32), **au plus 10⁻³**. Préalables, tous exigés ; un seul manqué → « non comparable », rangée et
  traitée comme « différente » : mêmes comptes de valeurs par cible ; toutes les valeurs finies ; `meta` égal champ par champ à
  celui du 18 ; `n_docs` [466, 466] ; `next_doc` 932 ; mêmes commits du code voisin et de la fonction de calcul. Sont rapportés
  aussi, sans critère : l'écart relatif maximal, l'écart sur `diffs` (la valeur lue pour les seuils de la tranche), et toute
  valeur qui change de côté du seuil de stabilité de 0,10. »

**C2 — Ce que la grandeur ne voit pas, et les deux séries de R (l. 34-37).**
- Avant : « **Condition nécessaire, pas suffisante** : 63 ou 64 nombres résument des matrices de 4 096 × 4 096 ; la mention ne dit pas
  « équivalente », elle dit « proche sur les différences entre moitiés ». »
- Après : « **Condition nécessaire, pas suffisante, et aveugle par construction** : la grandeur vaut ‖moyenne paire − moyenne
  impaire‖ / ‖moyenne‖ ; tout déplacement commun aux deux moitiés s'annule au numérateur. Elle dit si le bruit entre moitiés est
  retrouvé, pas si la lentille est au même endroit : une lentille déplacée de 13 % de sa norme à chaque couche, dans une direction
  commune aux deux moitiés, passe ce palier. La mention ne dit ni « équivalente », ni « proche », ni « même lentille ». **Pour R**,
  sont comparés en plus aux valeurs du 18 (`b-beta-export.json`, `17304c93…`, champ `valeurs`) l'écart maximal de chaque
  matrice à la lentille R publique (`npR_notre_R`, 28 couches) et à l'identité (`identite_notre_R`, 28 couches) : [au choix de
  l'auteur, fixé avant le scellement : condition nécessaire de plus, avec une tolérance conventionnelle déclarée ; ou rapportés sans
  critère]. **Pour S**, aucune grandeur sensible à la position n'existe dans les pièces du 18. »
  Le minimum pour sceller est « rapportés sans critère » ; une tolérance fixée d'avance vaut mieux.

**C3 — Section à ajouter : « Ce que chaque mention autorise ».**
- Avant : rien ; l. 38-39, « (le texte de lecture v2 le dit de son côté) ».
- Après : « **Seul le palier 1 établit l'identité** ; cette phrase prime sur « identité par les paliers 1 et 2 » du devis v2
  (décision 1). *Palier 1* : les mesures et le verdict du 18 décrivent la lentille rangée ; phrase permise : […]. *Palier 2* :
  l'identité n'est pas établie et le verdict du 18 ne se transporte pas ; Lazar en est averti en ces termes avant tout usage ; phrase
  permise : […] ; phrases interdites : […] (point 3 de la contre-lecture) ; en variante B (la course rejouée), les mesures qui décrivent la lentille
  rangée sont celles de la seconde course, lues par un lecteur neuf ; en variante A (ajustement seul), elle n'a aucune mesure propre, et le billet le
  dit ; une couche n'est tenue pour stable que si sa différence entre moitiés (`diffs`) est au plus 0,10 **dans les deux
  ajustements**. *Au-delà, ou « non comparable »* : rangée, marquée, aucune lecture sans nœud de Lazar. Dans tous les cas : tout
  usage dans une lecture passe par un texte de lecture neuf, contre-lu, qui recopie la mention et l'écart mesuré, et par le mot de
  Lazar (GO-2026-11-19-33) ; le billet dit le palier obtenu, quel qu'il soit, et, si la lentille n'est pas lue, le dit en une
  phrase ; la mention est écrite dans un fichier compagnon au lieu de rangement et à l'inventaire. »
  La parenthèse de la ligne 39 est retirée : ce texte n'existe pas encore.

**C4 — Section à ajouter : « Audit, le même dans les deux sens », et essais du programme.**
- Avant : rien.
- Après : « **Déclencheurs** : (i) palier 1 obtenu ; (ii) écart maximal exactement nul avec des octets différents ; (iii) « lentille
  différente » ; (iv) « non comparable » ; (v) pour R, empreinte du fichier égale et une empreinte de matrice ou d'export différente
  (anomalie : palier 1 suspendu). **Audit, par programme, sans lire aucune mesure de la course** : provenance des deux côtés de la
  comparaison (l'empreinte neuve vient du fichier de la course neuve — identifiant, heure, taille — et est relue au lieu de rangement
  après la copie ; la référence est lue dans la pièce du 18 par son empreinte ; les deux ne sortent pas du même fichier) ; table des
  différences de `meta`, des commits, des versions de bibliothèques, du pilote et du modèle de carte ; table des écarts par couche et
  par cible, avec leur signe. L'audit est versé scellé avec le verdict d'identité ; un contrôle manqué suspend la mention et ouvre
  un nœud de Lazar. Aucune relance pour obtenir un autre palier sans devis neuf et mot de Lazar. **Programme** : nommé, versionné,
  scellé et contre-lu avant la création, essayé sur un cas sain (les pièces du 18 contre elles-mêmes : écart nul, déclencheur (ii))
  et sur quatre artefacts (une valeur déplacée de 2 × 10⁻³ → « différente » ; une valeur `nan` → « non comparable » ; 62 valeurs au
  lieu de 63 → « non comparable » ; un champ de `meta` changé → « non comparable »). »

**C5 — Rattachement du plancher et libellé de la tolérance (l. 17-22, 31-33).**
- Avant (l. 17) : « ## Plancher mesuré (calcul de la session, 2026-11-19, sur ces seules pièces) ».
- Après : « ## Écart entre chemins de calcul (programme `…-v1.py`, empreinte … ; sortie …, empreinte … ; pièces
  `b-beta-ajustement-R.json` `129c43b0…` et `b-beta-ajustement-S.json` `2dce646e…`) » ; et, en fin de section : « Cet écart
  est celui du calcul final en simple ou en double précision sur les mêmes sommes. Le critère compare deux valeurs en double
  précision : cet écart n'y entre pas. Il ne borne l'écart d'un réajustement ni par le bas ni par le haut. »
- Avant (l. 31-33) : « Tolérance **conventionnelle, déclarée telle** : ≈ 17 fois le plancher mesuré entre chemins de calcul
  (5,86 × 10⁻⁵), un centième du seuil de stabilité de la tranche (0,10), sous la plus petite valeur (3,5 × 10⁻³). Aucune pièce ne
  mesure l'écart d'un réajustement. »
- Après : « Tolérance **conventionnelle, déclarée telle**, absolue [raison de ne pas la prendre relative, en une phrase]. Repères, qui
  ne la justifient pas : ≈ 17 fois le plus grand écart entre chemins de calcul (5,86 × 10⁻⁵) ; un centième du seuil de stabilité
  (0,10) ; 0,9 % de la plus grande valeur (0,111) ; 28 % (R) et 24 % (S) de la plus petite : aux couches les plus stables, ce palier
  ne distingue presque rien. Elle dépasse la distance au seuil de stabilité de la valeur de R la plus proche (0,10044, cible `mid`,
  troisième couche, à 4,4 × 10⁻⁴ de 0,10). Aucune pièce ne mesure l'écart d'un réajustement. »

**C6 — Qui applique (l. 45-47).**
- Avant : « Le calcul des empreintes et des écarts est fait **par programme** sur la machine (empreintes) et dans la session (écarts
  sur les pièces versées), avant toute lecture d'une mesure de la nouvelle course ; […] »
- Après : « Les empreintes sont calculées par programme sur la machine. Les écarts sont calculés par le programme scellé de C4, sur
  les pièces versées, **par la mère ou par un agent neuf**, et non par la session des lentilles, avant toute lecture d'une mesure de
  la nouvelle course ; […] »

## Remarques mineures
1. **Nom du fichier et égalité d'octets (l. 25-27).** La pièce écrit « `torch.save` écrit les mêmes octets pour le même contenu » ;
   l'essai cité tient aussi le **nom du fichier** constant (`r-llama.tmp` aux deux écritures) et le devis disait « au même nom de
   fichier ». Rétablir ces mots et exiger le même nom qu'au 18 dans la course neuve. À vérifier par l'auteur : je crois que le nom
   entre dans les octets de l'archive écrite ; non essayé ici (`torch` absent de mon environnement).
2. **Reprise sur sauvegarde (l. 40).** Si l'empreinte est égale après une reprise, les octets sont les mêmes ; lui refuser le
   palier 1 fait écrire une mention fausse. Proposé : « palier 1 prononcé, reprise notée, audit de C4 ».
3. **Ligne 27**, « Pour R, alors, les empreintes par couche […] sont égales elles aussi » : c'est une prédiction ; la règle si elle
   manque est au déclencheur (v) de C4.
4. **Lentille absente** (course arrêtée après R) : écrire « S non réajustée », R jugée seule.
5. **Commentaire du lanceur** (`b_beta_lancer_v3.py`, l. 499 et 505, « jamais lue pour un seuil », « pour mémoire seulement ») : il
   devient faux ; à corriger dans la version neuve du lanceur.
6. **En-tête** : dire le modèle de l'auteur ; la version corrigée prend un nom neuf (v2), la v1 reste archivée (règle des versions
   dans les noms, R12).
7. **Chemin des références (l. 11)** : `diag/20261118-164930-neuron-lens-b-beta/` n'est pas sur la branche principale ; donner la
   branche et le commit.

## Annexe — essai du contre-lecteur (hors dépôt, bloc-notes ; numpy seul)
```python
import numpy as np
rng = np.random.default_rng(np.random.SeedSequence(20261119)); n0 = n1 = 466; dim = 384
def diff(a, b): return np.linalg.norm(a / n0 - b / n1) / np.linalg.norm((a + b) / (n0 + n1))   # formule de _split_half_64
for cible in (0.111, 0.030, 0.00353):
    M = rng.standard_normal((dim, dim)); M /= np.linalg.norm(M)
    B = rng.standard_normal((dim, dim)); B *= (cible / 2) / np.linalg.norm(B)
    me, mo = M + B, M - B; d0 = diff(me * n0, mo * n1)
    for eps, genre in ((0.13, "orthogonal"), (0.25, "orthogonal"), (0.009, "colineaire"), (0.05, "colineaire")):
        if genre == "orthogonal":
            D = rng.standard_normal((dim, dim)); D -= (D * M).sum() * M; D *= eps / np.linalg.norm(D)
        else:
            D = eps * M
        print(cible, genre, eps, d0, diff((me + D) * n0, (mo + D) * n1))
```
Le plancher a été recalculé en lisant les trois champs des deux pièces et en prenant le maximum, sur toutes les couches et cibles, de
la valeur absolue de la différence au champ `diffs_float64`.
