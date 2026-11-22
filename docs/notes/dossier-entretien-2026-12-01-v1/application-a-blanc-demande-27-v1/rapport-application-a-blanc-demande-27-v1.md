# Application à blanc, par programme, de l'erratum interne et des différences du programme v3 (demande 27) — rapport v1

- 2026-11-22T18:12:39Z (`date -u`). Session fille « dossier de l'entretien du 1er décembre » (accord GO-2026-11-22-113), modèle Opus 5.5. Pièce de classe B (instrument : un programme d'application) avec ses sorties ; **rien n'est scellé comme texte en vigueur, rien ne remplace le programme v2** : la décision 1 de la réponse 27 (sceller maintenant, provisoirement, ou après les simulations) reste à Lazar.
- Ce contrôle est celui que Fable recommande en option (a) de sa décision 1 et en tête de « ce qu'un expert ferait » : chaque ANCIEN trouvé exactement une fois, application dans l'ordre, puis recherche des renvois orphelins.
- Aucun résultat de mesure lu.

## Entrées

| pièce | chemin | sha256 |
|---|---|---|
| réponse 27 de Fable (clé Luc, R-4849) | `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-27-luc/relecture-fable-api.md` | `6a042a7b…` (compagnon vérifié) |
| réponse 4 | `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-4/relecture-fable-api.md` | `cf55c7e0…` |
| réponse 8 | `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-8/relecture-fable-api.md` | `d81a74d3…` |
| note des problématiques v1 (original, non la copie sans nom servie à Fable) | `docs/notes/note-problematiques-programme-v1/note-problematiques-programme-v1.md` | voir compagnon |
| programme v2 | `docs/programme-controle-ia-v2.md` | `2fd63bad…` |

Programme : `appliquer_erratum_demande_27_v1.py` (ce dossier). Lancement : `python3 appliquer_erratum_demande_27_v1.py <réponse 27> <dossier de sortie>`, depuis la racine du dépôt. Rejoué deux fois : sorties identiques à l'octet.

## Résultat du contrôle

- **43 blocs** lus (8 pour la réponse 4, 6 pour la réponse 8, 10 pour la note des problématiques, 19 différences du programme), conformes aux comptes annoncés par Fable (31 entrées d'erratum, dont 7 de la section 3 renvoyées aux différences 5 à 11 ; 19 différences).
- **Chaque ANCIEN est trouvé exactement une fois** dans la pièce d'origine, et encore exactement une fois au moment de son application (aucun chevauchement entre corrections successives).
- **Un NOUVEAU non littéral** : la troisième correction de la réponse 8 dit « la thèse retenue, écrite en D3 de la pièce 2 ». Le programme l'applique avec le texte NOUVEAU de la différence 3, entre guillemets comme l'ANCIEN. À confirmer par Fable ou Lazar.

## Sorties (brouillons d'application, non en vigueur)

| fichier | sha256 |
|---|---|
| `programme-controle-ia-v3-application-a-blanc.md` | `5fcbe3f6dfa621aa0def9d911169465e7c9b2ad191542658cd60a79501cbd04a` |
| `note-problematiques-programme-v2-application-a-blanc.md` | `41754165c332c68cf4c95134e94cf56a689969555ddb02b82f09c2d21d3259d1` |
| `reponse-4-corrigee-application-a-blanc.md` | `36584ecf73bbe276c6dfd908063f4d6a677a9f7c6a38c790237b91d7283e1080` |
| `reponse-8-corrigee-application-a-blanc.md` | `0908c5210da58c57c5a629cc4bea32ce7c491ead46d2fc56761934242fc30544` |

## Renvois orphelins trouvés après application (recherche par mots : lemme, théorème, co-auteur, additivité, marge asymétrique, δ > 0)

Programme v3 appliqué à blanc :
1. Section 1, point 2 : « Colonne vertébrale théorique : lemme d'additivité interne + théorème négatif » reste en tête de la phrase ; seule une parenthèse finale dit la colonne retirée (différence 2). Lecture ambiguë.
2. Décision D-b : « lemme tenté seul ; la question d'un co-auteur en analyse séquentielle est revisitée à G1 » (Fable l'avait signalé).
3. Section 3 : le paragraphe « Additivité interne » (« la preuve interne s'additionne ») et les hypothèses (a) et (b) de l'ancien lemme restent sous le nouvel intitulé, sans marque de statut propre.
4. Section 3, « Hypothèse empirique pivot » : garde « déplace-t-il la marginale des scores (δ > 0) ? » avant la question Q.
5. H6, marge asymétrique (0,66), et l'expérience E1.6 : retirées des revendications par N-077, encore présentes (Fable l'avait signalé ; hors périmètre de la demande).
6. Phase 0 : « simulation du lemme et du théorème négatif » (Fable l'avait signalé).
7. E1.4 « Théorème négatif en semi-synthétique » : non touchée.
8. Section 15 : « Co-auteur en analyse séquentielle pour le lemme (revisité à G1) » (Fable l'avait signalé).

Note des problématiques v2 appliquée à blanc :
9. Table, ligne « A, complémentarité » : garde la forme conditionnée sur les manqués de la meilleure boîte noire, que l'entrée EN-7 corrige ailleurs (« à taux total de fausses alertes égal »).
10. Table, ligne « A, lemme d'additivité, reste » : garde « garantie (théorème) » et « revendication resserrée, à démontrer » ; l'entrée EN-4 annonçait « même correction » pour cette phrase, mais la lettre de la table diffère et le programme ne la touche pas.
11. L'en-tête garde « Écrite le 22 novembre vers 06:05 UTC » : une v2 doit dire sa propre date et qu'elle applique l'erratum de la réponse 27.

## Ce que ce contrôle ne dit pas

Il ne juge pas le fond des textes NOUVEAU (trois portent une hypothèse non simulée, selon Fable : différences 5, 7 et 16). Il ne cherche pas les 24 phrases dans tout le dépôt (décision 4 de Fable). Il ne vaut pas scellement.
