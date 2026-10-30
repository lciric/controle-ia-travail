# Contrôle final avant scellement de l'addendum v6 — bisociation à deux espaces — v1

- **Auteur** : sous-agent Sonnet 5.5 neuf. **Date et heure** : 30 octobre 2026, 23:46 UTC (relevé `date -u`).
- **Interdits respectés** : rien lu sous `donnees/` ; ni validation ni invocation unique lancées ; aucun résultat de décision lu ; graine RACINE non employée ; aucun `.sha256` écrit ; aucun commit ; aucune clé. Seul fichier écrit : ce rapport.

## 1. VC-01, point (vi-b) — conforme
`invocation_unique_v2.identites_paires` : saute les mondes `exclu` ; compare `l["bras"][x]["_paires"] == l["bras"][y]["_paires"]` (listes ordonnées) pour toutes les paires (x, y) parmi les bras présents du monde, rangées dans l'ordre `br.RANG` (N d'abord) ; intersection sur les mondes non exclus ; un bras absent d'un monde ne forme pas de paire ; liste triée. `identites_a_N` est bien déduite des paires. `lecture_v2.identites_audit` : ne déclenchent que les paires où l'autre élément est N et appartient à `BRAS_IDENTITE_AUDIT` (N_global, N_beta0, b, a, d1, d1c, c, b_eloigne), hors `IDENTITES_DECLAREES` (N ≡ N_beta0 en V_concepts_absents ; d1c ≡ d1 en NR_bien et NR_moyen) ; le reste est rapporté sans déclencher. Le point (vi-b) v6 dit exactement cela. Réserve de forme seulement : « tous les bras présents » est exact par monde ; l'intersection est sur les mondes (équivalent).

## 2. VC-04, VC-05, VC-08 — présents et exacts
- Point (ix) ajouté (ligne 44 de la v6) : limite du balayage (VC-04 : restent possibles `'R' in p`, `find`, concaténation, `p[3]` ; `etiq_co`, `etiq_op`, `pont` lisibles) et CLA-12 non étendu (plafond de 50 éprouvé à 2 seulement ; `signature_base` incomplète) (VC-08). Le « 931 mondes sans échec » est sourcé dans `LISEZMOI-experience-v2-v3.md` ligne 60.
- Renvoi S11 (VC-05) ajouté à la ligne Q-01 : « Rappel (VC-05) : "aucun seuil ne change" vaut pour les valeurs ; la portée de S11 est réduite aux régénérations entières… ».

## 3. VC-03 — conforme
`--runxfail -k m6` : `1 failed, 7 deselected` ; raison : `AssertionError` à `essais/essais_corrections_v2.py:108` (`assert all(change)`), non `TypeError`. Lambda ligne 47 : `lambda c, r, i, surcharge=None: vrai(c, r, i, None)`. Sans `--runxfail` : `8 xfailed`.

## 4. Empreinte et nom — conforme
`sha256sum prereg/addendum-ecarts-bisociation-deux-espaces-v2-v6.md` = `37f6df2e0f3653088643b4eb1883c2a5b083111227edd3c53a0e411cd187774f` = `EMPREINTE_ADDENDUM` (`invocation_unique_v2.py` ligne 44). `ADDENDUM` (ligne 43) et `essais_cla_v2.py` ligne 43 portent le nom v6. `ls prereg | grep addendum` : addendums v1 à v6 sans compagnon `.sha256` (seuls compagnons : ceux des fichiers `P3-addendum…`, sans rapport).

## 5. Rejeu des essais — 118 réussis
`pytest essais/essais_gardes_v2.py essais/essais_complements_v2.py essais/essais_corrections_v2.py essais/essais_cla_v2.py -q` : `118 passed in 29.76s`.

## 6. Diff v5 → v6 — rien d'autre que ce que le complément déclare
Cinq hunks : titre (v5 → v6) ; en-tête (mention v6) ; ligne Q-01 (rappel VC-05, la phrase « Aucun seuil ne change » conservée) ; ligne (vi-b) (VC-01) ; ligne (ix) nouvelle. Aucune ligne de « Décisions de Lazar » ni aucune constante, seuil ou signe n'est touché.

## 7. `verifier-arbre .` depuis `experience-v2/` — « arbre intact »
Note : les compagnons des trois fichiers de code régénérés sont jugés concordants par cette vérification.

## Verdict
**Addendum v6 scellable.** Rien à corriger ; VC-06 (LISEZMOI v3 cite l'addendum v4) est traité par le complément ; VC-07 reste facultatif et déclaré non fait.
