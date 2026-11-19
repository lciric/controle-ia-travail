# Vérification du critère d'identité v8 et du devis v8 du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v1

- Heure (`date -u`) au début de la vérification : 2026-11-19T12:48:08Z ; l'heure du scellement est celle du fichier compagnon.
- Vérificateur : le contre-lecteur des versions 4 à 7 (sous-agent, **Claude Opus 5.5**, `claude-opus-5-5`), d'un autre modèle que le
  rédacteur (Claude Fable 5.2). Il n'a écrit aucune des pièces vérifiées. Passe unique, demandée par la mère.
- Objet : branche `claude/brave-galileo-jhp684`, commit `5ad3666c`, lu par `git show`. Empreintes recalculées, égales à l'attendu et
  au compagnon : critère v8 `541bb86b15088c5cea5a291a294cccdd1067fe39be995b7f9014661f96cb3940` ; critère v7 `c8173979…` ; critère
  v6 `0700f3da…` ; devis v8 `0fa54bb4664ad7a91c61e26bb825c4634d4cc119d0d72ea48de0ce2c6ecf33fe` ; devis v7 `c1875462…` ; sortie du
  rejeu des essais `5cf86e2849969f502b30bc58394be2f705c50a5470bade79fbd7a056780e9fa9` (identique au commit `952fb75c`) ; programme de
  comparaison v4 inchangé (`4a0f3b2c…`). Ma vérification précédente est bien sur la branche principale (`e56e0a75…`, commit
  `53f7c0c2`).
- Fait : comparaison ligne à ligne v6 → v7 → v8 du critère et v7 → v8 du devis ; **contrôle par programme** du critère v8 contre la
  v7 et la v6 (seuils, libellés, tableau des autorisations, titres de paragraphe, blocs de règles) ; une sonde du programme v4 sur le
  cas de la sortie apparue pendant la comparaison ; les couples du devis v9 appliqués par programme au devis v8 et le résultat
  contrôlé. Tout est hors dépôt, dans le bloc-notes de la mère, dossier
  `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/opus-contre-lecture-critere-v4/v8/controle/` :
  `verif_v8_v1.py` (`eabb3391…`) et sa sortie `sortie-verif-v8-v1.txt` (`86e84a66…`) ; `sonde_course_sortie_v1.py` (`76bb9a86…`) et
  `sortie-sonde-course-v1.txt` (`4a15fc9b…`) ; `couples_devis_v9_v1.py`
  (`7e5d6e98a294c60ef316c28c16bbc2d994608c9818622e752d8dcc85ca7b8a3d`), ses sorties et les deux textes attendus du devis v9
  (`devis-v9-attendu-complet.md`, `3c667807206a3fad44efcc30cccd0d6ac1a1a626c993394b18c74ee76caa72f0` ; `devis-v9-attendu-minimal.md`,
  `20545c89…`). Non opposables tant que la mère ne les verse pas ; aucune pièce de `diag/` ni de `runs/` n'est lue.
- Non lu, selon le mandat : `docs/verdicts/`, tout fichier dont le nom commence par « verdict », `diag/`, `runs/`, `donnees/`, tout
  résultat de l'apprentissage des sondes sur la tâche ou des lentilles, tout fichier « consigne-privee » ou « conception-ii-b »,
  `brouillons/ii-b-saboteur-budget-v1/`. Aucune dépense, aucune machine, aucun commit, aucun fichier existant modifié. **Aucun refus
  d'outil.**

## Conclusion, par pièce

- **Critère d'identité v8 : scellable.** Contrôle par programme : aucun seuil, aucune tolérance, aucun libellé, aucune autorisation,
  aucun numéro de paragraphe ne change, ni contre la v7 ni contre la v6. Les différences sont exactement celles déclarées : le couple
  de ma passe précédente (v6 → v7), puis le bloc d'en-tête « Version 8 », les points (a) à (h) et leur table (v7 → v8). Les quatre écarts
  déclarés sont acceptés. Une erreur de renvoi est sans effet sur une règle : elle est dite en mineure 1 et ne demande pas de v9.
- **Devis v8 : scellable après ces couples exacts**, c'est-à-dire un devis v9. Il y a dix-sept couples (option complète, recommandée),
  et c'est le seul moyen d'atteindre ce que tu demandes : un devis qui ne nomme plus que le critère v8, hors son historique, et qui
  cite le rejeu scellé. Les trois endroits que la session a relevés ne suffisent pas : le corps nomme aussi le critère v5 à onze
  endroits, dont trois hors de la forme que couvre la règle de lecture du § 4. Je les avais laissés passer dans ma passe sur le devis
  v7. Une option minimale à quatre couples existe ; elle laisse le corps nommer le critère v5.
- **Rejeu des essais du programme v4 : tenu.** 311 essais passés, code de sortie 0, arbre propre, au commit `9b6a35c1`. Les empreintes
  du programme et des essais sont celles que le critère cite. La sortie est scellée.

## 1. Critère v8 : ce qui a changé, vérifié par programme

- **v6 → v7** : le titre, quatre lignes d'en-tête, une table au § 0.4, et le couple de ma passe `e56e0a75…`, porté à la lettre au § 4.
  Rien d'autre.
- **v7 → v8** : le titre, quatre lignes d'en-tête, la table « Différences de la v8 à la v7 », et les points (a) à (h). Ce sont neuf
  blocs de différence, tous déclarés. Dans le corps (§ 1 à § 10), les seules lignes changées sont celles de (a), (h), (g), (b), (c)
  et (d).
- **Contrôles tenus** (sortie `sortie-verif-v8-v1.txt`) :
  - mêmes seuils et mêmes comptes dans le corps (10⁻³ : 18 ; 10⁻⁹ : 3 ; 10⁻⁶ : 4 ; 0,10 : 5 ; repères 10⁻⁴, 10⁻⁵, 10⁻⁷, 10⁻⁸
    inchangés) ;
  - les cinq libellés aux mêmes occurrences ;
  - le tableau du § 5 identique à celui de la v7 et à celui de la v6 ;
  - les titres de paragraphe (`##` et `###`) identiques à ceux de la v7 et de la v6 ;
  - le paragraphe de la tolérance, les blocs « Les mentions » et « Préalables du programme », les § 5 et § 6 identiques à la v7.
- **Le point (h) est exact.** Le message du refus de démarrer est bien celui de la ligne 670 du programme (« … existe déjà : on
  n'écrase jamais (R12) », code 1). Pour la sortie apparue pendant la comparaison, la sonde donne une trace `FileExistsError`
  (« [Errno 17] File exists »), code 1, aucune sortie : ce cas relève bien du filet.
- Les points (e) et (f) sont exacts. Ma vérification de la v6 est sur la branche principale avec l'empreinte citée, et le rejeu est au
  commit `952fb75c` avec l'empreinte citée.

## 2. Les quatre écarts déclarés par la session

1. **« celle de son compagnon `.sha256` » : accepté.** Un fichier ne peut pas contenir sa propre empreinte : l'écrire changerait
   l'empreinte. Le compagnon est le moyen prévu par la règle R6. Le verdict cite l'empreinte recalculée sur le fichier, égale à celle
   du compagnon ; c'est ce que la phrase veut dire.
2. **L'ajout de (a) dans le gras du titre du cas : accepté, et c'est la bonne place.** Le défaut était justement que le titre, lu seul,
   couvrait encore les deux refus de démarrer.
3. **La puce « Version 7 — lecture de ce qui suit » gardée, corrigée par la puce « Version 8 » : accepté.** L'historique n'est pas
   récrit (R12). La correction est placée avant la puce qu'elle corrige, et elle dit exactement ce qui diffère de la v6 : le couple et
   les points (a) à (h).
4. **Le devis v8 nomme encore le critère v6 : à corriger, et pas seulement à ces trois endroits** (§ 4 ci-dessous, couples du devis
   v9).

## 3. Le rejeu des essais
Sortie `sortie-essais-programme-v4-20261119T124303Z-v1.txt`, lue en entier : début 12:43:03Z, fin 12:43:37Z, arbre `9b6a35c1`
propre pour `src` et `tests`, empreintes du programme (`4a0f3b2c…`) et des essais (`e1708b39…`) égales à celles que citent le critère
et le devis, commande écrite, « 311 passed in 32.55s », code de sortie 0. La réserve de ma passe précédente est levée : cette passe-là
tient lieu de la contre-lecture du programme v4 par un autre modèle, pour ce qu'elle a lu.

## 4. Devis v8 → devis v9 : couples exacts

**Constat** (relevé par programme sur le devis v8, lignes coupées comprises) :
- le critère v6 est nommé dans la tête (bloc « Version 7 »), au § 5, point 5 j (l. 297), et au § 5, point 6 (l. 306 et 309, avec
  « ligne non opposable ») ;
- le critère v5 est nommé onze fois dans le corps (§ 1 à § 8) :
  - huit sont des renvois « critère v5, § … », que la règle de lecture du § 4 couvre ;
  - trois sont hors de cette forme : « comparaison selon le critère d'identité v5 » (§ 2, l. 153) ; « contrôle K3 du critère v5 » (§ 5,
    point 5 g, l. 285) ; « Le critère v5 en garde la règle » (§ 7, décision 1, que Lazar lit, l. 343). Le devis reste juste, puisque
    le critère prime sur toute phrase du devis (§ 4), mais il n'est pas « propre » ;
- les mentions des § 0 et § 9 à 12 sont l'historique du devis : elles restent.

Chaque renvoi changé tombe sur le même objet dans le critère v8, dont les titres de paragraphe sont ceux de la v6, eux-mêmes ceux de
la v5. Je l'ai vérifié renvoi par renvoi :
- § 4, mention 1 et point 0 de la procédure ;
- § 5, tableau, seconde course incomplète, « Dans tous les cas » ;
- § 6, aucune relance ;
- § 7, K1 à K5 et K3 ;
- § 2, `versions`.

**Option complète (recommandée) : dix-sept couples.** Ils sont appliqués par programme au devis v8 (`couples_devis_v9_v1.py`) :
chaque « avant » s'y trouve une fois et une seule. Contrôles du résultat :
- aucune version du critère autre que la v8 n'est nommée hors de l'historique (tête, § 1 à § 8) ;
- « critère v6 » et « non opposable » ont disparu, et le rejeu est cité ;
- le § 3 est identique à la v8 ;
- les seuls nombres ajoutés au corps sont ceux de la citation du rejeu.

Le texte attendu est `devis-v9-attendu-complet.md` (`3c667807…`). Il porte trois champs à remplir entre crochets : [rédacteur],
[heure], [empreinte du rapport].

**Couple 1 — tête.** Avant : les lignes 1 à 32 du devis v8, du titre à « portés, le couple 7 tombe). » inclus (blocs « Version 8 » et
« Version 7 » ; empreinte du bloc, fin de ligne comprise : `2b47349f9d89c9aac20e0ecda4201144f5b8d98ab1b93f982f95ecc4c1deccb0`).
Après :
```
# Devis du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), pour les ranger et les faire entrer dans le programme — v9

**Version 9 — différences avec la v8.** Rédacteur de la v9 : [rédacteur]. Heure (`date -u`) : [heure]. Origine : la v8
(`devis-reajustement-lentilles-b-beta-v8.md`, `0fa54bb4664ad7a91c61e26bb825c4634d4cc119d0d72ea48de0ce2c6ecf33fe`), gardée octet pour octet hors
ce bloc et les couples de la vérification du critère v8 et du devis v8 par le contre-lecteur
(`docs/notes/neuron-lens-v1/verification-critere-v8-devis-v8-v1.md`, [empreinte du rapport]) ; elle reste archivée sans
modification, comme la v7 (`devis-reajustement-lentilles-b-beta-v7.md`,
`c187546226d61cf4cd8153a7d7b3add79e29eaa1a31a58daacd661f48b452451`) : leurs blocs de tête, retirés ici, disent leurs différences
avec la version qui les précède.
1. Titre : « v8 » devient « v9 » ; les blocs « Version 8 » et « Version 7 » sont remplacés par ce bloc.
2. Le critère d'identité nommé est sa version finale, la v8, et elle seule, hors l'historique du § 0 et des § 9 à 12 : les
   renvois des § 1 à 8 aux versions antérieures du critère deviennent des renvois au critère v8, aux mêmes paragraphes, le
   critère v8 gardant la numérotation de ses versions antérieures ; la règle de lecture du § 4 est récrite en conséquence ; la
   ligne « Statut » ne parle plus du marqueur d'une version antérieure de ce devis.
3. § 5, point 6 : les 311 essais du programme de comparaison v4 sont cités par leur rejeu scellé, et le critère qui le cite est
   la v8.

**Rien d'autre ne change** : aucun chiffre de durée, de prix ni de plafond, aucune variante, aucune recommandation, aucune
décision. Les lignes « Auteur », « Origine » et « Heure » ci-dessous sont celles de la v6 et décrivent son rédacteur. Le § 0
et le § 12 sont ceux de la v6 : là où ils disent la version finale du critère « à porter » ou le programme v4 « en cours
d'écriture », c'est fait (critère v8, § 0.1 : couples 1 à 6 portés, le couple 7 tombe).
```

**Couples 2 à 4 — les trois endroits relevés par la session.**
```
2 (§ 5, point 5 j)
AVANT : (préalables « K2 : … » du programme de comparaison, critère v6, § 4 ;
APRÈS : (préalables « K2 : … » du programme de comparaison, critère v8, § 4 ;

3 (§ 5, point 6, les essais)
AVANT : rejoués
   par le rédacteur du critère v6 : 311 passés, ligne non opposable ;
APRÈS : rejoués avant la création, sortie scellée
   (`docs/notes/neuron-lens-v1/devis-reajustement/banc-programme-v4/sortie-essais-programme-v4-20261119T124303Z-v1.txt`,
   `5cf86e2849969f502b30bc58394be2f705c50a5470bade79fbd7a056780e9fa9`, versée au commit `952fb75c` : arbre `9b6a35c1`,
   empreintes du programme et des essais égales à celles ci-dessus, « 311 passed », code de sortie 0) ;

4 (§ 5, point 6, le critère)
AVANT :    Le critère v6 la cite, elle seule,
APRÈS :    Le critère v8 la cite, elle seule,
```

**Couples 5 à 17 — la ligne « Statut », la règle de lecture du § 4 et les onze mentions du critère v5 dans le corps.**
```
5 (ligne « Statut »)
AVANT : **Le marqueur que portait la v6 est remplacé** (§ 4) par le chemin et l'empreinte de
  la version finale du critère d'identité, la v8
APRÈS : Le critère d'identité qui fait foi (§ 4) est sa **version finale, la v8**

6 (§ 1)
AVANT : avec audit**
  (critère v5, § 4).
APRÈS : avec audit**
  (critère v8, § 4).

7 (§ 2, variante A, comparaison)
AVANT : comparaison selon le critère d'identité v5 ;
APRÈS : comparaison selon le critère d'identité v8 ;

8 (§ 2, variante A, lecture)
AVANT : dans aucune lecture sans nœud de Lazar (critère v5, § 5).
APRÈS : dans aucune lecture sans nœud de Lazar (critère v8, § 5).

9 (§ 2, seconde course incomplète)
AVANT : traitée comme en variante A (critère v5, § 5).
APRÈS : traitée comme en variante A (critère v8, § 5).

10 (§ 3, aucune relance)
AVANT : mot de Lazar (critère
v5, § 6).
APRÈS : mot de Lazar (critère
v8, § 6).

11 (§ 4, règle de lecture)
AVANT : Les renvois « critère v5, § … » de ce devis gardent les numéros de paragraphe de la version 5
(`critere-identite-reajustement-lentilles-v5.md`, `50657b8929ab29ff5b09012b31cfe2a150f7815916b538acdba133f7042e24b6`) ; ils se lisent
comme la règle de même objet dans la version finale, qui prime en cas d'écart (hors le § 0, le point 6 du § 5 et les § 9 à 12, où
« critère v5 » nomme la version 5 elle-même).
APRÈS : Les mentions de versions antérieures du critère, au § 0 et aux § 9 à 12, sont l'historique de ce devis et nomment ces
versions elles-mêmes ; partout ailleurs, ce devis ne renvoie qu'à la version finale.

12 (§ 4, contrôles à la main)
AVANT : (critère v5, § 7, K1 à K5)
APRÈS : (critère v8, § 7, K1 à K5)

13 (§ 5, point 3, perte acceptée)
AVANT : « S non réajustée », critère v5, § 4)
APRÈS : « S non réajustée », critère v8, § 4)

14 (§ 5, point 5 g, matériel)
AVANT : contrôle K3 du critère v5)
APRÈS : contrôle K3 du critère v8)

15 (§ 5, point 5 g, versions)
AVANT : (critère v5, § 2 et § 4 : même
APRÈS : (critère v8, § 2 et § 4 : même

16 (§ 6)
AVANT : au lieu de rangement (critère v5, § 5).
APRÈS : au lieu de rangement (critère v8, § 5).

17 (§ 7, décision 1)
AVANT : Le critère v5 en garde la règle
APRÈS : Le critère v8 en garde la règle
```

**Option minimale, si tu ne veux que les trois endroits** : les couples 1 à 4, avec, au couple 1, ce point 2 au lieu du point 2
ci-dessus :
```
2. § 5, point 5 j : le renvoi devient un renvoi au critère v8, § 4. Les autres renvois du corps à une version antérieure du
   critère restent, lus par la règle du § 4 dans la version finale.
```
Le critère v6 disparaît alors et le rejeu est cité, mais le corps nomme encore le critère v5 à onze endroits, dont la décision 1
que Lazar lit. Le texte attendu est `devis-v9-attendu-minimal.md` (`20545c89…`). Je ne la recommande pas.

**Vérifier le devis v9 sans tout relire.** Remplacer les trois champs entre crochets du texte attendu par ceux du devis v9 ; les deux
textes doivent alors être égaux à l'octet, ou à l'espacement près si le rédacteur recoupe les lignes. Le script le montre en une
commande. Je peux faire cette vérification.

## Remarques mineures (sans effet sur le scellement)
1. **Critère v8, renvoi de ligne faux, deux fois** (« Version 8 — origine » et table (h)) : « programme v4, lignes 669-670 et 684 ».
   La création exclusive de la sortie, d'où vient la trace `FileExistsError`, est à la ligne **682** ; la ligne 684 est l'impression
   du résumé. La règle (h) elle-même est exacte (§ 1 ci-dessus). Si le critère est récrit pour une autre raison, y porter « 682 ».
2. **Critère v8, ligne (e)** : « le devis v8 le cite » reste vrai quand le devis v9 existera ; elle sera seulement incomplète. Pas de
   v9 du critère pour cela.

## Ce qui a servi (hors dépôt)
Le dossier `controle/` cité en tête : contrôle par programme du critère, sonde de la sortie apparue pendant la comparaison, couples du
devis v9, textes attendus dans les deux options, et les sorties de ces programmes, avec leurs empreintes. Le rapport et son compagnon
sont les seules écritures dans le dépôt.
