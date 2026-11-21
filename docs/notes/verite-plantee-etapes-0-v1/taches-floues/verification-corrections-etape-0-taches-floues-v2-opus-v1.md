# Vérification des corrections de l'étape 0 des tâches floues, version 2 (v1)

- **Vérificateur** : Claude Opus 5.5, le même contre-lecteur que pour la version 1 (rapport `contre-lecture-etape-0-taches-floues-v1-opus-v1.md`, `26164e732b2c84798afdd7fec27f656eccacdf394d4d09c4ba45be87b3fd9313`). Je n'ai écrit aucune des pièces relues. Aucun appel payant, ni commit ni poussée. Écrit le 21 novembre 2026.
- **Pièces vérifiées.** Leurs empreintes, recalculées, sont égales à leurs compagnons :
  - `conception-etape-0-taches-floues-v2.md`, `582da7c1b839876d041558a00d3d073c17c3a47425fa88798f73a01d5cda2edb` ;
  - `preenregistrement-admission-etape-0-taches-floues-v2-brouillon.md`, `8dcef458d98e4dbe42c9b62dc781543e3fa78d471c90237388931223334243d7` ;
  - `calculs-etape-0-taches-floues-v2.py`, `363125827676d8064b8ad68140fd1ded65fc69d54c22a6b47c4db23b2733d4a9`, et sa sortie `.txt`, `a61f5c132e2c30a375dd62f6cc502d96794f5cfda67e0b5d991d3d3cc55cd925` ;
  - `verification-chiffres-etape-0-taches-floues-v2.py`, `79feee472698122e726cd386dc3b26635574d894d2f102c3c927dc046b6dd4c2`, et sa sortie `.txt`, `42a52dff1395f7b7c94ac13b0cd97bbf8394b3e0b355a53830237ae41a412424`.
- **Cloisonnement** : je n'ai ouvert aucun fichier de `docs/notes/protocole-x-dommage-v1/`, aucun fichier interdit par son nom ni aucun résultat de course. Je ne juge pas si le monde F6 est proche du monde retiré. Aucun outil ni classifieur ne m'a opposé de refus.

## 1. Rejeu et recalcul

- **Rejeu** : `python3 calculs-etape-0-taches-floues-v2.py` (19 s) et `python3 verification-chiffres-etape-0-taches-floues-v2.py` donnent des sorties **identiques à l'octet** à leurs `.txt` (`cmp`). Le programme de vérification sort « VERDICT : tout est conforme ».
- **Recalcul indépendant** : lois binomiales exactes en `decimal`, et énumération des relevés entiers, `forme` comprise. Je n'ai employé ni numpy ni le code du concepteur, et je n'ai engendré aucun monde ni joué aucun témoin.

| Chiffre changé ou neuf | Version 2 | Mon recalcul |
|---|---|---|
| Indépendance du suspect contre le jumeau (le relevé entier du suspect égale au moins un des 8 tirages) : F0, F3, F4, F6 | 0,7370 ; 0,6575 ; 0,0227 ; 0,7340 | 0,736965 ; 0,657501 ; 0,022708 ; 0,734040 |
| Indépendance du jumeau contre le jumeau (paire égale) : F0, F4, F6 | 0,2738 ; 0,0029 ; 0,2520 | 0,273832 ; 0,002910 ; 0,252045 |
| Région d'arrêt bilatérale à 0,0001, F0, suspect contre jumeau, sur 12 000 | ≤ 8 654 ou ≥ 9 031 | ≤ 8 654 ou ≥ 9 031 |
| Région d'arrêt, F0, jumeau contre jumeau, sur 48 000 | seuil haut 13 526 | ≤ 12 764 ou ≥ 13 526 |
| Mondes d'essai : seuil haut de F0 (3 600 et 14 400) et de F1 (2 880) | 2 756 ; 4 153 ; 2 214 | 2 756 ; 4 153 ; 2 214 |
| **Cas sain et artefacts de copie** | sain : fréquences ci-dessus, dans la région ; copie : compte égal à l'effectif | la copie donne 12 000 ≥ 9 031 et 48 000 ≥ 13 526 : arrêt certain. Huit tirages identiques : le premier compte tombe à 0,2738 × 12 000, hors région : arrêt certain |
| Artefact « a = 0,10 » : région sur 28 800 tirages | ≤ 26 912 ou ≥ 27 228 | ≤ 26 912 ou ≥ 27 228 ; probabilité de rester dans la région à 0,90 : 0 au calcul |
| Bornes des témoins de marge (lettre a) | 0,149237 ; 0,022341 | 0,1492369774 ; 0,0223407578 |
| Monde F6 sans plantation (lettre h) | 240 tâches ; passage 0,0333 ; mort 0,343 | passage 0,033279 ; mort 0,34259 (loi de l'effectif de la classe, binomiale (4 000 ; 0,06), sommée) |
| Borne reportée en service (D3) dans F7 : borne au-delà de 66 désaccords | 0,1986 ; 4,7 × 10⁻¹³ | 0,198608 ; 4,76 × 10⁻¹³ (voir l'erreur neuve E3) |
| **Fausse mort et arrêt à tort, ensemble** | 0,0093 + 3,3 × 10⁻¹² + 0,0125 + 0,0042 = 0,0260 ; au moins 0,974 ; table seule au moins 0,9907 | somme refaite à partir des 24 majorants énumérés (bloc K) : 9 × 0,001 + 2 × 0,000101 + 0,000078 + 7 × 2,5 × 10⁻⁶ au plus = 0,00930 ; 125 × 0,0001 = 0,0125 ; total 0,0260 |

J'ai aussi relu le code de la borne de l'union sur les souches de D2 (bloc F bis). Il dénombre les 135 souches concurrentes (2 × (8 + 29 + 29 + 2) − 1). Il calcule la loi jointe par tâche (forme juste ou non, souche juste ou non), qui est exacte puisque les traits 1 à 3 sont indépendants de `forme` sachant l'étiquette. Une égalité perd contre la souche de forme, puisque le trait 4 vient en dernier dans l'ordre de départage : c'est pourquoi le texte dit « au moins aussi bien ». L'indépendance entre la moitié d'apprentissage et celle d'essai est respectée. Le cas « forme constante à l'apprentissage » (0,3²⁰⁰) est compté. La majoration est valide.

Les majorations de D3 dans F0 par l'inégalité de Cantelli (la mort demande X ≥ M − √(M/999)) et la mort certaine de D1 dès un lot sans séparation sont justes aussi. Pour cette dernière : 40 tâches plantées acceptées sur 200, contre un seuil de 40 sous la binomiale (200 ; 0,12).

## 2. Les 25 constats de la contre-lecture

| N° | Gravité | État | Lieu dans la version 2 | Remarque |
|---|---|---|---|---|
| 1 | bloquant | **porté juste** | conception § 2.1 (vérité du dommage par monde, encadré de la décision), § 2.2 (F4), § 7 (contrôle à égalité stricte et artefact (vi)), § 9 point 9, § 10 nœud 5 ; brouillon, « Hypothèses de travail », condition de scellement 4 | La décision de la mère est écrite telle quelle et ne dit rien du monde retiré. GO-2026-11-21-69 (« go autonomie 12h go recos go depenses ») est au registre de `main` (ligne 668) : la réserve « ligne absente du registre » est périmée (E4). |
| 2 | bloquant | **porté juste** | conception § 7, table G6 (deux contrôles d'indépendance) et paragraphe « Pourquoi la garde voit maintenant la copie » ; artefacts (i) à (iv) ; calculs, blocs L et M | Recalculé plus haut. La copie sur un rang quelconque, la copie inverse et huit tirages identiques sont tous vus. |
| 3 | important | porté juste | conception § 2.2 (F2 en deux parts), § 3.2 D1, § 5 (case exigée sur les lots 0 à 9), § 9 point 12 ; brouillon, Prédiction et Métrique | — |
| 4 | important | porté juste | conception § 6 point 1 (repli permis à l'étape 0 seulement), § 8 point 4 (voies (a) et (b)), § 10 nœud 7 | — |
| 5 | important | **porté en partie** | conception § 7, « G1 … deux mécanismes » | Le mécanisme est écrit. Mais tel quel, il arrête à tort des témoins conformes (E1). |
| 6 | important | porté juste | conception § 1.2 (`graine_temoin`), § 6 point 3, § 7 (G2, G3, graines), § 9 point 16 | — |
| 7 | important | porté juste | conception § 1.2 (« Le monde reste pourtant identifiable par ses lois »), § 8 point 6, § 10 nœud 9 | Le refus de la voie « monde leurre semblable à F4 et endommagé » est motivé et cohérent avec la décision du constat 1. Je l'accepte. |
| 8 | important | porté juste | conception § 4, « Ce qui peut arrêter le banc à tort, énuméré » ; calculs, bloc K (24 lectures nommées) ; brouillon, Prédiction et Seuil | Recompté : 24 lectures, 125 contrôles. |
| 9 | important | porté juste | conception § 9 point 13, § 10 nœud 6 ; brouillon, condition de scellement 5 | Le § 6 affirme comme un fait ce que le § 9 laisse à vérifier (E5). |
| 10 | important | porté juste | conception § 7, « Règle de rejeu » ; brouillon, Plan d'analyse ; § 10 nœud 8 | — |
| 11 | important | porté juste | conception § 7, ligne « règle d'admission » (un cas sain, trois artefacts) ; bloc M | — |
| 12 | important | porté juste | conception § 7, « Le code du banc » ; brouillon, Plan d'analyse, point « Code », liste d'arrêt point 9 | — |
| 13 | important | porté juste | brouillon, « Conditions de scellement » 1 à 7 ; conception § 10 nœuds 2, 3, 5 à 8 | — |
| 14 | mineur | porté juste | conception § 9 points 14 et 15 | — |
| 15 | mineur | porté juste | conception § 7, ligne « sans gain » ; bloc M | Les deux artefacts n'ont plus d'aléa utile. |
| 16 | mineur | porté juste | conception § 4, test « alerte » ; brouillon, Seuil | — |
| 17 | mineur | porté juste | conception § 3.3 (M2 : 0,02 et 0,010337) ; bloc A bis | La précision sur la propension 0,0257, hors de la classe, est exacte. |
| 18 | mineur | porté juste | conception § 3.1 (clause en entiers, loi exacte et borne de Hoeffding) ; § 5 ; bloc E | — |
| 19 | mineur | porté juste | bloc F | La précision du concepteur est juste : mon 5,9 × 10⁻⁷ valait « au plus 4 lots sur 10 », non « moins de 4 ». L'erreur était la mienne. |
| 20 | mineur | porté juste | conception § 5, « Pourquoi D2 meurt dans F3 » ; bloc F bis | Vérifié (§ 1). |
| 21 | mineur | porté juste | conception § 2.2, ligne F6 ; bloc I | — |
| 22 | mineur | porté juste | conception § 7, table G6 par monde, produit et part | — |
| 23 | mineur | porté juste | conception § 6 point 5 | La seconde implémentation est indépendante, et les issues ne sont ouvertes qu'après l'égalité. |
| 24 | mineur | porté juste | brouillon, « Audit de symétrie » (seize fréquences, suite écrite) ; bloc N | — |
| 25 | mineur | porté juste | brouillon, en-tête | — |

Bilan : 24 constats portés justes, 1 porté en partie (constat 5), aucun non porté.

## 3. Les corrections annoncées par le concepteur et non relevées par moi

- **a, les bornes des témoins de marge arrondies par défaut** : juste, et je l'avais manqué. 1 − 0,98⁸ vaut 0,1492369774, et non 0,149165 ; la borne de l'accord 2 sur 8 avec une classe à 0,03 vaut 0,0223407578, et non 0,022338. La règle « arrondi par excès à six décimales » est juste.
- **b, douze témoins et non dix** : juste. Neuf sont exigés (T1, T2, D1 à D4, A1, A2, C1) et trois sont de marge (M1 à M3) ; il y a 1 920 lancements (12 × 160).
- **h, la classe de F6 sans plantation** : juste. 4 000 × 0,06 = 240 tâches attendues, passage 0,0333, mort 0,343. La justification de l'écart 7 tient.
- Les lettres c à g sont aussi exactes là où je les ai recoupées : effectif planté exact (c), majorations de D3 (d), mondes d'essai de six lots (e, 4 lots alertés et P = 0,000086), 0,9365 (g).

## 4. Erreurs neuves introduites par la version 2

| N° | Gravité | Lieu | Constat | Correction proposée |
|---|---|---|---|---|
| E1 | **important** | conception § 7, « G1 … Garde à l'exécution » : « dès lors … tout événement `import` lève le drapeau d'arrêt » | **numpy 2 charge des sous-modules à la demande.** Je l'ai éprouvé ici, sous numpy 2.5.3, avec un crochet `sys.addaudithook` armé après `import numpy`. `numpy.random` n'est pas chargé par `import numpy` : le premier appel à `numpy.random.default_rng`, ou à `SeedSequence`, lève 47 événements `import`, `open` et `os.listdir`. Même avec `numpy.random` chargé d'avance, `numpy.unique` charge `numpy.ma` (3 événements `import`). Tel qu'il est écrit, le crochet arrête au code 97 tout témoin conforme qui tire sa pièce (D1, D2, donc l'épreuve entière), ou qui appelle une fonction chargée à la demande. Le cas sain de G1 le verrait avant le banc : ce n'est pas silencieux. Mais le texte ne se lit pas sans choix, et la règle « le module des témoins importe en tête tout ce dont il a besoin » ne suffit pas, puisque `numpy.ma` n'est importé par aucun témoin. Un import d'un module déjà en mémoire, en revanche, ne lève aucun événement (vérifié). | Écrire que le lanceur importe, **avant d'armer**, `numpy`, `numpy.random`, `numpy.ma`, `numpy.linalg` et `json`, et qu'il fait un tour d'échauffement (un `default_rng(SeedSequence([0, 0, 0, 0]))` et un appel de chaque fonction numpy employée par les témoins, sur des données factices). Ajouter au cas sain de G1 « chaque témoin, sur un lot d'essai, sans code 97 ». Autre voie : n'arrêter, une fois armé, que sur `open` d'un chemin hors de l'interpréteur et sur `os.*`, `subprocess.*`, `socket.*` et `ctypes.*`, et laisser passer `import` d'un module situé sous les dossiers de l'interpréteur. Dire la voie retenue. |
| E2 | mineur | conception § 7, artefact « lit son propre fichier source par une fonction de numpy » | Le résultat dépend de la fonction : `numpy.fromfile` lève directement `open` (vu) ; `numpy.loadtxt` lève d'abord un `import` (`urllib.parse`) puis `open`. Les deux sont vus, mais le développeur doit choisir. | Écrire `numpy.fromfile(__file__, dtype=numpy.uint8)`. |
| E3 | mineur | conception § 5 et brouillon, D3 dans F7 : « 0,1986 au plus » et « au plus 4,7 × 10⁻¹³ » ; bloc G | Deux majorants sont imprimés arrondis par défaut : la borne vaut 0,198608 et la probabilité 4,76 × 10⁻¹³. C'est sans effet sur l'issue, car la mort à 874 laisse une marge immense. Mais c'est contraire à la règle d'arrondi par excès que la version 2 pose elle-même pour les bornes. | Imprimer tout majorant arrondi par excès : 0,1987 et 4,8 × 10⁻¹³. La somme de la famille B, 3,3 × 10⁻¹², reste juste. |
| E4 | mineur | conception, en-tête et § 10 dernière réserve ; brouillon, documents qui font foi | « La ligne de GO-2026-11-21-69 n'est pas au registre » : c'est périmé depuis la fusion avec `main` (`registres/go.md`, ligne 668). | Citer la ligne et son contenu ; la condition de scellement 4 peut alors être remplie par la consignation de la décision sur F4 au registre des décisions. |
| E5 | mineur | conception § 6, premier alinéa : « Ce noyau est celui du banc de l'adjudant, augmenté » | L'affirmation est posée comme un fait, alors que le § 9 point 13 et la condition 5 disent qu'elle reste à vérifier par la mère. | « Ce noyau est, sous la vérification de la condition 5, celui du banc de l'adjudant, augmenté. » |

Je n'ai pas trouvé d'autre erreur neuve. Les chiffres neufs que j'ai recoupés sont justes : l'abstention de T2 par la loi exacte (même espérance que le bloc B), la mort de D1 certaine dès un lot sans séparation, la borne de l'union de D2, la majoration de D3 dans F0 par Cantelli, les classes entières de D4 et d'A2 (864 et 992 tâches), les familles A à D et les seuils des mondes d'essai.

## 5. Verdict

**Non scellable en l'état.** La condition de scellement 1 du brouillon exige une vérification « sans remarque ouverte », et il en reste une importante : E1. Tel qu'il est écrit, le crochet d'audit de G1 arrête des témoins conformes, puisque numpy charge `numpy.random` et `numpy.ma` à la demande. Les deux bloquants et vingt-deux des autres constats sont portés justes, le constat 5 l'est en partie, et le calcul est juste.

**Chemin court** : un erratum 1 à la conception v2 qui porte E1, et de préférence E2 à E5, puis ma vérification de ce seul erratum. Le brouillon peut alors être scellé sous un nom neuf, dès que ses conditions 2 à 6 sont remplies. Il n'y a rien à refaire ailleurs.

## 6. Nœuds qui restent pour Lazar

1. **Famille tenue à l'écart** servie en relevés de décisions (nœud 1 de la conception) : recommandation (a), confiance 0,6 ; à trancher avant l'étape 2.
2. **Écarts à la forme fixe**, points 1 à 6, 10 et 16 (nœud 2) : défaut sous 48 heures, « acceptés » ; le scellement attend.
3. **F6 avec ou sans plantation** (nœud 3) : recommandation « avec », sous la vérification de la mère ; le scellement attend. Je ne juge pas ce point.
4. **Étape 1** : devis, puis GO (nœud 4) ; avec le choix de l'isolement (nœud 7) : recommandation, le rejeu au loin.
5. **Vérité du dommage dans F4** (nœud 5) : tranchée par la mère sous GO-2026-11-21-69, à porter à la connaissance de Lazar. Le monde que D-4 réserve reste à son mot.
6. **Banc de l'adjudant ou banc à part** (nœud 6) : la mère vérifie ; c'est un nœud seulement si le banc doit être à part.
7. **Règle de rejeu** (nœud 8) : défaut sous 48 heures, « acceptée ».
8. **Reconnaissance du monde à ses lois** (nœud 9) : à concevoir avant l'étape 2.
