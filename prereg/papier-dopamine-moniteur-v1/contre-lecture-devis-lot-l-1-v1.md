# Contre-lecture — devis de la part du lot honnête neuf qui étalonne les deux verdicts principaux du bras « papier dopamine » — v1

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf de la session mère ; je n'ai écrit aucune pièce lue ici (R2). Écrit le 21 novembre 2026. Aucun appel payant, aucun appel aux interfaces du loueur, aucune machine créée.
- **Pièce contre-lue** : `prereg/papier-dopamine-moniteur-v1/devis-lot-l-1-v1.md` (`613f16a8d6be654539ddf7db8d2849f646baca3c955ca05a891768f0519f1638`), classe A.
- **Pièces lues, par leur chemin** : le programme de calcul `calculs-devis-lot-l-1-v1.py` (`5c43fe8f…`) et sa sortie `calculs-devis-lot-l-1-v1.txt` (`a37ae705…`) ; le relevé `releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json` (`bc54f8bd…`) ; le préenregistrement court v7, brouillon (`preenregistrement-court-papier-dopamine-v7-brouillon.md`, `e05f4a99…`), sections « Seuil » (l. 103-116) et « Le lot honnête neuf : exigences pour le devis » (l. 204-214), et sa contre-lecture (`contre-lecture-preenregistrement-court-papier-dopamine-v7-v1.md`, `a38b5469…`), corrections 1, 8, 10, 11 et choix 1 et 2 ; `registres/go.md`, ligne GO-2026-11-21-29 ; `registres/depenses.md`, l. 573 ; la source première du débit, `prereg/T0.6-organismes-v0-v1.md` (`ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`), l. 638-653 seulement, section « Sources des chiffres » du devis de ce texte (débits et prix ; aucun score, aucune table de résultats, aucun verdict) ; le devis scellé du barreau 5, § 1 à § 3. Aucun résultat d'expérience ouvert.

## Verdict

**Conforme après ces corrections** : six corrections, dont **une bloquante** (B-1, la ligne d'accord dit « au moins 437 » alors que la règle du devis permet de n'acheter que pour 368). Les chiffres sont justes et rejoués à l'octet ; la grille non fondée est présentée honnêtement ; la coupure de 37 USD est un choix de conception justifié et cohérent avec les arrêts.

## 1. Empreintes et rejeu

- Les compagnons `.sha256` du devis, du calcul, de sa sortie, du relevé, du brouillon v7 et de sa contre-lecture concordent avec les fichiers sur disque.
- Le programme ne fait aucun appel de réseau : il importe `json`, `math`, `sys`, `pathlib` et `scipy.stats.beta`, et lit le seul relevé voisin. Rejoué depuis la racine par `.venv/bin/python -I prereg/papier-dopamine-moniteur-v1/calculs-devis-lot-l-1-v1.py` : sortie **identique à l'octet** (`cmp`).
- Le relevé ne porte aucune clé (recherche de « bearer », « api_key », « authorization » : rien) ; `truncated: false` ; 30 offres, 13 de 80 Go.

## 2. Chiffres rapportés à leurs sources, et refaits à la main

- **368 et 437** : ⌈ln 0,025 / ln 0,99⌉ = 368 ; ⌈ln 0,0125 / ln 0,99⌉ = 437 ; égaux au calcul de la v7 et à la contre-lecture (« 368 (risque 0,025) et 437 (0,0125) »). 437 répond à la variante A de la correction 1, retenue par Lazar (GO-2026-11-21-29 : « risque au plus 5 %, P2 compris »). Bande de 1 à 11, K = 11, 133 par côté : égaux à la correction 1, A5.
- **Débit de 40,2 secondes par épisode en lots de 8** : relu sur la source première, `prereg/T0.6-organismes-v0-v1.md` l. 642-643 : course réelle de P3 sur A100 SXM4 80 Go, « 240 épisodes en 9 644,6 s, soit 40,2 s par épisode en lots de 8 » ; génération seule, la passe d'activations (0,45 s par épisode) est à part. La même course dure ≈ 3,6 heures en tout pour 2,68 heures d'épisodes : les 1,8 heure de frais fixes du devis sont prudentes. Réserve qui reste : ce débit est celui du banc de P3 ; le banc de ce lot n'est pas encore nommé (§ 8 du devis le dit).
- **Prix** : fourchette 1,0889 à 1,30, pire 1,40, stockage 0,03 à 0,08, téléchargement 0,026 à 0,05 : devis scellé du barreau 5, § 1, qui les tient de la même section de T0.6 (l. 648-653). Dernier prix payé, 1,055 USD de l'heure : `registres/depenses.md` l. 573. Deux offres aux bornes, 1,0970 et 1,1627 : relevé, refait (disques de 90,7 et 1 049,5 Go, 16 cœurs, stockage 0,333 et 0,24 USD par Go et par mois).
- **Refaits à la main** :
  - **borne haute** : 1,8 + 1 311 × 40,2 / 3 600 = 16,44 h ; 16,44 × 1,1189 + 42 × 0,026 = **19,49** ; 16,44 × 1,38 + 42 × 0,05 = **24,79 USD** ;
  - **pire cas** : 2 × 16,44 = 32,88 h × 1,48 + 2,10 = **50,76 USD** ;
  - **coupure** : 1,5 × 16,44 = 24,66 h × 1,38 + 2,10 = 36,13 → **37 USD** ; heures sous la coupure au pire : (37 − 2,10) / 1,48 = 23,58 h ; (23,58 − 0,25 − 3,6) / (2 × 40,2 / 3 600) = **883 épisodes** ;
  - cas de référence (150 familles, ρ = 0,10) : m = 3 donne 450 / 1,2 = 375 < 437 ; m = 4 donne 600 / 1,3 = 461 ≥ 437 : **600 épisodes**, 8,50 h, 10,60 à 13,83 USD ;
  - une case du § 3 (200 familles, ρ = 0,30) : m = 4, 800 / 1,9 = 421 ; m = 5, 1 000 / 2,2 = 454 : **1 000**.
  Tous égaux à la sortie.
- **Marqués non fondés** : F, ρ, le cas de référence, le facteur 1,5 de la coupure, les 10 actions par épisode, le disque de 80 Go. Rien d'autre ne l'est.

## 3. La grille non fondée, et la coupure de 37 USD

- **Grille** : honnêtement présentée. F et ρ sont dits inconnus, donnés en table et jamais en valeur ; le cas de référence est dit « convention d'affichage » au devis comme au calcul ; l'attendu est donné en fourchette de la borne basse à la borne haute ; les cases « — » et la règle « rien n'est acheté » disent qu'un lot peut ne rien valoir. Une imprécision : l'attendu est écrit « 9 à 25 USD » alors que le bas est 8,57 (correction B-5).
- **Coupure** : justifiée comme choix écrit. Elle laisse finir la borne haute sur un hôte jusqu'à une fois et demie plus lent au prix haut, et arrête vers 883 épisodes au pire cas. Le pire cas du devis (1,40 USD de l'heure) dépasse la borne de l'offre (1,30) : il est hérité du devis scellé. Sous les bornes, le pire cas réel est de 47,5 USD (2 × 16,44 h × 1,38 + 2,10), toujours au-dessus de la coupure, que la coupure arrête aussi. Pour un plan plus petit que la borne haute, l'arrêt n° 3 (deux fois la durée prévue) borne plus tôt que la coupure : pour 600 épisodes, 17 h, ≈ 25,6 USD. Cohérent.

## 4. Cohérence de l'attendu, du pire cas, de la coupure et de la ligne

- Plafond de la ligne = coupure = 37 USD ; pire cas non atteignable ; arrêts n° 1 à 5 cohérents entre eux ; la sortie de données, le stockage et le téléchargement sont comptés ; le temps des agents ne l'est pas, et c'est dit.
- La ligne tient au format à huit colonnes, sans barre verticale dans une cellule ; type « calcul » ; conditions de validité écrites dans la cellule ; échéance 2026-12-15.
- **Défaut bloquant** : la ligne dit « au moins 437 épisodes honnêtes effectifs », alors que la règle du § 3 prévoit, si 437 ne tient pas sous la borne, d'acheter pour 368 (la première question seule) : une course à 368 serait hors de la lettre de la ligne. Correction B-1.
- **Imprécision** : la ligne dit « une carte A100 », le § 5 chiffre aussi deux cartes, coupure commune. Correction B-2.

## 5. Dépense, conditions de départ, paiements supposés

- Aucune dépense n'est ouverte hors de la ligne ; « aucune rallonge sans devis neuf » ; les autres parts du lot, l'étape 1 et le lot des gains de fusion sont dits hors du devis.
- Conditions de départ écrites (§ 9) : préenregistrement scellé, porte de reproduction passée, addendum de l'étape 2a scellé et citant ce devis, code du lanceur contre-lu et inscrit, crédit suffisant. Rien ne suppose un paiement que Lazar n'a pas fait. Mais le crédit du loueur est commun à plusieurs courses (barreau 5, nouvelles attaques, seuil et moniteurs), et une recharge manquée a déjà arrêté des machines sans versement (GO-2026-11-20-40) : la condition doit compter les autres coupures ouvertes (correction B-3).
- La recommandation (b), attendre l'addendum, confiance 0,6, et l'absence de défaut sont conformes. Elle est d'autant plus juste que l'étape 1 et la pré-mesure de l'étape 2a n'ont pas de devis : sous (a), la ligne pourrait s'éteindre le 15 décembre avant que ses conditions soient remplies.

## 6. Ce que le devis suppose sans le dire, et ce qui le ferait déborder

1. **Quel ρ.** La v7 (l. 113) définit ρ sur « l'indicatrice en alerte au seuil commun de 20 % » d'un score ; cette part fixe le seuil de la sonde de réussite attendue pour P1 et P2, et peut-être d'autres. Si plusieurs scores prennent leur seuil sur elle, le nombre d'épisodes doit se calculer avec le plus grand de leurs ρ, sans quoi l'un d'eux tombe sous 437 effectifs (correction B-4).
2. **Variantes honnêtes** : le § 8 dit que le lot se multiplie par le nombre de variantes si chaque mode en demande une. C'est le débordement le plus gros, et il est dit ; il demande un devis neuf, pas un dépassement de la ligne.
3. **Banc et débit** : un banc plus long que celui de P3 allonge tout ; la coupure le tient, au prix d'un lot plus court et d'un verdict « non concluant ».
4. **Deux cartes** : sur deux instances à la borne haute et un hôte une fois et demie plus lent, le coût monte à ≈ 42 USD ; la coupure commune arrête avant. Acceptable s'il est dit (B-2).
5. Le maximum sur les jetons par relecture forcée est renvoyé à plus tard, hors devis : dit au § 10.

## 7. Corrections (liste fermée)

**B-1 (bloquante) — la cible de la ligne.** § 11, ligne d'accord : remplacer « au moins 437 épisodes honnêtes effectifs et 1 311 épisodes réels au plus, » par « 437 épisodes honnêtes effectifs visés, 368 pour la seule première question si 437 ne tient pas sous la borne, rien d'acheté si 368 n'y tient pas (règle du § 3), 1 311 épisodes réels au plus, ».

**B-2 — le nombre d'instances.** § 11, ligne d'accord : remplacer « Une carte A100 SXM4 de 80 Go à 1,30 USD de l'heure au plus ; » par « Une instance, deux au plus, chacune une carte A100 SXM4 de 80 Go à 1,30 USD de l'heure au plus, sous la coupure commune ; ».

**B-3 — le crédit commun.** § 9, point 5 : remplacer « Le crédit du loueur au moins égal à la coupure. » par « Le crédit du loueur, diminué des coupures restantes des autres courses ouvertes sur le même crédit, au moins égal à la coupure, relevé à la création ; aucune recharge n'est supposée. »

**B-4 — quel ρ.** § 3, « Règle » : remplacer « avec F familles retenues et le ρ gelé à l'étape 2a, » par « avec F familles retenues et le plus grand des ρ gelés à l'étape 2a pour les scores dont cette part fixe le seuil (la sonde de réussite attendue, et tout autre score que l'addendum lui assigne), ».

**B-5 — le bas de l'attendu.** § 5, puce « Cas attendu » : remplacer « soit **9 à 25 USD**. » par « soit **8,6 à 24,8 USD**. »

**B-6 — la source première du débit, relue.** § 4, puce « Débit » : remplacer « **De seconde main** : je n'ai pas ouvert la source première, qui est une conception d'organismes. Le contre-lecteur la relit. » par « **De seconde main** pour l'auteur ; relu par le contre-lecteur sur la source première (`prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`, l. 642-643) : course réelle de P3, 240 épisodes en 9 644,6 s, génération seule, la passe d'activations à part (0,45 s par épisode) ; la course entière, ≈ 3,6 heures, laisse ≈ 0,9 heure de frais fixes, sous les 1,8 heure comptées. Banc de P3 : à confirmer pour ce lot (§ 8). » ; et au § 8, ligne du débit, remplacer « le contre-lecteur (source première), puis la première heure de la course » par « source première relue par le contre-lecteur (banc de P3) ; la première heure de la course sur le banc de ce lot ».

## 8. Ce qui n'est pas une correction

- Le devis respecte les exigences de la v7 pour cette part, lues avec les corrections 10 et 11 : borne haute écrite, forme de la règle d'arrêt dite (par comptes), mélange de référence déclaré (uniforme sur les familles listées à l'addendum), aucune strate sur-tirée, donc pas de quantile pondéré ; part disjointe par famille des autres usages ; même banc, même harnais, même modèle que les épisodes sabotés servis.
- « Ne regarder que des comptes » garde valides les bornes exactes des seuils ; c'est la forme sûre des deux que la v7 permet.
