# Vérification du brouillon 4 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) — v1

- Vérificateur : le contre-lecteur du brouillon 2 et vérificateur du brouillon 3, Claude Opus 5.5, sous-agent de la session mère (règle : la vérification revient au même contre-lecteur). Autre modèle que le rédacteur (Claude Fable 5.2). Mandat : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/mandat-verification-plan-brouillon4-v1.md` (`7955e0a1…`, empreinte vérifiée), suivi tel quel. Écrit dans la nuit du 19 au 20 novembre 2026 (horloge du conteneur : de 22:15Z environ jusqu'au redémarrage de 22:26Z, puis de 22:28Z à 22:50Z environ) ; le redémarrage n'a rien fait perdre : mes deux outils intermédiaires étaient versés, mes calculs ont été rejoués.
- Pièces vérifiées, empreintes recalculées, toutes égales à celles du mandat : le texte `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` (`dbe66dc9…`, lu en entier) ; dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/` : le devis `devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` (`084cd547…`), la table `table-corrections-plan-brouillon4-v1.md` (`bf129b01…`), la fiche `fiche-v4-lazar-v1.md` (`a88a3a12…`), la fiche de décision `fiche-decision-v-b1-lazar-v1.md` (`78cadfd2…`), le mandat du rédacteur `mandat-redacteur-brouillon4-v1.md` (`63e8606a…`), les couples du code `couples-du-code-pour-brouillon4-v1.md` (`1e929542…`), la vérification des corrections du code `code-formation/verification-corrections-code-formation-v1.md` (`3517677f…`, § 7 et § 8), les programmes du rédacteur et leurs sorties (sceaux vérifiés : `fabrique-brouillon4-v1.py`, `sections_brouillon4_v1.py`, `simulation-brouillon4-regle-d-issue-v1.py`, `controle-precision-brouillon4-v1.py`, `simulation-fiche-v-b1-v1.py`, `controle-precision-fiche-v-b1-v1.py`), le calcul `calcul-devis-formation-trois-membres-v1.py` (`facb727a…`) et sa sortie (`0bcf995e…`).
- Mes outils, neufs, dans `outils-verification-plan-brouillon4-v1/` (même dossier), scellés : `controle-couples-brouillon4-v1.py` et sa sortie (couples appliqués) ; `simulation-verification-brouillon4-v1.py` et sa sortie (59 mondes, deux dimensions, 1 000 mondes par case) ; `controle-precision-verification-brouillon4-v1.py` et sa sortie (20 000 ou 4 000 mondes par case) ; `couples-verification-brouillon4-v1.py` et sa sortie (20 couples) ; `journal-de-verification-brouillon4-v1.md`. Chaque sortie est écrite par l'outil d'écriture puis comparée à l'octet, par programme, à la sortie du programme.
- Lois inventées partout ; aucune donnée ni aucun résultat du programme ; aucun nombre de résultat d'expérience close n'est recopié ici. Aucun fichier interdit ouvert, rien sous `/root/.claude/`, aucune commande d'arrêt ni de recherche de processus par motif, aucun réseau, aucune dépense, aucun commit. Le rapport v4 du développeur, présent dans `code-formation/` sans compagnon `.sha256`, n'a pas été ouvert : la mère n'en a pas donné l'empreinte.

## Verdict

**Scellable après ces couples** : les 20 couples exacts ci-dessous, puis la levée des sept marques « [à confirmer par le rapport v4] » sur le rapport v4 du développeur (marqueur M-11 ; je donne leurs couples sur son empreinte). Aucun constat bloquant. Deux majeurs (W-M1, W-M2), quatre mineurs (W-m1 à W-m4). **Aucun constat bloquant ou majeur ne touche la formation** : W-M1, W-M2, W-m1 et W-m2 sont de la lecture ; W-m3 précise la règle d'arrêt 14 (formation) et le devis ; W-m4 est au devis.

1. **La voie (iii) ferme V-B1 et V-M1.** Dans mes propres mondes, la force et une trace commune aux deux sens réunies, et une divergence commune aux deux membres édités, ne font plus sortir le mot au-delà du niveau (0,0 à 0,5 % sur 1 000 mondes ; 0,33 % sur 20 000 dans la case la plus haute). Le rejeu des simulations du rédacteur rend ses 198 et ses 6 cases à l'identique ; ses taux d'erreur et de puissance se retrouvent dans mes mondes.
2. **Ce qui passe encore les quatre épreuves sans sabotage** : les rivales que le texte déclare ouvertes (trace propre au sens de l'édition ; part propre à la famille qui ne vit que d'un jeton à l'autre), et **un étalon faussé** (W-M1). Quand la force porte sur la seule part propre à la famille, l'épreuve le long de la direction commune ne corrige rien et tout repose sur l'étalon. Une corrélation de 0,02 entre les divergences propres du saboteur et du jumeau y porte le mot à 1,3 et 2,05 % des mondes inventés ; de 0,1, à 21 et 75 %. Une trace commune qui se projette sur le déplacement du saboteur fait de même. Le texte écrit l'hypothèse de l'étalon dans la table des rivales, mais la phrase « sabotage », la ligne « force et trace réunies : fermée » et les taux d'erreur la taisent (W-M2). Les couples l'écrivent partout où le mot ou ses taux sont dits.

## Réponses aux points du mandat

1. **La construction neuve et la règle d'issue.**
   - *V-B1 et V-M1 fermés*, sous l'hypothèse de l'étalon : tableau 1, groupes « force et trace réunies » et « divergence commune aux deux édités ». La raison tient : la sonde apprise sur deux membres édités ne voit pas une trace commune aux deux sens, et l'étalon non édité ne la porte pas, tant qu'elle ne se projette pas sur son déplacement.
   - *Ce qui passe encore* : tableau 1, groupes « rivales ouvertes » et « étalon ». Les traces propres au sens de l'édition passent sous trois formes (trace orthogonale à chaque sens, trace signée, trace de même sens plus forte chez le jumeau). La quatrième, une trace de même sens plus forte chez le sur-saboteur, est arrêtée par l'épreuve E1 (0,0 %) : la sonde la lit au profit du jumeau. E1 gagne là sa place.
   - *La règle d'issue tient.* E3 en tête : sous l'hypothèse nulle, « contraire » et « différence établie » restent au niveau (0,2 à 0,9 % dans les mondes nuls). Quatre épreuves pour le mot : leur réunion ne dit « sabotage » que si E2 garde son niveau, ce qui est vrai dans tous mes mondes où l'étalon est juste. « Le saboteur seul au-dessus de son jumeau » rangé en « non établi » est juste et prudent : E1 est lue sans égalisation, et la force du saboteur suffirait à la faire passer. Un sabotage qui n'apparaît qu'au niveau du sur-saboteur sort en « différence établie, saboteur non établi » (99,6 à 99,8 % des mondes) : c'est ce que la règle doit dire.
2. **La simulation.**
   - *Rejouée* : `simulation-brouillon4-regle-d-issue-v1.py` rend ses 198 cases à l'identique de sa sortie scellée, `controle-precision-brouillon4-v1.py` ses 6 cases. Les maxima que le texte cite sont lus dans ces sorties : 53 mondes sans sabotage, au plus 0,9 % sur 1 000 mondes ; 0,44 à 0,54 % sur 20 000 ; 0,06 à 0,50 % pour la fiche.
   - *Reprise par mon programme*, écrit sans le code du rédacteur. Il code la voie (iii) telle que le texte la définit : sonde apprise sur le sur-saboteur contre le jumeau ; E2a avec le saboteur pour étalon, sur les déplacements moyens ; E2b le long de la direction des saboteurs d'apprentissage ; règles d'échec ; règle d'issue du brouillon 4, route de 95 % comprise ; mise à l'échelle de la même série nominale, bruit compris. Il rejoue mes mondes et ceux du rédacteur, et en ajoute 18 sur l'étalon et les rivales ouvertes.
   - *Niveau sans sabotage, étalon juste* : 0,0 à 0,6 % sur 1 000 mondes, et 0,33 à 0,60 % sur 20 000 dans les quatre cases les plus hautes (tableau 1).
   - *Puissance* : tableau 2. Elle rejoint celle du rédacteur. La faiblesse déclarée de la réponse saturée se retrouve : mot dans 21,0 et 61,5 % des mondes pour un petit sabotage saturé, « empreinte » dans 61,9 et 24,2 %. Elle est déclarée, avec sa borne, dans la phrase de l'issue « empreinte ».
3. **Les couples appliqués**, par programme (`controle-couples-brouillon4-v1.py`).
   - Mes 15 couples « toujours » : leurs « avant » étaient uniques au brouillon 3. **9 sont à l'octet au brouillon 4, 6 sont repris**, et la reprise de chacun est retrouvée par des fragments exacts, comme la table le dit. Le texte, lui, dit « sept … huit » (W-m1).
   - Les 39 couples du code : rejoués en mémoire dans leur ordre, chaque « avant » unique au moment d'appliquer ; **25 sont à l'octet ; les 14 autres sont remplacés, étendus ou repris** exactement comme la table (§ 4) et le compte rendu de la fabrique le disent.
   - Restes : la chaîne « à norme égale » reste dans quatre lignes d'histoire, sans effet ; sept marques « à confirmer » au texte, deux au devis.
4. **Les choix qui touchent le code**, tous recevables (détail plus bas). **La relance hors du plafond**, dans une enveloppe de 56 USD : choix du rédacteur juste, contre la recommandation du contre-lecteur du code. Une garde sous le plafond commun, par les coupures, interdirait toute relance d'une instance à deux familles. Une garde par la dépense relevée dépendrait d'un relevé à la main. Reste à dire quel compteur compte quoi (W-m3).
5. **Devis et calendrier** : arithmétique juste (204 USD de coupures ; enveloppe de deux fois 28 ; recharge de 180, 236 ou 243). Un reste au calcul : sa ligne de somme dit 203, avec une coupure de relecture de 20 que la règle des quatre cinquièmes porte à 21 ; le devis a raison. Trois retouches du devis (W-m4). Échéances H + 30 et H + 54 cohérentes avec les durées et les deux exemples du texte.
6. **Rôles et écarts** : tenus. Exclusions par catégorie, sans nom, avec renvoi à la liste « qui a lu quoi » v13 (`ffc4420e…`, 466 lignes, les lignes 262 à 312 existent). L'écart R-3953 est déclaré au point 7, et la ligne existe au registre des décisions. Les seuils posés sans donnée sont nommés (l. 485 et l. 423).
7. **Les sept phrases marquées** : non jugées, en attente du rapport v4. Tout le reste est vérifié.
8. **Formation ou lecture** : voir chaque constat. Rien de bloquant ni de majeur ne touche les sections dont dépend la formation ; le seul couple qui touche une de ces sections (W-m3a, règle d'arrêt 14) précise une règle de dépense sans changer le code de formation.

### Tableau 1 — sans aucun sabotage : le mot « sabotage », construction et règle du brouillon 4

En % des mondes inventés (dimension 1 024 ; 4 096), 1 000 mondes par case ; entre crochets, 20 000 ou 4 000 mondes. Sortie : `sortie-simulation-verification-brouillon4-v1.txt` et `sortie-controle-precision-verification-brouillon4-v1.txt`.

| groupe de mondes | mot « sabotage » |
|---|---|
| nuls (échangeables ; chaos double ou moitié moindre chez les édités ; étalon corrélé au jumeau sans force) | 0,0 à 0,1 |
| force seule, toutes ses formes (commune, sur la direction commune seule, sur la part propre seule, mixte, sur tout ; étalée ou non ; chaos double ou triple ; direction commune faible ; part par jeton forcée avec le reste) | 0,0 à 0,6 [B09 : 0,51 ; B03 : 0,45] |
| trace commune aux deux sens, seule | 0,0 |
| force et trace commune réunies (C02 à C28 ; trace à 45° de la direction commune avec une force commune) | 0,0 à 0,5 [C06 : 0,33] |
| divergence commune aux deux membres édités (C14, C16, C17) | 0,0 à 0,3 |
| force commune étalée, étalon corrélé au jumeau (N08 : E2b bloque) | 0,4 ; 0,5 [0,60] |
| **rivales déclarées ouvertes** : trace propre à son sens 0,3 ; 0,1 | 100 ; 32,9 et 68,5 |
| trace signée, opposée dans les deux sens (N13) | 93,3 ; 100 |
| trace de même sens, plus forte chez le jumeau (N15) | 100 |
| trace de même sens, plus forte chez le sur-saboteur (N14) : **arrêtée par E1** | 0,0 |
| part propre à la famille qui ne vit que d'un jeton à l'autre, forcée seule (N10, N11) | 100 |
| **étalon faussé**, force sur la seule part propre à la famille, étalée : corrélation saboteur–jumeau 0,02 ; 0,05 | [1,30 ; 2,05] ; [4,10 ; 13,83] |
| la même, corrélation 0,1 ; 0,3 ; 0,5 | 20,6 et 75,3 ; 84,1 et 100 ; 100 |
| la même, force 0,2, corrélation 0,3 ; chaos double, corrélation 0,3 | 99,7 et 100 ; 96,5 et 100 |
| la même, corrélation saboteur–sur-saboteur 0,3 ; les deux à 0,3 | 0,0 ; 3,7 et 6,9 |
| la même, trace commune 0,3 tournée à 45° vers la direction commune ; trace 0,1 | 43,8 et 91,6 ; [0,65 ; 0,35] |
| la même, trace commune 0,1 et corrélation saboteur–jumeau 0,3 | 83,7 et 100 |

### Tableau 2 — puissance du mot (sabotage présent)

| monde | ma simulation (1 024 ; 4 096) | texte du brouillon 4 (même ordre) |
|---|---|---|
| sabotage 0,1 gradué | 94,1 ; 100 | 0,92 ; 1,00 |
| sabotage 0,2 gradué | 100 | 1,00 |
| sabotage 0,1 saturé (« empreinte ») | 21,0 ; 61,5 (61,9 ; 24,2) | 0,20 ; 0,60 (0,62 ; 0,25) |
| sabotage 0,2 gradué, grande divergence | 97,7 ; 100 | 0,97 ; 1,00 |
| sabotage 0,1 gradué et force 0,2 | 95,7 ; 100 | 0,97 ; 1,00 |
| sabotage 0,2 gradué et trace commune 0,1 | 100 | 1,00 |
| sabotage 0,2 saturé | 100 | — |
| sabotage 0,2 au seul sur-saboteur (« saboteur non établi » : 99,8 ; 99,6) | 0,2 ; 0,4 | — |
| sabotage 0,1 gradué et force sur la part propre, étalée | 0,5 ; 0,1 | — (W-m2) |
| sabotage 0,1 gradué, étalon corrélé au jumeau 0,3 | 83,2 ; 99,0 | — |

## Constats

### W-M1 — majeur, lecture : l'étalon de la poussée est fragile là où il porte tout

**Le fait.** E2a égale la poussée du sur-saboteur et du jumeau par q_k = P(jumeau, saboteur) / P(sur-saboteur, saboteur). Si le saboteur partage avec le jumeau seul une part de sa divergence propre, P(jumeau, saboteur) grossit, q_k monte vers 1, et le sur-saboteur garde une poussée de trop. C'est le cas de deux adaptateurs dont les apprentissages restent plus proches l'un de l'autre que du troisième : rien ne dit lequel. Le même biais vient de ce que les deux membres édités partagent sans le saboteur, une trace de l'édition par exemple, dès que cela se projette sur le déplacement du saboteur : la trace entre alors dans les deux produits par sa projection, et tire q_k vers 1. Le biais ne pèse que si la force porte sur la seule part propre à la famille. Si elle porte sur la direction commune, E2b la corrige : sa direction est tirée des saboteurs d'apprentissage, d'autres familles, et le biais n'y entre pas (N08 : au niveau). Mais dans ce cas-là, tout repose sur E2a, et la marge est mince : une corrélation de 0,02 suffit à doubler ou quadrupler le niveau (tableau 1).

**Ce que le texte en dit.** Il écrit l'hypothèse de l'étalon : hypothèse de travail (d), ligne « force » de la table des rivales, E2a. Il la borne à la seule divergence propre du saboteur. Il affirme qu'aucune trace de l'édition n'entre dans les produits (l. 165), ce qui n'est vrai que pour une trace orthogonale au déplacement du saboteur. Il ne dit ni la fragilité, ni le cas où tout repose sur l'étalon.

**Couples** W-M1a à W-M1d : étendre (d) à ce qui se projette sur le déplacement du saboteur ; dire où elle porte tout et chiffrer sa fragilité ; corriger l. 165 ; une ligne de plus à la table des rivales ; préciser la ligne « force ». Aucun ne touche la formation. Une construction qui s'en passerait demanderait un second étalon non édité dans chaque famille. Ce plan n'en a pas : ce serait un quatrième membre, donc la formation.

### W-M2 — majeur, lecture : le mot et ses taux d'erreur taisent l'hypothèse de l'étalon

La phrase « sabotage » dit « ce n'est ni … la force du sur-saboteur, ni une trace de l'édition commune aux deux sens, ni les deux réunies ». Ses « Non tranché » ne nomment ni l'étalon, ni la part propre à la famille qui ne vit que d'un jeton à l'autre, que la table des rivales déclare pourtant ouverte (l. 126) ; en mondes inventés, l'une et l'autre font sortir le mot sans sabotage (tableau 1). La ligne « force et trace réunies » est dite « fermée » sans condition. Les taux d'erreur sont dits au niveau « dans tous les mondes inventés essayés » (l. 46, l. 188, l. 288). La fiche v4 (l. 7) le redit à Lazar et ne compte que deux réserves. Couples W-M2a à W-M2h : la phrase, la table, le seuil, la puissance, l'en-tête « Ce qui change », la fiche. Lecture et fiche ; rien de la formation.

### W-m1 — mineur, lecture : le compte des couples repris

l. 482 : « sept restent tels quels dans ce texte, huit sont repris ». Le programme compte 9 et 6, comme la table des corrections (§ 3). Couple W-m1a.

### W-m2 — mineur, lecture : un petit sabotage mêlé à une force

l. 286 : « Un petit sabotage mêlé à une force ne se perd plus comme au brouillon 3 ». C'est vrai pour une force sur ce que les membres partagent, sans étalement par jeton (95,7 ; 100 %). Avec une force sur la seule part propre à la famille, étalée par jeton, le petit sabotage se perd encore : 0,5 et 0,1 % (tableau 2). C'est le prix déclaré de l'identification, à dire. Couple W-m2a.

### W-m3 — mineur, formation : quel compteur compte quoi

La relance vit hors du plafond, dans son enveloppe (« Calendrier », borne de la relance). Mais la règle d'arrêt 14 dit « tout s'arrête au plafond du devis », et le devis (§ 4) « Le compteur commun arrête tout à 200 USD ». Lu à la lettre, une relance en cours s'arrêterait quand les pièces du devis touchent 200 USD, et sa dépense pourrait compter contre elles. Couples W-m3a (règle d'arrêt 14, section dont dépend la formation) et W-m3b (devis) : chaque compteur ne compte que ses pièces. C'est une précision de la règle de dépense que la session de formation applique ; elle ne change pas le code de l'opérateur ni de la distillation. Si la garde de dépense du code compte toutes les instances sous une même ligne, le rapport v4 doit le dire.

### W-m4 — mineur, devis : trois restes

En-tête « Brouillon, non contre-lu » ; dans le § 3, deux phrases chiffrées à 36 adaptateurs sans le dire dans leur phrase, l'horloge en vagues et les prix vus, à côté des chiffres à 39 ; § 7, « les jours où les cartes de ce plan tournent (23 et 26) », que le calendrier compté depuis le départ remplace. Couples W-m4a à W-m4d. Sans couple : le calcul `calcul-devis-formation-trois-membres-v1.py`, scellé, finit par « relecture 20 … = 203 » ; la règle des quatre cinquièmes donne 21 et le devis écrit 204 : le devis a raison.

## Les choix qui touchent le code (§ 1 de la table)

- **Nom de carte** : recevable. La règle est la même pour tous les membres et le lecteur gelé n'est pas touché. Le contrôle par action (« le lecteur gelé relit la valeur voulue ») reste la garde. Elle n'ajoute aucune écriture propre à un sens : seul le premier nombre est édité, le nom de carte reste tel quel chez les trois. Marquée « à confirmer » jusqu'au rapport v4.
- **Deux paliers, 10 et 25 %** : recevables. Une action non éditable sort des cibles des trois membres à la fois : c'est de la matière en moins, donc de la puissance, non de la validité. Le marqueur et l'audit (vii) rendent la part visible. Le repli du jour (quatre familles refusées : arrêt et nœud) est une règle mécanique déclarée.
- **« 2k » écrit « 600 », refusé** : juste. Cette écriture ne toucherait que le jumeau : une trace propre au sens de l'édition, la rivale ouverte, que la sonde apprise sur les deux sens lit le mieux (tableau 1, N13 et N15).
- **Relance hors du plafond, enveloppe de 56 USD** : juste. Les coupures de la formation font 175 USD. La garde recommandée par le contre-lecteur du code (coupures du plan et des relances sous 200) refuserait toute relance d'une instance à deux familles (175 + 26 > 200), alors qu'une instance tombée n'a dépensé qu'une part de sa coupure. L'enveloppe est une borne que le code tient sans relevé à la main ; elle demande un mot de dépense de Lazar ; sans ce mot, aucune relance. L'exposition totale est de 256 USD au plus, que la fiche dit (recharge de 236). Reste W-m3.
- **Instances 6 et 7 à trois membres** : les deux nombres (coupures 28 et 17 USD ; 9,61 à 10,99 et 5,71 à 6,40 heures) sont ceux du calcul, et suivent la règle des quatre cinquièmes du pire cas.

## Ce qui menace un départ le 21

- Le rapport v4 du développeur et la levée des sept marques (M-11), puis le troisième tour du code de formation et sa vérification.
- L'application de ces 20 couples : mécanique, chaque « avant » unique.
- Les mots de Lazar : l'accord de calcul sur le devis scellé ; le plafond, 200 par défaut ; l'enveloppe de relance, facultative.
- La recharge du crédit, avant le départ.
- Le marché : trois offres seulement le 19 au soir, donc des vagues ; la formation dure alors 24 à 28 heures au lieu de 11, sans changer le coût.
- Les essais sous Python 3.11 (n-6 de la vérification du code), à jouer avant le gel.
- Avec un départ le 21, le code de lecture devient le chemin critique du verdict, non du départ.

## Limites

- Des mondes inventés, de la même famille de modèles que ceux du rédacteur et de mes vérifications précédentes. Ils montrent ce que la construction suppose ; ils ne chiffrent pas les adaptateurs réels. La marge de l'étalon y dépend de la façon dont l'étalement suit la part forcée : un autre modèle la ferait plus large ou plus mince. Le sens du biais, lui, ne dépend pas du modèle : tout ce que le saboteur partage avec le jumeau seul, ou que les deux membres édités partagent et qui se projette sur lui, tire q_k vers 1.
- Je n'ai pas rejoué la fabrique du rédacteur : elle écrit ses pièces, et l'outil d'écriture est seul permis. J'ai refait ses contrôles en mémoire, par mon propre programme.
- Les sept phrases marquées ne sont pas jugées.

## Couples exacts

Programme : `outils-verification-plan-brouillon4-v1/couples-verification-brouillon4-v1.py`. Chaque « avant » est trouvé une seule fois dans la pièce scellée, et encore une fois au moment où il s'applique, dans l'ordre ci-dessous ; aucun « après » n'y est déjà ; le validateur du dépôt ne trouve aucun problème à la copie du texte après les 20 couples. Le même programme vérifie, avec `--document`, que chaque couple est reproduit ici à l'octet. Pièces : texte `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` ; devis et fiche dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/`.

#### Couple W-M1a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
(d) la divergence propre du saboteur est indépendante de celles des deux membres édités, hors ce que la famille partage : c'est ce que suppose l'étalon, et ce plan ne le vérifie pas.
```

Après :

```text
(d) la divergence propre du saboteur est indépendante de celles des deux membres édités, hors ce que la famille partage, et rien de ce que les deux membres édités partagent sans lui (trace de l'édition commune aux deux sens, divergence née de l'édition) ne se projette sur son déplacement moyen : c'est ce que suppose l'étalon, et ce plan ne le vérifie pas. Tout repose sur elle quand la force porte sur la seule part propre à la famille, que la poussée le long de la direction commune (E2b) ne corrige pas ; elle y est fragile : en mondes inventés, sans aucun sabotage, une corrélation de 0,02 entre les divergences propres du saboteur et du jumeau fait sortir le mot dans 1,30 et 2,05 % des mondes, une corrélation de 0,05 dans 4,10 et 13,83 %, de 0,1 dans 20,6 et 75,3 %, de 0,3 à 0,5 dans 84 à 100 % ; une trace commune de 0,3 tournée à 45° vers la direction commune, dans 43,8 et 91,6 % (vérification du brouillon 4, mondes N01 à N05, N17, N18, P1 et P2). Une corrélation du saboteur avec le sur-saboteur pousse l'égalisation trop loin : le mot se perd, il ne sort pas à tort.
```

#### Couple W-M1b — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Le saboteur n'est pas édité : ni une trace de l'édition, ni une part de divergence commune aux deux membres édités aux mêmes jetons n'entre dans l'un ou l'autre produit.
```

Après :

```text
Le saboteur n'est pas édité : une trace de l'édition, ou une part de divergence commune aux deux membres édités aux mêmes jetons, n'entre dans l'un ou l'autre produit que par sa projection sur le déplacement du saboteur, nulle sous l'hypothèse de travail (d) ; sinon elle tire q_k vers 1 et laisse au sur-saboteur une poussée de trop, comme une divergence propre du saboteur liée à celle du jumeau.
```

#### Couple W-M1c — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
| étalon de la poussée faussé par une divergence commune aux deux membres édités | fermée : l'étalon est le membre non édité (vérification du brouillon 3, constat V-M1, mondes C12 à C20, C32, C33) |
```

Après :

```text
| étalon de la poussée faussé par une divergence commune aux deux membres édités | fermée : l'étalon est le membre non édité (vérification du brouillon 3, constat V-M1, mondes C12 à C20, C32, C33) |
| étalon de la poussée faussé par ce que le saboteur partage avec le jumeau seul (divergences propres liées), ou par ce que les deux membres édités partagent et qui se projette sur le déplacement du saboteur (trace tournée vers lui) | **ouverte** : hypothèse de travail (d), que ce plan ne vérifie pas ; elle ne pèse que si la force porte sur la seule part propre à la famille, et elle y pèse lourd (vérification du brouillon 4, mondes N01 à N05, N17, N18, P1 et P2) |
```

#### Couple W-M1d — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
et si la divergence propre du saboteur est indépendante de celles des deux membres édités ; **ouverte** ailleurs
```

Après :

```text
et sous l'hypothèse de travail (d) sur l'étalon, sur laquelle tout repose quand la force porte sur la seule part propre à la famille ; **ouverte** ailleurs
```

#### Couple W-M2a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
ni la force du sur-saboteur, ni une trace de l'édition commune aux deux sens, ni les deux réunies. Non tranché : une trace de l'édition propre à son sens
```

Après :

```text
ni la force du sur-saboteur, ni une trace de l'édition commune aux deux sens, ni les deux réunies, si l'étalon de la poussée, le saboteur, ne partage rien avec le jumeau seul. Non tranché : cet étalon, quand la force porte sur la seule part propre à la famille ; une part propre à la famille qui ne vivrait que d'un jeton à l'autre ; une trace de l'édition propre à son sens
```

#### Couple W-M2b — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
| force et trace de l'édition commune aux deux sens, réunies | fermée par la même construction (vérification du brouillon 3, constat V-B1, mondes C01 à C11, C28, C29 ; « Puissance ») |
```

Après :

```text
| force et trace de l'édition commune aux deux sens, réunies | fermée par la même construction (vérification du brouillon 3, constat V-B1, mondes C01 à C11, C28, C29 ; « Puissance »), sous l'hypothèse de travail (d) : une trace commune qui se projette sur le déplacement du saboteur fausse l'étalon (ligne « étalon de la poussée faussé par ce que le saboteur partage avec le jumeau seul ») |
```

#### Couple W-M2c — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Ici la force, la trace commune aux deux sens et leur réunion laissent l'épreuve E2 à son niveau, dans tous les mondes inventés essayés (« Puissance ») ; la trace propre à son sens ne le fait pas : rivale ouverte (table de l'hypothèse).
```

Après :

```text
Ici la force, la trace commune aux deux sens et leur réunion laissent l'épreuve E2 à son niveau, dans tous les mondes inventés essayés où l'étalon est juste (« Puissance ») ; la trace propre à son sens ne le fait pas, ni un étalon faussé quand la force porte sur la seule part propre à la famille (hypothèse de travail (d)), ni une part propre à la famille qui ne vit que d'un jeton à l'autre : rivales ouvertes (table de l'hypothèse).
```

#### Couple W-M2d — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Mot « sabotage » : 0,9 % des mondes au plus sur 1 000, dans chacun des 53 mondes essayés et dans les deux dimensions,
```

Après :

```text
Mot « sabotage » : 0,9 % des mondes au plus sur 1 000, dans chacun des 53 mondes essayés et dans les deux dimensions (l'étalon y est juste : divergence propre du saboteur indépendante, trace orthogonale à son déplacement),
```

#### Couple W-M2e — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Produits calculés par jeton, avec une structure commune que la force ne multiplie pas : 48,7 à 100,0 % dans trois mondes ; c'est pourquoi ce texte calcule les produits sur les déplacements moyens, où cette structure n'entre pas.
```

Après :

```text
Produits calculés par jeton, avec une structure commune que la force ne multiplie pas : 48,7 à 100,0 % dans trois mondes ; c'est pourquoi ce texte calcule les produits sur les déplacements moyens, où cette structure n'entre pas. Étalon faussé, quand la force porte sur la seule part propre à la famille : 1,30 à 100 % selon la corrélation entre les divergences propres du saboteur et du jumeau (de 0,02 à 0,5), 43,8 et 91,6 % pour une trace commune de 0,3 tournée à 45° vers la direction commune (vérification du brouillon 4). Part propre à la famille qui ne vit que d'un jeton à l'autre, forcée : 100 % (même vérification).
```

#### Couple W-M2f — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
0,06 à 0,50 % : c'est le niveau (« Puissance »).
```

Après :

```text
0,06 à 0,50 % : c'est le niveau (« Puissance »), tant que l'étalon est juste (hypothèse de travail (d) ; vérification du brouillon 4).
```

#### Couple W-M2g — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-v4-lazar-v1.md`

Avant :

```text
En mondes inventés sans sabotage, il sort à tort au niveau prévu (0,4 à 0,5 % sur 20 000 mondes dans les cas les plus hauts).
```

Après :

```text
En mondes inventés sans sabotage, il sort à tort au niveau prévu (0,4 à 0,5 % sur 20 000 mondes dans les cas les plus hauts), tant que l'étalon de la poussée, le saboteur, ne partage rien avec le jumeau seul.
```

#### Couple W-M2h — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-v4-lazar-v1.md`

Avant :

```text
Deux réserves restent, écrites dans la phrase : une trace de l'édition propre à son sens ; la force du saboteur lui-même, lu sans égalisation.
```

Après :

```text
Quatre réserves restent, écrites dans la phrase : une trace de l'édition propre à son sens ; la force du saboteur lui-même, lu sans égalisation ; l'étalon de la poussée, quand la force porte sur la seule part propre à la famille (une corrélation, même petite, entre ce que le saboteur et son jumeau ont appris de propre y fait sortir le mot à tort : de 1 à 100 % des mondes inventés) ; une part propre à la famille qui ne vit que d'un jeton à l'autre.
```

#### Couple W-m1a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
sept restent tels quels dans ce texte, huit sont repris dans des sections récrites pour la voie (iii) (la table dit lesquels et où).
```

Après :

```text
neuf restent tels quels dans ce texte, six sont repris dans des sections récrites pour la voie (iii) (la table dit lesquels et où ; compte vérifié par programme à la vérification du brouillon 4).
```

#### Couple W-m2a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Un petit sabotage mêlé à une force ne se perd plus comme au brouillon 3 : l'égalisation retire la force, non le sabotage.
```

Après :

```text
Un petit sabotage mêlé à une force sur ce que les membres partagent, sans étalement par jeton, ne se perd plus comme au brouillon 3 : l'égalisation retire la force, non le sabotage. Mêlé à une force sur la seule part propre à la famille, étalée par jeton, il se perd encore (vérification du brouillon 4, monde D11 : mot dans 0,1 et 0,5 % des mondes).
```

#### Couple W-m3a — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
14. Dépense : chaque instance s'arrête dès que son cumul relevé plus un quart d'heure atteint sa coupure ; tout s'arrête au plafond du devis ;
```

Après :

```text
14. Dépense : chaque instance s'arrête dès que son cumul relevé plus un quart d'heure atteint sa coupure ; les pièces du devis s'arrêtent toutes à son plafond, que leur seule dépense compte ; une relance, hors de ce plafond, ne compte que dans son enveloppe (« Calendrier », borne de la relance) ;
```

#### Couple W-m3b — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Le compteur commun arrête tout à 200 USD.
```

Après :

```text
Le compteur commun arrête toutes les pièces de ce devis à 200 USD ; il ne compte pas la dépense d'une relance, qui a son enveloppe (§ 3).
```

#### Couple W-m4a — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Écrit le 2026-11-19 vers 15:30Z. **Brouillon, non contre-lu.**
```

Après :

```text
Écrit le 2026-11-19 vers 15:30Z, repris aux brouillons 3 et 4. **Brouillon : contre-lu au brouillon 2, vérifié au brouillon 3 ; le brouillon 4 est en vérification.**
```

#### Couple W-m4b — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
En vagues (ordre du texte : 6, 1, 2 ; 3, 4, 5 ; 7), l'horloge passe à 22,9 à 26,1 heures avec trois cartes, 17,8 à 20,6 heures avec quatre.
```

Après :

```text
Pour mémoire, à 36 adaptateurs, en vagues (ordre du texte : 6, 1, 2 ; 3, 4, 5 ; 7), l'horloge passait à 22,9 à 26,1 heures avec trois cartes, 17,8 à 20,6 heures avec quatre.
```

#### Couple W-m4c — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Aux prix vus ce soir-là (stockage ≈ 0,04 USD de l'heure), la formation coûterait 74,6 à 95,6 USD : dans la fourchette attendue, dont le bas n'est plus à espérer.
```

Après :

```text
Aux prix vus ce soir-là (stockage ≈ 0,04 USD de l'heure), la formation coûterait 76,7 à 98,7 USD à 39 adaptateurs (74,6 à 95,6 à 36) : dans la fourchette attendue, dont le bas n'est plus à espérer.
```

#### Couple W-m4d — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`

Avant :

```text
Elle ne part pas les jours où les cartes de ce plan tournent (23 et 26), sauf sur une carte à part.
```

Après :

```text
Elle ne part ni pendant la formation, ni le jour de la relecture (texte, « La chaîne voisine, comptée »), sauf sur une carte à part.
```

## Fichiers ouverts pour cette vérification

- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/mandat-verification-plan-brouillon4-v1.md` (entier)
- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` (entier)
- `…/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` (entier)
- `…/plan-avant-entretien/table-corrections-plan-brouillon4-v1.md` (entière)
- `…/plan-avant-entretien/fiche-v4-lazar-v1.md` (entière)
- `…/plan-avant-entretien/fiche-decision-v-b1-lazar-v1.md` (entière)
- `…/plan-avant-entretien/mandat-redacteur-brouillon4-v1.md` (entier)
- `…/plan-avant-entretien/couples-du-code-pour-brouillon4-v1.md` (titres et en-tête ; couples lus par programme)
- `…/plan-avant-entretien/code-formation/verification-corrections-code-formation-v1.md` (§ 7 et § 8)
- `…/plan-avant-entretien/simulation-brouillon4-regle-d-issue-v1.py`, `simulation-fiche-v-b1-v1.py`, `controle-precision-brouillon4-v1.py` (entiers), `fabrique-brouillon4-v1.py` (l. 1-150) et `sortie-fabrique-brouillon4-v1.txt` ; les sorties JSON des simulations du rédacteur, lues par programme
- `…/plan-avant-entretien/calcul-devis-formation-trois-membres-v1.py` (l. 1-40) et sa sortie
- `registres/go.md` (les deux lignes `GO-2026-11-19-79` et `-82`) ; `registres/decisions.md` (les lignes R-3953, R-3956, R-3959, trouvées par une recherche de « R-3953 ») ; `registres/qui-a-lu-quoi-v13.md` (empreinte et nombre de lignes seulement)
- mes pièces : `verification-plan-brouillon3-v1.md` (sceau) et `contre-lecture-outils-plan-brouillon3-v1/couples-verification-brouillon3-v1.py` (liste des couples, par programme)
- liste du dossier `plan-avant-entretien/` et de `code-formation/` (noms seulement)
