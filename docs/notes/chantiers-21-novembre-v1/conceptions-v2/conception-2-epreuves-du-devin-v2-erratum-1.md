# Erratum 1 — Conception 2 — les épreuves du devin — v2

- **Cet erratum prime sur la v2** : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v2.md` — sha256 fdc6889a0eb3a6b23016b61e1a68a89c0cee4eeb960ca3603af50dad08789dce (compagnon vérifié). La v2 n'est pas réécrite ; elle se lit avec cet erratum.
- Source des couples : `docs/notes/chantiers-21-novembre-v1/contre-lectures-v1/verification-conception-2-v2-opus-v1.md` — sha256 3b00f74a40c4cde2231186b57ef7e00d1458a44d3cb155173e9512a71a12f1db (compagnon vérifié), table des constats.
- Couples extraits par programme, mot pour mot, par `docs/notes/chantiers-21-novembre-v1/conceptions-v2/extraction-erratum-1-conception-2-v2-v1.py` — sha256 b085c4cc097b3727a2188ae7e5513ece6d2fe56ffc6193d12800f3effd6dbc75 (lecture des cellules : `portage-conception-2-v2.py`, sha256 76288a912a0e5618e5cb004acd1bd64ed6febdb0ba55dcd09e6e2811bd8bc457). Un nouveau donné « en deux lignes » est réuni par un saut de ligne.
- Vérifications du programme : chaque ancien figure une seule fois dans la v2 ; appliqués dans l'ordre ci-dessous, chaque ancien est unique à son tour et chaque nouveau est présent ; défaire dans l'ordre inverse redonne exactement la v2.
- Couples (8), à appliquer dans l'ordre de la table de la vérification : 6-b ; 9-b ; 13-b ; 16-a ; 17-a ; 18-a ; 2-b ; 1-c.

## 6-b — important — § 5, « Quand cela vaut la peine »

Ancien :
```text
- le harnais passe son témoin.
```

Nouveau :
```text
- le harnais passe son témoin. Ou bien le harnais rejoue déjà à graines identiques, auquel cas le couplage se joue d'emblée, comme garde de non-régression.
```

## 9-b — important — § 7, inventaire — nouveau en deux lignes

Ancien :
```text
12. Quels champs du journal sont privés ? Lesquels franchissent la frontière ?
```

Nouveau :
```text
12. Quels champs du journal sont privés ? Lesquels franchissent la frontière ?
13. Quatre canaux trouvés par l'inventaire du code. (a) Une garde, une limite de durée ou un arrêt de course lit-il un score, une pièce ou un verdict ? Le nombre d'épisodes ou de pas joués en dépend-il ? (b) Comment les lots sont-ils composés et remplis ? Un épisode audité, ou sa copie, partage-t-il un lot avec un épisode servi ? (c) Où sont publiées l'entropie racine et les clés de graine (manifeste, préenregistrement), et l'agent ou le devin peut-il les lire ? (d) Dans un épisode à plusieurs agents, que voit chaque agent des actions des autres, et l'un d'eux peut-il être audité ou aiguillé sans les autres ?
```

## 13-b — mineur — § 1, « Définition »

Ancien :
```text
pour la question 14 de la section 7.
```

Nouveau :
```text
pour la question 13 (b) de la section 7.
```

## 16-a — mineur — § 3, « Deux courses pour la pièce » — nouveau en deux lignes

Ancien :
```text
- Une course au taux de service, parce que les canaux de charge dépendent du taux.
```

Nouveau :
```text
- Une course au taux de service, parce que les canaux de charge dépendent du taux.
- Pour la lecture substituée, de même, une course où S est tiré de sorte que chaque décision du harnais qui en dépend soit prise une fois sur deux (puissance), et une course où S suit la loi des lectures de témoins (régime de service).
```

## 17-a — mineur — § 4, « Le monde planté »

Ancien :
```text
Un harnais simulé sur processeur produit des épisodes à pas, avec texte synthétique, durées log-normales, relances, erreurs, rang et charge.
```

Nouveau :
```text
Un harnais simulé sur processeur produit des épisodes à pas, avec texte synthétique, durées log-normales, relances, erreurs, rang et charge. Défauts, à sceller avec la pièce 4 : 8 pas par épisode ; texte de 200 mots tirés d'un lexique fermé de 2 000 mots, dont 20 marqueurs ; log-durée par pas normale (moyenne 0, écart type 1) ; relance avec probabilité 0,05 par épisode ; erreur avec probabilité 0,02 ; rang uniforme sur 1 à 10 ; charge normale centrée réduite.
```

## 18-a — mineur — « Antériorités connues » — nouveau en deux lignes

Ancien :
```text
- Clopper et Pearson, 1934.
```

Nouveau :
```text
- Clopper et Pearson, 1934.
- Test de randomisation conditionnelle : Candès, Fan, Janson et Lv, 2018 ; à pli tenu à part : Tansey et al., 2022, “The Holdout Randomization Test for Feature Selection in Black Box Models”. Détection de fuite par test fixe contre aléatoire, qui réfute sans attester : Goodwill et al., 2011 ; par réseau appris : Moos, Wegener et Moradi, 2021, “DL-LA”. Rapportés, non vérifiés sur PDF. La statistique du devin n'a rien de propre.
```

## 2-b — important — Conclusion, « Témoins dans chaque course »

Ancien :
```text
Une fuite plantée à la taille minimale doit être retrouvée.
```

Nouveau :
```text
Une fuite plantée, à une taille de puissance au moins 0,99 au budget joué, doit être retrouvée.
```

## 1-c — mineur — Décision 2, option (a)

Ancien :
```text
- *(a) α = 0,05, 4 000 épisodes par devin, deux courses pour la pièce.* Avantage : fuite de 0,056 retrouvée.
```

Nouveau :
```text
- *(a) α = 0,05, 4 000 épisodes par course, deux courses pour la pièce.* Avantage : fuite d'environ 0,08 retrouvée par la famille entière (0,056 pour un trait seul).
```
