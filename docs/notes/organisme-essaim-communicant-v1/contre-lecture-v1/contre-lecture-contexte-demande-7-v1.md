# Contre-lecture — contexte et demande 7 (essaim qui communique) — v1

Mode d'échec affecté : chiffre sans pièce. Lecteur neuf, hostile, aveugle. Aucun appel, aucune dépense, aucun git, aucune pièce hors liste lue.

**Verdict : Conforme avec réserves.** Tous les chiffres de la section 3 (journaux, monde riche, devis, source descriptive) se rejouent à la pièce citée ; les empreintes recalculées sont toutes conformes. Quatre réserves : une citation d'énoncé fausse (N-045), un gloss attribué à la ligne de GO qui n'y figure pas, un oracle défini sur les seules cartes promues non signalé comme entrée indirecte du juge, une omission dans la source descriptive. Aucune des deux pièces ne porte consigne d'attaque, texte de saboteur, donnée cachée, nom de personne ni revendication de nouveauté sans antériorité.

## 1. Empreintes (recalculées par `sha256sum`)

Conformes à l'attendu : contexte `e767cf40…`, demande `7d3fbcf0…`, lignes GO `08778543…`, PDF `1c1d3d84…` (67 pages, `pdfinfo`), N-044 `2b70bdac…`, N-045 `c7b05e39…`, N-058 `854f2724…`, devis v1 `50e7d2f1…`, devis v2b `b2319472…`, conception v4 `47e38ec0…`, analyse `8a82b5ee…`, sortie JSON `3b65a5e8…` (le contexte dit « non recalculée » ; recalculée ici : conforme), antériorité `c3835fe4…`.

## 2. Table des chiffres (contexte = C ; demande = D)

| chiffre / affirmation | ligne | source citée | rejoué |
|---|---|---|---|
| 2 cartes par appel (estimation), 4 (haut) ; aiguilleur « une par carte » ; deux juges par carte | C9-11 | devis v1 § 2 | oui |
| 3,3 octets/jeton ; 6 000 jetons de sortie (haut 16 000) | C58 | devis v1 § 3 | oui |
| 55 / 110 / 220 appels ; 39,62 et 121,10 USD ; plafond 90 | C58 | devis v2b § 1 | oui |
| score rendu avec coût ; énoncé 2 (N-045) | C14 | N-045 énoncé 2 | oui |
| héritage récompensé, K ≥ 3, bandit à un pas exclu | C15 | N-045 énoncé 5 | oui |
| universalité sur familles inédites | C15 | N-044 énoncé 1 | oui |
| N-058 points 1 et 2 ; « Ce que la décision ne fixe pas » | C19 | N-058 | oui |
| pilote de bruit, test A/A | C23 | N-045 énoncé 6 | oui |
| témoin « un modèle, vote à k, coût apparié » rangé à « énoncé 6 » | C23 | N-045 | **divergent** : il est à l'énoncé 4 (et à « Ce que cela change ») ; l'énoncé 6 porte le pilote de bruit et le test A/A |
| 23 cartes (5+6 ; 6+6) ; 192 suites, 16 essais | C31, C38 | analyse §1 | oui |
| 9/23 = 0,391 ; 11 formes ; 11/23 = 0,478 | C32 | analyse M2 ; JSON l. 282, 287 | oui |
| 0 carte sur 23 identique à une plantée du monde | C33 | analyse M1, E1 | oui |
| oracle 12/6/6/0 et 11/5/5/0 ; promues toutes en génération 1 | C34 | analyse M1 | oui |
| coût par carte 0,027 à 0,067 ; 1,429736 (11 cartes) ; 0,564574 (12) | C35 | analyse M1 ; JSON l. 46, 154, 203, 253 | oui |
| M3 « indécidable » sur S1 | C36 | analyse §3 | oui |
| M4 : 0,415/0,320 et 0,360/0,166 | C42 | analyse M4 ; JSON l. 949, 962, 1501, 1514 | oui |
| « aucune règle de différence entre bras » (écart E5) | C42 | analyse E5 | oui avec réserve : E5 vise la différence de M3 ; pour M4 le texte ne fixe pas non plus de règle, mais E5 n'en parle pas |
| E4, E10, audit de symétrie | C41, C43 | analyse §3, §4 | oui |
| part marginale 0,0195 (14) contre 0,47 (18) | C49 | conception v4 § 4.3 | oui |
| garde : 8/12 avec masquage, Wilson [0,39 ; 0,86] ; 0/12 sans ; 0,02 « estimé, aucune pièce » | C50 | v4 § 4.2, § 3.2 | oui |
| progrès certifié 8/12 ; génération 3 : 1 monde ; fausses 36/204 (17,6 %) | C51 | v4 § 4.4 | oui |
| devis central 41,11 ; pire 363,00 et 56,20 ; plafonds 365 et 57 | C52 | v4 § 5 | oui |
| 200 articles « d'une conférence d'apprentissage automatique » ; Re-Search arXiv 2611.14487v1, 10 novembre 2026 | C62 | antériorité JSON l. 183-186 | oui avec réserve : la source dit « Built from 200 ICML » (résumé tronqué à 500 caractères) ; « articles » et « conférence d'apprentissage automatique » sont une glose |
| antériorité générer/vérifier depuis 2023, Re-Search ne la cite pas, limite de débit | C69 | JSON l. 949-950 | oui |
| deux mesures de Re-Search (branches ouvertes ; score au tour k) | C64-66 | « mot du directeur » | hors mandat (PDF de Re-Search non lu, déclaré par la pièce) ; orphelin mais étiqueté |
| 936 agents, 35 laboratoires, 936 études, 9 500 messages, 229 salons, douze semaines | C75 | PDF p. 1 | oui |
| observationnelle et non randomisée ; deux cinquièmes ; deux tiers | C76 | PDF p. 6, p. 34 | oui |
| « travaux voisins évaluent un agent isolé ou une équipe orchestrée » | C77 | PDF p. 32 | oui |
| 88 % contre 30 % ; sans scores le troupeau cesse ; figure 12 | C78 | PDF p. 22, figure 12 p. 21 | oui |
| 15,7 points de plus, 35 % de jetons en moins | C78 | PDF p. 22 | oui |
| comité 3,5 fois plus bas « à calcul égal » | C78 | PDF p. 22 | oui |
| 72 heures : 0,83 et 0,26 ; au moins une semaine | C81 | PDF p. 12 | oui |
| autocritique contre vote majoritaire, « non résolue », 48 citations | C79 | PDF p. 11 | oui |
| gains concentrés sur la première itération ; D1 | C79 | PDF p. 34, p. 64 | oui |
| revue du texte seul a manqué des défauts | C82 | PDF p. 33, p. 34 | oui |
| 67 pages | C73 | `pdfinfo` | oui |
| ≈ 2 480 mots (rapport) | rapport | `wc -w` : 2 488 | oui |
| « messages, mémoire partagée, revue entre pairs » comme mot du directeur à la ligne GO-2026-11-22-12 point 4 | C88, D3 | lignes-go-12-et-15.md | **divergent** : la ligne dit seulement « agents qui communiquent, mêmes agents isolés, agent seul » ; le gloss entre parenthèses n'y est pas |

Aucun autre chiffre orphelin. Les pièces marquent honnêtement « rapporté » ou « non vérifié » ce qui n'est pas rejoué (protocoles des études de la cohorte, aiguilleur, type du juge, mesures de Re-Search).

## 3. Réponses courtes

**La demande 7 sert-elle fidèlement la décision ?** Oui sur le fond : trois configurations (communiquent, isolés, seul), même coût, jugées par l'oracle du monde planté et le coût, jamais par le juge (D3, D10 point 5, point 2 « aucun verdict du juge dans un choix d'agent ») ; N-058 est citée correctement. Deux réserves : (i) le gloss « messages, mémoire partagée, revue entre pairs » n'est pas dans la ligne servie ; (ii) l'oracle de la course réelle est « défini sur les cartes promues seulement » (C12, C34), donc conditionné par le verdict du juge ; la demande (D10 point 5) exige « sur l'oracle seul » sans dire au concepteur que cette forme d'oracle laisse entrer indirectement le juge dans la comparaison des agents (esprit de N-058) ; à lui faire traiter (oracle par carte, promue ou non).

**Consigne d'attaque, texte de saboteur, référence cachée, nom de personne, nouveauté sans antériorité ?** Non. Aucun nom de personne (grep : seulement « alphaXiv », plateforme). Les lignes 38-43 du contexte décrivent par ses seules mesures une épreuve du juge où le proposeur voit ses verdicts : description, pas consigne. Aucune loi d'un monde secret (famille MR-2 déclarée publique, v4 § 2.2). Pas de revendication de nouveauté pour nous : la ligne 84 pose une zone « question (R8) » et D15 demande l'antériorité ; D3 « notre plan doit apporter la comparaison contrôlée » est une visée, non une revendication, mais D3 dit « sans comparaison randomisée de la société à un agent seul (p. 6, p. 32, p. 34) », plus fort que les pages (elles disent « observationnelle, non randomisée » et ce que d'autres plateformes évaluent) ; le contexte lui-même (C77) dit que les annexes n'ont été que parcourues.

## Relevé de méthode

**Chaîne de raisonnement.**
1. Empreintes des 13 pièces recalculées : toutes égales à l'attendu (`sha256sum`).
2. Chaque chiffre du contexte rattaché à sa pièce (table ci-dessus) : décisions N-044, N-045, N-058 lues en entier ; devis v1, v2b et conception v4 lus en entier ; analyse lue en entier ; douze valeurs de la sortie JSON retrouvées par `grep`.
3. Chiffres du PDF retrouvés dans `pdftotext -layout` avec page déduite des sauts de page (`awk`) : p. 1, 6, 11, 12, 21, 22, 32, 33, 34, 64.
4. Gloss de la ligne GO comparé à `lignes-go-12-et-15.md` : absent.
5. Énoncé N-045 du témoin « vote à k » : énoncé 4 (lignes 66-69 de N-045), non 6.
6. Oracle « promues seulement » : analyse § 1 (S1) et E2 ; contexte ligne 12.

**Objets de contrôle.** Faux par construction : le gloss « messages, mémoire partagée, revue entre pairs » ; attendu : introuvable dans la ligne GO ; rendu : introuvable (cassé). Vrai par construction : « 88 % contre 30 % » ; attendu : retrouvé dans le PDF ; rendu : retrouvé aux pages 22 et 21 (figure 12). Le mécanisme (recherche textuelle sur pièce) distingue les deux.

**Premier pas non justifié.** Le pas 3 pour la page 21 contre 22 de la figure 12 : le contexte écrit « p. 22 ; p. 21, figure 12 », retrouvé, mais la numérotation du PDF (saut de page) et la pagination imprimée diffèrent d'une unité ; ce qui le justifierait : lecture de la page 21 en image. Sans incidence sur le verdict.

**Mode d'échec affecté.** Chiffre sans pièce : tenu, sauf trois points cassés : la citation d'énoncé N-045 (6 au lieu de 4), le gloss de la ligne GO, la formulation « sans comparaison » de la demande plus forte que les pages citées.

**Trouvaille de côté.** (1) Le PDF rapporte aussi que l'agent seul (planificateur) a fixé un pic médiocre et trouvé l'optimum dans 2 % des essais contre 42 % pour l'aléatoire et 73 % pour l'optimisation bayésienne (p. 22) : donnée directement utile au bras (c) agent seul, omise du contexte. (2) Le JSON d'antériorité dit « aucun PDF téléchargé » (l. 6) mais son `constat` dit « pages 10 à 13, lues entières » (l. 950) : incohérence interne de la source de la note, non poursuivie. (3) Le contexte attribue les trois configurations au « mot du directeur » alors que la ligne les décrit en réponse à des recommandations de Fable (ligne GO point 4) : provenance à préciser.

**Évaluateur et conseil.** Ce qui juge ma contre-lecture : le recalcul d'empreintes et la recherche de texte sur pièces, sans témoin d'admission externe ; je pourrais avoir manqué un chiffre non pointé par l'auteur ; je n'ai pas rejoué le code de l'analyse ni lu `registres/go.md`. Bon jugement non mérité possible : un chiffre juste mais d'une pièce voisine que je n'ai pas lue (par exemple la sortie JSON hors des douze valeurs vérifiées).
