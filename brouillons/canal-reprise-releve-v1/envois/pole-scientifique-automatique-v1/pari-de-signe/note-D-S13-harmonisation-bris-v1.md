# D-S13 — convention d'égalité : harmonisation du texte de la conception v4 (« bris toujours ») avec R-685 (« score continu exigé ; bris scellé sinon ») — note v1

Lignée conv-audit (instance de reprise ; **servie par Opus 5.5** pour cette note — l'en-tête de session le dit ; les pièces précédentes du jour
l'étaient par Fable 5.1), 29 octobre 2026, relevé `date -u` 12:07. Répond au point 5 du n° 180 de session-depot (divergence relevée par les notes
P-13 / N-029, `cfdcc86a…`). **Proposition ; ne modifie aucun fichier scellé.**

## Les deux textes

- **Conception v3 du pari, tableau des décisions, l. 277 ; repris en v5** (D-S13, clos par R-685 sur `main`) : « **score continu exigé** (probabilité
  du jeton de verdict) **pour toute cellule de G1 ; bris d'égalité scellé sinon** ».
- **Conception v4, l. 76-81** (correction locale de la ligne 2) : le bris « s'applique **toujours** (un score « continu » peut saturer près du
  quantile), avec une uniforme par épisode, fonction de l'identité de l'épisode et d'une graine scellée avant tout calcul de score, la même pour le
  calibrage et l'épreuve, **jamais retirée** ».

## Lecture : pas de contradiction de fond, une ambiguïté de mot

« Sinon » (R-685) peut se lire « si le score n'est pas continu » ou « si des ex æquo restent ». La v4 dit pourquoi la seconde lecture est la bonne :
un score continu par construction (probabilité d'un jeton) **sature** près de 0 et de 1, donc produit des ex æquo au voisinage du quantile τ. Appliquer
le bris à une cellule sans ex æquo ne change aucun rang (l'uniforme ne départage que des égalités) : « toujours » n'a d'effet que là où « sinon » en
aurait. La v4 ajoute deux garanties absentes du texte court : **même graine au calibrage et à l'épreuve** et **jamais retiré** (ni par fiche ni par
génération : le retirer après lecture serait une sélection, N-053).

## Texte harmonisé proposé (à porter au préenregistrement de G1 et à la version suivante de la conception)

> **D-S13.** Toute cellule de G1 exige un **score continu** (probabilité du jeton de verdict). Le **bris d'égalité scellé** est **toujours actif** :
> il départage tout ex æquo résiduel (saturation comprise) par une uniforme par épisode, fonction de l'identité de l'épisode et d'une clé engagée
> par empreinte avant le premier score, **la même au calibrage et à l'épreuve**, révélée après ; il est sans effet hors ex æquo ; il n'est **jamais
> retiré**, ni par fiche, ni par génération. Le nombre d'ex æquo départagés par cellule et le pas au voisinage de τ sont rapportés.

Ce texte tient R-685 (le score continu reste exigé ; le bris est « scellé ») et la v4 (« toujours », même graine, jamais retiré). Il coïncide avec le
lot L2 de session-depot (`src/controle_ia/bases/bris_egalite_v1.py`, `b329f9b5…`, R-769 : clé de 64 bits engagée par empreinte avant le premier
épisode, révélée après ; dérivation salée par cellule, épisode, moniteur ; clé de tri (score, condensat)), qui applique déjà le bris partout.

## Décision

**Décision** : retenir le texte harmonisé pour D-S13. **Enjeu** : une cellule de G1 lue avec ou sans bris selon la lecture de « sinon » donnerait deux
taux de faux positifs différents au voisinage de τ (contrôle 12 joint). **Options** : (a) texte harmonisé (« toujours actif, sans effet hors ex æquo ») —
avantage : aucune lecture laissée au lecteur, conforme au code L2 ; inconvénient : aucun ; (b) lecture stricte de R-685 (bris seulement pour les cellules
sans score continu) — avantage : texte court ; inconvénient : ex æquo par saturation non départagés, contredit le code L2. **Recommandation : (a)**,
confiance 0,85 (c'est une clarification, pas une modification : D-S13 reste clos). **Défaut sous 48 heures** (≈ 31 octobre 12:00 UTC) : (a), consigné
par session-depot sur `main` à côté de R-685.
