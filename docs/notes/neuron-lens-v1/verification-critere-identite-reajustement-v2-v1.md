# Vérification de la version 2 du critère d'identité du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), de son programme de comparaison et de l'erratum du devis — v1

- Heure (`date -u`) : 2026-11-19T10:31:33Z.
- Vérificateur : le contre-lecteur de la v1 (sous-agent, modèle Fable 5.2, `claude-fable-5-2`) ; il n'a écrit ni le critère, ni le
  programme, ni ses essais, ni l'erratum.
- Objet : branche `claude/brave-galileo-jhp684`, commit `de8368978e91bdd74e3337f57db906676456bb64`, pièces lues par l'identifiant
  du commit. Empreintes recalculées, toutes égales à leur compagnon : critère v2
  `fc706d8e5bd0bb75942e17844a450ca82520972746e1b7233881817a8c3f679c` ; programme de comparaison
  `src/controle_ia/neuron_lens/comparer_reajustement_v1.py` `247b695911d08045b505d5b1c443734c0e181ab82998f299a5c2525d1553f897` ;
  ses essais `0f5b5bdbab50101c8ae5e28f096377e3e1fd2135aaca6e65be5f3c40f7d6f969` ; erratum du devis
  `c7915a23402515cdc2a4af61be74993cff32b69ff4b634868383ab1d14c8f6f9` ; calcul de l'écart entre chemins `2084dae7…`, sortie
  `21d04198…` ; essai du nom de fichier `1893d03e…`, sortie `3a2dbb16…` ; manifeste de la course du 18 `b90c1514…`.
- Fait, dans un dossier à part du bloc-notes, sur une copie des fichiers du commit : les 19 essais rejoués ; 53 gardes ou calculs
  faussés un à un sur des copies du programme, essais rejoués à chaque fois, avec un témoin non modifié ; 20 sondes du programme
  d'origine sur des cas qu'aucun essai ne joue ; le calcul de l'écart entre chemins rejoué (sortie identique à l'octet). Non rejoué :
  l'essai du nom de fichier (`torch` absent de mon environnement) ; je m'en tiens à sa sortie scellée.
- Mêmes interdits que pour la contre-lecture, tenus. Aucune dépense, aucune machine, aucun modèle, aucun commit, aucun fichier
  existant modifié. Aucun refus d'outil.

## Conclusion

**Pas avant : sept corrections (D1 à D7), dont quatre au programme de comparaison.** Le texte du critère répond aux corrections C1 à
C6, presque toutes à la lettre, et les 19 essais passent. Mais le programme prononce « même lentille, octets identiques » sur des
pièces qui se contredisent, dès que le champ de l'empreinte est égal ; il écrit « octets différents » quand l'empreinte neuve
manque ; les essais ne fixent ni la tolérance de 10⁻³ ni la valeur absolue ; et la phrase permise au billet ignore les deux séries
de R que le critère fait désormais rapporter. Comme le critère cite l'empreinte du programme et ses 19 essais, il ne peut pas être
scellé avant le programme corrigé.

Dernière ligne des essais rejoués : `19 passed in 0.40s`.

## 1. Les corrections C1 à C6 sont-elles faites ?

| correction | état | écart |
|---|---|---|
| C1, mention et définition du deuxième palier | **faite, à la lettre**, et au-delà (nom du fichier, empreinte du texte de la fonction) | le programme ne compare du manifeste que le commit du code voisin : D2 |
| C2, grandeur aveugle, séries de R, S | **faite** au minimum annoncé (séries rapportées sans critère, raison donnée) | la phrase du billet n'en tient pas compte : point 2 et D5 |
| C3, ce que chaque mention autorise | **faite, à la lettre** (primauté sur le devis, phrases en deux langues, couche stable dans les deux ajustements, parenthèse retirée) | — |
| C4, audit dans les deux sens, programme essayé | **faite dans la lettre**, pas dans l'esprit | le programme n'exécute pas l'audit ; le premier palier n'a aucun contrôle de cohérence ; essais incomplets : D1 à D4, D6 |
| C5, rattachement de l'écart entre chemins, libellé de la tolérance | **faite, à la lettre** ; chiffres rejoués à l'identique ; raison de la valeur absolue donnée | — |
| C6, qui applique | **faite, à la lettre** | deux échappatoires : point 4 et D6 |
| mineures 1 à 4, 6, 7 | faites ; mineure 5 renvoyée au lanceur v4 : admis, à vérifier à sa contre-lecture | l'heure de l'en-tête est encore à venir (« entre 10:20 et 10:45 UTC », commit à 10:21:50Z) |

## 2. Rapporter les deux séries de R sans critère : défendable ? — **Oui ; mais la marge reste dans ce que le billet écrit.**
La raison donnée tient : aucune pièce ne mesure la variation de ces séries, une tolérance y serait une seconde convention, et le
deuxième palier n'établit déjà ni l'identité ni le transport du verdict. Le choix ne change donc aucune mention.
La marge après coup est ailleurs. Les séries ne peuvent que montrer un déplacement, et rien ne dit ce qu'on en fait :
- la phrase permise au deuxième palier écrit toujours « La seule comparaison possible porte sur la différence entre les deux
  moitiés » (l. 78-79) : c'est faux pour R depuis que les séries sont rapportées, et la phrase reste la même que les séries bougent
  ou non ;
- rien n'oblige le billet, le texte de lecture ni l'avertissement à Lazar à donner ces chiffres ; rien n'interdit de les citer
  seulement s'ils sont flatteurs (« la distance à la lentille publique est inchangée »).
Le billet n'en tient donc pas compte. Correction D5 : les chiffres deviennent obligatoires, dans les deux sens, sans qualificatif.

## 3. Le programme de comparaison

**Les 19 essais passent.** Un `nan`, un `inf`, une valeur absente, un texte, 62 valeurs, une cible de plus, des séries vides, un
`meta` absent rendent bien « non comparable », sans maximum calculé, **quand les empreintes des fichiers diffèrent** (essais, et
sondes S15 à S18). **Ce n'est plus vrai quand le champ de l'empreinte est égal** : la branche du premier palier rend sa mention
avant tout contrôle.

### Sondes du programme d'origine (non modifié)
| sonde | cas | mention rendue | attendu |
|---|---|---|---|
| S1 | même empreinte de fichier, une différence entre moitiés déplacée de 0,05 | **premier palier, « même lentille »** | anomalie |
| S2 | même empreinte, un `nan`, `meta` changé, `n_docs` changé | **premier palier** (« préalables tous tenus : faux » seulement noté) | anomalie |
| S3 | même empreinte, taille différente | **premier palier** | anomalie |
| S4, S5 | empreinte neuve absente ou vide, valeurs égales | **deuxième palier, « octets différents »** | « non comparable » |
| S6, S7 | lentille R sans pièces d'export | deuxième ou premier palier, sans un mot ; séries et compte des matrices absents | signalé |
| S8 | la référence comparée à elle-même, même manifeste | **premier palier** | refus : les deux côtés sortent du même fichier |
| S9 | même empreinte, export de référence sans empreintes de matrices | premier palier (« 0 couche égale sur 0 ») | anomalie |
| S10 | export neuf sans le champ des séries | deuxième palier, séries « 0 couche » sans alerte | signalé |
| S19 | champ `finies` faux (sommes non finies) | deuxième palier | « non comparable » |
| S20 | référence et course neuve échangées | deuxième palier | refus : la référence n'est pas vérifiée par son empreinte |
| S12 à S14 | écart de −2 × 10⁻³, de −0,999 × 10⁻³, de +1,001 × 10⁻³ | « différente », deuxième palier, « différente » | conforme |

Le premier palier est le seul qui établit l'identité et transporte le verdict du 18. Or le programme le prononce sur l'égalité de
deux chaînes lues dans deux fichiers, dont l'un sera écrit par un lanceur qui n'existe pas encore. Le contrôle de provenance que le
§ 5 confie à l'audit n'est exécuté par aucun programme.

### Gardes faussées une à une : 30 tuées par les essais, 23 survivent
Témoin non modifié : 19 essais passés. Survivent à leur retrait ou à leur altération :

| garde ou calcul faussé | portée |
|---|---|
| tolérance portée à 1,5 × 10⁻³ | **décide de la mention** : les essais ne jouent que 0,9 × 10⁻³ et 2 × 10⁻³ |
| comparaison stricte (« < » au lieu de « ≤ ») | **décide de la mention** : le bord n'est pas essayé |
| écart signé au lieu de la valeur absolue | **décide de la mention** : aucun essai ne déplace une valeur vers le bas ; une lentille dont les valeurs baissent de 0,05 passerait |
| premier palier prononcé quand l'empreinte manque des deux côtés | **décide de la mention** |
| `meta` absent tenu pour égal | **décide de la mention** |
| séries vides acceptées ; mêmes cibles non exigées | décident de la mention si la pièce de référence est abîmée ou si une cible s'ajoute |
| nom de fichier, commit du code voisin, texte de la fonction : absents des deux côtés acceptés | préalable |
| finitude non vérifiée sur `diffs` (simple précision) ; sur le côté de la référence ; type de la valeur ; booléen accepté ; valeurs qui ne sont pas des listes | préalable (dans plusieurs de ces cas le programme s'arrêterait sur une erreur plutôt que de rendre une mention) |
| `n_docs` et `next_doc` non vérifiés du côté de la référence | préalable |
| garde de finitude du maximum retirée | redondante, jamais essayée |
| **séries de R jamais rapportées ; séries de R toujours nulles** | **rapporté** : aucun essai ne lit ces séries, qui sont toute la correction C2 |
| écart relatif toujours nul ; écart sur `diffs` toujours nul ; signe de la table perdu ; compte des matrices égales faux | rapporté |

Tuées, donc bien gardées : comptes différents ; finitude du côté neuf et sur `diffs_float64` ; `meta` changé ; `n_docs`,
`next_doc`, nom de fichier, commit du voisin, texte de la fonction changés ; préalables ignorés ; tolérance à 10⁻² ; décision prise
sur `diffs` ; premier palier ; anomalie des matrices ; reprise ; déclencheurs (i) à (iv) ; changement de côté du seuil et sa
valeur ; mention de S ; sortie non écrasée.

## 4. Qui calcule les écarts après la course ? — **Écrit ; deux échappatoires.**
Le § 7 dit : la mère ou un agent neuf qu'elle lance, pas la session des lentilles, avant toute lecture d'une mesure ; verdict écrit
et scellé par la mère. Restent :
1. **D'où viennent les pièces.** « Sur les pièces versées » ne dit pas par qui. Si la session des lentilles remet les fichiers, elle
   choisit ce que la mère compare. Le programme ne vérifie ni l'empreinte des pièces de référence, ni que le manifeste neuf est
   celui du résultat neuf (le résultat porte pourtant l'empreinte de son manifeste), ni que les deux courses sont distinctes.
2. **Ce qui est facultatif.** Les pièces d'export de R et l'indication d'une reprise sont des options de la ligne de commande :
   les oublier ne produit aucune alerte (S6, S7).
L'audit du § 5 est dit « par programme » ; aucun programme ne le fait, et personne n'en est chargé.

## 5. L'erratum du devis suffit-il ? — **Pour la phrase visée, oui ; pour ce que Lazar lira, non.**
- La phrase « identité par les paliers 1 et 2 » (devis v2, § 7, décision 1) est bien corrigée, et le § 4 du devis est bien dit
  remplacé par le critère.
- Deux autres phrases du devis portent la même idée et ne sont pas visées : l'enjeu de la décision 1, « ranger des lentilles dont on
  sait si ce sont celles qui ont été jugées » (l. 150) ; et le § 2, « non pas l'identité des lentilles (les paliers 1 et 2 sont
  communs) » (l. 41-42).
- Une conséquence manque pour le choix de la variante : au deuxième palier, la lentille rangée par la variante A (ajustement seul)
  n'a aucune mesure propre ; seule la variante B (course rejouée) lui en donne. Lazar doit le lire **avant** d'accorder la dépense,
  pas « avant tout usage ».
- Forme : la règle des errata (`docs/notes/allegement-procedure-v1/proposition-allegement-procedure-v1.md`, `2568dd44…`, point 7)
  les réserve aux classes B et C, « sans effet sur un seuil, une garde ou une revendication ». Le devis est de classe A et l'erratum
  remplace un seuil. À la mère de dire si elle l'admet ; dans tous les cas, c'est le texte de la décision soumis à Lazar pour la
  ligne de calcul (accord GO-2026-11-19-33 : paramètres non tranchés) qui doit porter les phrases corrigées.

## Corrections (texte avant et après)

**D1 — Premier palier : cohérence exigée (critère, l. 65-66 ; programme, l. 148-157).**
- Avant : « 4. **Anomalie** : pour R, empreinte du fichier égale mais une empreinte de matrice des moitiés différente → mention
  suspendue, nœud de Lazar. »
- Après : « 4. **Anomalie** (mention suspendue, nœud de Lazar) : empreinte du fichier égale **et** l'un de ces faits : un préalable
  du point 2 manqué ; une taille différente ; un écart maximal sur `diffs_float64` supérieur à 10⁻⁹ (les mêmes sommes donnent la
  même valeur, à l'arrondi du calcul près) ; pour R, des pièces d'export absentes ou incomplètes, ou une empreinte de matrice des
  moitiés différente. »
- Programme : dans la branche du premier palier, calculer les préalables et la table des écarts, et suspendre dans ces cas.
  Essais à ajouter : S1, S2, S3, S9.

**D2 — Préalables de provenance (critère, l. 44-47 ; programme, `preconditions` et `main`).**
- Avant : « […] `n_docs` [466, 466] et `next_doc` 932 des deux côtés ; même nom de fichier ; même commit du code voisin ; même texte de
  `_split_half_64` […]. »
- Après : ajouter « ; empreintes des deux fichiers d'ajustement présentes et bien formées, tailles présentes ; `finies` vrai des deux
  côtés ; pièces de référence d'empreintes égales à celles du § 1, vérifiées par le programme ; course neuve distincte de celle du
  18 (identifiant de course et heure de début différents) ; manifeste neuf d'empreinte égale à celle que porte le résultat neuf ;
  champs `ajustement`, `correctifs`, `graines`, `modele`, `revision` et `corpus` de la configuration du manifeste égaux à ceux du 18 ». La phrase
  permise au billet affirme « même code, même corpus, mêmes graines » : seuls ces champs le portent.
- Essais à ajouter : S4, S5, S8, S19, S20 ; un champ du manifeste changé. Le cas sain « pièces du 18 contre elles-mêmes » devient un
  cas refusé ; le cas sain du premier palier se joue sur une copie dont l'identifiant de course et l'heure de début diffèrent.

**D3 — Pièces d'export de R obligatoires (programme, l. 132-147, 195-196).**
- Avant : `if lentille == "R" and eref is not None and eneuf is not None:` ; `--ref-export` et `--neuf-export` facultatifs.
- Après : pour R, les deux pièces sont exigées ; 31 couches de matrices et 28 couches par série des deux côtés, valeurs finies ;
  sinon « non comparable » (ou anomalie au premier palier, D1). Le critère l'écrit parmi les préalables : « pour R, pièces d'export
  présentes et complètes des deux côtés ». Essais à ajouter : S6, S7, S10.

**D4 — Essais à ajouter pour les gardes qui survivent (essais ; critère, l. 110-115).**
- Avant : « bord de tolérance (0,9 × 10⁻³) → palier 2 ».
- Après : « bord de tolérance : 0,999 × 10⁻³ → palier 2 ; 1,001 × 10⁻³ → « différente » ; −2 × 10⁻³ → « différente » ; la constante
  vaut 10⁻³ », plus un essai par ligne du tableau des survivantes : empreinte absente des deux côtés ; `meta` absent ; séries vides
  des deux côtés ; une cible de plus ; nom, commit, fonction absents des deux côtés ; pour R, une valeur d'une série déplacée d'une
  quantité connue et retrouvée dans la sortie, 28 couches comptées ; 30 matrices égales sur 31 comptées ; écart relatif, écart sur
  `diffs` et signe de la table vérifiés sur un artefact.

**D5 — La phrase du billet et les séries de R (critère, l. 77-82 et 88-91).**
- Avant : « La seule comparaison possible porte sur la différence entre les deux moitiés du corpus, couche par couche : elle
  s'écarte d'au plus [écart mesuré] de celle du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³). Cette grandeur ne
  voit pas un déplacement commun aux deux moitiés : nous ne savons pas si la lentille réajustée lit comme celle du 18 novembre. »
- Après : « Deux comparaisons restent possibles. La différence entre les deux moitiés du corpus, couche par couche, s'écarte d'au
  plus [écart mesuré] de celle du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un
  déplacement commun aux deux moitiés. Pour la lentille R seulement, l'écart maximal de chaque matrice à la lentille publique et à
  l'identité change d'au plus [valeur] et [valeur] d'une course à l'autre, pour des écarts qui valaient de [valeur] à [valeur] le
  18 novembre ; aucun seuil n'était fixé d'avance pour ces deux séries. Pour la lentille S, aucune comparaison de ce genre n'existe.
  Nous ne savons pas si les lentilles réajustées lisent comme celles du 18 novembre. »
  (*“Two comparisons remain. The per-layer split-half difference deviates by at most [x] from the 18 November values (tolerance
  fixed in advance, by convention, at 10⁻³); this quantity is blind to any shift common to both halves. For lens R only, the largest
  entrywise gap of each matrix to the public lens and to the identity changes by at most [y] and [z] between the two runs, for gaps
  that ranged from [a] to [b] on 18 November; no threshold had been fixed in advance for these two series. No such comparison
  exists for lens S. We cannot establish that the refitted lenses read like those measured on 18 November.”*)
- Règle à ajouter : « Ces chiffres sont **obligatoires**, quel que soit leur sens, dans toute phrase du billet et du texte de lecture
  qui cite la lentille R au deuxième palier, et dans l'avertissement à Lazar. Aucun qualificatif ne leur est attaché (« inchangé »,
  « stable », « négligeable », « a bougé »), faute de seuil fixé d'avance. » Aux phrases interdites, ajouter : « la distance à la
  lentille publique est inchangée », ou toute phrase qui tire des séries un appui à la proximité.

**D6 — Qui fait l'audit, d'où viennent les pièces (critère, l. 100 et l. 119-121).**
- Avant (l. 100) : « **Audit, par programme, sans lire aucune mesure de la course** : provenance des deux côtés […] »
- Après : « **Audit, fait par la mère ou par l'agent neuf du § 7, sans lire aucune mesure de la course** : le programme du § 6 donne
  les préalables, la comparaison des manifestes et la table des écarts ; la relecture de l'empreinte au lieu de rangement, les
  versions du pilote et le modèle de carte sont relevés à la main, avec chemin et empreinte ; l'audit dit ce qui vient du programme
  et ce qui est relevé à la main. Provenance des deux côtés […] »
- Avant (l. 119-121) : « Les écarts sont calculés par le programme scellé du § 6, sur les pièces versées, **par la mère ou par un agent
  neuf qu'elle lance**, et non par la session des lentilles, avant toute lecture d'une mesure de la nouvelle course ; »
- Après : « Les écarts sont calculés par le programme scellé du § 6, dont l'empreinte est vérifiée avant le lancement, sur les pièces
  **prises sur la branche de résultats poussée par la machine** (commit noté), jamais sur une copie remise par la session des
  lentilles, **par la mère ou par un agent neuf qu'elle lance**, et non par la session des lentilles, avant toute lecture d'une
  mesure de la nouvelle course ; pour R, les deux pièces d'export sont toujours fournies ; l'indication d'une reprise est lue au
  journal de la course ; la ligne de commande et la sortie sont versées scellées avec le verdict ; »

**D7 — Erratum du devis.**
- Avant : une seule phrase corrigée (§ 7, décision 1, option A) et le § 4 remplacé.
- Après, à ajouter : « § 7, décision 1, enjeu : lire « ranger des lentilles ; on ne saura si ce sont celles qui ont été jugées qu'au
  palier 1 ». § 2 : lire « (les paliers 1 et 2 sont communs ; seul le palier 1 établit l'identité) ». Conséquence pour le choix de la
  variante : au palier 2, la lentille rangée par la variante A n'a aucune mesure propre ; seule la variante B lui en donne. » Et la
  décision soumise à Lazar pour la ligne de calcul recopie ces phrases.

## Remarques mineures
1. En-tête du critère, l. 3-4 : heure à venir ; la relever par `date -u` au scellement.
2. Programme, l. 34 et l. 121 : la mention écrit « 10⁻³ » en dur alors que la tolérance est un paramètre de `comparer` ; retirer
   le paramètre ou bâtir la mention sur lui.
3. Critère, l. 12 : « commit `cdb854c0` ou plus récent » ; les empreintes suffisent, « ou plus récent » peut partir.
4. La version corrigée du programme et celle du critère prennent des noms neufs ; le critère cite alors l'empreinte neuve du
   programme et le nombre de ses essais.

## Ce qui a servi à cette vérification (hors dépôt, dossier propre du bloc-notes)
`mutations.py` (53 altérations par remplacement de texte, une copie par altération, témoin en tête) et
`sondes_gardes_absentes.py` (20 appels de `comparer` sur les pièces du 18 altérées en mémoire). Aucun n'écrit dans le dépôt.
