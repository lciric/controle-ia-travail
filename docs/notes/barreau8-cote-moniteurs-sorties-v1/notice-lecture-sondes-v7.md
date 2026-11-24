# Notice d'emploi — code de la lecture des sondes du barreau 8, côté moniteurs — v7

> **Version 7 de cette notice, écrite le 2026-11-24 par le développeur du côté des moniteurs (session fille du code de la lecture des sondes v6).** Elle accompagne le **code de la lecture en version 6** : `src/controle_ia/barreau8_moniteurs/lecture_sondes_v6.py` et son module à part des lectures descriptives `src/controle_ia/barreau8_moniteurs/lectures_descriptives_additif_1_v1.py` ; essais `tests/test_barreau8_moniteurs_lecture_v6.py` (empreintes dans les compagnons `.sha256` et dans le bordereau du code). Elle remplace, pour ce code, la notice v6 (`notice-lecture-sondes-v6.md`, qui accompagne le code de version 5 et reste scellée à côté de lui). Ce qui n'est pas redit ici est inchangé depuis la v6 de la notice.

Pour le lecteur neuf des sondes. Cette notice dit comment lancer le code, dans quel ordre, avec quelles entrées, ce qu'il refuse et ce qu'il rend. **Elle ne porte aucun résultat.** Le verdict n'est pas prononcé par ce code : il rend une sortie mécanique scellée (états, lignes déclenchées, réserves, lignes de tête des additifs, bloc des lectures descriptives hors verdict) que le juge neuf applique à la table des critères gelés.

## Pièces qui font foi

- Texte préenregistré scellé : `prereg/lecture-sondes-barreau8-v1.md`, empreinte `8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4` (ligne `SCELLEMENT-SONDES-IIB`).
- Additif 1, organisme changé : `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md`, empreinte `fc5b0610ed004ea4b1565e7a50567d7538b0f9e66b129c874c2f8c5bc2a4d8c2` (ligne `SCELLEMENT-ADDITIF-1-SONDES-IIB`).
- Additif 2, format des entrées : `prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md`, empreinte `8e930abadcdbb050e026771cb67f90bb47ebed63955b498364d0fa9c9f7eab5e` (ligne `SCELLEMENT-ADDITIF-2-SONDES-IIB`).
- Table neuve des constantes reportées (M-4), **seule source des constantes de forme** : `docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json` (`d576c16b…ddc4`), citée par la clé `constantes` du bordereau du code.
- Pièces de la condition D-14 : table de l'additif 1 (`constantes-reportees-additif-1-v1.json`, `f6e9c8d5…2171`, pièce de constat), notes d'interface v6 et v7 et fiche v7 (à leurs empreintes citées par la table neuve), pièce de comparaison v2 (`comparaison-interface-v6-v7-v2.json`).
- Rapport de contre-lecture de conformité du code v6 : cité par la clé `rapport_conformite` du bordereau du code ; son chemin et son empreinte se lisent là.

## Ce que tu ne fais pas

Comme en v6 : aucun choix de sonde, de couche ni de seuil ; aucune ouverture de la consigne privée, de la conception, du verdict du témoin positif planté (existence et empreinte seulement), **ni de l'ordre du lancement et de ses pièces** (seule la pièce d'attestation de l'ordre, sans contenu, est lue) ; aucune seconde lecture ; aucune ligne de registre inscrite à la main (la commande de lecture inscrit elle-même `LECTURE-SONDES-IIB`).

## Où poser les entrées (ce qui change depuis la v6)

- **L'extrait des états** : `docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json` et son compagnon, chemin exigé par la commande (RP-10 ; ligne 3) ; il porte `4(m + 1) + 1` états (13 à la version 6), paires lues dans la table neuve.
- **Pièce d'attestation de l'ordre (D-6 lue avec M-3)** : `docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-ordre-course-lue-additif-1-v1.json`, empreinte exigée `8f6b5025…e76a` ; elle remplace la « pièce de comparaison de l'ordre scellé » de la v6 de la notice (l'option `--piece-ordre-scelle` n'existe plus).
- **Pièce d'attestation de la course et de l'oracle (D-15)** : `docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json` et son compagnon.
- **Référence boîte noire (LD-4), facultative** : `docs/notes/barreau8-cote-moniteurs-entrees-v1/reference-boite-noire-course-lue-additif-1-v1.json`. Absente : LD-4 « non jouée », sans effet. Présente mais hors de sa forme, non citée par le mandat du lecteur, d'une autre course, ou à scores illisibles : « non lisible », cause écrite, sans refus.
- **Mandat du lecteur** : il cite cinq empreintes — liste des exclus, registre « qui a lu quoi », attestation de l'ordre, attestation de la course et de l'oracle, et la référence boîte noire si elle existe. Le mandat du juge cite les deux premières.
- **Heure de remise de la note d'interface version 7**, attestée par la session mère, passée par `--remise-note-v7 AAAA-MM-JJTHH:MM:SSZ` (ligne (vi) de RP-14 ; hors format : refus `[RP-14]`).
- Arbre de travail propre, registre des accords, trois fichiers de sondes : inchangés.

## Ordre des commandes

De la racine du dépôt. `LECTURE` = `PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.lecture_sondes_v6` ; `REG` = `registres/sondes-iib-v1.md`. Fichiers de sondes inchangés (`--sondes-legeres`, `--planchers`, `--sondes-neuves`, chacun avec son compagnon).

### 0. Bordereau du code (une fois, avant la ligne `CODE-LECTURE-SONDES-IIB`)

```
LECTURE modules
LECTURE bordereau-code --racine . \
  --texte-scelle prereg/lecture-sondes-barreau8-v1.md \
  --additif prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md \
  --additif-2 prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md \
  --constantes docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json \
  --rapport-conformite <rapport scellé de la contre-lecture de conformité> \
  --notice docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v7.md \
  --accord-lecture GO-AAAA-MM-JJ-NN \
  --sortie <chemin neuf du bordereau du code>
```

`modules` imprime les modules `controle_ia` chargés et leurs empreintes ; le module des lectures descriptives y figure ; ni la bibliothèque des cartes de calcul ni le code de la passe n'y sont. `bordereau-code` refuse d'écrire sous une table neuve qui dit « nœud » (`[21]`) ou hors de sa forme (`[20]`), écrit et scelle le bordereau (**neuf clés** : `texte_scelle`, `additif`, `additif_2`, `constantes`, `modules`, `commit`, `rapport_conformite`, `notice`, `accord_lecture`) et imprime la ligne `| CODE-LECTURE-SONDES-IIB | heure | chemin | empreinte |` que la session mère inscrit, **strictement après** la ligne `SCELLEMENT-ADDITIF-2-SONDES-IIB` (rang et heure). Même forme de lancement (`python -m`) que la lecture.

### 1. Garde de réception seule (condition D-11)

```
LECTURE reception --racine . --registre REG --sondes-legeres <…> --planchers <…> --sondes-neuves <…>
```

Jouable dès que les lignes des trois scellements, du code de la passe, du code de la lecture et de la livraison sont inscrites. **Avant d'ouvrir quoi que ce soit de la livraison**, elle exige le registre propre à huit clés, les trois textes scellés (D-17), le bordereau du code à neuf clés, les modules chargés égaux à ceux du bordereau, la table neuve à son empreinte disant « report », et les pièces de la condition D-14. Les formes (tâches, épisodes, pas, jetons, conditions, adaptateurs, pas du sous-échantillon 16 × k et 128 × k, effectifs n15 et n7) viennent de la table neuve ; r4 et r5 les contrôlent. Sortie : « GARDE DE RÉCEPTION TENUE » et le repère de couche r8, ou le refus et sa cause, sans score ni écart de score.

### 2. Contrôle de l'extrait des états

```
LECTURE etats --racine . --registre REG
```

### 3. Recette de la puissance (RP-4)

```
LECTURE puissance --racine . --registre REG --entropie <F-3> --run-id AAAAMMJJ-HHMMSS-puissance-barreau8
```

Recette dérivée de la table neuve (conditions par rôle ; budget `12 × ⌈T·E·A·m / 1280⌉` heures, au moins 12). À la version 6 des constantes, les tirages de la recette sont ceux du code de version 5 (essai à l'appui).

### 4. Lecture : une seule commande, une seule fois

```
LECTURE lecture --racine . --registre REG \
  --sondes-legeres <…> --planchers <…> --sondes-neuves <…> \
  --entropie <F-3> --run-id AAAAMMJJ-HHMMSS-lecture-sondes-barreau8 \
  --registre-accords registres/go.md \
  --puissance diag/<run de la recette>/aires-minimales-detectables-barreau8-v1.json \
  --mandat-lecteur <mandat scellé> --mandat-juge <mandat scellé> \
  --empreinte-liste-exclus <64 caractères> --empreinte-qui-a-lu-quoi <64 caractères> \
  --remise-note-v7 AAAA-MM-JJTHH:MM:SSZ
```

Étapes : conditions de départ ; garde de réception ; manifeste ; conditions jugées (par rôle, RP-9) ; essai de la chaîne (étiquettes tirées **par épisode**, ⌊A/2⌋ actions étiquetées 1, RP-3) ; lecture décisive (c) à (g) ; **étape (g bis) : lectures descriptives LD-1 à LD-5, dans le bloc `descriptif_additif_1`, jamais dans le verdict ni dans les déclencheurs de l'audit** — non jouées sous S1, S3, S4 et L5 ; une exception du module est capturée et écrite « échec », la lecture décisive reste ; sortie scellée portant en tête les **lignes de tête RP-14** (liste ordonnée `{"ligne", "texte"}`, sans effet sur le verdict) ; inscription de `LECTURE-SONDES-IIB`.

### 5. Audit de symétrie, seulement si un déclencheur a joué

```
LECTURE audit --racine . --registre REG --sondes-legeres <…> --planchers <…> --sondes-neuves <…>
```

Inchangé, sauf : contenu (1) lu avec RP-5 (E épisodes de A actions par tâche et par condition) ; une relecture arrêtée par une garde est écrite comme défaut D3 (« relecture arrêtée », cause comprise), jamais tue. L'auditeur ne lit pas le bloc des lectures descriptives.

## Conditions de départ vérifiées mécaniquement

Dans cet ordre ; au premier manque, refus, rien n'est ouvert plus avant.

1. Aucune sortie `lecture-sondes-barreau8-v1.json` sous `diag/`.
2. Registre propre, **huit clés** : les trois lignes de scellement, une seule chacune, dans l'ordre (texte, additif 1, additif 2), strictement par le rang et par l'heure (`[5]`, `[18]`, `[30]`) ; pour les cinq clés comptées (`CODE-PASSE-IIB`, `CODE-LECTURE-SONDES-IIB`, `LIVRAISON-PASSE-IIB`, `ETATS-COURSE-IIB`, `LECTURE-SONDES-IIB`), exactement une ligne strictement postérieure à la ligne de l'additif 2 (une ligne antérieure ne compte pas et s'écrit telle dans la sortie ; une ligne de code seulement antérieure : `[23]`) ; clé hors des huit : `[5]` ; chaque fichier cité à l'empreinte de sa ligne ; chaque ligne antérieure à l'instant d'ouverture ; livraison après le code de la passe ; `LECTURE-SONDES-IIB` absente.
3. Trois textes scellés, intacts, aux empreintes de leurs lignes (D-17) ; cellule F-3 égale à l'entropie donnée (`[1]`).
4. Bordereau du code à neuf clés ; textes égaux à ceux des lignes ; rapport de conformité de la version 5 refusé ; modules chargés exactement ceux du bordereau.
5. Table neuve à son empreinte, « report », quatre champs exactement « couvert par l'additif 2 » (`[21]`), cohérente avec les règles RP (`[20]`) ; constante de forme d'un cadre différente de la table : `[24]` ; pièces de la condition D-14 (`[20]`, `[21]`).
6. Accord de lecture (D-4).
7. Mandats (D-5).
8. Attestation de l'ordre (D-6 lue avec M-3) : empreinte de M-3, citée par le mandat du lecteur, forme fermée, faits O-1, O-2, O-4, O-7 « tient », O-3, O-5, O-6 « non dit » au plus, aucun « ne tient pas », réponse « non » à la question E-1, ordre et pièces scellés, ligne de calcul `GO-2026-11-22-75` (`[16]`).
9. Témoin positif planté (D-9).
10. Aires minimales détectables (D-10).
11. Chemin et forme de l'extrait des états (D-12 ; `[3]`).
12. Fichiers de sondes (D-8) ; garde de réception r1 à r7 (D-11).
13. Nom de la course égal dans la trace de la passe et dans l'extrait (`[3]`).
14. Attestation de la course et de l'oracle (D-15) : citée par le mandat du lecteur, forme fermée, « conforme », même course que l'extrait et la trace (`[22]`) ; désignation de l'oracle après la première sortie de l'évaluation : écrite en tête, n'arrête pas.
15. Référence boîte noire : jamais un refus.
16. Heure de remise de la note version 7 (`[RP-14]` si hors format).

## Sorties (ce qui s'ajoute à la v6)

- Dans `conditions_de_depart` : table neuve, pièces de la condition D-14, attestation de l'ordre (états seulement), attestation de la course et de l'oracle, statut de la référence boîte noire, heure de remise de la note v7, lignes antérieures qui ne comptent pas.
- En tête : `lignes de tête des additifs (RP-14), sans effet sur le verdict`, liste ordonnée des lignes (i) à (xii) qui s'appliquent.
- `descriptif_additif_1` : état (« jouées », « non jouées » et sa cause, « échec » et sa classe), comptes, LD-1 jumeau honnête (aires, rappels au seuil hors de la tâche), LD-2 bases d'épisode (maximum, dernier état, cascade ; différences appariées de rappel), LD-3 base « mots et coût », LD-4 référence boîte noire (statut, et par sonde si lisible), LD-5 par mode. Chaque valeur porte sa clé de graine ; marque « trop propre : réserve (règle R4) » au-delà de 0,95 ou en deçà de 0,05 d'aire, ou à un rappel de 1.
- Manifeste : graines de la lecture, de la recette et des lectures descriptives (clés `additif-1/…`), et la forme lue dans la table neuve.

## Codes de refus ajoutés

| code | sens |
|---|---|
| `[16]` | attestation de l'ordre absente, d'une autre empreinte, non citée, hors forme ou n'attestant pas (M-3) |
| `[18]` | ligne de l'additif 1 absente, répétée, ou bordereau sans additif 1 conforme |
| `[20]` | table neuve ou pièce de la condition D-14 absente, d'une autre empreinte, sans compagnon ou hors de sa forme |
| `[21]` | table neuve disant « nœud » ou champs « couvert par l'additif 2 » autres que les quatre ; pièce de comparaison v2 d'autres comptes ou d'autres champs |
| `[22]` | attestation de la course et de l'oracle absente, non citée, hors forme, « écart », ou d'une autre course |
| `[23]` | ligne de code (passe ou lecture) seulement antérieure à la ligne de l'additif 2 |
| `[24]` | constante de forme d'un cadre différente de la table neuve |
| `[30]` | ligne de l'additif 2 absente, répétée ou mal placée ; bordereau sans `additif_2` conforme |
| `[RP-14]` | heure de remise de la note version 7 hors format |

## Durée et mémoire sur processeur

**Mesuré ici, sur données factices aux tailles de la table neuve** (2 560 actions, 2 409 directions dont 3 × 800 de plancher, environ 524 000 jetons notés ; 2 000 tirages, 200 permutations), quatre cœurs, calcul seul (sans la réception ni le chargement des archives) :

- lecture décisive seule (essai de la chaîne, production, diagnostic, couches 7 et 23, dose, déclencheurs) : **104,5 secondes** ;
- lecture décisive suivie des lectures descriptives (sans référence boîte noire) : **123,1 secondes** (une partie des cœurs était occupée par un autre calcul pendant cette mesure : les lectures descriptives ajoutent de l'ordre de vingt secondes) ;
- pic de mémoire vive du processus, données factices comprises : **environ 800 Mo** dans les deux cas.

Script de mesure (hors dépôt, données factices seulement) : la lecture est appelée par sa fonction `calculer_lecture`, sur un tableau de scores d'action et de scores par jeton tirés au hasard, avec la vraie table neuve des constantes.

**Estimé, repris de la v6 de la notice (non remesuré)** : garde de réception 3 à 5 minutes, pic de 2,5 à 3 Go (cinq archives rebâties en mémoire, fichier des sondes neuves d'environ 430 Mo chargé en entier) ; la lecture la rejoue. Prévoir une machine avec au moins 4 Go libres. Recette de la puissance : environ 1,6 heure pour les cinq cases de f = 1 et 4,8 heures pour les quinze (mesure de 5,7 secondes par répétition), budget de 12 heures. Un rappel descriptif avec référence boîte noire ajoute deux jeux de tirages par surveillant et par sonde.

## Ce qui a été éprouvé, et ce qui ne l'a pas été

**Éprouvé** (145 essais sur données factices) : chaque garde de réception, chaque condition de départ et chaque code de refus ci-dessus sur cas sain et sur artefact ; lecture de bout en bout avec ligne inscrite et seconde lecture refusée ; lectures descriptives à valeurs connues ; sortie décisive identique à l'octet avec ou sans lectures descriptives, avec ou sans référence, et sous une exception du module ; table neuve, pièces de la condition D-14 et attestation de l'ordre **réelles** (elles ne portent aucun contenu de la course) ; conditions aux noms et doses autres que la version 6 (lecture par rôle) ; module lancé par `python -m` en sous-processus.

**Non éprouvé** : la vraie livraison, le vrai extrait des états, la vraie attestation de la course et de l'oracle (absents, et hors du cloisonnement du développeur) ; les vrais fichiers de sondes ; la recette entière ; la réception aux tailles réelles.

## Récupérer ce qui est récupérable (règle de Lazar, R-3661)

Inchangé depuis la v6 de la notice : le code ne supprime aucun fichier ; tout ce que produit chaque commande jouée (manifestes, sorties, sorties imprimées, ligne inscrite) se verse scellé, inventaire par programme, avant tout message à la session mère ; aucune seconde exécution pour récupérer une sortie manquante.
