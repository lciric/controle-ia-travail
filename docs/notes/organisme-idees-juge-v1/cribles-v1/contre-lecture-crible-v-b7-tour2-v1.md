# Contre-lecture du crible (v), brouillon 8 (tour 2 de la boucle B7) — lecteur C

Lecteur : modèle C, neuf (n'a écrit aucune pièce). Pièce : `crible-v-brouillon8.md`, empreinte `8047040ba7b8268ac26e20a41406a71fa72e474ca303e9e60e1c686a55153d82` (égale à son compagnon). Précédente : `crible-v-brouillon7.md`, `083a322de48bc12d1ac250d8687f304dcf876bfcfd557bd84e154d7321a232b1`. Rapport corrigé : `contre-lecture-crible-v-b7-tour1-v1.md`, `7dd672353ce772bd4a80bfeba8030cad83eb410ecd6df0156183643415f14347` (égale). Lecture du 2026-11-16, 15:25Z à 15:30Z (`date -u`). Rien lu sous `diag/`, `runs/`, `donnees/` ; aucun appel, aucune dépense, aucun fichier existant modifié.

## Verdict : **corrections** (1 majeure, 2 mineures, 2 remarques facultatives). Pas de « a_refaire ».

## 1. Application des corrections du tour 1 : fidèle
`diff brouillon7 brouillon8` : 17 zones, toutes expliquées. Les 12 couples B7-01a, B7-01b, B7-02a, B7-02b, B7-03a à B7-03e, B7-04, B7-05a, B7-05b sont appliqués mot pour mot (chaque « nouveau » retrouvé dans le diff à l'endroit de son « ancien ») ; aucun ancien résiduel (« 34 à 42 », « 107 à 126 », « 37 à 39 », « 1,7 à 2,1 », « Dans l'enveloppe » : absents ; « presque sûrement » ne reste que dans la réponse du rédacteur). Les six couples propres (titre, en-tête, statut, validateur, tête de section, entrée « Contre-lecture 7 ») sont les seuls autres changements ; l'entrée porte les deux empreintes entières, exactes. Aucun critère, seuil, graine ni décision de R-2992 touché hors les endroits demandés. `controle_ia.prereg.problemes` : liste vide. Programme `appliquer-corrections-crible-v-brouillon8.py` : empreinte égale à son compagnon.

## 2. Vérifications refaites sur les passages touchés
- **Devis** : 20 × 4 = 80 appels ; pires cas 46,80 + 40 + 46,80 + 60 + 3 = 196,60 (crédits 100 ; hors 96,60) ; + sonde neuve 8,07 = 204,67 ; 204,67 − 183 = 21,67 ; 196,60 − 183 = 13,60. Compte de la configuration : Pr-1 1,75 à 2,25 par appel, 35 à 45 ; hors crédits 68,35 à 79,55 ; total 107,95 à 128,75 (≈ 108 à 129) ; part 36,7 à 38,2 % (≈ 37 à 38). Fourchette publique 79,95 à 92,75 ; part 49,5 à 53,0 % (« 50 à 53 » : arrondi acceptable). Le plafond de 2,34 pour deux proposeurs est cohérent avec le bloc gelé (déjà établi au tour 1). La formulation sur l'enveloppe de GO-2026-11-15-06 (« appartenance non acquise », cumul à tenir sous 1 275, sinon nœud de Lazar) est conforme à R-2992 point 3.
- **Gel de l'étape 2** : la phrase est maintenant lisible ; la seule exception nommée est la ligne « coût d'un appel » ; empreinte entière du texte gelé et liste des écarts exigées. Rien d'ouvert après lecture.
- **Annexe A, sortie 4** : 0,7481 ; 0,9147 ; 0,9831 ; 0,9985 correspondent aux arrondis de la section « Taille ».
- **Minimum, étage 1** : définitions de « fournisseur » (trois voies) et de « perdu en entier » présentes, déterministes. Le monde complet (un appel répondu par moitié) fait que la perte d'un seul fournisseur après un premier appel répondu laisse le minimum possible : cohérent.
- Étage 0 : la ligne « fournisseur abandonné » reste exclue de l'étage 0 (lue à l'étage 1) : cohérent avec la nouvelle règle.

## 3. Corrections exigées

### Majeure

**C8-01 — La ligne d'arrêt « fournisseur abandonné… » : l'essai sain et l'artefact ne sont plus justes sous la règle écrite par B7-02b (R5).** Sous la règle nouvelle : (i) l'essai sain « panne d'un appel : le crible continue » est faux si l'appel en panne est le tout premier du fournisseur (aucun appel répondu : le fournisseur est abandonné et perdu en entier, donc arrêt) ; (ii) l'artefact « panne de tous les appels d'un fournisseur au monde 3 : arrêt » n'arrête rien si le fournisseur a répondu aux mondes 1 et 2 : le minimum reste possible (chaque moitié garde un proposeur) et l'abandon n'est pas une perte entière ; la garde ne déclencherait donc pas sur son propre artefact. Le rédacteur du tour l'a lui-même relevé et laissé. Une garde dont l'artefact ne tire pas viole R5 ; elle fixe aussi l'instant d'arrêt, donc la dépense. Un couple (cellules « essai sain » et « artefact » ; l'ancien figure une seule fois) :

`C8-01`
```
ANCIEN: | panne d'un appel : le crible continue | panne de tous les appels d'un fournisseur au monde 3 : arrêt |
NOUVEAU: | panne de relais d'un appel d'un fournisseur ayant déjà répondu à un appel, minimum encore possible : le crible continue, appels restants de ce fournisseur « échec » sans être lancés | panne de relais du tout premier appel d'un fournisseur (aucun appel répondu) : arrêt ; panne d'un fournisseur au monde 3 simulée de sorte que le minimum de mondes complets devienne impossible : arrêt |
```

### Mineures

**C8-02 — La grille de l'annexe A (point 11) suppose des appels indépendants et aucun abandon ; la pièce ne le dit pas.** Les probabilités 0,75 à 0,9985 de « atteindre le minimum » ignorent que, selon la règle du pilote, une seule panne de relais abandonne la voie pour tous les mondes restants ; la probabilité d'arrêt par abandon, dominante pour la voie à 40 appels (Pr-2 et Pr-4), n'est pas dans la grille. Un lecteur pourrait y voir la probabilité du crible d'aboutir. Un couple :

`C8-02`
```
ANCIEN: (à lire sur le taux du pilote, à titre d'information)
NOUVEAU: (à lire sur le taux du pilote, à titre d'information ; la grille suppose des appels indépendants et ne compte pas l'abandon d'un fournisseur après une seule panne de relais : la probabilité que le crible aille à son terme est plus basse, non chiffrée ici)
```

**C8-03 — Entrée « Contre-lecture 8 » à écrire par le rédacteur** (couples propres, non fournis) : lecteur C neuf, heures 15:25Z à 15:30Z, empreinte **entière** du présent rapport (lue dans son compagnon après scellement) et celle du brouillon 8 relu (`8047040ba7b8268ac26e20a41406a71fa72e474ca303e9e60e1c686a55153d82`), verdict et comptes ; titre « brouillon 9 », en-tête, statut (« contre-lu huit fois »), tête de section ; sans quoi `problemes` rend un défaut.

### Remarques facultatives (non exigées)
- **F-B8-1** : un fournisseur dont tous les appels sont tronqués ou refusés (donc « perdu en entier ») sans panne de relais n'est pas « abandonné » : aucune ligne n'arrête, le crible dépense jusqu'au bout pour une issue acquise à l'étage 1. On pourrait ajouter une ligne : « fournisseur sans aucun appel répondu après les trois premiers mondes : arrêt ». Perte limitée à la dépense ; la décision est celle de la mère.
- **F-B8-2** : les remarques F-B7-1 à F-B7-6 restent ouvertes, telles que transmises par le tour précédent (V4 en mesure rapportée, risque « non lançable », tension avec N-058 pour l'archive « toutes les cartes de la génération 1 », programmes de l'annexe à déposer).

## 4. Points déjà tenus (non rejoués)
R1 complet, N-058 borné, partie A descriptive, graines par `SeedSequence`, antériorités à chercher, aucun identifiant de modèle, durée par monde (règle B_a, M ≤ 2, « non lançable » sinon) : relus aux endroits touchés seulement ; rien de dérangé. La durée exige, comme dit dans la pièce, un code et une configuration neufs (concurrence M des relais non éprouvée) : c'est ce qui fixe la date de lancement, dans la fenêtre du GO qui échoit le 30 novembre.

## 5. Incidents
Aucun. Rien de lu hors de la liste ; pas de `pytest`, pas de fichier existant modifié.

## 6. Points pour la mère
1. **Règle d'abandon du pilote** (une panne de relais abandonne la voie, sans reprise) : même après C8-01, une panne passagère au premier appel d'une voie termine le crible à l'étage 1 ; la voie de crédits sert deux proposeurs. Si Lazar ou la mère préfère une règle plus tolérante (une reprise), c'est un mot avant scellement ; je ne l'invente pas.
2. **Enveloppe** : 204,67 USD au pire pour ce crible ; le cumul des cinq reste à refaire avant toute ligne « calcul » (R-2992 point 3).
3. **Scellement** : après application de C8-01 à C8-03, un tour différentiel limité à ces endroits suffit ; les anciens ci-dessus figurent une seule fois dans le brouillon 8.
