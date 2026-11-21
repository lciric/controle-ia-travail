# Rapport du planificateur — v4 du plan de la course principale

- Auteur : planificateur du plan v4, modèle F. Je n'ai écrit ni les plans v1 à v3, ni leurs contre-lectures, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevés de `date -u` : 08:15:31Z avant l'écriture ; 08:21:49Z à l'alignement sur l'erratum 2.
- Commande : le mandat `mandat-planificateur-plan-v4-course-principale-v1.md` (`1bf2d874d2c575dbdc62641a088d0abdea6d9ea3d3cc18f4cfebd0b51184234d`, égale à son compagnon), puis deux compléments de la mère reçus en cours de travail : l'erratum 2 de la note d'abord « demandé », ensuite arrivé, à citer par son empreinte complète, avec les lots C2 et C3 à aligner et tout écart à signaler.
- Processeur seul : aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucune machine louée, aucun code de l'organisme lancé, aucune écriture dans un dépôt, aucun commit. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Seul programme joué : mon programme de calcul, sans entrée.
- **Aucun refus de permission, de classifieur ni de garde n'a été rencontré.**

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/planificateur-plan-v4-course-principale/`. Chaque pièce a son compagnon `.sha256`.

| pièce | objet |
|---|---|
| `plan-experimentateur-tests-de-mort-course-principale-v4.md` | la v4 |
| `differentiel-plan-v3-v4.md` | ce qui change, partie par partie |
| `rapport-planificateur-v4.md` | ce rapport |
| `table-empreintes-planificateur-v4.md` | empreintes |
| `calculs_plan_v4.py` et `calculs-plan-v4-sortie.txt` | les calculs refaits ; joué deux fois, `cmp` muet avec `calculs-plan-v4-passe-2.txt` |

Exclues du versement : les copies de registre (`lecture-…`) et les fichiers de préfixe `lu-`.

## 2. Ce que j'ai porté, correction par correction

### 2.1 Les quatre corrections du contrôle de la v3

| n° | correction demandée | lieu dans la v4 | portée |
|---|---|---|---|
| 1 | D5 (a) : retirer « dans la v69 comme l'additif scellé le veut, AC-1 l'appelant sans le modifier » ; socle = couche sous le sommet ; sommet d'AC-1 dans AC-1 ; sommet de la v69 tel que scellé ; nœud du sommet unique déclaré ; défaut redit | § 7.2, D5 ; § 3.1 ; § 0, point 4 | oui : option (a) récrite ; option (c) = sommet unique, nœud de Lazar déclaré, sans défaut, non tranché ; défaut de (a) compté à partir de la v4, pour le lieu du socle et l'ordre des écritures seulement ; la v3 dite ne plus devoir courir |
| 2 | E1 scindé ; C3 hors de la v69 ; 1 à 2 heures pour le sommet d'AC-1 ; rapport, § 4, point 5, récrit | § 4.2, table (E1-v69, E1-AC, C3) et chemin critique ; § 5 ; ce rapport, § 4, point 5 | oui : quatorze lots ; 46 à 56 heures de code ; 18,25 à 20,25 heures jusqu'au premier dollar |
| 3 | D8 (a) : « étend le modèle de GO-15 et GO-28 sur deux points » ; dire quels champs sont fermés | § 7.3, option (a) | oui pour la phrase et les deux points, les deux lignes d'accord citées à la lettre ; **non pour les noms des champs fermés** (écart 1, § 5) |
| 4 | § 6.3 : 0,081 au lieu de 0,08 ; D8 (d) chiffrée | § 6.3, première ligne ; § 7.3, option (d) ; § 0, point 3 | oui : 0,081 ; 92 au plus ; onze identifiants nommés par GO-2026-11-19-55 et -56 |

### 2.2 Les ordres de grandeur de l'erratum 1

| ce que dit l'erratum 1 | lieu dans la v4 |
|---|---|
| banc joueur sur la machine jetable, banc noteur chez la mère, contre-calcul à l'octet sans exécuter le greffon, banc d'étalonnage à 0 USD chez la mère | § 3.2, récrit ; § 2.1, ligne « où cela tourne » ; § 0, point 7 ; § 4.2, C2 et C3 |
| la durée du rejeu, non chiffrée ; première mesure à l'étalonnage avant tout devis de machine | § 3.2 ; § 6.2, dernier alinéa : heures dites planchers, plafonds de machine dits non établis |
| lecteur témoin : 0,061 USD par test, borne haute, relevé d'une course et d'un modèle | § 6.1 ; § 6.3 |
| par greffon : 0,14 à 4,10 USD ; facteur trente environ | § 6.3 ; § 2.4, point 3 ; § 7.2, D6 |
| mesure sur les témoins = nombre de greffons témoins × cette fourchette, plus la machine | § 6.3, ligne 1 ; § 0, point 8 |
| barreau 2 : 640 à 1 430 USD par carte à cinq espèces, 110 à 430 à deux, l'étage dans la boucle | § 6.4, section neuve ; § 0, point 8 ; § 2.1 ; § 7.1, note sur N1 |
| N1 à N7 inchangés | § 7.1, recopiés tels quels |

### 2.3 Le compte des cartes

Inscrit comme **borne pour le devis**, jamais comme le compte de la note : § 0, point 3 ; § 6.2 (ligne 2 gardée à 94) ; § 6.3 ; § 7.3, option (d), avec ce que le compte est et ce qu'il n'est pas.

### 2.4 L'erratum 2 de la note

Cité par son empreinte complète (`12c6034978e7475e007147df632327537b6a4a32c458ceef5e7d51b4aa3127de`, égale à son compagnon tiré de `origin/main`, commit `8b527dd5…`) : en-tête, § 1, § 3.1, § 7.2. Alignement : la liste du socle du § 3.1 est la sienne ; C3 porte le rejeu et le banc joueur, C2 le banc noteur, le contre-calcul, la porte des lots, le registre et le mécanisme des témoins ; E1-AC apporte au socle la forme d'épreuve, le constructeur de la fiche et le contrôle d'après-étage ; le lanceur est propre à chaque emploi ; l'ordre passe à « socle avant E3 ».

## 3. Les deux lignes de coût, refaites

| | ligne 1, les seuls témoins | ligne 2, les cartes |
|---|---|---|
| appels | nombre de greffons témoins × 0,14 à 4,10 USD : 0,57 à 16,40 pour 4 ; 1,70 à 49,20 pour 12 | 13,35 à 385,40 USD pour 94 cartes au plus ; 13,06 à 377,20 pour 92 ; traducteurs non chiffrés |
| machine, hors rejeu du banc joueur | 2, 4, 12 heures : 0,15 à 3,36 USD aux tarifs relevés ; 2,60 à 15,60 à 1,30 USD de l'heure | 7, 25, 48 heures : 0,51 à 13,44 USD ; 9,10 à 62,40 à 1,30 USD de l'heure |
| plafond de machine proposé | 5 USD, 12 heures | 15 USD, 48 heures |
| ce qui manque | la durée du rejeu sur la machine, mesurée nulle part | la même, plus les traducteurs |

Barreau 2, hors de ces deux lignes : de l'ordre de 640 à 1 430 USD par carte à cinq espèces, de 110 à 430 à deux. Mon recalcul trouve 643 où l'erratum écrit 642 (642,80) ; sans effet.

## 4. Ce que la lettre ne fixe toujours pas

1. La durée du rejeu du barreau 1 sur la machine jetable ; donc les deux plafonds de machine.
2. Le nombre de cartes déjà sous un texte scellé : deux porteuses nommées pour les lignes 1 et 3, onze identifiants nommés en tout par deux lignes d'accord, les fusionnées non dénombrées.
3. Le coût des deux traducteurs.
4. Les noms des champs fermés parmi les dix champs d'une carte.
5. **Le fichier où vit le sommet d'étage** : la v3 l'écrivait « dans la v69, AC-1 l'appelant sans le modifier » ; c'était incompatible avec l'additif scellé. La v4 écrit : le sommet d'AC-1 dans AC-1, en fichier neuf ; celui de la v69 tel que scellé ; le socle commun sous les deux, en fichiers neufs hors de la v69. Les noms de ces fichiers ne sont fixés nulle part.
6. Le partage des heures entre E3, C2 et C3 après que l'erratum 2 a rangé le banc dans le socle.
7. Si le socle se laisse appeler par plusieurs sommets sans réécriture : à établir sur le code.

## 5. Écarts

1. **Champs fermés de D8 (a) non nommés.** Le mandat demande « les champs fermés nommés ». La pièce qui les porte, la configuration scellée de la course v9, n'est pas dans mes lectures ; le registre dit seulement que le code « exige les dix champs obligatoires ». J'ai écrit la conséquence (si aucun champ n'est fermé, le premier point d'extension tombe) et demandé que la mère les relève avant que l'option aille à Lazar.
2. **GO-2026-11-21-28 n'existe pas** dans `registres/go.md` au commit lu (la dernière ligne du jour est la -22), et GO-2026-11-21-15 porte sur un autre objet. J'ai lu « GO-15 et GO-28 » comme GO-2026-11-20-15 et GO-2026-11-20-28, que la v3 et le contrôle citent ; GO-2026-11-21-16 est citée telle quelle.
3. **Une recherche à joker.** Pour trouver le chemin de l'additif, que ni le plan v3 ni sa table ne portent, j'ai fait une recherche d'un préfixe d'empreinte avec un motif de noms de fichiers sur les tables des plans v1 à v3. C'est contraire à l'interdit de tête du mandat. Elle n'a rendu qu'une ligne de la table du plan v1 ; rien d'autre n'a été ouvert par elle.
4. **L'additif lu sur `origin/main` à un autre chemin** que celui de la table du plan v1 (qui n'est pas sur `main`) : `prereg/organisme-auto-conception-v9/orchestrateur-v69/…`, chemin donné par la note ; même empreinte aux deux endroits.
5. **Noms de fichiers devinés** pour le plan v3, son rapport, le rapport du compte et le compagnon de l'erratum 2, faute de liste ; tous trouvés au premier essai, empreintes conformes.
6. **La lecture descriptive de la course v9 copiée de `main`** pour y chercher la liste des dix champs ; seule la ligne 99 m'est revenue. La copie est exclue du versement.
7. **Lots et ordre changés au-delà de la lettre du contrôle**, par alignement sur l'erratum 2 : banc joueur et banc noteur sortis de E3 vers C3 et C2 ; C2 et C3 ne dépendent plus de E3 ; le socle s'écrit avant E3 ; C2 rejoint le chemin jusqu'au premier dollar (20,25 à 23,25 heures).
8. **Confiance sur D5 (a) portée de 0,6 à 0,7** : mon jugement, l'option ne heurtant plus aucun texte scellé.
9. **Ligne 2 gardée à 94 cartes dans le tableau de machine**, la borne du devis selon le mot de la mère ; 92 est montré à côté.
10. **Section § 3.3 ajoutée**, pour les écarts entre l'erratum 2 et le plan : nœud du sommet unique déclaré ici alors que l'erratum écrit « aucun nœud neuf » ; heures non redistribuées ; table d'admission, mécanisme commun et valeurs propres, lecture de moi.
11. **Registres lus au commit `aea06e63…`**, l'erratum 2 au commit `8b527dd5…` : je n'ai pas relu les registres au second commit.
12. Quelques commandes `sha256sum` à plusieurs chemins complets, sans joker.

## 6. Remarque pour la mère

Le § 3.1 de la note — alinéa de tête et point 1, « l'écrire une fois, la forme d'épreuve en paramètre » — portait le même conflit avec l'additif scellé que le « lanceur 11 » de son point 6 : un paramètre de forme sur le sommet de la v69 est le champ de configuration que l'additif interdit (§ 2, C3), et un greffon passé par ce sommet serait refusé par la garde 10 ou privé de contre-calcul par la garde 11. **L'erratum 2 corrige les deux points** (ses phrases 2 à 4). Restent à faire suivre à son auteur, si tu le veux : les points 2 et 3 du § 3.3 du plan (heures non redistribuées entre E3, C2 et C3 ; lecture de « la table d'admission » dans le socle).

Le défaut de D5 sous 48 heures ne doit courir que sur le texte de la v4.

— planificateur du plan v4, modèle F
