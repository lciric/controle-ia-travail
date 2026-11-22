# Relance — nœud pour Lazar : l'oracle de la famille aveugle n° 1 face à la règle des questions fermées — v1

- **Au coffre.** Classe C (note de nœud). Écrite le 2026-11-22 vers 15:00 UTC par le monteur de l'oracle du cycle 1,
  relance (`session_01XJ6MgmSDBZpPAuXLe3diix`). Contient de la forme d'oracle : ne sort pas du coffre ; la mère en
  reçoit le chemin, l'empreinte et l'issue en un mot. Lazar la lit de droit.
- Textes confrontés, empreintes recalculées avant lecture :
  - la spécification de la famille, `f4c479c5:donnees/bras-attaque-scellement-2-v1/piece-3-famille-aveugle-1-verite-du-dommage-v2.md`, `2a7416a823c406a1…` ;
  - l'oracle monté par le prédécesseur, `piece-2-oracle-monte-famille-1-v1.md`, `758e404a4327f5a3…`, et
    `oracle_famille_1_v1.py`, `43c4c8f1de288781…` (ce dossier) ;
  - la pièce de sécurité v16, section 3.5, « Règle des questions fermées », branche `claude/piece-securite-banc-ferme-v1`, `b8bcda60ead6f58f…` ;
  - la course, brouillon 17, section D6, liste d'arrêt et « Champs ouverts et nœuds », branche
    `claude/loving-lamport-7ol5ws`, `cf5d35d8472137d3…` ;
  - la répétition générale, brouillon 9, champ R-5, branche `claude/prereg-course-banc-ferme-v1`, `a58cab35cf4914a4…`.

## 1. Décision demandée, en une phrase

Sous quelle règle l'oracle de la famille aveugle n° 1 pose-t-il ses questions aux lecteurs externes, alors que la règle
des questions fermées exige des paramètres identiques au caractère près aux entrées de la référence, toutes reprises,
dans l'ordre de la référence, et tirés ni de la pièce 2 ni de la pièce 3 de la famille ?

## 2. Constat

**Sur les fichiers du banc, hors coffre, par programme, comptes seuls** (aucun texte affiché ;
`taches-evaluation.json` `76cdeace861d2fff…`, `taches-entrainement.json` `8d20a698d76baa8a…` ; 14:46 UTC) :
- la référence cachée de chaque tâche (`cibles`) a quatre parties, toujours dans cet ordre : `compute` (un
  dictionnaire), `controls`, `fruitful_directions`, `sterile_directions` ; chaque entrée de liste a quatre champs :
  `id`, `description`, `evidence`, `section` ;
- **l'identifiant dit le type** : préfixe `C`, `F` ou `S` selon la partie, sur toutes les entrées (736 en évaluation,
  356 en épreuve) ;
- **l'ordre de la référence range les directions par type** : les fructueuses d'abord, les stériles ensuite ;
- **les descriptions brutes disent souvent l'issue** : portent au moins un mot de la liste `MOTS_D_ISSUE` de l'oracle
  monté, en évaluation 65 descriptions fructueuses sur 192 et 78 stériles sur 165 ; sur les tâches d'épreuve, 46 sur
  95 et 37 sur 70 (contrôles : 127 sur 379 et 81 sur 191, sans type à trahir).

**Ce que la spécification exige** (pièce 3 v2, section 1) : lecteurs aveugles au type de la direction ; énoncés
neutres réécrits par une main neuve avant toute lecture (« étape 0 »), le type dans un fichier à part ; précondition de
neutralité P6. L'oracle monté en tient compte : un identifiant tiré au sort par énoncé, ordre mêlé par graine,
directions seules (les contrôles et le calcul ne sont pas notés par cette famille).

## 3. La règle, point par point

| point de la règle (pièce de sécurité v16, 3.5 ; course D6) | l'oracle tel que spécifié | tenu ? |
|---|---|---|
| un gabarit de question unique, scellé, identique pour toutes les tâches | invite 4.1 de la pièce 2 du prédécesseur | oui |
| chaque paramètre est, au caractère près, une entrée de la référence | énoncé neutre réécrit ; copier la description casserait l'aveuglement au type que la spécification exige, et P6 n'aurait plus d'objet | **non** |
| la liste reprend toutes les entrées | directions seules ; « toutes » ferait entrer contrôles et calcul, que la règle de l'oracle ne note pas | **non** |
| dans l'ordre de la référence | l'ordre de la référence dit le type ; l'oracle mêle l'ordre | **non** |
| (la règle ne dit rien des identifiants) | ceux de la référence disent le type ; l'oracle les tire au sort | — |
| les deux jumeaux reçoivent le même jeu, au caractère près, dans le même ordre | oui : le jeu est celui de la tâche, tiré une fois | oui |
| aucun paramètre choisi d'après la consigne, le lot, la famille ou le mode | la sélection (directions) et l'étape 0 sont fixées par la pièce 3 de la famille | **non attestable** |
| contrôles hors gabarit, repli interne (GO-2026-11-21-85, option (a)) | aucun élément de cet oracle ne se juge par programme sans lecteur. Tenir tous ses éléments pour « hors gabarit » laisserait sa règle sans rien pour appliquer son seuil : c'est la limite du repli | ne s'applique pas |

**Conséquence, à la lettre de la course** (liste d'arrêt : « Gabarit ou liste de paramètres… paramètre qui s'écarte
d'un caractère » ; « L'oracle de la famille… ne se ramène pas au gabarit pour ce qui part » ; « Le monteur de l'oracle
ne peut pas attester que les paramètres ne viennent ni de la pièce 2 ni de la pièce 3 ») : **rien ne part ; nœud pour
Lazar.** L'addendum O ne peut pas porter l'attestation de provenance, ni l'attestation « sans les contrôles hors
gabarit » ; donc aucun dépôt chez le tiers, donc aucune course.

Ce nœud reprend, sans les changer, le point 2 du message v12 du prédécesseur (`fd3dbb42…` : « Si la v12 exige une
copie, la neutralité tombe et la spécification ne tient plus : c'est un nœud ») et le nœud de son attestation 1 v13
(`6a8234f4…`). Les versions v13 à v16 de la pièce de sécurité et le brouillon 17 de la course ont gardé « au caractère
près » ; je n'ai trouvé au registre aucun mot de Lazar qui tranche ce point.

## 4. Enjeu

Sans décision, la famille aveugle n° 1 ne peut pas être lue par des lecteurs externes : la course du banc fermé ne part
pas. Le choix touche ce que la garde des questions protège : qu'aucune question ne dise la condition, la consigne ni le
mode (pièce de sécurité, 3.5, préambule de la règle).

## 5. Options

**(a) Une exception nommée pour cet oracle**, écrite sans contenu par une version nouvelle de la pièce de sécurité et
de la course : les paramètres sont dérivés de la référence par une procédure scellée au coffre ; un programme vérifie,
là où est la référence, la chaîne d'empreintes de chaque entrée source à son paramètre, la complétude sur ce qui est
envoyé et l'identité des jeux entre jumeaux ; identifiants et ordre tirés par une graine scellée, indépendante de la
condition ; la main qui réécrit ne voit que la référence (ni consigne, ni lot, ni famille). Le détail — quelles parties
de la référence envoyer, et si les paramètres réécrits passent la garde de fuite contre la part propre des consignes —
est une conception d'oracle : à Fable 5.2, au coffre, contre-lue.
- Avantage : l'oracle reste celui que la spécification décrit, éprouvable tel quel ; la règle garde son but (aucun mot
  d'une question ne vient de la consigne ; même jeu pour les jumeaux).
- Inconvénients : « au caractère près » devient une garde par provenance, plus faible ; une réécriture pourrait, en
  principe, rencontrer un mot de la consigne sans l'avoir vue, d'où la garde à décider ; ce qui part laisse voir
  quelle partie de la référence l'oracle lit, sauf à envoyer aussi les autres parties, non notées ; deux attestations
  de l'addendum O changent de lettre ; deux versions nouvelles contre-lues.

**(b) La règle à la lettre, et l'oracle changé** : paramètres = descriptions brutes de toutes les entrées, dans l'ordre,
sans les identifiants de la référence.
- Avantage : aucune version nouvelle de la pièce de sécurité.
- Inconvénients : l'aveuglement au type que la spécification exige tombe (ordre et mots d'issue le trahissent) ; version
  nouvelle de la spécification par son auteur, contre-lue ; le dommage mesuré serait biaisé dans un sens inconnu.

**(c) Le repli écrit de la course** : un second lecteur à poids ouverts sur machine fermée, d'où rien ne sort, puis les
juges du programme ; la règle des questions n'a plus d'objet sans voie d'envoi.
- Avantage : rien ne sort.
- Inconvénients : lecteur plus faible, à qualifier par les épreuves ; risque d'entrer dans une base boîte noire de G1
  (réserve 1 du réfutateur) ; modèle neuf, devis et GO ; version nouvelle de la course.

## 6. Recommandation

**(a)**, confiance 0,55. Si Lazar ne veut aucune exception à la pièce de sécurité : (c) avant (b). Sous (a), je
reprends la recommandation du prédécesseur sur « qui écrit » (v12, point 1) : la main neuve rédige ; le monteur fixe
par programme identifiants, ordre et complétude, scelle les listes et atteste sans contenu.

**Aucun défaut à 48 heures** : c'est un nœud ; tant qu'il n'est pas tranché, rien ne part.
