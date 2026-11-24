# Vérification du devis du collisionneur, dossier des questions du directeur du 24 novembre (v1)

- **Nature** : pièce de travail (classe C) ; vérification d'un brouillon de classe A (devis). Aucun appel à un modèle, aucune interface payante, aucune dépense ; seules des pages publiques de tarifs et de documentation ont été lues en ligne. Pièce vérifiée non modifiée. Non commité.
- **Heure** : `2026-11-24T17:26Z` (`date -u`), après l'enregistrement du test de devinette (`test-neutralite-devinette-questions-directeur-v1.md`).
- **Auteur** : Claude Opus 5.5, vérificateur neuf (sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`) ; n'a écrit ni le devis ni ses scripts.
- **Pièce vérifiée** : `devis-collisionneur-questions-directeur-v1-brouillon.md` (empreinte conforme à son compagnon), avec `verif_devis_questions_directeur_v1.py` (`7d16c136…`) et sa sortie (`3e868a76…`).
- **Script de vérification** : `contre_verif_devis_questions_directeur_v1.py`, même dossier, sortie `contre-verif-devis-questions-directeur-v1-sortie.txt` (empreintes dans leurs compagnons) ; `PYTHONDONTWRITEBYTECODE=1 python3 -I contre_verif_devis_questions_directeur_v1.py`, **code 0**, toutes les vérifications tiennent. Il reprend du brouillon les seuls comptes de jetons par cellule. Il recalcule tout le reste avec les tarifs relus : coûts, réglages, chemins, pointes et tableaux.
- **Forme suivie** : `docs/notes/protocole-x-boucle-organisme-controle-v1/verification-devis-v2.md`.

## Verdict

**Devis conforme, avec trois réserves.** Les chiffres du brouillon sont reproduits au dix-millième. Les 18 lignes de ses tableaux concordent au centime. Les tarifs sont confirmés à la source le 24 novembre, et les réglages de Google respectent les trois règles de `CLAUDE.md`. Le plafond séquentiel proposé est juste : 16 USD par bras en option A, 18 en option B. La pointe en envoi parallèle, refaite par programme, confirme le calcul fait à la main : 14,93 et 14,94 USD. La même règle y donne **20 USD par bras**. **Condition** : la question groupée échoue au test de devinette (partie 3). Une fois retouchée, ses tailles changent : il faut relancer les deux scripts et revoir ce devis avant le mot de Lazar.

## 1. Rejeu et concordance des tailles

- `verif_devis_questions_directeur_v1.py` rejoué : code 0, **sortie identique octet pour octet** à la sortie versée.
- Entrées : faits 3 333 octets, 3 235 caractères, 563 mots ; question groupée 9 253, 8 922, 1 479 ; question témoin 2 702, 2 608, 430. Ces nombres sont ceux du brouillon (section 0), et leurs empreintes sont conformes.
- Devis natif du moteur : 15,8928 (principal) et 15,8095 (témoin), soit les 15,89 et 15,81 du brouillon.
- Moteur `collisionneur_v9_v8d.py` (`b7803838…`), garde commune `garde_google_v3.py` (`923679b5…`), relevé `releve-journaux-v2.json` (`52cd710f…`) et `calcul_devis_v8_v3.py` : empreintes conformes à leurs compagnons.

## 2. Tarifs, relus à leur source publique le 24 novembre 2026

| Espèce | Brouillon | Source relue aujourd'hui | Concorde |
|---|---|---|---|
| Carbon (`gemini-4-carbon`) | compté 4 / 20 ; facturé 2 / 10 jusqu'au 30 novembre, 4 / 20 dès le 1er décembre | page de tarifs de Google, relevée à 17:19:00Z (`https://ai.google.dev/gemini-api/docs/pricing`, même contenu sous `aistudio.google.com/docs/pricing`), section « Gemini 4 Carbon », onglet « Standard » : entrée « $2.00 through November 30, 2026. $4.00 starting December 1, 2026. », sortie, réflexion comprise, « $10.00 through November 30, 2026. $20.00 starting December 1, 2026. » ; copie versée `releve-sources-tarifs-20261124T1719Z-v1/page-prix-gemini-api-20261124T171900Z.md.txt` (`3d7b87d6…`) | oui |
| Neon (`gemini-4-neon`) | 3 / 15 | même page, section « Gemini 4 Neon », onglet « Standard » : 3,00 / 15,00 | oui |
| Opus 5.5 | 4 / 20 | page de tarifs d'Anthropic relue à 17:19:21Z (`platform.claude.com/docs/en/about-claude/pricing.md`) : empreinte `488e03e9…`, **identique** à la copie versée le 22 novembre que cite le brouillon ; ligne 23, 4 USD par million en entrée, 20 en sortie | oui |

- La page de Google rappelle que chaque jeton est facturé, réflexion comprise.
- Sortie maximale de 65 536 jetons en synchrone pour Carbon et Neon, selon les pages des deux modèles relevées à 17:20Z (copies versées au même sous-dossier, `c880e69c…` et `b841dd32…`).
- Le palier « Standard » est le bon : le moteur envoie en flux continu, hors lot, et Carbon n'a aucun repli par lot.

## 3. Réglages de réflexion et plafonds de sortie, contre les règles de `CLAUDE.md`

Le script applique une règle écrite indépendamment de la garde commune, puis la garde commune v3. Les deux portent sur le corps réel que produit `demande_gemini` du moteur, au premier envoi et à la relance de chaque tour.

| Règle de `CLAUDE.md` | Carbon | Neon |
|---|---|---|
| Réflexion explicite, au niveau le plus haut admis (page « Gemini thinking » versée, `fe0b8d88…`, relue en ligne aujourd'hui à l'identique, ligne 592 : Carbon admet au plus `high`, Neon `xhigh`) | `thinkingLevel: "high"`, aucun budget | `thinkingLevel: "xhigh"`, aucun budget |
| Plafond ≥ réflexion + 16 000 jetons de texte | 65 536 ≥ 49 152 + 16 000 (texte 16 384) | 65 536 ≥ 32 768 + 16 000 (texte 32 768) |
| Limite de mots dans le plafond de texte (4,2 et 5,1 jetons par mot, mesurés) | 3 500 mots → 14 700 ≤ 16 384 (**marge 1 684**) ; 3 000 → 12 600 | 3 500 → 17 850 ≤ 32 768 ; 3 000 → 15 300 |
| Plafond ≤ limite de l'appel | 65 536 en flux ; hors flux 32 768 : lot refusé | 65 536 ; lot permis, non demandé |

**Épreuve sur cas sain et sur artefacts (règle R5)** : les corps du moteur passent, sans aucun problème, aux deux règles. Cinq mutations par espèce sont toutes refusées, et par les deux règles : réglage de réflexion retiré ; budget ajouté au niveau ; plafond à « provision + 15 999 » ; limite de mots au-delà du texte ; niveau `medium`.

## 4. Comptes de jetons et coûts par cellule

- Attendu, haut et pire des 18 cellules, recalculés aux tarifs relus : écart maximal nul.
  - attendu = entrée attendue × prix d'entrée + sortie médiane × prix de sortie ;
  - haut = entrée maximale × prix d'entrée + 90e centile de sortie × prix de sortie ;
  - pire = garde d'entrée × prix d'entrée + (plafond + provision) × prix de sortie.
- Les tableaux 4.1 et 4.2 du brouillon, lus par programme, concordent au centime (18 lignes, entrée en jetons et cinq montants).
- Les sorties médianes et le 90e centile (relevé des journaux du service v8) concordent avec le relevé, par espèce et par tour.
- Les totaux de la section 5 du brouillon sont repris de la sortie, à l'arrondi près.
  - Option A : 8,64 hors pannes et 10,81 avec pannes ; chemin haut 19,39 ; pire 23,87 sans relance, 71,61 avec toutes relances.
  - Option B : 12,06, 14,55, 23,72, 32,33 et 88,52.

## 5. Pointe et plafond

| | Principal, séquentiel | Principal, parallèle | Témoin, séquentiel | Témoin, parallèle |
|---|---:|---:|---:|---:|
| Option A : pointe (lieu) | 10,8074 (III.3 réponse A, marge du kit) | **14,9347** (lot III.3) | 10,7521 | **14,8616** |
| Option A : plafond = ⌈pointe + 2 × 2,50⌉ | **16** | **20** | **16** | **20** |
| Option B : pointe (lieu) | 12,7971 (III.3 réponse C) | **14,9410** (lot III.3) | 12,7025 | **14,8456** |
| Option B : plafond | **18** | **20** | **18** | **20** |

- **Modèle de l'envoi parallèle** : les trois cellules d'un tour partent ensemble. La marge exigée du lot est la somme de leurs marges : le pire de chaque envoi, ou la marge du kit pour Opus par l'abonnement. La relance d'une cellule coupée part seule, après le lot.
- **Chemin haut** : deux coupures de Carbon, aux tours III.1 et III.2, comme au brouillon.
- **Calcul du brouillon confirmé** : 14,93 et 14,94 USD. Sous le plafond séquentiel, aucune coupure de Carbon de plus n'est tolérée en option A, et une seule en option B (calcul fait par programme).
- **Le moteur v8d envoie en séquence** : `lancer_etage` parcourt les tours puis les lettres, une cellule à la fois. Avant chaque envoi, il refuse si la dépense déjà faite plus le pire de cet envoi dépasse le plafond. La pointe séquentielle vaut donc pour l'option B. Pour l'option A, la voie de l'abonnement (moteur révision 8m) n'a pas été vue, par moi pas plus que par l'auteur : rien ne dit si elle envoie en parallèle.

**Plafond recommandé** :
- **option B** : 18 USD par bras, 36 en tout ;
- **option A** : 16 USD par bras (32) si le lanceur de la voie de l'abonnement envoie en séquence, ce qu'il faut attester avant envoi ; sinon 20 par bras (40).
- Toute commande redonne `--plafond-usd`, qui vaut 40 par défaut.

## 6. Réserves

1. **Réflexion non bornée, texte non garanti.** Le maximum de sortie de Google comprend les jetons de réflexion. La page « Gemini thinking » le dit, lignes 911 à 916 et 1273 : « including thought tokens ». Sous `thinkingLevel`, aucun budget n'est envoyé. Les 16 384 jetons de texte de Carbon reposent donc sur la provision de 49 152, qui est une hypothèse et non une borne. Si la réflexion la dépasse, la réponse s'arrête en `MAX_TOKENS`. C'est un défaut journalisé (code 9), suivi d'une relance identique puis d'un dernier recours. La règle de `CLAUDE.md` est tenue à la lettre. La marge de 1 684 jetons sur 3 500 mots est mince.
2. **Le pire compte deux fois la provision.** Il compte plafond plus provision au prix de sortie, alors que la provision est déjà dans le plafond. Le pire réel d'un envoi de Carbon est d'environ 1,4 USD, non 2,4. C'est une prudence voulue par le moteur ; aucune correction n'est demandée.
3. **Dernier recours de relance au niveau `medium`** (`reglage_de_relance`) : il déroge à « niveau le plus haut admis ». L'écart est déclaré et accordé (R-4664), mais je ne l'ai pas revérifié au-delà de la ligne du registre.
4. **Taux de pannes.** Ceux du brouillon (Carbon 7/56, Neon 1/26, Opus 2/52) sont conformes à leur source, ligne 19.
   - Dans le relevé des journaux, au troisième étage, Carbon a 9 envois interrompus sur 79 (0,114). Il a aussi 4 arrêts « réflexion hors provision », venus d'un réglage antérieur, soit 13 non valides sur 79 (0,165). Opus a 1 interrompu sur 75 ; ses 14 réponses tronquées datent d'un plafond plus bas.
   - Au taux de 13/79 pour Carbon, l'attendu avec pannes monte d'environ 0,57 USD pour les deux bras (11,38 en option A, 15,12 en option B ; calcul de l'auteur sur les pires de la sortie).
   - Les plafonds ne changent pas : ils viennent de la pointe.
5. **Date de l'envoi.** Avant le 1er décembre, Carbon est facturé 2 / 10 : attendu avec pannes de 8,37 (A) et 12,12 (B), ligne d'information du brouillon. Au barème haut, le devis reste prudent.
6. **Sorties tirées d'une autre question.** Les sorties attendues viennent des journaux du service v8, sur une autre question. La question groupée, de 1 479 mots, est plus longue que d'habitude, mais la limite de mots borne le texte de chaque tour ; la réflexion n'est pas bornée (réserve 1).
7. **Observation hors devis** : le moteur porte pour Fable 5.2 un prix de 10 / 50 ; la page d'Anthropic donne 8 / 40. Fable n'est pas dans la composition ; l'écart est à signaler aux mainteneurs du moteur.

## 7. Résumé

| Point | Résultat |
|---|---|
| Rejeu du script du brouillon | identique, code 0 |
| Tarifs (Carbon, Neon, Opus 5.5) | confirmés à la source le 24 novembre |
| Réglages de réflexion et plafonds | conformes aux trois règles ; 10 artefacts refusés sur 10 |
| Comptes de jetons et tableaux | concordent (dix-millième, centime) |
| Attendu avec pannes | A 10,81 ; B 14,55 (confirmés ; +0,57 au taux de pannes de Carbon le plus prudent) |
| Pointe parallèle | A 14,93 / 14,86 ; B 14,94 / 14,85 (calcul à la main confirmé) |
| Plafond | B 18 par bras ; A 16 par bras en séquence attestée, sinon 20 |
| Condition | retouche de la partie 3 de la question, nouveau test à l'aveugle, puis rejeu des deux scripts avant le mot de Lazar |
