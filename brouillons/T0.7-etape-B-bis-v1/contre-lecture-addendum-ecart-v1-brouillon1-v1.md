# Contre-lecture (R2) du brouillon 1 de l'addendum d'écart au préenregistrement scellé de T0.7, étape B bis — v1

- **Lecteur** : sous-agent neuf de la session mère (modèle noté sans identifiant). Je n'ai écrit aucun fichier de l'étape B bis.
- **Heure (UTC, `date -u`)** : rapport écrit à 2026-11-16T00:46:57Z ; lecture depuis 00:40 environ.
- **Pièce lue** : `brouillons/T0.7-etape-B-bis-v1/T0.7-etape-B-bis-v1-addendum-ecart-v1-brouillon1.md`,
  `991ab56066c229c2a04cfa0489e6cbe0f2b11a717587d305fdcfb65ea1582efe` (compagnon juste), commit `2d7f93d7`
  (2026-11-16T00:38:58Z) de `prep/t07bbis-code-v1`, poussé (tête distante égale, relevée à 00:42:38Z).
- Processeur seulement ; aucune machine, aucun appel payant ; rien lu ni écrit sous `diag/`, `donnees/`, `docs/verdicts/` ;
  aucun fichier existant modifié ; rien committé ; rien inscrit à aucun registre.

## Verdict

**Scellable après corrections.** Le fond est juste et le contrôle mécanique se rejoue à l'octet. Deux majeurs, tous deux de
rédaction (aucun ne touche les huit blocs « nouveau ») ; huit mineurs ; couples exacts au § « Corrections ».

- **M1 — m4 et m5 dépassent la lettre de ce qui a été porté à Lazar.** Le nœud de R-2933 portait « les couples des brouillons 4
  à 6 » (dix-sept couples, a1 à a5, b1, b2, c1 à c10), et la voie (ii) acceptée dit « qui porte exactement les couples ». Les
  ajouts m4 (dans le premier écart) et m5 (dans le deuxième) sont deux fragments de plus sur un texte scellé. Le § 1 de
  l'addendum ne le dit pas : il présente la ligne de décision comme couvrant tout. Ma lecture : m4 écrit ce que le code fait
  déjà et ce que la phrase scellée de la garde de débit implique (« aucun score ») ; m5 élargit une réserve neuve dans le sens
  prudent ; ils étaient écrits en couples dans la contre-lecture dont Lazar a accepté la recommandation. Ils sont donc
  défendables, mais un écart à un texte scellé est un nœud de Lazar : il faut l'écrire au § 1 et le dire à Lazar **avant** le
  scellement (R-2955 le prévoit ; l'addendum doit le porter). Correction C1.
- **M2 — Les noms « E1 » à « E8 » des écarts heurtent les états « E0 » à « E6 » et « E1b » du texte scellé.** Le texte scellé
  nomme ainsi ses états de lecture (68 occurrences : « plafond échoue (E1, E1b) », « pour chaque dose en E4 à E6 », « seule
  voie vers E6 »). L'addendum demande au verdict de « lire les critères du texte scellé modifiés par E1 à E4 » et de « tenir
  pour arrêt chacun des cas de E4 » : pour un lecteur du verdict, « E4 » est d'abord l'état « ne sépare pas à texte égal ».
  Un addendum qui modifie des critères gelés ne doit pas pouvoir être confondu avec eux. Correction C2 (renommage, 22 lieux).

## 1. Contrôle mécanique (programme à moi)

Programmes : `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/contre-lecture-addendum-v1/verif.py`
et `verif2.py` (même dossier), joués par `.venv/bin/python -I` ; le second est en annexe. Entrées vérifiées par empreinte dans
le programme : texte scellé `0ae6210f…` (293 lignes), brouillon 6 `bf1be58e…` (325 lignes), addendum `991ab560…`.

- **Huit écarts** extraits des blocs de l'addendum (deux blocs par écart, aucun retour à la ligne dans un bloc).
- **Chaque « ancien » figure une seule fois dans le texte scellé, à la ligne citée** : 105, 155, 175, 186, 227, 227, 227, 228.
  Aucun « nouveau » ne figure déjà dans le texte scellé.
- **Chaque « nouveau » figure une seule fois dans le brouillon 6 complété de m4 et m5**, à la ligne citée plus 32.
- m4 et m5 : leurs « ancien » (contre-lecture du brouillon 6, lignes 103 à 110) figurent une seule fois dans le brouillon 6
  (lignes 137 et 187).
- **Texte scellé + huit remplacements, aligné ligne à ligne sur le brouillon 6 complété** (`difflib`, lignes entières) : les
  seules différences sont la ligne 1 (titre, et les 32 lignes de tableaux insérées à sa suite), 5, 22, 76, 93, 116, 293.
  Aucun autre fragment ne change : **aucun écart omis, aucun ajouté**.
- Texte scellé contre brouillon 3 (`f104917f…`) : lignes 5, 76, 93, 116, 293 seulement (le couple mécanique du scellement).
- Les 32 lignes insérées en tête du brouillon 6 ne sont que les trois tableaux de différentiel (c1 à c10, a5, a1 à a4, b1, b2) :
  les dix-sept couples retombent tous dans les huit fragments.
- Le brouillon 6 du commit `6c346a03` (2026-11-15T17:14:46Z) a bien l'empreinte `bf1be58e…` : la règle de lecture de la
  répétition y était écrite avant la quatrième passe.

Précision de forme : l'addendum dit « le brouillon 6 a 32 lignes de plus en tête » ; exactement, elles suivent le titre
(ligne 1 des deux côtés). Sans effet.

## 2. Chaque écart : raison, pièces, ce qui ne change pas

Toutes les empreintes citées par l'addendum ont été recalculées par `sha256sum` et sont justes : brouillons 3 à 6 ; les quatre
scripts de couples (`4a42e3b7…`, `51135f43…`, `8608d87c…`, `b61ed1d3…`) ; `contre-lecture-brouillon5-et-code-v2-v1.md`
`93b0724d…` ; `contre-lecture-brouillon6-et-code-v3-v1.md` `35745ece…` ; les deux diagnostics `5ecb9235…` et `dd67802d…` ;
`corrections-controle-attention-v1.md` `45aeddba…` et `-v2.md` `4e4fad18…` ; `fichiers-fiche-code-bbis-v3.txt`
`b8fb095b…` (103 lignes, comptées ; la seule ligne qui contient « prereg » est `src/controle_ia/prereg.py`) ;
`commun_v1.py` `9db2b40b…`, `validation_imbriquee_v3.py` `71bffa5b…`, `marche_v3.py` `7009b34d…`, `lecture_v2.py`
`154795f4…`, `registre_bbis_v1.py` `c3b1848b…`, `t07/registre_v1.py` `e5023657…`, `amorce_bbis_v3.sh` `18e2f205…`,
`lancer_bbis_v3.sh` `dc26ea01…`, `ABSENCE-B-BBIS-v1.json` `134ac847…`.

Chiffres relus à leur source, lignes citées justes : 0,633 (diagnostic de l'écart, lignes 23 et 67) ; 2,131·10⁻² (lignes 39 et
65) ; 2,9·10⁻⁷ et 5,9·10⁻⁷ (ligne 163) ; 0,46, 0,0074, 7,8·10⁻⁵, 0,558 à 0,983, 4,0·10⁻² au signal faible, 1,9·10⁻⁵ au plus
(diagnostic de stabilité, lignes 17 à 21) ; 30 artefacts sur 35, 5,8·10⁻⁹, 2,9·10⁻¹⁰, 5,2·10⁻⁶ à 4,1·10⁻⁵, 3,4·10⁻⁸ à 7,8·10⁻⁷,
largeur 1 024 (contre-lecture du brouillon 5, lignes 220 à 290) ; 183 passés (contre-lecture du brouillon 6, ligne 213).
Numéros de ligne du code justes : `commun_v1.py` 27 et 28 ; `lecture_v2.py` 125 à 139, 512 et 513, 520 à 553, 1124, 1137 ;
`registre_bbis_v1.py` 42, 97 et 98, 212 à 215 ; `t07/registre_v1.py` 136 à 148.

Raisons : justes pour les huit. Le code v3 fait ce que le premier écart écrit (`validation_imbriquee_v3`, docstring et
lignes 56 à 135 : linéaire à 300 époques, attention à 3, déterminisme de l'attention à 300 par second apprentissage sur la
carte, arrêt sur sonde de contrôle en échec, tirage parmi les sondes finales finies).

**Ce qui est déclaré inchangé l'est.** Les six lignes touchées sont 105 (plan, point 5), 155 et 175 (critères de lecture),
186 (liste d'arrêt), 227 et 228 (code neuf). Aucune ligne des sections « Hypothèse » (32 à 45), « Prédiction » (46 à 64),
« Métrique » (65 à 86), « Seuil » (87 à 95), « Puissance » (200 à 209), « Calcul et dépense » (216 à 219), « Lignes de
registre » (220 à 223) n'est touchée. Dans la ligne 105, tout ce qui n'est pas la phrase du contrôle est identique (grille,
300 époques, pas, critère de choix, ex aequo, sonde finale, garde de débit, variantes). Aux critères : aucun état, aucune issue,
aucun libellé, aucun seuil de verdict ne change ; une réserve toujours écrite et un point (7) s'ajoutent. À la liste d'arrêt :
seule la ligne du contrôle s'étend ; sa fin (« correction du code sous un nom neuf… relance sous ce texte ») est intacte.
Deux choses que le § 3 de l'addendum ne dit pas (mineurs m3 et m4 ci-dessous) : le moment de l'arrêt du contrôle change
(fin de l'apprentissage), et la sélection du réglage peut dépendre de la pile.

## 3. Antériorité

- Registre propre (dépôt principal, `main` à `43996069`) : deux lignes seulement, `SCELLEMENT-BBIS` et `ABSENCE-B-BBIS` du
  2026-11-14T12:30:30Z. Ni `CODE-BBIS`, ni `GO-BBIS`, ni `SCORES-BBIS`.
- **Branche de données de la course absente à distance**, par les noms seulement, depuis l'arbre de travail, les trois variables
  `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE` constatées non posées puis retirées dans un sous-interpréteur, à
  **2026-11-16T00:42:38Z** : `git ls-remote --exit-code origin refs/heads/donnees/t07-etape-b-bis-v1` → **code 2** ; motif
  `refs/heads/donnees/t07-etape-b-bis*` → code 2 ; témoin positif `refs/heads/prep/t07bbis-code-v1` → code 0 (`2d7f93d7`).
  Branches de répétition présentes à distance : `…-v1` (`56f5b8b8`) et `…-v2` (`3528a2e8`) ; ni v3 ni v4 à cette heure.
  Références locales de l'arbre : aucune `donnees/t07-etape-b-bis*`.
- Le nom de la branche de sortie de la course est bien celui-là (`scripts/amorce_bbis_v3.sh`, ligne 36).
- Le § 4 de l'addendum cite « § 3 et § 8 » de la contre-lecture du brouillon 6 pour l'absence à 20:56 : c'est le § 3
  (ligne 183) qui porte la branche de la course ; le § 8 ne parle que de la branche de la répétition. Sans effet.
- La quatrième passe de répétition tourne (R-2953, machine créée à 00:35 UTC) : données synthétiques, écart accordé par R-2802.
  Le brouillon 1 et ses huit blocs sont committés et poussés avant toute sortie de cette passe (aucune branche v4 à 00:42:38Z).
  Si la mesure de la passe entre au texte avant le scellement (R-2955), elle ne doit entrer qu'aux § 4 et § 5, jamais dans un
  bloc ; à prouver par le rejeu du programme du § 1 sur la version scellée (mineur m8).

## 4. L'affaiblissement déclaré : réponse

**Nature.** C'est un changement de **contrôle**, pas d'hypothèse ni de revendication. L'hypothèse (HB-1 à HB-5), les
grandeurs, les seuils et les états ne changent pas ; aucune phrase du programme ne revendique la reproductibilité d'une sonde
« attention » d'une pile de calcul à l'autre ; le texte scellé place lui-même B bis hors de H1 à H8 et hors du critère 3 de G0.
Le contrôle scellé est une garde d'intégrité de la chaîne, et il arrêtait à tort (0,633 entre deux jeux d'instructions du même
paquet gelé, sans aucune erreur). R-PILE et le point (7) restreignent ce que le verdict peut dire d'une aire : c'est un écart
aux critères de lecture gelés, donc un nœud de Lazar, mais c'est précisément l'un des objets nommés à R-2933 (« contrôle de
l'attention à 3 époques, R-PILE, point 7 ») que la ligne de décision accorde. **Il ne faut donc pas de mot propre de plus pour
le fond.** Une réserve : la phrase nue « la sonde lue à 300 époques n'est plus comparée à une référence d'une autre pile »
n'était pas dans le nœud de R-2933 ; R-2955 prévoit de la dire à Lazar ; je recommande qu'elle soit dite avant le scellement,
dans le même message que m4 et m5 (confiance 0,7 que cela suffit sans GO neuf).

**Honnêteté.** Oui : le § 5 nomme l'affaiblissement comme tel (point 4), dit l'aveuglement après la troisième époque (point 1),
le seuil (point 2), les erreurs communes aux deux côtés (point 3), l'absence de mesure sur carte et le couple unique (point 5).

**Complétude : non, il manque six choses** (aucune ne change le fond ; couples C4) :
1. **Le réglage retenu peut lui-même dépendre de la pile.** Sans signal, l'étendue 0,0074 dépasse le seuil d'ex aequo 0,005 :
   la famille, la couche ou la régularisation retenues peuvent changer d'une pile à l'autre (diagnostic de stabilité, lignes 24
   et 106), donc aussi le fait que R-PILE s'écrive ou non. R-2917 le savait ; l'addendum ne le dit nulle part.
2. **Le régime intermédiaire n'est pas mesuré.** Les chiffres viennent d'un bruit gaussien isotrope ; entre les aires 0,47 et
   0,56 rien n'est mesuré ; « de vraies activations peuvent mêler un signal faible et une forte mémorisation » (même pièce,
   ligne 108). Une cellule décidée à quelques millièmes d'un seuil par une sonde « attention » pourrait changer d'état sur une
   autre pile ; l'état rapporté est celui de la carte de la course.
3. **Ce que voit exactement le couple tiré.** Si son réglage retenu est linéaire, sa sonde lue est comparée comme au texte
   scellé, et les sondes « attention » du contrôle (3 et 300 époques) ne sont pas des sondes lues ; s'il est « attention », la
   sonde lue n'a que le déterminisme. Les sondes « attention » des autres couples et celles d'ENC ne reçoivent aucun contrôle
   (c'était déjà le cas au texte scellé).
4. **Le déterminisme ne prouve pas la justesse** : une erreur déterministe propre à la carte après la troisième époque passe
   les trois contrôles. Le point 1 le dit à demi (« sans comparaison directe ») ; à écrire en clair.
5. **L'horizon 3 a été fixé sur des trajectoires synthétiques** (diagnostic de l'écart, lignes 161 à 169 ; à 11 époques il n'y
   a plus de marge : 4,4·10⁻⁵ et 8,7·10⁻⁵).
6. **Un couple dont la sonde finale est en échec n'est jamais contrôlé**, et le contrôle vient en fin d'apprentissage : une
   erreur de chaîne coûte désormais tout l'apprentissage (mineur m7 de la contre-lecture du brouillon 6, non repris).
Détail : le § 5 annonce 30 artefacts sur 35 et n'en nomme que quatre non attrapés ; le cinquième (actions et étiquettes
permutées ensemble) n'est pas une erreur ; à écrire pour que le compte ferme.

Observation, sans demande : une comparaison plus lâche de la sonde de 300 époques entre la carte et le processeur (aires ou
rangs, 388 s de processeur mesurées) n'a pas été étudiée par le diagnostic ; elle aurait gardé une référence d'une autre pile
quand la sonde apprend un signal. C'est une idée pour une version future, pas une condition.

## 5. Rattachement du code v3 et citation par le verdict

Les faits du § 6 de l'addendum sont justes : `TEXTE` et `TEXTE_SHA256` (`commun_v1.py`), `texte_sha256` écrit par
`lecture_v2` (ligne 1124), refus d'une autre ligne `SCELLEMENT-BBIS` (ligne 1137), motif d'extraction
`/prereg/T0.7-etape-B-bis-v1.md*` de l'amorce (ligne 161). J'ajoute : la fiche de `CODE-BBIS` porte aussi
`"texte": "prereg/T0.7-etape-B-bis-v1.md"` (`registre_bbis_v1.py`, ligne 149), et `marche_v3` vérifie sur l'instance chaque
fichier de la fiche (ligne 223) : **l'addendum ne doit pas entrer dans la liste de la fiche** (il n'est pas extrait sur
l'instance, la marche s'arrêterait). L'addendum a raison de le laisser dehors.

**Suffisant ? Pas encore.** Aucune pièce que le lecteur du verdict lira par construction (texte scellé, registre propre,
sortie de `lecture_v2`) ne nomme l'addendum ; le seul indice mécanique est que la lecture écrit « R-PILE » et un point (7)
que le texte cité ne porte pas. « Le lecteur ajoute la citation à la main » est une consigne, pas une garde. Trois ajouts
(couple C5) : (i) une règle de recevabilité écrite dans l'addendum : un verdict qui ne cite pas l'addendum, son empreinte et
sa ligne n'est pas scellé, et la mère le vérifie par `grep` avant de le soumettre ; (ii) l'addendum figure nommément dans la
liste des fichiers donnés au lecteur du verdict (R13) et dans `registres/etat.md` ; (iii) la table conjointe et tout document
qui cite une aire de B bis citent aussi l'addendum. Avec le nom du fichier scellé voisin du texte dans `prereg/`
(`T0.7-etape-B-bis-v1-addendum-ecart-v1.md`), cela suffit.

## 6. Inscription : registre voisin

**La contrainte est réelle, vérifiée dans le code.**
- `lecture_v2.lire_lignes` (lignes 520 à 553) : au registre propre, toute ligne de quatre champs dont la date et la clé sont de
  bonne forme et dont la clé n'est pas l'une des huit (`CLES_PROPRES`, lignes 512 et 513) rend « registre propre : clé …
  inconnue » et la lecture refuse. Une seconde ligne d'une clé permise refuse aussi (« en double »).
- `registre_bbis_v1.ajouter_ligne_propre` (lignes 95 à 98) refuse d'écrire toute clé hors de `CLES_BBIS` et tout autre
  registre ; `exiger_ancetre_de_la_fiche` (lignes 212 à 215) relit le registre propre par `lecture_v1.lire_lignes` : une clé
  inconnue bloquerait donc aussi le lancement, pas seulement la lecture.
- Le registre partagé est exclu (texte scellé, ligne 222 ; garde `exiger_partage_sans_bbis`).
La décision de la mère (R-2955) est donc la bonne, et l'option (c) de l'auteur (une forme de clé que le code ignorerait) est
écartée à raison. « Au registre propre » est bien la formule de la mère dans la ligne de décision, pas le mot de Lazar (mot
verbatim : onze mots, sans lieu).

**Un registre voisin ne gêne pas le code v3**, sous deux conditions de nom :
- aucun code de `src/controle_ia/t07bbis/`, aucun script `*bbis*`, aucun essai `*bbis*` ne parcourt `registres/` (recherche de
  `glob`, `iterdir`, `listdir`, `rglob`, `walk`) : ils ouvrent des chemins nommés (`t07-etape-b-bis-v1.md`,
  `scellements-v1.md`, `t07-etape-b-bis/…`, `go-extraits/…`) ; le seul parcours de `registres/` de la suite
  (`tests/test_t06_chaine_v13.py`, ligne 230) porte sur une racine factice et sur `*.json` ;
- `verifier-arbre` ne couvre pas `registres/` (hors `registres/passations`) : un registre vivant sans compagnon ne crée ni
  orphelin ni faute ; le fichier scellé sous `prereg/`, lui, doit avoir son compagnon ;
- **condition 1** : le nom ne doit pas commencer par `t07-etape-b-bis-v1.md` (motif d'extraction
  `/registres/t07-etape-b-bis-v1.md*` de l'amorce, ligne 164, qui prend déjà `….md.ouvertures.md`) ni se trouver sous
  `registres/t07-etape-b-bis/` (ligne 165) : sinon il monterait sur l'instance ; l'essai de la chaîne tient
  `registres/autre-v1.md` pour interdit sur l'instance (`tests/test_t07bbis_chaine_instance_v1.py`, ligne 75) ;
- **condition 2** : de même sous `prereg/`, le nom scellé ne doit pas commencer par `T0.7-etape-B-bis-v1.md`.
  Vérifié par `fnmatch` : `t07-etape-b-bis-v1-addenda-v1.md` et `T0.7-etape-B-bis-v1-addendum-ecart-v1.md` ne sont pris par
  aucun des deux motifs.

**Proposition.**
- Fichier scellé : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md` et son compagnon.
- Registre voisin : `registres/t07-etape-b-bis-v1-addenda-v1.md` (version dans le nom, R12 ; pluriel : il recevra un éventuel
  addendum suivant ; sans compagnon, comme le registre propre). En-tête d'une ligne :
  `# Registre voisin des addenda au texte « T0.7, étape B bis » (prereg/T0.7-etape-B-bis-v1.md, 0ae6210f…) — lu par aucun code ; lignes ajoutées, jamais réécrites ; jamais recopiées dans registres/t07-etape-b-bis-v1.md (le code v3 y refuse toute clé hors des huit) ni dans registres/scellements-v1.md ; décision R-2955 ; format : | clé | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 | décision |`
- Ligne :
  `| ADDENDUM-ECART-1-BBIS | <AAAA-MM-JJTHH:MM:SSZ, date -u> | prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md | <sha256 entier> | GO-2026-11-16-01 ; R-2950 ; R-2955 ; R-<ligne du scellement> |`
  Cinq champs, exprès : même recopiée par erreur au registre propre, une ligne de cinq champs n'y serait pas lue comme une clé
  de bonne forme… **non : je retire cet argument**, une ligne ignorée en silence serait justement la forme écartée en (c). Le
  cinquième champ ne sert qu'à porter la décision ; la garde contre la recopie est l'en-tête et la ligne R-. Si la mère préfère
  quatre champs (format identique au registre propre), la décision va dans la ligne R- seule ; les deux conviennent.
- Ligne R- de `registres/decisions.md` : chemin, empreinte entière, heure, « avant `CODE-BBIS` » (le registre propre ne
  porte pas encore cette clé), état de l'étape B relevé, mention de m4, m5 et de l'affaiblissement dits à Lazar.

## 7. Mot du directeur, identifiants, marqueurs

- Mot recopié verbatim : « go recos sur les 6 décisions, on a dit go recos pendant l'autonomie » — identique, au caractère,
  à la ligne `GO-2026-11-16-01` de `registres/go.md` (ligne 342). La « lecture » du point (1) est recopiée exactement aussi.
  Le mot de R-2802 (« Recommandation : (b), confiance 0,65 : go ») est exact.
- Aucun identifiant de modèle dans l'addendum (recherche des noms de familles de modèles, sans casse : rien).
- Marqueurs restants : un seul, `<<ETAT_ETAPE_B_AU_SCELLEMENT_ADDENDUM>>`, deux occurrences (lignes 233 et 282), listé (P1).
  S'y ajoutent, non marqués mais à réécrire au scellement : le titre et la ligne de statut (« brouillon 1 »), la date, P2
  (tranché par R-2955), et la mesure de la quatrième passe si elle entre.

## Corrections (couples exacts ; numéros de ligne du brouillon 1)

**C1 (M1) — ligne 30.** Ancien : « ne valent ici que par cette ligne. » Nouveau : « ne valent ici que par cette ligne. **Hors
des dix-sept couples** (a1 à a5, b1, b2, c1 à c10) que R-2933 a portés à Lazar : les ajouts m4 (premier écart) et m5 (deuxième
écart), mineurs de la même contre-lecture ; m4 écrit ce que `marche_v3` fait déjà, m5 étend R-PILE à la sonde d'ENC (la
réserve s'écrit plus souvent, sans changer d'issue). Ils ont été dits à Lazar, avec l'affaiblissement du § 5, point 4, avant
le scellement : <<MESSAGE_A_LAZAR_M4_M5>> (heure, ligne R-). »

**C2 (M2) — renommage.** Remplacer « E1 » … « E8 », quand ils désignent un écart, par « EC-1 » … « EC-8 » aux 22 lieux
suivants, et nulle part dans les blocs : titres des lignes 42, 75, 98, 115, 132, 149, 166, 183 ; renvois des lignes 112, 129,
146, 212, 213, 214, 228, 230, 251, 256, 273, 276, 277, 278. Ajouter à la ligne 40, après « dans les blocs. » : « Les écarts
sont nommés EC-1 à EC-8 pour ne pas être confondus avec les états E0 à E6 du texte scellé. »

**C3 (P2 tranché, R-2955).**
- lignes 6 et 7. Ancien : « et l'inscription de sa ligne (point ouvert P2 du § 7), **avant `CODE-BBIS`** ». Nouveau : « et
  l'inscription de sa ligne au registre voisin `registres/t07-etape-b-bis-v1-addenda-v1.md` et d'une ligne R- de
  `registres/decisions.md` (décision de la mère R-2955, § 7), **avant `CODE-BBIS`** ».
- ligne 26, après la citation de la lecture, ajouter : « « Au registre propre » est la formule de la mère, non le mot de
  Lazar ; le registre propre n'admet que huit clés (§ 7) : inscription au registre voisin, R-2955, dit à Lazar. »
- ligne 275. Ancien : « et sa ligne (P2) ». Nouveau : « et sa ligne `ADDENDUM-ECART-1-BBIS` du registre voisin ».
- lignes 284 à 295 (P2) : garder l'exposé de la contrainte jusqu'à « rendrait donc la course illisible. », puis remplacer
  « Options : … l'exige. » par : « **Décision de la mère (R-2955)** : registre voisin à nom neuf
  `registres/t07-etape-b-bis-v1-addenda-v1.md` (lu par aucun code ; nom hors des motifs d'extraction de l'amorce) et ligne R- ;
  aucune ligne au registre propre ni au registre partagé ; une forme de clé que le code ignorerait est écartée (ce serait
  passer une garde par sa forme). Fichier scellé : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`. »

**C4 (§ 5, complétude).**
- ligne 251. Ancien : « seul son déterminisme sur la carte est vérifié. » Nouveau : « seul son déterminisme sur la carte est
  vérifié, et le déterminisme ne prouve pas la justesse (une erreur déterministe propre à la carte après la troisième époque
  passe les trois contrôles). Si le réglage retenu du couple tiré est linéaire, sa sonde lue est comparée comme au texte
  scellé et les sondes « attention » du contrôle ne sont pas des sondes lues ; les sondes « attention » des autres couples et
  celles d'ENC ne reçoivent aucun contrôle, comme au texte scellé. »
- après la ligne 254, ajouter trois points :
  « 6. le réglage retenu peut dépendre de la pile : sans signal, l'étendue 0,0074 dépasse le seuil d'ex aequo 0,005 ; la
  famille, la couche ou la régularisation retenues, donc l'écriture même de R-PILE, peuvent changer d'une pile à l'autre
  (`diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`, lignes 24 et 106) ; l'état rapporté est celui de la carte de la
  course ;
  7. les régimes mesurés sont ceux d'un bruit gaussien isotrope ; entre les aires 0,47 et 0,56, et pour un signal faible mêlé
  à une forte mémorisation, rien n'est mesuré (même pièce, ligne 108) ; l'horizon de 3 époques a été fixé sur ces trajectoires
  synthétiques (`diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…`, lignes 161 à 169) ;
  8. un couple dont la sonde finale est en échec n'est jamais contrôlé ; le contrôle vient à la fin de l'apprentissage : une
  erreur de chaîne coûte tout l'apprentissage (mineur m7 de la contre-lecture du brouillon 6 ; le pire cas du devis compte
  déjà une relance complète). »
- ligne 247, après « 3,4·10⁻⁸ à 7,8·10⁻⁷) », ajouter : « ; le cinquième artefact non attrapé, actions et étiquettes permutées
  ensemble, n'est pas une erreur ».

**C5 (§ 6) — ligne 278, à la fin.** Ajouter : « **Recevabilité** : un verdict de B bis qui ne cite pas cet addendum, son
empreinte et sa ligne n'est pas scellé ; la mère le vérifie avant de le soumettre à Lazar. L'addendum figure nommément dans
la liste des fichiers donnés au lecteur du verdict (R13) et dans `registres/etat.md` ; la table conjointe et tout document qui
cite une aire de B bis le citent aussi. Il n'entre pas dans la liste de la fiche `CODE-BBIS` (`marche_v3` vérifie chaque
fichier de la fiche sur l'instance, où il n'est pas extrait). »

## Mineurs (sans couple imposé, sauf mention)

- **m1** — § 0, ligne 15 : dire que « relance sous ce texte » (liste d'arrêt scellée, ligne 186) se lit désormais « sous ce
  texte et cet addendum ».
- **m2** — § 2, ligne 37 : « 32 lignes de plus en tête » → « 32 lignes de plus après le titre ».
- **m3** — § 3, ligne 213 : après « Calcul et dépense … inchangés », renvoyer au point 8 neuf du § 5 (arrêt tardif) et dire le
  surcoût sur la carte (au plus une linéaire de 300 époques, une attention de 3 et deux de 300 ; docstring de
  `validation_imbriquee_v3`).
- **m4** — § 3 : renvoyer au point 6 neuf du § 5 (le choix du réglage n'est pas modifié par l'addendum, mais il dépend de la
  pile).
- **m5** — § 4, ligne 223 : « § 3 et § 8 » → « § 3 (ligne 183) » ; ajouter le relevé de cette contre-lecture (code 2 à
  2026-11-16T00:42:38Z, témoin positif) et celui de la mère au scellement.
- **m6** — premier écart, bloc « nouveau » : « la sonde « attention » de 300 époques du couple » est ambiguë quand le réglage
  retenu est linéaire (c'est alors une sonde apprise sur la carte au réglage « attention » de mêmes couche et régularisation).
  **Ne pas toucher au bloc** ; le dire dans la « Raison » (la correction C4 le couvre).
- **m7** — § 8 : R-2931 et R-2955 manquent à la liste des lignes à donner au contre-lecteur.
- **m8** — si la mesure de la quatrième passe entre au texte : seulement aux § 4 (deuxième puce) et § 5 (point 5), avec chemin
  et empreinte ; les huit blocs restent ceux de `991ab560…` ; le rejeu du programme du § 1 sur la version scellée le prouve ;
  une vérification éclair par un lecteur neuf suffit alors (différentiel du brouillon 1 à la version scellée).

## Ce que je n'ai pas vérifié

- Je n'ai rejoué aucun essai (`pytest` interdit) : « 183 passés » est repris de la contre-lecture du brouillon 6.
- Je n'ai pas rejoué les scripts de couples un à un ; l'égalité finale (texte scellé + huit remplacements = brouillon 6
  complété) les rend superflus pour la question posée.
- L'état de l'étape B de T0.7 (P1) : à relever par la mère, par les noms.
- La quatrième passe : rien lu d'elle.
- Lignes R-2844, R-2869, R-2902, R-2746 : débuts seulement (420 caractères), assez pour l'objet et la date.

## Incidents de ma main

- Une première recherche dans `registres/go.md` (motif de date) a rendu plus que les lignes visées ; la sortie, trop longue,
  a été rangée par l'outil dans un fichier de résultats hors du dépôt ; je n'en ai vu que l'aperçu (début d'une ligne de GO du
  2 novembre, sans rapport). Seconde recherche bornée aux trois lignes voulues.
- Début (420 caractères) de R-2953, hors de la liste donnée : identifiant et étiquette de la machine de la quatrième passe,
  heure de création ; aucun résultat.
- Mon premier programme alignait mal le titre (décalage des 32 lignes) et affichait une fausse différence à la ligne 1 ;
  corrigé par un second programme à alignement par `difflib` ; les deux sont gardés dans le bloc-notes.
- Présence des trois variables `GIT_*` testée par leur nom dans l'interpréteur de commandes (`eval` sur le nom, aucune valeur
  affichée) ; ni `env` ni `printenv`. Quatre `git ls-remote` en lecture ; un `git show` d'un seul fichier (brouillon 6 au
  commit `6c346a03`) vers `sha256sum`, sans extraction.
- Dans ce rapport, § 6, j'ai écrit puis retiré un argument (ligne à cinq champs) : laissé visible plutôt que réécrit.
- Aucune écriture hors de ce rapport, de son compagnon et de mon sous-dossier du bloc-notes.

## Annexe — programme du contrôle mécanique (`verif2.py`)

```python
import re, sys, difflib, pathlib
W = pathlib.Path(sys.argv[1]); B = W/"brouillons/T0.7-etape-B-bis-v1"
add = (B/"T0.7-etape-B-bis-v1-addendum-ecart-v1-brouillon1.md").read_text(encoding="utf-8")
sc = (W/"prereg/T0.7-etape-B-bis-v1.md").read_text(encoding="utf-8")
b6 = (B/"T0.7-etape-B-bis-v1-brouillon6.md").read_text(encoding="utf-8")
secs = re.split(r"^### (E\d) ", add, flags=re.M)
res=sc
for i in range(1,len(secs),2):
    a,n = re.findall(r"```text\n(.*?)\n```", secs[i+1], flags=re.S)
    assert res.count(a)==1; res=res.replace(a,n)
for a,n in (("aucun : arrêt (erreur de chaîne). Raison, écrite avant toute lecture :","aucun : arrêt (erreur de chaîne) ; après un arrêt de la garde de débit, aucun contrôle n'est joué (aucun score n'est écrit). Raison, écrite avant toute lecture :"),
            ("(écrite dès qu'une sonde finale lue est de la famille « attention » :","(écrite dès qu'une sonde finale lue, celle d'une source ou celle d'ENC, est de la famille « attention » :")):
    assert b6.count(a)==1; b6=b6.replace(a,n)
R=res.split("\n"); C=b6.split("\n")
sm=difflib.SequenceMatcher(None,R,C,autojunk=False)
for t,a,b,c,e in sm.get_opcodes():
    if t!="equal": print(t,"scelle+E lignes",a+1,"-",b,"| b6c lignes",c+1,"-",e)
# le bloc insere
for t,a,b,c,e in sm.get_opcodes():
    if t=="insert":
        print("--- bloc insere, debuts de ligne :")
        for x in C[c:e]: print("   ",x[:110])
```

Sortie : sept lignes « replace », scellé + écarts lignes 1, 5, 22, 76, 93, 116, 293 contre brouillon 6 complété lignes 1 à 33,
37, 54, 108, 125, 148, 325 ; rien d'autre.
