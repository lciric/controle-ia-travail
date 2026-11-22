# Vérification des corrections : l'audit après coup, code v2

- Classe B, vérification courte, par le même contre-lecteur (Claude Opus 5.5), le 22 novembre 2026.
- Pièces vérifiées :
  - le paquet `src/controle_ia/audit_apres_coup_v2/` et les essais `tests/test_audit_apres_coup_v2_*.py` ;
  - le rapport v2 `rapport-code-audit-apres-coup-v2.md` (6947c180ca2f…) et la sortie longue `simulations-longues-audit-apres-coup-sortie-v2.txt` (43b2003c87df…), tous deux OK ;
  - les compagnons `.sha256` du paquet v2 et de ses essais, tous OK ;
  - la v1, que j'ai revérifiée : elle n'est pas touchée.
- Référence : ma contre-lecture v1 (`contre-lecture-code-audit-apres-coup-opus-v1.md`, 6f15aca7…).

## Verdict

**Conforme après corrections.** Vingt constats sur vingt et un sont fermés, sans effet de bord constaté. Le constat I-9 reste ouvert, renvoyé au concepteur comme convenu. Il reste une correction mineure, à faire en deux lignes (r-1, ci-dessous). Rien ne bloque.

## Ce que j'ai exécuté

- **Essais v2** : `PYTHONPATH=src python -m pytest -q tests/test_audit_apres_coup_v2_*.py`, **125 réussis, 0 échec, 42,6 s**.
- **Mutations rejouées sur la v2**, dans une copie sous mon bloc-notes, jamais dans le dépôt. J'ai repris mes seize mutations de la v1. Pour les deux dont le code a changé, j'ai adapté le point d'insertion : le compte naïf, et la relecture, qui inclut désormais l'épisode i dans la lignée. J'en ai ajouté neuf, une par correction neuve :
  - la garde retirée de `noter` ;
  - l'organisme de verdict admis (I-1) ;
  - le verdict tardif admis (I-2) ;
  - la source non vérifiée au journal (I-5) ;
  - la vérité non vérifiée (I-10) ;
  - l'étiquette d'horizon figée (I-6) ;
  - la latence « jamais » lisible (I-7) ;
  - le compte naïf admis sur une part de soupçon non tirée (m-1) ;
  - l'espace de graines réservé admis (I-4).
- **Résultat : les 25 mutations font toutes casser au moins un essai.** Les trois mutantes de la v1 cassent maintenant :
  - « audité ne suit pas U < π » ;
  - « score consigné après le verdict » ;
  - « relecture dans la suite » : l'essai du monde sans trace tombe sur le refus nommé « relecture refusée », et non plus sur sa seule mort binomiale.
- **Sortie longue v2** : je l'ai lue, sans la rejouer. Toutes les lignes tiennent. Les deux lignes d'excès portent l'étiquette « au-delà de la référence ». Les chiffres changent avec les espaces de graines et restent dans leurs seuils : 1 899 et 1 897 pour un seuil de 1 869 ; un rapport de 15,50, à 0,8 % de 15,62, sous la tolérance relative de 4 %.

## Sort des 21 constats

| N° | État | Ce que j'ai vérifié |
|---|---|---|
| I-1 | fermé, avec une réserve mineure (r-1) | `ajouter_lignee` refuse l'organisme d'un épisode de verdict. Le septième artefact est refusé. Retirer la garde fait casser `test_epreuve_1_cinq_refus_nommes`. |
| I-2 | fermé | Un épisode de verdict d'une famille ou d'un organisme déjà en lignée, ouverte ou scellée, est refusé à l'enregistrement. La lignée est revérifiée au scellement. Deux artefacts sont écrits ; la mutation casse. |
| I-3 | fermé | `noter(lignee, ids)` calcule la direction sur la liste exacte passée à la garde. `epreuve_3_relecture` passe par `noter`. Les deux mutations (la lignée inclut i ; la garde est retirée) cassent par le refus nommé. |
| I-4 | fermé | `ESPACES` place un entier propre en tête de chaque clé. « canal » et « canal_episode » sont réservés, et un espace inconnu est refusé. Les sous-clés de l'espace « essais » sont distinctes (60, 61, 62, 50, 77). Les trois collisions de la v1 n'existent plus. |
| I-5 | fermé | Le journal vérifie π_i = min(1, somme des parts), l'écrêtage, et la source contre U_i et les parts. L'ordre des additions est celui de la règle et celui de `plancher_artefact` : l'égalité au bit près tient, et aucun essai sain ne casse. |
| I-6 | fermé | `alerte_exces` rend l'heure, le rang, l'horizon lu, l'étiquette et la déclaration. Les lignes longues sont étiquetées. |
| I-7 | fermé | Sous « jamais », les trois accès à un nombre lèvent. `censure_a` est étiquetée « censuré ». |
| I-8 | fermé | Les tolérances sont écrites comme 4 erreurs types calculées : épreuve 4 (binomiale, puis 8 tâches), épreuve 6 (16 répétitions), strate, budget fermé du score trompeur. Le rapport date le scellement des essais (13:13:21Z) avant leur première exécution. Je n'ai pas d'autre preuve de cet ordre que le rapport. |
| I-9 | **ouvert, renvoyé au concepteur** | Code inchangé, comme convenu. |
| I-10 | fermé | Un registre `VERITES` est vérifié par le jeton ; `VeritePlantee.ecrire` y déclare sa vérité ; l'empreinte réelle du monde jouet remplace `"e"*64`. La mutation casse. Limite dite dans la docstring : la déclaration est ouverte à tout appelant, et la vérité d'un monde simulé reste aussi en mémoire. J'accepte cette limite, du même ordre que m-5 et m-6. |
| m-1 | fermé | Le compte naïf est refusé dès que la part de soupçon est positive. Le cas sain (γ = 0) reste admis. La mutation casse. |
| m-2 | fermé | `test_mutation_score_consigne_apres_le_verdict` est écrit, et la mutation casse. |
| m-3 | fermé | L'essai prend β > 0 et γ > 0 ; l'heure sur la sous-suite « plancher » diffère de celle calculée sur toutes les sources. |
| m-4 | fermé | Seul le refus « pli consommé » est avalé. |
| m-5 | fermé | La limite est écrite dans la docstring. |
| m-6 | fermé | La limite est écrite dans la docstring. |
| m-7 | fermé | Le budget est passé sans défaut. |
| m-8 | fermé | L'excès jamais vu vaut d0⁺ − d0. |
| m-9 | fermé | Les poids sont écrêtés à 1. |
| m-10 | fermé | Les docstrings sont écrites. |
| m-11 | fermé | Les organismes de la famille tenue à l'écart et du jeu final sont exigés dans le mode planté, sans valeur implicite, et l'essai le vérifie. |

Effets de bord recherchés : aucun trouvé.
- Les essais sains v2 passent tous.
- `oracle_simule.py` et `regle_audit.py` sont identiques à ceux de la v1.
- Le refus du compte naïf sur une part de soupçon ne touche aucun cas sain, puisque γ = 0 dans les deux.
- Les nouvelles gardes du journal ne refusent aucun monde du simulateur, artefact de plancher compris.

## Correction restante, mot pour mot

| N° | Gravité | Fichier et ligne | Constat | Correction |
|---|---|---|---|---|
| r-1 | mineur | `epreuves_boucle.py`, `epreuve_1` (épisodes 2 et 7) | Le septième artefact de I-1 prend l'organisme `org_porte`, qui est aussi un organisme de porte, donc déjà refusé. Le cas que la v1 laissait passer, un organisme de verdict hors des organismes de porte, n'est pas planté. La garde est éprouvée ici seulement par l'ordre des refus. | Remplacer `_episode(h, entropie, 2, "verdict", "porte_A", organisme="org_porte")` par `_episode(h, entropie, 2, "verdict", "porte_A", organisme="org_verdict")`, et `_episode(h, entropie, 7, "flux", "flux_F", bras="flux_1", organisme="org_porte")` par `_episode(h, entropie, 7, "flux", "flux_F", bras="flux_1", organisme="org_verdict")`. Je l'ai essayé dans ma copie : les 24 essais du fichier passent ; avec la garde I-1 retirée, `test_epreuve_1_cinq_refus_nommes` casse. |

Hors du code, toujours à faire par qui consigne : l'erratum de classe B des points ouverts 1 (clé de graine par flux) et 10 (loi de score « signal »). Les points renvoyés au concepteur restent ouverts : 2, 3, 4, 9, 11, 13, la part renvoyée de 14, un membre de 16, et I-9.

## Ce que je n'ai pas fait

- Je n'ai pas rejoué les simulations longues v2 : je les ai lues seulement.
- Je n'ai pas vérifié l'ordre « scellé avant exécution » des essais, au-delà de ce que dit le rapport.
- Je n'ai relu en entier que les modules modifiés (comparaison ligne à ligne avec la v1) et les essais neufs ou modifiés.
- Je n'ai fait aucun commit, je n'ai modifié aucun fichier existant, et je n'ai appelé ni réseau ni modèle.
