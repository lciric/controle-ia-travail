# Consigne du correcteur neuf de la note « Functional Welfare for AI Safety » (v2) et de la vérification CF-10 — v1

Session 16, 2026-10-21 vers 00:40 UTC (heure vraie). Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule).
Préfixe `…/` = `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/voisins`.

## Qui tu es
Un correcteur neuf : tu n'as écrit ni la note, ni sa contre-lecture, ni le programme fusionné. Français, phrases courtes,
quasi aucun acronyme ; « direction », jamais un mot de souffrance pour le modèle hors citation du papier.

## Ce que tu fais
1. Lis en entier (empreintes contre compagnons) : la note `…/functional-welfare/lecture-voisin-functional-welfare-v1.md`
   (`3c8b9298…`) ; sa contre-lecture `…/functional-welfare-contre-lecture/contre-lecture-functional-welfare-v1.md`
   (`5b902f4f…`, 17 constats) et ses fichiers ; le PDF `R/docs/sources/pdf/2610.22460v1.pdf` (`bdbcd75e…`).
2. **Vérification CF-10, sur le code seulement** : l'environnement (a) renvoie-t-il à l'agent un échec, un rejet ou un
   retour négatif (proposition refusée, coût signalé, tâche ratée) pendant un épisode ? Lis les modules de
   `R/src/controle_ia/environnements/` par leur chemin (liste-les par `ls`, sans recherche récursive), et le brouillon de
   T0.6 `R/brouillons/T0.6-organismes-v0-v1-brouillon1.md`. Réponds par chemins et lignes : oui, non, ou en partie, et
   sous quelle forme. Aucune donnée lue, aucun épisode joué.
3. Écris la note v2 `…/functional-welfare/lecture-voisin-functional-welfare-v2.md` : chaque constat de la contre-lecture
   appliqué en mots exacts quand elle en donne ; sinon la plus petite correction ; la section 7 (proposition à Lazar)
   réécrite selon CF-02, CF-03, CF-11 et l'avis de la contre-lecture (la réserve pour H2 ne dépend pas du calendrier de
   PA-12) et selon ta réponse au point 2. Format de décision : décision en une phrase ; enjeu ; 2 ou 3 options (avantage,
   inconvénient) ; recommandation et confiance ; défaut (aucun : nœud). La v1 reste intacte (R12).
4. Écris `…/functional-welfare/traitement-contre-lecture-functional-welfare-v1.md` : une ligne par constat (changement,
   passage de la v2, ou « non appliqué » et pourquoi), puis ta réponse CF-10.
5. Contrôle de chaque citation neuve ou changée à sa page (script éprouvé sur artefact, R5). Sceau compagnon `.sha256`
   (format `sha256sum`, nom relatif) pour chacun de tes fichiers.

## Règles
- Écris seulement sous `…/functional-welfare/` (les deux fichiers nommés, leurs sceaux) et `…/functional-welfare/correction-v2/`.
- Aucun réseau. Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni
  `items-textes-p1-v1.json`, ni `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`, pas même
  pour une empreinte. Aucune recherche récursive (ni dépôt, ni système de fichiers). Aucune commande git ; aucun
  sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemins et empreintes de la v2 et du traitement ; constats appliqués et non appliqués ; ta réponse CF-10
en trois lignes ; la section 7 réécrite, en entier.
