# Passation — rédacteur Opus du préenregistrement v11 de la course d'affinage : brouillons 4 à 6, devis v11c à v11e

- Écrite le 2026-11-23T05:55:28Z (`date -u +%FT%TZ`), sur la branche `prep/preenregistrement-affinage-v11-opus-v1`, née de `prep/preenregistrement-affinage-v8-v1` à `d8e7d8f3`. Elle suit les passations du rédacteur Fable (`2026-11-22-1855-…`, son erratum 1, `2026-11-22-1958-…`, `2026-11-22-2034-…-brouillon-3.md`), qui restent en place.
- Rédacteur : Opus 5.5 en effort maximal, session neuve, sur GO-2026-11-22-145 (quota de Fable épuisé jusqu'au 2026-11-29T18:00Z, R-5071) ; écart à R-3735 et à GO-2026-11-21-75 déclaré dans chaque pièce. Consigne de la session de l'organisme (`session_013QMaymD1EsQJ68Qivpubes`), le 2026-11-23 : décisions 1 à 7 (réglages d'Argon, Carbon, libellé, déclencheurs, relevé des crédits, GO de la course, le reste comme au brouillon 3), inscrites depuis sous R-5130 au registre des décisions de `main` ; puis quatre messages de la même session (ci-dessous), dont les décisions datées 05:45Z (à inscrire par la mère avec R-5130). Aucun appel à un modèle externe, aucune dépense, aucune instance lancée.

## Fait

Pièces écrites et scellées (compagnons vérifiés par `controle_ia.scellement verifier`), sous `docs/notes/organisme-affinage-mentors-v1/` :

| pièce | chemin | sha256 | commit |
|---|---|---|---|
| brouillon 4 du préenregistrement v11 (329 lignes ; non scellé comme préenregistrement) | `course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-4.md` | `dc711f945276755110aff48fad913590ba0f041d8c28f45b8f7e2441cffbd05d` | `8a5584e1f` |
| programme d'assemblage du brouillon 4 | `course-v11/assembler-brouillon-4-preenregistrement-v11.py` | `ddec4b6832958c01fa29484c2b2f8f69f04641162ce2bf152ae0896861541ca2` | `8a5584e1f` |
| devis v11c | `devis-course-affinage-mentors-v11c.md` | `94f7f378c36e6af70a05166c9b26e9b012e9a44c7cd4df2ce059fa13a653bb2e` | `8a5584e1f` |
| programme de calcul du devis v11c (176 chiffres contrôlés, aucun écart ; vaut pour le devis v11d) | `course-v11/calcul-devis-course-affinage-mentors-v11c.py` | `bb52afbcc24cffa591c1ef42473ebd2a9aba9fc5aeb9bc4bf992bdd91e968e5f` | `8a5584e1f` |
| **brouillon 5** du préenregistrement v11 (330 lignes ; non scellé comme préenregistrement) | `course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-5.md` | `3fd9267fd364a9e595d300061def1b858cd0c28a0af2ac4f84fe5cd3a66b0163` | `00315438d` |
| programme d'assemblage du brouillon 5 | `course-v11/assembler-brouillon-5-preenregistrement-v11.py` | `938a86a84ccfe2865eef13855127af73b31e231e501852b3980f331e9cd0a7a9` | `00315438d` |
| **devis v11d** (le v11c sans chiffre changé : R-5130, lanceur v11d, mesure d'Argon avec et sans) | `devis-course-affinage-mentors-v11d.md` | `daf218f260f835a755db63cf1bc214c44a23dbe5880a23bb3d1520f98d5bad7d` | `00315438d` |
| **brouillon 6** du préenregistrement v11 (333 lignes ; non scellé comme préenregistrement) | `course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-6.md` | `a8de23b50e0e359e0cf45caf143674a845ceeed2958b9aa1e209cef4c8f95b3d` | `cf697a9e1` |
| programme d'assemblage du brouillon 6 | `course-v11/assembler-brouillon-6-preenregistrement-v11.py` | `ba163d554bcf21324815ec35a0d70199319115125ddf7a6391ca31b76016c5c4` | `cf697a9e1` |
| **devis v11e** (le v11d plus la mesure d'Argon fixée : 4,58 USD au pire sans reprise, seuil 31 462) | `devis-course-affinage-mentors-v11e.md` | `c824fb2b4493f595dcdb2b05d01a3a72a75326deb540153033767ef6c313192b` | `cf697a9e1` |
| programme de calcul de la mesure préalable d'Argon (19 chiffres contrôlés, aucun écart) | `course-v11/calcul-mesure-prealable-argon-v11e.py` | `6416e1c56c2cde540221e3bd54f31e4fde81b4db9fdc1c7043c97fbec915dc04` | `cf697a9e1` |

Les brouillons 1 à 5, les devis v11 à v11d et leurs programmes restent en place (R12). Pièces de départ vérifiées à leur compagnon : brouillon 3 `af226efa…`, devis v11b `13d962b1…`, mandat `0f7ddc54…`, contre-lecture du lanceur v11b `cd7e5455…`, page de Google `fe0b8d88…` ; pièces scellées du lanceur v11c (`1ed883749` sur `prep/lanceur-affinage-v11c-interrompu-v1`) vérifiées à leur compagnon.

Rejeux, à l'octet près :
- `python3 -I course-v11/assembler-brouillon-4-preenregistrement-v11.py course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-3.md <sortie> 2026-11-23T05:22:30Z` ;
- `python3 -I course-v11/assembler-brouillon-5-preenregistrement-v11.py course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-4.md <sortie> 2026-11-23T05:40:12Z` ;
- `python3 -I course-v11/assembler-brouillon-6-preenregistrement-v11.py course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-5.md <sortie> 2026-11-23T05:54:27Z`.

Contrôles du brouillon 6 : 17 sections identiques à la v10 ; lignes 1 à 295 du brouillon 5 gardées à leur numéro (12 touchées), point 16 et dernière section récrits ; 14 « EMPREINTE À INSCRIRE » et 4 « RÉFÉRENCE À INSCRIRE » (décisions datées 05:45Z, à inscrire) ; seul nombre neuf, 4,58, retrouvé dans la sortie du calcul de la mesure ; chaque nombre neuf du devis v11e retrouvé dans les sorties des deux programmes de calcul ; renvois « devis v11, § n » retrouvés dans le devis v11e. Contrôles du brouillon 5 : 17 sections identiques à la v10 scellée (`7fc71712…`) ; lignes 1 à 295 du brouillon 4 gardées à leur numéro (29 touchées ; l'annexe `abb967a9…` reste valable), point 16 du différentiel à la ligne 296, dernière section récrite ; aucun « RÉFÉRENCE À INSCRIRE » ni « RÉGLAGE À INSCRIRE » restant ; 14 « EMPREINTE À INSCRIRE » ; seuls nombres neufs par rapport au brouillon 4 : un numéro de ligne (296), une confiance (0,6) et une heure ; chaque renvoi « devis v11, § n » retrouvé dans le devis v11d ; R-5130 relu sur `main` (`dbafadaae`, inchangé à `27dced074`). Contrôles du brouillon 4 : comme dit au commit `8a5584e1f` (17 sections identiques à la v10 ; chaque nombre neuf retrouvé dans la sortie du calcul v11c ou dans une pièce citée).

## Faits trouvés en chemin (portés à la session de l'organisme)

1. Le lanceur v11c garde trois contrôles des v8 et v9 sur Carbon (provision ≥ 25 870, sortie ≥ 24 500, délai ≥ 1 500 s) que le brouillon 3 disait retirés : texte aligné sur le code.
2. Il rejoue la garde de Google sur la seule entrée la plus longue de chaque rôle (plus la plus courte) et contrôle la limite de l'invite en caractères (la commande ne reçoit aucune limite de mots) : texte aligné.
3. Pire cas d'un juge d'Argon : 0,917240 USD au lanceur v11b, 0,917356 au v11c (entrée de juge de la forme de l'orchestrateur, 11 596 caractères) ; les deux sont cités.
4. Aux réglages du lanceur, le seuil de coupure par la réflexion d'Argon (32 476 jetons de moyenne) est sous la sortie maximale (45 056) : la phrase « pas de prise réaliste » est retirée ; le motif de R-5018 pour dire sans objet la mesure de GO-2026-11-22-128 ne tient plus.
5. Argon n'a jamais été servi au-delà de 32 768 jetons de sortie (en-tête de la garde commune) : risque pour la tentative unique, dit au texte.
6. Configuration v11c scellée : notes `changements_v11.carbon` et `.argon` qui citent `commande_gemini_flux_v1.py` ; champ inerte `relais_persistants_v4.plafond_relais_claude_usd` = 150 (corrigés en v11d selon la session de l'organisme, non lue).
7. Base de l'écart au devis : 35,683407 exacte, 35,683424 au lanceur (prix par appel arrondis d'abord) : même valeur au millième.
8. Le seuil de 32 476 jetons vaut pour la moyenne des 176 appels d'Argon (16 de proposeur, 160 de juge) : la règle de lecture de la mesure prend donc la moyenne pondérée comme dans la course, et non celle des seuls juges (devis v11d, § 4).
9. Le lanceur v11c lit le relevé du prix Claude du jour (`RELEVE_PRIX`, l. 389 : `course-v11/releve-prix-claude-course-affinage-v11.json`), jamais un gabarit : emplacement du gabarit retiré.
10. Une reprise après un échec de la génération est comptée par la commande en flux v2 à son pire cas (« pire cas dès que la requête de génération est partie, sauf usage lu ») : quinze envois de la mesure feraient 13,74 USD comptés, au-dessus de la ligne de 10,50 ; la ligne borne donc la mesure (au plus onze envois comptés à leur pire cas).
11. Avant la course, aucune fiche n'existe pour le juge : « la première fiche dans l'ordre épinglé » est écrite comme la première fiche acceptée de la réponse de l'appel de proposeur de la mesure (lecture du rédacteur, faite sur la v53 des fonctions de fiches, à confirmer sur la v54 épinglée).

## Échanges avec la session de l'organisme

Heures de réception de cette session ; entre parenthèses, l'heure écrite par l'organisme dans son message.
- Reçu vers 05:25Z (« 05:15Z ») : lanceur v11c scellé (`1ed883749`), empreintes « qui peuvent encore changer », points à aligner. Vérifié : chaque pièce égale à son compagnon et, à l'octet, au travail interrompu lu pour le brouillon 4.
- Envoyé à 05:26Z : chemins, empreintes et points délicats du brouillon 4 et du devis v11c.
- Reçu à 05:27Z (« 05:31Z ») : gabarit du relevé des crédits en v11d ; lanceur v11d (une ligne : la clé LUC dans les réglages de l'essai à blanc) ; configuration v11d (notes corrigées, champ du plafond Claude à 45 ou retiré) ; gabarit des prix Claude à retirer si le lanceur ne le lit pas ; points 6 à 8 demandés en trois lignes.
- Envoyé à 05:27Z : points 6 à 8 avec recommandation (mesure de GO-2026-11-22-128 avant le départ, 0,7 ; même mesure pour la sortie de 45 056 jetons d'Argon, 0,7 ; notes de la configuration corrigées et champ inerte retiré, 0,6).
- Reçu à 05:28Z, puis de nouveau à 05:36Z (« 05:35Z ») : décisions inscrites sous R-5130, à citer ; mesure d'Argon portée à Lazar, rien ne part avant son mot ; le texte doit dire le cas avec la mesure et le cas sans ; la Vast 62097676 est la relance du bras A (R-5122).
- Envoyé à 05:41Z : chemins, empreintes et points délicats du brouillon 5 et du devis v11d ; deux points à trancher (seuil de la règle ; consignes et nombre d'appels de la mesure, à fixer avant le scellement).
- Reçu à 05:41Z (« 05:45Z ») : seuil 31 462 (marge comprise) ; un appel de proposeur et quatre de juge, pièces de rang 1 écrites comme règle de choix ; reprises des 429 et 5xx au plus deux fois par appel ; champ inerte retiré en v11d ; règle de lecture retenue telle quelle ; « attends les empreintes v11d définitives et la vérification du même contre-lecteur, puis écris le texte scellable ».
- Envoyé après la poussée de cette passation : chemins et empreintes du brouillon 6 et du devis v11e, chemin de cette passation, essais.

## Reste

- Recevoir les empreintes définitives des pièces du lanceur v11d (lanceur, essais, configuration v11d, gabarit de déclaration, gabarit du relevé des crédits v11d, commande en flux v2 et sonde commune v3 avec leurs essais), après la vérification du même contre-lecteur, et la ligne du registre qui inscrit les décisions datées 05:45Z ; écrire alors le texte scellable sous `course-v11/preenregistrement-course-affinage-mentors-v11.md` (sans la ligne d'état ni la dernière section du brouillon 6).
- Réponses attendues de la session de l'organisme sur deux points du brouillon 6 : la lecture de « la première fiche » (point 7 de la dernière section) ; la condition proposée sur `hypothese_sortie_maximale_tenue` (point 8 ; recommandation : l'ajouter, 0,7). Si l'une change le texte, un brouillon 7 précède le texte scellable.
- Le mot de Lazar sur la mesure n'est pas requis pour sceller : le texte dit les deux cas.
- Contre-lecture du préenregistrement et du devis v11d par un Opus neuf (libellé « Opus 5.5, contre-lecteur neuf »), organisée par la session de l'organisme.

## Réserves

- Le lanceur v11d et la configuration v11d ne sont pas lus (en écriture ailleurs) : le texte les décrit sur le mot de la session de l'organisme (« le v11c à une ligne près » ; notes corrigées) ; à constater sur les pièces scellées avant le scellement du texte.
- Les appels et les pièces de la mesure sont fixés au brouillon 6 ; la fiche du juge dépend de la réponse de l'appel de proposeur de la mesure (règle de rang, aucun contenu lu) ; la lecture des fiches est faite sur la v53, non sur la v54 épinglée.
- Le seuil retenu (31 462) n'est pas celui que le rédacteur recommandait (32 476, confiance 0,6) : décision de la session de l'organisme, écrite telle quelle.
- Routine de reprise : étape 1 faite (trois documents de lancement conformes ; vérification de l'arbre : 1 638 problèmes, aucun dans le dossier de l'affinage, comme au brouillon 3) ; étape 2 faite (passations du rédacteur et passation de pause de nuit de l'organisme, `2026-11-22-2310-organisme.md` sur `lot/compte-organisme-v1`) ; étape 3 non faite (branche de préparation : aucun registre vivant modifié) ; étape 4 en lecture seule (voir « Instances ») ; étape 5 : essais du dépôt lancés deux fois dans ce conteneur — le premier passage s'arrête à la collecte (86 erreurs : `torch` 63, `scipy` 22, `huggingface_hub` 1, absents) ; le second, avec `--continue-on-collection-errors`, est coupé par sa minuterie de 3 000 s à 72 % : sur 5 112 essais passés, 4 959 réussis, 40 échecs, 2 erreurs, 111 sautés ; échecs non examinés (aucun résumé, la minuterie ayant coupé avant). Aucun fichier de `src/` ni de `tests/` n'est changé par cette session.
- `registres/etat.md` non modifié : état vivant de la session de l'organisme.
- Le rédacteur et le contre-lecteur prévu sont du même modèle (Opus 5.5) : écart déclaré par GO-2026-11-22-145, dit au texte.
- Aucune demande de fusion ouverte (consigne de la session de l'organisme).

## Prochaine action

Sur le mot de la session de l'organisme, avec les empreintes définitives du lanceur v11d (après la vérification du même contre-lecteur), la référence des décisions datées 05:45Z et ses réponses aux points 7 et 8 de la dernière section du brouillon 6 : écrire le texte scellable (ou un brouillon 7 si une réponse change le texte). Sinon, rien.

## Instances actives

Aucune lancée par cette session. Relevé en lecture seule, vers 04:55Z puis 05:41Z, identique : Hetzner, liste vide pour le jeton de cet environnement ; Vast.ai, trois instances en marche qui ne sont pas de cette session — 62094628 (`iib-voie-a-v1`, R-5111), 62096662 (`b5f-lecture-v1`, R-5119) et 62097676 (`bras-a-ligne-1-v1`, relance du bras A, R-5122) — et quatre arrêtées (58936096, 58936099, 58936100, 60988826). Aucune touchée : leurs tâches relèvent de la mère (R10).
