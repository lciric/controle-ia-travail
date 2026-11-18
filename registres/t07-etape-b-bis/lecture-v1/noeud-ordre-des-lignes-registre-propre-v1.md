# Nœud pour Lazar — l'ordre des lignes du registre propre arrête la lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Écrit le 2026-11-18 vers 20:25Z par le préparateur de la commande de lecture (sous-agent neuf, modèle Fable 5.2), à la demande de la conductrice de la lecture (`session_013QMayjNC5GKdDFTN87oAV5`). Par lecture seule de textes scellés, du registre propre, du code et de l'histoire git de ces fichiers. Aucune mesure, aucun score, aucune issue n'a été lu par personne (§ 6).

## 1. Décision en une phrase

Lazar, dis-nous comment se lit l'égalité à la seconde entre la ligne de l'accord de calcul (`GO-BBIS`) et la ligne de la fiche de code remplaçante (`CODE-BBIS`, seconde ligne) du registre propre : laisser la garde d'ouverture refuser et tenir la lecture pour « non lue », ou accorder un quatrième addendum d'écart, scellé et contre-lu avant toute lecture, qui dit que ces deux lignes, entrées par un même commit, sont dans l'ordre.

## 2. Enjeu

- La course de l'apprentissage des sondes sur la tâche s'est finie, ses scores sont fermés sur la branche `donnees/t07-etape-b-bis-v2`, personne ne les a lus.
- Le module de lecture en vigueur (`src/controle_ia/t07bbis/lecture_v3.py`) commence par une garde d'ouverture. Sur le registre propre tel qu'il est, cette garde refuse : deux lignes portent la même seconde là où le second addendum exige un ordre strict. Au refus, le code n'ouvre aucun score et écrit la phrase gelée « Étape B bis non lue : [motif]. ».
- La cause est une heure d'inscription, pas une mesure. Mais c'est la lettre d'un texte scellé : la lire autrement est un écart à un préenregistrement scellé, donc ton nœud, sans défaut sous 48 heures.
- Échéance du texte : verdict scellé au plus tard le dimanche 22 novembre (`prereg/T0.7-etape-B-bis-v1.md`, section « Calendrier », l. 230).

## 3. Les faits, mot pour mot

### 3.1 Ce que les textes exigent

- **Second addendum, point SA-11** (plan d'analyse, point 2, ordre des lignes), `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`, l. 249, bloc « Nouveau, qui fait foi » :
  > Puis `CODE-BBIS`, `GO-BBIS`, (second addendum : `CODE-BBIS` remplacée une seule fois, strictement après `GO-BBIS`), création, `SCORES-BBIS`, lecture,
- **Second addendum, point SA-5** (liste d'arrêt), même fichier, l. 142, bloc « Nouveau, qui fait foi » :
  > correction du code sous un nom neuf, ligne `CODE-BBIS` remplacée une seule fois (au registre propre : une seconde ligne `CODE-BBIS`, ajoutée après `GO-BBIS` et avant la création de la course qu'accorde GO-2026-11-16-11, strictement postérieure à la première, qui fait foi ; la première reste ; jamais une troisième), relance sous ce texte ; […]
  Sa raison (l. 145-149) nomme le code qui porte cette lecture : « `lecture_v3.lire_lignes` (`remplacables`), `lecture_v3.exiger_ordre_propre`, `registre_bbis_v2.ajouter_ligne_propre` ».
- **Texte scellé, section « Lignes de registre »**, `prereg/T0.7-etape-B-bis-v1.md`, l. 222 : « format `| clé | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 |`, lignes ajoutées, jamais réécrites ».
- **Troisième addendum** (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md`) : il ne dit rien de l'ordre entre `GO-BBIS` et la seconde ligne `CODE-BBIS`. Il en dit trois choses voisines :
  - l. 138-141 : « une troisième ligne `CODE-BBIS` est refusée par la liste d'arrêt scellée (« ligne `CODE-BBIS` remplacée une seule fois »), par la garde d'entrée de la marche (`lecture_v3.lire_lignes` : deux lignes au plus, « en double ou mal formée » au-delà), par `registre_bbis_v2.ajouter_ligne_propre` et par la garde de création » ;
  - l. 317-318 : « fiche remplaçante inscrite au registre propre à 11:05:29Z (seconde ligne `CODE-BBIS`) et versée au commit `c098fb51` à 11:07:47Z » ;
  - § 3, « Inchangés » : « liste d'arrêt (dont « ligne `CODE-BBIS` remplacée une seule fois » : aucune troisième ligne) » et « registre propre (aucune ligne neuve, aucune clé neuve) ».
- **Issue prévue au refus**, `prereg/T0.7-etape-B-bis-v1.md`, l. 143 : « | I0 | marche sans scores, garde refusée, ou les quatre cellules P-S_d en E0 | « Étape B bis non lue : [motif]. » | ».

### 3.2 Ce que porte le registre propre

`registres/t07-etape-b-bis-v1.md`, lignes 5 à 8 :

- l. 5 : `| CODE-BBIS | 2026-11-16T12:57:27Z | registres/t07-etape-b-bis/code-bbis-v1.json | ee362bb7… |`
- l. 6 : `| CODE-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/code-bbis-v2.json | 4b28535c… |`
- l. 7 : `| GO-BBIS | 2026-11-17T11:05:29Z | registres/t07-etape-b-bis/go-bbis-v2.txt | 33f38e67… |`
- l. 8 : `| SCORES-BBIS | 2026-11-18T19:43:48Z | diag/20261118-154143-bbis-t07-v1/sondes-bbis.json | 645a172f… |`

Les lignes 6 et 7 portent la même seconde, `2026-11-17T11:05:29Z`. Dans le fichier, la ligne de la fiche remplaçante (l. 6) est écrite **avant** celle de l'accord de calcul (l. 7), alors que SA-5 dit « ajoutée après `GO-BBIS` ».

### 3.3 Ce que le code exige

`src/controle_ia/t07bbis/lecture_v3.py`, l. 636-645 :

```python
def exiger_ordre_propre(lignes: dict) -> None:
    """Ordre du plan, point 2 ; second addendum : une ligne `CODE-BBIS` remplacée se lit SCELLEMENT-BBIS < CODE-BBIS (première)
    < GO-BBIS < CODE-BBIS (remplacement) < SCORES-BBIS."""
    lignes, chaine = dict(lignes), list(ORDRE_PROPRE)
    if "CODE-BBIS" in lignes and "remplace" in lignes["CODE-BBIS"]:
        lignes["CODE-BBIS (première)"] = lignes["CODE-BBIS"]["remplace"]
        chaine = ["SCELLEMENT-BBIS", "CODE-BBIS (première)", "GO-BBIS", "CODE-BBIS", "SCORES-BBIS"]
    for a, b in zip(chaine, chaine[1:]):
        if a in lignes and b in lignes and not lignes[a]["instant"] < lignes[b]["instant"]:
            raise RefusLecture(f"ligne {a} ({lignes[a]['date']}) pas strictement antérieure à {b} ({lignes[b]['date']})")
```

- La comparaison porte sur les dates écrites dans les lignes, à la seconde, strictement (`<`). L'ordre des lignes dans le fichier et l'ordre des commits n'y entrent pas.
- Elle est appelée dans la garde d'ouverture de la lecture, l. 1246, à l'intérieur du bloc dont le refus rend l'issue « non lue » (l. 1261-1264 : `res["issue"] = issue_complete({}, {}, None, motif_i0=f"garde refusée ({e})")`, puis retour, sans rien ouvrir).
- **Refus relevé à la préparation**, par cette fonction jouée sur le seul registre propre (aucun fichier de résultat) : « ligne GO-BBIS (2026-11-17T11:05:29Z) pas strictement antérieure à CODE-BBIS (2026-11-17T11:05:29Z) ».
- Le module précédent (`lecture_v2.py`, que le mandat de la session nommait par erreur) refuse plus tôt, à la lecture des lignes : « ligne CODE-BBIS en double ou mal formée ». Le module en vigueur est bien `lecture_v3.py` (second addendum, SA-7, l. 176 ; fiche de code `registres/t07-etape-b-bis/code-bbis-v2.json`).

### 3.4 L'histoire des commits du registre propre (relevée à la préparation, noms et commits seulement)

| commit | date du commit | ce qu'il fait au registre propre | dans l'ascendance de `main` et du commit de la course (`438a9c52`) |
|---|---|---|---|
| `f72d28334` | 2026-11-14T12:30:47Z | ajoute le fichier, lignes du scellement et du constat d'absence de l'étape B | oui |
| `ff24998f8` | 2026-11-16T12:57:58Z | ajoute une première ligne `CODE-BBIS` | **non** (branches `donnees/t07-etape-b-bis-v1`, `prep/t07bbis-code-v1`) |
| `31fa8ac60` | 2026-11-16T12:59:01Z | ajoute une ligne `GO-BBIS` datée `2026-11-16T12:58:51Z`, chemin `registres/go-extraits/GO-BBIS-v1.md`, empreinte `33f38e67…` | **non** (mêmes branches) |
| `c098fb512` | 2026-11-17T11:07:47Z | ajoute **ensemble** la ligne `CODE-BBIS` de la fiche remplaçante et la ligne `GO-BBIS` actuelle (lignes 6 et 7), sur un registre qui ne portait alors que les deux lignes du 14 novembre | oui |
| `06c883281` | 2026-11-17T11:14:06Z | insère la ligne `CODE-BBIS` de la première fiche (l. 5) ; message : « CODE-BBIS v1 (…) restaurée de l'historique et inscrite au registre propre à sa date d'origine (2026-11-16T12:57:27Z) » | oui |
| `9e90e525f` | 2026-11-18T19:43:48Z | ajoute la ligne des scores | oui pour la tête de travail ; postérieur à la course |

Ce que cela dit, sans plus :
- Sur la lignée de `main`, l'accord de calcul et la fiche remplaçante sont entrés par **un seul commit**, avec une seule heure écrite pour les deux. Il n'y a jamais eu, sur cette lignée, d'instant où `GO-BBIS` était inscrite sans la fiche remplaçante.
- La ligne `GO-BBIS` du 16 novembre n'existe que sur une autre lignée. Son extrait d'accord a la même empreinte (`33f38e67…`) que celui de la ligne actuelle : c'est le même texte d'accord, sous un autre chemin et une autre date.
- La ligne de la première fiche a été **insérée après coup** (commit postérieur à celui de la fiche remplaçante, date écrite antérieure) : le registre propre n'a pas été tenu en « lignes ajoutées, jamais réécrites » au sens strict sur la lignée de `main`. C'est un second écart, voisin, à déclarer quel que soit ton choix.
- Tout cela précède la course : `c098fb512` et `06c883281` sont des ancêtres du commit de la course ; le registre lu sur la machine portait déjà ces cinq lignes.

### 3.5 Pourquoi la marche de la course n'avait pas ce contrôle

- La garde d'entrée de la marche (`src/controle_ia/t07bbis/marche_v4.py`, fonction `gardes_d_entree`, l. 205-222) lit les lignes par `lecture_v3.lire_lignes` (l. 216-217 : présence, forme, deux lignes `CODE-BBIS` au plus, la seconde strictement postérieure à la première), vérifie les sceaux et la fiche. Elle n'appelle pas `exiger_ordre_propre`.
- Dans tout le code, `exiger_ordre_propre` n'est appelée que par les modules de lecture (`lecture_v1.py` l. 1069, `lecture_v2.py` l. 1136, `lecture_v3.py` l. 1246).
- La garde de création (`src/controle_ia/t07bbis/registre_bbis_v2.py`, `exiger_creation`, l. 394 et suivantes) compte deux lignes `CODE-BBIS` (l. 410) et ne compare pas leurs dates à celle de `GO-BBIS`. La garde d'écriture (`ajouter_ligne_propre`, l. 111) exige seulement que `GO-BBIS` soit présente quand la seconde ligne `CODE-BBIS` s'ajoute.
- L'ordre strict n'a donc été éprouvé sur le registre réel par aucune garde avant la lecture ; les essais le couvrent sur des registres jouets (`tests/test_t07bbis_second_addendum_v1.py`, l. 297-315).

## 4. Options

### (a) La garde refuse telle quelle : « non lue » est l'issue

- **Ce que c'est** : on applique la lettre. Le module en vigueur est lancé une fois, sa garde refuse, il écrit et scelle le fichier de lecture avec la phrase gelée « Étape B bis non lue : garde refusée (…) », sans ouvrir aucun score ; le verdict la recopie.
- **Texte** : aucun texte neuf ; la ligne I0 du texte scellé (l. 143) le prévoit. **Code** : aucun.
- **Avantage** : aucun écart, aucune lecture « arrangée » après la course ; rapide.
- **Inconvénient** : une course payée, menée au bout et jamais lue, pour une heure d'inscription ; le billet sort sans cette étape ; relire plus tard les mêmes scores demanderait de toute façon un texte neuf scellé avant lecture, donc l'option (b) en plus tardif et sous un jour moins net (une issue « non lue » déjà scellée).

### (b) Un quatrième addendum d'écart déclaré, scellé et contre-lu avant toute lecture

- **Ce que c'est** : un addendum qui remplace, dans SA-11 (et, s'il le faut, dans le « ajoutée après `GO-BBIS` » de SA-5), « strictement après `GO-BBIS` » par une lecture écrite : la fiche remplaçante est dans l'ordre si sa date est postérieure **ou égale** à celle de `GO-BBIS` **et** si les deux lignes ont été ajoutées par le même commit ou si le commit de `GO-BBIS` est un ancêtre de celui de la fiche — preuve par les commits, inscrite à part avant la lecture. Tout le reste de l'ordre reste strict (scellement, première fiche, scores).
- **Ce qu'il doit déclarer** : l'égalité à la seconde et le commit commun `c098fb512` ; l'insertion après coup de la ligne de la première fiche (`06c883281`) et l'existence de la ligne `GO-BBIS` du 16 novembre sur une autre lignée (§ 3.4) ; l'antériorité de l'écart sur toute lecture (aucun score ouvert, § 6) ; ce qu'il ne change pas (hypothèses, métrique, seuils, critères gelés, liste « Jamais », graines, entropie).
- **Texte** : addendum sous `prereg/`, contre-lu par un sous-agent neuf (R2), scellé, ligne `ADDENDUM-ECART-4-BBIS` au registre voisin `registres/t07-etape-b-bis-v1-addenda-v1.md` (pas au registre propre, qui n'admet que huit clés), ton mot inscrit à `registres/go.md`. Le verdict devra citer quatre lignes d'addenda et porter une réserve nommée.
- **Code** : un module de lecture sous un nom neuf (`lecture_v4.py`, R12), égal à la v3 hors la fonction d'ordre, avec ses épreuves (cas sain : même seconde et même commit ; artefacts : fiche remplaçante antérieure à l'accord, commit de l'accord non ancêtre), contre-lu. **Il ne peut pas entrer par la fiche de code** : une troisième ligne `CODE-BBIS` est interdite (« jamais une troisième », SA-5 ; troisième addendum, l. 138-141). Il serait donc rattaché par son empreinte écrite dans l'addendum, comme le troisième addendum l'a fait pour la chaîne de lancement (son point TA-2).
- **Avantage** : la lecture a lieu, sur le plan scellé, sans qu'aucun critère de lecture ne bouge ; l'écart est borné à une comparaison de dates, décidé à l'aveugle, et prouvable par l'histoire git.
- **Inconvénient** : un écart à la garde, décidé après la course (quatrième addendum de cette étape) ; un module de lecture hors de la fiche de code ; un jour ou deux de rédaction, de code et de contre-lecture avant le 22 novembre ; c'est aussi l'option « commode », à tenir pour suspecte par symétrie (R4) même si personne ne sait ce que la lecture dira.

### (c) Corriger le registre propre pour que le code en vigueur passe — exclue par les textes

- Changer la date d'une des deux lignes, ou retirer et réinscrire une ligne, c'est réécrire : interdit (« lignes ajoutées, jamais réécrites », texte scellé, l. 222).
- Ajouter une troisième ligne `CODE-BBIS` plus tardive est interdit (« jamais une troisième », SA-5), et le code la refuse ; ajouter une seconde ligne `GO-BBIS` est refusé par `lire_lignes` (une ligne par clé, hors `CODE-BBIS`).
- Je ne la propose donc pas ; je l'écris pour que personne ne la tente.

### Ce que la liste d'arrêt en dit

- Aucune ligne de la liste d'arrêt du texte scellé ne nomme l'ordre entre `GO-BBIS` et la fiche remplaçante ; c'est SA-5, qui étend la ligne du contrôle carte-processeur, qui porte « ajoutée après `GO-BBIS` […] jamais une troisième ».
- La ligne 180 (« Changement d'une cellule, d'un réglage de la grille, des plis, d'un adversaire, d'un niveau ou d'un seuil après la lecture de toute sortie […] : lecture invalide, version neuve ») n'est pas touchée par (b) : rien de cela ne change, et aucune sortie de cette course n'a été lue.
- La liste d'arrêt ne prévoit pas qu'un refus de garde dû au registre se corrige et se rejoue : c'est pourquoi (b) demande ton mot et un texte scellé, et non une simple relance.

## 5. Recommandation et confiance

**Option (b)**, confiance 0,6.

- Pour : la règle d'ordre sert à prouver que l'accord de calcul précède le code qui part ; l'histoire git le montre mieux que deux dates égales (un même commit, ancêtre du commit de la course) ; rien n'a été lu, donc l'écart ne peut pas avoir été choisi d'après un résultat ; l'option (a) ne ferait que repousser la même question.
- Contre, et ce qui me retient à 0,6 : c'est un quatrième écart sur cette étape ; le registre propre montre une insertion après coup, qui affaiblit la confiance dans ses dates et que le verdict devra porter en réserve ; un module de lecture hors de la fiche de code est un précédent de plus.
- Si tu préfères la lettre, (a) est propre et ne demande rien.

Pas de défaut sous 48 heures : écart à un préenregistrement scellé, c'est ton nœud. D'ici ton mot, rien n'est lancé.

## 6. Ce que personne n'a lu, et les réserves

- **Aucune mesure lue.** Ni la session de la course, ni la conductrice, ni moi n'avons ouvert un fichier de scores, de sondes ou de relecture de cette course, ni le verdict ou le fichier de lecture de l'étape B. Le module de lecture n'a jamais été lancé sur les données réelles. Les fichiers de la branche des sorties n'ont été vus que par leurs noms, leurs tailles et leurs commits.
- **Pour cette note**, je n'ai rien exécuté : lecture des textes, du registre propre, du code, et de l'histoire git de ces fichiers.
- **Réserve 1** : le refus cité au § 3.3 et le tableau du § 3.4 viennent de mes relevés de préparation (fonction d'ordre jouée sur le seul registre propre ; `git log` et `git merge-base` par les noms). Ils n'ont pas été contre-lus.
- **Réserve 2** : je n'ai pas lu `registres/decisions.md`, `registres/etat.md` ni les passations (cloisonnement) : la raison pour laquelle les lignes du 16 novembre ont disparu de la lignée de `main` puis la première fiche a été remise ne m'est connue que par les deux messages de commit cités.
- **Réserve 3** : la commande de lecture n'est pas écrite (arrêt sur un refus du classifieur pendant l'essai d'un brouillon) ; d'autres points ouverts de la préparation restent à trancher par la conductrice, sans rapport avec ce nœud.
- **Réserve 4** : je n'ai pas vérifié si d'autres comparaisons de la garde (sceaux, chemins, antériorité à l'ouverture) refuseraient aussi sur l'arbre de lecture complet ; ce nœud ne couvre que l'ordre des lignes.
