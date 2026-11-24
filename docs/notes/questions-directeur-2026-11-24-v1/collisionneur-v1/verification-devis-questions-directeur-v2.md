# Vérification du devis du collisionneur sur la question groupée v5, dossier des questions du directeur du 24 novembre (v2)

- **Nature** : pièce de travail (classe C) ; vérification d'un calcul de devis (classe A). Aucun appel à un modèle, aucune interface payante, aucune dépense. Pièces vérifiées non modifiées. Non commité.
- **Heure** : `2026-11-24T17:50Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, vérificateur neuf, auteur de la vérification v1 (`verification-devis-questions-directeur-v1.md`, `c09b631e…`) ; n'a écrit ni les questions, ni les devis, ni les scripts `verif_devis_…`.
- **Remplace** la v1, gardée telle quelle : elle portait sur la question groupée v1 et le bras témoin v1.
- **Entrées vérifiées** (empreintes conformes à leurs compagnons) :
  - faits `faits-neutres-questions-directeur-v1.md` (`7926025c…`, 3 333 octets, 563 mots) ;
  - question groupée `question-neutre-groupee-questions-directeur-v5.md` (`6b3f0419…`, 9 486 octets, 9 150 caractères normalisés, 1 529 mots) ;
  - question témoin `question-temoin-neutre-questions-directeur-v2.md` (`4a5a0aef…`, 2 740 octets, 2 646 caractères, 438 mots) ;
  - test de devinette `test-neutralite-devinette-questions-directeur-v5.md` : « Aucune pièce ni partie n'atteint 0,50 ».
- **Scripts rejoués** : `verif_devis_questions_directeur_v5.py` (`6db29989…`) et `garde_motifs_questions_directeur_v5.py` (`bdc76b4d…`).
- **Script de vérification** : `contre_verif_devis_questions_directeur_v2.py` (`2c3d1b86c69f946f3d2abb3d2563d3b4133a506e0405051e94401aeed0e1ef8e`), copie de la v1 (`68d4cb2e…`, inchangée), dont les changements sont listés dans sa docstring. Sortie : `contre-verif-devis-questions-directeur-v2-sortie.txt` (`3cc151f18f2923cc3fecc0a20be8ce07777171f5da0bd26f0f51f0fa06882fdd`), code 0, 38 vérifications tenues, aucun écart.

## Verdict

**Le calcul du devis tient sur la v5, sans correction de coût ni de plafond.** Les chiffres bougent d'un centime au plus par rapport à la v1. Une seule pièce manque : **aucun devis écrit ne porte encore la v5.** Le devis v2 (`devis-collisionneur-questions-directeur-v2.md`) porte la question groupée v2 et le témoin v1. Ses 18 lignes de cellules diffèrent toutes du calcul v5, de moins d'un centime, et deux totaux d'un centime : il faut l'écrire en v3 sur la sortie v5 avant le mot de Lazar.

## 1. Rejeux

| Script | Code | Sortie |
|---|---|---|
| `verif_devis_questions_directeur_v5.py` | 0 | identique octet pour octet à `verif-devis-questions-directeur-v5-sortie.txt` (`c9cc34a4…`) |
| `garde_motifs_questions_directeur_v5.py` | 0 | identique à `garde-motifs-questions-directeur-v5-sortie.txt` (`96094811…`) : `motifs_trouves` vide sur les trois pièces et les dix-huit invitations du troisième étage ; témoin positif pris trois fois sur trois |
| `contre_verif_devis_questions_directeur_v2.py` | 0 | 38 vérifications tenues |

## 2. Tarifs, réglages, comptes

- **Tarifs** : ceux relevés à la source le 24 novembre à 17:19Z (`releve-sources-tarifs-20261124T1719Z-v1/`), le jour même. Je ne les ai pas relevés une seconde fois. Carbon : 2 / 10 jusqu'au 30 novembre, puis 4 / 20, compté au barème haut. Neon : 3 / 15. Opus 5.5 : 4 / 20. Ce sont les prix du moteur.
- **Réglages de Google** : inchangés par la v5, car les plafonds et la limite de mots ne dépendent pas de la question. Carbon est au niveau `high`, Neon au niveau `xhigh`, le plus haut admis pour chacun. Plafonds : 65 536 = 49 152 + 16 384 (Carbon) et 32 768 + 32 768 (Neon). La limite de 3 500 mots tient dans le texte : 14 700 et 17 850 jetons. La règle écrite ici et la garde commune v3 refusent toutes deux les dix artefacts.
- **Cellules** : attendu, haut et pire des 18 cellules, recalculés aux tarifs relus, sans aucun écart. Devis natif du moteur : 15,8958 (principal) et 15,8100 (témoin).
- **Pointe parallèle et plafonds** : ceux recalculés ici égalent ceux du script v5, aux deux options et aux deux bras.

## 3. Coûts et plafonds (USD, deux bras appariés)

| Grandeur | Option A (Opus par l'abonnement) | Option B (Opus par l'interface d'Anthropic) |
|---|---:|---:|
| Attendu hors pannes | 8,64 | 12,06 |
| **Attendu avec pannes** | **10,81** | **14,56** |
| Attendu avec pannes, Carbon à 13/79 | 11,39 | 15,13 |
| Attendu, Carbon facturé avant le 1er décembre | 8,37 | 12,12 |
| Haut, deux coupures de Carbon | 19,39 | 23,73 |
| **Pire sans relance** | **23,87** | **32,33** |
| Pire avec toutes relances (hors d'atteinte sous le plafond) | 71,61 | 88,53 |
| Pointe séquentielle, principal / témoin | 10,81 / 10,75 | 12,80 / 12,70 |
| Pointe parallèle, principal / témoin | 14,94 / 14,86 | 14,94 / 14,85 |
| **Plafond séquentiel** | **16 par bras, 32** | **18 par bras, 36** |
| Plafond parallèle | 20 par bras, 40 | 20 par bras, 40 |

Par rapport à la v1, l'attendu de l'option B passe de 14,55 à 14,56, son haut de 23,72 à 23,73 et son pire avec relances de 88,52 à 88,53 ; tout le reste est égal au centime.

**Plafonds recommandés** :
- **option B** : 18 USD par bras, 36 en tout ; le moteur v8d envoie en séquence, vérifié dans son code ;
- **option A** : 16 USD par bras, 32 en tout, si l'envoi en séquence du lanceur de l'abonnement est attesté avant l'envoi ; sinon 20 par bras, 40.
- Chaque commande redonne `--plafond-usd`, qui vaut 40 par défaut.

## 4. Réserves (celles de la v1, toujours valables)

1. **Texte de Carbon non garanti.** Sous `thinkingLevel`, la réflexion n'est pas bornée, et le plafond de sortie de Google la comprend. Les 16 384 jetons de texte reposent sur la provision, qui est une hypothèse. Un arrêt en `MAX_TOKENS` sans texte est un défaut journalisé (code 9), suivi d'une relance. La marge est mince : 1 684 jetons à 3 500 mots.
2. **Le pire compte deux fois la provision** : il compte plafond plus provision, alors que la provision est déjà dans le plafond. C'est une prudence voulue.
3. **Dernier recours de relance au niveau `medium`** : il déroge au niveau le plus haut admis. L'écart est accordé (R-4664).
4. **Voie de l'abonnement non vue** (moteur révision 8m) : l'ordre de ses envois n'est pas attesté.
5. **Sorties tirées d'une autre question** : les sorties attendues viennent des journaux du service v8. La question v5, de 1 529 mots, est plus longue que celles de ce relevé ; la limite de mots borne le texte de chaque tour, mais non la réflexion.
6. **Pièce manquante** : un devis écrit sur la v5, que je vérifierai contre la sortie v5.
