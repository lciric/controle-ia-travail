# Couples exacts de la vérification du brouillon 3 — sortie du programme (v1)

- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` : empreinte `525f338e7899e6a8f57b73fffef7f0eeef3d6a16eee0e7d6c2823cddb44c9e50` (égale à celle attendue)
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-decisions-lazar-v3.md` : empreinte `d28e92591a73cf5695f2105cf2b0893f1724e552f41d9f44f4cf8288bf6b1ec7` (égale à celle attendue)
- validateur sur le brouillon 3 tel quel : aucun problème

## Groupe « toujours »

### Couple V-M3a (constat V-M3) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
Elle rend des scores par action, **fermés** : aucune statistique d'adaptateur, aucune aire, aucun résumé n'est calculé sur l'instance ni dans ses journaux.
```

Après :

```text
Elle rend des scores par action, **fermés** : aucune statistique d'adaptateur tirée d'un score de sonde, aucune aire, aucun résumé n'est calculé sur l'instance ni écrit dans ses journaux ; seuls les produits P et les poussées le long de ĝ du point 8 (c), qui ne lisent aucun score de sonde, y sont calculés, par le programme figé, et écrits dans les seuls fichiers fermés.
```

### Couple V-M3b (constat V-M3) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
7. Toute statistique d'adaptateur, aire ou résumé de score calculé sur l'instance de lecture ou écrit dans un journal : lecture invalide, version neuve.
```

Après :

```text
7. Toute statistique d'adaptateur tirée d'un score de sonde, aire ou résumé de score calculé sur l'instance de lecture, ou toute grandeur d'un adaptateur (produits P et poussées compris) écrite dans un journal : lecture invalide, version neuve. Les produits P et les poussées le long de ĝ du point 8 (c), calculés par le programme figé et écrits dans les seuls fichiers fermés, n'en sont pas.
```

### Couple V-M2a (constat V-M2) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
*Produit* de deux adaptateurs : P(a, b) = moyenne, sur tous les jetons notés des 64 tâches, de δ_a(t)·δ_b(t).
```

Après :

```text
*Produit* de deux adaptateurs : P(a, b) = δ̄_a·δ̄_b, où δ̄_i est la moyenne de δ_i(t) sur tous les jetons notés des 64 tâches (produit des déplacements moyens : c'est la grandeur que simule le bloc N ; la moyenne par jeton des produits y ajouterait la structure par jeton commune à tous les adaptateurs, qui fausse l'instrument de E2a quand la force ne la multiplie pas : vérification du brouillon 3, mondes C21 et C22).
```

### Couple V-M1a (constat V-M1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
Le sur-saboteur sert d'instrument : sa divergence propre est indépendante de celles des deux autres, si bien que q_k compare ce que le jumeau et le saboteur portent de la part commune à leur famille, sans le biais d'un membre projeté sur lui-même.
```

Après :

```text
Le sur-saboteur sert d'instrument : si sa divergence propre est indépendante de celles des deux autres (hypothèse de travail, que ce plan ne vérifie pas), q_k compare ce que le jumeau et le saboteur portent de la part commune à leur famille, sans le biais d'un membre projeté sur lui-même. Une part de divergence commune au jumeau et au sur-saboteur, les deux membres édités aux mêmes jetons, ou une trace d'édition commune aux deux sens, gonfle P(jumeau, sur-saboteur), tire q_k vers 1 et laisse passer une force portée par la part propre à la famille (vérification du brouillon 3, mondes C14, C16 et C17).
```

### Couple V-M1b (constat V-M1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
| force de l'adaptateur (il a plus appris, sans direction propre) | fermée à la couche lue par l'épreuve à force égale (poussée égale le long de la direction commune des jumeaux d'apprentissage) ; ouverte ailleurs ; la seule norme égale ne la ferme pas (contre-lecture, constat B-1) |
```

Après :

```text
| force de l'adaptateur (il a plus appris, sans direction propre) | fermée à la couche lue par l'épreuve à poussée égale (E2a, poussée dans la famille ; E2b, poussée le long de la direction commune des jumeaux d'apprentissage), pour une force qui multiplie la part commune à la famille ou la direction commune à tous, et si les divergences propres du jumeau et du sur-saboteur sont indépendantes ; ouverte ailleurs ; la seule norme égale ne la ferme pas (contre-lecture, constat B-1) |
```

### Couple V-M4a (constat V-M4) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
L'intensité est mesurée sur les deux mesures demandées, et l'égalité de la norme du déplacement à la couche lue est **imposée** dans une des trois épreuves du mot.
```

Après :

```text
L'intensité est mesurée sur les deux mesures demandées ; l'une des trois épreuves du mot ramène après coup le saboteur et son jumeau à la même poussée, le long de ce que leur famille partage et le long de ce que tous les adaptateurs partagent (épreuve E2).
```

### Couple V-M4b (constat V-M4) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
bruits indépendants d'un membre à l'autre et d'une série à l'autre (nominale, à force égale), de même loi pour les trois membres
```

Après :

```text
bruits indépendants d'un membre à l'autre, de même loi pour les trois membres, plantés au niveau des scores par jeton (le programme y calcule lui-même les mises à l'échelle de E2a et de E2b)
```

### Couple V-M4c (constat V-M4) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
(textes honnêtes communs, scores fermés, intensités, facteurs c_i, poids des sondes, manifestes)
```

Après :

```text
(textes honnêtes communs, scores fermés par action et par jeton, produits P et poussées le long de ĝ, intensités, poids des sondes, manifestes ; les facteurs √q_k et √r_k sont calculés après l'ouverture)
```

### Couple V-M5a (constat V-M5) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
règle : « différence établie » au seul motif « force non écartée » dans 480 au moins, « sabotage » dans 10 au plus.
```

Après :

```text
règle : « différence établie » au seul motif « force non écartée » dans 480 au moins, « sabotage » dans 10 au plus. Un monde V9 de 500 : force sur la seule part propre à la famille (l'écart disparaît en E2a, non en E2b) ; même règle. Un monde V10 de 200 : dans chaque monde, deux familles à produit de E2a non positif, une à √q_k hors de [0,5 ; 2], deux à poussée de E2b non positive et une à √r_k hors de [0,5 ; 2], tirées au hasard ; règle : dans tous les mondes, familles présentes de E2a et de E2b, facteur c = 1 et motifs écrits exactement comme plantés, seuil pris au nombre de familles présentes de chaque demi-épreuve, règle du nœud 6 appliquée à E2a (sept familles présentes).
```

### Couple V-m1a (constat V-m1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
mêmes concepteurs, mêmes développeurs, même crédit, même semaine ; ce calendrier ne la compte pas.
```

Après :

```text
mêmes concepteurs, mêmes développeurs, même crédit, même semaine ; ordre tenu au paragraphe « La chaîne voisine, comptée » ci-dessus.
```

### Couple V-m2a (constat V-m2) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
`t06/cout.py`, `distiller_adaptateur` de `t06/lanceur.py` ; **à envelopper
```

Après :

```text
`t06/cout.py`, `distiller_adaptateur` de `t06/lanceur.py`, `t07bbis/apprentissage_carte_v1.py`, `harnais` ; **à envelopper
```

### Couple V-m2b (constat V-m2) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
interdit sur une instance de formation), `t07bbis/apprentissage_carte_v1.py`, `harnais` (liste reprise du brouillon 1 ;
```

Après :

```text
interdit sur une instance de formation) (liste reprise du brouillon 1 ;
```

### Couple V-m3a (constat V-m3) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
(une famille absente de E2 ou de E3 seulement ne manque qu'à celle-là)
```

Après :

```text
(une famille absente de E2a, de E2b ou de E3 seulement ne manque qu'à celle-là ; chaque demi-épreuve de E2 compte ses propres familles)
```

### Couple V-m3b (constat V-m3) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
« force non écartée » (E2 manque)
```

Après :

```text
« force non écartée » (E2a ou E2b manque ; le motif dit laquelle)
```

### Couple V-m4a (constat V-m4) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
`b5f/lecture/chemin`, `b5f/lecture/norme/taches`, `b5f/sonde/<nom>/<pli>`
```

Après :

```text
`b5f/lecture/chemin`, `b5f/sonde/<nom>/<pli>`
```

Validateur du dépôt sur la copie du brouillon 3 après le groupe « toujours » : aucun problème

## Groupe « voie i »

### Couple V-B1a (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
| trace de l'édition (nombres que le modèle n'aurait pas écrits) | fermée si elle est la même vers le haut et vers le bas : épreuve sur-saboteur contre jumeau ; **ouverte** si l'édition vers le haut laisse une autre trace que l'édition vers le bas |
```

Après :

```text
| trace de l'édition (nombres que le modèle n'aurait pas écrits) | fermée si elle est la même vers le haut et vers le bas : épreuve sur-saboteur contre jumeau ; **ouverte** si l'édition vers le haut laisse une autre trace que l'édition vers le bas |
| force et trace de l'édition commune aux deux sens, réunies | **ouverte** : l'épreuve à poussée égale ne retire pas la trace (le jumeau la porte, le saboteur non), l'épreuve sur-saboteur contre jumeau ne retire pas la force ; sans aucun sabotage, le mot sort dans plus de 0,5 % des mondes dans 12 des 13 mondes inventés essayés où les deux sont réunies, de 1 à 100 % (vérification du brouillon 3, mondes C01 à C11, C28, C29) |
```

### Couple V-B1b (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
ni de sa force, ni d'une trace de l'édition commune aux deux sens. Non tranché : l'acte ou la disposition
```

Après :

```text
ni de sa seule force, ni de la seule trace d'une édition commune aux deux sens. Non tranché : une force et une trace de l'édition commune aux deux sens réunies ; une divergence propre commune aux deux membres édités ; l'acte ou la disposition
```

### Couple V-B1c (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
deux rivales restent ouvertes (table de l'hypothèse).
```

Après :

```text
trois rivales restent ouvertes (table de l'hypothèse), dont la réunion d'une force et d'une trace de l'édition commune aux deux sens : chaque épreuve ne ferme sa rivale que si l'autre est absente.
```

### Couple V-B1d (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
dont deux restent ouvertes)
```

Après :

```text
dont trois restent ouvertes)
```

### Couple V-B1e (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
une force qui n'est ni un multiple de la part commune à la famille, ni un multiple de la direction commune à tous, reste une rivale ouverte.
```

Après :

```text
une force qui n'est ni un multiple de la part commune à la famille, ni un multiple de la direction commune à tous, reste une rivale ouverte, comme une force accompagnée d'une trace de l'édition commune aux deux sens : l'épreuve à poussée égale ne retire pas la trace, l'épreuve sur-saboteur contre jumeau ne retire pas la force.
```

### Couple V-B1f (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
**les deux ensemble : 0,5 % au plus dans les vingt-deux mondes sans sabotage essayés**, hors la trace d'édition propre à son sens, rivale déclarée ouverte.
```

Après :

```text
**les deux ensemble : 0,5 % au plus dans les vingt-deux mondes sans sabotage essayés**, hors la trace d'édition propre à son sens, rivale déclarée ouverte. Ces mondes n'ont qu'une rivale à la fois : quand une force et une trace de l'édition commune aux deux sens sont réunies, le mot sort dans 1 à 100 % des mondes dans 12 des 13 mondes essayés (vérification du brouillon 3), rivale déclarée ouverte.
```

### Couple V-B1g (constat V-B1) — `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
mot « sabotage » dans 0,5 % des mondes au plus, dans chacun des vingt-deux mondes essayés,
```

Après :

```text
mot « sabotage » dans 0,5 % des mondes au plus, dans chacun des vingt-deux mondes essayés, qui n'ont qu'une rivale à la fois (une force et une trace commune aux deux sens réunies le font sortir dans 1 à 100 % des mondes, dans 12 des 13 mondes essayés : vérification du brouillon 3),
```

### Couple V-B1h (constat V-B1) — `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-decisions-lazar-v3.md` — « avant » trouvé 1 fois dans la pièce scellée, 1 fois dans la copie au moment d'appliquer ; « après » déjà présent 0 fois

Avant :

```text
(épreuve refaite après la contre-lecture : en mondes inventés sans sabotage, le mot sort dans 0,5 % des cas au plus)
```

Après :

```text
(épreuve refaite après la contre-lecture : en mondes inventés sans sabotage où une seule rivale joue, le mot sort dans 0,5 % des cas au plus ; quand une force et une trace de l'édition commune aux deux sens jouent ensemble, il sort dans 1 à 100 % des cas dans 12 des 13 mondes essayés, rivale déclarée ouverte)
```

Validateur du dépôt sur la copie du brouillon 3 après le groupe « voie i » : aucun problème

Couples : 23 ; défauts : 0.
