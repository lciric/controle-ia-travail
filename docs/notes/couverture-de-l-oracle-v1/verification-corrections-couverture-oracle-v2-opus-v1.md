# Vérification des corrections de la note sur la couverture de l'oracle (v2)

- **Date** : 21 novembre 2026, 16:14 UTC (`date -u`). Dépôt à `8e449e9fc`.
- **Auteur** : Claude Opus 5.5, le même contre-lecteur que pour la v1 (R-3735), à la demande de la session mère. Pièce de travail (classe C).
- **Contre-lecture de référence** : `contre-lecture-reponse-fable-couverture-oracle-v1-opus-v1.md` (`8f6e49dd10d4e084e6d7408b3d7d30f9e1b30228abec8639fb765e6c40161cb7`).
- **Pièces vérifiées** (compagnons `.sha256` conformes) :
  - `reponse-fable-couverture-oracle-v2.md` (`d95d855462f5398350fb2d3ba5d66fc63e80b887428a42428b5ddf4b9c6b6003`), lue en entier ;
  - `calculs-couverture-oracle-v2.py` (`bccb90a3…`) et `.txt` (`d7097a21…`). Rejoué une fois dans mon bloc-notes (Python 3.13.18) : sortie **identique à l'octet**. Le différentiel avec la v1 se réduit à trois ajouts, contrôlés à la main : l'alinéa sur la sensibilité s à la fin du bloc C (ii) (183,9 divisé par s) ; la dernière ligne du bloc G ; le bloc H, qui reprend la loi du bloc A avec r = w·d (299, 1 497, 2 995, 5 990 retrouvés).
  - `collisionneur-v2/faits-couverture-oracle-v2.md` (`b04cf3791c86dda5…`) et `collisionneur-v2/question-couverture-oracle-v2.md` (`3957729fe86a76e8…`) : empreintes égales à celles que donne la note (§ 6). La garde de motifs (`collisionneur_v9_v3.py`, `850df311…`) rejouée sur les deux fichiers et sur la sous-question du § 7 rend une liste vide.
  - Renvois neufs relus : en-tête de N-060 v3 (« plan de recherche en texte », l. 7) ; Terekhov et al., `docs/sources/pdf/2606.08892v2.pdf`, p. 1 (« proxy “ground-truth” scorer ») : conformes.
- **Toujours non ouvert** : le rapprochement des trois voix et tout chemin contenant « verite ».

## Verdict

**Conforme.** Les quatorze constats sont portés juste ; aucun n'est manquant. Une remarque mineure, non bloquante (R1 ci-dessous), à régler par erratum si la mère le juge utile.

## Constats, un par un

| N° | Porté | Où je l'ai vérifié | Remarque |
|---|---|---|---|
| 1 | juste | Verdict 5 ; § 2 (4) ; § 3.5, point 3 (b') ; § 3.6, supposition 10 ; proposition 3 (test de mort neuf, chances de 0,45 à 0,4) ; § 5, point 4 ; relevé, pas 12 ; bloc H | Le texte proposé est repris et chiffré par le bloc H, qui est juste. |
| 2 | juste | Couple v2 ; § 6 | Le couple ne souffle plus les réponses : le point 3 dit « classées par toi », le point 6 est ouvert, le point 8 ne donne plus de liste, et la phrase « la détection s'écrit » a disparu des faits. Ce qui reste soufflé (les quatre méthodes du point 4, les voies du point 5, la masse manquante, l'exemple de test de mort, et dans les faits ce qui a déjà été proposé) est déclaré au § 6, avec la règle « un accord n'y compte pas ». C'est la seconde branche de ma correction. |
| 3 | juste | Verdict 3 ; § 2 (1) ; § 3.1 (principe et table) ; § 3.4, alinéa neuf ; § 5, point 1 ; § 7 ; relevé, pas 4 | « Vérifier coûte moins que produire » est marqué [de mémoire], comme il convient. |
| 4 | juste (voir R1) | En-tête ; § 3.1, ligne « Floue » ; § 3.2, fiche ; proposition 2 ; relevé ; faits v2 ; question v2, point 2 | Aucune mention de la source ne reste, sauf la déclaration de son retrait. Aucune citation entre guillemets ne vient d'elle. Dans les faits v2, les limites venues de cette source et deux autres, gardées par prudence, sont retirées ; il n'en reste que deux, l'une tirée de N-060 v3 (référence tirée de l'article), l'autre de N-075 (jumeau au banc seulement). La fiche est désormais sourcée à N-060 v3, v4 et à l'erratum 1 ; l'écart entre plan et exécution est rattaché à l'en-tête de N-060 v3, que j'ai vérifié. La phrase sur l'altération subtile a disparu de la proposition 2 et des faits. La v1 et le couple v1 restent au dépôt, non réécrits (R12) ; la note dit que le couple v1 n'est pas à lancer. |
| 5 | juste | § 3.2, « Taille » ; § 3.6, supposition 11 ; § 3.8, point 3 ; proposition 5 (second test de mort) ; § 5, point 4 ; D-4 ; bloc C | Deux chiffres de qualité désormais : σ et le minimum de s. |
| 6 | juste | Verdict 2 ; § 3.7 ; § 3.8, point 1 ; bloc G | Les citations exactes de 9.30 et 9.32 ; le produit et le « seulement si » sont donnés comme une lecture sous le modèle du bloc G. |
| 7 | juste | § 3.1, ligne « Floue » ; relevé | — |
| 8 | juste | § 3.1, ligne « Exécutable » ; « Trouvaille de côté » | Texte proposé, repris mot pour mot. |
| 9 | juste | Verdict 6 ; § 3.3 | « À 95 % simultanément » ; 29 plants pour une strate seule. |
| 10 | juste | Verdict 6 ; § 3.3 ; § 3.8, point 5 ; relevé | — |
| 11 | juste | Verdict 4 ; § 2 ; § 3.2 (ligne « Étalon » dans les deux tables) ; § 3.6, supposition 12 ; § 7 | Appui neuf, vérifié sur PDF : Terekhov et al., p. 1. |
| 12 | juste | § 3.6 | Douze suppositions de défense ; aucun mode opératoire. |
| 13 | juste | D-2 (tranchée, GO-2026-11-21-61) ; proposition 1 ; D-6 ; annexe | Je n'ai pas vérifié l'affirmation selon laquelle « Blindfold » a été « déjà lu en entier pour la décision sur le plancher » : elle est reprise de la v3 de cette décision. |
| 14 | juste | Verdict 1 | — |

## Remarque restante

**R1 (mineur, non bloquant)**, au § 3.2, dans la fiche, ligne « Pièce », colonne « Ce qu'ils ne mesurent pas ». La v2 garde « la persuasion par le texte ». En v1, ces mots partageaient leur cellule avec une citation du rapprochement. De son côté, la v2 retire des faits, « par prudence », la limite voisine (« être persuadés par le texte qu'ils jugent »). Le traitement n'est pas cohérent. L'idée a pourtant d'autres appuis, lus sur PDF ou au dépôt : Libon et al., p. 10 (« accept a benign rationale ») ; et, dans les faits, « ce qui a déjà été proposé » (lire avec et sans le récit de l'agent, pour mesurer la persuasion). Correction proposée, par erratum : « la persuasion par le texte (Libon et al., p. 10 ; mesure déjà proposée : le même plant lu avec et sans récit) ». Rien de cette ligne ne part vers le collisionneur.
