# Contre-lecture (règle R2) — préenregistrement de la course à plusieurs générations, brouillon 6 — tour 3, v1

- **Lecteur** : modèle C, lecteur neuf ; je n'ai écrit aucune des pièces. Je n'ai pas tenu pour acquis le rapport du tour 2 : j'ai recontrôlé ses couples sur le brouillon 6.
- **Heures** (`date -u`) : début 2026-11-17 02:33:05 ; fin : relevée juste avant le scellement.
- **Pièce lue** : `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon6.md`, `4deec5252a35362f5ef050834a9b56836e76385bcc1f28d860368b37ac251a82` (égale à son compagnon ; écrite à 02:32:07, comme le dit l'en-tête). Brouillon 5 : `7100a978335893ffd3d0ae9ec142622361869621e8496be138b3f1d782f907f8` (égale à son compagnon). Rapport du tour 2 : `d067513c1a505ef85e9219c90e8dd2a0decbd58865b1bf66210ef72b4acc936e` (empreinte recalculée égale).

## Verdict (une ligne)

**Corrections** : les six mineures du tour 2 (douze couples) sont appliquées fidèlement et le différentiel ne contient rien d'autre que l'en-tête et la section « Contre-lecture » ; **aucune majeure** ; **deux mineures de cohérence** (m-18, m-19), toutes deux déjà vues par le rédacteur ; la pièce reste non scellable tant que les marqueurs sont ouverts (dit par la pièce).

## 1. Différentiel brouillon 5 → brouillon 6 (par `diff`)

`diff` brut : 200 lignes. Chaque bloc est classé ; aucun bloc hors de la liste.

| bloc | nature | conforme |
|---|---|---|
| ligne 1 (titre) ; lignes 3 à 6 (statut) ; 12-13 (ordre des étapes) ; 34a38 (rédacteur du brouillon 6) ; 68a83 (heures) | en-tête | annoncé ; aucun chiffre touché ; l'heure 02:32:07 égale la date d'écriture des fichiers (`ls`) |
| 307 (D.3 point 4) | couple m-15 | texte du rapport, caractère pour caractère |
| 470 et 474 (D.12) | couples m-12 (deux) | idem |
| 564 (Métrique « Appels »), 693 (Plan d'analyse point 8), 829 (W-13), 937 (V-17) | couples m-12 (quatre) | idem |
| 609 (Seuil, règle 3) | couple m-14 | idem |
| 989 (Préalables point 8) | couple m-17 | idem |
| 1041 (Points ouverts point 5) | couple m-13 | idem |
| 1051a1071 (point 11 neuf) | couple m-16, premier | idem |
| 1103 (ligne des marqueurs) | couple m-16, second | **retouche de forme déclarée** : la cellule « où » est prolongée de « ; Décisions » (voir ci-dessous) |
| 1110, 1211-1219 (section « Contre-lecture ») | section | annoncé (phrase d'ouverture ; contre-lecture 4, réponse, constats, déclaration, « À faire ») |

Les douze couples y sont, un par un : m-12 (six), m-13, m-14, m-15, m-16 (deux), m-17. Comptage par programme : chaque « ancien » du rapport figurait une fois dans le brouillon 5 ; chaque « nouveau » figure dans le brouillon 6. Aucune retouche cachée.

**Retouche de m-16** : « Seuil ; À vérifier sur le code » devient « Seuil ; À vérifier sur le code ; Décisions ». Elle est dite dans la table de réponse, elle n'est pas dans le rapport du tour 2 (qui ne la demandait pas), et elle est juste : la ligne Q-4 … Q-8 et le point 11 sont dans la section « Décisions tranchées et points ouverts ». **Acceptée.**

**Différentiel scellé** : le différentiel du rédacteur appliqué au brouillon 5 par `patch` redonne le brouillon 6 octet pour octet (`cmp`) ; les deux compagnons `.sha256` (programme des couples, différentiel) se vérifient. Son découpage des blocs diffère légèrement d'un `diff` brut (placement d'une ligne vide en tête), sans effet.

## 2. Vérifications refaites

| contrôle | résultat |
|---|---|
| validateur `controle_ia.prereg.problemes` | liste vide |
| aucun identifiant de modèle ni de fournisseur | tenu (rôles C1, C2, E, X1, X2) ; seule trace : « famille Claude » en « Portée » (ligne 1103), nom de famille déjà signalé aux tours 1 et 2, remarque facultative inchangée |
| m-12 | la liste « complet, sans carte, tronqué, coupé, refusé » + échec : cinq non fautifs, échec en sixième, **juste** ; six endroits portés (L.5 W-13, D.12 deux, Métrique, Plan point 8, V-17) ; **trois endroits non portés, voir m-18** |
| m-13 | 52 000 + 29 395 / 0,2 ≈ 198 975 : « environ 199 000 » ; 200 000 à la borne exacte : **juste** ; l'attribution « lecteur du tour 1, refait au tour 2 » est vraie |
| m-14 | la phrase de la règle de n ne contredit plus celle de τ ; l'ancienne forme ne subsiste que dans la table de réponse (citation) |
| m-15 | D.3 dit désormais que le contrôle est fait par le lanceur hors machine ; **cohérent avec la garde 35 et avec la garde « machine sans jeton »** |
| m-16 | point 11 placé après le point 10, numérotation continue ; ligne de marqueur portée ; la ligne Q-4 … Q-8 de la table « Tranchées » dit « ligne ouverte » : **cohérent** |
| m-17 | les deux mesures nommées, avec renvois exacts (D.1 « Régularités », D.8 point 4, V-21) |
| conditions des lignes GO-2026-11-13-01 et -02 | relues : inchangées par ce brouillon ; plafonds, échéance 2026-11-30, conditions toutes exigées, banc, secret machine poussé avant la phrase de Lazar, devis revu après la v4 : portés par la pièce et ses préalables ; rien touché par les couples |
| GO-2026-11-17-05 (un seul banc complet, règle en dernier, dénominateur = tous les mondes tirés) | inchangé |
| R3 (aucun run visant un signe) ; R4 (symétrie, A0 à G = 24 comme à G < 12) ; R5 (liste d'arrêt testable) ; cohérence avec la conception v7 | aucune de ces sections n'est touchée, hors les énumérations d'états d'appel de m-12 |
| en-tête | « Le brouillon 5 est lui-même le brouillon 4 … corrigé de la même façon » : phrase longue mais exacte ; ordre des étapes : tours 1 et 2 faits, vérification courte à faire : exact |

## 3. Corrections exigées

Deux mineures. Chaque « ancien » figure **une seule fois** dans le brouillon 6 (compté par programme). Le fond est exigé ; la formule est libre si elle garde le sens.

**m-18. L'état « sans carte » (couple m-8, étendu par m-12) manque encore dans trois énumérations d'appels non fautifs.** Constat (1) du rédacteur du brouillon 6, retenu : le rapport du tour 2 ne les visait pas, mais le principe de m-12 est le même. Pour A6, l'omission pèse : un négatif causé par des appels sans carte serait lu sans que l'audit le demande. D.12 dit déjà « sans arrêt » pour cet état ; la liste d'arrêt doit le dire aussi.
- ancien : `**appels tronqués, coupés au plafond ou refusés, par proposeur et génération**`
- nouveau : `**appels tronqués, coupés au plafond, refusés ou sans carte, par proposeur et génération**`
- ancien : `appels tronqués, coupés ou refusés, comptés par fournisseur et`
- nouveau : `appels tronqués, coupés, refusés ou sans carte, comptés par fournisseur et`
- ancien : `**Appels tronqués, coupés au plafond, refusés** : jamais un arrêt (D.12).`
- nouveau : `**Appels tronqués, coupés au plafond, refusés, sans carte** : jamais un arrêt (D.12).`

**m-19. Les « Préalables », étape 1, décrivent une contre-lecture « de ce brouillon 4 » avec des corrections « portées dans un brouillon 5 », faites depuis (tours 1 et 2).** Constat (2) du rédacteur, retenu : dans la liste d'ordre qui commande le scellement, une phrase fausse sur l'état du texte ; le rédacteur la renvoie à la version finale, mais la version finale part de ce texte. Correction minimale, sans réécrire la liste de fichiers :
- ancien : `1. **Contre-lecture R2 de ce brouillon 4** par un lecteur neuf`
- nouveau : `1. **Contre-lecture R2 de ce brouillon** (tours 1 et 2 faits sur les brouillons 4 et 5 ; reste la vérification courte du brouillon 6) par un lecteur neuf`
- ancien : `portées dans un brouillon 5 (R12).`
- nouveau : `portées dans les brouillons 5 et 6 (R12).`

## 4. Remarques facultatives (aucune n'est exigée)

1. La remarque 4 du tour 2 (renvois au brouillon 3 à lister exhaustivement) reste bien inscrite à « À faire » pour la version finale ; rien à ajouter.
2. L'étiquette « progrès tardif » de la ligne V (FD ne prononce aucun progrès) : toujours une étiquette seulement.
3. Le nom de famille de modèles en « Portée » : à garder ou retirer selon la mère.
4. Le texte de la table de réponse est très long (une ligne par cellule) ; cela gêne la lecture, non le fond.

## 5. Ce que le rédacteur déclare, et ce qui tient

- « Rien d'autre ne change » : **confirmé** par le `diff` et par le rejeu du différentiel scellé.
- « Rédacteur : modèle A » alors que la consigne de sa tâche le nommait C : raison donnée (R-2982, R-2992), confirmation demandée à la mère ; je ne la donne pas. La réserve de lignée (même modèle que les rédacteurs des brouillons 4 et 5) est **levée pour cette vérification** : je suis C et je n'ai écrit aucune pièce.
- Sa déclaration d'incidents (lignes de registre affichées en passant) : rien de plus à relever.

## 6. Points pour la mère

1. **Verdict : corrections**, deux mineures (m-18, m-19), en couples exacts ; **aucune majeure**, pas de nouveau tour sur le fond. Comme pour les tours précédents, le même programme de couples les applique ; une vérification courte du différentiel brouillon 6 → brouillon 7 (deux ajouts, un par couple) suffira.
2. **Mots de Lazar nécessaires (inchangés)** : sous-choix de τ ; Q-4, Q-6 et l'étendue de Q-5 et de Q-8 (point 11) ; lecture d'E-2 (MR-2 ne satisfait pas la lettre de Q-13 (c)) ; tout relèvement d'un plafond de session ; second cycle du banc ; publication.
3. **À trancher par la mère** : lettre du rédacteur (A contre C) ; lecture de « code v68 gelé » (module neuf égal à la v4, ou import) avant tout secret ; taille des lois servies.
4. **Risque de fond, non corrigeable par la pièce** (inchangé) : troncatures de X1 et X2 à 2 USD, archive servie croissante aux générations 2 et 3, échéance du 2026-11-30 courte ; le devis de la course doit le chiffrer. Le code de la course et du banc reste à écrire, pas seulement à contre-lire.
5. **Le brouillon 6 ne peut toujours pas se sceller** avant le banc, le code, la règle de calibration lue et la levée des marqueurs.

## Déclaration

- **Rôle** : lecteur neuf, modèle C, sous-agent d'un script d'orchestration ; aucune autorité de décision ; aucune pièce modifiée.
- **Écrit** : ce rapport seul (scellé, compagnon `.sha256`) ; au bloc-notes, hors dépôt : un `diff` brut des deux brouillons, une copie du brouillon 5 pour rejouer le différentiel scellé.
- **Lu** : rapport du tour 2 ; brouillons 5 et 6 (différentiel en entier, passages touchés et alentours, D.12, Seuil, Points ouverts, Préalables, Marqueurs, Contre-lecture) ; lignes GO-2026-11-13-01 et -02 de `registres/go.md` ; programme des couples et différentiel scellé (empreintes seules et `patch` du différentiel) ; `controle_ia.prereg.problemes` par son appel.
- **Incidents de ma main** : (1) validateur et scellement sous l'interpréteur du venv avec `PYTHONPATH=src` : des `__pycache__` ignorés par git peuvent en naître ; (2) aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune dépense ; aucune branche `calcul/pilote-mr2-v74-entree-*` ; aucun secret ; aucun monde ; ni code du pilote ni verdict relus ; rien lu sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque ni du mode tenu à l'écart ; aucune valeur de clé, ni `env` ni `printenv` ; aucun `GIT_DIR`, `GIT_WORK_TREE` ni `GIT_INDEX_FILE` ; rien committé.
