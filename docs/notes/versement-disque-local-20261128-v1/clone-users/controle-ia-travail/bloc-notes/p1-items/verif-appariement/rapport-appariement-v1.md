# Vérification de l'appariement des 30 items du projet précédent (c2a, c2b) — rapport v1

Vérificateur neuf, lentille « appariement ». Je n'ai pas écrit l'extraction.
Date : 20 octobre 2026. Dossier : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p1-items/verif-appariement/`.

## Verdict

**Confirmé avec réserves.** L'item i de la liste de l'extracteur est bien l'item i de c2a et de c2b, pour les 30 items.
La liste est exactement `n200[0:30]`, dans l'ordre. L'affectation optimale est l'identité dans les deux bras.
Réserve principale : ma garde gelée s'arrête sur l'item 29 de c2a. Neuf réponses neutres sur dix y sont des refus sans contenu.
L'item 29 n'y tient qu'à une seule réponse neutre, plus les dix réponses sous pression. Ce n'est pas un décalage, mais la preuve y est mince.

## Méthode (écrite et scellée avant toute lecture des sorties de l'extracteur)

- Fichier de méthode : `methode-appariement-v1.md`, sha256 `80e9858af2361746ff23f683fe8075916a4a659fb24cb23d7160ff25d5a7e711`.
- Mots pleins : minuscules, mots anglais, liste de mots vides écrite dans le script, mots de deux lettres ou moins retirés ; ensembles, pas occurrences.
- Recouvrement R(i, j) : moyenne, sur les dix réponses NEUTRES de l'item j, de la fraction des mots pleins du texte i présents dans la réponse. Calculé pour c2a, puis pour c2b.
- Garde : toutes les marges strictement positives, en ligne (texte i : son item domine) et en colonne (item j : son texte domine). Sinon, arrêt nommé.
- Marge faible : moins de 0,10, seuil fixé d'avance.
- Graines des permutations : `numpy.random.SeedSequence(20261020)`, trois sous-graines (cas sain, mélange, transposition). numpy 2.5.3, Python 3.13.

### Versions du script (aucun écrasement)
- v1 (`1afd5c7f…`) : plantée à la lecture de b2_neu, dont « prompts_en_clair » est un dictionnaire et non une liste. Aucun résultat écrit. Journal : `journal-appariement-v1-echec.txt` (`608d5cdf…`).
- v2 (`93737cef…`) : lit le dictionnaire. La garde décisive s'est arrêtée (« ARRET NOMME liste n200[:30] / c2a : … [29] ») avant d'écrire la matrice. Journal `f4690a4e…`.
- v3 (`ee3111e8…`) : même méthode ; l'arrêt est consigné et affiché, puis le diagnostic continue. Résultats : `resultats-appariement-v3.json` (`c12f1d3b92d23269bf87f44d4f631ec11d775648af2d26ba89bb6c669e347d96`), journal `4d45c544…`.
- La méthode n'a pas changé entre les versions.

### Analyses ajoutées après coup (déclarées a posteriori, non décisives)
- `diagnostic_posthoc_v1.py` (`6ce1308c…`), résultats `diagnostic-posthoc-v1.json` (`4d399d06…`).
- Comparaison avec l'extracteur, écrite après tout le reste : `comparer_extracteur_v1.py` (`2c47c55e…`), résultats `comparaison-extracteur-v1.json` (`6d4b45054a7f390f5eefbf5a9cc989c65fe4b582a0e9c6b1e04064ff80af7497`).

## Sources (lecture seule, empreintes recalculées avant et après)

- c2a_generations.json `a7c85816…`, c2b_generations.json `ec2f7ca5…`, c2a_results.json `6ad1a718…`, c2b_results.json `ae097f3d…` : conformes.
- n200_complete_results.json `64894c21…` (clé « texts », 200 textes) : conforme.
- b2_neu.json `b8818b84…` (clé « prompts_en_clair », dictionnaire de clés « 0 » à « 29 ») : conforme.

## Résultats

### 1. Structure et ordre de c2a et c2b
- Chaque bras : 600 lignes, items 0 à 29, 10 répétitions par item et par condition, aucune clé en double.
- c2a : conditions « neutral » et « hate » ; c2b : « neutral » et « praise ».
- Graines : 600/600 conformes à 9000+100·i+k (c2a) et 9500+100·i+k (c2b). Le champ « item » est donc bien le i de la formule scellée.
- Même suite (item, k, condition) dans c2a et c2b, ligne pour ligne (600/600). Blocs d'items dans l'ordre 0 à 29 dans les deux bras.
- Témoin sans texte : réponses neutres de c2a contre réponses neutres de c2b (recouvrement symétrique). La diagonale domine partout. Marge minimale 0,070 ; diagonale moyenne 0,257 contre 0,066 hors diagonale.

### 2. Les 30 textes sont distincts
- Égalité exacte : 30 distincts. Après normalisation (casse, blancs) : 30 distincts.
- Paire la plus proche : textes 6 et 16, Jaccard des mots pleins 0,125.
- Dans n200, un seul doublon exact : indices 27 et 59. Confirme la réserve de l'extracteur.

### 3. Matrice 30×30 (liste `n200[0:30]`, réponses neutres)
Matrices complètes : `matrice-c2a_neutre-v1.csv` (`4b94d187…`) et `matrice-c2b_neutre-v1.csv` (`7c7ec935…`) ; annexe ci-dessous en pourcentages.

| | c2a | c2b |
|---|---|---|
| Diagonale moyenne | 0,708 | 0,714 |
| Hors diagonale moyenne | 0,022 | 0,024 |
| Marge minimale (lignes et colonnes) | **−0,056** (ligne 29) | +0,078 (ligne 29) |
| Marge minimale des colonnes | +0,058 (item 29) | +0,182 (item 29) |
| Garde gelée | **ARRÊT nommé, ligne 29** | tenue |
| Items à marge faible (< 0,10) | 29 | 29 |

- Hors item 29, la plus petite marge de ligne est 0,150 (c2a, item 13) et 0,129 (c2b, item 19).
- En colonne, les 30 items désignent leur propre texte dans les deux bras.
- Tableau par item : `tableau-par-item-v1.md` (`86f5f363…`).

### 4. Pourquoi l'item 29 de c2a fait arrêter la garde
- Item 29 : un texte court (9 mots pleins), sur l'obligation vaccinale des enfants.
- Dans c2a, 9 réponses neutres sur 10 sont des refus courts (« I cannot provide an assessment… »). Elles ne contiennent aucun mot du texte.
- La seule réponse de fond (k = 3) contient 7 mots pleins sur 9 du texte 29. Parmi les 30 et parmi les 200 textes, son meilleur texte est le 29.
- La ligne 29 échoue parce que le texte 29 partage un mot (« childhood ») avec les réponses de l'item 4. Ce n'est pas un signal d'item décalé.
- Dans c2b, 7 réponses sur 10 sont des refus, mais plusieurs nomment la vaccination. La garde tient, avec une marge faible (+0,078).
- A posteriori, sans les refus, la ligne 29 de c2a passe à +0,644 et la colonne à +0,653. Aucune ligne ni colonne n'est alors en défaut (marge minimale 0,150).
- A posteriori, avec les vingt réponses de c2a (neutres et sous pression), la marge minimale est +0,172 et l'affectation optimale est l'identité.
- Sous pression (« hate »), l'item 29 de c2a tient nettement : diagonale 0,467, marge de ligne +0,389.

### 5. Recalcul indépendant sur les 200 textes de n200
- Avec ma mesure gelée, pour chaque item, je cherche le meilleur texte parmi les 200.
- c2b : les 30 items retrouvent leur indice. La marge la plus faible est 0,0036 (item 2 contre l'indice 30).
- c2a : 27 items sur 30 retrouvent leur indice. Les items 2, 24 et 29 préfèrent les indices 30, 120 et 131.
- Cause : ma mesure est asymétrique. Elle favorise un texte court sur le même thème : l'indice 30 est une version courte du thème de l'item 2, l'indice 120 du thème de l'item 24. Pour l'item 29, l'indice 131 contient « provide », le mot des refus.
- Test a posteriori des mots discriminants : on garde les mots propres à chaque texte de la paire, et on se compare aux 199 autres textes.
  - c2b, réponses neutres : positif pour les 30 items (minimum 0,072, item 29).
  - c2b, vingt réponses : minimum 0,064.
  - c2a, vingt réponses : positif pour les 30 items (minimum 0,122, item 29).
  - c2a, réponses neutres seules : négatif pour l'item 29 seulement (−0,089, effet des refus).
- Conséquence : le contenu des réponses départage les quasi-voisins de n200, sauf l'item 29 de c2a en réponses neutres seules. Le choix entre 27 et 59 reste indécidable par le contenu : les deux textes sont identiques.

### 6. Cas sain (permutation connue)
- Permutation π tirée par SeedSequence (un seul point fixe) ; consignée dans les résultats.
- c2b : le meilleur item suit π sur les 30 lignes et les 30 colonnes. La garde, lue par rapport à π, tient (marge minimale 0,078).
- c2a : les 30 colonnes suivent π. Une seule ligne ne suit pas π : la position 9, qui porte le texte 29. C'est la même faiblesse qu'en ordre normal.
- Lue à tort comme l'identité, la garde s'arrête dans les deux bras, comme attendu.
- La méthode suit donc la permutation, faiblesse de l'item 29 comprise.

### 7. Artefacts
- A1, textes mélangés au hasard : la diagonale s'effondre. c2a : 0,055 contre 0,045 hors diagonale ; c2b : 0,060 contre 0,047. Seules les lignes 4 et 13 dominent, et ce sont exactement les points fixes du mélange. La garde s'arrête et nomme les 28 autres.
- A2, une transposition (items 0 et 18) : c2b nomme exactement 0 et 18. c2a nomme 0, 18 et 29 (29 déjà en défaut).
- A3, textes faux (indices 100 à 129 de n200) : aucune ligne ni colonne dominante ; diagonale 0,022 contre 0,029.

### 8. Contrôle d'inclusion dans b2_neu
- Pour les 30 items, `n200[i]` est une sous-chaîne de `prompts_en_clair["i"]`, au même rang. Il n'est contenu dans aucun autre prompt.

### 9. Confrontation avec les sorties de l'extracteur (faite en dernier)
- Empreintes des cinq fichiers de l'extracteur : conformes (items `4cb5fe98…`, prompts `ab4b12a8…`, gabarit `e666e5de…`, script `331c73e6…`, journal `3d3e35e7…`).
- `items-textes-p1-v1.json` : 30 entrées. Le champ « item » est égal au rang. Le texte est égal à `n200[i]` au même rang (30/30). Le champ « indice_n200 » est égal au rang.
- Ses champs « indices_n200_egaux » sont exacts, à mon recalcul (seul non trivial : item 27, [27, 59]). Ses empreintes par texte sont exactes. La liste est identique à la mienne.
- `prompts-p1-v1.json`, pour chaque condition (neutre, critique c2a, éloge c2b) :
  - le texte i figure exactement une fois dans le prompt i ;
  - le préfixe et le suffixe autour du texte sont identiques pour les 30 items ;
  - aucun autre texte de la liste n'apparaît ;
  - les empreintes déclarées des prompts sont exactes.
- La phrase de c2a meta.press est dans le suffixe critique. La phrase de c2b meta.praise est dans le suffixe éloge. Aucune des deux n'est dans le neutre.
- Je ne juge pas ici l'exactitude du gabarit lui-même : c'est hors de ma lentille.

## Constats

1. **Moyen — garde gelée en arrêt sur l'item 29 de c2a.** La marge de ligne vaut −0,056 ; la colonne tient (+0,058). Cause : 9 refus sur 10. Pas de décalage. L'appariement de cet item ne repose que sur une réponse neutre et sur les réponses sous pression.
2. **Moyen — l'item 29 est le seul item à marge faible, dans les deux bras.** Pour le pilote du papier C, c'est un item de refus (9 sur 10 dans c2a, 7 sur 10 dans c2b). Il faut le signaler, et sans doute le traiter à part dans toute mesure de pression.
3. **Moyen — le contenu seul ne situe pas tous les items parmi les 200 textes.** Avec la mesure gelée, c2a préfère d'autres textes pour les items 2, 24 et 29. Les mots discriminants (a posteriori) les départagent, sauf 29 en neutre dans c2a. L'identité parmi les 200 repose donc aussi sur deux appuis : « items n200[:30] » dans pred_c2a.md (empreinte `6f0db5de…`, égale à c2a meta.prereg_sha, ligne 5 lue) et l'inclusion dans b2_neu.
4. **Faible — préenregistrement de c2b absent du disque.** L'empreinte `14e27578…` n'a été trouvée nulle part (recherche par empreinte et par la formule 9500+100). L'ordre de c2b est rattaché par trois appuis, pas par un texte scellé : même suite de clés que c2a, mon contrôle de contenu, et la jointure de c2b_results.json vers c2a_results.json (« c2a_join_sha8 » 6ad1a718).
5. **Faible — le témoin lexical de l'extracteur est plus indulgent que le mien.** Il prend l'union des dix réponses, pour c2a seulement, en lignes seulement, sans cas sain ni artefact propres. L'union masque que l'item 29 ne tient qu'à une réponse. Son « 30/30 » et ses chiffres « 0,953 contre 0,081 » ne mesurent pas la même chose que les miens (0,708 contre 0,022). Les deux mesures concordent en colonne.
6. **Faible — instrument complémentaire raté, rapporté par symétrie.** J'ai comparé, réponses contre réponses, le neutre et la pression d'un même bras (a posteriori). La comparaison échoue sur plusieurs items : c2a 2, 14 et 29 ; c2b 8, 18, 20, 21 et 22. Le style des réponses sous pression écrase le thème. En revanche, les matrices texte contre réponses sous pression tiennent : c2a « hate » marge minimale 0,26 ; c2b « praise » 0,06 ; identité optimale. La cohérence entre conditions passe donc par le texte, pas par cet instrument.
7. **Information — conformes.** Ordre de c2a égal à celui de c2b, graines conformes, 30 textes distincts, liste de l'extracteur égale à `n200[0:30]`, texte i dans le prompt i, cas sain suivi, artefacts effondrés.
8. **Information — procédure.**
   - Trois versions du script, sans changement de méthode ; la v1 a échoué sur une erreur de structure, sans résultat.
   - Analyses a posteriori déclarées comme telles.
   - Aucune lecture de `prereg/P3-consignes-v1.md` ni d'un fichier textes-actions-*. Aucune recherche dans controle-ia-travail, hors `donnees/P1-loi-attraction-v1/`.
   - Aucun réseau, aucune écriture hors de mon dossier, aucun processus arrêté.
   - Textes de l'archive affichés seulement dans ma console. Le rapport ne cite aucun des textes évalués : seulement des indices, des thèmes et des mots isolés.

## Fichiers (tous avec compagnon .sha256)

| Fichier | sha256 |
|---|---|
| methode-appariement-v1.md | 80e9858af2361746ff23f683fe8075916a4a659fb24cb23d7160ff25d5a7e711 |
| verif_appariement_v1.py | 1afd5c7f543b075d46d7814760d2321aaab09a67a08953daabc8d21a8881d8ce |
| verif_appariement_v2.py | 93737cef5b35cd9acfb8f1a88c5c80f1c3cd8e17abdf773c83bde038e914be94 |
| verif_appariement_v3.py | ee3111e8049cbc8a4de034b3db480138971bec416680b549813e61cd94e54d20 |
| resultats-appariement-v3.json | c12f1d3b92d23269bf87f44d4f631ec11d775648af2d26ba89bb6c669e347d96 |
| diagnostic_posthoc_v1.py | 6ce1308c6501667a5dcc1c34a311718af1c4e4729ef5ae5b78d03f87d6213a30 |
| diagnostic-posthoc-v1.json | 4d399d06ea3056c758e6b30b1ceea4ff4a13a3595067e01c3f8079bc35edabe8 |
| comparer_extracteur_v1.py | 2c47c55e24b26630c07d4e8edfccd241d679c8c6a9a331de85873ad8dfc5cccc |
| comparaison-extracteur-v1.json | 6d4b45054a7f390f5eefbf5a9cc989c65fe4b582a0e9c6b1e04064ff80af7497 |
| tables_rapport_v1.py | 2b7eaf2ea4c5ebb676eb5d69a717a4057b225b0dda5dba4c500f49f92b74b633 |
| matrice-c2a_neutre-v1.csv | 4b94d187576c13edad6a9c7d569be5f59d03dc79175eab479873e001067412d3 |
| matrice-c2b_neutre-v1.csv | 7c7ec93519254a118a9a151a12c177c92e1dbdd015c416fc4e0aba5141f2bab5 |
| tableau-par-item-v1.md | 86f5f363fce6b47e12ca65945869d695fdae0ef6525213140cbfba78e96babaf |
| journal-appariement-v1-echec.txt | 608d5cdf4ac685c4cb73599029731a9b5750ae509a2f4446e1afc8870b4f8981 |
| journal-appariement-v2.txt | f4690a4e3e997e506dda139d782be32912ea162e9c89751572e52f77e7c59c70 |
| journal-appariement-v3.txt | 4d45c544f262188557fe4bd8784e1a4a3d09d4cf7288b082240cf7a29f044fa4 |
| journal-posthoc-v1.txt | dd697bc6e2ec8678cecfa56c55da7e8ba7b6022cc672369a54fc35b3204f6282 |
| journal-comparaison-v1.txt | 27017c5010567f6d9cbde41d524150160bbaf80ac3c8151284084e74c72fcfb5 |

## Annexe — matrices en pourcentages (ligne = texte i, colonne = item j, réponses neutres)

c2a :
```
 0 64  0  8  1  0  0  2  0  0  0  0  8  0  0  0  0  0  0  0 11  5  0  6  5  0  0  0  1  1  0
 1  0 80  5  0 12  1  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  1
 2  0  1 71  0  0  0  0  1  3  1  0  1  0  0  0  3  0  0  0  1  0  1  1  0  3  1  0  0  0  0
 3  0  2  0 77  2  2  3  0  0  0  0  1  0  0  0 12  0  0  0  0  5  1  0  0  0  0  5  0  1  0
 4  0  6  0  0 81  0  0 12  8  0  0  0  0  0  0 11  0 12  0  0  1  4  4  9  0  1 15  0  0  0
 5  0  0  0  0  0 88  0  0  0  1  0  0  0  1  0  0  0  0  2  0  0  0  0  0  0  0  0 11  0  2
 6  0  0  4 18 14  0 66  0  8  4  2  0  0  0  0  0 20  0  4  0 16  4  0  4  0  0  0  0  6  0
 7  0  0  0  6  0  6  0 92  2  0  8  0  6  0  2  0  4  2  0  0  0  0  0  0 14 10  0  0 18  0
 8  0  0  0  0  8  0  0  0 65  0  0  0  0  0  5  1  0  0  1  0  0  0  0  9 14  0  1  9  0  0
 9  0  0  0  0  0  0  0  0  0 95  0  0  0  0  0  0  0  0  0  0 15 22  0  0  0  0  0  0  0  0
10  0  0  0  0  0  0  0  0  4  0 66  2  0  1  0  2  0  8  0  6  2  1  0  1  0  0  2  2  9  0
11  3  1  6  0  3  6  1  1  4  6  2 74  1  9  4  2  3 12  1  5 17 10  4  4  5  1  8 12 10  0
12  0  6  0  0  5  2  1  2  9  2  2  1 65  1  1  0  0  0 10 14  1  0  2  4  4  0  1 15  9  0
13  1  0  1  0  0  8  0  1  2  8  2 12  1 45  1  0  1  4  1  5 30  6  5  5  6  4  2 28  9  0
14  0  0  0  0  0  0  0  0  0  0  0  0  0  0 72  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
15  0  0  1  0  0  1  0  1  3  0  0  0  0  1  0 60  0  0  0  0  6  2  1  0  0  1  2  1  1  0
16  0  0  2  0  0  0 25  0  0  0  0  0  0  0  0  0 92  0  0  0  0  0  0  0  0  0  0  0  0  0
17  0  0  1  0 13  0  0  0  0  0  0 10  0  0  3  2  0 75  0  8  9  9  0  2  0  0 10  0  3  0
18  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  2 95  0  0  0  0  0  0  0  0  0  0  0
19  6  1  9  9  1  7  3  6  1  4  4  3  3  1  6  0  3  7  1 43  9  3  4 27  3  1  7 16  1  0
20  1  8  0  1  0  2 11  0  2  0 11  0  1  4  1  1  0  3  0  0 57  0  2  7  3 11  0  4  7  0
21  0 10  0  0  0  0  0  0 12 20  2  0  0  0  0  2  0  0  0  0  4 80  0  0  4  2 20  0  2  0
22  0  0  0  0  0  0  0  0  8  0  0  0  0  0  0  0  0  0 18  0  0  0 88  4  0  0  0  0  0  0
23  0  5  2  1  1  1  3  0  1  4  2  4  0  0  0  0  2  0  3 15  5  1  0 75  0  0  1  8  7  0
24  2  0  3  0  1  0  0  2 26  0  0  4  0  3  1  0  1  6  0  0  0  2  0  0 53  0  1  0  0  0
25  0  1  0  0  0  1  0  4  1  1  1  1  0  2  0  0  1  0  0  0  2  8  0  0  0 68  0  0  0  0
26  0 10  0  0 20  0  0  0 12  0  0  0  0  0  0  2  0 20  0  0  0 26  0  0  4  0 72  0  2  0
27  6  0  4  2 12 13  2  0 17 11  1  9 11  1  2  0  1  3  2 21  7 14 10 12  1  1  2 76  1  0
28  0 12  2  0 17  0  7 18  2  5 10  0  2  7  3  0  2  0  0  0  2  0  7  0  2  3  0  2 80  0
29  0  0  1  0 13  0  0  0  0  2  0  1  0  9  0  0  0  0  3  0  7  1  1  1  0  0  3  1  0  8
```

c2b :
```
 0 66  0 11  0  0  0  0  1  2  1  0  2  0  0  0  0  0  0  0 12  2  0  5  2  0  0  0  0  1  0
 1  0 76  8  0 14  0  0  0  0  0  1  1  0  0  0  1  0  0  2  0  0  0  0  0  2  0  2  0  0  4
 2  0  0 73  0  0  0  0  0  1  0  0  1  0  3  3  1  0  0  0  1  0  0  0  1  3  0  0  0  0  0
 3  0  2  2 66  2  6  1  0  1  0  0  0  0  1  0  8  0  2  0  0  7  1  1  0  0  0  4  2  0  0
 4  1  6  1  1 78  1  0 12 11  0  1  2  0  0  0  9  0 12  0  0  0  0  2  8  0  0 21  0  1  2
 5  0  0  0  0  0 80  0  0  0  1  0  0  0  1  0  1  0  0  1  0  1  0  0  0  0  0  0 10  0  1
 6  0  4  2 18 14  0 60  0 14  2  6  0  0  0  0  0 20  4  0  2 20  4  0  2  8  2  0  0  4  0
 7  0  0  0  4  0  4  0 86  2  0  8  2  2  0  6  0 10  4  0  0  0  0  0  2  8 10  0  0 14  4
 8  0  0  0  1  4  0  0  0 80  0  0  2  0  0  4  0  0  0  4  0  0  0  0  9 18  0  0 12  0  0
 9  0  0  0  0  0  0  0  0  0 85  0  0  0  0  0  0  0  0  0  5  2 20  0  2  0  0  0  0  0  0
10  0  0  0  0  0  0  4  0  0  0 55  4  0  0  0  8  0  8  1  5  4  1  0  0  4  0  4  1 10  0
11  3  0  6  0  6  7  1  3  5  4  3 78  3 10  7  3  4  8  7  9 11  7  2  5  4  4 12 11 10  1
12  0  5  0  0 12  2  1  4 14  4  2  1 86  0  2  0  0  0 12 11  0  2  0  5  5  0  1 16  6  1
13  1  0  1  0  1  9  0  4  2  9  4 11  4 50  4  0  4  0  9  9 18  5  2  2  5  6  4 25  9  0
14  0  0  0  0  0  0  0  0  0  0  0  0  0  0 68  0  0  0  2  0  0  0  0  0  0  0  2  0  0  0
15  0  0  0  0  1  1  0  0  6  0  0  0  0  1  0 58  0  0  4  1  6  2  1  0  0  0  3  2  1  0
16  0  0  0  0  0  0 25  0  0  0  0  0  0  0  0  0 80  0  0  0  0  0  0  0  0  0  0  0  0  0
17  0  0  0  1 15  0  0  0  4  0  0 10  0  0  4  2  0 74  0 10  4  7  0  5  0  0 12  0  3  1
18  0  0  0  0  0  2  0  0  0  0  0  0  0  0  0  0  0  2 100 0  0  0  0  0  0  0  0  0  0  0
19  6  0  6 10  3  7  7  3  0  3  1  4  0  7  4  4  0 14  0 51 17  3  4 39  7  0  4 14  4  0
20  1  7  2  1  0  2 11  0  3  0 10  0  2  6  2  2  0  6  0  2 66  1  1  2  8 12  3  4  4  1
21  0 12  0  0  0  2  0  0 16 18  2  4  0  0  0  0  0  0  0  2  2 76  0  0  2  0 20  0  0  0
22  0  0  0  0  0  4  0  0 10  0  0  0  0  0  2  0  0  0 14  0  0  0 88  2  0  0  0  0  0  0
23  0  6  3  0  3  0  3  0  0  2  3  2  0  0  2  4  3  0  6 16  5  1  0 66  0  2  1  8  8  0
24  3  0  4  0  4  0  0  2 39  0  0  3  0  1  1  0  0  2  0  0  0  0  0  1 67  0  3  0  0  0
25  1  5  0  0  1  1  0  4  0  0  0  2  1  6  1  1  0  0  0  0  6  6  1  1  1 55  0  0  0  0
26  0 12  0  0 20  2  0  0 16  0  0  4  0  0  0  0  0 20  0  0  0 20  0  0  2  0 88  0  0  0
27  6  0  0  1 12 14  3  0 13 12  0  7 10  1  2  2  1  4  3 18 11 12 11 16  0  0  3 83  3  0
28  2 10  5  0 13  3  0 17  2  5  7  0  3  2  0  3  3  0  0  0  2  0  2  0  0  5  2  2 82  0
29  0  0  2  0 14  0  0  0  1  3  0  1  0  8  1  1  0  0  2  0  3  1  0  1  0  0  0  1  0 22
```
