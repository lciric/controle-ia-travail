# Vérification du brouillon 45 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf. Je n'ai écrit ni le brouillon 45, ni la réponse de son rédacteur, ni son mandat, ni la fiche des faits, ni aucun brouillon précédent. Je ne scelle et ne committe que ce rendu.
- **Brouillon vérifié** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon45.md`, `4588944f9658a7ddb563296821392404be96241ba41027b7d15df72194eb6b4d` (recalculée, égale à son compagnon), 2 543 lignes.
- **Base** : brouillon 44, `b30aa902a8135f888911519f4efd0a3583fddd6b8f748889146d9bca5da43eb8` (recalculée), 2 514 lignes.
- **Pièces de l'écriture** (empreintes recalculées, compagnons vérifiés) : mandat `docs/notes/relance-organismes-discrets-v1/brouillon45-par-api-v1/mandat-redacteur-fable-api-brouillon45-v1.md`, `213ad3db9bb95abe683333be828f7b8cd8ae78be7045a19f2666281c27d035fd` ; fiche des faits `…/brouillon45-par-api-v1/fiche-des-faits-brouillon45-v1.md`, `96483cbcf883453f0bc58edd8009814241ae828332c85feafd79de4b91c78173` ; réponse du rédacteur `…/brouillon45-par-api-v1/sortie/relecture-fable-api.md`, `a4e1712a84671616f5ce5af66edcd4b884129de0652d55050186a1ab2f4aa00d` ; rapport d'application `…/brouillon45-par-api-v1/application-operations-brouillon45-v1.json`, `a437358e1867f7a92337d0d083dd130dee21b1ccae7874a2da49b3d78683648c` ; vérification du brouillon 44 `docs/notes/relance-organismes-discrets-v1/verification-brouillon44-bras-a-v1.md`, `be7b0453e677b061080ad18836bf19954fda3f240d373e63a02dcd6939a777dc`.
- **Date** : 2026-11-22. Branche `claude/pensive-bardeen-1fv7hw`, commit `9cfd677f9`. Registre lu à `origin/main` = `697580de2acfb972418f6006082a9d3e0aae5228`, sans `git fetch` ni réseau.

## Verdict : **engageable après corrections** — cinq corrections, toutes de fait ou de précision, aucune ne touche une règle ; neuf mineurs

- **Seules les lignes déclarées changent.** Je l'ai vérifié par programme, à la ligne et au signe. Le rejeu indépendant des 28 opérations rend le même fichier, à l'empreinte près (`4588944f…`).
- **Les huit règles d'admission, lignes 542 à 550 du 45, sont égales caractère pour caractère aux lignes 529 à 537 du 44.** La comparaison des listes rend vrai. L'empreinte des neuf lignes jointes vaut `3d1f0afe82f5aeb3bf5dd757cb6d814e19c66b93a89a65b6f08677823e1b8f96`, la même qu'aux brouillons 43 et 44.
- **Aucune règle, aucun seuil, aucune issue et aucune prédiction ne change.** Sections 7, 8, 9, 10, 11 et 12 : intactes. Sous-sections 3.2, 3.3 et 3.5, et section 4 : intactes. Sections 6.1 à 6.10 et 6.12 : intactes. Une seule ligne de la section 6 change, en 6.11 (mineur m-1) : une cellule d'état de la table des dépenses, purement factuelle. En 13.2, seules les deux cases visées changent : « version des modèles » et le lanceur de l'étape de discrétion.
- **Tous les faits de la fiche sont exacts contre le disque**, chemins et empreintes. Les lignes de GO nommées sont exactes contre le registre.
- **Il ne reste aucune marque ⟦ ⟧.** Seule la marque `⟦D1⟧` a servi dans les opérations, et elle est rétablie en « Lazar ».
- **Défaut de fond trouvé (correction C-1).** Le brouillon pose une contradiction qui n'existe pas : une sonde « exemptée » et pourtant « comprise ». L'exemption de la ligne GO-2026-11-22-03 porte sur un seul contrôle de la sonde, pas sur son envoi. L'avenant qui la porte est nommé dans cette ligne de GO : il peut être cité.
- **Point (b), tranché : ce n'est pas un écart aux huit règles, ni au texte en vigueur au premier envoi.** C'est un ordre que le texte laissait ouvert. Il est à dire à Lazar en une ligne d'information, non comme un nœud (partie 3, (b)).

## 1. Contrôles par programme, et leur sortie

| contrôle | sortie | conclusion |
|---|---|---|
| `diff` du 44 au 45 | `1c1 3c3 5,6c5,6 9,10c9,10 205a206,218 505c518 519c532 524,525c537,538 538c551 941c954 1437c1450 1449,1450c1462,1463 1460c1473 1470c1483 1477c1490 2499a2513,2528 2511,2512c2540,2541` | égal au rapport d'application : 20 lignes remplacées, 29 lignes neuves (13 lignes de table et 16 lignes de 14.57) ; 2 515 → 2 544 éléments (`split("\n")`) |
| rejeu des opérations, `python3 -I scripts/appliquer_operations_brouillon_v1.py` (script `b179a0bf…`), sur le 44, la réponse et la table des marques, sortie dans mon dossier de travail | code 0, 28 opérations, sortie `4588944f…` | **identique** au brouillon 45 |
| lignes visées contre les extraits montrés au rédacteur (175 lignes `L…`) | les 22 lignes d'ancrage (1, 3, 5, 6, 9, 10, 205, 505, 519, 524, 525, 538, 941, 1437, 1449, 1450, 1460, 1470, 1477, 2498, 2511, 2512) sont toutes montrées ; chaque `ancien` y figure une fois ; sur les lignes coupées (3, 5, 9, 538), chaque `ancien` est dans la partie montrée ; la ligne 8 n'est pas touchée | conforme au mandat |
| au signe (`difflib`), ligne par ligne | 1 : « 4 » → « 5 » ; 3 : « 4 » → « 5 » et une insertion ; 5, 6, 9, 10, 518, 538, 1450, 1462, 1483, 1490, 2540 : **insertions seules** ; 532 : insertion, et « ** » → fin de citation ; 537 : insertions seules, sauf le remplacement proposé par m-1 ; 551 : insertion du point (3) ; la phrase « Limite, dite » est récrite (« ce texte ne dit pas laquelle » devient une phrase d'histoire suivie de la règle neuve) ; 954 : une cellule récrite ; 1463 : la case est récrite au statut, avec insertions ; 1473 : le reste (b) est récrit, et une phrase est ajoutée au reste (f) ; 2541 : insertion, et « le brouillon 44 est à vérifier » → « le brouillon 45 va à la contre-lecture 10 » | tout est déclaré par la note |
| parité des `**` et équilibre des « » sur chaque ligne changée | aucun écart | — |
| sections des lignes changées (titres du 45) | en-tête 1–10 ; table 206–218 ; 3.4 (516–557) : 518, 532, 537, 538, 551 ; 6.11 : 954 ; préambule de 13 : 1450 ; 13.1 : 1462, 1463, 1473 ; 13.2 : 1483 (« version des modèles »), 1490 (lanceur) ; 14.57 : 2513–2528 ; « Contre-lecture » : 2540, 2541 | rien en 3.2, 3.3, 3.5, 4, 6.1–6.10, 6.12, 7 à 12 |
| huit règles | `r44[528:537] == r45[541:550]` → `True` ; empreinte `3d1f0afe…` | nouveaux numéros 542 à 550 (titre en 542, règles 1 à 8 en 543–550), comme la note le dit |
| marques | `⟦` : 0 ; `⟧` : 0 | rétablies |
| validateur du dépôt, `controle_ia.prereg.problemes()` | 44 : 2 problèmes ; 45 : les deux mêmes (« marqueur À REMPLIR restant hors des sections exigées » ; « contre-lecture 10 sans ses deux empreintes ») | inchangé |
| marques « À REMPLIR » | 44 : 8 occurrences sur 7 lignes ; 45 : 8 sur 7 lignes (les mêmes cases de 13.1) | aucune case fermée en silence |
| consignes de registre | « intervalle impossible » 23/23 ; « non ajustable » 26/26 ; « moniteur appris » 36/36 ; mentions `GO-2026-11-19-…` 264/264 | aucune recopie neuve |
| identifiants de GO neufs (mentions au 45) | 21-69 (1), 21-74 (3), 21-75 (4), 21-83 (2), 21-86 (3), 22-02 (2), 22-03 (1), 22-16 (2), 22-40 (2), 22-57 (1), 22-60 (2), 22-61 (2), 22-62 (2) | tous dans la fiche ou dans l'extrait de la vérification ; confrontés au registre (partie 4) |

## 2. Corrections (avant la contre-lecture 10)

**C-1. Sonde de borne, ligne 551, point (3), et ligne m-2 de 14.57 (m-2 ; point (c) de la note).** Le 45 écrit : « la sonde est exemptée, exemption confirmée par GO-2026-11-22-03 ; la fiche des faits relève pourtant, aux deux vérifications du 22 novembre, une sonde de borne « comprise » sur chaque clé, ce que ce brouillon rapporte sans le trancher ; l'avenant qui porte l'exemption n'est pas cité ».

La lecture est fausse. La ligne GO-2026-11-22-03 dit : « exemption de la sonde de borne de Google (sortie maximale de 256) de la règle « réflexion plus 16 000 » des appels à Google ; elle garde un réglage de réflexion explicite et ne produit aucune lecture jugée ». Elle nomme aussi l'avenant : avenant 2 au devis, version 3, `docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v3.md`, `9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3`, recalculée et égale à son compagnon. L'avenant, section 6, précise que la sonde est exemptée « d'un seul contrôle » et qu'elle rend toujours « comprise », « non comprise » ou « indécidée ». La sonde est donc envoyée, et « comprise » sur chaque clé est son issue normale. Le point (3) garde son objet, et la vérification du 44 se trompait en proposant « sans objet ». Le rédacteur a eu raison de ne pas écrire cette formule.

Texte proposé, à la place de la parenthèse insérée au point (3) :

> (brouillon 45 ; vérification du brouillon 44, m-2) : sous la décision de la session mère du 21 novembre 2026 (sous GO-2026-11-21-69), la sortie maximale envoyée à Google est de 65 536, au niveau de réflexion gardé. La sonde de borne de chaque vérification de clé de Google est exemptée du seul contrôle « réflexion plus 16 000 jetons de texte ». Elle est envoyée, à sa sortie maximale de 256, garde un réglage de réflexion explicite et ne produit aucune lecture jugée (avenant 2 au devis, version 3, section 6, `docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v3.md`, `9d4b8a08…` ; exemption confirmée par Lazar, GO-2026-11-22-03, qui remplace GO-2026-11-21-88). Aux deux vérifications du 22 novembre, son issue est « comprise » sur chaque clé (fiche des faits), si bien que ce point garde son objet.

Ligne m-2 de 14.57, à la place de son traitement : « **ajouté** au point (3) : l'exemption ne vise que le contrôle « réflexion plus 16 000 » ; la sonde est envoyée et rend « comprise » sur chaque clé ; l'avenant 2, version 3 (`9d4b8a08…`), est cité ». Ajouter aussi une ligne de table pour cet avenant : l'avenant 2 n'est cité nulle part dans le 45, ni par son chemin ni dans la table (recherche par programme : 0 occurrence).

**C-2. Case « lecteurs et juge des ancres », 13.1, ligne 1463 : les restes que la fiche ne donnait pas sont dans les pièces citées.** Ce sont des compteurs seulement, que j'ai lus par programme dans les deux applications des règles et les deux rapports techniques cités. Le texte proposé remplace « reste À REMPLIR, pour ce que la fiche ne donne pas : la sortie maximale du second lecteur à la course (règle 7), le compte des réponses étayées et le coût projeté de chacun, les champs exacts de chaque service » par :

> reste À REMPLIR : les champs exacts de chaque service. Le reste est transcrit des pièces citées, compteurs seulement :
> - **Mistral Large 4** : sortie facturée la plus haute observée, 12 652 jetons ; **sortie maximale à la course, 51 200** par la règle 7, lue sur la réponse et la réflexion ensemble (application des règles `98581778…`) ; réponses étayées, 24 sur 24 ; coût projeté (champ `cout_projete.C_usd` du rapport technique `74106c3e…`), 104,9661 USD ; hôte `api.eu.mistral.ai` ; nom servi relevé à la vérification, `mistral-large-4-0` (même rapport).
> - **`gemini-4-neon`** : réponses étayées, 8 sur 8 ; coût moyen par appel, 0,1131545 USD pour l'appariement et 0,2578845 USD pour la couverture (champ `cout_projete` du rapport technique `7bb8cc95…`).

Contrôle de la règle 7 : 4 × 12 652 = 50 608, arrondi aux 1 024 supérieurs, donne 51 200 ; 4 × 21 132 = 84 528 donne 84 992. Ces chiffres confirment aussi la réserve 8 du rédacteur : le nom servi de Mistral est relevé dans le rapport, et non déduit. La phrase « saine voulant dire, en 3.4, … » peut rester ou être remplacée par ce relevé.

**C-3. Voie de service du juge à la course, ligne 551 et ligne 1483 (m-4 ; point (a)) : « file » et « rang » ne sont pas définis par rapport à 6.3.** À la course, 6.3 fait appeler le juge à deux étapes : l'étape (d), qui porte les deux ancres (48 actions pour l'appariement, 8 plans pour la couverture), et l'étape (e′), qui porte les 24 jumeaux d'épreuve, construits seulement après la garde de puissance (h1). 6.3 dit aussi « un item par appel ». La section 3.4 parle de « la file du juge » d'un seul tenant sur (d) et (e′) ; la section 8.6 dit que les appels partent « dans l'ordre tiré ». La règle du 45, « dans chaque file du juge à la course, … dans l'ordre de ses items », laisse donc ouvert ce qui fait une file : une seule file pour (d) et (e′), une par étape ou une par ancre. Elle ne dit pas non plus de quel ordre il s'agit. Comme la parité est fixée à la configuration scellée, le choix ne peut pas dépendre d'une lecture ; il doit pourtant être écrit dans le texte, puisque la règle se dit « écrite avant lecture ».

Texte proposé, ligne 551, à la place de « dans chaque file du juge à la course, les appels partent dans l'ordre de ses items » :

> à chacune des deux étapes où le juge est appelé à la course (étape (d) de 6.3, les deux ancres de la première partie, en un seul lot ; étape (e′), les 24 jumeaux d'épreuve, en un second lot), les appels, un item par appel, partent dans l'ordre tiré du lot (8.6). Le rang compte à partir de 1 dans chaque lot. Le tableau des clés par rang associe un rang à une clé, sans nommer d'item. Il est donc écrit avant que le lot de l'étape (e′) existe.

Ligne 1483 : ajouter « (rang compté dans chaque lot du juge, étapes (d) et (e′), dans l'ordre tiré du lot) ». Rien d'autre ne heurte 6.3. La règle ne lit ni réponse, ni solde, ni dépense. Elle ne crée aucune issue : un refus pour crédit épuisé reste un défaut qui arrête la ligne, sans passage sur l'autre clé.

**C-4. Case « familles », ligne 1462, et ligne 518 (point (b)) : écrire le constat tranché, et non « sans être tranché ».** Le raisonnement est en partie 3, (b). Texte proposé, à la place de « (… ; les deux files d'admission sont parties avant elle, ce qui est dit ici sans être tranché) » :

> (… ; les deux files d'admission sont parties avant elle. Ce n'est pas un écart : au premier envoi, sous le brouillon 44, le point (iii) de l'alinéa « Admission d'un modèle » (3.4) était porté par le contrôle au niveau des familles, écrit dans cette case et en 3.4 (trois familles distinctes, Claude, Mistral et Google, hors des familles exclues, Llama et Qwen, par les mots de Lazar). Cette même case laissait la confrontation des identifiants au lecteur habilité, au renvoi de la base, comme un reste à remplir avant le scellement. Aucune lecture n'en dépend : seuls des compteurs ont été lus. C'est dit à Lazar comme une information.)

**C-5. Pièces de l'écriture du 45, à inscrire (lignes 9 et 2541 ; réserve 4 de la note).** Le 45 laisse deux trous : « la session … en inscrit le chemin et l'empreinte » (ligne 9) et « le chemin et l'empreinte du rapport entier, son auteur et son verdict sont à inscrire par la session » (ligne 2541). Texte proposé :

- Ligne 9 : « note du rédacteur du brouillon 45 : `docs/notes/relance-organismes-discrets-v1/brouillon45-par-api-v1/sortie/relecture-fable-api.md`, `a4e1712a84671616f5ce5af66edcd4b884129de0652d55050186a1ab2f4aa00d` ; mandat : `…/brouillon45-par-api-v1/mandat-redacteur-fable-api-brouillon45-v1.md`, `213ad3db9bb95abe683333be828f7b8cd8ae78be7045a19f2666281c27d035fd` ».
- Ligne 2541 : « rapport `docs/notes/relance-organismes-discrets-v1/verification-brouillon44-bras-a-v1.md`, `be7b0453e677b061080ad18836bf19954fda3f240d373e63a02dcd6939a777dc` ; vérificateur : agent neuf, Claude Opus 5.5 ; verdict « engageable », aucune correction, neuf mineurs ».
- Inscrire ensuite la présente vérification de la même façon.

## 3. Les points demandés

**(a) La règle de la voie de service, confrontée à 6.3.** Elle est compatible avec 6.3 : la clé dépend du seul rang, et la parité est fixée à la configuration du bras, scellée à l'étape (a), avant le premier appel de l'étape (d). Mais le rang, défini « sans voir 6.3 », est ambigu sur l'unité, file ou lot, et sur l'ordre. La correction C-3 fixe : un lot par étape, (d) puis (e′) ; l'ordre tiré de 8.6 ; un rang compté à partir de 1 par lot ; un tableau qui associe un rang à une clé sans nommer d'item. Ce dernier point lève la seule tension réelle avec 6.3 : le lot des jumeaux n'existe pas encore quand la configuration est scellée. La règle n'ajoute ni seuil ni issue et ne touche aucune des huit règles. C'est bien le partage éprouvé à l'essai : rangs impairs sous `GEMINI_API_KEY` et rangs pairs sous `GEMINI_API_KEY_2`, comme le confirme la ligne GO-2026-11-22-62.

**(b) La case « familles ». Tranché.**
1. **Les huit règles ne demandent pas la confrontation.** La règle 2 énumère ce qui retient la file du juge : « ses conditions d'envoi constatées, son devis contre-lu, sa ligne de calcul et sa clé vérifiée ». La famille n'y est pas. La règle 8 ne vise que le changement des règles après le premier envoi. Ce n'est donc pas un écart aux règles d'admission.
2. **L'alinéa « Admission d'un modèle, fixée avant le premier envoi de sa file » (ligne 536, inchangée depuis le 44) demande que la case de 13.1 porte « (iii) le contrôle de sa famille ».** Au premier envoi, sous le brouillon 44, le texte portait déjà ce contrôle au niveau des familles. La ligne 518 dit « Trois familles distinctes — Claude, Mistral, Google —, toutes hors des familles exclues — Llama et Qwen — de la liste empreintée ». La case « familles » le redit, sur les mots de Lazar. Cette même case confiait expressément la confrontation des identifiants au lecteur habilité, avec « au renvoi de la base » dans sa colonne de responsabilité, comme un reste. L'ordre suivi est donc celui que le texte en vigueur écrivait. Lire le point (iii) comme exigeant aussi la confrontation des identifiants avant l'envoi serait une lecture plus stricte que le texte. Elle rendrait le texte contradictoire avec sa propre case, et elle ne change rien à aucune lecture : seuls des compteurs sont lus, et une confrontation négative laisserait le rôle non pourvu par les règles 5 et 6.
3. **À porter à Lazar ?** Oui, en une ligne d'information, non comme un nœud. Le texte n'est pas scellé, aucune règle n'est franchie, et la dépense est déjà faite sous ses lignes de GO. Une phrase proposée : « Les deux essais d'admission sont partis avant que les identifiants `mistral-large-4-0` et `gemini-4-neon` soient confrontés à la liste des familles par le lecteur habilité. Le texte en vigueur le permettait, le contrôle par famille étant fait ; la confrontation reste à faire avant le scellement. »

**(c) La sonde « exemptée » et pourtant « comprise ».** Il n'y a pas de contradiction : l'exemption ne porte que sur le contrôle « réflexion plus 16 000 », et la sonde est bien envoyée. C'est la correction C-1.

**Réserves 1 à 10 de la note du rédacteur.**
1. Avenant de l'exemption : retrouvé, voir C-1.
2. Lignes GO-2026-11-21-69, -74 et -75 : transcrites de l'extrait de la vérification, qui était une pièce donnée au rédacteur. Je les ai confrontées au registre : -74 donne bien la région globale et la recharge non comptée, -75 un crédit d'au moins 7,87 €. Les garder.
3. Chemins en « …/ » complétés : les dix chemins de la fiche existent sur le disque, avec ces empreintes (partie 4).
4. Pièces à inscrire : voir C-5.
5. Ligne 8 : non touchée, comme il le fallait.
6. Ligne 3 : voir le mineur m-2.
7. Ligne 1436 du 44 (1449 du 45) : laisser telle quelle.
8. Nom servi de Mistral : confirmé par le rapport technique, voir C-2.
9. Espaces insécables : aucune opération n'a été refusée, et le rejeu est identique.
10. Contrôles par programme : faits ici, en partie 1.

**Les mineurs m-1 à m-9 de la vérification du 44, et les points du mandat.** m-1 est fidèle, texte proposé à la lettre, avec (a) et (b) ; le repli global n'a pas joué, l'hôte européen étant confirmé par le rapport technique. m-2 : voir C-1. m-3 est fidèle. m-4 est fidèle sur le fond, avec la précision C-3. m-5 est fidèle ; il touche 6.11 (mineur m-1). m-6 et m-7 sont fidèles. m-8 tient en une phrase, sans décision. m-9 : rien à faire, puisque les captures sont les mêmes (16:24Z). Pour le mandat : le point 1 renvoie à ce qui précède ; le point 2 est porté (compléments en C-2) ; les points 3, 4 et 6 sont portés ; le point 5 est porté, et ses deux cases sont déclarées ouvertes, une phrase chacune (lignes 1462 et 1473), sans aucun contenu habilité.

## 4. Faits contre le disque et le registre

- **Empreintes recalculées : toutes égales à celles du texte et à leurs compagnons.**
  - Rapports techniques : `74106c3e…` et `7bb8cc95…`.
  - Applications des règles : `98581778…` et `c593784b…`.
  - Configurations des files : `371d5b23…` et `37a23ab2…`.
  - Programme `scripts/chef_essais_admission_bras_a_v12.py` : `6aa04397…` ; sa vérification : `bd935fd8…`.
  - Fichier des règles : `cd0e384c…`.
  - Pièces de constat : Mistral `4907d092…`, Google `2234e0cb…`.
  - Avenant 3, version 2 : `4b331d9a…`.
  - Fiche des faits : `96483cbc…` ; extraits : `47bb9dc3…` ; extrait de la vérification : `b0f6bdc4…`.
  - Le dossier `runs/verification-cle-mistral-bras-a-v1/20261121-213114-verification-mistral-eu` existe ; je ne l'ai pas listé.
- **Pièce du côté habilité non suivie** : `docs/notes/bras-a-moniteurs-v1/verification-habilitee-lanceur-discretion-v2-sans-interne-v1.md` (`33efc50f…`), transcrite de la fiche. Elle est cloisonnée : ni ouverte ni empreintée.
- **Compteurs, confrontés à la fiche et au texte.**
  - Mistral : 24 lectures jouées, 24 réponses de code 200, 24 conformes, 0 refus, 0 fin par sortie maximale ; hôte `api.eu.mistral.ai` ; ligne GO-2026-11-21-83.
  - Le juge : 8 lectures, 4 sous chaque clé, 8 réponses de code 200, 8 conformes, 0 défaut ; ligne GO-2026-11-22-62.
  - Les deux applications citent `cd0e384c…`, et les deux rapports citent le brouillon 44 (`b30aa902…`) comme texte en vigueur.
- **Lignes du registre, à la lettre.**
  - GO-2026-11-21-83 et -86 : bon objet, et l'hôte européen pour -86.
  - GO-2026-11-22-60, -61 et -62 : clés et rangs conformes.
  - GO-2026-11-22-02, -16 et -03 : conformes. La -03 nomme l'avenant 2 v3 (C-1).
  - GO-2026-11-22-40 : contient bien « Google (bras A) : « la recharge automatique vient de s'activer pour 20 euros » ».
  - GO-2026-11-22-57 : décision de Lazar. Je n'en ai vu que le début de la ligne, et le calendrier (23 et 29 novembre) vient de la fiche, dont c'est le point 5.

## 5. Mineurs

- **m-1.** Une ligne de la section 6 est touchée : en 6.11, la cellule d'état de la table des dépenses (ligne 954). C'est un changement de fait seulement, déclaré sous m-5 ; aucun chiffre de plafond ni aucune règle ne change. Je l'accepte. La même ligne garde « une vérification de clé par fournisseur, un appel minimal », que les lignes 538 et 551 font lire autrement : cela suffit.
- **m-2.** Ligne 3 (réserve 6 du rédacteur) : « Il ne modifie ni les brouillons 1 à 41 » est périmé, à écrire « 1 à 44 ». « inscrite comme contre-lecture 9 » est une phrase d'histoire, alors que la section « Contre-lecture » annonce la contre-lecture 10 : ajouter « (au brouillon 45 : contre-lecture 10) ».
- **m-3.** Ligne 518 : « mineurs m-1 à m-8 » devient « m-1 à m-9 ».
- **m-4.** En-tête de 14.57 : « aucune fiche n'est ajoutée » est obscur, puisque 13 lignes de table sont ajoutées. Écrire « aucune section de jugement n'est touchée ; treize lignes de table sont ajoutées ».
- **m-5.** D'après le rapport technique, la file du juge est partie au régime **prudent**, imposé par la configuration sur décision de la session mère, alors que les deux sondes étaient « comprises ». Le point (3) de la ligne 551 dit que deux sondes « comprises » font partir la file au régime de compte courant. Ce point relève du devis, « non de ce texte », et le régime prudent est le plus strict. Le dire en une phrase.
- **m-6.** Ligne 551 : « la décision de la session principale du 21 novembre » devient « de la session mère ». Le texte réserve « session principale » à une autre session ; le registre dit « session mère » pour GO-2026-11-21-69 et la suite. C'est repris dans le texte de C-1.
- **m-7.** Le fichier des règles cite toujours les lignes 529 à 537 et le brouillon 44, ce qui est juste par la règle 8 (« le brouillon en vigueur au premier envoi »). Il n'y a rien à faire, sauf à dire dans 14.57 que les mêmes règles sont désormais aux lignes 542 à 550.
- **m-8.** Le mandat parle des mineurs « m-1 à m-8 », alors que la vérification du 44 en compte neuf. Le rédacteur a reçu les neuf, par l'extrait, et les a tous traités : sans effet.
- **m-9.** Information (m-8 de la vérification du 44, inchangé) : un constat des journaux de Google avant la course reste à la décision de Lazar.

## 6. Ce que j'ai ouvert

- **En entier** : CLAUDE.md (dans mes consignes) ; le mandat ; la fiche des faits ; la réponse du rédacteur ; le rapport d'application ; `compteurs.json` de la sortie.
- **En partie** :
  - la vérification du brouillon 44 : verdict, parties 1 à 6 par recherche ;
  - le brouillon 44 et le brouillon 45 : par programme, avec affichage des lignes changées, de 6.3, de 8.6, des règles 542–550, des lignes 536, 1462, 2510–2529 et du début de 2540 ;
  - l'avenant 2, version 3 : titres et section 6 ;
  - le script d'application : son en-tête ;
  - la table des marques des extraits ;
  - l'extrait nettoyé du 44 : par programme, pour les lignes montrées.
- **Compteurs seulement** : les deux rapports techniques et les deux applications des règles cités par la fiche, dont j'ai lu les champs simples, sans aucun texte de réponse.
- **Registre** : `git show origin/main:registres/go.md | grep -F` pour les lignes 21-69, 21-74, 21-75, 21-83, 21-86, 22-02, 22-03, 22-16, 22-40, 22-57, 22-60, 22-61 et 22-62. Les commandes ont rendu en passant les lignes 21-82, 22-58 et 22-60, qui contiennent ces chaînes ; je n'en fais rien.
- **Débord, déclaré.** Mon programme de confrontation des empreintes a pris tous les couples chemin–empreinte des lignes changées. Mon filtre a manqué trois préfixes cloisonnés, et le programme a donc :
  - (a) calculé l'empreinte de deux fichiers sous `docs/notes/bras-a-sans-interne-v1/` et d'un fichier sous `runs/essai-mesure-lecteurs-bras-a-v1/`, dont seuls l'égalité et huit signes ont été affichés, sans aucun contenu ;
  - (b) testé l'existence de sept chemins sous `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/` et `tests/…habilite…`, tous absents sur cette branche.

  Je n'ai ouvert aucun de ces fichiers et n'utilise aucun de ces résultats.
- **Rien d'autre** sous `bases/`, `sondes/`, `t07*`, T0.8, `scripts/mots_et_cout_*`, `prereg/T0.6-…`, `docs/notes/bras-a-moniteurs-v1/`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`, `docs/sources/`, `archives-reponses-modeles/`, `reponses-brutes-non-lues/`, ni dans les fichiers « consigne-privee » ou « conception-ii-b ».
- **Aucun** réseau, `git fetch`, clé, appel de modèle ni sous-agent.
