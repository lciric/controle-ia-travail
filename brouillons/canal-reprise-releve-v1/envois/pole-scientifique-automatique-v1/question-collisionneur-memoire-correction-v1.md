# Question pour le collisionneur — mémoire et correction de génération en génération du pôle « scientifique automatique » — v1 (brouillon de conv-audit ; session-depot fige sa version)

Écrit par conv-audit le 26 octobre 2026. Mot de Lazar (dans la session de conv-audit, 19:10 heure de Paris) : « et bien
sûr que l'organisme ait une mémoire, qu'il puisse itérer les expériences nouvelles en se corrigeant de génération en
génération, demande au collisionneur comment faire pour concevoir ça ». Forme « arbitre », trois modèles, trois tours, une
tentative par cellule, un refus arrête le tour. Complète la question du « pôle scientifique automatique » (GO-2026-10-26-06)
sans la répéter.

## Question

« Un pôle de recherche automatique fonctionne par générations : des fiches d'hypothèses (prédiction signée et chiffrée,
nul, seuil qui peut échouer, sévérité attendue) sont gelées, testées chacune par un agent expérimentateur dans un bac à
sable, vérifiées par un agent d'une autre famille de modèles, sélectionnées par la sévérité du test survécu, puis les
survivantes sont recombinées sur un mode bisociatif ; des témoins à vérité connue mesurent la qualité du pôle à chaque
génération (pièces fournies). Nous voulons qu'il ait **une mémoire** et qu'il **se corrige de génération en génération**
— dans les hypothèses qu'il propose, dans les expériences qu'il conçoit, et dans son propre code.

1. **Que mémoriser** (au-delà de l'archive brute) et sous quelle forme : verdicts et causes d'élimination ; protocoles qui
   ont donné des tests sévères ; désaccords entre expérimentateur et vérificateur ; calibration de chaque source
   (sévérité annoncée contre issue) ; leçons de génération ; autre ? Pour chacun : à quoi il sert à la génération
   suivante, et ce qui se passe s'il est faux.
2. **Comment la mémoire corrige** : quelles règles (ou quels apprentissages) font qu'une génération exploite la mémoire
   sans s'y enfermer — éviter de retester l'éliminé, réutiliser les protocoles sévères, pondérer les sources calibrées —
   tout en gardant l'exploration (nouveauté, recombinaison de domaines éloignés) ? Quel équilibre exploitation /
   exploration, et comment le mesurer ?
3. **Correction de son propre code** : comment une modification que le pôle propose de lui-même devient une fiche testée
   comme les autres (sur les témoins, contre la version précédente), avec quel critère d'adoption, et quelles parties du
   système ne doivent **jamais** être réécrites par lui (bornes, gardes, évaluation scellée, mesure de qualité) ?
4. **Pathologies** au niveau de la méthode : mémoire empoisonnée par un verdict faux ; auto-confirmation (le pôle
   apprend à proposer ce qui survit facilement, pas ce qui est vrai et fort) ; dérive des témoins (le pôle reconnaît les
   témoins) ; effondrement de la diversité ; accumulation d'erreurs de calibration. Pour chacune : le signe qui la révèle
   et la parade.
5. **Comment prouver que la mémoire aide** : l'ablation minimale (pôle avec et sans mémoire, même budget) et les mesures
   (qualité sur témoins, survie des fiches nouvelles à des tests sévères, taux de redites, diversité), avec un seuil qui
   peut échouer.
6. **Ce que la littérature fait déjà** (mémoires d'agents, archives des algorithmes évolutionnaires à la MAP-Elites et
   « stepping stones », bibliothèques de compétences, réflexion entre épisodes) : ce qui se transpose et ce qui ne se
   transpose pas, en disant ce que vous savez et ce que vous ne savez pas. »

## Faits à servir

- La conception du pôle (`conception-pole-scientifique-v1.md`, `a4f94148…`).
- La génération 0 réelle (essais de la brique 1, `5b7011b1…`) : l'exemple d'une génération et de ses verdicts ; en
  particulier, la mémoire spectrale actuelle de l'organisme est aveugle à la similarité sur des textes réels (rappel du
  plus proche voisin 0,000, hasard 0,038) et le critère d'arrêt annoncé n'est pas dans le code — ce sont des faits sur
  la mémoire existante.
- Le code de la v6.2.1 (`memoire_isvd.py`, archive « Stepping Stones ») comme mémoire actuelle.
- Si elle est rendue avant le tour : la réponse du tour GO-2026-10-26-06 (pôle scientifique) — sinon rien.
