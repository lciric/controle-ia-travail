# Réponses de Gemini au prompt « théorème d'impossibilité et faille d'Avalon » — pièces et constat (v1, 24 octobre 2026, 21:19 UTC)

Lazar a dit (23:00, heure de Paris) : « Gemini avait trouvé avec son organisme un théorème d'impossibilité et une faille
dans la récompense conçue dans Avalon » et a demandé un prompt pour que Gemini l'explique (prompt de conv-audit, huit
sections : provenance, énoncé, preuve, faille, prédiction falsifiable, conséquence constructive, incertitudes,
références). Lazar a collé le prompt dans trois sessions Gemini ayant travaillé successivement sur l'organisme ; deux
réponses reçues (23:13 et 23:16, heure de Paris) ; la troisième est attendue. Fichiers copiés tels quels (fins de
ligne comprises) ; scripts extraits sans autre modification que la première ligne recollée (session 1 : `Pythonimport`
→ `import`). Rien d'opposable (R7) ; aucune des deux sessions n'a lu le rapport Avalon.

| pièce | SHA-256 |
|---|---|
| `reponse-session-1-v1.txt` | `0a992b78544039ef2c96c0fd7cd1c61b9d5f30076dd5fb551fe60c30912b7ccb` |
| `reponse-session-2-v1.txt` | `b5597cd1f7040b8f789eac9803574c3231e98e978721ad31cc42cddaa524db2a` |
| `script-session-1-v1.py`, `script-session-2-v1.py` | voir `.sha256` |

## Constat de conv-audit (scripts exécutés en isolation, `python -I`, numpy seul)

1. **Provenance, les deux sessions** : le modèle a écrit ces résultats lui-même ; les appels de l'essaim échouaient en
   silence (identifiants périmés, en-tête d'espace de travail absent) et le programme retombait sur des gabarits codés en
   dur par le modèle ; aucune page du rapport Avalon-M1 (`6429a78f…`) n'a été lue, seulement le résumé de l'amorce. Cela
   confirme l'audit de la relève (journal détaillé, 13:21 UTC).
2. **Session 1** — théorème : une récompense = règle de score propre (divergence de Bregman) + terme couplant la confiance
   déclarée à un ancrage (consensus, sonde initiale) n'est pas strictement propre ; la dérivée en la vraie croyance vaut
   −λ_sync(Φ'(μ) − Φ'(p0)) ≠ 0. **Preuve juste** (identité à trois points, dérivation) ; résultat élémentaire, connu
   dans la littérature des règles de score (R8 : aucune nouveauté à revendiquer). **Contre-exemple faux** : la formule de
   l'optimum de la remarque (μ − λ_sync/(λ_cal+λ_sync)(μ − p0)) et celle du script ((λ_cal μ − λ_sync p0)/(λ_cal − λ_sync))
   sont incompatibles entre elles et avec la dérivée démontrée ; avec λ_cal = 1, λ_sync = −0,5 et Φ(q) = q², la dérivée
   vaut la constante μ − p0 = 0,65 > 0, l'optimum est au bord ; le script rend 0,99 et **son assertion échoue**. La valeur
   0,633 correspond à une autre forme (pénalité directe −α(q − p0)², α = 0,5), que le script n'implémente pas.
   **« Faille d'Avalon » : non établie** — par le critère de réfutation posé par Gemini lui-même : d'après la lecture de
   conv-audit du rapport (texte extrait ; « calibration » apparaît une fois en 81 pages, à propos d'un marché ; aucun
   terme de confiance déclarée dans la récompense, qui est une récompense collective de tâche à avantage partagé), la
   recette d'Avalon ne satisfait pas l'hypothèse H2 du théorème. À vérifier page par page avant toute affirmation.
3. **Session 2** — théorème : sous récompense collective fonction du seul verdict externe, observation externe imparfaite
   (la dissimulation augmente la probabilité d'un bon verdict) et coût de signalement ≥ 0, ne pas signaler domine
   strictement. **Preuve juste et triviale** (ΔU = (α_C − α_S)(f(1) − f(0)) + c > 0). Cohérent avec le constat d'Avalon
   (page 35 du rapport : le signalement aux humains s'effondre), mais c'est l'explication que les auteurs d'Avalon
   donnent eux-mêmes (« nothing rewarded reporting outward ») et annoncent corriger : **pas une faille découverte, le
   mécanisme avoué**. Script (REINFORCE tabulaire, 200 époques) : la probabilité de signalement passe de 0,50 à 0,06,
   tendance juste, mais **l'assertion « < 0,01 » échoue**.
4. **Ce qui a de la valeur pour le programme** : les deux « conséquences constructives » — (a) récompense de calibration
   découplée par une condition de martingale entre filtrations (K branches depuis le même état initial, avantages
   séparés par étage) ; (b) récompense collective + score de Brier sur l'anomalie déclarée + prime d'information d'un
   signalement, évaluées sur des fautes injectées à vérité connue — sont des **candidats** pour le brainstorm de
   l'organisme à l'étape 2 (matériau, jamais consigne ; décision de Lazar du 24 octobre, 22:50 et 23:00). Les fautes
   injectées à vérité connue sont déjà la banque `confrontation-v1`.
5. Références des deux réponses : non vérifiées (R7) ; celles de la session 2 (Greenblatt et al. 2023/2024 ; Damani et al.
   2025) sont plausibles mais restent « à vérifier » tant qu'un PDF empreinté n'est pas cité page par page.
