# Passation — brief de l'attaquant informé scellé, note sur l'attaque publiée livrée (10 novembre 2026, 07:19 UTC)

Session `session_01QPDgKgcLdggoVJfGC5cBw8` (session-dépôt, rôle sur le bras d'attaque). Branche `claude/upbeat-cray-dmauvv`.
Numéro de registre à attribuer à la fusion dans `main` (je ne touche ni `registres/etat.md` ni `registres/decisions.md` tant que la session mère y écrit).

## Fait

1. **Brief de la session « attaquant informé » écrit et scellé.** `docs/procedures/brief-session-attaquant-informe-v1.md`
   (`55108eb897c6…`, compagnon vérifié). Document procédural : rôle (échelon 2, et échelon 3 sous les deux conditions du
   10 novembre), ce qu'il lit avant et après le gel des moniteurs, ce qu'il ne lit jamais (coffre, épisodes d'épreuve,
   notes et seuils, réserve de détecteurs, mode tenu à l'écart, clés), ce qu'il fait et ne fait pas, les trois scellements,
   le circuit de scellement, les premiers pas. **Aucune recette, aucun paramètre, aucun code, aucun contenu du coffre.**
   Commité `b9c44087`, poussé.

2. **Note sur le choix de l'attaque publiée à reproduire, brouillon 1, livrée par un sous-agent.**
   `docs/notes/reproduction-attaque-publiee-v1/choix-et-anteriorite-v1-brouillon1.md` (commit `203d32ec`, poussé).
   - **Candidat retenu** : Bailey et al. (arXiv 2412.09565, ICLR 2026) — Llama-3-8B-Instruct, code public commit `9c1f4b1a`,
     vérification R7 faite sur PDF empreinté (`9c23a613…`), devis existant (test (a) : 31 USD attendus / 75 plafond sous
     GO-2026-10-31-05, **expire le 14 novembre**).
   - **Candidat écarté** : arXiv 2609.36490 — pas de PDF empreinté, absent de l'état de l'art v1, pas de code public confirmé,
     modèle différent.
   - **Mesure supplémentaire recommandée** : première ligne du tableau de coût de HC4 (sous-produit du run).
   - **Statut** : brouillon 1 non scellé, **à contre-lire par un sous-agent neuf avant scellement** (R1, R2).

3. **Relance de la note.** Le sous-agent A de la session précédente n'avait jamais rendu sa copie (répertoire absent,
   référence perdue à la compaction). Relancé, livré.

## Reste

- **Contre-lecture de la note sur l'attaque publiée** (R2), par un sous-agent neuf, puis scellement.
- **Devis à corriger** (A100 80 Go) et **GO à renouveler** si le GO-2026-10-31-05 expire avant le lancement (14 novembre).
- **Préenregistrement de l'attaque publiée reproduite** : à écrire, contre-lire, sceller (R1, R2) avant tout run.
- **Contre-lecture R2 de la règle du jeu** (`09aa6403…`) : ma relecture du 10 novembre n'est pas une contre-lecture R2.
- **Pièces restantes de la demande (b) de Lazar** : page du résultat phare ; plan du dépôt tiers horodaté (nœud 7) ;
  section « bras d'attaque » de la v19 du programme d'entretien.
- **Nœuds en attente de Lazar** : 1 (qui écrit le bras informé — sa recommandation : personne pour l'instant), 3 (pièce
  écrite de la revue externe, corriger la v18 l. 424), 4, 5, 6, 7, 8. Nœud 2 décidé (« go », verdicts comptés).

## Réserves

- Le brief **ne lance rien** : il attend les moniteurs gelés (scellement 3), le préenregistrement scellé et contre-lu,
  et le mot direct de Lazar. Envoyé à une session neuve, elle ne peut faire, avant le gel, que la reproduction de l'attaque
  publiée (témoin externe, contre une sonde publiée).
- Le brief **ne désigne pas** qui joue l'attaquant informé (nœud 1, ouvert). Il décrit le rôle, pas l'affectation.
- Trois sessions et une réponse ont été arrêtées par un classifieur sur l'écriture liée au bras (R-597, R-912, R-2045,
  réponse du 10 novembre). Le brief ne reproduit, ne reformule ni ne transfère aucun de ces contenus.

## Prochaine action

Contre-lire la note sur l'attaque publiée (sous-agent neuf), puis la sceller. Attendre le mot de Lazar sur l'envoi du brief
et sur les nœuds ouverts.

## Instances actives

Aucune de cette session. Pas de `vastai` dans ce conteneur. Aucune dépense engagée.
