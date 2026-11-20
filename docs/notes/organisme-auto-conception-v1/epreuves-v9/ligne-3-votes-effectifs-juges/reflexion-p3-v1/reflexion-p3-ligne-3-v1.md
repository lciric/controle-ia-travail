# Réflexion de fond — faut-il changer la règle de la prédiction P3 de la ligne 3 pour pouvoir la trancher ? — v1

Pièce de travail (classe C). Rédacteur neuf, modèle F. Écrite le 2026-11-20 (temps universel, `date -u` : 08:27Z à la fin des calculs). Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/reflexion-p3-v1/mandat-reflexion-p3-fable-v1.md` (`e14a6614cd340ac0ef365473b949947e203098cd90e74e3d4d9573cf8c61aa2a`, vérifiée contre son compagnon avant tout autre geste).

**Je propose, je ne décide rien.** Changer la règle de P3 est un écart à un préenregistrement scellé : c'est ton nœud, Lazar.

**Aveugle tenu.** Je n'ai ouvert aucune mesure de l'étage 1 : ni le résultat, ni le verdict, ni sa contre-lecture, ni la lecture des prédictions, ni aucun fichier des dossiers `execution-etage-1-v1/` et `verdict-etage-1-v1/`. Je n'ai pas lancé le banc. De l'étage 1 je ne sais que ce que dit le mandat : verdict « non, pas à cette taille » ; P3 non lue.

## 0. Verdict

1. **Non : ne change pas la règle de P3.** Elle ne décide rien, et un calcul exact, sans tirage ni mesure, dit déjà ce que le banc pouvait répondre.
2. **La clause « blocs » de P3 ne pouvait pas être gagnée sur ce banc.** Avec les blocs {1, 2}, {3, 4}, {5} et des juges égaux et symétriques, la majorité stricte est la meilleure règle possible, à toute corrélation de la grille : aucun gain n'existe à prendre. Le gain prédit (0,02 à 0,06) est celui d'une autre forme de blocs, trois juges liés et deux libres (0,026 à 0,056), que le banc ne joue pas.
3. **Des graines neuves ne rendraient pas la lecture aveugle.** À 2 000 répliques, un écart moyen par cellule est fixé par les lois à quelques millièmes près (± 0,002 pour celui que je sais calculer) : un rejeu redonnerait ce que l'étage 1 contient déjà.

## 1. Ce que P3 veut dire, d'après les seuls textes d'avant mesure

P3 est à la ligne 135 du préenregistrement v7 (`4e3680d9…`). Elle est égale à l'octet de la version 1 (ligne 98) à la version 7 : même empreinte de ligne, `0072ce65…`, dans les sept versions (extraction par programme, `mentions-p3-textes-avant-mesure-v1.json`). Personne ne l'a discutée : ni la contre-lecture de la version 1 (aucune occurrence de « P3 »), ni les cinq vérifications des versions 2 à 6 (aucune occurrence de « P3 », « majorité fixe », « échangeable » ni « agrégation étalonnée »), ni l'additif 1 (`e1c1ee84…`), qui comble les silences A à J et deux autres, et pas celui-là. Le code (`09bfe0db…`) ne porte aucune lecture de P3 : ses critères mécaniques lisent la branche (2) de `fefca0bd94064`, non P3 (lignes 1521 à 1539 et 1610 à 1617).

Classes : (a) le texte tranche ; (b) plusieurs lectures restent admissibles ; (c) aucune lecture n'est écrite.

| trou | ce que disent les textes (fichier, ligne) | classe |
|---|---|---|
| 1. L'agrégation visée | **Pour le bras C** : à la ligne du bras C de l'étage 2, « collège, agrégation étalonnée du bras C de l'étage 1 » (v1 l. 209 ; v7 l. 279) ; « quatre comparaisons de l'agrégation étalonnée […] ; les bras F […] et P sont rapportés hors de la correction de Holm » (v7 l. 184 : le bras P y est distingué de « l'agrégation étalonnée ») ; « la règle que l'agrégation étalonnée doit choisir […] et celle que le bras C choisit en population » (v7 l. 237) ; le code, écrit avant tout tirage, prend C pour pivot de toutes ses comparaisons (l. 807). **Pour « C ou P »** : H-agrégation dit « une agrégation étalonnée sur les erreurs » (v7 l. 122) ; « les bras C et P […] choisissent […] sur l'étalonnage » (v7 l. 107) ; le bras à cinq juges rend « ce qu'une agrégation étalonnée y gagne ou y perd » (v7 l. 222). | **(b)**, lecture dominante : bras C |
| 2. « Majorité fixe » | Quand P3 est écrite, le bras F vaut : « au moins un » ; « à cinq juges, aussi la majorité stricte » (v1 l. 166) et « poids égaux » n'existe pas (aucune occurrence en v1). « Poids égaux » entre en version 2, nommé pour autre chose : « la référence « poids uniformes » de la branche (2) de `fefca0bd94064` et l'« agrégation uniforme » de `fa38f9faa24e0` », avec « même règle de seuil que C », donc un seuil estimé, non fixe (v2 l. 191 ; v7 l. 216). P4 emploie les mêmes mots à la ligne suivante (v7 l. 136) et le code la lit contre `F_majorite_stricte` (l. 809-810). | **(a)** : la majorité stricte du bras F |
| 3. « Échangeables » | Trois occurrences par version, aucune définition. **Lecture large, la lettre** : H-agrégation oppose « échangeables » à « inégaux ou corrélés par blocs » (v7 l. 122) ; sont alors échangeables toutes les cellules de la loi 1 à taux égaux entre juges, profils « sévère » et « indulgent » compris (42 cellules) ; c'est aussi le sens ordinaire du mot. **Lecture étroite, l'intention probable** : au § 0, écrit pour deux juges, le texte réserve son « cas d'école » aux juges « égaux et symétriques » et dit qu'avec des « erreurs dissymétriques » une agrégation étalonnée « peut gagner » (v1 l. 70 ; repris en v7 l. 105 : « ou avec des juges inégaux ou dissymétriques ») ; « au mieux jeu égal » ne vaudrait alors que pour les quatre profils égaux (28 cellules). Le même trou vaut pour « juges en blocs » : 12 cellules (profils égaux, ρ ≥ 0,6) ou 18. | **(b)**, et c'est le trou qui décide |
| 4. La statistique (hors mandat) | « Gain de 0,02 ou plus » : dans une cellule, dans toutes, en moyenne, avec ou sans intervalle, à quelle taille d'étalonnage ? « Aucun gain » : nul ou négatif, ou sous 0,02 ? « Jeu égal » : aucune marge ; la seule équivalence du texte (± 0,05, v7 l. 180) est plus large que les effets prédits. La marge descriptive de l'étage 1 (0,05 et borne basse au-dessus de 0, v7 l. 178) contredit les seuils propres de P3 (0,02). | **(c)** |

**Conclusion.** P3 n'est pas lisible telle quelle ; on ne s'est pas trop retenu. Seul le trou 2 est tranché. Il pèse d'ailleurs peu : sur les profils égaux, la majorité stricte et « poids égaux » diffèrent d'au plus 0,0071 à 25 témoins d'étalonnage, 0,0022 à 50, 0,0003 à 100 (calcul exact, point 3).

## 2. Ce que P3 apporte au programme

Rien qui décide.

- **La taille de l'étage 2 : non.** Elle suit la seule règle de l'estimateur (v7 l. 233 et l. 313 à 315).
- **La composition des juges : non.** « Le verdict d'un juge, seul ou agrégé, corrigé ou non, […] ne décide ni de la composition de l'organisme ni de ce qui va à l'épreuve » (v7 l. 47) ; « changer d'agrégation descriptive ou changer de juges sont des décisions de Lazar » (v7 l. 345) ; « aucun de ces bras ne porte le « oui » de la ligne » (v7 l. 318) ; le bras à cinq juges « ne dit rien d'un collège réel » (réserve 9, v7 l. 400) et ne plante aucune propriété des lignées (v7 l. 222).
- **Une revendication : non.** « Ce texte ne porte aucune revendication neuve » (v7 l. 43) ; H-agrégation est une hypothèse de travail propre à l'épreuve (v7 l. 117 à 122).
- **Ce qu'elle pourrait nourrir** : la note de conception du juge (un juge par lignée ; GO-2026-11-19-65 et -68, cités v7 l. 14). Ce dont cette note a besoin est donné par le calcul du point 3 et par la branche (2) de `fefca0bd94064`, qui, elle, a une règle gelée (v7 l. 321) et que le code lit.

## 3. Ce que la théorie dit d'avance — calcul exact, sans tirage

`calcul_exact_p3_ligne_3_v1.py` (`2bc8c492…`), sortie `calcul-exact-p3-ligne-3-v1.json` (`d4c4c90f…`), table lisible `table-calcul-exact-p3-ligne-3-v1.md` (`1b00bbaf…`). Bibliothèque standard seule ; aucun tirage, aucun fichier lu ; fractions exactes pour les 32 configurations de votes, les règles fixes et les règles à étalonnage infini ; convolution en double précision pour l'étalonnage fini. Joué deux fois, sorties égales à l'octet. Six gardes, dont un artefact (règle codée à l'envers), une valeur connue (0,05792 pour la majorité de cinq juges indépendants au taux 0,2) et deux formules du texte (ρ moyenne plantée égale à ρ sous la loi 1 et à 7ρ/15 sous la loi 4, v7 l. 161). Les 91 cellules du banc à cinq juges y sont (loi 1 : sept profils ; loi 4 : six ; sept valeurs de ρ).

« Gain » veut dire partout : erreur équilibrée de la majorité stricte moins celle de la règle.

**(i) Juges égaux et symétriques : la majorité stricte est la meilleure règle qui existe.** Dans les 56 cellules à profil égal (loi 1 et loi 4, toutes les valeurs de ρ), l'erreur équilibrée de la majorité stricte égale, à la fraction près, celle de la meilleure fonction des cinq votes. Raison, sous la loi 4 : deux juges d'un même bloc qui s'accordent pèsent toujours au moins autant qu'un juge seul, tant que le taux d'erreur est sous 0,5. Or une règle gelée sur l'étalonnage et lue sur une moitié indépendante a pour erreur moyenne celle de la règle choisie. **Aucune agrégation, étalonnée ou non, C ou P, à aucune taille d'étalonnage, ne peut donc y avoir un gain moyen positif.** À étalonnage infini, le bras C y rend exactement la majorité stricte ; le bras P fait un peu moins bien dans les blocs à ρ ≥ 0,6 (perte de 0,0001 à 0,0071).

**(ii) Blocs : le gain tient à la forme des blocs, et le banc a pris une forme sans gain.** Complément `calcul_exact_p3_structure_des_blocs_v1.py` (`6d373522…`), sortie `calcul-exact-p3-structure-des-blocs-v1.json` (`58b64491…`), joué deux fois lui aussi : même construction que la loi 4, autres partitions des cinq juges, hors du banc, profils égaux.

| partition des cinq juges | gain maximal de toute règle, ρ ≥ 0,6, taux 0,1 à 0,3 | bras C à étalonnage infini |
|---|---|---|
| 2 + 2 + 1 (la loi 4 du banc) | 0 | égal à la majorité |
| 3 + 1 + 1 | 0,026 à 0,056 | prend tout le gain |
| 2 + 1 + 1 + 1 ; 3 + 2 | 0 | égal à la majorité |
| 4 + 1 | 0 | **perd** 0,003 à 0,028 |

La prédiction chiffrée de P3 (0,02 à 0,06) est donc juste pour trois juges liés et deux libres, et fausse pour le banc. Avec les profils « sévère » et « indulgent », la loi 4 laisse un gain possible de 0,0065 à 0,0192 à ρ ≥ 0,6, jamais 0,02 ; il vient du seuil, non des blocs (point (iii)).

**(iii) Profils « sévère » et « indulgent » : tout tient à une égalité au seuil.** La meilleure règle n'y est plus la majorité mais « au moins deux » (sévère) ou « au moins quatre » (indulgent) : gain possible de 0,0297 à ρ = 0, 0,0208 à ρ = 0,30, 0,0030 à ρ = 0,90 (loi 1). Mais le « seuil au milieu des deux moyennes de classe », commun aux bras C, P et « poids égaux », tombe exactement sur un nombre entier de votes (2 ou 3) dans les 14 cellules de la loi 1 et les 6 de la loi 4 à ρ ≥ 0,6. Le bras « poids égaux » joue alors le bon quota une fois sur deux environ (probabilité 0,49 à 0,50 à 25 témoins d'étalonnage), et plus de témoins n'y changent rien : gain sur la majorité stricte de 0,0014 à 0,0148 à 25 témoins, de 0,0015 à 0,0153 à 200, jamais 0,02 (loi 1). C'est une propriété de la convention d'égalité du banc et du choix 0,30 / 0,10 à cinq juges, non un fait sur l'agrégation.

**(iv) Ce que deviennent les deux clauses de réfutation selon la lecture.**

| clause | lecture | ce que le calcul dit d'avance |
|---|---|---|
| « gain de 0,02 ou plus avec des juges échangeables » | cellules étroites, référence majorité stricte | gain moyen ≤ 0 : la clause ne peut être atteinte que par une faute du banc |
| | cellules étroites ou larges, référence « poids égaux » | gain de toute règle ≤ 0,0071 (étroites), ≤ 0,0158 (larges) : jamais atteinte |
| | cellules larges, référence majorité stricte | ouverte dans 6 cellules (sévère, indulgent, ρ ≤ 0,30) ; se joue sur l'égalité au seuil ; non calculée pour C et P |
| « aucun gain en blocs à 200 témoins » | blocs à profils égaux (12 cellules) | atteinte par construction : aucun gain n'existe |
| | avec « sévère » et « indulgent » (18 cellules) | dépend du sens de « aucun gain » : gain possible, sous 0,02 |

Le reste de P3, « moins bien de 0,01 à 0,04 à 25 témoins », n'est pas calculable exactement (voir « Non calculé »). C'est, à 0,0071 près sur les profils égaux, la grandeur de la branche (2) : bras C contre « poids égaux », par taille d'étalonnage, sous une règle gelée.

**(v) Juges inégaux (hors de P3, pour H-agrégation).** Profil inégal, loi 1 : gain possible de 0,005 à 0,087 ; bras C à étalonnage infini, de −0,002 à 0,085. C'est là qu'une pondération paie.

**(vi) Précision à 2 000 répliques.** Pour l'écart apparié « poids égaux » moins majorité stricte, la demi-largeur à 95 % de la moyenne par cellule est d'au plus 0,0014 (profils égaux) et 0,0020 (dissymétriques) à 25 témoins d'étalonnage. Pour les bras C et P, je l'estime du même ordre, sans calcul.

**Non calculé.** La perte des bras C et P à étalonnage fini : la loi de leurs poids estimés porte sur des tirages à 32 cases par classe, hors d'atteinte d'une énumération. La borne du (i) vaut pourtant à toute taille.

**Pistes de littérature, non vérifiées (règle R7), aucun chiffre repris** : Condorcet (1785) ; Nitzan et Paroush (1982) ; Shapley et Grofman (1984) ; Ladha (1992) ; Dawid et Skene (1979). Les résultats ci-dessus ne s'appuient pas sur elles : ils sortent du seul calcul.

## 4. Les options

| option | avantage | inconvénient |
|---|---|---|
| **(A) Ne rien changer** : P3 « non lue », avec sa raison | aucun écart au texte scellé ; aucun coût ; règles R1 et R3 intactes | une prédiction sans mot ; le défaut de conception de la loi 4 reste tu |
| **(B) Lecture multiple déclarée** : les huit lectures de chaque clause (C ou P ; majorité stricte ou « poids égaux » ; cellules étroites ou larges), par taille d'étalonnage, tirées par programme de la sortie existante, sans mot | montre tout, ne choisit rien ; la liste est fixée ici, à l'aveugle | lecture ajoutée après mesure, à nommer telle ; « P contre majorité stricte » n'a pas d'intervalle dans la sortie (pour le bras P, le code n'en rend que contre C et contre « poids égaux », l. 807 à 812) ; la sortie ne garde que des moyennes par cellule, rien par réplique (l. 765 à 779) ; huit lectures invitent à en préférer une |
| **(C) Règle neuve, scellée, sur graines neuves** | un mot sous une règle propre | voir ci-dessous : quatre raisons |
| **(D) Trancher par le calcul, sans mot du banc** (la mienne) : (A), plus une note de théorie scellée, refaite par une autre lignée | dit plus que le banc ne pouvait dire ; ne touche pas au texte scellé ; donne un contrôle gratuit du banc (point 5) | ce n'est pas un mot sur P3 ; vaut pour les lois que nous avons choisies (réserve 1 du texte) |

**Pourquoi pas (C).**
1. **Elle n'est aveugle qu'en apparence.** Les écarts moyens par cellule sont fixés par les lois à quelques millièmes près (point (vi)) : des graines neuves redonnent les nombres de l'étage 1. Quiconque a vu l'étage 1 sait ce que la règle neuve rendra ; la décision de l'adopter ne peut plus être aveugle.
2. **Le calcul en fixe déjà l'issue**, lecture par lecture (table du (iv)). Choisir la lecture, c'est choisir le mot. Un tirage dont l'issue est connue par construction n'est pas une épreuve (règle R3, dans son esprit).
3. **Le banc ne peut rendre qu'un mot sur la clause « blocs ».** Le texte lui-même écrit qu'« une épreuve qui ne peut rendre qu'un mot contre une carte ne porte pas de mot (règle R4) » (v7 l. 224).
4. **Le coût** : préenregistrement neuf, contre-lecture, code neuf (le code v3 refuse toute racine hors du texte, l. 154-155), contre-lecture du code, additif, exécution, verdict par un agent neuf. Pour un résultat qui ne décide rien, et un précédent : récrire après coup la règle d'une prédiction scellée.

**Si tu voulais (C) malgré tout**, voici la règle que j'écrirais, à prendre ou à laisser en bloc. Agrégation : bras C (bras P rapporté, sans mot). Référence : la majorité stricte (« poids égaux » rapporté à côté). Échangeables : loi 1, quatre profils égaux, sept valeurs de ρ ; « sévère » et « indulgent » rapportés à part, sans mot, pour cause d'égalité au seuil. Blocs : loi 4, quatre profils égaux, ρ ≥ 0,6. Statistique : écart apparié par réplique, sur les mêmes tirages, moyenne sur 2 000 répliques, par cellule, aux tailles d'étalonnage 25, 100 et 200. « Jeu égal » : deux tests unilatéraux, marge 0,01. Gain « établi » : test unilatéral rejeté et gain observé de 0,02 au moins. Multiplicité : Holm sur les 84 tests des cellules échangeables et les 12 des blocs. Puissance du « jeu égal », calculée d'avance pour le seul bras où elle est exacte (« poids égaux » contre majorité stricte, niveau 0,05 / 84, la plus basse des 28 cellules échangeables) : 0,87 à 25 témoins, 1,00 à 100 et à 200 ; pour le bras C elle demande un écart type par réplique que je n'ai pas. Graines : racines neuves (par exemple 2026112001 et 2026112002), `SeedSequence(racine, spawn_key=(clé,))`, scellées avant tout lancement, jamais 2026111932 ni 2026111933.

## 5. Ce qui permettrait de vérifier hors de nous

- **Refaire le calcul par une autre lignée, à partir du seul texte** (lois 1 et 4, v7 l. 203 à 206 ; bras, l. 212 à 220). Six nombres à retrouver : 0,05792 ; majorité stricte égale à la règle de Bayes dans 56 cellules sur 56 ; 0,0297 ; 0,0192 ; 0,026 et 0,056 pour la partition 3 + 1 + 1.
- **Comparer le banc au résultat exact, sans rien choisir.** La sortie donne, pour chaque cellule et chaque taille, l'erreur équilibrée exacte des bras sans étalonnage (majorité stricte, unanimité, « au moins un », juge seul) et de « poids égaux », avec l'erreur type sur 2 000 répliques. Une personne qui a le droit d'ouvrir l'étage 1 compare : au-delà de trois ou quatre erreurs types, c'est une faute du banc ou du calcul. Ce contrôle ne lit aucune prédiction.
- **Pour (C) seulement** : graines neuves scellées avant tout lancement ; réimplémentation du banc par une autre lignée.
- **Ce qui reste invérifiable sur un banc scripté** : que des juges réels soient échangeables, symétriques, ou liés par blocs, et selon quelle partition. Les juges réels ne sont lus qu'à l'étage 2, à deux juges, où une agrégation pondérée n'est qu'une règle fixe parmi cinq (v7 l. 107) : P3 n'y a aucun pendant.

## 6. Recommandation

- **Décision, en une phrase.** Garder P3 « non lue » sur le banc, sans changer sa règle, et joindre une note de théorie qui dit ce que le calcul exact tranche.
- **Enjeu.** Aucun pour la suite de la ligne : P3 ne règle ni la taille de l'étage 2, ni les juges, ni une revendication. L'enjeu est de méthode : ne pas récrire après coup une règle scellée, et ne pas laisser croire qu'un banc a éprouvé ce qu'il ne pouvait pas montrer.
- **Options.** (A) ne rien changer ; (B) lecture multiple, sans mot ; (C) règle neuve sur graines neuves ; (D) (A) plus la note de théorie, refaite par une autre lignée.
- **Recommandation.** (D). (B) seulement si tu veux voir les nombres côte à côte, et alors sans mot. Pas (C). **Confiance : 0,8** sur « ne pas changer la règle » ; 0,9 sur le calcul, sous réserve qu'une autre lignée le refasse.
- **Défaut sous 48 heures.** (A), qui est l'état actuel, avec la note de théorie versée comme pièce descriptive. **(B) et (C) sont sans défaut** : lecture ajoutée après mesure ou écart au texte scellé, donc nœud.
- **Deux suites que je te rends, sans les décider.** (1) Si l'agrégation pondérée compte pour le collège d'un juge par lignée, elle s'éprouve dans la note de conception du juge, avec une forme de blocs qui peut rendre les deux mots (3 + 1 + 1 à côté de 2 + 2 + 1) et des juges inégaux : une épreuve neuve, non une relecture. (2) Pour le gabarit : chaque prédiction nomme son bras, sa référence, ses cellules, sa statistique et son seuil, et le contre-lecteur vérifie que le code porte une fonction pour chacune ; ici les critères mécaniques n'en avaient aucune pour P3, et personne ne l'a vu en six relectures.

## 7. Écarts, limites, pièces

**Écarts au mandat, tous déclarés.**
1. **L'additif 2 (`f5562d20…`) n'a pas été trouvé ni lu.** Le mandat ne donne pas son nom de fichier. Trois noms essayés par `git show` sur main, sans succès ; sept recherches étroites dans `registres/etat.md`, `registres/decisions.md` et `registres/go.md`, écrites pour ne rendre qu'un nom de fichier, sans rien trouver ni rien afficher d'autre. Aucune commande de liste. Si c'est l'additif de code que le texte prévoit, il « ne change aucune règle de ce texte » (v7 l. 7) ; s'il parlait de P3, le point 1 serait à relire.
2. **Le code du banc et les versions 1 à 6, avec leurs contre-lectures, ne sont pas sur main** aux chemins donnés (« exists on disk, but not in origin/main »). Pris sur disque ; chaque empreinte est égale à celle que citent le mandat ou la version 7. Le préenregistrement v7 et l'additif 1 viennent de main (`git fetch`, tête `04a5ce7d6`, puis `git show` redirigé).
3. **Lus en entier** : versions 1 et 7, contre-lecture de la version 1, additif 1, mandat. **Lus par extraction** : versions 2 à 6 (ligne de P3 et dix termes ; comptes égaux de la version 4 à la version 7) et les cinq vérifications (aucune occurrence des dix termes). **Du code** : les lignes 1 à 1037 et 1380 à 1679 ; le double rendu, la garde de cadrage et l'alarme non lus.
4. **Routine de reprise (règle R14) non jouée** : lire l'état vivant et la dernière passation m'aurait exposé aux mesures de l'étage 1.
5. Python lancé sans option, à la lettre de l'en-tête du mandat.
6. Cinq `git show` ont échoué (chemin absent de main) en laissant chacun un fichier vide dans mon dossier ; deux ont été remplacés par la copie du disque, les trois autres supprimés.

Aucune écriture dans le dépôt, aucun commit, aucun appel de modèle, aucune dépense, aucune recherche sur la toile, aucun refus d'outil.

**Limites.** Les résultats valent pour les lois du banc, choisies par nous. « À étalonnage infini » suppose des classes égales. Le calcul n'a été refait par personne : c'est la première chose à faire avant de s'en servir.

**Pièces rendues** (dossier `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/reflexion-p3-ligne-3-v1/`, chacune avec son compagnon `.sha256`).

| pièce | sha256 |
|---|---|
| `calcul_exact_p3_ligne_3_v1.py` | `2bc8c4922a0727acde1f2323f36c04f5bfe6d46befd95d3a21e9ba600fcfcb2a` |
| `calcul-exact-p3-ligne-3-v1.json` | `d4c4c90f2a82ba3902d0c0c10347e734d5e17ad867867a9737713857dce2591a` |
| `calcul_exact_p3_structure_des_blocs_v1.py` | `6d37352237bbeab023ce538ec7cc33147063c94b1883b27dbaca25827f7553c6` |
| `calcul-exact-p3-structure-des-blocs-v1.json` | `58b64491e3532c38931c02c70c9e0d24bbd161f3ff3d176ede0347a8e16e915e` |
| `tableau_calcul_exact_p3_v1.py` | `1f6fc28ccbc5b0ea0329d9347c4e7fe6efbe3a48cd7ce43b345a1ae00c56f4b2` |
| `table-calcul-exact-p3-ligne-3-v1.md` | `1b00bbafbb4e119e61776929a5082d8e01de0f018dc60da82840c332562e4c9a` |
| `extraire_mentions_p3_v1.py` | `5600993d5c6c1e96d3576d52df7ca185647fc2030dd52e08c25ff362123f105b` |
| `mentions-p3-textes-avant-mesure-v1.json` | `a57d44fbd913c321dcbe983dabefacd6ab1a975e2a84286d1112f3636d190cc3` |

**Pièces lues, empreintes recalculées.**

| pièce | sha256 | d'où |
|---|---|---|
| préenregistrement, version 7 | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | main |
| additif 1, version 2 | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` | main |
| `banc_juges_scriptes_ligne_3_v3.py` | `09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0` | disque |
| préenregistrement, versions 1 à 6 | `928b9db3…`, `7519cf5c…`, `9b62fd5a…`, `26bb2214…`, `915fbe4b…`, `b040d24c…` | disque |
| contre-lecture de la version 1 | `32e446c7a38915d48c57e44f558fcd5d806c9b9581457734fc62414694b0e7ba` | disque |
| vérifications des versions 2 à 6 | `5b3dc137…`, `6e2b540f…`, `597b97bb…`, `9031205f…`, `cbaf44de…` | disque |

Les empreintes abrégées sont entières dans `mentions-p3-textes-avant-mesure-v1.json`.

Rédacteur neuf, modèle F.
