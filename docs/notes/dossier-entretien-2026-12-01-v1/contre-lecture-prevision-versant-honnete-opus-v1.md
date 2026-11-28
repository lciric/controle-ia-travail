# Contre-lecture (R2) de la prévision courte du versant honnête — Opus 5.5 neuf — v1

## Attestation

2026-11-24, 11:41Z à 11:58Z (`date -u`). Non lus : la lecture scellée de l'étalonnage (LECTURE-T08), son verdict (VERDICT-T08-V3), les scores de sondes de l'honnête de 7b ; ni épisode, sortie, résultat, diagnostic, score, verdict ou lecture ; ni `coffre/` ni `registres/` ; du texte de l'étalonnage, les lignes 35 à 45. Vu en passant, non employé : l'aire 0,8878 de P3 citée par P8-1. Dépôt non modifié.

| pièce (empreinte) | lu |
|---|---|
| prévision `prereg/versant-honnete-jumeau-v1.md` (`9044b7b0…`) ; consigne (`27dc81c1…`) | en entier |
| devis v2 (`95989dbe…`), erratum 1 (`8ae6972c…`), contre-lecture du devis (`7423f87b…`) | en entier |
| instruction (`df6d6dfe…`) | l. 45-70, titres |
| attestation sur manifestes, `2f63d6db` (`e3f1ee56…`) | en entier |
| N-076 (`49b664c1…`) ; errata 1-3 (`34a59c49…`, `c2943188…`, `3335284d…`) | l. 1-82, 287-335 ; errata en entier |
| étalonnage v3, `50a6d30c` (`72a2611b…`) | l. 1-34, 46-279, 327-366, 402-405, 466-475 |
| gabarit (`8cad4371…`), `prereg.py` (`3b2e3ee5…`) | en entier |
| prévision complète, brouillon 1 v3 (`deaf1909…`) | titres ; recherche « L2 », « 3 % », « 2 % » |

## Verdict

**Scellable après corrections** : un majeur, six moyens, six mineurs. Validateur : seuls les manques voulus restent ; la ligne du commit, masquée tant que la contre-lecture est vide, est refusée ensuite (essai sur copie). Annexe rejouée : sorties égales au texte, sauf défauts 3 et 11. Tiennent : loi exacte bilatérale, plancher 1/6, accumulation sur les tâches, V(n), puissances, contraintes de la consigne.

## Défauts

1. **Majeur — tables T, E, C ; « Ce que le verdict commande ».** « Chaque ligne est écrite à cinq et à six », mais aucune règle ne dit quelle lecture juge PH-4, PH-5, PH-7 ni déclenche « T1 et E2 ». Correction : cinq décisive (sans l'hypothèse 3), six rapportée.
2. **Moyen — seuil, table T.** Le départage au hasard sert aussi la part entre tâches : sous égalités nombreuses (le coût déclaré peut en avoir), il gonfle la variance intra-tâche et peut réfuter PH-4 (0,30) par artefact. Correction : ρ sur rangs moyens, plancher par permutation.
3. **Moyen — plan 2, étape 0.** « 0,063 à cinq » est faux : 0,0676 sur 40 000 mondes (approximation de Fisher 0,0678) ; l'annexe n'en tire que 1 000. Centrée sur 0,063 ± 0,008, l'étape 0 condamnerait un code juste environ 5 fois sur cent. Correction : 0,068.
4. **Moyen — ligne E3.** « PH-5 confirmée pour la forme » lit un nul comme une confirmation. La bande cumule bornes de ρ et quantiles des mondes, sur les mêmes données : environ ±3 écarts types du taux, E1 quasi impossible sous le modèle. Correction : E3 « non concluante pour le signe » ; taux de E1 sous le modèle mesuré à l'étape 0.
5. **Moyen — point 4.** « Pas de défaut » bloque le scellement, alors que la loi du rang est exacte sans référence : seule l'étiquette de J5 en dépend. Correction : défaut (a) sous 48 heures, comme L2, ou J5 « au-delà de la référence » jusqu'à la réponse.
6. **Moyen — hypothèse 4, arrêt, étape 0.** L'essai « refuse » une sonde apprise sur un épisode lu ; la liste d'arrêt retire la tâche. Rien sur des sondes apprises sur ces tâches (les 60 du premier test sont parmi les 64). Correction : une règle, le retrait ; tâches d'apprentissage à la fiche ; réserve sur PH-4 et PH-7 (b).
7. **Moyen — pont.** 0,10 et 0,02 posés sans échelle. Correction : tolérance de la garde de 7b si elle porte sur des scores de sondes ; sinon garder (réserve seule).
8. **Mineur — phrase gelée de E.** « Le rang n'atteint 1 % qu'à partir de trois tâches » contredit le tirage au sort à la valeur critique : ajouter « sans tirage au sort ».
9. **Mineur — audit R4.** « Part entre tâches nulle » arrive 51 fois sur cent sans effet de tâche (rejoué) : retirer.
10. **Mineur — métrique.** Écrire : original retiré à chaque partage (sinon l'erreur type du témoin est fausse) ; loi nulle sur les tâches lues, non « 64 » ; formule à effectifs inégaux.
11. **Mineur — métrique.** « 5 à 6 % à 64 tâches » : 4,7 % à cinq, 5,9 % à six.
12. **Mineur — ligne V2.** Code corrigé après le scellement : additif sur la ligne du commit.
13. **Mineur — table de principe.** « C'est la loi de la référence honnête » présente le point 1 de N-076 : ses citations obligatoires (§ 11, erratum 3), ou phrase retirée.

## Question 4

Défendables : 0,05/k (Holm possible) ; 3 % et 2 % (lecture rapportée) ; 0,30 et 0,10 ; témoins (1,5 % est à cinq écarts types). À changer avant le scellement : défauts 2, 3, 7 et 9.

## Question 5

Vrais nœuds : point 4 (lecture d'une décision, à rendre non bloquant) ; point 1 (périmètre, défaut déjà écrit). Sans Lazar : 2 (contre-lecture) ; 3, 5, 6, 8, 9 (information) ; 7 (routine).

## Question 6

Incomplète. Ajouter `DECISIONS_LAZAR_VH` (points 1, 2, 4) ; la ligne `GO-2026-11-24-17` vérifiée au registre (citée d'après la consigne) ; dans `FICHE_SONDES_VH` : k écrit, tâches d'apprentissage, score par action sans moyenne ni médiane sur les jetons (sinon nœud).

## Ligne « qui a lu quoi »

> 2026-11-24, 11:41Z à 11:58Z — Claude Opus 5.5, contre-lecteur neuf et aveugle de `prereg/versant-honnete-jumeau-v1.md` (`9044b7b0…`) : a lu la pièce, sa consigne (`27dc81c1…`), le devis v2 (`95989dbe…`), son erratum 1 (`8ae6972c…`), sa contre-lecture (`7423f87b…`), l'instruction (`df6d6dfe…`, § 2-3), l'attestation sur manifestes (`e3f1ee56…`), N-076 (`49b664c1…`, § 0-2, 11-13) et ses errata 1-3, l'étalonnage v3 (`72a2611b…`, hors l. 35-45), le gabarit, `prereg.py`, la prévision complète (`deaf1909…`, par recherche) ; aucun résultat, score, épisode, verdict ni lecture ; rien sous `coffre/`.
