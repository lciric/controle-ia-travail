# Contre-lecture des douze fiches de la veille sur l'exploration des idées — v1

Écrit le 18 novembre 2026 par un sous-agent contre-lecteur, d'une autre lignée que les lecteurs, avec consigne de réfuter. Je n'ai fait ni commit, ni dépense, ni écriture dans `registres/`, et je n'ai ouvert aucun résultat sous embargo. J'ai seulement relu les documents déjà versés, sans rien télécharger de neuf. Les PDF ont été lus par `pdftotext` (mode mise en page, puis mode ordre de lecture). Les programmes de contrôle sont des brouillons hors du dépôt et n'ont rien exécuté venant des documents. Je n'ai relevé dans les pièces relues aucune consigne adressée à un lecteur automatique.

## Verdict d'ensemble

Les citations sont fidèles. Sur 160 citations courtes rejouées par programme, 158 sont à la page citée et 2 sont sur la page voisine, à l'intérieur de l'intervalle de pages donné par la fiche. Aucune citation n'est introuvable. Sur 149 chiffres rejoués, 145 sont à la page citée et 4 sont sur une autre page du même document. Aucun chiffre n'est absent. Toutes les empreintes des PDF relus sont égales à celles annoncées.

Trois choses sont à corriger :
- **Article de Gençay** (fiche 01) : la date de première version arXiv n'est pas fiable, et son ordre par rapport à N-064, N-065 et N-067 est à revoir.
- **Article « Bad Genius »** (fiche 10) : le verdict « contredit » vise la mauvaise phrase de N-049, et il repose sur une seule ligne de tableau apparue en version 3.
- **Machine de Huxley-Gödel** (fiche 05) : le verdict « voisin » sur le destinataire du signal est trop favorable.

## 1. Rejeu des citations et des chiffres

Méthode : le texte de chaque PDF est extrait page par page. La normalisation joint les coupures de fin de ligne, unifie guillemets, tirets et signes moins, et ignore la casse. On cherche ensuite chaque citation sur la page citée, puis dans tout le document.

| Fiche | Document (empreinte vérifiée) | Citations à la page citée | Chiffres à la page citée |
|---|---|---|---|
| 01 Gençay, 2611.14539v1 | 7d2cc012… | 17 sur 17 (une retrouvée à la main : coupure après « ledger », p. 7) | 4 sur 4 |
| 02 Liu, 2611.04070v2 | 921119fd… | 19 sur 19 | 12 sur 12 |
| 03 Yang et Shi, 2611.00643v1 | 62be7556… | 26 sur 26 | 15 sur 17 (« 1,55 » est p. 2, 3 et 26, pas p. 8 ; « −,58 » est écrit « ρ = −.58 » p. 10, présent) |
| 04 Agarwal et al., 2606.29182v1 | 77d57d06… | 11 sur 11 | 14 sur 15 (« 30,62 % » est p. 1 et 3, pas p. 7) |
| 05 Huxley-Gödel, 2510.21614v3 | 06cbf326… | 7 sur 7 | 21 sur 21 |
| 07 Oved et al., 2610.23977v1 | aa439be4… | 9 sur 11 à la page exacte ; les 2 autres (« 12 of 15 pairs… », « The difference was the task… ») sont p. 4, dans l'intervalle « p. 4-5 » de la fiche | 9 sur 9 |
| 08 AIDE², 2609.26457v1 | 8ba79e0a… | 21 sur 21 (une retrouvée à la main : retour à la ligne, p. 5) | 18 sur 19 (« 0,749 » est p. 6, dans l'intervalle « p. 5-6 ») |
| 09 Lineage Is Memory, 2610.41157v1 | 3b0b0c0c… | 6 sur 6 | 11 sur 11 |
| 10 Bad Genius, 2609.18366v3 et v1 | a9a567ab…, 62eb5e4b… | 17 sur 17 (voir la note ci-dessous) | 16 sur 16 |
| 11 Ferreira et al., 2609.35875v1 | 5fc206ae… | 11 sur 11 (deux retrouvées à la main : « 1.6× » écrit avec le signe ×, et « generationbudget-matched » sans trait d'union, p. 3 et 5) | 10 sur 10 |
| 12 Qin et al., 2611.05108v1 | aae12565… | 14 sur 14 | 15 sur 15 |
| 06 MetaEvoForge (résumé seul) | page de la conférence versée | 9 phrases du résumé sur 9 trouvées dans la page | sans objet |

Note sur la fiche 10 : la phrase de limites de la version 1 (« This claim is relative to the evaluated counterfactual family… three-round search budget », p. 9) n'est lisible dans le texte extrait que dégradée (« fam y whose coverage s m ed by our hree-round search budge »). Elle est bien présente. Elle est absente de la version 3, ce qui confirme la fiche. J'ai aussi vérifié le comptage par versions : « HarnessEvolve » apparaît 2 fois en version 1 et en version 2, 24 fois en version 3 ; les nombres « 11.70 » et « 8.65 » n'apparaissent qu'en version 3.

Autres contrôles faits :
- **Fiche 01** : dans l'archive de Zenodo, les configurations `p2_e3_full_plain` et `p2_e3_deflated_plain` diffèrent par le champ `feedback`, et aussi par leur nom et leur description, ce qui est sans portée. `feedback.py.txt` sert bien les quatre nombres `search_bar`, `search_excess`, `search_trials_spent` et `search_wealth`. `v_floor` vaut 0,1204512… dans les configurations « plain » et « hwm » comme dans `e0_calibration.json`. `endpoints.json` est daté du 30 juillet 2026, avec une version de code suffixée « -dirty ».
- **Fiche 02** : les textes extraits des versions 1 et 2 ne diffèrent que par la ligne du tampon arXiv. C'est confirmé.
- **Fiche 03** : la notice du dépôt sur Open Science Framework donne une création le 29 octobre 2026 à 20:34:26 et « registration: false ». Ses 17 fichiers sont datés de 20:35:21 à 20:35:31. Le contrôle des empreintes des préenregistrements par `SHA256SUMS.txt` donne 16 sur 16. Le tableau 23 (p. 38) va du 21 octobre 00:56 au 24 octobre 01:42.
- **Fiche 05** : « discount », « horizon », « depth » et « ablation » apparaissent 0 fois dans la version 3. Dans la version 1, le mot « clade » et le chiffre 0,778 sont déjà présents.

## 2. Fiche par fiche

**01, Gençay, « Can a search hold its own bar? » : à corriger (date), et verdict 1 à nuancer.**
- Les citations et les verdicts 14 et 2 tiennent.
- Verdict « voisin » sur le juge au nul formé des lois connues : il tient, mais la phrase « aucune archive… n'entre dans le seuil » va trop loin. Le plancher de variance est « calibrated once, from prior-system search ledgers only » (p. 6). Une archive de recherches passées entre donc dans le seuil, comme dispersion et non comme lois. Le lecteur sévère le dira.
- Date : l'identifiant 2611.14539 ne peut pas correspondre au 14 octobre. La série des documents versés est cohérente : 2610.23977 le 13 octobre, 2610.41157 le 30 octobre, 2611.00643 le 31 octobre, 2611.04070 le 2 novembre, 2611.05108 le 3 novembre. Un numéro 2611.14xxx tombe donc vers le 10 au 13 novembre. Le PDF a été produit par arXiv le 13 novembre à 01:01 UTC. C'est une inférence, mais elle s'appuie sur les tampons et les métadonnées des documents versés.
- Conséquence sur la phrase « dans tous les cas antérieur à N-064, N-065 (9 novembre) et N-067 (13 novembre) » : elle ne tient que par l'archive de Zenodo du 31 juillet, qui porte le code, les configurations et les bras de retour. Elle ne tient pas pour le texte de l'article, dont la mise en ligne réelle est probablement postérieure à N-064 et N-065 et voisine de N-067 au jour près.

**02, Liu, « Are LLM Research Agents Reliable Judges… » : tient avec réserves.**
- Les 19 citations et les 12 chiffres sont présents. Les dates sont confirmées : version 1 le 2 novembre à 23:25:11, version 2 le 8 novembre à 22:46:30, même texte.
- Les verdicts « libre » (tirages semés par l'empreinte de l'engagement ; nul formé des lois connues) tiennent au sens « absent de la pièce ».
- Réserve : la p. 3 cite deux voisins non lus sur la pression de consigne et l'engagement sur l'inconnaissable (Balani et Panda 2026 ; arXiv 2608.27167). Ils touchent la prémisse du bras du juge génératif et sont à lire avant de dire « voisin » au-delà de ce document.

**03, Yang et Shi, « Selecting LLM-Generated Hypotheses… » : tient.**
- Les 26 citations sont présentes.
- Deux pages de chiffres sont à rectifier : 1,55 se lit p. 2, 3 et 26, non p. 8 ; −0,58 se lit p. 10 sous la forme « ρ = −.58 ».
- Les dates du dépôt sur Open Science Framework et des préenregistrements sont vérifiées. Les verdicts « occupé en partie » sont les moins flatteurs possibles.
- À ajouter : les mêmes auteurs signent la fiche 09, à quelques jours d'écart, avec la même pratique de préenregistrement auto-daté. Leur journal de commits mentionne une « de-AI rewrite ». Ces deux préenregistrements ne sont donc pas des pièces indépendantes.

**04, Agarwal et al., croyances informées par les preuves : tient.**
- Les 11 citations et 14 des 15 chiffres sont à la page citée. Le +30,62 % se lit p. 1 et 3, pas p. 7.
- Les verdicts tiennent. La date du 28 juin 2026 à 04:06:12 est confirmée.

**05, Machine de Huxley-Gödel : tient avec réserves, un verdict à durcir.**
- Les citations, les chiffres et la date (24 octobre 2025) tiennent. Le premier commit du dépôt de code date du 24 octobre 2025 (f3ca5f8).
- Le verdict « voisin » sur le destinataire est trop favorable. Le signal de lignée alimente un tirage de Thompson qui apprend, sur la descendance, quelle lignée faire concevoir ensuite (p. 6-7, algorithme 1 p. 17). C'est un apprentissage de la conception au niveau « qui se reproduit ». Je le passe à « occupé en partie ».
- Ce qui reste libre, au regard de ce seul document : un concepteur dont les paramètres ou la consigne apprennent de ce signal.

**06, MetaEvoForge (résumé seul) : tient.**
- Les 9 phrases du résumé citées sont dans la page versée.
- Le bouton « Project Page » pointe vers le même forum d'OpenReview : il n'y a donc ni projet ni code caché manqué.
- La lecture reste sur résumé et n'est pas opposable : la réserve de la fiche est juste.

**07, Oved et al., « … Should be Compared by Tokens » : tient.**
- Toutes les citations sont présentes. Deux sont p. 4, dans l'intervalle annoncé « p. 4-5 ».
- Les dates sont vérifiées sur les pages de résumé versées : 13 octobre 2026 pour l'article, 17 septembre pour le compagnon, 18 février pour Gideoni et al. (dont une version 2 existe depuis le 12 octobre 2026, à noter).

**08, AIDE² : tient.**
- Les 21 citations et 18 des 19 chiffres sont à la page citée.
- Date du billet : métadonnées « datePublished 2026-07-14 », flux du blog au 14 juillet, et capture d'archive.org du 15 juillet 2026 à 08:55:01 dont l'existence est vérifiée. Le contenu d'époque n'est pas vérifié, comme la fiche le dit.

**09, Lineage Is Memory : tient.**
- Les citations et les chiffres sont présents. Le premier commit 0fc25a8 date du 28 octobre 2026 à 22:42:40, heure du Pacifique.
- Un détail : un commit « Add authors: Shanglin Yang, Zhan Shi, Li Yin » nomme trois auteurs, quand le PDF et la fiche en nomment deux. C'est sans effet sur les verdicts.

**10, Bad Genius : à corriger (verdict « contredit »).**
- Les citations, les chiffres et les trois dates de version tiennent.
- Le verdict « contredit » vise la mauvaise phrase. N-049 dit déjà que l'organisme « ne peut s'adapter qu'au générateur et à la famille » ; l'article ne contredit pas que la banque sœur sépare « adapté aux textes » de « adapté à la famille ». Ce qu'il contredit, c'est la prémisse citée en tête de N-049 : « Le sur-ajustement porte sur les 36 textes, pas sur la famille ». Il montre qu'un gain peut porter sur un raccourci propre au générateur, que des tâches fraîches du même générateur ne voient pas.
- La preuve de cette contradiction est faible : une seule méthode, une course, aucun intervalle, et une ligne absente des versions 1 et 2 (vérifié ci-dessus).
- Je passe donc le verdict à « contredit faiblement, cible corrigée ».

**11, Ferreira et al., « Beyond Symmetric Agents » : tient avec réserves.**
- Les citations et les chiffres sont présents.
- Le passage de « contredit » à « voisin » sur la revendication 12 (c) tient sur la mesure. En revanche, la phrase de la p. 7 (« teams do not benefit from spanning more model families once member strength is accounted for ») est une affirmation explicite contraire. Elle doit être citée comme contre-indice déclaré, même mal appuyée.
- À citer de même, en sens inverse : la même page note que des équipes mixtes de niveau faible ou moyen battent leur meilleur membre seul d'au moins 10 points dans 19 cellules, sans appariement de budget.

**12, Qin et al., « Continual AutoResearch » : tient.**
- Les 14 citations et les 15 chiffres sont présents. La date du 3 novembre 2026 à 16:02:34 est confirmée.
- Les dates d'OpenReview restent non vérifiées, comme la fiche le dit.

## 3. Verdicts que je change

1. **Fiche 05, revendication 8, destinataire du signal** : « voisin » devient « occupé en partie ». Un tirage de Thompson apprend du signal de lignée où concevoir ; seul un concepteur qui apprend dans ses paramètres ou sa consigne reste non trouvé.
2. **Fiche 10, revendication 11, banque sœur** : « contredit » devient « contredit faiblement ». La cible est la prémisse « le sur-ajustement porte sur les textes, pas sur la famille », non la séparation elle-même. La preuve tient à une ligne de la version 3.
3. **Fiche 01, date de première version** : « 14 octobre 2026 » devient « affichée le 14 octobre ; mise en ligne probable entre le 10 et le 13 novembre 2026 ». L'antériorité sur N-064, N-065 et N-067 ne tient que par l'archive de Zenodo du 31 juillet.
4. **Fiche 01, revendication 1** : le verdict « voisin » est gardé, mais la preuve doit mentionner le plancher de variance calibré sur les registres de recherches antérieures (p. 6).
5. **Fiche 11, revendication 12 (c)** : le verdict « voisin » est gardé, en ajoutant comme contre-indice déclaré l'affirmation contraire de la p. 7.

Aucun verdict « libre » n'est retourné en « occupé » : je n'ai trouvé dans les pièces relues aucune occupation cachée de ce qui est dit libre.

## 4. Mes limites

- Je n'ai relu que les documents déjà versés, sans nouvelle recherche web : je ne peux donc rien dire sur le champ au-delà de ces pièces (règle R8).
- Le rejeu porte sur les citations courtes et les chiffres, pas sur la justesse de chaque paraphrase.
- Mes verdicts durcis (fiches 05 et 10) sont des jugements de lecture, à trancher par Lazar.
- La date corrigée de la fiche 01 est une inférence tirée de la série des identifiants et des métadonnées du PDF. Elle n'est pas lue sur une source d'arXiv qui la dise.
- Ni l'archive de Zenodo entière ni les dépôts de code n'ont été rejoués. Je n'ai pas vérifié à nouveau les lectures des figures, ni les pages relues sur image par les lecteurs, sauf la p. 9 de la version 1 de « Bad Genius », rendue en image puis contrôlée par le texte dégradé.
