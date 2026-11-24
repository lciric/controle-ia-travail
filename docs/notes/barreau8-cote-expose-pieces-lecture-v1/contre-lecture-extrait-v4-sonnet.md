# Contre-lecture de l'extrait des états, côté moniteurs, v4 (Sonnet, contre-lecteur neuf)

**Verdict : autorisable après corrections** (aucun bloquant ; une correction d'essai majeure à faire, trois mineures facultatives).

Fichiers relus : `extrait_iib_etats_lectures_cote_moniteurs_v4.py` (219 lignes) et son essai (166 lignes), empreintes compagnes vérifiées OK. Les 18 essais passent. Diff v3 → v4 fait.

## Conformité aux exigences
- D-12 (forme fermée, contrôles à la réception) : construire() est identique à la v3 (même diff), mêmes quatre clés, même avertissement, mêmes treize états, mêmes vocabulaires. Conforme.
- RP-10 / additif 1 : nom de sortie imposé `etats-lectures-iib-v1.json` (l. 69, 201-202) ; refus d'écraser (l. 203-204 et ouverture "x" l. 207). Conforme. Note : RP-10 dit « fichier cité par ETATS-COURSE-IIB, même dossier » ; le dossier n'est pas contrôlé par le programme (D-12 nomme `docs/notes/barreau8-cote-moniteurs-entrees-v1/`) : c'est la réception qui contrôle, acceptable.
- Additif 2, D-17 (l. 266-267) : refus sans les trois lignes (l. 100-102), une seule par clé (l. 95-96), à quatre colonnes (regex l. 70), heures strictement croissantes dans l'ordre (l. 107) et passées (l. 105), chemins relatifs sans « .. » (l. 110), texte scellé à l'empreinte de la ligne (l. 112). Conforme.
- Contrôle T0 (spec l. 93) : racine des registres = parent du dossier `registres/` (l. 73-77), nom exact du registre ; textes pris sous cette racine (l. 112) et non sous `--racine` ; seules les lignes `| SCELLEMENT-` sont lues, une autre clé arrête (l. 93-94) ; empreintes de la section 5.1 : les trois codées l. 66-68 sont égales à celles de la spec et aux empreintes réelles des trois textes (sha256sum fait).
- Section 11 : les clés lues (phrase ; lecture_1.sha256 et .phrase ; jeux à 10 clés avec etat ; etat_par_unite.unites à 3 clés avec etat ; phrase) et les deux noms sont ceux que la spec garde. Conforme.
- Registre réel (`origin/main:registres/sondes-iib-v1.md`, 7 lignes de table) : essai rejoué avec le registre et les trois textes extraits de main : les trois scellements passent, les empreintes attendues égales ; la ligne SPEC-LECTURES-… est ignorée sans refus (ne commence pas par `| SCELLEMENT-`). Les lignes CODE-… et LIVRAISON-… aussi.
- Invariants v3 conservés : forme de sortie, vocabulaire, refus sans imprimer la valeur refusée dans les chemins de `_dans`, `exiger_run_id`, discordances. Rien d'autre de modifié dans construire/_lire/_dans.

## Remarques

### Bloquant
Aucune.

### Majeur
M1. Essai manquant pour la garde « chemin sans `..` » (l. 110). Mutation faite (suppression de `or ".." in Path(chemin).parts`) : les 18 essais passent encore. Le cas « absolu » seul est testé (essai l. 100-102). Or la spec (T0) liste « chemin absolu ou portant `..` » comme artefacts à refuser (R5 : chaque garde, cas sain et artefact). Correction : ajouter à `test_artefacts_scellements` un cas `"remonte"` qui remplace `| prereg/texte-1.md |` par `| prereg/../prereg/texte-1.md |` (même fichier, donc seule la garde « .. » peut refuser) et attend GardeArret.

### Mineur
m1. Heures égales non testées : la mutation `<=` → `<` (l. 107) survit. Ajouter un cas « egales » (heures[1] == heures[0]) ; la règle écrite est « strictement postérieure ». 
m2. L'écriture exclusive ("x", l. 207) n'est pas distinguée de "w" par les essais (mutation survit) : la garde exists() l. 203 la précède, donc la seule valeur de "x" est la course entre contrôle et écriture, non testable simplement. Acceptable ; au minimum un commentaire le dit. De plus, si `sceller` échoue après l'écriture (l. 209), un fichier sans compagnon reste et bloque toute relance (exists) : à signaler au ordre de lancement (nettoyage manuel nommé) ou à traiter par un try/except qui renomme/consigne.
m3. Message d'erreur `type(e).__name__ : e` (l. 211) : pour une `UnicodeDecodeError` (sous-classe de ValueError, attrapée) le message imprime l'octet fautif de la valeur refusée ; `JSONDecodeError` n'imprime que la position. Impact faible (octets, pas des mots du vocabulaire) mais contraire à l'esprit « valeur refusée non imprimée ». Correction : pour ValueError, n'imprimer que le nom du type (`print(... type(e).__name__ ...)` sans `e` quand `isinstance(e, ValueError)`).
m4. Changement de la ligne de succès (l. 213-214) et du préfixe d'erreur (nom du type ajouté) par rapport à la v3 : la docstring dit « rien d'autre ne change » ; c'est exact pour le fichier produit, pas pour la sortie texte. Si un script lit la ligne de succès, le dire ; sinon une phrase dans la docstring.
m5. Les lignes de scellement avec un espacement différent (`|  SCELLEMENT-…`, ou espace initial) ne commencent pas par `| SCELLEMENT-` et sont ignorées silencieusement (l. 87), alors que la spec les définit par la « première colonne ». Un doublon ainsi écrit passerait. Correction éventuelle : tester `re.match(r"^\s*\|\s*SCELLEMENT-", l)` puis laisser la regex stricte refuser (mal formée). Risque faible : le registre est en ajout seul.

## Gardes et essais (R5)
Mutations jouées sur le fichier (copie dans le bloc-notes) : ordre strict (survit, m1), nom de sortie (tué), "x" (survit, m2), doublon (tué), « .. » (survit, M1), futur (tué), filtre de préfixe (tué, 5 essais), racine des registres (tué). Cas sains présents pour chaque garde neuve (trois scellements jouet, registre réel de main, programme entier). Registre absent, mal formé, clé inconnue, empreinte attendue, nom de registre/dossier : couverts.

## Défauts de code
Pas de défaut bloquant. Chemins : registre/racine corrects, `--racine` n'est plus utilisé pour les textes (conforme). Erreurs du système (OSError, ValueError) rendues en refus code 1. Écriture : refus d'écraser ET "x" ; compagnon créé par `sceller` (qui refuse d'écraser une autre empreinte). Pas de repli silencieux, pas d'effet de bord avant les gardes (mkdir après construire).
