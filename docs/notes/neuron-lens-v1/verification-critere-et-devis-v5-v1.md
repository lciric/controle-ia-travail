# Vérification des versions 5 du critère d'identité et du devis du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v1

- Heure (`date -u`) à l'écriture : 2026-11-19T11:42:59Z ; l'heure du scellement est celle du fichier compagnon.
- Vérificateur : le contre-lecteur de la v4 (sous-agent, **Claude Opus 5.5**, `claude-opus-5-5`), d'un autre modèle que le rédacteur
  (Claude Fable 5.2). Il n'a écrit ni les versions 5, ni le programme de comparaison v3, ni ses essais. Vérification courte des
  corrections de sa contre-lecture (`contre-lecture-critere-et-devis-v4-v1.md`, `c61466fa…`, branche principale, commit `f113e756`,
  vérifié), étendue aux sept questions de la mère.
- Objet, lu par identifiant de commit sur la branche `claude/brave-galileo-jhp684`, sans extraction de l'arbre. Empreintes
  recalculées, égales à l'attendu et au compagnon : critère v5 (commit `3e7fa633`)
  `50657b8929ab29ff5b09012b31cfe2a150f7815916b538acdba133f7042e24b6` ; devis v5
  `f2a12fd05d9bedee2f1449af181462e8a34413820750cc0d96a23942faa78f76` ; programme de comparaison v3 (commit `2e1d9ec5`, inchangé au
  commit `3e7fa633`) `c8fc62034f2e4e1c18e803c9108598c1d70b74b6c2eab61fef1eb653fdd89d3a` ; ses essais
  `5996a4150062c619a5a0e748d572ab8bdff108a8fb79d176821c0bd4300dc35e`.
- Lu en plus, au commit `3e7fa633` : le lanceur de la course du 18 (`b_beta_lancer_v3.py`, `582fd9ef…`, identique au commit
  `5e5cb65b` du dépôt réduit) aux lignes 51, 55-70, 120-131, 222-233, 585-612, 640-656, 886-926 ; le module de contrôles
  (`controles_b_beta_v2.py`, `ddc36c55…`, identique aux deux commits) l. 139-161 ; `src/controle_ia/manifeste.py` l. 33-118 ; la
  copie de lecture du code voisin (`docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/scripts-02_fit.py.txt`, `309f4988…`,
  l. 138-170) ; la commande v8 par recherche (l. 119-146) ; le script de relevé de prix (`releve_prix_h100_v3.py`, `321872f3…`,
  l. 14 et 40-42) ; le texte gelé de la tranche (`texte-gele-tranche-b-beta-v1.md`, `f5d46860…`, l. 82-105 et 166-206 : un
  préenregistrement, aucun résultat). Les critères et devis v4, déjà lus.
- **Sondes** : 21 appels du programme v3 non modifié, sur des pièces **inventées** (aucune pièce de `diag/` ni de `runs/` n'est
  lue), dans mon dossier du bloc-notes de la mère :
  `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/opus-contre-lecture-critere-v4/v5/sondes/sondes_synthetiques_v1.py`
  (`5b1d20332adbef4a0ec7e4d237fa208ac2d9f1bdcdf7d6da3ba94199f8522617`) et sa sortie `sortie-sondes-synthetiques-v1.txt`
  (`8f87be7a9dc82a9ed58b82bf1e867ed0da0a90d4097dc0a91e07df83bcaab536`), dans le même dossier ; hors dépôt, **non opposables** tant
  que la mère ne les verse pas. Elles sont citées ci-dessous par leurs étiquettes V0 à V20. Les 123 essais du programme n'ont pas été
  rejoués : ils lisent `diag/` et `runs/` (essais, l. 13-14).
- Non lu, selon le mandat : `docs/verdicts/`, tout fichier dont le nom commence par « verdict », `diag/`, `runs/`, `donnees/`, tout
  résultat de l'apprentissage des sondes sur la tâche ou des lentilles, tout fichier « consigne-privee » ou « conception-ii-b »,
  `brouillons/ii-b-saboteur-budget-v1/`. Aucune dépense, aucune machine, aucun commit, aucun fichier existant modifié. **Aucun refus
  d'outil.**

## Conclusion, par pièce

- **Critère v5 : scellable après ces couples exacts** (sept couples, plus bas). Aucun ne touche un seuil ni un libellé, et aucun
  n'ouvre une autorisation. Trois ferment des choix encore laissés au contrôleur (quel commit en K1, quel lanceur en K2, quel journal en
  K4 — ce dernier pouvait faire lire des mesures avant le verdict). Deux retirent ce que le texte dit de plus que les pièces : la
  phrase du premier palier en cas mixte, et la phrase sur le champ `lentilles`, inexacte. Un donne une phrase aux autres verdicts. Le
  dernier met le texte d'accord avec la décision de la mère (programme v4 avant la création).
- **Devis v5 : scellable après ces couples exacts** (trois couples : valeurs des versions, programme v4, calcul des séries de R).
- **Le programme v4 étant décidé avant la création, le critère appliqué sera celui qui le cite.** Si cette version arrive dans la
  journée, porter les couples 1 à 6 directement dans elle et ne sceller qu'elle ; sinon sceller la v5 avec les couples, pour figer les
  règles, et faire de la version suivante une vérification courte (§ 7 ci-dessous dit ce qu'elle peut changer, et rien d'autre).

## 1. E1 à E6 et m1 à m8 — **toutes appliquées ; le point refusé de E1 l'est à bon droit ; quatre restes (E1, E4, E5, m1), dont un vient de ma propre rédaction de E1.**

| correction | appliquée ? | remarque |
|---|---|---|
| E1, fonction fixée, lanceurs rattachés | **oui, autrement** : texte de la fonction comparé à la constante `a5495c68…` par le programme, des deux côtés (sonde V16 : fonction modifiée → « non comparable ») ; lanceur neuf rattaché à la main (K2) | **Le refus tient.** Du lanceur de référence, le programme ne lit que le texte de la fonction, exigé égal à la constante ; les valeurs de référence viennent des pièces du 18, vérifiées par empreinte. Quel fichier est passé n'importe donc pas au-delà de sa fonction, et le lien de la constante à la course du 18 est écrit une fois au § 2 (fichier `582fd9ef…`, égal au commit `5e5cb65b`, que j'ai recalculé). **Reste**, hérité de ma propre rédaction de E1 : « le fichier du même chemin » ne dit pas quel fichier est le lanceur ; un autre lanceur portant la même fonction passe (sonde V3). Couple 1. |
| E2, couches des matrices 0 à 30 | oui, préalable du programme (sonde V19) | — |
| E3, ce que l'audit peut conclure | oui, à la lettre ; « K1 » pour « H2 », à juste titre | — |
| E4, une phrase par lentille, « même code d'ajustement », norme nommée | oui, en deux langues ; le singulier du premier palier est ajouté | ce singulier dit trop en cas mixte (point 5, couple 3) |
| E5, versions, pièces au commit, matériel | oui (sondes V4 et V4b : une clé ou une valeur de `versions` changée → « non comparable ») ; K1 ; K3 | le devis ne reprend que les clés, pas les valeurs (couple 1 du devis) |
| E6, fin de course | oui, mieux que demandé : inventaire poussé à la fin de chaque étape | — |
| m1, arrondi du plancher, ancre | oui pour l'arrondi | la phrase ajoutée « toute différence du champ `lentilles` … paraît dans la table » est **inexacte** : ce champ ne porte que des noms (`list(SPECS)`, lanceur du 18, l. 64 et 598) ; l'ancre n'est vérifiée nulle part à la comparaison (sonde V14). Couples 1 et 2. |
| m2 | oui | — |
| m3 | oui ; vérifié dans la copie de lecture `309f4988…` : `path.with_suffix(".tmp")`, `v.cpu()`, `os.replace`, l. 161-166 | source du « `H100_SXM` » indirecte (mineure 1) |
| m4 | oui (décisions 6 et 7 du devis) | point 6 |
| m5 | oui (arrêt sur erreur ; seconde course incomplète) | — |
| m6 | oui, préalable du programme (sonde V17) | — |
| m7 | oui, par la seconde branche (lignes dites non opposables) | — |
| m8 | oui (§ 5, point 9 ; décision 3) | — |

## 2. Seuils, mentions, autorisations, chiffres — **rien n'est relâché ; quatre changements vont dans le sens sévère et sont déclarés ; aucun chiffre du devis n'a changé ; les deux variantes sont écrites en entier.**

- **Critère.** Mêmes seuils (10⁻³, 10⁻⁹, 10⁻⁶, 0,10) ; le seul nombre neuf en 10⁻ⁿ est le « ≈ 3 × 10⁻⁷ » de l'arrondi (m1), qui n'est
  pas un seuil. Les cinq libellés sont identiques, dans le texte et dans le programme (constantes l. 69-73). Le tableau de ce que
  chaque mention autorise ne change qu'en un mot, « course rejouée **en entier** », qui restreint et qui est déclaré (différence
  n° 9). Vont aussi dans le sens sévère : l'arrêt du programme sur une erreur, qui vaut « non comparable » ; le contrôle K2 ; la
  lentille perdue avant sa copie, qui reçoit « non réajustée ». La « mention du programme » au deuxième palier avec un écart sur
  `diffs` au-delà de 10⁻³ est maintenant « suspendue » d'emblée au lieu de « palier 2 » puis suspendue par le contrôle H7 : verdict
  inchangé, déclaré (différence n° 5).
- **Devis.** Tableau du § 3, prix, frais fixes, plafonds, arrêts durs, minuteries et comptes rendus identiques à la v4 (comparaison
  ligne à ligne). Chiffres ajoutés, recalculés et justes : marges de reprise 5,7 h et 7,1 h à l'attendu, 1,2 h et 1,3 h au pire
  cas, deux reprises entières au pire débit 1,38 h ; décision 6 : 2 × 1,25 h × 2,3713 = 5,9 USD, quatre ajustements de 30 documents
  à 19,8 s (18 414 s / 932) ≈ 10 min chacun, 1,6 USD, total 7,5 USD ; décision 7 : 15 min, 0,6 USD. La confiance du rédacteur reste
  0,7 ; la mienne est rapportée juste (B, 0,75, avec ma raison).
- **Variantes** A et B écrites en entier (§ 2, § 3, § 7), avec le cas de la seconde course incomplète.

## 3. Les contrôles H1 à H7 dans le programme v3 ; la liste K1 à K5 — **H2 à H7 : faits ; H1 : seulement relevé, comme le critère le dit ; la liste K n'est pas encore fermée en trois points.**

- **Dans le programme**, lu ligne à ligne et sondé : H2, export neuf rattaché à la course neuve et différent de celui du 18 (l. 201-208 ;
  sonde V13) ; H3, clés des séries 0 à 27 (l. 199 ; V18), et les couches des matrices 0 à 30 (l. 192 ; V19) ; H4, séries de R
  inchangées à zéro exact au premier palier (l. 291 ; V6 : un changement de 10⁻⁷ suspend) ; H5, bibliothèque des lentilles,
  précision, `versions` hors `plateforme` en égalité stricte, contenu des correctifs aux deux commits par `git show`, un fichier
  illisible étant un manqué (l. 142-156 ; V4, V4b, V15) ; H6, déclencheur (vi) avec `audit_requis` (l. 315-320 ; V7) ; H7, `diffs`
  au-delà de 10⁻³ au deuxième palier ou de 10⁻⁶ au premier (l. 293-295 et 312-314 ; V5). H1 : le programme verse `pieces_lues` et
  `commit_resultats` sans rien vérifier (l. 255) ; c'est ce que dit le critère, et K1 le complète.
- **K3 et K5 sont fermés.** **K1, K2 et K4 laissent chacun un choix :**
  1. **K1** : « le commit … est celui de la branche de résultats poussée par la machine ». La machine pousse à la fin de chaque étape
     (devis v5, § 5, point 3) : plusieurs commits portent des versions successives des pièces. Lequel ? Couple 6 : la tête de la
     branche, lue après la destruction de la machine.
  2. **K2** : « le fichier du même chemin » ne dit pas quel fichier est le lanceur ; un autre lanceur du même commit, portant la même
     fonction, passe (V3). Et la même ancre des séries de R, que le plancher suppose, n'est vérifiée nulle part (V14). Couple 1 : le
     lanceur est celui que nomme la commande scellée ; ses lignes d'ancre et le calcul des séries sont comparés à des empreintes fixées.
  3. **K4** : « le journal de la course neuve est lu ». En variante B ce journal porte des mesures, et le § 8 exige la comparaison
     « avant toute lecture d'une mesure de la nouvelle course ». Couple 5 : seul le journal de l'étape d'ajustement est ouvert, et
     seulement ses en-têtes de lancement (une ligne « === » par lancement, `executer`, lanceur du 18, l. 226-231).

## 4. Les deux écarts déclarés — **la longueur se défend ; le contrôle K2 ajouté est juste.**

- **Longueur** (431 lignes au compte de `wc`, contre 311). « Une v5 courte » disait l'effort des corrections, non une limite. La
  croissance vient des phrases au singulier que E4 demandait, en deux langues (≈ 45 lignes), de la liste K avec ses raisons
  (≈ 27), des tableaux d'historique du § 0 (≈ 40), du tableau des sondes (≈ 13) et des nœuds du § 9 (≈ 15). J'ai vérifié qu'aucune
  règle n'est cachée dans les parties d'historique (le § 9 le dit, et c'est vrai). Pour la version qui citera le programme v4 : ne
  garder que le texte appliqué, et verser l'historique dans une note compagne (mineure 6).
- **K2, `depot_propre`.** La raison tient : les correctifs et le lanceur sont lus au commit du manifeste, ce qui ne décrit le code qui
  a tourné que si l'arbre était propre. Le contrôle ne peut que faire descendre une mention, il est fixé avant de voir et coûte une
  lecture. Il sera presque toujours tenu, puisque `creer_manifeste` refuse un arbre sale sauf permission explicite (`manifeste.py`,
  l. 81-84 ; le lanceur du 18 ne la donne pas, l. 590) : il garde précisément contre un lanceur neuf qui la donnerait (sonde V1 : le
  programme ne le voit pas). Accepté ; le couple 1 l'étend.

## 5. La phrase du cas mixte — **au deuxième palier, oui ; au premier palier, elle dit plus que le palier n'autorise ; et un verdict n'a pas de phrase.**

- Les phrases au singulier du deuxième palier, pour R et pour S, ne disent que ce que le palier autorise : « même code d'ajustement »
  est couvert par les préalables et K2, les chiffres sont obligatoires, et S dit qu'aucune autre comparaison n'existe.
- **Premier palier, cas mixte.** « les mesures du 18 novembre décrivent cette lentille » : les mesures du 18 ne portent pas toutes sur
  une seule lentille. La condition de la mesure B-1 sur la différence entre moitiés est exigée « à chaque couche et chaque cible
  **des deux lentilles** » (texte gelé de la tranche, `f5d46860…`, l. 174) ; la lecture côté entrée (B-5) porte sur S (l. 82) ; les
  autres portent sur R ; et un verdict d'ensemble les combine (ligne « verdict d'ensemble » du tableau des prédictions, l. 105 ; celui
  du 18 est « partiel », accepté : critère v5, § 1). Si R est au premier palier et S ne l'est pas, les
  mesures faites sur R se transportent, mais ni le verdict d'ensemble ni la condition commune aux deux lentilles. Couple 3, sur la
  phrase et sur la ligne du tableau.
- **« l'autre reçoit la phrase de son propre verdict »** : seuls les deux paliers ont une phrase. Pour « différente », « non
  comparable », mention suspendue ou non réajustée, la phrase reste à écrire par qui écrit le billet. Couple 4 la donne.

## 6. Devis v5 : la fin de course et les décisions 6 et 7 — **la fin de course est juste ; les deux décisions sont claires ; trois couples pour d'autres phrases.**

- **Fin de course (E6)** : l'inventaire est poussé à la fin de chaque étape, puis clos ; copie refaite au plus deux fois, puis « pas
  de destruction sans la mère », dans la limite de l'arrêt dur ; destruction seulement après l'inventaire clos et la relecture ; la
  perte acceptée d'avance est écrite, avec « Lazar lit cette ligne avant d'accorder » ; empreinte recalculée en flux, durée et trafic à
  mesurer avant le GO. Les marges de reprise sont justes et la conséquence au pire cas est dite (l'arrêt dur l'emporte). Rien à reprendre.
- **Décision 6, essai court** : coût, délai, limite (30 documents ne garantissent pas 932), options, recommandation conditionnelle
  (non si B, oui si A, confiance 0,7) et défaut (pas d'essai) sont clairs. Le coût de 7,5 USD est un plancher : il compte deux machines
  au prix le plus bas, alors que le relevé du 19 n'avait qu'une offre vérifiée sous 4 USD/h (la suivante à 4,10), et il ne compte pas
  la fin de course ; vers 10 à 12 USD. Cela renforce « non si B » (mineure 4).
- **Décision 7, croquis** : coût borné, effet nul sur cette course, défaut, recommandation (oui, 0,8) clairs. Deux mots à ajuster
  (mineure 5).
- **Couples du devis** : 1, les **valeurs** de `versions` (le critère les exige égales ; le devis ne parle que des clés ; or les copies
  vers la plateforme de modèles passent par `huggingface_hub`, paquet de la liste du manifeste : une mise à jour pour les copies
  rendrait « non comparable » une course payée) ; 2, le point 6, qui dit le préalable du programme « levé » alors que la mère a
  décidé une version 4 avant la création ; 3, le calcul des séries de R gardé, comme l'ancre (point 5 k).

## 7. Le programme v3 et ses six défauts ; la version du critère qui citera la v4 — **la v5 reste juste avec la v3 ; voici ce que la suivante peut changer, et elle seule.**

- **Avec la v3, la v5 est juste** : chacun des six défauts que signale l'auteur du programme est tenu par le critère. `depot_propre`
  non lu → K2 (sonde V1) ; champs du haut du manifeste hors de la table → K5 (V2) ; commit des résultats non vérifié contre les
  pièces → K1 ; lanceur neuf rattaché à rien → K2 (V3) ; quatre formes mal formées qui lèvent une erreur → règle de l'arrêt sur
  erreur, « non comparable » (V10 à V12 : `versions` en liste, correctifs en liste de listes, configuration en liste) ; `audit_requis`
  posé pour le seul déclencheur (vi) → le § 6 dit que l'audit est dû dès que la liste des déclencheurs n'est pas vide (V8, V9 : rien
  pour « différente » ni pour le premier palier). Je n'ai trouvé aucune affirmation du critère v5 sur le programme qui soit fausse ;
  la seule phrase inexacte porte sur le contenu du manifeste (couple 2).
- **La version du critère qui citera la v4 change ceci, et rien d'autre** (sinon, contre-lecture complète) :
  1. le § 7 cite le programme v4 (chemin, empreinte, fichier d'essais, empreinte, nombre d'essais) et lui seul ; les étiquettes de
     l'en-tête du programme nomment cette version du critère ;
  2. chaque contrôle que la v4 prend en charge passe de la liste K aux préalables du § 4, **avec la même conséquence** (« non
     comparable » à octets différents, suspension à octets égaux) et le nom de l'essai qui le joue : `depot_propre` ; lanceur neuf égal au
     fichier de son chemin au commit du manifeste, ses lignes d'ancre et le calcul des séries (couple 1, si la v4 les lit) ; pièces
     neuves égales aux fichiers du même chemin au commit de résultats ; champs du haut du manifeste dans la table, sans critère ;
  3. reste à la main ce que la v4 ne peut pas voir : que le chemin donné est celui que nomme la commande scellée ; que le commit est
     la tête de la branche distante après destruction (sauf si la v4 la lit) ; le matériel (K3) ; les en-têtes du journal
     d'ajustement (K4), sauf si la v4 les lit ; la relecture au lieu de rangement ; l'audit ;
  4. la règle de l'arrêt sur erreur **reste**, comme filet pour toute exception non prévue ; les quatre formes connues rendent « non
     comparable » (ou suspendent) sous les libellés inchangés ;
  5. au § 6, la règle « l'audit est dû dès que la liste n'est pas vide » reste ; seule la remarque sur `audit_requis` suit ce que fait
     la v4 ;
  6. constantes et libellés identiques à l'octet ; tout changement d'un seuil, d'un libellé ou d'une autorisation sort de la
     vérification courte ;
  7. les couples 1 à 6 de ce rapport y sont portés ; le § 0 dit chaque différence avec sa raison et son essai.

## Couples du critère (texte avant, texte après)

**Couple 1 — K2 : quel lanceur, et la même ancre (§ 7).**
- Avant : « - **K2 — Le code qui a tourné est celui du manifeste.** Le manifeste neuf porte `depot_propre` vrai ; le lanceur neuf donné
  au programme (empreinte `lanceur_neuf` de la sortie) est égal au fichier du même chemin au commit que porte le manifeste neuf ; le
  dépôt donné au programme est le dépôt de travail, où les deux commits des manifestes sont lisibles. *Pourquoi à la main* : le
  programme ne lit pas `depot_propre` et ne rattache pas le lanceur au commit. »
- Après : « - **K2 — Le code qui a tourné est celui du manifeste.** Le manifeste neuf porte `depot_propre` vrai ; le lanceur neuf donné
  au programme (empreinte `lanceur_neuf` de la sortie) est le fichier de lanceur que nomme la commande scellée de la course neuve, et
  il est égal au fichier de ce chemin au commit que porte le manifeste neuf (`git show <commit>:<chemin> | sha256sum`) ; ce lanceur
  fixe l'ancre des séries de R comme celui du 18 (`REVISION_NEURONPEDIA = "d2527c3cdbaa60dd4b65cbca1604921f044e989a"` et, pour `npR`,
  l'empreinte `a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c` : lanceur du 18, l. 58 et 130-131), et le module de
  contrôles qu'il importe (`controles_b_beta_v2` pour celui du 18, l. 51) porte, au même commit, les textes de `ecart_max`,
  `ecarts_identite` et `ecarts_npr` du commit `5e5cb65b…` (méthode `empreinte_fonction` du programme :
  `4f6be7e9709d58bbcc009cf8101aa4131578e2d467ce1f2d142059a330002819`, `587e98a80863f7ca3f7a704f427173221982f6093cbb259e37498e160c1a599d`,
  `51c9cee2c1bc19cca6c28ae80e86c4879b5e3b7eb1e35c7bfe40b0e3d1ffeaf0`) ; le dépôt donné au programme est le dépôt de travail, où les
  deux commits des manifestes sont lisibles. *Pourquoi à la main* : le programme ne lit pas `depot_propre`, ne rattache pas le lanceur
  au commit et ne lit ni l'ancre ni le calcul des séries. »
  (La suite, « Manqué : « non comparable » (octets différents) ou mention suspendue (octets égaux). », est inchangée.)

**Couple 2 — ce que le plancher suppose (§ 4, « Pour R, deux séries rapportées sans critère »).**
- Avant : « et elle suppose la même ancre aux deux courses — la lentille publique est épinglée par révision et vérifiée par empreinte
  dans le lanceur du 18 (relevé du contre-lecteur de la v4, non refait ici), le lanceur neuf doit garder ces lignes (devis v5, § 5,
  point 5), et toute différence du champ `lentilles` de la configuration paraît dans la table des différences des manifestes. »
- Après : « et elle suppose la même ancre et le même calcul aux deux courses — la lentille publique est épinglée par révision et
  vérifiée par empreinte dans le lanceur du 18 (l. 58 et 130-131), le lanceur neuf doit garder ces lignes et ce calcul (devis v5,
  § 5, point 5 k), et le contrôle K2 le vérifie ; le champ `lentilles` de la configuration ne porte que des noms de lentilles
  (lanceur du 18, l. 64 et 598), il ne dit rien de l'ancre. »

**Couple 3 — premier palier en cas mixte (§ 5, tableau et phrase).**
- Avant (tableau) : « | premier palier | établie | oui, avec leurs limites (verdict « partiel », couches stables du 18) | par un texte
  de lecture neuf et contre-lu, sous l'accord GO-2026-11-19-33 | »
- Après (tableau) : « | premier palier | établie | oui, avec leurs limites (verdict « partiel », couches stables du 18) ; **si l'autre
  lentille n'est pas au premier palier**, seulement les mesures faites sur celle-ci : le verdict d'ensemble et les conditions qui
  portent sur les deux lentilles ensemble ne se transportent pas tels quels | par un texte de lecture neuf et contre-lu, sous l'accord
  GO-2026-11-19-33 | »
- Avant (phrase) : « Si **une seule** lentille est au premier palier, la phrase est écrite pour elle seule : « Le fichier d'ajustement
  réajusté de la lentille [R | S] est identique à l'octet à celui du 18 novembre (empreinte …) ; les mesures du 18 novembre décrivent
  cette lentille. » (*“The refitted fit file of lens [R | S] is byte-identical to that of 18 November (hash …); the 18 November
  measurements describe this lens.”*) »
- Après (phrase) : « Si **une seule** lentille est au premier palier, la phrase est écrite pour elle seule : « Le fichier d'ajustement
  réajusté de la lentille [R | S] est identique à l'octet à celui du 18 novembre (empreinte …) ; les mesures du 18 novembre faites sur
  cette lentille la décrivent. » (*“The refitted fit file of lens [R | S] is byte-identical to that of 18 November (hash …); the
  18 November measurements made on this lens describe it.”*) Le verdict d'ensemble du 18 (« partiel ») et les conditions communes aux
  deux lentilles ne se transportent pas tels quels : la condition sur la différence entre moitiés (mesure B-1) est exigée « des deux
  lentilles » (texte gelé de la tranche, `texte-gele-tranche-b-beta-v1.md`, `f5d46860…`, l. 174) ; le texte de lecture dit, mesure par
  mesure, ce qui porte sur cette lentille. »

**Couple 4 — une phrase pour les autres verdicts (§ 5, deuxième palier).**
- Avant : « Si **une seule** lentille est au deuxième palier, la phrase est écrite pour elle seule, au singulier, et l'autre reçoit la
  phrase de son propre verdict. »
- Après : « Si **une seule** lentille est au deuxième palier, la phrase est écrite pour elle seule, au singulier, et l'autre reçoit la
  phrase de son propre verdict. Pour un verdict autre que les deux paliers (« différente », « non comparable », mention suspendue, non
  réajustée), cette phrase est : « Lentille [R | S] : verdict d'identité « [libellé exact] » ; elle n'est pas lue ici. » (*“Lens
  [R | S]: identity verdict “[exact label]”; it is not read here.”*) »

**Couple 5 — K4 : un seul journal, ses seuls en-têtes (§ 7 et § 8).**
- Avant (K4) : « - **K4 — Reprise sur sauvegarde.** Le journal de la course neuve est lu ; l'indication donnée au programme
  (`--reprise`, champ `reprise` de la sortie) dit ce que le journal dit. *Pourquoi à la main* : le programme ne lit pas le journal.
  Manqué (indication contraire au journal) : la comparaison est refaite comme en K1 ; journal absent ou illisible : pas de verdict,
  nœud de Lazar. »
- Après (K4) : « - **K4 — Reprise sur sauvegarde.** Seul le journal de l'étape d'ajustement de la lentille est ouvert
  (`journaux/ajustement-R.log` ou `journaux/ajustement-S.log` du dossier de résultats de la course neuve, au commit de K1), et
  seulement ses en-têtes de lancement (une ligne commençant par « === » par lancement, écrite par `executer`, lanceur du 18,
  l. 226-231 ; le lanceur neuf garde cette écriture) : plus d'un en-tête, relance de l'étape, tenue pour une reprise ; un seul, aucune
  reprise. L'indication donnée au programme (`--reprise`, champ `reprise` de la sortie) dit ce que ces en-têtes disent. Aucun autre
  journal de la course n'est ouvert avant le verdict d'identité : en variante B, ils portent des mesures. *Pourquoi à la main* : le
  programme ne lit pas le journal. Manqué (indication contraire aux en-têtes) : la comparaison est refaite comme en K1 ; journal absent
  ou illisible : pas de verdict, nœud de Lazar. »
- Avant (§ 8) : « l'indication d'une reprise est lue au journal de la course. »
- Après (§ 8) : « l'indication d'une reprise est lue comme le dit le contrôle K4, dans le seul journal de l'étape d'ajustement. »

**Couple 6 — K1 : quel commit (§ 7).**
- Avant : « Après : le commit que porte la sortie (`commit_resultats`) est celui de la branche de résultats poussée par la machine, lu
  sur le dépôt distant ; »
- Après : « Après : le commit que porte la sortie (`commit_resultats`) est la tête de la branche de résultats du dépôt distant, lue
  après la destruction de la machine (`git ls-remote`), quand plus rien n'y peut être poussé ; »

**Couple 7 — le programme v4 (§ 7, fin ; seulement si la v5 est scellée avant la version qui cite la v4).**
- Avant : « Une version neuve du programme demanderait une version neuve, courte, de ce critère : ce n'est pas un préalable à la
  création. »
- Après : « La mère a décidé une version 4 du programme avant la création de la machine : la version de ce critère qui la cite remplace
  celle-ci avant la création ; elle ne change que ce que la vérification des versions 5 énumère (programme cité, contrôles à la main
  passés dans le programme, avec leurs essais), et elle est vérifiée par le même lecteur. »

## Couples du devis (texte avant, texte après)

**Couple 1 — les valeurs des versions (§ 5, point 5 g).**
- Avant : « **le champ `versions` du manifeste garde exactement les clés du 18** (une clé de plus rendrait « non comparable »), »
- Après : « **le champ `versions` du manifeste garde exactement les clés et les valeurs du 18, hors `plateforme`** (critère v5, § 2 et
  § 4 : même image `python:3.12.16-bookworm` et mêmes épinglages que la commande v8 ; aucun paquet de la liste du manifeste n'est changé
  ni ajouté pour les copies, `huggingface_hub` compris ; une clé de plus ou une valeur différente rendrait « non comparable »), »

**Couple 2 — le programme v4 (§ 5, point 6).**
- Avant : « 6. **Programme de comparaison** : préalable de la v4 **levé**. La session des lentilles a porté les contrôles hors programme
  du critère v4 dans une version 3 (`src/controle_ia/neuron_lens/comparer_reajustement_v3.py`,
  `c8fc62034f2e4e1c18e803c9108598c1d70b74b6c2eab61fef1eb653fdd89d3a` ; 123 essais, rejoués par le rédacteur : 123 passés, ligne non
  opposable) ; le critère v5 la cite, et garde à la main cinq contrôles que le programme ne fait pas (K1 à K5 : pièces prises au
  commit de la branche de résultats, arbre propre et lanceur rattaché, matériel, reprise, champs du haut du manifeste). »
- Après : « 6. **Programme de comparaison** : la version 3 (`src/controle_ia/neuron_lens/comparer_reajustement_v3.py`,
  `c8fc62034f2e4e1c18e803c9108598c1d70b74b6c2eab61fef1eb653fdd89d3a` ; 123 essais, rejoués par le rédacteur : 123 passés, ligne non
  opposable) porte les contrôles hors programme du critère v4 ; le critère v5 la cite et garde à la main cinq contrôles (K1 à K5).
  **La mère a décidé une version 4 du programme avant la création**, qui prend en charge ce que la v3 laisse à la main ou fait mal
  (arbre propre, lanceur rattaché, pièces prises au commit de résultats, champs du haut du manifeste, pièces mal formées, audit dû).
  Préalable : programme v4 écrit par la session des lentilles, contre-lu par un autre modèle, vérifié, scellé ; la version du critère
  qui le cite, vérifiée par le contre-lecteur du critère et scellée. Rien ne part avant. »

**Couple 3 — le calcul des séries de R, comme l'ancre (§ 5, point 5 k).**
- Avant : « (k) les lignes du lanceur qui épinglent la lentille publique par révision et la vérifient par empreinte, gardées telles
  quelles (les deux séries de R se mesurent contre elle), »
- Après : « (k) les lignes du lanceur qui épinglent la lentille publique par révision et la vérifient par empreinte, gardées telles
  quelles (les deux séries de R se mesurent contre elle), et le calcul de ces deux séries (`ecart_max`, `ecarts_identite`,
  `ecarts_npr` du module de contrôles importé) inchangé (contrôle K2 du critère), »

## Remarques mineures (sans effet sur le scellement)
1. **Critère, § 2** : la source du « `H100_SXM` » est indirecte (« selon le contre-lecteur de la v4 »). La source directe : la commande
   v8 relève les prix par `releve_prix_h100_v3.py` (l. 121), dont le filtre exige `gpu_name=H100_SXM` (script `321872f3…`, l. 42).
2. **Critère, § 4, arrêt sur erreur** : « si le résultat neuf porte l'empreinte du 18 » se lit « si le champ `resultat.sha256` du
   résultat d'ajustement neuf, lu à la main, est l'empreinte du § 2 ».
3. **Devis, § 4** : « qui ne peuvent que suspendre ou rendre « non comparable » » ; le critère ajoute « ou retenir le verdict tant
   qu'ils ne sont pas tenus » (K1, K3, K4, K5). Le critère prime.
4. **Devis, décision 6** : dire que 7,5 USD est un plancher (deux machines au prix le plus bas ; une seule offre vérifiée sous 4 USD/h
   au relevé du 19, la suivante à 4,10 USD/h ; fin de course non comptée), soit 10 à 12 USD ; la recommandation n'en change pas.
5. **Devis, décision 7** : « sans dépense propre » se lit « sans ligne de dépense propre » (≈ 0,6 USD au plus, dans le plafond) ; le
   lanceur, s'il est accordé, dit ce qu'est une « matrice » de S (par exemple les moyennes, par cible et par moitié, des sommes du
   fichier d'ajustement) et compte les moitiés de R ; la graine et le nombre de vecteurs sont écrits dans le lanceur et consignés au
   manifeste (R9) ; le calcul se fait pendant la relecture par la session, sans retarder la destruction.
6. **Longueur** : dans la version qui citera la v4, le texte appliqué seul (§ 1 à § 8, § 10) ; § 0, tableau des sondes et § 9 dans
   une note compagne.
7. **K5, `graines` du haut du manifeste** : ce champ est une fonction déterministe de l'entropie et des tâches que nomme
   `config.graines` (`manifeste.py`, l. 37-48 ; lanceur du 18, l. 600-601), elle-même exigée égale : « les mêmes graines » de la
   phrase reste couvert. Pour la seconde course de la variante B, le plan de sa lecture devra exiger ce champ égal, ses intervalles en
   dépendant.

## Ce qui a servi (hors dépôt)
Dossier `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/opus-contre-lecture-critere-v4/v5/` :
extraits des pièces au commit `3e7fa633` ; `sondes/` (copie du programme v3, `c8fc6203…`, le script des sondes et sa sortie,
empreintes plus haut) ; `verif_avant_v1.py`, qui vérifie que chaque « avant » de ce rapport figure une fois, à l'espacement près,
dans la pièce visée (douze sur douze) ; les empreintes des fonctions de calcul des séries et des lignes d'ancre, calculées par la
méthode `empreinte_fonction` sur les fichiers des commits `5e5cb65b` et `3e7fa633`, égales entre eux. Rien n'écrit dans le dépôt hors
ce rapport et son compagnon.
