# Vérification des corrections — note pour l'entretien, v4 — Opus, v1

- **Date** : 21 novembre 2026, 16:31 UTC (`date -u`). **Auteur** : Claude Opus 5.5, le contre-lecteur de la v3 (R-3735 : vérification des corrections par le même contre-lecteur). Pièce de classe C. Lecture seule hors de ce fichier ; aucun appel payant, aucune requête en ligne, aucun commit.
- **Pièces** : `note-entretien-controle-diffus-v4.md`, `cd593d8f…` (empreinte égale à son compagnon) ; ma contre-lecture de la v3 (`1f51b865…89aa`) ; la v2 du protocole X (`dbe929e7…5db8`, égale à son compagnon), par motifs ; `calculs-controle-diffus-v2.py` (empreinte égale) rejoué une fois dans un dossier temporaire (`python3 -I`), sortie identique à l'octet à `calculs-controle-diffus-v2.txt` (`a7abb7e4…c4c1`) ; bloc A3 inchangé (0,2281 et 0,9962).
- **Revérifié à la page** (`pdftotext`, rang de la page dans le fichier), pour ce qui a changé : Taylor et al. p. 3, 4 (« clear correct answers, not open-ended »), 16, 18, 25 (« single demonstration », « gold-standard demonstrations ») ; Hollinsworth et al. p. 3, 9, 30 ; Boxo et al. p. 1, 8, 9 ; Goldowsky-Dill et al. (`2502.03407v1`, empreinte égale) p. 5 et 6 ; Schaeffer et al. p. 1, 4, 5, 7, 8, 9, 23 ; Westphal et al. p. 9 ; Lucassen et Kaufman p. 1, 2, 10 ; Taufeeque et al. p. 7, 8 ; Terekhov et al. (attaques adaptatives) p. 3, 7, 8, 10, 18, 19, 20 ; papier de l'entretien, version 3, p. 4, 5, 8, 25, 26 ; version 2, p. 24, 25, 68 ; Gao p. 1 ; Jang et al. p. 3.

## Verdict

**Conforme**, avec un constat mineur nouveau. Les vingt-six constats sont portés justes, y compris le refus partiel de I-6, que j'accepte. Lazar peut porter cette note à son entretien, sous trois conditions que la note dit elle-même : compléter les phrases 2, 5 et 9 de la section 3 par qui connaît le banc ; ne dire la suite de la phrase 4 qu'après son mot sur D-1 ; et porter la précision n-1 ci-dessous.

## Constats de la v3

| N° | Porté | Remarque |
|---|---|---|
| I-1 | juste | Phrase 1 et objection 3 conformes aux p. 3, 16, 18, 25 ; « sans doute » rend « arguably ». Ajout juste : tâches à réponse claire (p. 4). |
| I-2 | juste | § 4 et objection 3 : dénégations, 63 % et 93 %, question de suite (p. 3, 9, 30). |
| I-3 | juste | Dite comme une lecture, contre-exemple et réserve « réponse claire » ajoutés. |
| I-4 | juste | Fait 5 et § 4 conformes aux figures 16 (p. 25) et 17 (p. 26). |
| I-5 | juste | Plus la puce « Leurs attaques ne savent pas qu'elles nuisent » : bonne. |
| I-6 | juste, refus partiel accepté | Le refus est fondé : ni le rédacteur ni moi n'avons ouvert le banc ; je décrivais l'état d'après les consignes permanentes. La phrase est maintenant au conditionnel du plan (« décidé ; rien n'y est encore mesuré »), marquée « à compléter », et l'information de N-060 v3 est donnée à Lazar. C'est la bonne forme. |
| I-7 | juste | Fin de phrase remplacée par l'engagement de publier ; § 4 et § 8 citent N-062. |
| I-8 | juste | 79 % et 59 %, 52 % au tableau et 53 % au texte (p. 7, 8), « seul modèle essayé » (p. 9), « fidèle au résumé » (p. 1). Les ajouts de la p. 4 sont exacts (la grille demande de prédire la note d'un moniteur plus faible ; la version raccourcie « could have been written by a RT without any access to monitor scores »). |
| I-9 | juste | Affinage sur traces bénignes et nature des détecteurs (p. 3). |
| m-1 à m-17 | justes | Chacun au lieu dit. m-15 : les sept pages de la concordance sont exactes (« cannot coordinate statefully across sessions », p. 3 ; annexe B.2 commence p. 19). m-16 : la lecture de la ligne GO-2026-11-21-63 est juste ; la confirmation reste à la mère, comme écrit. |

## Constat nouveau

| N° | Gravité | Lieu | Constat | Correction proposée |
|---|---|---|---|---|
| n-1 | mineur | § 5, objection 3, « Pour » | Le 0,983 de Goldowsky-Dill et al. (p. 6) porte sur un jeu où « the system prompt directly instructs the model to sandbag, with a step by step procedure » (p. 5) : l'ordre est dans le contexte lu, exactement la fuite textuelle que Boxo et al. mesurent deux lignes plus bas. Dit sans cette réserve, un juré le retourne. La contre-lecture du protocole X le demandait (« leur rabais […] est à dire »). | « … 0,983 sur un jeu de sous-rendement sous consigne explicite, l'ordre étant dans le contexte (Goldowsky-Dill et al., p. 5-6) ; c'est le cas que la fuite textuelle explique (Boxo et al.) ». |

## La phrase « attaques grossières » dans la v2 du protocole X

**Confirmé.** `reponse-fable-controle-diffus-v2.md`, ligne 282 (phrases à ne pas tenir) : « « Leurs attaques sont grossières » sans dire que c'est la vérité, non le juge faible, qui les voit (p. 25) ». La p. 25 de la version 3 dit « to an outside observer » et montre le modèle faible, employé comme détecteur, signalant les attaques d'origine (figure 16). La v2 du protocole X est à corriger sur ce point, par erratum, avec le texte de la v4, section 4.
