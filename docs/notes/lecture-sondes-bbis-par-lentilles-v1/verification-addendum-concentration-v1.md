# Vérification de l'addendum « concentration » corrigé, et contre-lecture de la garde d'égalité au vingtième rang — v1

- **Contre-lecteur** : le même que pour le brouillon (rapport `715ddfa7…`), agent sous-agent de la session mère, modèle servi
  **Opus 5.5** (`claude-opus-5-5`) ; il n'a écrit ni le texte scellé, ni l'addendum, ni ses corrections, ni la garde, ni le code ; il
  ne sera ni développeur, ni opérateur, ni lecteur. Le rédacteur des corrections est sur Fable 5.2.
- **Date (UTC)** : 2026-11-19 ; lecture à partir de 14:07:22 ; programmes joués de 14:13 à 14:24 ; rapport écrit ensuite.
- **Pièces vérifiées** (branche `claude/brave-galileo-jhp684`, commit `209cf169d`, lues dans un arbre détaché du bloc-notes ;
  empreintes recalculées, égales au mandat et aux compagnons) :
  - version corrigée, nom final : `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
    `924d02989412700d6241d0e3663fd4914e462bc68560df345b8cdc1889f2813c` (« la version ») ;
  - brouillon contre-lu, renommé : `…-addendum-concentration-v1-brouillon1.md`, `0a862760…`, inchangé d'un octet (« le brouillon ») ;
  - brouillon 3 de la version 2 du texte : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon3.md`,
    `1bfac4672e27e07ff8680e7be70c28f79dd921d0eccdc00ce873b8af467c47c7` ;
  - appui de la garde : `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/frequence_egalite_vingtieme_rang_v1.py`
    `b1d0d47439be89d7380aa81c08f08ae83b0f92053b3dbefda27810e6be97d5b2`, et sa sortie
    `sortie-frequence-egalite-vingtieme-rang-v1.txt` `26f4abba8e5816165b5cb01bdba969ff90af570791578967ac6c7d666cc02e74`.
- **Référence** : ma contre-lecture du brouillon, `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-addendum-concentration-v1.md`,
  `715ddfa7fb65352126f21c773e9f4ad9359d25cc5a57d1a2816d4018111bf106`, et le code préparé du développeur (commit `e2e24cac`), relu pour
  la garde (`statistiques_v1.py` : listes, attendu des familles, pôles).
- **Pièces de cette vérification** : dossier `docs/notes/lecture-sondes-bbis-par-lentilles-v1/verification-addendum-concentration-outils-v1/`,
  à côté de ce rapport (programmes, sorties, commandes et entropie ; chaque fichier scellé avec son compagnon ; liste au § 7).

## Conclusion

**Scellable après ces couples exacts** : les couples obligatoires G1 à G8 (§ 6), et le mot de Lazar sur la garde, qui reste un point
d'écart neuf (§ 9, point 7, de la version). Les couples H1 et H2 sont facultatifs. Condition de nommage, comme la première fois : la
version `924d0298…`, déjà scellée comme candidate sous le nom final, garde un nom de brouillon (par exemple
`…-addendum-concentration-v1-brouillon2.md`, même empreinte) ; la version, couples appliqués, prend le nom final.

**Avis sur la garde, à porter à Lazar** (cinq lignes) :

1. La garde est saine : ses deux bornes encadrent toute valeur p qu'un départage donnerait, et un libellé égal aux deux n'en dépend pas ; aucun contre-exemple.
2. Mais la borne haute compte toute nulle marquée, même hors de portée : arrêts sans objet possibles ; des bornes exactes (G1) les ôtent pour quelques lignes de code.
3. Deux trous : la valeur p écrite et l'attendu des familles dépendent encore du tri ; les listes de dix des pôles ne sont pas gardées (G1, G3 à G5).
4. Le chiffre est du bon ordre, un peu bas : 9 × 10⁻⁶ par liste (modèle gaussien ; 8 × 10⁻⁶ à 1,5 × 10⁻⁵), 1,6 à 2,9 égalités attendues ; lentille réelle : inconnu, 10⁻⁶ à 10⁻⁴.
5. Options 1 et 2 honnêtes à deux chiffres près (l'option 1 peut aussi changer un libellé sans le dire) ; avis : option 3 avec bornes exactes, arrêt de l'ordre de 1 %.

## 1. Les couples de la contre-lecture : appliqués à la lettre, rien d'autre de changé hors de la garde et du § 12

- **Par programme** (`differentiel_version_contre_lecteur.py`) : les huit couples sont extraits du § 9 de mon rapport `715ddfa7…`. Chaque
  texte « avant » paraît une fois dans le brouillon, et chaque texte « après » paraît mot pour mot dans la version. Le brouillon, couples
  appliqués, est ensuite comparé à la version. Le différentiel restant (183 lignes, sortie `diff-brouillon1-couples-vers-version.txt`)
  tient en cinq blocs, tous annoncés :
  - la puce « Statut » de l'en-tête (12 lignes) ;
  - EC-6, la garde (90 lignes, après EC-5) ;
  - la ligne 7 du § 4 (3 lignes) ;
  - le point 7 du § 9 (23 lignes) ;
  - le § 12 neuf (47 lignes).

  Rien d'autre n'a changé.
- **F1** est juste : le crochet [ρ²(c² − 1)/2 + ρ]/M est l'écart relatif du z d'une nulle au seuil, et l'écart relatif de la part vaut
  environ c·h fois plus (mon § 2.1, refait). La phrase suivante, sur la fenêtre anti-conservatrice, parle bien de la part.
- **F2** est juste : un mélange de lois binomiales de taille n n'est fixé que par les n premiers moments de sa loi de mélange. « Si »
  est vrai, « seulement si » ne l'est pas.
- **F3** est juste, compte compris : douze calibrations portent des libellés, et 12 × 1,865 × 10⁻⁴ = 2,24 × 10⁻³. Avec le repli par
  direction, le nul partagé s'ajoute (3 couches × 2 lentilles × 3 nuls) : 18 × 1,865 × 10⁻⁴ = 3,36 × 10⁻³, écrit 3,4 × 10⁻³.
- **§ 12** : la table des changements et les raisons de prendre F1 à F3 sont exactes. Les points ouverts 1 à 6 gardent leurs mots du
  brouillon, et le § 12 en donne l'état après la contre-lecture : c'est acceptable.

## 2. La garde d'égalité au vingtième rang (EC-6) : contre-lecture entière

### 2.1 La règle à trois étages

- **Le critère est exact.** L'ensemble des vingt premiers est défini sans ambiguïté si et seulement si la vingtième valeur est
  strictement plus grande que la vingt-et-unième. Une égalité plus haut ne change que l'ordre d'affichage. Le rang du jeton de début est
  déjà calculé sans dépendre d'un départage (`statistiques_v1.jeton_de_debut` : 1 + nombre de scores strictement plus grands).
- **Direction lue, arrêt.** C'est juste : la liste montrée, la part, les familles et les comparaisons de v dépendraient du tri. C'est
  aussi ce qui rend S(v) unique, condition des bornes de (ii).
- **Direction nulle, marque et bornes.** La seule statistique de la nulle qui dépend des vingt premiers est son S (part ou compte de
  famille). Le quantile des M − 1 autres n'emploie aucune liste. La valeur p de v est (1 + nombre de nulles avec S(u_j) ≥ S(v))/(M + 1) :
  - une nulle non marquée compte ou ne compte pas, quel que soit le départage ;
  - une nulle marquée compte 0 ou 1.

  Donc tout départage donne une valeur p entre p_bas (aucune marquée ne compte) et p_bas + (nombre de marquées)/(M + 1) (toutes
  comptent). Les libellés vont de « concentrée » à « intermédiaire » puis à « non distincte du nul » quand l'une ou l'autre valeur p
  croît, et « sur-représentée » cesse quand l'une croît. Ils sont donc monotones dans chaque coordonnée. Le libellé de tout point du
  pavé des deux nuls est compris entre celui du coin bas et celui du coin haut ; s'ils sont égaux, il est fixé. **La règle est saine.**
- **Témoin, compté et écrit.** C'est juste : le compte de calibration ne lit que la concentration. Le texte sous-entend la liste par
  score, la seule qu'ont les témoins ; c'est suffisant.

### 2.2 Les bornes encadrent-elles tout départage ? Oui ; mais la borne haute est trop large

- **Encadrement** : aucun contre-exemple n'est possible, par l'argument du § 2.1. Énumération sur 4 000 jouets (14 jetons, cinq
  premiers, 9 nulles, scores arrondis pour forcer les égalités ; `bornes_departage_contre_lecteur.py`, sortie `e86b9036…`) : la
  valeur p de tous les départages tombe entre les deux bornes dans tous les cas (0 violation).
- **Contre-exemple à « la lecture ne s'arrête que si l'égalité compte »** (option 3, § 9). Prenons :
  - v a une part de 0,90 ;
  - une seule nulle non marquée a une part ≥ 0,90, donc p_bas = 2/2 001 ≤ 0,001 ;
  - une nulle marquée a une part de 0,50 ou de 0,55 selon le départage.

  La borne de la version donne p_haut = 3/2 001 > 0,001. Si v est à p ≤ 0,01 sous le nul des signes, son libellé passe de « concentrée »
  à « intermédiaire » entre les deux bornes, et le calcul s'arrête. Pourtant la valeur p vaut 2/2 001 sous tous les départages. Dans
  mes jouets, 2 248 franchissements de seuil par les bornes de la version sur 3 906 sont de ce type, sans objet. Les jouets forcent les
  égalités : ce n'est pas la fréquence de la lecture réelle. Mais une direction lue très concentrée, à une ou deux nulles du seuil, est
  justement le cas que la lecture cherche.
- **Correction (G1)** : pour chaque nulle marquée, calculer S_min et S_max, la plus petite et la plus grande valeur de S quand les
  places laissées par les jetons strictement au-dessus du vingtième sont données de toutes les façons aux jetons de même score.
  - Pour la part, avec A⁺ jetons au-dessus de leur quantile parmi les jetons strictement au-dessus, r places, un groupe de G jetons à
    égalité dont g⁺ sont au-dessus de leur quantile : S_min = (A⁺ + max(0, r − G + g⁺))/20 et S_max = (A⁺ + min(r, g⁺))/20.
  - Pour une famille, de même avec l'appartenance.

  Les bornes deviennent la plus petite et la plus grande valeur p atteinte (vérifié : 0 écart sur les 4 000 jouets). Le calcul ne
  s'arrête plus que si un départage change vraiment un libellé. Coût : quelques lignes, appelées seulement pour les nulles marquées.

### 2.3 Deux trous

- **Valeur p écrite et attendu des familles.** La version dit que le code rend « à côté de p » deux bornes, sans dire ce qu'est p
  quand une nulle est marquée : le code la calcule avec le départage de `topk`, ce qui est le choix silencieux que la garde veut
  ôter. De même, l'« attendu sous le nul » de la phrase gelée des familles est la moyenne des comptes des M nulles
  (`statistiques_v1.py`, l. 151), marquées comprises. G1 écrit p_haut comme valeur p et calcule l'attendu sur les nulles non marquées.
- **Listes de dix des pôles.** Deux listes de dix entrent dans les tables et dans la phrase gelée des pôles :
  - les dix pôles par cosinus (`signes.topk(10)`, parmi 57 344) ;
  - les dix premiers jetons de la lecture de chaque pôle.

  La version les déclare « non concernés » (« aucun n'emploie les vingt premiers jetons »), ce qui est vrai à la lettre, mais le tri y
  choisit en silence. G3, G4 et G5 les mettent sous (i), égalité lue au dixième rang. Fréquence dans le même modèle : 4,6 × 10⁻⁶ par
  liste, quelque 440 listes, soit environ 0,2 % par lecture.

### 2.4 Le chiffre d'appui, refait

- **Par mon propre programme**, à entropie neuve (`egalite_rang_k_contre_lecteur.py`, sortie `fe7274f1…`). Je ne compte pas
  d'événements rares :
  - je tire seulement le vingt-et-unième score y (représentation de Rényi, exacte) ;
  - la probabilité d'égalité sachant y est exacte : 1 − (survie(e)/survie(y))^20, e étant le bord supérieur de la cellule d'arrondi de y.

  Contrôle au pas 10⁻³ contre un tirage direct : 0,0353 ± 0,0034 contre 0,0366.

  Résultats, par liste de vingt :

  | modèle (89 498 scores gaussiens, simple précision) | par liste | sur ≈ 195 000 listes | au moins une |
  |---|---|---|---|
  | scores centrés réduits | **9,0 × 10⁻⁶** (± 3 × 10⁻⁹) | 1,75 | 0,83 |
  | centrés, écart type de 1 à 2 (place dans la puissance de deux) | 8,3 × 10⁻⁶ à 1,5 × 10⁻⁵ | 1,6 à 2,9 | 0,80 à 0,95 |
  | moyenne à dix écarts types | 3,6 × 10⁻⁵ | 7,0 | ≈ 1 |
  | moyenne à cent écarts types | 2,9 × 10⁻⁴ | 56 | 1 |

  Le comptage direct, comme l'auteur, sur 40 000 000 de directions par ligne (`egalite_comptage_direct_contre_lecteur.py`, sortie
  `56bb8d00…`), rend 9,8 ± 0,5 × 10⁻⁶, 3,67 ± 0,10 × 10⁻⁵ et 2,857 ± 0,027 × 10⁻⁴ : il confirme la formule. Les 28 égalités de l'auteur
  sur 4 000 000 (7,0 × 10⁻⁶) sont une fluctuation basse d'une attente de 36. **Le chiffre est du bon ordre, un peu bas** (G6, G7, G8).
- **Ce qu'il vaut pour la lentille réelle** : un ordre de grandeur seulement. Dans tout modèle, la probabilité par liste vaut à peu près
  10 × (x·h(x)) × (pas d'arrondi en x / x), x étant le vingtième score et h le hasard de la loi des scores en x.
  - Pour la loi normale, x·h ≈ 13 et pas/x ≈ 6 × 10⁻⁸ à 1,2 × 10⁻⁷.
  - Une queue plus lourde (normes de lignes inégales) baisse x·h.
  - Un décalage commun des scores (composante commune des lignes de sortie) monte pas/x devant l'écart entre rangs : quatre fois à dix
    écarts types, trente-deux fois à cent.
  - Deux jetons gardés de même ligne de sortie ajoutent environ 1,1 × 10⁻⁵ par liste et par paire.

  Fourchette plausible : 10⁻⁶ à 10⁻⁴ par liste, soit de 0,2 à 20 égalités sur le calcul. Sous l'option 3, les marques peuvent être
  nombreuses sans effet ; les arrêts restent rares (de l'ordre de 1 % dans le modèle gaussien, jusqu'à quelques pour cent au haut de la
  fourchette). Compter au montage les lignes de sortie identiques (H2) ôte la part structurelle de l'inconnu.

### 2.5 Les options soumises à Lazar

- **Option 1** (arrêt sur la direction lue seule) : décrite honnêtement, à deux choses près. Son chiffre est donné « par direction
  lue » : c'est par liste, et il y a quelque neuf cents listes. Et une égalité sur une nulle, tranchée en silence, peut aussi changer un
  libellé, sans que rien ne l'écrive (G7).
- **Option 2** (arrêt sur toute direction) : honnête ; la probabilité d'un arrêt est de 0,8 à 0,95 dans le modèle, non « 0,7 ou plus »
  (G8). La conclusion (« la lecture s'arrêterait donc le plus souvent ») en sort renforcée.
- **Option 3** : sa phrase « la lecture ne s'arrête que si l'égalité compte » est fausse avec la borne haute de la version (§ 2.2), et
  vraie avec G1.
- **Deux variantes manquent**, que Lazar peut vouloir voir (H1) :
  - (a) la règle de départage fixe de la version 2, dès maintenant : jamais d'arrêt, valeurs p valides ; mais un second écart, et une
    préférence pour les petits identifiants ;
  - (b) au lieu de l'arrêt, « non calculable » pour le seul libellé ou la seule direction en cause, comme le texte le fait pour une
    calibration hors de ses bornes.

### 2.6 Codable sans choix, essayable (R5)

Avec G1 à G5, la garde est codable sans choix : listes nommées, égalité exacte en simple précision, S_min et S_max par formule, p
écrit, attendu, messages et lignes d'arrêt nommés. Les essais de la version couvrent cas sain et artefact à chaque étage. G2 les
accorde aux bornes exactes : nulle marquée hors de portée, pas d'arrêt ; S_min et S_max contre une énumération. G5 ajoute l'essai des
listes de dix. Deux essais restent souhaitables, sans être exigés : plusieurs nulles marquées, et une égalité sur trois valeurs à
cheval sur le vingtième rang.

## 3. Brouillon 3 de la version 2 du texte

- **Les quatre endroits sont corrigés, mot pour mot de l'addendum** :
  - « Métrique », point 6, concentration (C5 et les deux arrêts compris) ;
  - « Métrique », point 6, part ;
  - « Plan », point 6, calibration, en ses deux passages.

  **Rien ne manque ailleurs.** J'ai cherché « m_t et s_t », « quantile 0,99 », « négligeable », « loi exacte » et « u_j » dans tout le
  brouillon :
  - le recouvrement et son p jugent chaque nulle sur elle seule ;
  - la corrélation et son quantile ne portent aucun p ;
  - les résumés gardés sont ceux des M ;
  - notre S passe par le point 6 ;
  - les deux restes (récit des contre-lectures, table d'historique) sont de l'histoire.
- **La règle de départage** (score décroissant, puis identifiant de jeton croissant) **ne change pas la validité des valeurs p** : c'est
  une fonction fixe des scores, appliquée de même à v, aux nulles et aux témoins, donc l'échangeabilité sous le nul est gardée. **Mais
  elle n'est pas neutre envers les familles.** À score égal, elle garde toujours le plus petit identifiant. Dans les vocabulaires à
  octets du type de celui de Llama 3, les plus petits identifiants sont les caractères seuls ; s'il s'y trouve, comme c'est probable, les
  chiffres seuls et « $ » (à vérifier sur le tokeniseur), la règle compte, dans l'égalité, un jeton de famille plutôt qu'un autre, pour v
  comme pour les nulles. Le taux de « sur-représentée » à tort n'en change pas, mais, pour une direction donnée, une égalité tranchée
  ainsi pousse vers « sur-représentée ». C'est minime (≈ 10⁻⁵ par liste). La phrase « elle ne penche vers aucun libellé » est donc à
  reprendre (« elle ne change pas la validité des valeurs p »). Une permutation fixe des identifiants, tirée par graine, serait neutre.
- **Ce qui bloquerait son scellement plus tard** :
  - (1) le mot de Lazar pour la version 2 : celui de GO-2026-11-19-47 est donné pour la version 1, le brouillon le dit ;
  - (2) l'empreinte de l'addendum scellé, à reporter ;
  - (3) les listes de dix (pôles, par la lentille publique et par notre R ; garde de la fonction de lecture, que sa tolérance couvre
    déjà) : la règle ne les couvre pas, le brouillon le dit ;
  - (4) les essais du code (statistique corrigée, ses deux arrêts, règle de départage), absents ;
  - (5) l'ordre de la ligne de registre de l'addendum par rapport à celles de la version 2 ;
  - (6) la phrase sur le penchant, ci-dessus.

  Son paragraphe « Lien avec la v1 » reste vrai avec G1.

## 4. Règles

- **Préenregistrement scellé avant toute lecture (R1)** : aucune donnée réelle, ni par le rédacteur ni par moi ; la garde attend le mot
  de Lazar avant le scellement, comme la version le dit. Tenue.
- **Symétrie des audits (R4)** : le chiffre d'appui est refait par deux méthodes à moi, à entropie neuve ; les bornes sont éprouvées sur
  des jouets énumérés ; l'écart relevé (borne trop large) va dans le sens qui arrête, mais il est corrigé de même. Tenue.
- **Gardes essayées sur un cas sain et sur un artefact (R5)** : tenue, avec G2 et G5.
- **Chiffres de l'état de l'art (R7)** : aucun. Les chiffres renvoient à des fichiers et à des empreintes.
- **Versions dans les noms (R12)** : le brouillon a bien été renommé sans changer un octet, et la pièce d'appui a un nom neuf. Pour la
  suite, voir la condition de nommage de la conclusion.

## 5. Ce que j'ai fait, lu et produit

- **Actions** :
  - un `git fetch` de la branche ;
  - un arbre détaché du commit `209cf169d` dans le bloc-notes ;
  - des programmes au processeur, sur données synthétiques.

  Aucun modèle chargé, aucune machine, aucune dépense, aucun commit, aucun push. Aucun refus d'outil.
- **Lu** : la version en entier, par différentiel et par lecture de EC-6, du § 4 et des § 9 et 12 ; le brouillon ; la pièce d'appui et
  sa sortie ; du brouillon 3 de la version 2, l'en-tête des changements, « Métrique » et la calibration, plus une recherche de mots dans
  tout le texte ; du code préparé, `statistiques_v1.py` (listes, attendu, pôles).

  **Jamais ouverts** : aucune sonde, aucun score, aucune table, aucune lecture, aucun verdict, rien sous `docs/verdicts/`, aucune
  branche de données ou de calcul, aucun fichier dont le nom porte « consigne-privee » ou « conception-ii-b ». Je n'ai pas ouvert de
  tokeniseur : les deux du dépôt sont des jouets, et l'un se trouve dans un dossier que le texte met parmi les « jamais ouverts ».

## 6. Couples exacts

Texte « avant » copié de la version corrigée (`924d0298…`), retours à la ligne compris ; chacun y paraît une seule fois, et tous s'appliquent ensemble (vérifié par programme, `couples_verification_contre_lecteur.py`). G1 à G8 sont obligatoires ; H1 et H2 sont facultatifs.

**G1** (obligatoire : EC-6 (ii) : bornes exactes au lieu de la borne haute qui compte toute direction marquée ; valeur p écrite et attendu des familles définis quand une direction est marquée (sinon le tri choisit encore en silence)).

Avant :

```
> égalité au vingtième rang n'arrête pas à elle seule ; la direction nulle est **marquée**. Pour chaque statistique S qui dépend des
> vingt premiers jetons (part au-dessus du nul ; compte de chaque famille), le code rend, à côté de p, deux bornes :
> p_bas = (1 + #{j non marquée : S(u_j) ≥ S(v)}) / (M + 1) et p_haut = p_bas + (nombre de directions marquées) / (M + 1). Le libellé
```

Après :

```
> égalité au vingtième rang n'arrête pas à elle seule ; la direction nulle est **marquée**. Pour une direction marquée u_j et une
> statistique S qui dépend des vingt premiers jetons (part au-dessus du nul ; compte de chaque famille), S_min(u_j) et S_max(u_j)
> sont la plus petite et la plus grande valeur de S quand les places des vingt premiers que laissent les jetons de score strictement
> plus grand que le vingtième sont données, de toutes les façons possibles, aux jetons de score égal au vingtième. Le code rend, pour
> chaque S, deux bornes, sur les directions du même nul et de la même lentille :
> p_bas = (1 + #{j non marquée : S(u_j) ≥ S(v)} + #{j marquée : S_min(u_j) ≥ S(v)}) / (M + 1) et
> p_haut = (1 + #{j non marquée : S(u_j) ≥ S(v)} + #{j marquée : S_max(u_j) ≥ S(v)}) / (M + 1) : la plus petite et la plus grande
> valeur p que donnerait un départage. Quand une direction est marquée, la valeur p écrite dans les tables et les phrases est p_haut
> (sens conservateur), p_bas écrit à côté, et l'attendu sous le nul d'une famille est la moyenne sur les seules directions non
> marquées. Le libellé
```

**G2** (obligatoire : EC-5 de la garde, essais : les essais des directions nulles suivent G1).

Avant :

```
- **direction nulle, cas sain** : une direction nulle à égalité au vingtième rang, libellé égal aux deux bornes : pas d'arrêt, une
  direction marquée écrite, p_haut − p_bas = 1/(M + 1) ;
- **direction nulle, artefact** : jouet à M = 99 où, pour une famille, p_bas = 0,01 sous les deux nuls et p_haut = 0,02 sous l'un
  d'eux (une direction marquée ; libellé « sur-représentée » à une borne seulement) : arrêt, message (ii) ;
```

Après :

```
- **direction nulle, cas sain** : une direction nulle à égalité au vingtième rang, avec S_min < S(v) ≤ S_max, libellé égal aux deux
  bornes : pas d'arrêt, une direction marquée écrite, p_haut − p_bas = 1/(M + 1) ; une direction marquée avec S_max < S(v) :
  p_bas = p_haut, pas d'arrêt ; S_min et S_max égaux au plus petit et au plus grand S d'une énumération de tous les départages, sur
  un jouet à trois jetons de même score au vingtième rang ; valeur p écrite égale à p_haut ; attendu calculé sans la direction
  marquée ;
- **direction nulle, artefact** : jouet à M = 99 où, pour une famille, p_bas = 0,01 sous les deux nuls et p_haut = 0,02 sous l'un
  d'eux (une direction marquée avec S_min < S(v) ≤ S_max ; libellé « sur-représentée » à une borne seulement) : arrêt, message (ii) ;
  le même jouet où la direction marquée a S_max < S(v) : pas d'arrêt ;
```

**G3** (obligatoire : EC-6 (i) : les listes de dix des pôles sont des listes montrées de la direction lue ; sans garde, le tri y choisit en silence).

Avant :

```
> (i) **Direction lue** (chaque vecteur, chaque signe, chaque lentille, lentille des logits comprise ; chaque liste qui entre dans
> une table ou une comparaison : vingt premiers par score, vingt premiers par z sous le nul isotrope, listes du témoin de couche) :
```

Après :

```
> (i) **Direction lue** (chaque vecteur, chaque signe, chaque lentille, lentille des logits comprise ; chaque liste qui entre dans
> une table ou une comparaison : vingt premiers par score, vingt premiers par z sous le nul isotrope, listes du témoin de couche ;
> et les deux listes de dix des pôles, les dix pôles par cosinus et les dix premiers jetons de la lecture de chaque pôle, où
> l'égalité se lit entre la dixième et la onzième valeur) :
```

**G4** (obligatoire : EC-6 (iii), dernière phrase, accordée à G3).

Avant :

```
> nul). La concentration, les pôles et les bornes de calibration ne sont pas concernés : aucun n'emploie les vingt premiers jetons.
```

Après :

```
> nul). La concentration, la concentration des pôles (cosinus maximal, rang parmi les maxima nuls) et les bornes de calibration ne
> sont pas concernées : aucune n'emploie une liste de premiers ; les listes de dix des pôles le sont, par (i).
```

**G5** (obligatoire : essai de G3).

Avant :

```
  de la liste par z : arrêt ;
```

Après :

```
  de la liste par z : arrêt ; deux colonnes égales d'une matrice `W_down` jouet, au dixième et au onzième cosinus : arrêt ;
```

**G6** (obligatoire : EC-6, chiffres d'appui : valeur du modèle calculée sans comptage d'événements rares, et étendue selon l'échelle).

Avant :

```
rang est de **7,0 × 10⁻⁶ par direction** (28 sur 4 000 000 ; ± 1,3 × 10⁻⁶) pour des scores centrés ; 3,2 × 10⁻⁵ si la moyenne des
scores vaut dix écarts types, 2,8 × 10⁻⁴ si elle en vaut cent (l'arrondi pèse plus quand les scores sont grands devant leur
dispersion). Soit, pour des scores centrés : rare pour une direction lue ; 0,014 direction marquée attendue par jeu de 2 000
directions nulles ; mais **1,4 égalité attendue sur les ≈ 195 000 lectures du calcul** (texte, plan, point 6), c'est-à-dire au moins
une avec une probabilité d'environ 0,74 (1 − e^(−1,36)), et davantage si les scores ne sont pas centrés (6 et 54 égalités attendues
aux deux autres lignes).
```

Après :

```
rang est de **9,0 × 10⁻⁶ par liste** pour des scores centrés réduits (valeur du modèle calculée par la contre-lecture sans compter
d'événements rares ; le comptage de l'auteur, 28 sur 4 000 000, soit 7,0 × 10⁻⁶ ± 1,3 × 10⁻⁶, en est une fluctuation basse), de
8,3 × 10⁻⁶ à 1,5 × 10⁻⁵ selon l'échelle des scores ; 3,6 × 10⁻⁵ si la moyenne des scores vaut dix écarts types, 2,9 × 10⁻⁴ si elle
en vaut cent (l'arrondi pèse plus quand les scores sont grands devant leur dispersion). Soit, pour des scores centrés : rare pour une
direction lue ; 0,018 direction marquée attendue par jeu de 2 000 directions nulles ; mais **1,6 à 2,9 égalités attendues sur les
≈ 195 000 lectures du calcul** (texte, plan, point 6), c'est-à-dire au moins une avec une probabilité de 0,80 à 0,95, et davantage si
les scores ne sont pas centrés (7 et 56 égalités attendues aux deux autres lignes).
```

**G7** (obligatoire : § 9, point 7, option 1 : chiffre par liste et non par direction ; ce que l'option laisse passer).

Avant :

```
     Avantage : la plus simple ; arrêt rare (≈ 7 × 10⁻⁶ par direction lue dans le modèle simple de EC-6). Inconvénient : une égalité
     sur une direction nulle reste tranchée en silence par le tri, et peut déplacer une valeur p de 1/2 001.
```

Après :

```
     Avantage : la plus simple ; arrêt rare (≈ 10⁻⁵ par liste dans le modèle simple de EC-6, soit de l'ordre de 0,5 à 1 % pour les
     quelque neuf cents listes des directions lues). Inconvénient : une égalité sur une direction nulle reste tranchée en silence par
     le tri, et peut déplacer une valeur p de 1/2 001, donc, rarement, un libellé, sans que rien ne l'écrive.
```

**G8** (obligatoire : § 9, point 7, option 2 : chiffre).

Avant :

```
     ≈ 195 000 lectures, au moins une égalité est attendue avec une probabilité de l'ordre de 0,7 ou plus dans le même modèle ; la
```

Après :

```
     ≈ 195 000 lectures, au moins une égalité est attendue avec une probabilité de 0,8 à 0,95 dans le même modèle ; la
```

**H1** (facultatif : § 9, point 7 : deux variantes que Lazar peut vouloir voir).

Avant :

```
   - **Recommandation** : option 3 ; confiance moyenne à bonne (environ 0,75).
```

Après :

```
   - **Variantes, pour mémoire** : (a) adopter dès maintenant la règle de départage de la version 2 (score décroissant, puis
     identifiant croissant) : jamais d'arrêt, valeurs p valides (même règle pour v et les nuls) ; mais c'est un second écart au texte
     scellé, et, à score égal, la règle préfère toujours les petits identifiants ; (b) au lieu d'arrêter le calcul, rendre « non
     calculable » le seul libellé en cause (ou la seule direction lue à égalité), comme le texte le fait pour une calibration hors de
     ses bornes : la lecture continue et l'égalité est écrite ; mais un libellé manque sans mot de Lazar.
   - **Recommandation** : option 3 ; confiance moyenne à bonne (environ 0,75).
```

**H2** (facultatif : EC-6 : rendre connu d'avance le cas des lignes de sortie identiques, qui fait des égalités pour toute direction).

Avant :

```
> | égalité au vingtième rang d'une direction nulle, décisive pour un libellé | arrêt ; nœud |.
```

Après :

```
> | égalité au vingtième rang d'une direction nulle, décisive pour un libellé | arrêt ; nœud |. Au montage, le code compte les paires de
> jetons gardés dont les lignes de `lm_head.weight` sont égales octet pour octet, et l'écrit, sans arrêt.
```

## 7. Pièces de cette vérification

Dossier `verification-addendum-concentration-outils-v1/`, à côté de ce rapport ; empreinte complète dans chaque compagnon ; commandes,
entropie et versions dans `commandes-v1.txt`.

| pièce | rôle | empreinte |
|---|---|---|
| `commandes-v1.txt` | commandes, entropie, versions | `4f198fba…` |
| `differentiel_version_contre_lecteur.py` | couples du premier rapport appliqués au brouillon, comparés à la version | `cb3020b2…` |
| sortie du programme précédent | comptes du différentiel | `1516d0f8…` |
| `diff-brouillon1-couples-vers-version.txt` | différentiel restant | `a533ee90…` |
| `egalite_rang_k_contre_lecteur.py` | fréquence d'égalité, loi conditionnelle exacte | `b3e070c0…` |
| sortie du programme précédent | chiffres du § 2.4 | `fe7274f1…` |
| `egalite_comptage_direct_contre_lecteur.py` | fréquence d'égalité, comptage direct | `ef5e2b05…` |
| sortie du programme précédent | contrôle du § 2.4 | `56bb8d00…` |
| `bornes_departage_contre_lecteur.py` | bornes, énumération de tous les départages sur jouets | `ea28deba…` |
| sortie du programme précédent | chiffres du § 2.2 | `e86b9036…` |
| `couples_verification_contre_lecteur.py` | couples du § 6, vérification et application | `4c2e84b1…` |
