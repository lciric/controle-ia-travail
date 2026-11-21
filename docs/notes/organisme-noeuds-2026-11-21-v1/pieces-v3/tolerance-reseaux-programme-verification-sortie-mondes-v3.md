# Tolérance propre aux réseaux du programme de vérification de la sortie des mondes — règle v3, corrigée après la contre-lecture de la note d'écart — sans effet avant le scellement de la note

- **Nature.** Règle de travail pour le programme de vérification de la sortie de l'auteur des mondes plantés (instrument, classe B). Elle met en œuvre la note d'écart, et rien de plus. Conçue et corrigée par Claude Fable 5.2, concepteur de la session mère pour l'organisme d'idéation, le 2026-11-21, de 19:15:54Z à 19:21:22Z (`date -u`).
- **Remplace** `docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v2/tolerance-reseaux-programme-verification-sortie-mondes-v2.md` (`3806ff34cebfe862dbb400342915206103a7f51430de19265cd04a005ea1d776`), qui reste intacte (règle R12). Ce n'est plus une extraction à l'octet de la source.
- **Cause.** La contre-lecture de la note d'écart par la session de l'organisme, verdict « À corriger » : `docs/notes/organisme-noeuds-2026-11-21-v1/contre-lecture-note-ecart-tolerance-v1/contre-lecture-note-ecart-tolerance-v1.md`, branche `lot/compte-organisme-v1` (`b84519a390f50850a6a71898f182e319a50f889a082682b078dff3eec736dee9`, égale à son compagnon). Son mode 4 et sa première trouvaille de côté : la règle v2 (point 5, l. 19) juge « conforme au pas du réseau » aussi sous l'unité brute, ce que la note n'accorde pas ; le programme doit suivre la note.
- **Statut : sans effet.** Lazar a accordé l'écart et sa valeur (GO-2026-11-21-66), mais rien ne joue avant le scellement de la note d'écart. D'ici là : 0,005 partout. La phrase de l'extraction v2, « La valeur 0,02 n'est retenue par personne », est caduque depuis cet accord ; il reste vrai qu'aucune session ne l'applique avant le scellement.
- **Va avec** le projet de note d'écart v2, même dossier : `projet-note-d-ecart-tolerance-du-controle-par-l-aire-lois-arrondies-v2.md`. Les mots de cette règle sont ceux de sa section « Les mots de cette note ».

## Table « remarque → correction »

« v2 » désigne la règle v2 ; « l. » ses lignes. Les remarques 1 à 7 viennent de la contre-lecture ou du mandat de la mère ; la remarque 8 réunit ce que j'ajoute sans qu'on me l'ait demandé.

| n° | remarque, et d'où elle vient | correction, et où elle est |
|---|---|---|
| 1 | Contre-lecture, mode 4 et trouvaille de côté 1 ; mandat de la mère : la v2 (point 5, l. 19) applique « conforme au pas du réseau » aussi sous l'unité brute ; la note ne l'accorde pas ; le programme suit la note. | § 2, point 6 : « unité brute constatée » se juge à 0,005 seul, « conforme au pas du réseau » jamais sous l'unité brute. § 1, « Rang » : la note prime. Conséquence dite au § 5, point 3. Épreuve et mutation au § 4. |
| 2 | Contre-lecture, correction demandée 1 : la conversion tient à chaque décalage de la famille, dans chaque tranche. | § 2, point 4. La v2 le disait déjà (point 3, dernière phrase) ; la v3 le dit seul, avec « un seul couple … suffit ». Épreuve « famille mixte » au § 4. |
| 3 | Contre-lecture, correction demandée 2 : raisons exhaustives ; le cas d'une aire encadrante réalisée hors du plafond alors que l'autre est dans le plafond ; une raison pour l'ordre. | § 2, point 7 : quatre raisons par couple, dans un ordre fixe, dont « aire encadrante hors du plafond » et « aires non croissantes dans la tranche » ; raison de la famille ; preuve au relevé de méthode du projet de note v2, pas 9. |
| 4 | Contre-lecture, correction demandée 3 : définir « arrondie » et la portée. | § 1, « tranche arrondie » : le type `arrondi` au premier niveau, décidé sur l'objet écrit par l'auteur ; § 2, points 2 et 3 : la règle joue couple par couple. |
| 5 | Contre-lecture, correction conseillée 5 : la condition d'ordre est redondante. | § 2, point 8 : garde de cohérence, jamais raison d'une famille. La v2 (point 7) en faisait une cause de « non lisible » à elle seule. |
| 6 | Contre-lecture, trouvaille de côté 2 : un saboteur qui n'est pas une simple translation. | § 2, point 11 : constat nommé au compte rendu. |
| 7 | Contre-lecture, trouvaille de côté 3 et conseil : porter les corrections dans les épreuves de mutation du programme, avec une raison attendue pour chacune ; écrire l'artefact d'unité brute avec le facteur d'écart type. | § 4 : table des épreuves et des mutations. |
| 8 | Ajouts du concepteur. | § 2, point 9 : ce que le programme rend sans l'empreinte de la note, et à quelle tolérance il lit alors ses raisons ; § 2, point 10 : comparaisons sur les valeurs calculées, et précision dite pour un décalage posé sur un multiple du pas ; § 3 : statut mis à jour après l'accord ; § 5 : quatre limites de plus. |

La correction conseillée 4 de la contre-lecture (ligne d'attestation) ne touche pas la règle : elle est portée au projet de note v2, section « Conditions ».

Ce qui ne bouge pas : la valeur 0,02 ; l'égalité à 10⁻⁹ près ; les deux aires encadrantes, paliers et sauts ; le nom « conforme au pas du réseau » et ce que le compte rendu en donne ; la condition d'empreinte ; les trois issues du contrôle.

## 1. Rang et mots

**Rang.** La note d'écart, une fois scellée, prime sur cette règle. La règle la met en œuvre pour le programme ; elle n'accorde aucune conversion que la note n'accorde pas. Où elles diffèrent, c'est la règle qui est fausse, et le programme suit la note.

**Mots.** Ceux de la note : loi arrondie, décalage lu dans une tranche, aire réalisée, aires atteignables, aires encadrantes, unité brute. Pour le programme, la règle ajoute :

- **couple** : un décalage lu dans une tranche. Une famille a trois décalages, un par aire dite a (0,69, 0,80, 0,95), lus dans chacune de ses tranches ;
- **lecture retenue** : le décalage vaut le nombre écrit multiplié par l'écart type de la loi honnête de la tranche. **Unité brute** : le décalage vaut le nombre écrit ;
- **v_sous** et **v_sur** : les deux aires encadrantes de a dans la tranche, celle du dessous et celle du dessus ;
- **tranche arrondie** : tranche dont l'objet `loi_honnete` est de type `arrondi` au premier niveau. Le programme le décide sur le type écrit par l'auteur, non sur la façon dont il calcule l'aire. Une tranche d'un autre type n'ouvre pas la tolérance, même si son aire se calcule sur un réseau.

## 2. La règle

Pour chaque famille, visible ou tenue à l'écart, pour chaque tranche et pour chacun des trois décalages :

1. **Aires encadrantes.** Dans toute tranche arrondie, le programme calcule, par la somme finie qu'il a déjà, les valeurs de palier et de saut autour de a, puis v_sous et v_sur. Il les calcule que l'écart joue ou non, et les rend au compte rendu avec l'aire réalisée.
2. **(a) conforme** : inchangé. L'aire réalisée sous la lecture retenue est à 0,005 au plus de a. Vaut dans toute tranche.
3. **(a bis) conforme au pas du réseau** : dans une tranche arrondie seulement, sous la lecture retenue seulement, et seulement si le programme a reçu et vérifié l'empreinte de la note scellée. (a) échoue pour ce couple ; l'aire réalisée est égale à v_sous ou à v_sur, à 10⁻⁹ près ; elle est à 0,02 au plus de a ; les trois aires réalisées de la tranche sont strictement croissantes.
4. **Famille conforme** : chaque couple de la famille est (a) ou (a bis). Un seul couple qui n'est ni l'un ni l'autre suffit à ce qu'elle ne le soit pas, quels que soient les autres. Les témoins à saboteur d'une famille conforme sont convertis comme aujourd'hui pour (a) : la vérité se calcule sur la loi et le décalage écrits par l'auteur.
5. **Chaque (a bis) est un écart nommé** : une observation de code neuf, avec le chemin du décalage et le rang de la tranche ; au compte rendu, v_sous, v_sur et l'aire réalisée (aires calculées sur les lois de l'auteur, non valeurs vraies de témoins), et un champ qui dit que la tolérance des réseaux a servi. Les écarts de plus de 0,001 des couples (a) restent nommés comme aujourd'hui.
6. **(b) unité brute constatée** : comme aujourd'hui, et à 0,005 seul. La famille n'est pas conforme, et ses trois décalages, lus en unité brute, réalisent leurs aires dites à 0,005 au plus dans toutes ses tranches. **Le critère (a bis) ne se juge jamais sous l'unité brute** : la note ne l'accorde que sous la lecture retenue. La famille n'est pas convertie ; le compte rendu dit qu'il faut le mot de la mère ; aucune des raisons du point 7 ne s'y ajoute.
7. **(c) non lisible**, dans tout autre cas, avec sa raison. Les raisons d'aujourd'hui ne changent pas : « écart type indéfini », « loi hors du contrôle », « calcul impossible », « aucune unité ne réalise les aires ». S'y ajoute, pour chaque couple d'une tranche arrondie qui n'est ni (a) ni (a bis), une raison et une seule, la première qui s'applique dans cet ordre :
   1. « réseau trop grossier pour l'aire dite » : ni v_sous ni v_sur n'est à 0,02 au plus de a ; aucun décalage ne pouvait passer ;
   2. « aire encadrante hors du plafond » : l'aire réalisée est v_sous ou v_sur, à plus de 0,02 de a, alors que l'autre est à 0,02 au plus ;
   3. « aucune unité ne réalise les aires » : l'aire réalisée n'est ni v_sous ni v_sur ;
   4. « aires non croissantes dans la tranche » : l'aire réalisée est v_sous ou v_sur, à 0,02 au plus de a, et l'ordre manque.

   Ces quatre raisons couvrent tous les couples dont les aires ont été calculées. La raison de la famille est la première, dans l'ordre 1, 2, 3, parmi celles de ses couples ; si seuls des couples de tranches non arrondies manquent, c'est « aucune unité ne réalise les aires », comme aujourd'hui. Le compte rendu donne la raison de chaque couple.
8. **Ordre** : garde de cohérence, portée par (a bis). Elle ne peut manquer que si un autre couple de la même tranche porte déjà la raison 1, 2 ou 3 : la raison 4 n'est jamais celle d'une famille.
9. **Sans l'empreinte de la note** : (a bis) n'existe pas, 0,005 vaut partout, aucune issue ne change par rapport à aujourd'hui. Le programme rend quand même, pour toute tranche arrondie, v_sous, v_sur et l'aire réalisée. Ses raisons se lisent alors à la tolérance en vigueur, 0,005 : « réseau trop grossier pour l'aire dite » si ni v_sous ni v_sur n'est à 0,005 au plus de a, « aucune unité ne réalise les aires » sinon ; les raisons 2 et 4, qui supposent le plafond, ne paraissent pas. Avec une empreinte fausse : refus de départ.
10. **Comparaisons** : sur les valeurs calculées, jamais sur leur forme arrondie à l'affichage. Aucune marge n'est ajoutée à 0,005 ni à 0,02 ; seule l'égalité à v_sous ou à v_sur se juge à 10⁻⁹ près. Le programme dit au compte rendu à quelle précision il tient un décalage pour posé sur un multiple du pas (§ 5, point 2).
11. **Forme du saboteur** : les aires atteignables sont celles de la lecture du programme, où le décalage s'ajoute au score arrondi ; c'est sous cette lecture que la vérité des témoins se calcule. Si la `forme` écrite par l'auteur dit autre chose, par exemple un arrondi appliqué après le décalage, le programme le constate et le nomme au compte rendu. Ce constat ne change pas, par lui-même, l'issue du contrôle par l'aire : ni la pièce scellée ni la note ne tranchent ce cas.

## 3. Statut, et ce qui peut s'écrire sans attendre

**Statut.** Lazar a accordé l'écart et sa valeur : GO-2026-11-21-66, vers 17:10Z, « Organisme : tolérance des réseaux 0,02 « go reco » (note d'écart à sceller) ». L'accord ne prend effet qu'au scellement de la note d'écart par la mère, après la vérification des corrections par le même contre-lecteur, et avant toute lecture d'une sortie de l'auteur. **D'ici là, la lettre scellée s'applique : 0,005 partout.** Si une sortie de l'auteur est lue avant le scellement, la note ne se scelle pas et l'écart tombe : un écart choisi après lecture viserait un résultat (règles R1 et R3). La pièce scellée est `prereg/ideation-seuil-moniteurs-v1/scellement-erratum-v5-texte-servi-v3-devis-v8-mondes-plantes-v1.md` (`dfe0aace22a2e0eb4fa48656556e3be7ef532801304323b9a95c6f99dffae171`, l. 30).

**Ce qui peut s'écrire sans attendre** (instrument, classe B : un autre modèle le contre-lit, puis vérifie les corrections) : le programme de vérification v6, l'écart éteint, sur cette règle. L'issue (a bis) n'y existe que derrière la condition d'empreinte ; sans elle, 0,005 partout (point 9). Si un programme v6 a déjà été écrit sur la règle v2, trois choses y changent : le constat d'unité brute se juge à 0,005 seul (point 6) ; chaque couple non reçu d'une tranche arrondie porte l'une des quatre raisons, et l'ordre n'est plus une cause à lui seul (points 7 et 8) ; la tranche arrondie se décide sur le type `arrondi` (§ 1). Je ne sais pas où en est ce programme : je ne l'ai pas lu.

## 4. Épreuves à porter au programme (règle R5)

Reprises de l'épreuve du contre-lecteur (`sortie-epreuve-v2.txt`, `c295f6c746757e05c32e212024fa891fbf8e5f223c1a74c81fafc5caab88ce63`) et de la mienne (`epreuve-du-concepteur-v1/sortie-epreuve-note-ecart-v2-regle-v3-reseau-factice-v1.txt`, `9d8a123eb060a572b9cbfe04a69ed3d6717c940ef457bfe84a1a34f955a4cdb1`), toutes deux sur réseau factice, non opposables. Elles disent quoi éprouver, non ce que le programme rendra. Les aires citées sont celles d'une normale réduite arrondie. Chaque épreuve a son issue et sa raison attendues, écrites avant l'essai.

| épreuve | construite | attendu |
|---|---|---|
| Famille à tranches continues, décalages exacts | cas sain | neuf couples (a) ; convertie ; aucun écart nommé |
| Trois tranches arrondies au pas 0,25, décalages tirés de la loi continue | cas sain | 0,69 et 0,80 en (a bis), aires 0,6705 et 0,7865 ; 0,95 en (a), aire 0,9532, écart de plus de 0,001 nommé comme aujourd'hui ; convertie ; six couples (a bis) nommés |
| Une tranche continue, deux tranches arrondies, mêmes décalages | cas sain | (a) dans la tranche continue, (a bis) dans les autres ; convertie |
| Famille mixte : 0,69 en (a bis), 0,80 un palier trop loin | artefact | non convertie ; pour 0,80, « aucune unité ne réalise les aires » |
| Pas 0,5 : aire encadrante du dessous réalisée, à 0,0545 ; celle du dessus à 0,0111 | artefact | non convertie ; « aire encadrante hors du plafond » |
| Pas 0,1 : palier voisin à 0,0129, non encadrant | artefact | non convertie ; « aucune unité ne réalise les aires » |
| Pas 0,1 : palier du dessus, que la valeur de saut sépare de l'aire dite | artefact | non convertie ; « aucune unité ne réalise les aires » |
| Pas 1 | artefact | non convertie ; « réseau trop grossier pour l'aire dite » pour 0,69 et 0,80 |
| Nombres en unité brute, écrits comme nombre en écarts types multiplié par l'écart type ; écart type 2, pas 0,5 | artefact | (c), non (b) ; non convertie |
| Les mêmes, pas 0,001 | artefact | (b) unité brute constatée, comme aujourd'hui ; non convertie ; aucune des quatre raisons |
| Une tranche continue où les décalages réalisent les aires dites plus 0,01 ; deux tranches arrondies où ils sont reçus | artefact | non convertie : 0,005 seul dans la tranche continue |
| Le décalage de 0,80 réalise la même aire que celui de 0,69 | artefact | non convertie ; « aires non croissantes dans la tranche » pour 0,69, et une autre raison pour 0,80 |
| Le deuxième cas sain, sans l'empreinte de la note | artefact | 0,005 partout ; non convertie ; le compte rendu donne v_sous, v_sur et l'aire réalisée |
| Le deuxième cas sain, avec une empreinte fausse | artefact | refus de départ |

Mutations, chacune à tuer par une épreuve nommée ci-dessus : un seul couple (a bis) suffit à la famille ; (a bis) jugé aussi sous l'unité brute ; égalité à v_sous ou v_sur omise ; plafond relevé ; raison « aire encadrante hors du plafond » omise ; plafond de 0,02 étendu, sans l'égalité à v_sous ou v_sur, aux tranches non arrondies d'une famille qui a une tranche arrondie ; valeurs de saut omises ; condition d'empreinte retirée ; tranche arrondie décidée sur le calcul et non sur le type. Les huit premières sont jouées dans mon épreuve ; la dernière ne l'est pas, mon réseau factice n'ayant pas de type.

## 5. Limites, dites

1. **Convention des ex æquo.** Celle de l'auteur n'est pas connue. Un décalage posé exactement sur un multiple du pas est lu à mi-hauteur ; s'il sort ainsi de la règle, l'issue est (c) et le compte rendu le dit. Aucune tolérance de plus.
2. **Une valeur de saut n'est atteinte par aucun nombre écrit.** L'une des deux aires encadrantes est toujours une valeur de saut. Un auteur qui la vise et écrit son nombre à quatre ou six décimales tombe sur le palier du dessous, encadrant et reçu, ou sur celui du dessus, non encadrant et refusé, selon le sens de son arrondi (`epreuve-du-concepteur-v1/sortie-limite-decalage-vise-sur-un-multiple-du-pas-v1.txt`, `69c628d79492de728ae8f1f2700426e5a5fa1ae50f9e919bec23404c2eded5ec`, illustration non opposable : au pas 0,25, pour 0,69, le nombre 0,7480 est reçu et le nombre 0,7481 ne l'est pas). D'où la précision demandée au point 10 du § 2. Nœud pour Lazar, avec une recommandation de ne rien ajouter.
3. **Conséquence du point 6.** Une famille à tranche arrondie écrite en unité brute, sur un réseau où 0,005 ne peut pas être tenu, n'est plus reconnue « unité brute constatée » : elle est rendue (c). Aucun témoin n'était converti dans un cas ni dans l'autre ; ce qui se perd est le constat, et le chemin par le mot de la mère. Le compte rendu donne toujours les aires sous les deux lectures, et v_sous et v_sur : la mère peut y voir le cas. Nœud pour Lazar.
4. **(a bis) passe avant (b).** Une famille dont l'écart type est proche de 1 et dont les nombres sont en unité brute peut être reçue au pas du réseau sous la lecture retenue : elle est convertie sous cette lecture, écart nommé. La v2 avait le même ordre.
5. **Une seule famille de lois.** Toutes les aires citées viennent d'une normale arrondie. Dans cette illustration, au pas 0,25, le seul palier encadrant de 0,69 est à 0,0195 de l'aire dite : à 0,0005 du plafond.

## Pièces lues

Les mêmes que pour le projet de note v2, dont la table « Pièces lues » donne chemins, empreintes et étendue de lecture. Pour cette règle : la règle v2 (`3806ff34…`, en entier ; ses deux commandes de contrôle à l'octet rejouées, code 0) ; la contre-lecture (`b84519a3…`) et ses épreuves, lues et non relancées ; la source du concepteur, § 6 (`4521273497513cb0de5eecdedfce4a6f088dd367b4e8675cc436d40d463af15e`) ; le rapport v6 du développeur du programme de vérification (`28d9155f34badaee245bc5f5125ae5fe24e13b56b8b940c5e567fe767cff0e72`, en entier) ; l'arbitrage de l'unité des décalages (`a8f8acfabf2757a383dd459be2dcd352cd4ad2a3bd53a0ad82986cc1be989636`) ; la pièce scellée (`dfe0aace…`) ; le texte servi v3 (`f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008`, l. 86 à 108 et l. 143 à 148). **Non lu** : aucune sortie de l'auteur des mondes, aucune vérité, aucun fichier dont le nom porte « vérité », « rendu » ou « scores » ; ni le programme de vérification, ni le programme de vérité.

## Relevé de méthode

### Chaîne de raisonnement

1. La règle v2 (`3806ff34…`) est la source, l. 547 à 557 et l. 575 à 591, à l'octet : les deux commandes de son en-tête, rejouées, ne rendent rien (code 0).
2. Son point 5 (l. 19) dit : « le critère (a) ou (a bis) étant appliqué sous l'unité brute pour les lois arrondies ». Le projet de note garde la lecture en écarts types (projet v1, l. 32 ; projet v2, section « Ce qui ne change pas »). La contre-lecture (`b84519a3…`, mode 4) : « Le programme doit suivre la note, non la règle ». Donc le point 6 de la v3.
3. « Comme aujourd'hui » : le constat d'unité brute demande toutes les aires à 0,005 près dans toutes les tranches, ne convertit pas et requiert le mot de la mère ; les raisons de « non lisible » sont quatre (rapport v6 du développeur, `28d9155f…`, partie 0, point 2). **Supposé** pour le programme lui-même, que je n'ai pas lu.
4. Les quatre raisons par couple couvrent tout, et l'ordre ne manque jamais seul : pas 9 et 10 du relevé de méthode du projet de note v2.
5. La tranche arrondie se décide sur le type `arrondi` : texte servi v3 (`f3d87162…`, l. 147) ; pas 5 du même relevé.
6. Sans l'empreinte, la tolérance en vigueur est 0,005 ; « aucun décalage ne pouvait passer » se lit donc à 0,005 (choix du concepteur, que la source ne fixait pas : sa section 6.5 nommait deux raisons pour l'écart éteint sans dire à quel seuil).
7. La lecture « le décalage s'ajoute au score arrondi » est celle du programme (rapport v6, partie 6, remarque 1) ; l'arbitrage (`a8f8acfa…`, § 3, point 4) l'avait laissée ouverte. Donc le point 11 : un constat, non une issue.

### Objets de contrôle

Ceux de l'épreuve du concepteur, décrite au relevé de méthode du projet de note v2 : programme `epreuve-du-concepteur-v1/epreuve_note_ecart_v2_regle_v3_reseau_factice_v1.py` (`d0928633cf0e9cdd5322cd0e27d6e7eb70dc7cd683bc2865b3512bb1bb52ac6c`), sortie `9d8a123e…`, illustration non opposable. Pour la correction propre à cette règle : objet faux, des nombres en unité brute sur une loi d'écart type 2 arrondie au pas 0,5 ; prédit, « non lisible » et non « unité brute constatée » ; rendu, conforme ; sous la v2, c'était « unité brute constatée » (mutation vue). Objet vrai pour le constat : les mêmes nombres au pas 0,001 ; prédit, « unité brute constatée », comme aujourd'hui ; rendu, conforme. Treize objets sur treize et huit mutations sur huit conformes à la prédiction, à la première exécution : trop propre pour être cru sans réserve (règle R4), les prédictions venant des mêmes valeurs que les objets.

### Premier pas non justifié

Le **pas 3** : « comme aujourd'hui » repose sur le rapport du développeur, non sur le programme. Ce qui le justifierait : la lecture du contrôle par l'aire dans le programme v5, par le développeur ou son vérificateur.

### Mode d'échec affecté

Sans objet : je suis le concepteur de la règle, non un relecteur.

### Dérivation de l'énoncé seul

Sans objet : je ne suis pas un agent de re-dérivation, j'avais la règle v2 en main.

### Trouvaille de côté

Les limites 2, 3 et 4 du § 5 : la valeur de saut qu'aucun nombre écrit n'atteint ; le constat d'unité brute perdu sur un réseau grossier ; la réception au pas du réseau qui passe avant ce constat. Je ne les poursuis pas : les deux premières vont à Lazar, par la mère.

### Évaluateur et conseil

Ce qui juge cette règle : le même contre-lecteur, avec le projet de note v2 ; puis le développeur du programme v6 et son vérificateur, sur les épreuves du § 4. Ce qui l'a jugée ici : mon programme d'épreuve, qui code ma lecture et n'a ni types de lois ni empreinte à vérifier. Par où elle pourrait être bien jugée sans le mériter : parce qu'elle répète la note ; une divergence entre la note et la règle est justement ce que la contre-lecture avait trouvé. Conseil : vérifier la règle contre le texte à sceller de la note, phrase par phrase, et non contre la règle v2.
